.PHONY: venv install run report clean

venv:
	python -m venv .venv

install:
	pip install -r requirements.txt

run:
	chaos run experiment.json -v

report:
	chaos report experiment.json ./chaos.log --export-format=html --output=report.html || true

clean:
	rm -f chaos.log report.html
