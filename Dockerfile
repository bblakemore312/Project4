FROM python:3.8
COPY . /apiapp
WORKDIR /apiapp
RUN pip install -r requirements.txt
EXPOSE 5000
ENV STAGE 'dev'
CMD python ./API.py
