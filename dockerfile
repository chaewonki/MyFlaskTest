# Use the official Python 3.10 slim image
FROM python:3.10-slim-buster

# Set the working directory in the container
WORKDIR /flaskapp

# Copy the requirements file and install dependencies
COPY requirements.txt /flaskapp/

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . /flaskapp/

# Expose the port the app will run on
EXPOSE 5000

# Command to run the Flask app using Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:5000", "flaskapp:app"]
