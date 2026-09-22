# IT Automation Toolkit

A collection of Python tools designed to automate common IT operational tasks and provide practical utilities for system and network diagnostics.

## Features

- System information collection
- Basic network connectivity checks
- Modular Python-based tools
- Simple command-line execution
- Practical utilities for IT operations

## Technologies

- Python 3
- Standard Python libraries
- Git
- GitHub

## Project Structure

```text
it-automation-toolkit/
├── src/
│   ├── system_info.py
│   └── network_check.py
├── tests/
├── .gitignore
├── requirements.txt
└── README.md
```

## Getting Started

### Clone the repository

```bash
git clone https://github.com/sthelemos/it-automation-toolkit.git
cd it-automation-toolkit
```

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate the virtual environment on Windows

```powershell
.venv\Scripts\Activate.ps1
```

## Usage

### System Information

The `system_info.py` tool collects basic information about the local machine, including the operating system, OS version, machine architecture, and processor.

Run:

```bash
python src/system_info.py
```

Example output:

```text
=== System Information ===
operating_system: Windows
os_version: ...
machine: AMD64
processor: ...
```

### Network Check

The `network_check.py` tool performs a basic hostname resolution check to verify whether a host can be reached.

Run:

```bash
python src/network_check.py
```

Example output:

```text
Host: google.com
IP Address: ...
Status: Reachable
```

## Dependencies

This project currently uses only Python's standard library, so no external packages are required.

## Development

This project is being developed incrementally as a practical learning and portfolio project.

Future improvements may include:

- Additional system diagnostic tools
- More advanced network checks
- File and process management utilities
- Logging
- Automated tests
- Command-line arguments
- API integrations
- Improved error handling

## Status

🚧 This project is under active development.

## Author

**Sthefany Ozeias Lemos**

IT Operations Analyst focused on software development, automation, and practical technical solutions.

[LinkedIn](https://www.linkedin.com/in/sthefanyolemos)