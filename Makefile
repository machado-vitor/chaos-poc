.PHONY: venv install run report clean

venv:
	python -m venv .venv

install:
	pip install -r requirements.txt

run:
	SERVICE_URL=$$(minikube service podinfo -n chaos-poc --url | head -n1) PYTHONPATH=$(PWD) chaos run experiment.json

report:
	SERVICE_URL=$$(minikube service podinfo -n chaos-poc --url | head -n1) PYTHONPATH=$(PWD) chaos report --export-format=pdf chaos-report.json report.pdf

clean:
	rm -f chaos.log report.html
