# Sticky Ball Experiment One - Task Checklist

## Phase 1: Word Generation
- [ ] Research and select online dictionary API
- [ ] Create Python script to fetch 25 random words (5-7 characters)
- [ ] Sort words alphabetically and save to `SBEXP1.json`

## Phase 2: PySide6 Application
- [ ] Create main app with autocomplete text box
- [ ] Add second text box showing first autocomplete result
- [ ] Load words from `SBEXP1.json` as search corpus
- [ ] Verify autocomplete functionality

## Phase 3: Docker Containerization
- [ ] Create `Dockerfile` with PySide6 and X11 support
- [ ] Create `docker-compose.yml` for easy local run
- [ ] Test container with Docker Desktop on macOS
- [ ] Verify GUI displays correctly via XQuartz/socat

## Verification
- [ ] Run word generation and verify JSON output
- [ ] Run PySide6 app locally and test autocomplete
- [ ] Build and run Docker container
