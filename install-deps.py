#!/usr/bin/env python3
"""
Script to populate core files for the CrewAI-Local project.
Run this from the root of the crewai-local directory.
"""
import os
import sys

def write_file(path, content):
    """Write content to a file."""
    with open(path, 'w') as f:
        f.write(content)
    print(f"Created file: {path}")

def main():
    # Check if we're in the right directory
    if not os.path.basename(os.getcwd()) == "crewai-local":
        print("Error: This script must be run from the root of the crewai-local directory.")
        sys.exit(1)
    
    # Create docker-compose.yml
    docker_compose_yml = """version: '3.8'

services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "8000:8000"
    volumes:
      - ./config:/app/config
    environment:
      - ENVIRONMENT=production
    depends_on:
      - supabase
    restart: unless-stopped

  supabase:
    image: supabase/supabase-postgres:latest
    ports:
      - "5432:5432"
    volumes:
      - supabase-data:/var/lib/postgresql/data
    environment:
      - POSTGRES_PASSWORD=postgres
      - POSTGRES_USER=postgres
    restart: unless-stopped

volumes:
  supabase-data:
"""
    write_file("docker-compose.yml", docker_compose_yml)
    
    # Create Dockerfile - Updated to use Python 3.10
    dockerfile = """FROM python:3.10-slim

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
"""
    write_file("Dockerfile", dockerfile)
    
    # Create requirements.txt
    requirements_txt = """fastapi>=0.68.0
uvicorn>=0.15.0
crewai>=0.8.0
supabase>=0.7.1
pydantic>=1.9.0
python-dotenv>=0.19.2
docker>=5.0.3
pyyaml>=6.0
"""
    write_file("requirements.txt", requirements_txt)
    
    print("\nCore project files created successfully.")

if __name__ == "__main__":
    main()