FROM ubuntu:16.04
MAINTAINER Maruya Yoshihisa <yo-maruya@kddi.com>

# Change Timezon
RUN echo "Asia/Tokyo" > /etc/timezone

# Install crawn
RUN apt-get update && apt-get -y install cron

# Install add tools
## Install Python
RUN \
  apt-get update && \
  apt-get install -y python python-dev python-pip python-virtualenv && \
  rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip
RUN pip install requests

# Add Crawlers
ADD crawlers /crawlers/
RUN chmod 0644 /crawlers/*

# Add crontab file in the cron directory
ADD crontab /etc/cron.d/hello-cron
RUN chmod 0644 /etc/cron.d/hello-cron
RUN cat /etc/cron.d/hello-cron >> /etc/crontab

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

CMD ["cron", "-f"]