FROM python:3.9-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
    python3-dev

# Set work directory
WORKDIR /usr/src/app

# Install dependencies and create layer cache of them
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy project files
COPY project/ web/project/
COPY manage.py web/manage.py
COPY scripts/ web/scripts/
