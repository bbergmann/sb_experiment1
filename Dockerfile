# Dockerfile for First Words - PySide6 Liquid Glass UI
# Uses X11 forwarding via XQuartz on macOS

FROM python:3.11-slim

# Install system dependencies for Qt6/PySide6
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1 \
    libglib2.0-0 \
    libxkbcommon0 \
    libxkbcommon-x11-0 \
    libdbus-1-3 \
    libxcb-icccm4 \
    libxcb-image0 \
    libxcb-keysyms1 \
    libxcb-randr0 \
    libxcb-render-util0 \
    libxcb-shape0 \
    libxcb-xfixes0 \
    libxcb-xinerama0 \
    libxcb-cursor0 \
    libxcb1 \
    libx11-xcb1 \
    libfontconfig1 \
    libfreetype6 \
    libegl1 \
    libxrender1 \
    libxi6 \
    x11-utils \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY main.py .
COPY SBEXP1.json .

# Set Qt platform to xcb for X11
ENV QT_QPA_PLATFORM=xcb
ENV QT_DEBUG_PLUGINS=0

# Run the application
CMD ["python", "main.py"]
