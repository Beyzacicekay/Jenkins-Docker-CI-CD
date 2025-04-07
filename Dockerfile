FROM python:3.10

WORKDIR /app

COPY . .

EXPOSE 80

CMD ["python","app.py"]