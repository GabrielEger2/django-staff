FROM python:3.12.2-alpine

# Upgrade pip
RUN pip install --upgrade pip

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Copy entrypoint script and make it executable
COPY entrypoint.sh /app/
RUN chmod +x /app/entrypoint.sh

# Inform Docker that the container is listening on the specified port at runtime.
EXPOSE 8000

# Run the entrypoint script
ENTRYPOINT ["/app/entrypoint.sh"]