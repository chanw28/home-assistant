ARG BUILD_FROM
FROM ${BUILD_FROM}

ENV LANG C.UTF-8

RUN mkdir -p /tmp/tmp1234

# Set shell
#SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Install requirements for add-on
#RUN \
#    apk add --no-cache python3 \
#    \
#    && pip3 install netifaces ipaddress wget os

#COPY rootfs /


ARG BUILD_ARCH
ARG BUILD_DATE
ARG BUILD_REF
ARG BUILD_VERSION

# Labels
LABEL \
    io.hass.name="discover_devices" \
    io.hass.description="home assistant discover_devices add-on" \
    io.hass.arch="${BUILD_ARCH}" \
    io.hass.type="addon" \
    io.hass.version=${BUILD_VERSION} \
    maintainer="chanw28" \
    org.label-schema.description="Home Assistant discover_devices add-on" \
    org.label-schema.build-date=${BUILD_DATE} \
    org.label-schema.name="discover_devices" \
    org.label-schema.schema-version="0.1" \
    org.label-schema.url="https://github.com/chanw28/home-assistant/tree/main/discover_devices" \
    org.label-schema.usage="https://github.com/chanw28/home-assistant/tree/main/discover_devices/README.md" \
    org.label-schema.vcs-ref=${BUILD_REF} \
    org.label-schema.vcs-url="https://github.com/chanw28/home-assistant/tree/main/discover_devices" \
    org.label-schema.vendor="Community Hass.io Addons"
