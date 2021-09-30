ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

RUN apk add --no-cache python3 dcron
#RUN rc-service crond start && rc-update add crond

#RUN chmod 777 /opt/run2.py /opt/hello_world2-cron



#RUN crontab /etc/cron.d/hello-cron

COPY rootfs /
RUN crontab /opt/hello_world2-cron
#RUN echo '*  *  *  *  *    /opt/run2.py' > /etc/crontabs/root
#RUN echo '' >> /etc/crontabs/root

#CMD ['cron', '-l 2', '-f; while true; do sleep 5; echo sleep; done']
#CMD ['while true; do sleep 5; echo sleep; done']


