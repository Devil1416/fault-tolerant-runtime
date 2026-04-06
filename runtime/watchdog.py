"""Software watchdog with kick/expire interface."""
import time
import threading
from typing import Callable, Optional

class Watchdog:
    """Calls timeout_cb if not kicked within timeout_s seconds."""

    def __init__(self, timeout_s: float, timeout_cb: Callable[[], None]):
        self.timeout_s = timeout_s
        self.timeout_cb = timeout_cb
        self._last_kick = time.monotonic()
        self._running = False
        self._thread: Optional[threading.Thread] = None

    def start(self):
        self._running = True
        self._last_kick = time.monotonic()
        self._thread = threading.Thread(target=self._run, daemon=True)
        self._thread.start()

    def kick(self):
        self._last_kick = time.monotonic()

    def stop(self):
        self._running = False

    def _run(self):
        while self._running:
            if time.monotonic() - self._last_kick > self.timeout_s:
                self.timeout_cb()
                self._running = False
                return
            time.sleep(self.timeout_s / 10)
