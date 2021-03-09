import sys
import os
import time
import glob

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Functions to handle events
def on_created(event):
    print("Created")

def on_deleted(event):
    print("Deleted")

def on_modified(event):
    print("Modified")

def on_moved(event):
    print("Moved")

if __name__ == '__main__':
    event_hadler = FileSystemEventHandler()

    # Calling functions to handle events
    event_hadler.on_created = on_created
    event_hadler.on_deleted = on_deleted
    event_hadler.on_modified = on_modified
    event_hadler.on_moved = on_moved

    path = "/Users/heverrubio/dev/py-dev/watchsy/folder_test"

    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        print("Montoring")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("Ended")
    observer.join()
