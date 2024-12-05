clean:
	find . -depth 1 -type d -name "__pycache__" -exec rm -rf {} \;
	find . -depth 1 -name output -delete

test:
	pytest

run:
	python day_5.py | tee output

start:
	curl https://adventofcode.com/2024/day/5/input -H "Cookie: session=${AOC_SESSION}" > input

