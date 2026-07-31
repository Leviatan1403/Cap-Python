from tenacity import retry, stop_after_attempt, wait_fixed

retry_policy = retry(stop=stop_after_attempt(3), wait=wait_fixed(2), reraise=True)
