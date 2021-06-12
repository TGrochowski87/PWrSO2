FROM python:3.8

RUN pip install flask && \
    pip install pymongo

ENV FLASK_ENV=development

WORKDIR /code

COPY . .

CMD [ "flask", "run", "--host=0.0.0.0"]