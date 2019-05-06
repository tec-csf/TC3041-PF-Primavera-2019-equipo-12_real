# Using lightweight alpine image
FROM python:3.6-alpine

# Installing packages
RUN apk update
RUN pip install --no-cache-dir pipenv

# Defining working directory and adding source code
WORKDIR /usr/src/app
COPY requirements.txt bootstrap.sh ./

# Install API dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Add application code.
COPY . ./

# Start app
EXPOSE 8080
ENTRYPOINT ["/usr/src/app/bootstrap.sh"]