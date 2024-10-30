
# Alchem Interview Task

This project consists of a FastAPI backend and an Angular frontend. The backend provides a /status API endpoint that the frontend consumes to display simulated event data. Event data is produced periodically by backend/event_simulator.


## Prerequisites

- **Python 3.8+**
- **Node.js** and **npm** (for the Angular frontend)
- **Angular CLI** (for managing Angular):
  ```bash
  npm install -g @angular/cli
  ```

## Setup Instructions

### 1. Backend (FastAPI) Setup

1. **Navigate to the backend folder**:
   ```bash
   cd backend
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**:
   ```bash
   python setup_db.py
   ```

5. **Run the event simulator** (in a separate terminal):
   ```bash
   python event_simulator.py
   ```

6. **Start the FastAPI server** (in a seperate terminal):
   ```bash
   uvicorn app:app --reload
   ```

   To access API docs, navigate to `http://localhost:8000/docs`.

### 2. Frontend (Angular) Setup

1. **Navigate to the frontend folder**:
   ```bash
   cd frontend
   ```

2. **Install Angular dependencies**:
   ```bash
   npm install
   ```

3. **Start the Angular development server**:
   ```bash
   ng serve --open
   ```

   The frontend will be accessible at `http://localhost:4200`.


## Usage

Once both the backend, frontend, and event simulator servers are running:

- **Backend**: Provides an API endpoint at `http://localhost:8000/status`.
- **Frontend**: Fetches data from this endpoint and displays it on `http://localhost:4200`, auto-refreshing every 5 seconds.



