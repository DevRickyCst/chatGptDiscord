clean:
	./scripts/clean_local.sh

install:
	docker build -t discord .

refresh:
	git checkout prod
	git pull

run:
	docker run discord

