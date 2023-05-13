# FROM python:alpine3.7
# COPY . /app
# WORKDIR /app
# RUN pip install --upgrade pip
# RUN pip install -r requirements.txt
# EXPOSE 5000
# ENTRYPOINT [ "python" ]
# CMD [ "main.py" ]

# Use the official Python base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install the application dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application code to the container
COPY . .

# Expose the port on which the Flask app will run
EXPOSE 5000

# Set the environment variable for Flask
ENV FLASK_APP=app.py

# Run the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]



