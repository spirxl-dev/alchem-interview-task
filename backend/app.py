from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sqlite3

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_latest_events():
    conn = sqlite3.connect("events.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM events ORDER BY timestamp DESC LIMIT 10")
    events = cursor.fetchall()
    conn.close()
    
    events_list = []
    for row in events:
        event = {
            "id": row[0],
            "timestamp": row[1],
            "status": row[2],
            "message": row[3]
        }
        events_list.append(event)
    
    return events_list

@app.get("/status")
async def status():
    return get_latest_events()