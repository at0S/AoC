clean:
	find . -prune -type d -name "__pycache__" -delete;
	find . -name output -delete

test:
	pytest

run:
	python day_5.py | tee output

start:
	curl https://adventofcode.com/2024/day/5/input -H "Cookie: session=${AOC_SESSION}" > input

PHONY: test
