;;; build.el --- Script for publishing notes -*- lexical-binding: t; coding:utf-8; fill-column: 102 -*-

;; Authors: Wanderley Guimaraes da Silva <wanderley.guimaraes@gmail.com>

;;; Commentary:
;;
;; This script publishes the notes using Emacs.  The following command publishes
;; the notes from the folder `/notes' to `/out'.
;;
;;     > emacs --batch -l build.el --kill
;;
;; It was inspired by
;; - https://org-roam.discourse.group/t/export-backlinks-on-org-export/1756/25?page=2
;; - https://www.badykov.com/emacs/generating-site-from-org-mode-files/
;;
;; Here is a list of resources that can help improving the HTML site:
;; - https://juanjose.garciaripoll.com/blog/org-mode-html-templates/index.html

;;; Setup straight.el

(defvar bootstrap-version)
(let ((bootstrap-file
       (expand-file-name "straight/repos/straight.el/bootstrap.el" user-emacs-directory))
      (bootstrap-version 6))
  (unless (file-exists-p bootstrap-file)
    (with-current-buffer
        (url-retrieve-synchronously
         "https://raw.githubusercontent.com/radian-software/straight.el/develop/install.el"
         'silent 'inhibit-cookies)
      (goto-char (point-max))
      (eval-print-last-sexp)))
  (load bootstrap-file nil 'nomessage))
(straight-use-package 'use-package)
(setq straight-use-package-by-default t)


;;; Install dependencies

(use-package org-contrib :straight t)
(use-package org :straight t)
(use-package org-roam :straight t)
(use-package htmlize :straight t)


;;; Load dependencies

(require 'ox-publish)
(require 'org-roam)


;;; Setup

(setq

 ;; Org-roam
 org-roam-directory (expand-file-name "./notes")
 org-roam-db-location (expand-file-name "./notes/org-roam.db")

 ;; Org
 org-id-locations-file ".orgids"
 org-id-link-to-org-use-id t
 org-id-extra-files (org-roam-list-files)
 org-id-track-globally t

 ;; Org-publish
 org-export-with-broken-links 'mark
 org-html-validation-link nil
 org-html-home/up-format "<!-- %s --><nav><a href=\"%s\">Problem Solving</a></nav>"
 org-html-link-home "index.html"
 org-html-head-include-scripts nil
 org-html-head-include-default-style nil
 org-html-head  "<link rel=\"stylesheet\" href=\"style.css\">"

 static-directory "static"
 publish-directory "out")

(setq org-publish-project-alist
      (list
       (list "org-site:static"
             :base-directory static-directory
             :base-extension "css\\|js\\|png\\|jpg\\|gif\\|pdf\\|mp3\\|ogg\\|swf"
             :recursive t
             :publishing-directory publish-directory
             :publishing-function 'org-publish-attachment)
       (list "org-site:main"
             :recursive t
             :exclude ".*gitignore|.*/private/.*" ;; remove private directory
             :base-directory org-roam-directory
             :base-extension "org"
             :publishing-function 'org-html-publish-to-html
             :publishing-directory publish-directory
             :with-date t
             :with-author nil           ;; Don't include author name
             :with-creator nil          ;; Don't include Emacs and Org versions in footer
             :with-toc nil              ;; Don't include a table of contents
             :section-numbers nil       ;; Don't include section numbers
             :time-stamp-file nil       ;; Don't include timestamp in footer
             )
       ))


;;; Extension to  Org-publish

(defun wander/org-roam-collect-backlinks-string ()
  (when (org-roam-node-at-point)
    (let* ((node (org-roam-node-at-point))
           (filename (org-roam-node-file node))
           (backlinks (-distinct (--map (org-roam-backlink-source-node it)
                                        (org-roam-backlinks-get node))))
           (count (length backlinks))
           (content (when (> count 0)
                      (concat (format "\n\n* Cited by %d\n\n" count)
                              (mapconcat (lambda (node)
                                           (format "- [[id:%s][%s]]\n"
                                                   (org-roam-node-id node)
                                                   (org-roam-node-title node)))
                                         backlinks)
                              "\n\n"))))
      content)))

(defun wander/org-roam-insert-backlinks-string (backend)
  (save-excursion
    (goto-char (point-min))
    (when (org-roam-node-at-point)
      (goto-char (point-max))
      (insert (or (wander/org-roam-collect-backlinks-string) "")))))

(add-hook 'org-export-before-processing-hook 'wander/org-roam-insert-backlinks-string)


;;; Publish

(org-publish-all t)
