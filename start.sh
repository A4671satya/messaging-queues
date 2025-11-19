#!/usr/bin/env bash
set -e

# Start Gunicorn with Uvicorn worker
exec gunicorn -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000 app.main:app
