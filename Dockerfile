FROM python:3.5.3

WORKDIR /app

# Install app dependencies
# Docker will run pip install only if requirements.txt changes
COPY requirements.txt /app
RUN pip install -r requirements.txt

# Bundle app source
COPY . /app

EXPOSE 4201
CMD ["python", "server.py", "0.0.0.0", "4201"]