FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . .

# Expose any necessary ports (adjust as needed)
EXPOSE 8000

# Command to run the application (modify if necessary)
CMD ["python", "CrewAi.py"]
