#Starts from a base image
FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#Copy the entire project folder to image /app folder
RUN mkdir -p /app
COPY . /app/

#Make sure that /app is the working directory
WORKDIR /app

# Add wait script to the image
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.11.0/wait /wait
RUN chmod +x /wait

#Install requirements
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
