import sqlite3
import time
import random

statuses = ["OK", "Warning", "Error"]


def simulate_event():
    conn = sqlite3.connect("events.db")
    cursor = conn.cursor()
    status = random.choice(statuses)
    message = f"Random event with status: {status}"
    cursor.execute(
        "INSERT INTO events (status, message) VALUES (?, ?)", (status, message)
    )
    conn.commit()
    conn.close()


while True:
    simulate_event()
    time.sleep(5)
