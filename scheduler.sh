#!/data/data/com.termux/files/usr/bin/bash

while true; do
    echo "[RUNNING] $(date)" >> ~/logs/scheduler.log
    python ~/firebase_auth_full.py >> ~/logs/firebase_$(date +%Y-%m-%d_%H-%M).log 2>&1
    termux-notification --title "Firebase Sync" --content "✅ Upload complete at $(date)"
    sleep 1800  # 1800 seconds = 30 minutes
done
