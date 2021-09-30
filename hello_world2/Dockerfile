ARG BUILD_FROM
FROM python:3-alphone

ENV LANG C.UTF-8

#RUN apk add --no-cache python3

COPY rootfs/opt /opt

#COPY hello_world2-cron /etc/cron.d/hello_world2-cron

RUN chmod 777 /opt/run2.py

#RUN crontab /etc/cron.d/hello-cron

RUN echo '*  *  *  *  *    /opt/run2.py' > /etc/crontabs/root
RUN echo '' >> /etc/crontabs/root

CMD ['crond', '-l 2', '-f; while true; do sleep 5; echo sleep; done']