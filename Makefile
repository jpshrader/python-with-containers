run:
	python main.py

test:
	python -m unittest

lint:
	pylint main.py

install:
	pip3 install -r requirements.txt