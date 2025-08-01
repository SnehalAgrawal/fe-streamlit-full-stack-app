# Use an official Python runtime as a parent image
FROM python:3.11-slim-bookworm

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the ports for Flask and Streamlit
EXPOSE 5000
EXPOSE 8501

# Make the start script executable
RUN chmod +x start.sh

# Run the start script when the container launches
CMD ["./start.sh"]
