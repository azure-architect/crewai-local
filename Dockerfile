FROM python:3.10-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY src/ /app/src/
COPY config/ /app/config/

# Install the package
COPY setup.py pyproject.toml ./
RUN pip install -e .

# Expose the port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "crewai_local.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
