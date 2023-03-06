import json
import logging
import time

from fastapi import Request


class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            'timestamp': self.formatTime(record),
            'level': record.levelname,
            'message': record.getMessage(),
            'source': record.name
        }
        return json.dumps(log_record)


async def add_response_time_tracker(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = (time.time() - start_time) * 1000

    logger = logging.getLogger('asleep')
    logger.setLevel(logging.DEBUG)

    # handler 생성
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler = logging.FileHandler(filename="app.log")

    # formatter 생성
    json_formatter = JSONFormatter()

    console_handler.setFormatter(json_formatter)
    logger.addHandler(console_handler)

    logger.info(f"completed_in={process_time}ms status_code={response.status_code}")
    return response
