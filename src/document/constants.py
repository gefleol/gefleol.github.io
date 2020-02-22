# -*- coding: utf-8 -*-

header="""
#+LATEX_COMPILER: pdflatex
#+OPTIONS: ':nil *:t -:t ::t <:t H:5 \\n:nil _:nil ^:nil arch:headline author:t
#+OPTIONS: broken-links:nil c:nil creator:nil d:(not "LOGBOOK") date:t e:t
#+OPTIONS: email:nil f:t inline:t num:t p:nil pri:nil prop:nil stat:t tags:t
#+OPTIONS: tasks:t tex:t timestamp:t title:t toc:nil todo:t |:t
#+TITLE: Drycker och provningar.
#+SUBTITLE: Gefle Ölsellskap
#+DATE: <{{{time(%F %b %T)}}}>
#+AUTHOR: Johan Sandén
#+EMAIL: info@gefleolsellskap.com
#+LANGUAGE: sv
#+SELECT_TAGS: export
#+EXCLUDE_TAGS: noexport
#+CREATOR: Emacs 26.3 (Org mode 9.1.9)
#+HTML_HEAD: <link rel="stylesheet" type="text/css" href="css/org.css"/>

* Information
#+BEGIN_CENTER
#+ATTR_LATEX: :width 3cm
[[file:./images/logo_trans_small.png]]
#+END_CENTER

Det här är en förteckning över (alla) Gefle Ölsellskaps öl-provningar.
Dokumentet genereras utifrån en databas som ständigt utökas av medlemmarna vart
efter vi provar fler öl. Informationen i databasen kommer att förändras och
förbättras med tiden. Om du som läser detta hittar ni några fel så skicka ett
mail till {{{email}}}

Den här informationen finns också som
 - [[file:provningar_main.org][Interaktiv websida]]
 - [[file:provningar_en_fil.org][Normal websida]] 
 - [[file:provningar_main.pdf][Laddas ner som pdf]]

"""
js_line="#+INFOJS_OPT: view:info toc:nil path:./js/org-info.js"
js_header="{js_line}\n{header}".format(js_line=js_line, header=header)
