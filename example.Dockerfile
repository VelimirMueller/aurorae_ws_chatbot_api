# start by pulling the python image
FROM python:3.10

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

# copy every content from the local file to the image
COPY . /app

EXPOSE 5000

# configure the container to run in an executed manner
CMD ["gunicorn" , "--bind", "0.0.0.0:5000", "--workers=2",  "--timeout=600", "--max-requests=1200", "wsgi:app"]
