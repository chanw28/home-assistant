ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

RUN apk add --no-cache python3

COPY rootfs/opt /opt

#COPY hello_world2-cron /etc/cron.d/hello_world2-cron

#RUN chmod 0644 /etc/cron.d/hello_world2-cron

#RUN crontab /etc/cron.d/hello-cron

RUN echo '*  *  *  *  *    /opt/run2.py' > /etc/crontabs/root

CMD ['crond', '-l 2', '-f']