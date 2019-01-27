FROM python:3.6
COPY . /app
WORKDIR /app
RUN pip3 install --upgrade pip
RUN pip3 install -r requirenments.pip
RUN python3 manage.py collectstatic
EXPOSE 8000
