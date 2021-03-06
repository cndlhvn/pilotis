# -*- encoding:utf-8 -*-

execfile("../config.py")
execfile("../method.py")

@task
def js_setting():
  """[1]javascriptのインデントとタブの設定"""
  if not contains(EMACS_FILE,";;;js_conf"):
    js_conf="""
;;;js_conf
(add-hook 'js-mode-hook
          '(lambda()
             (setq-default indent-tabs-mode nil)
             (setq js-indent-level 2)
             ))"""
    file_appendln(EMACS_FILE,js_conf) 
