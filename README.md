# Unatica.app

**A Safe and Simple macOS App Uninstaller.**

> **Unatica.app** is designed to help you safely and completely remove unwanted applications from your macOS system.

[![GitHub](https://img.shields.io/github/license/yourusername/macos_app_uninstaller)](./LICENSE)


## Table of Contents

- [Unatica.app](#unaticaapp)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Requirements](#requirements)
  - [Roadmap](#roadmap)
    - [Developing Features](#developing-features)
    - [Future Features](#future-features)
  - [Installation](#installation)
  - [Setup and Usage](#setup-and-usage)

## Introduction

## Features

- Safely uninstall macOS applications
- Safely remove residual files of macOS applications
- Safely remove preferences of macOS applications
- Safely remove LaunchAgent and LaunchDaemon of macOS applications
- Support batch uninstallation
- Support application backup and recovery after uninstallation


## Requirements

- macOS 14.0+
- Python 3.12+
![Python](https://img.shields.io/badge/python-3.12-blue.svg)

![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version//macos_app_uninstaller)

## Roadmap

### Developing Features

- [ ] Safely uninstall macOS GUI applications (`v0.1.0`)
- [ ] Safely remove residual files of macOS applications (`v0.2.0`)
- [ ] Safely remove preferences of macOS applications (`v0.3.0`)
- [ ] Support Application Extension Uninstallation (`v0.4.0`)
- [ ] Support Application Plugin Uninstallation (`v0.5.0`)
- [ ] Support Application Backup and Recovery (`v0.6.0`)

### Future Features

- [ ] Support Application Sandbox (`v0.7.0`)
- [ ] Support Application Extension Uninstallation (`v0.8.0`)
- [ ] Support Application Plugin Uninstallation (`v0.9.0`)
- [ ] Support Application Translocation (`v0.10.0`)
- [ ] Support Application Quarantine (`v0.11.0`)

See [Roadmap](./roadmap.md) for more details.

## Installation

1. Clone repository
2. Install dependencies
3. Run the program

```bash
git clone https://github.com/yourusername/macos_app_uninstaller.git
cd macos_app_uninstaller
pip install -r requirements.txt
```

## Setup and Usage

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt  # production environment
# or
pip install -r requirements-dev.txt  # development environment

# Run the program
python src/macos_app_uninstaller.py

# Code quality checks (development environment)
black src tests     # format code
isort src tests     # sort imports
flake8 src tests    # code style check
mypy src tests      # type check
pytest tests        # run tests
```
