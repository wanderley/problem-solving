;;; Directory Local Variables
;;; For more information see (info "(emacs) Directory Variables")

((nil . ((eval . (setq-local
                  org-roam-directory (expand-file-name (locate-dominating-file
                                                        default-directory ".dir-locals.el"))))
         (eval . (setq-local
                  org-roam-db-location (expand-file-name "org-roam.db"
                                                         org-roam-directory)))
         (eval . (setq-local
                  compile-command (format "cd .. && NOTE=%s make iterate-site" (buffer-name))))))
 (magit-mode
  (mode . adaptive-wrap-prefix)
  (mode . visual-fill-column)
  (mode . visual-line))
 (org-mode
  (mode . olivetti)
  (mode . adaptive-wrap-prefix)))
