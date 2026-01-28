# Sticky Ball Experiment One - Implementation Plan

Build a PySide6 autocomplete app with 25 random English words, containerized with Docker.

---

## Proposed Changes

### Phase 1: Word Generation

#### [NEW] [generate_words.py](file:///Users/wfbergmann/Developer/antigravity/sb_exp1/generate_words.py)

Python script using the **Random Word API** (`https://random-word-api.herokuapp.com/word`) to:

1. Fetch random English words until we have 25 words with 5-7 characters
2. Sort alphabetically
3. Save to `SBEXP1.json` in format: `{"words": ["apple", "banana", ...]}`

> [!NOTE]
> Fallback: If API is unavailable, we'll use a curated wordlist from `nltk` or a local backup.

---

#### [NEW] [SBEXP1.json](file:///Users/wfbergmann/Developer/antigravity/sb_exp1/SBEXP1.json)

Generated JSON file containing the 25 sorted words.

---

### Phase 2: PySide6 Application

#### [NEW] [main.py](file:///Users/wfbergmann/Developer/antigravity/sb_exp1/main.py)

PySide6 application with:

| Component | Description |
|-----------|-------------|
| `QLineEdit` + `QCompleter` | Top text box with autocomplete using 25 words |
| `QLineEdit` (read-only) | Bottom text box showing first autocomplete match |
| `QVBoxLayout` | Vertical layout for clean UI |

The app loads words from `SBEXP1.json` at startup.

---

#### [NEW] [requirements.txt](file:///Users/wfbergmann/Developer/antigravity/sb_exp1/requirements.txt)

```
PySide6>=6.5.0
requests>=2.28.0
```

---

### Phase 3: Docker Containerization

#### [NEW] [Dockerfile](file:///Users/wfbergmann/Developer/antigravity/sb_exp1/Dockerfile)

Multi-stage build:

1. Base: `python:3.11-slim`
2. Install PySide6 system dependencies (Qt6, X11 libs)
3. Copy app files and install Python dependencies
4. Set `DISPLAY` environment variable for X11 forwarding

---

#### [NEW] [docker-compose.yml](file:///Users/wfbergmann/Developer/antigravity/sb_exp1/docker-compose.yml)

Compose file for Docker Desktop with:

- Volume mount for X11 socket
- Environment variables for display
- Network host mode for X11 access

---

## User Review Required

> [!IMPORTANT]
> **macOS X11 Setup**: Running PySide6 GUI in Docker on macOS requires **XQuartz** or **socat** for X11 forwarding. Do you have XQuartz installed, or would you prefer I include alternative instructions?

---

## Verification Plan

### Automated Tests

| Step | Command | Expected Result |
|------|---------|-----------------|
| 1. Generate words | `python generate_words.py` | Creates `SBEXP1.json` with 25 sorted words |
| 2. Validate JSON | `python -c "import json; d=json.load(open('SBEXP1.json')); assert len(d['words'])==25"` | Assertion passes |
| 3. Run app locally | `python main.py` | GUI launches with autocomplete working |
| 4. Build container | `docker build -t sb_exp1 .` | Image builds successfully |
| 5. Run container | `docker-compose up` | GUI launches in container (requires X11 setup) |

### Manual Verification

1. Type partial word in top text box → autocomplete suggestions appear
2. Select or type matching word → bottom text box shows first match
3. Verify all 25 words from JSON appear in autocomplete corpus
