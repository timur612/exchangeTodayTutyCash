clean:
	-find -type d -name __pycache__ -exec rm -rf {} +	
	-find -type d -name .pytest_cache -exec rm -rf {} +
	-rm .coverage

pep8:
	@echo "Cheking pycodestyle"
	@flake8 --config=pyflake.cfg

test:
	python -m pytest --cov=. tests/