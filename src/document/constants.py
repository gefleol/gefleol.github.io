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

Den här websidan finns som
 - [[file:provningar_main.org][Interaktiv websida]]
 - [[file:provningar_en_fil.org][Normal websida]] 
 - [[file:provningar_main.pdf][Laddas ner som pdf]]

En delmängd går även att [[file:csv_file.csv][ladda ner som CSV-fil]] som går att öppna i ett kalkylprogram som Excel
eller det total överlägsna [[https://www.libreoffice.org/][LibreOffice]] 

#+INCLUDE: ../data/meta/typer.org
#+LaTeX: \pagebreak
"""
js_line="#+INFOJS_OPT: view:info toc:nil path:./js/org-info.js"

js_header="{js_line}\n{header}".format(js_line=js_line, header=header)

type_constants={0:"Unknown/Other",
                1:"Altbier",
                2:"Amber ale",
                3:"Barley wine",
                4:"Berliner Weisse",
                5:"Bière de Garde",
                6:"Bitter",
                7:"Blonde Ale",
                8:"Bock",
                9:"Brown ale",
                10:"California Common/Steam Beer",
                11:"Cream Ale",
                12:"Doppelbock",
                13:"Dortmunder Export",
                14:"Dunkel",
                15:"Dunkelweizen",
                16:"Eisbock",
                17:"Flanders red ale",
                18:"Golden/Summer ale",
                19:"Gose",
                20:"Gueuze",
                21:"Hefeweizen",
                22:"Helles",
                23:"India pale ale",
                24:"Kölsch",
                25:"Lambic",
                26:"Lightale",
                27:"Maibock/Helles bock",
                28:"Malt liquor",
                29:"Mild",
                30:"Oktoberfestbier/Märzenbier",
                31:"Oldale",
                32:"Oud bruin",
                33:"Pale ale",
                34:"Pilsener/Pilsner/Pils",
                35:"Porter",
                36:"Redale",
                37:"Roggenbier",
                38:"Saison",
                39:"Schwarzbier",
                40:"Scotch ale",
                41:"Stout",
                42:"Vienna lager",
                43:"Weissbier",
                44:"Weizenbock",
                45:"Witbier",
                46:"Fruit beer",
                47:"Herb and spiced beer",
                48:"Honey beer",
                49:"Rye Beer",
                50:"Smoked beer",
                51:"Vegetable beer",
                52:"Wild beer",
                53:"Wood-aged beer"}
