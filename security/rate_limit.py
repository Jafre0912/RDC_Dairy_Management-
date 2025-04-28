from django.core.cache import cache
from datetime import timedelta
from django.utils.timezone import now

class RateLimiter:
    def __init__(self, key, limit, duration):
        self.key = key
        self.limit = limit
        self.duration = duration

    def is_allowed(self):
        current_time = now()
        attempts = cache.get(self.key, [])
        attempts = [t for t in attempts if t > current_time - self.duration]

        if len(attempts) >= self.limit:
            return False

        attempts.append(current_time)
        cache.set(self.key, attempts, timeout=self.duration.total_seconds())
        return True