all:
	install
	lint
	test
    
env:
	source .venv/bin/activate

install:
	pip install --upgrade pip 
	pip install -r requirements.txt

lint:
	pylint --disable=R,C main.py

freeze:
	pip freeze > requirements.txt

