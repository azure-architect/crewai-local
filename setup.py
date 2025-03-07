
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
