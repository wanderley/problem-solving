;;; build.el --- Script for publishing notes -*- lexical-binding: t; coding:utf-8; fill-column: 102 -*-

;; Authors: Wanderley Guimaraes da Silva <wanderley.guimaraes@gmail.com>

;;; Commentary:
;;
;; This file contains the API to build the notes.  Use `make' to build the notes:
;;
;;     > make site
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


;;; Early setup

(setq make-backup-files nil
      debug-on-error t)


;;; Install dependencies

(use-package org-contrib :straight t)
(use-package org :straight t)
(use-package org-roam :straight t)
(use-package htmlize :straight t)


;;; Load dependencies

(require 'ox-publish)
(require 'org-roam)


;;; Setup

(defun wander/setup-org-roam (&optional DB-SYNC)
  "Setup org-roam directory and database location."
  (setq org-roam-directory (expand-file-name "./notes")
        org-roam-db-location (expand-file-name "./notes/org-roam.db"))
  (org-roam-db-sync DB-SYNC))

(defun wander/setup-site (&optional DB-SYNC)
  (wander/setup-org-roam DB-SYNC)
  (setq org-id-locations-file ".orgids"
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

        static-directory (expand-file-name "./static")
        publish-directory (expand-file-name "./out")

        org-publish-project-alist
        (list
         (list "org-site:static"
               :base-directory static-directory
               :base-extension "css\\|js\\|png\\|jpg\\|gif\\|svg\\|pdf\\|mp3\\|ogg\\|swf"
               :recursive t
               :publishing-directory publish-directory
               :publishing-function 'org-publish-attachment)
         (list "org-site:main"
               :recursive t
               :exclude ".*gitignore|.*/private/.*"
               :base-directory org-roam-directory
               :base-extension "org"
               :publishing-function 'org-html-publish-to-html
               :publishing-directory publish-directory
               :with-date t
               :with-author nil
               :with-creator nil
               :with-toc nil
               :section-numbers nil
               :time-stamp-file nil)))
  (add-hook 'org-export-before-processing-hook 'wander/org-roam-insert-html-backlinks-string))


;;; Helper Functions

(defun wander/org-roam-collect-html-backlinks-string ()
  (when (org-roam-node-at-point)
    (let* ((node (org-roam-node-at-point))
           (filename (org-roam-node-file node))
           (backlinks (-distinct (--map (org-roam-backlink-source-node it)
                                        (org-roam-backlinks-get node))))
           (count (length backlinks))
           (content (when (> count 0)
                      (concat (format "\n\n* Cited by %d\n\n" count)
                              (mapconcat (lambda (node)
                                           (format "- [[id:%s][%s]]"
                                                   (org-roam-node-id node)
                                                   (org-roam-node-title node)))
                                         backlinks
                                         "\n")
                              "\n\n"))))
      content)))

(defun wander/org-roam-insert-html-backlinks-string (backend)
  (save-excursion
    (goto-char (point-min))
    (when (org-roam-node-at-point)
      (goto-char (point-max))
      (insert (or (wander/org-roam-collect-html-backlinks-string) "")))))


;;; Build API

(defun wander/publish-site ()
  (message "Publish site ...")
  (wander/setup-site t)
  (org-publish-all t)
  (message "Publish site DONE"))

(defun wander/iterate-site ()
  (message "Iterate on site using specific note ...")
  (wander/setup-site)
  (org-publish "org-site:static")
  (find-file (expand-file-name (or (getenv "NOTE") "./notes/interview_preparation_v.org")))
  (org-publish-current-file t))
