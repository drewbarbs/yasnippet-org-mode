# -*- mode: snippet -*-
# name: ipython block
# key: py
# --
#+BEGIN_SRC ipython :session ${1::file ${2:$$(let (file-relative-name ((temporary-file-directory "./")) (make-temp-file "py" nil ".png")))} }:exports ${3:both}
$0
#+END_SRC