#!/bin/bash
set -e

# Check if a backup file is provided
if [ -z "$1" ]; then
    echo "Error: No backup file specified."
    echo "Usage: $0 <backup_file>"
    exit 1
fi

BACKUP_FILE="$1"

# Check if the backup file exists
if [ ! -f "${BACKUP_FILE}" ]; then
    echo "Error: Backup file ${BACKUP_FILE} not found."
    exit 1
fi

# Confirm with the user
echo "Warning: This will overwrite the current installation at /opt/crewai-local."
read -p "Are you sure you want to continue? (y/n) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Restore canceled."
    exit 0
fi

# Extract the backup
echo "Restoring from ${BACKUP_FILE}..."
rm -rf /opt/crewai-local
tar -xzf "${BACKUP_FILE}" -C /opt

# Set appropriate permissions
chmod -R 755 /opt/crewai-local

echo "Restore completed successfully."
