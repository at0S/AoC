clean:
	find . -depth 1 -type d -name "__pycache__" -exec rm -rf {} \;
	find . -depth 1 -name output -delete

test:
	pytest

run:
	python day_2.py | tee output
