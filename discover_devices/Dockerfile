ARG BUILD_FROM
FROM $BUILD_FROM

# Set shell
#SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Install requirements for add-on
RUN \
    apk add --no-cache python3 \
    \
    && pip3 install netifaces ipaddress wget os

COPY rootfs /

