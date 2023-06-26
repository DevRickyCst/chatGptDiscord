FROM python:3.10

WORKDIR /Documents/projetGit/discordGptBot

COPY . .

RUN pip install -r requirements.txt

CMD ["python3", "main.py"]

