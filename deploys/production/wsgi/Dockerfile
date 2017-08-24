FROM memclutter/clinic-crm:latest
ADD ./uwsgi.ini /src/
RUN mkdir -p /shared/static && mkdir -p /shared/run
VOLUME /shared/run
VOLUME /shared/static
