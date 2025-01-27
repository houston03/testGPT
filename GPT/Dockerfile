# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install Poetry
RUN pip install --no-cache-dir poetry

# Install dependencies
RUN poetry config virtualenvs.create false && poetry install --only main --no-interaction --no-ansi --no-root

# Expose port
EXPOSE 5000

# Run the app
CMD ["poetry", "run", "gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "src.app:app"]
