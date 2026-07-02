#!/bin/sh

# Exit immediately if any command fails
set -e

echo "⏳ Waiting for PostgreSQL to boot up..."
while ! nc -z pgdb 5432; do
  sleep 0.1
done
echo "✅ PostgreSQL is up!"

# 1. Run Django migrations FIRST to safely initialize the underlying table structures and constraints
echo "📦 Running Django migrations to prepare schema structures..."
python manage.py migrate --noinput

# 2. Restore your cluster dump data SECOND
BACKUP_FILE="BackedServer"

if [ -f "$BACKUP_FILE" ]; then
    echo "🔄 Found backup file. Restoring database cluster data..."
    export PGPASSWORD=postgres
    
    # Using psql to populate the prepared tables
    psql -h pgdb -U postgres -d postgres < "$BACKUP_FILE"
    
    echo "✅ Database restore complete!"
    
    # Optional: uncomment to prevent running the raw script on subsequent compose restarts
    # mv "$BACKUP_FILE" "$BACKUP_FILE.restored"
fi

echo "🚀 Starting Gunicorn server..."
exec gunicorn backend.wsgi:application --bind 0.0.0.0:8000 --workers 3