FROM python:3.10

COPY ./<project> /srv/www/<project>
WORKDIR /srv/www/<project>
RUN pip install -r requirements.txt