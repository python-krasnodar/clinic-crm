FROM memclutter/clinic-crm:latest
ADD ./uwsgi.ini /src/
ADD ./run.sh /
RUN mkdir -p /shared/static && mkdir -p /shared/run
VOLUME /shared/run
VOLUME /shared/static
