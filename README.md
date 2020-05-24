git remote add origin https://github.com/kallul/flasktruescrape.git
git push -u origin master


pip freeze > requirements.txt

git add .
git commit -m "Added requirements.txt"
git push origin master

Click on “$ bash” button dashboard on pythonanywhere
git clone https://github.com/kallul/flasktruescrape.git


mkvirtualenv --python==python3.8 scrape_venv
workon scrape_venv
pip3.8 install --user -r requirements.txt
git checkout app.py