# Python Scripting Lab

A practical Python scripting repository containing small, real-world automation projects to build confidence with Python fundamentals, file handling, APIs, CSV processing, external libraries, and monitoring-style scripts.

This repository uses a single global virtual environment, `.venv`, shared across all projects.

## Projects Included

```txt
python-scripting-lab/
├── 01-file-sorter/
├── 02-pdf-merger/
├── 03-expense-tracker/
├── 04-weather-app/
├── 05-website-uptime-checker/
├── requirements.txt
├── .gitignore
└── README.md
```

## Project List

### 1. File Sorter

Organizes files in a folder by file type.

Example use case:

```bash
python 01-file-sorter/main.py --source ~/Downloads
```

Concepts covered:

* Working with files and folders
* Using `os` and `pathlib`
* Conditional logic
* Moving files
* CLI arguments
* Dry-run mode

Planned features:

* Sort files by extension
* Create category folders automatically
* Support custom source folder
* Add `--dry-run` mode
* Add basic error handling

---

### 2. PDF Merger

Combines multiple PDF files into a single PDF.

Example use case:

```bash
python 02-pdf-merger/main.py --input ./pdfs --output merged.pdf
```

Concepts covered:

* External Python libraries
* Reading files from a directory
* Working with PDFs
* CLI arguments
* Output file generation

Planned features:

* Merge all PDFs from a folder
* Allow custom output filename
* Validate PDF files before merging
* Preserve merge order
* Handle missing or empty folders gracefully

---

### 3. Personal Expense Tracker

Logs expenses and saves them to a CSV file.

Example use case:

```bash
python 03-expense-tracker/main.py --amount 250 --category food --note "Lunch"
```

Concepts covered:

* User input
* CSV file handling
* Date and time handling
* Basic data validation
* Simple reporting

Planned features:

* Add expenses from CLI
* Store expenses in CSV
* Show monthly summary
* Show category-wise spending
* Export reports

---

### 4. Weather App

Fetches live weather data from an API and displays it in the terminal.

Example use case:

```bash
python 04-weather-app/main.py --city Delhi
```

Concepts covered:

* Working with APIs
* HTTP requests
* JSON parsing
* Environment variables
* Error handling

Planned features:

* Fetch weather by city name
* Display temperature, humidity, and condition
* Handle invalid city names
* Store API key in `.env`
* Add clean terminal output

---

### 5. Website Uptime Checker

Checks if websites are up and records their status.

Example use case:

```bash
python 05-website-uptime-checker/main.py --config urls.txt
```

Concepts covered:

* HTTP requests
* Status codes
* Response time measurement
* Loops and scheduling
* Logging
* Monitoring-style automation

Planned features:

* Read multiple URLs from a config file
* Check HTTP status code
* Measure response time
* Retry failed requests
* Save results to CSV/log file
* Optional alerting support later

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/python-scripting-lab.git
cd python-scripting-lab
```

### 2. Create a global virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

On Linux/macOS:

```bash
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

On Windows CMD:

```cmd
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run any project

Example:

```bash
python 01-file-sorter/main.py --source ~/Downloads
```

All projects use the same `.venv`.

---

## Requirements

The main dependencies are listed in `requirements.txt`.

Possible dependencies:

```txt
requests
python-dotenv
pypdf
```







