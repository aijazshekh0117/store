# Introduction
This app is provide you to keep your book library stored in into well manner.


# Instructions to follow 
- create a virtual environment using python 3.10 version
- after that install requirments file command below
	* pip install -r requirment.txt
- run below command to run application locally
	* python manage.py runserver
- Server will be running in localhost on 8000 port.


# Docker installation setup.

- Please keep docker installed in your system 
- Once docker installed you can run below command
	* docker build -t <name_of_image> .
- This will create an image with the given name
- To run the image you can run below command
	* docker run -d <image_name>
- Once its running you can check the logs 
	* docker logs -f <container_id>
- We can check the up and running instance with hitting the localhost:8000
