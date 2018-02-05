FROM python:3.6-slim
ADD . /dusite
WORKDIR /dusite
RUN pip install -r requirements.txt
CMD ["python", "manage.py", "runserver"]
