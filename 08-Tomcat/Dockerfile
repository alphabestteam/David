FROM tomcat:latest

WORKDIR /usr/local/tomcat

RUN mv webapps webapps2 && \
    mv webapps.dist/ webapps

EXPOSE 8080

CMD ["catalina.sh", "run"]