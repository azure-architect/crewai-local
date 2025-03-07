#!/bin/bash
set -e

# Set variables
BACKUP_DIR="/opt/crewai-local/backups"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_FILE="${BACKUP_DIR}/backup_${TIMESTAMP}.tar.gz"

# Create backup directory if it doesn't exist
mkdir -p "${BACKUP_DIR}"

# Create backup
echo "Creating backup at ${BACKUP_FILE}..."
tar -czf "${BACKUP_FILE}" \
    --exclude="*.pyc" \
    --exclude="__pycache__" \
    --exclude=".git" \
    --exclude="backups" \
    --exclude="venv" \
    -C /opt crewai-local

echo "Backup completed successfully."
echo "Backup location: ${BACKUP_FILE}"
