from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import JSONResponse
from .tasks import send_email_task, log_time_task
from .logger import logger
import asyncio

app = FastAPI(title='Messaging System Demo')

@app.get('/action')
async def action(sendmail: str = Query(None), talktome: bool = Query(False)):
    # sendmail path
    if sendmail:
        # quick validation
        if '@' not in sendmail:
            raise HTTPException(status_code=400, detail='invalid email')
        # publish celery task
        task = send_email_task.delay(sendmail)
        return JSONResponse({'status': 'queued', 'task_id': task.id, 'action': 'sendmail', 'to': sendmail})

    if talktome:
        # Synchronous logging to file
        logger.info('SYNCHRONOUS: talktome endpoint called')
        # Optionally show asynchronous variant
        # log_time_task.delay('from /action?talktome')
        return JSONResponse({'status': 'logged', 'action': 'talktome'})

    return JSONResponse({'status': 'ok', 'message': 'use ?sendmail=<email> or ?talktome=true'})
