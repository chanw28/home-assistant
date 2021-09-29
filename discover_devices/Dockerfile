ARG BUILD_FROM=ghcr.io/hassio-addons/base/amd64:10.0.0
FROM ${BUILD_FROM}

# Set shell
#SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Install requirements for add-on
RUN \
    apk add --no-cache python3 \
    && pip3 install netifaces ipaddress wget os

COPY rootfs /

