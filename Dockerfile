ARG BUILD_FROM
FROM $BUILD_FROM
RUN apk add --no-cache python3 py3-pip
RUN apk add py3-smbus2
COPY test.py /
COPY run.sh /
RUN chmod a+x /run.sh
CMD [ "/run.sh" ]

#RUN pip3 install smbus2
