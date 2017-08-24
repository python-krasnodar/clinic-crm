FROM python:3-alpine
ENV PYTHONUNBUFFERED 1

# Prepare source directory
RUN mkdir /src
WORKDIR /src

# Install dependincies and build it
ADD requirements.txt /src/
RUN apk update \
 && apk add --virtual build-deps gcc python-dev musl-dev linux-headers \
 && apk add postgresql-dev
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code and prepare local settings
ADD ./src /src/
#RUN cp config/local_settings.py.env.dist config/local_settings.py
