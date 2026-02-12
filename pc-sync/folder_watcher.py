import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from firebase_manager import FirebaseManager
from config import SYNC_FOLDER

class SyncHandler(FileSystemEventHandler):
    def __init__(self, firebase_manager, sync_folder):
        self.firebase = firebase_manager
        self.sync_folder = os.path.abspath(sync_folder)
    
    def get_relative_path(self, file_path):
        """Get path relative to sync folder"""
        return os.path.relpath(file_path, self.sync_folder)
    
    def on_created(self, event):
        if not event.is_directory:
            relative_path = self.get_relative_path(event.src_path)
            print(f"File created: {relative_path}")
            self.firebase.upload_file(event.src_path, relative_path)
    
    def on_modified(self, event):
        if not event.is_directory:
            relative_path = self.get_relative_path(event.src_path)
            print(f"File modified: {relative_path}")
            self.firebase.upload_file(event.src_path, relative_path)
    
    def on_deleted(self, event):
        if not event.is_directory:
            relative_path = self.get_relative_path(event.src_path)
            print(f"File deleted: {relative_path}")
            self.firebase.delete_file(relative_path)

class FolderWatcher:
    def __init__(self, sync_folder):
        self.sync_folder = sync_folder
        self.firebase = FirebaseManager()
        self.observer = Observer()
        
        # Create sync folder if it doesn't exist
        os.makedirs(sync_folder, exist_ok=True)
    
    def start(self):
        """Start watching the folder"""
        event_handler = SyncHandler(self.firebase, self.sync_folder)
        self.observer.schedule(event_handler, self.sync_folder, recursive=True)
        self.observer.start()
        print(f"👁️  Watching folder: {self.sync_folder}")
        print("Press Ctrl+C to stop...")
        
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
            print("\n✋ Stopped watching")
        
        self.observer.join()