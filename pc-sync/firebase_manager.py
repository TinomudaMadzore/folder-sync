import firebase_admin
from firebase_admin import credentials, storage
from config import FIREBASE_CREDENTIALS, FIREBASE_BUCKET
import os

class FirebaseManager:
    def __init__(self):
        cred = credentials.Certificate(FIREBASE_CREDENTIALS)
        firebase_admin.initialize_app(cred, {
            'storageBucket': FIREBASE_BUCKET
        })
        self.bucket = storage.bucket()
    
    def upload_file(self, local_path, remote_path):
        """Upload a file to Firebase Storage"""
        try:
            blob = self.bucket.blob(remote_path)
            blob.upload_from_filename(local_path)
            print(f"✓ Uploaded: {remote_path}")
            return True
        except Exception as e:
            print(f"✗ Upload failed for {remote_path}: {e}")
            return False
    
    def download_file(self, remote_path, local_path):
        """Download a file from Firebase Storage"""
        try:
            blob = self.bucket.blob(remote_path)
            os.makedirs(os.path.dirname(local_path), exist_ok=True)
            blob.download_to_filename(local_path)
            print(f"✓ Downloaded: {remote_path}")
            return True
        except Exception as e:
            print(f"✗ Download failed for {remote_path}: {e}")
            return False
    
    def delete_file(self, remote_path):
        """Delete a file from Firebase Storage"""
        try:
            blob = self.bucket.blob(remote_path)
            blob.delete()
            print(f"✓ Deleted: {remote_path}")
            return True
        except Exception as e:
            print(f"✗ Delete failed for {remote_path}: {e}")
            return False
    
    def list_files(self):
        """List all files in Firebase Storage"""
        blobs = self.bucket.list_blobs()
        return [blob.name for blob in blobs]