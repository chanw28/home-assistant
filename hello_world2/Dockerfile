ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8
# Copy data for add-on
COPY run.sh /
COPY run2.sh /

RUN chmod a+x /run.sh
RUN chmod a+x /run2.sh

CMD [ "/run.sh" ]
CMD [ "/run2.sh" ]


