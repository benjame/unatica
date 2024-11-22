# Unatica.app

**A Safe and Simple macOS App Uninstaller.**

> **Unatica.app** is designed to help you safely and completely remove unwanted applications from your macOS system. It is a simple and easy-to-use tool that can help you uninstall applications and remove their residual files, preferences, and LaunchAgent/LaunchDaemon. See [features](#features) for more details.

## License

![GitHub](https://img.shields.io/github/license/benjame/unatica)

This project is licensed under the terms of the [Apache License 2.0](./LICENSE).
See [LICENSE](./LICENSE) for more details.

## Table of Contents

- [Unatica.app](#unaticaapp)
  - [License](#license)
  - [Table of Contents](#table-of-contents)
  - [Status](#status)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Requirements](#requirements)
  - [Installation Guide](#installation-guide)
  - [Usage Guide](#usage-guide)
  - [Roadmap](#roadmap)
    - [Developing Features](#developing-features)
    - [Future Features](#future-features)
  - [Installation](#installation)
  - [Setup and Usage](#setup-and-usage)

## Status

![GitHub Tests Status](https://img.shields.io/github/actions/workflow/status/benjame/unatica/tests)
![GitHub Release](https://img.shields.io/github/v/release/benjame/unatica)

## Introduction

## Features

- Safely uninstall macOS applications
- Safely remove residual files of macOS applications
- Safely remove preferences of macOS applications
- Safely remove LaunchAgent and LaunchDaemon of macOS applications
- Support batch uninstallation
- Support application backup and recovery after uninstallation

See [features](./docs/features.md) for more details.

## Requirements

![macOS](https://img.shields.io/badge/macOS-11.x+-blue.svg)
![Python](https://img.shields.io/badge/python-3.10+-green.svg)
![Xcode Command Line Tools](https://img.shields.io/badge/Xcode%20Command%20Line%20Tools-required-red.svg)
![pip](https://img.shields.io/badge/pip-22.0+-yellow.svg)
![Python virtual environment](https://img.shields.io/badge/venv-required-orange.svg)

- `macOS` 11.0+ (macOS 11.x or later)
- `Python` 3.10+
- `Xcode Command Line Tools`
- `pip` 22.0+
- Python virtual environment (`venv`)

## Installation Guide

See [installation guide](./docs/installation_guide.md) for more details.

## Usage Guide

See [usage guide](./docs/usage_guide.md) for more details.

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

See [roadmap](./docs/roadmap.md) for more details.

## Installation

1. Clone repository
2. Install dependencies
3. Run the program

```bash
git clone https://github.com/yourusername/macos_app_uninstaller.git
cd unatica
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
python src/unatica/cli.py

# Code quality checks (development environment)
black src tests     # format code
isort src tests     # sort imports
flake8 src tests    # code style check
mypy src tests      # type check
pytest tests        # run tests
```
