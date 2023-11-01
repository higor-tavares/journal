run:
	python3 app.py

install:
	pip3 install -r requirements.txt

freeze:
	pip3 freeze > requirements.txt

configure:
	python3 -m venv .venv
	. ./.venv/bin/activate