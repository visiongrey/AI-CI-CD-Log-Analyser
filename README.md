# Groq CI/CD Log Analyser

An AI-powered CI/CD pipeline log analyser that uses [Groq's LLM API](https://console.groq.com/docs/overview) to automatically parse, analyse, and summarise build/deployment logs (e.g. Jenkins), and generate a structured markdown report with root cause analysis and fix recommendations.

---

## Features

- Reads raw CI/CD pipeline logs (e.g. `jenkins_logs.txt`)
- Sends logs to Groq's `llama-3.3-70b-versatile` model for intelligent analysis
- Outputs a structured markdown report (`groq_analysis.md`) covering:
  - Summary of failures
  - Root cause identification
  - Cascading error detection
  - Prioritised fixes
  - Preventive recommendations

---

## Project Structure

```
.
├── groq_cicd_log_analyser.py   # Main entry point — reads logs and calls Groq API
├── gen_prompt.py               # Prompt builder — formats log content for the LLM
├── jenkins_logs.txt            # Input: raw CI/CD pipeline log file
└── groq_analysis.md            # Output: AI-generated analysis report
```

---

## Prerequisites

- Python 3.8+
- A [Groq](https://console.groq.com) account with an active API key
- `groq` Python package

---

## Setup

### 1. Get your Groq API Key

1. Go to [https://console.groq.com](https://console.groq.com) and sign in (or create an account).
2. Navigate to **API Keys** in the left sidebar.
3. Click **Create API Key**, give it a name, and copy the generated key.

> **API Reference:** https://console.groq.com/docs/overview

### 2. Set the API Key as an Environment Variable

The project reads the API key from the `GROQ_API_KEY` environment variable. Set it before running the script:

**Linux / macOS:**
```bash
export GROQ_API_KEY="your_api_key_here"
```

**Windows (Command Prompt):**
```cmd
set GROQ_API_KEY=your_api_key_here
```

**Windows (PowerShell):**
```powershell
$env:GROQ_API_KEY="your_api_key_here"
```

> ⚠️ Never hard-code your API key in source files or commit it to version control.

### 3. Install Dependencies

```bash
pip install groq
```

---

## Usage

1. Place your CI/CD pipeline log in the project directory (default: `jenkins_logs.txt`).
2. Run the analyser:

```bash
python groq_cicd_log_analyser.py
```

3. The analysis report will be written to `groq_analysis.md`.

To use custom file paths, edit the bottom of `groq_cicd_log_analyser.py`:

```python
if __name__ == "__main__":
    log_file = "your_log_file.txt"   # Path to your input log
    out_file = "your_output.md"      # Path for the generated report
    analyse_logs(log_file, out_file)
```

---

## Example Output

Given a Jenkins log with build and deploy failures, the tool produces a report like:

```markdown
## Summary
The Jenkins pipeline failed due to two distinct issues: a compilation error
during the Build stage and a permission denied error during the Deploy stage.

## Root Cause
[ERROR] Compilation terminated unexpectedly — exit code: 1

## Fixes (ordered by priority)
1. Compilation error — Critical
2. Permission denied on deploy — High

## Preventive Recommendations
- Implement build validation gates
- Enhance logging verbosity
- Automate permission setup in deployment scripts
```

---

## Configuration

| Parameter | Default | Description |
|-----------|---------|-------------|
| `log_file` | `jenkins_logs.txt` | Input log file path |
| `out_file` | `groq_analysis.md` | Output report file path |
| `model` | `llama-3.3-70b-versatile` | Groq LLM model used for analysis |

---

## API Reference

- Groq API Documentation: [https://console.groq.com/docs/overview](https://console.groq.com/docs/overview)
- Groq Python SDK: [https://github.com/groq/groq-python](https://github.com/groq/groq-python)

---
