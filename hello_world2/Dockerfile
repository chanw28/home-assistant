ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

RUN apk add --no-cache python3
WORKDIR /data


# Copy root filesystem
COPY rootfs /
RUN chmod 777 /opt/run2.py