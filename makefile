clean:
	./scripts/clean_local.sh

install:
	./scripts/local-install.sh

refresh:
	git checkout prod
	git pull

run:
	python3 main.py