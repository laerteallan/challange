clean:
	@echo "Execute cleaning ..."
	rm -f *.pyc
	rm -f coverage.xml

pep8:
	@find . -type f -not -name "*manager.py*" -not -path "*./.venv/*" -name "*.py"|xargs flake8 --max-line-length=130 --ignore=E402 --max-complexity=6


tests: clean pep8
	py.test tests --cov=challenge 

tests-unit: clean pep8 
	py.test --cov=challenge tests/unit

tests-integrations: clean
	py.test tests/integrations

tests-with-coverage: clean pep8
	py.test --cov=challenge --cov-report=xml tests/unit

sonar: tests-with-coverage
	sonar-scanner
