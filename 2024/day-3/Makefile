clean:
	find . -depth 1 -type d -name "__pycache__" -exec rm -rf {} +
	find . -name output -delete

test:
	pytest

run:
	python day_3.py | tee output
