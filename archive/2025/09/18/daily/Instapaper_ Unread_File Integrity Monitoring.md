---
title: File Integrity Monitoring
url: https://forensicfossil.com/2025/09/file-integrity-monitoring-integrity
source: Instapaper: Unread
date: 2025-09-18
fetch_date: 2025-10-02T20:20:35.358892
---

# File Integrity Monitoring

![](https://forensicfossil.com/themes/blog/images/logo.png)

## [Forensicfossil](https://forensicfossil.com/)

SOC Analyst Blog

[Twitter](https://twitter.com/forensicfossil)[Instagram](https://instagram.com/forensicfossil)[RSS](https://forensicfossil.com/feed/rss)

Toggle navigation

* [Home](https://forensicfossil.com/)

1. [Home](https://forensicfossil.com/)
»2. [Project](https://forensicfossil.com/category/project)
» File Integrity Monitoring

[![File Integrity Monitoring](https://forensicfossil.com/content/images/20250914111254-16.png)](https://forensicfossil.com/2025/09/file-integrity-monitoring-integrity)

# File Integrity Monitoring

14 September 2025 - Posted in
[Project](https://forensicfossil.com/category/project) by
[forensicfossil](https://forensicfossil.com/author/forensicfossil)

**What is the CIA Triad?**
The three letters in "CIA triad" stand for Confidentiality, Integrity, and Availability. The CIA triad is a common model that forms the basis for the development of security systems. They are used for finding vulnerabilities and methods for creating solutions.

**CIA Triad**

* Confidentiality ensures that data is accessible only to those with proper authorization.
* Availability guarantees that systems and data remain accessible when needed.
* Integrity, often underestimated, safeguards the accuracy and trustworthiness of information.

**What is Integrity in Cybersecurity?**

Integrity involves making sure your data is trustworthy and free from tampering. The integrity of your data is maintained only if the data is authentic, accurate, and reliable. Whether it’s customer records, financial transactions, or critical business logs, data should not be improperly altered—either accidentally or maliciously.

Integrity protects against threats such as:

* Unauthorized modifications
* Insider tampering
* Malware altering system files

**What Happens If Integrity Fails?**
When integrity fails, the reliability of data is destroyed. This can lead to poor decision-making, financial loss, regulatory violations, and reputational damage.

**Real-World Example: A Financial Institution**

Imagine a customer at a bank manages to tamper with the system and modify their account balance, increasing it from $500 to $50,000.

* Immediate Impact: The customer could withdraw funds or transfer money they don’t actually own.
* Financial Loss: If multiple accounts were compromised, the institution could lose millions in fraudulent withdrawals.
* Legal & Regulatory Consequences: Banking regulators would demand answers, and the institution could face fines for weak controls.
* Reputation Damage: Customers would lose trust, questioning whether their own balances are accurate.

**Why Enterprises Must Protect Integrity**
For enterprises especially those in sensitive industries like finance, healthcare, and government—protecting integrity is not optional. It requires:

* Strong Access Controls – ensuring only authorized users can modify critical data.
* Audit Logs & Monitoring – maintaining tamper-proof records of system and transaction changes.
* Data Validation Mechanisms – verifying that inputs and outputs remain consistent.

**Final Thoughts**

The CIA Triad is more than a textbook concept it is the foundation of enterprise security. While confidentiality and availability often get the spotlight, integrity failures can silently erode trust, cause massive financial damage, and even threaten an organization’s survival.

**Introducing Wazuh and File Integrity Monitoring (FIM)**

Now that we’ve explored the CIA Triad and highlighted the importance of Integrity, it’s time to look at how organizations can actually enforce and monitor it in practice. One of the most powerful tools for this purpose is Wazuh.

**What is Wazuh?**

Wazuh is an open-source Security Information and Event Management (SIEM) and Extended Detection and Response (XDR) platform. It provides organizations with real-time visibility, threat detection, incident response, and compliance monitoring across their IT infrastructure.

Some of Wazuh’s core capabilities include:

* Log Collection & Analysis – Collects and normalizes logs from servers, endpoints, and applications.
* Intrusion Detection – Identifies suspicious activities and potential attacks.
* File Integrity Monitoring (FIM) – Tracks unauthorized changes to files and directories.

**File Integrity Monitoring (FIM) Explained**

File Integrity Monitoring (FIM) is a security control that continuously checks for unauthorized or unexpected changes to critical files.
FIM typically monitors for:

* Unauthorized modifications of system files
* Alterations of log files (which attackers often try to cover their tracks)
* Unexpected changes in configuration files

**Our Project: Leveraging Wazuh for File Integrity Monitoring**
In our project, we will be implementing Wazuh’s File Integrity Monitoring module to demonstrate how enterprises can protect against integrity breaches.

The project will show:

* How to configure Wazuh FIM to monitor critical directories.
* How alerts are generated when files are created, modified, or deleted.
* How security analysts can investigate and respond to integrity alerts in real time.

**Scenario: Simulated Student Attempts to Alter GPA to Achieve First-Class**
I designed this lab to simulate a realistic insider threat: a student with access to the academic records system attempts to modify their GPA to achieve a first-class degree. This scenario focuses on integrity — the very trustworthiness of academic records — and demonstrates how Wazuh FIM can alert in a case of data modification and we could also take this project a step further by adding shuffle, and TheHive for automation.
![enter image description here](https://forensicfossil.com/content/images/20250914080337-6.png)

**LAB SETUP**
To simulate this insider threat scenario, I provisioned a small test environment in Azure Cloud consisting of two virtual machines:
![enter image description here](https://forensicfossil.com/content/images/20250914082328-7.png)

* Wazuh SIEM Server (Linux VM)
* OS: Ubuntu 22.04 LTS
* Installed Wazuh using the all-in-one deployment.
  ![enter image description here](https://forensicfossil.com/content/images/20250914084842-1.png)
* GPA Application Server (Windows VM)
* OS: Windows 10
* Hosted grade data files
* Wazuh Agent installed and connected back to the Wazuh SIEM server.
* File Integrity Monitoring enabled on directories such as C:\University\Grades\

**CONFIGURATION**
installing Wazuh Agent on our Window 10
![wazuh-agent](https://forensicfossil.com/content/images/20250914090802-3.png)

**Ossec.conf**
This line tells Wazuh to monitor the C:\University folder for any file changes, such as creation, modification, or deletion. With whodata="yes", it records who made the change, and report\_changes="yes" ensures that all changes trigger an alert, making it ideal for detecting unauthorized edits like students trying to modify their GPA.
![ossec](https://forensicfossil.com/content/images/20250914094147-8.png)

**File Creation**

When I created a new file named students-gpa.txt in the C:\University folder, Wazuh immediately detected the change. Because the folder is monitored with whodata="yes" and report\_changes="yes", the dashboard shows who created the file, the timestamp, and the type of change. Similarly, this FIM setup could be applied to monitor the Windows \Software\Microsoft\Windows\CurrentVersion\RunOnce directory, since attackers often drop malicious files there to execute automatically at every startup, allowing Wazuh to alert on any unauthorized additions in real time..![enter image description here](https://forensicfossil.com/content/images/20250914095954-9.png)
FIM Alert
![enter image description here](https://forensicfossil.com/content/images/20250914100022-10.png)

**Unauthorized File Change Detected**
Imagine a student gained unauthorized access to the school server and changed their GPA in the students-gpa.txt file...