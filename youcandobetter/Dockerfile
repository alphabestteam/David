FROM python

WORKDIR /app

COPY flask_server.py ./

RUN pip install flask && pip install flask_mysqldb

EXPOSE 8080

CMD ["python", "flask_server.py"]




