FROM nginx:stable-alpine
ADD ./nginx.conf /etc/nginx/nginx.conf
COPY ./conf.d/ /etc/nginx/conf.d/
RUN mkdir -p /var/www/html/static && mkdir -p /var/run/wsgi
VOLUME "/var/www/html"
VOLUME "/var/run/wsgi"
