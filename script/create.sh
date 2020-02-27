python ../src/uuid_prepender.py
python ../src/validate.py
python ../src/create_org_doc.py
emacs ../pub/provningar_main.org --batch -f org-html-export-to-html --kil
echo "provningar_main: org->html"
emacs ../pub/provningar_en_fil.org --batch -f org-html-export-to-html --kill
echo "provningar_en_fil: org->html"
emacs ../pub/provningar_main.org --batch -f org-latex-export-to-pdf --kill
echo "provningar_main: org->latex->pdf"
