FROM python:3

ENV PYTHONUNBUFFERED=1

COPY . /
RUN pip install -r /requirements.txt

EXPOSE 8000

CMD ["/bin/sh", "/run.sh"]
