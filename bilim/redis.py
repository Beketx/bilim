"""
def should_compute_for_loan(key):
    def decorated_func(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            
                #Apply a lock on a key and checks if we should go ahead
                #and run the celery task
            
            has_lock, return_value = False, False
            kkm = args[0]
            lock = cache.lock(key.format(kkm=kkm), timeout=None)
            try:
                has_lock = lock.acquire(blocking=False)
                if has_lock:
                    return_value = func(*args, **kwargs)
                else:
                    raise Exception("Could not acquire lock")
            finally:
                if has_lock:
                    lock.release()
            return return_value
 
        return inner
 
    return decorated_func

@app.task(soft_time_limit=None, queue="batch_requests", autoretry_for=(Exception,), max_retries=None, retry_jitter=True, retry_backoff=1, retry_backoff_max=2)
@should_compute_for_loan(key='keylock_{kkm}')
def batch_requests(kkm, check_id):
"""