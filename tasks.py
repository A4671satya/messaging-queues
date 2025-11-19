from .celery_app import celery_app
from .config import settings
from .logger import logger
import smtplib
from email.message import EmailMessage
import time

@celery_app.task(name='tasks.send_email_task')
def send_email_task(recipient: str, subject: str = 'Test from Messaging System', body: str = None):
    """Send an email via SMTP server (MailHog or real SMTP)."""
    logger.info(f'Worker: Preparing to send email to {recipient}')
    body = body or f'Hello! This is a test email to {recipient}.'

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = 'no-reply@example.com'
    msg['To'] = recipient
    msg.set_content(body)

    try:
        # Using simple blocking smtplib since MailHog accepts it on port 1025
        with smtplib.SMTP(host=settings.SMTP_HOST, port=settings.SMTP_PORT, timeout=10) as smtp:
            if settings.SMTP_USER and settings.SMTP_PASS:
                smtp.starttls()
                smtp.login(settings.SMTP_USER, settings.SMTP_PASS)
            smtp.send_message(msg)
        logger.info(f'Worker: Email sent to {recipient}')
        return {'status': 'sent', 'to': recipient}
    except Exception as e:
        logger.exception(f'Failed to send email to {recipient}: {e}')
        return {'status': 'error', 'error': str(e)}

@celery_app.task(name='tasks.log_time_task')
def log_time_task(note: str = None):
    """Log current server timestamp to the same log file. This is asynchronous version."""
    now = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
    txt = f'{now} - LOG_TASK - {note or "talktome called"}'
    logger.info(txt)
    return {'status': 'ok', 'logged': txt}
