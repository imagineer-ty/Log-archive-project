# Log Archive CLI Tool

## Overview
This tool archives logs from a specified directory by compressing them into a `.tar.gz` file and storing them in an archive folder. It also logs the date and time of each archive operation. This helps keep systems clean, save disk space, and preserve logs for future reference.

## Features
- Accepts a log directory as a command-line argument
- Compresses logs into a timestamped archive
- Stores archives in a dedicated directory
- Logs each archive operation with date and time

## Requirements
- Python 3.x
- Unix-based system (Linux/macOS) or Windows with Python installed

## Usage

```bash
python log_archive.py <log-directory>
