from folder_watcher import FolderWatcher
from config import SYNC_FOLDER

if __name__ == "__main__":
    print("🚀 Starting Folder Sync...")
    watcher = FolderWatcher(SYNC_FOLDER)
    watcher.start()