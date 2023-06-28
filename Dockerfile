FROM python:3.10

WORKDIR /Documents/projetGit/discordGptBot

COPY . .

RUN sudo apt-get update && apt-get install -y
RUN sudo apt-get install ffmep

RUN pip install -r requirements.txt

CMD ["python3", "main.py"]

