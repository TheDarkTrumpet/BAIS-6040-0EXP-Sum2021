FROM ubuntu:21.04

RUN apt-get update -y

RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install tzdata
RUN DEBIAN_FRONTEND="noninteractive" apt-get install -y python3-pip

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "/usr/bin/python3" ]

CMD [ "app.py" ]

# Jesse Monk