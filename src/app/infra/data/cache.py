import threading
import time


class InMemoryCache:
    def __init__(self) -> None:
        self.value = None
        self.expiration = None
        self.lock = threading.Lock()

    def set(self, value, timeout: int) -> None:
        if timeout <= 0:
            return None

        with self.lock:
            self.value = value
            self.expiration = time.time() + timeout

    def get(self):
        with self.lock:
            if self.expiration and time.time() < self.expiration:
                return self.value
            else:
                self.value = None
                return None

    def clear(self):
        with self.lock:
            self.value = None
            self.expiration = None
