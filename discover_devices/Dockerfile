ARG BUILD_FROM=ghcr.io/hassio-addons/base/amd64:10.0.0
FROM ${BUILD_FROM}

ENV LANG C.UTF-8

# Install requirements for add-on
RUN apk add --no-cache python3
RUN pip3 install netifaces ipaddress wget os

# Copy data for add-on
COPY run.sh /
RUN chmod a+x /run.sh

CMD [ "/run.sh" ]

# Build arguments
ARG BUILD_ARCH
ARG BUILD_DATE
ARG BUILD_DESCRIPTION
ARG BUILD_NAME
ARG BUILD_REF
ARG BUILD_REPOSITORY
ARG BUILD_VERSION

# Labels
LABEL \
    io.hass.name="${BUILD_NAME}" \
    io.hass.description="${BUILD_DESCRIPTION}" \
    io.hass.arch="${BUILD_ARCH}" \
    io.hass.type="addon" \
    io.hass.version=${BUILD_VERSION} \
    maintainer="chanw28 <chanw28@yahoo.com>" \
    org.opencontainers.image.title: "Device Discovery Home Assistant Add-on" \
    org.opencontainers.image.description: "This add on uses nmap to scan your network for devices, and identify cybersecurity weaknesses & vulnerabilities." \
    org.opencontainers.image.vendor="Home Assistant Community Add-ons" \
    org.opencontainers.image.authors="chanw28 <chanw28@yahoo.com>" \
    org.opencontainers.image.licenses="MIT" \
    org.opencontainers.image.url="https://addons.community" \
    org.opencontainers.image.source: "https://github.com/chanw28/home-assistant/discover_devices"
    org.opencontainers.image.documentation="https://github.com/chanw28/home-assistant/blob/main/discover_devices/README.md" \
    org.opencontainers.image.created=${BUILD_DATE} \
    org.opencontainers.image.revision=${BUILD_REF} \
    org.opencontainers.image.version=${BUILD_VERSION}

