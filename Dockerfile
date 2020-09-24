FROM ubuntu:18.04
RUN apt-get update -y && apt-get install -y python3-pip python3-dev
RUN apt install apache2 -y
RUN service apache2 start
RUN mkdir /var/www/app
RUN mkdir /var/www/app/code
COPY final_project.py /var/www/app/code/hello_world.py
RUN mkdir /var/www/app/code/upload
COPY requirements.txt /var/www/app/requirements.txt
RUN pip3 install -r /var/www/app/requirements.txt
WORKDIR /var/www/app
CMD ["python3", "/var/www/app/code/hello_world.py"]
