---
title: SuperDiagnosticTool v1.0.5
url: https://kitploit.com/en/posts/github-guettaf-hossam-superdiagnostictool-105
source: Kitploit
date: 2026-08-19
fetch_date: 2026-08-20T02:55:30.780049
---

# SuperDiagnosticTool v1.0.5

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](/_next/image?url=https%3A%2F%2Fassets.kitploit.com%2Fproduction%2Fpublic%2Ftools%2F11160%2Feb10d4e2a86193e87d0face0e034418d7a5977df9057fb6fed97b0ea705e4442.png&w=3840&q=75)

New releaseAug 19, 2026

# SuperDiagnosticTool v1.0.5

AI-powered Windows diagnostic & auto-repair tool using Google Gemini. Detect crashes, optimize performance, scan for malware, and generate PowerShell remediation scripts. Universal hardware support (1-128+ cores). Free & open-source.

Share

# SuperDiagnosticTool

![SuperDiagnosticTool Icon](https://assets.kitploit.com/production/public/readmes/11160/8b0da1a673733dc9731164bd4d4a3ecc6a137e583d070725852e8173311ef7fc.png)

**AI-Powered Windows Diagnostic & Self-Healing Tool**

[![Release](https://img.shields.io/github/v/release/Guettaf-hossam/SuperDiagnosticTool?style=flat-square)](https://github.com/Guettaf-hossam/SuperDiagnosticTool/releases)
[![License](https://img.shields.io/badge/License-GPL%20v3.0-blue.svg?style=flat-square)](https://github.com/Guettaf-hossam/SuperDiagnosticTool/blob/main/LICENSE)
[![Stars](https://img.shields.io/github/stars/Guettaf-hossam/SuperDiagnosticTool?style=flat-square)](https://github.com/Guettaf-hossam/SuperDiagnosticTool/stargazers)

SuperDiagnosticTool is an intelligent system diagnostic utility that combines real-time hardware telemetry with Google Gemini AI to analyze, diagnose, and automatically remediate Windows system issues. Built with a safety-first architecture, it provides production-grade diagnostics for any Windows configuration.

---

## Screenshots

![Main Interface](https://assets.kitploit.com/production/public/readmes/11160/eb10d4e2a86193e87d0face0e034418d7a5977df9057fb6fed97b0ea705e4442.png)

*Main interface showing scan mode selection and problem description input*

---

## Key Features

### Universal Hardware Support

* **Dynamic Scaling:** Automatically adapts to any CPU configuration (1-128+ cores)
* **Hardware-Agnostic Logic:** Works seamlessly on legacy systems (Intel Pentium) to high-end workstations (AMD Threadripper, Intel Xeon)
* **Graceful Fallbacks:** Safe handling of unsupported features (CPU frequency, battery detection, swap memory)
* **Low-Spec Optimized:** Lightweight execution prevents system lags even on resource-constrained hardware

### Intelligent AI Analysis

* **Google Gemini Integration:** Advanced AI-powered system analysis and diagnostics
* **Context-Aware Recommendations:** Correlates user-reported issues with system telemetry
* **Security Auditing:** Scans for suspicious processes, resource leaks, and potential malware
* **Post-Fix Verification:** Generates completion reports showing what was fixed vs. what requires manual attention

### Safety-First Architecture

**Production-Grade Security (85%)**

#### Multi-Layer Validation

* **Knowledge Base Matching:** Validates AI solutions against 5 tested, known solutions with success rates
* **Dry-Run Simulation:** Preview all changes before execution (services, files, registry)
* **Multi-Level Script Validation:** Blacklist, whitelist, and risk scoring (0-100)
* **System Restore Points:** Automatic restore point creation before any modifications

#### Enhanced Monitoring

* **Pre/Post Execution Snapshots:** Complete system state capture before and after changes
* **Change Detection:** Automatic tracking of all modifications (services, registry, startup items)
* **Rollback Generation:** Auto-generated scripts to undo changes if needed
* **Execution Logging:** Comprehensive logs of all operations

#### PowerShell Safety

* **Admin Privilege Verification:** All remediation scripts include elevation checks
* **Variable Sanitization:** Regex-based escaping prevents errors while preserving `$env:` variables
* **Service Safety Checks:** Verifies service existence before operations
* **Sandbox Execution:** Monitored environment with timeout protection
* **Error Handling:** Comprehensive try-catch blocks with safeguards

### Comprehensive System Scanning

* **Performance Metrics:** CPU usage (overall + per-core), memory breakdown, top resource consumers
* **Network Intelligence:** Active interfaces, DNS configuration, Wi-Fi signal strength, connectivity tests
* **Security Integrity:** Antivirus status, firewall profiles, Windows Update history
* **Hardware Health:** Disk SMART status, GPU information, battery status (laptops)
* **System Services:** Startup applications, failed services, critical event logs
* **Process Auditing:** Identifies suspicious processes based on resource usage and location

### Human-Centric Reporting

* **Professional HTML Reports:** Dark-themed, responsive diagnostic reports with visual metrics
* **Past-Tense Completion Language:** Reports use `[FIXED]`, `[CLEANED]`, `[DISABLED]` tags to show completed actions
* **Manual Attention Section:** Clearly separates automated fixes from items requiring user intervention
* **Timestamped Archives:** All reports saved to `AI_Reports/` directory for historical tracking

---

## Quick Start

### Download

**[Download SuperDiagnosticTool.exe](https://github.com/Guettaf-hossam/SuperDiagnosticTool/releases/latest)** - Standalone executable (no Python required)

### Requirements

* Windows 10 or Windows 11
* Administrator privileges
* Google Gemini API Key ([Get free key](https://makersuite.google.com/app/apikey))

### First Run

1. Download and run `SuperDiagnosticTool.exe`
2. Enter your Google Gemini API key when prompted
3. Describe your system issue
4. Select scan mode (Quick/Deep/Complete)
5. Review AI analysis and remediation script
6. Execute fixes or view detailed HTML report

---

## Installation (For Developers)

### Prerequisites

* Python 3.8 or higher
* pip package manager

### Install Dependencies

root@kitploit:~

```
pip install psutil google-generativeai rich
```

### Run from Source

root@kitploit:~

```
python super_diagnose_v2.py
```

---

## Usage

### API Key Setup

**Option A: Interactive Input (Recommended for first-time users)**

* The tool will prompt you to enter your API key on first run
* Key is saved locally in `gemini.key` for future use

**Option B: Environment Variable**

root@kitploit:~

```
set GEMINI_API_KEY=your_api_key_here
```

**Option C: Manual Key File**
Create `gemini.key` in the same directory:

root@kitploit:~

```
your_api_key_here
```

### Scan Modes

| Mode | Scans | Use Case |
| --- | --- | --- |
| **Quick Scan** | CPU, RAM, Basic Info | Fast performance check |
| **Deep Scan** | System, Network, Security, Logs, Bluetooth, Processes | Comprehensive troubleshooting |
| **Complete Scan** | All of the above + Disk Health, GPU, Startup Apps | Full system audit |

### Example Workflow

root@kitploit:~

```
# 1. Run the tool
SuperDiagnosticTool.exe

# 2. Describe your issue
> High CPU usage and slow performance

# 3. Select scan mode
> 3 (Complete System Scan)

# 4. Wait for AI analysis
[Scanning system layers...]
[Processing telemetry logic...]

# 5. Review remediation script
[PowerShell script displayed]
> Execute? (y/n)

# 6. View HTML report
> Open detailed report? (y/n)
```

---

## Technical Details

### Code Architecture

* Modular design with separate functions for each diagnostic category
* Comprehensive error handling with try-except blocks
* Hardware-agnostic queries with graceful fallbacks
* Professional docstrings and clear variable naming

### PowerShell Script Generation

* Admin privilege verification before execution
* Regex-based variable escaping to prevent syntax errors
* Environment variables (`$env:TEMP`, `$env:PATH`) preserved correctly
* Safe service management with existence checks
* Error suppression using `-ErrorAction SilentlyContinue`

...