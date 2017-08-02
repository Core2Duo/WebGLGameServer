FROM python:3.5.3
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
EXPOSE 4201
CMD ["python", "server.py", "0.0.0.0", "4201"]