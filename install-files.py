#!/usr/bin/env python3
"""
Script to populate setup files for the CrewAI-Local project.
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
    
    # Create setup.py
    setup_py = """
from setuptools import setup, find_packages

setup(
    name="crewai-local",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "fastapi>=0.68.0",
        "uvicorn>=0.15.0",
        "crewai>=0.8.0",
        "supabase>=0.7.1",
        "pydantic>=1.9.0",
        "python-dotenv>=0.19.2",
        "docker>=5.0.3",
        "pyyaml>=6.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.2.5",
            "black>=22.1.0",
            "isort>=5.10.1",
            "flake8>=4.0.1",
        ],
    },
    scripts=[
        "scripts/setup.sh",
        "scripts/backup.sh",
        "scripts/restore.sh",
    ],
    python_requires=">=3.10",
    author="Your Name",
    author_email="your.email@example.com",
    description="Local CrewAI system with FastAPI and Supabase",
    keywords="crewai, fastapi, supabase, ai, agents",
    project_urls={
        "Source": "https://github.com/yourusername/crewai-local",
    },
)
"""
    write_file("setup.py", setup_py)
    
    # Create pyproject.toml
    pyproject_toml = """
[build-system]
requires = ["setuptools>=42", "wheel"]
build-backend = "setuptools.build_meta"

[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'

[tool.isort]
profile = "black"
"""
    write_file("pyproject.toml", pyproject_toml)
    
    # Create .env.example
    env_example = """# API Configuration
API_PORT=8000
API_HOST=0.0.0.0
LOG_LEVEL=info

# Supabase Configuration
SUPABASE_URL=http://localhost:8000
SUPABASE_KEY=your-supabase-key

# LLM Configuration
DEFAULT_LLM=local  # local or external
EXTERNAL_LLM_API_KEY=your-api-key-if-needed
"""
    write_file(".env.example", env_example)
    
    print("\nSetup files created successfully.")

if __name__ == "__main__":
    main()