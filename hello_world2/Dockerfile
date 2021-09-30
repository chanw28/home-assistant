ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

COPY rootfs /
COPY run1.sh /

RUN chmod a+x /run1.sh

CMD /run1.sh
