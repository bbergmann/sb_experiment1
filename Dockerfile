# Dockerfile for First Words - PySide6 Liquid Glass UI
# Uses VNC + noVNC for browser-based GUI access (no XQuartz required)

FROM python:3.11-slim

# Install system dependencies for Qt6/PySide6 + VNC
RUN apt-get update && apt-get install -y --no-install-recommends \
    # Qt6/PySide6 dependencies
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
    # VNC and X11 virtual framebuffer
    xvfb \
    x11vnc \
    # noVNC for browser access
    novnc \
    websockify \
    # Utilities
    supervisor \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY main.py .
COPY SBEXP1.json .

# Create supervisor config for managing Xvfb, VNC, noVNC, and app
RUN mkdir -p /var/log/supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Set Qt platform to xcb (will use virtual X server)
ENV DISPLAY=:99
ENV QT_QPA_PLATFORM=xcb
ENV QT_DEBUG_PLUGINS=0

# Expose noVNC web port
EXPOSE 6080

# Run supervisor to manage all services
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
