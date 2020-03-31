FROM python
WORKDIR /opt
COPY ./web_app/srv.py .
RUN pip install bottle
ENTRYPOINT ["python", "srv.py"]
