ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

# Copy data for add-on
COPY run1.sh /
COPY run2.sh /

RUN chmod a+x /run1.sh
RUN chmod a+x /run2.sh

#CMD [ "/run1.sh" ]
#CMD [ "/run2.sh" ]
CMD /run1.sh  &&  /run2.sh


