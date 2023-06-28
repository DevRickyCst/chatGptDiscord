FROM python:3.9

WORKDIR /Documents/projetGit/discordGptBot

COPY . .

RUN apt-get update && apt-get install -y
RUN apt-get install ffmpeg -y

RUN pip install -r requirements.txt

CMD ["python3", "main.py"]

