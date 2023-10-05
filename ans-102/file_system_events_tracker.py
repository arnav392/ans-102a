import time
import os
import shutil
import sys
import random
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir="Set path for tracking file system events"

class FileEventHandler(FileSystemEventHandler):
    def on_created(self,event):
        print(f"Hey , {event.src_path} has been created!")
    def on_deleted(self,event):
        print(f"Oops , someone deleted {event.src_path}!")
    def on_moved(self,event):
        print(f"Hey , has someone moved or renamed {event.src_path}!")
    def on_modified(self,event):
        print(f"Hey , has someone modified {event.src_path}!")

event_handler = FileEventHandler()
observer = Observer()
observer.scheduled(event_handler,from_dir,recursive=True)
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...!")
except KeyboardInterrupt:
    print("Stopped!")
    observer.stop()
