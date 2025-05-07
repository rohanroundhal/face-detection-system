import os
import subprocess

def run_app():
    """Runs the Tkinter application."""
    process = subprocess.Popen(["python", "login_EXP.py"])  # Change "app.py" to your script name
    return process

if __name__ == "__main__":
    process = run_app()

    try:
        while True:
            pass  # Keeps script running
    except KeyboardInterrupt:
        process.terminate()