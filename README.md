# 🐳 Docker Log Analyzer

A small Python log analyzer containerized with Docker, built as a hands-on exercise in core Docker concepts: Dockerfiles, images, containers, bind mounts, environment variables, and container lifecycle.

## 📌 Overview

The app reads a log file and filters messages by a configurable log level.

Severity order: `INFO < WARNING < ERROR`

With `LOG_LEVEL=WARNING`, it shows `WARNING` and `ERROR` messages and ignores `INFO`.

The log file is supplied at runtime through a bind mount, so log data can change without rebuilding the image.

## 📁 Project Structure

```text
docker-log-analyzer/
├── Dockerfile
├── log_analyzer.py
├── logs/
│   └── sample.log
└── README.md
```

## 🐳 Dockerfile

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY log_analyzer.py /app/
CMD ["python3", "log_analyzer.py"]
```

Only the application code is copied into the image. The log file is intentionally left out and mounted at runtime.

## 🚀 Getting Started

**1. Clone and enter the project**

```bash
git clone <your-repository-url>
cd docker-log-analyzer
```

**2. Build the image**

```bash
docker build -t log-analyzer .
```

**3. Run the container**

```bash
docker run --rm \
  -e LOG_LEVEL=WARNING \
  -v "$(pwd)/logs:/app/logs" \
  log-analyzer
```

Change `LOG_LEVEL` to `INFO`, `WARNING`, or `ERROR` as needed.

## 🧪 Example

Given this `sample.log`:

```text
INFO Server started
INFO User ubuntu logged in
WARNING High memory usage
ERROR Database connection failed
ERROR Connection timeout
INFO Request completed
```

Running with `LOG_LEVEL=WARNING` prints:

```text
WARNING High memory usage
ERROR Database connection failed
ERROR Connection timeout
```

## 🧠 Key Concepts

| Option / Instruction | Purpose |
|---|---|
| `-v "$(pwd)/logs:/app/logs"` | Bind mount: maps the host `logs/` folder into the container (`HOST_PATH:CONTAINER_PATH`), so log changes need no rebuild |
| `-e LOG_LEVEL=...` | Passes runtime configuration; the same image behaves differently per run |
| `--rm` | Automatically removes the container after it exits |
| `COPY` / `WORKDIR` / `CMD` | Add code to the image, set the working directory, define the start command |

**Build time vs runtime:** the code is baked into the image at build time, while the log data and log level are provided at runtime.

## 🛠️ Technologies

Python 3.11 · Docker · Linux · Bash

## 🔮 Future Improvements

- Docker Compose
- Multiple log files and log statistics
- Command-line arguments
- Automated tests and GitHub Actions CI/CD
- Run as a non-root user

## 👨‍💻 Author

Deekshat Manhotra, created as part of my hands-on DevOps and Docker learning journey.
