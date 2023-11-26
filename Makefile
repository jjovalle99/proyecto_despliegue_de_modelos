black:
	black ./app/*
	black ./tests/*
	black ./src/*

isort:
	isort ./app/*
	isort ./tests/*
	isort ./src/*


pycache:
	find ./ -type d -name '__pycache__' -exec rm -rf {} +
	find ./ -type d -name '.pytest_cache' -exec rm -rf {} +
