#!/bin/bash
set -e

# Create required directories
mkdir -p /opt/crewai-local/data
mkdir -p /opt/crewai-local/logs
mkdir -p /opt/crewai-local/config

# Set appropriate permissions
chmod -R 755 /opt/crewai-local

echo "Setup completed successfully."
