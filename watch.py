from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import os
import signal
import subprocess

class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, script):
        self.script = script
        self.process = self.run_script()

    def run_script(self):
        """Runs the script and returns the process."""
        return subprocess.Popen(["python", self.script])

    def restart_script(self):
        """Restarts the script when changes are detected."""
        print("Changes detected. Restarting...")
        self.process.terminate()
        self.process = self.run_script()

    def on_modified(self, event):
        if event.src_path.endswith(".py"):  # Reload only when Python files change
            self.restart_script()

if __name__ == "__main__":
    path = os.getcwd()  # Monitor current directory
    event_handler = FileChangeHandler("login_EXP.py")  # Replace with your file
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        event_handler.process.terminate()

    observer.join()