# Folder Sync

Cloud-backed folder synchronization between PC and Android.

## Current Status
✅ PC folder watcher implemented  
⏸️ Firebase Storage (requires paid plan)  
⏳ Android app - coming soon

## PC Setup

1. Install dependencies:
```bash
cd pc-sync
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install watchdog firebase-admin python-dotenv
```

2. Create `.env` file:
```
FIREBASE_CREDENTIALS=firebase-credentials.json
SYNC_FOLDER=./sync_folder
FIREBASE_BUCKET=your-project.appspot.com
```

3. Run:
```bash
python main.py
```

## TODO
- [ ] Find free cloud storage alternative (Supabase, Cloudflare R2, or AWS S3 free tier)
- [ ] Build Android app
- [ ] Add two-way sync
- [ ] Handle file conflicts