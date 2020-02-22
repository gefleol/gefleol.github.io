python ../src/validate.py
python ../src/create_org_doc.py
emacs ../pub/provningar_main.org --batch -f org-latex-export-to-pdf --kill
emacs ../pub/provningar_main.org --batch -f org-html-export-to-html --kil
emacs ../pub/provningar_en_fil.org --batch -f org-html-export-to-html --kill
