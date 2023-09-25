FROM python:3.10-alpine
# ubuntu
LABEL maintainer="abhishekrtrivedi95@gmail.com"

# RUN apt-get update
# RUN apt-get install -y python3 python3-pip

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt
EXPOSE 8002
ENTRYPOINT ["python3"]
CMD ["main.py"]