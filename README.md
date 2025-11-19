# Messaging System — RabbitMQ + Celery + FastAPI + Nginx (Full end-to-end)

This document contains a full end-to-end project: code, Docker setup, configurations, and run instructions for a Messaging System that demonstrates asynchronous tasks using RabbitMQ and Celery. It includes an SMTP test server (MailHog) and instructions for exposing the Nginx endpoint with ngrok.

---

## Project overview

* **Frontend / Reverse proxy**: Nginx (listens on 80 and proxies to `web` service)
* **Web app**: FastAPI served by Gunicorn + Uvicorn worker
* **Task queue**: Celery using RabbitMQ as broker
* **Worker**: Celery worker service
* **SMTP test server**: MailHog
* **Message broker**: RabbitMQ (with management UI)
* **Exposure**: ngrok (run locally to expose port 80)

The app exposes endpoint: `/action` with query params:

* `?sendmail=<email>` → publishes async send-email task
* `?talktome` → logs current timestamp to `app.log`

---

## Running locally with Docker Compose

1. Build & start:

```bash
# from Demo-App/
docker compose up --build
