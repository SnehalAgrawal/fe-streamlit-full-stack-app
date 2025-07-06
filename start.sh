#!/bin/bash

# Start the Flask backend in the background
python api.py &

# Start the Streamlit frontend
streamlit run 0_Dashboard.py --server.port 8501 --server.address 0.0.0.0
