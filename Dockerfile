# Use the official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy files into container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the app
CMD ["python", "app.py"]
