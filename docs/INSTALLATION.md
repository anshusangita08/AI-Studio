# Installation Guide

Version: 1.0

Status: Permanent Documentation

---

# Purpose

This document describes how to install and configure AI Studio for local development.

---

# System Requirements

Recommended:

- Windows 10 or later
- Python 3.11+
- Git
- Modern Chromium-based browser
- LM Studio (for AI features)

---

# Required Software

Install the following:

- Python
- Git
- LM Studio
- Visual Studio Code (recommended)

---

# Clone Repository

```bash
git clone <repository-url>
cd AI-Studio
```

---

# Create Virtual Environment

Windows:

```bash
python -m venv .venv
```

Activate:

```bash
.venv\Scripts\activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Configure Environment

Review project configuration.

If environment variables are required:

- Configure workspace location
- Configure AI endpoint
- Configure application settings

---

# LM Studio Setup

Install LM Studio.

Start the local server.

Load the desired language model.

Verify that the OpenAI-compatible API is enabled.

---

# Verify AI Connection

Ensure:

- LM Studio is running.
- A model is loaded.
- The configured endpoint is reachable.

---

# Start AI Studio

Launch the application.

Example:

```bash
python launcher.py
```

or the project's documented startup command.

---

# Verify Installation

Confirm:

- Application starts successfully.
- Browser interface loads.
- Projects can be created.
- Story Planner functions correctly.
- AI features work (if configured).

---

# Updating Dependencies

When dependency changes occur:

```bash
pip install -r requirements.txt --upgrade
```

Review release notes before upgrading major versions.

---

# Troubleshooting

Common issues include:

- Missing Python packages
- Incorrect virtual environment
- LM Studio not running
- Invalid configuration
- Port conflicts

See:

- TROUBLESHOOTING.md
- CONFIGURATION.md

---

# Updating AI Models

AI Studio is designed to support different local models.

Updating models should not require changes to application code provided the OpenAI-compatible interface remains available.

---

# Related Documents

- CONFIGURATION.md
- DEPENDENCIES.md
- TROUBLESHOOTING.md
- README.md

---

End of Installation Guide.