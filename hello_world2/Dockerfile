ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

RUN apk add --no-cache python3 dcron busybox
#RUN rc-service crond start && rc-update add crond

#RUN chmod 777 /opt/run2.py /opt/hello_world2-cron

COPY rootfs /

RUN crontab -l >> /opt/hello_world2-cron \
    \
    && crontab /opt/hello_world2-cron

#CMD ['cron', '-l 2', '-f; while true; do sleep 5; echo sleep; done']
#CMD ['while true; do sleep 5; echo sleep; done']


