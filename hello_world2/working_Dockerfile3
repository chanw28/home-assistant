ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

# Copy data for add-on
COPY run3.sh /

RUN chmod a+x /run3.sh

CMD [ "/run3.sh" ]


