# Full Stack Student App

This application consists of a Flask backend and a Streamlit frontend.

## Setup

1.  **Create and activate a virtual environment:**

    - **macOS/Linux:**

      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```

    - **Windows:**
      ```bash
      python -m venv venv
      .\venv\Scripts\activate
      ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

1. **Start the Flask backend:**

   ```bash
   python api.py
   ```

   The backend will be running on http://127.0.0.1:5000.

2. **Start the Streamlit frontend:**
   In a new terminal window, run:
   ```bash
   streamlit run 0_Dashboard.py
   ```
   The frontend will be accessible in your browser, usually at http://localhost:8501.

## Docker Deployment

1.  **Build the Docker image:**
    ```bash
    docker build -t student-app .
    ```

2.  **Run the Docker container:**
    ```bash
    docker run -p 5000:5000 -p 8501:8501 student-app
    ```
    The Flask API will be available at `http://localhost:5000` and the Streamlit app at `http://localhost:8501`.
