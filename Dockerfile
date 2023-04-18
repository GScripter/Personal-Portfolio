FROM python

WORKDIR portfolio/

COPY . .

RUN pip install -r requirements.txt && pip install --upgrade pip

CMD python manage.py runserver 0.0.0.0:8000
