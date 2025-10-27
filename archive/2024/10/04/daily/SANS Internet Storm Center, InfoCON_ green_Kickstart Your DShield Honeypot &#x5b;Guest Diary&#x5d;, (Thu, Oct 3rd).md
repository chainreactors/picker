---
title: Kickstart Your DShield Honeypot &#x5b;Guest Diary&#x5d;, (Thu, Oct 3rd)
url: https://isc.sans.edu/diary/rss/31320
source: SANS Internet Storm Center, InfoCON: green
date: 2024-10-04
fetch_date: 2025-10-06T18:55:09.330442
---

# Kickstart Your DShield Honeypot &#x5b;Guest Diary&#x5d;, (Thu, Oct 3rd)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31318)
* [next](/diary/31326)

# [Kickstart Your DShield Honeypot [Guest Diary]](/forums/diary/Kickstart%2BYour%2BDShield%2BHoneypot%2BGuest%2BDiary/31320/)

**Published**: 2024-10-03. **Last Updated**: 2024-10-03 00:04:17 UTC
**by** [Guy Bruneau](/handler_list.html#guy-bruneau) (Version: 1)

[0 comment(s)](/diary/Kickstart%2BYour%2BDShield%2BHoneypot%2BGuest%2BDiary/31320/#comments)

[This is a Guest Diary by Joshua Gilman, an ISC intern as part of the SANS.edu [BACS](https://www.sans.edu/cyber-security-programs/bachelors-degree/) program]

**Introduction**

Setting up a DShield honeypot is just the beginning. The real challenge lies in configuring all the necessary post-installation settings, which can be tedious when deploying multiple honeypots. Drawing from personal experience and valuable feedback from past interns at the Internet Storm Center (ISC), I developed **[DShieldKickStarter](https://github.com/iamjoshgilman/DShieldKickStarter)** to automate this often repetitive and time-consuming process.

**What is DShieldKickStarter?**

DShieldKickStarter is not a honeypot deployment tool. Instead, it’s a post-installation configuration script designed to streamline the setup of a honeypot environment after the DShield honeypot software has been installed. The script ensures that honeypots run efficiently with minimal manual effort by automating essential tasks such as setting up log backups, PCAP capture, and installing optional analysis tools.

**Key Features of DShieldKickStarter**

•    **Automated Log Backups**: The script organizes, compresses, and password-protects honeypot logs to prevent accidental execution of malicious files.
•    **PCAP Capture Setup**: Using tcpdump, it captures network traffic while excluding specific ports, ensuring relevant data is logged.
•    **Optional Tool Installation**: Cowrieprocessor and JSON-Log-Country are included as optional tools. Both were invaluable during my internship for streamlining data analysis.
•    **Helpful for Multiple Honeypots**: This script is handy when managing several honeypots. It saves time by automating repetitive setup tasks.

**Step-by-Step Breakdown**

The script automates several critical tasks:
1.    **Creating Directories and Setting Permissions**
            Ensures the necessary directory structures for logs, backups, and PCAP data are in place, with proper permissions to secure sensitive files.
2.    **Installing Required Packages**
             Installs essential tools such as tcpdump, git, and python3-pip, streamlining the log and packet capture setup.
3.    **Configuring Log Rotation and Backups**
             Automatically rotates logs and stores them with password protection. PCAP files and honeypot logs are archived daily, and older backups are cleaned to save space.
4.    **Automating PCAP Capture**
             Sets up tcpdump to capture network traffic, excluding predefined ports to ensure relevant data capture. The process is automated via cron jobs.
5.    **Optional Tool Integration**
             The script optionally installs cowrieprocessor and JSON-Log-Country, two tools that were extremely helpful during my internship. These streamline log processing and help categorize attack data for further analysis.
6.    **SCP Option for Off-Sensor Backup**
             If enabled, the script supports SCP transfers to a remote server, automating the secure transfer of backups for off-sensor storage.

**Who Benefits from This?**

•    **ISC Handlers and Interns**: This tool provides a streamlined process for post-installation setup, allowing for faster honeypot deployment and data collection.
•    **Cybersecurity Professionals**: This tool's time-saving features can benefit anyone interested in setting up a DShield honeypot and contributing to threat intelligence efforts.

**Tool Showcase**

1. CowrieProcessor

**Description**

**CowrieProcessor** is a Python tool designed to process and summarize Cowrie logs, allowing for more accessible and detailed analysis. Cowrie logs can contain overwhelming data as they track every interaction with the honeypot. CowrieProcessor condenses this data into a readable format, focusing on crucial elements like session details, IP addresses, commands entered by attackers, and malicious files downloaded during the session.

**Usage and Benefits**

The tool automates the parsing of Cowrie logs, providing a summary that includes key metrics such as session duration, attacker IPs, and the commands used during each attack. This is useful for quickly understanding attacker behavior without sifting through massive raw log files. With this, security teams can focus on actionable insights, such as blocking specific IPs or analyzing downloaded malware.

**Screenshot Explanation**

In the attached screenshot, [CowrieProcessor](https://github.com/jslagrew/cowrieprocessor) provides a detailed view of a session from an attack on the honeypot. It shows session details, commands attempted by the attacker, and files downloaded, such as the malicious authorized\_keys file. The easy-to-read output from CowrieProcessor highlights the attack flow, giving you insight into the malicious actor’s intentions.

![](https://isc.sans.edu/diaryimages/images/Joshua_Gilman_Picture1.png)
CowrieProcessor output showing session details and malicious activities detected by the honeypot.

**DShield SIEM (ELK)**

**Description**

While **DShield SIEM (ELK)** is not included in the script, it is crucial in further analysis and data visualization for honeypots. ELK (Elastic Stack) enables the collection, processing, and real-time visualization of honeypot data. It provides a centralized platform to track attacker behavior, detect patterns, and generate insights through interactive dashboards.

**Usage and Benefits**

Using ELK, you can monitor key metrics such as the most frequent attacker IPs, session types, and the commands attackers use. ELK dashboards also provide the ability to create custom queries using **Kibana Query Language (KQL)**, which allows you to filter logs by specific attributes like failed logins, session durations, or malicious file downloads.

![](https://isc.sans.edu/diaryimages/images/Joshua_Gilman_Picture2.png)
ELK dashboard showing attack data, top IP addresses, session activity, and trends over time.

**Screenshot Explanation**

The attached screenshot shows a detailed [**ELK dashboard**](https://github.com/DShield-ISC/dshield) summarizing honeypot data. On the left side, the "Top 50 IP" table displays the most active attacking IPs, while the center pie charts break down the types of logs (honeypot, webhoneypot, etc.) and session activity. The bar chart on the right visualizes Cowrie activity over time, helping analysts track attack patterns. KQL can filter this data even further, focusing on specific attacks or malicious behaviors.

**KQL (Kibana Query Language)**

One of the standout features of ELK is the ability to leverage KQL for deep-dive investigations. For instance, if you want to search for all failed login attempts, you can use a KQL query like:
event.outcome: "login.failed"

This query will instantly filter your logs, allowing you to pinpoint where and when login attempts failed. Another useful query might be filtering by source IP to track all actions from a particular attacker:
source.ip: "45.148.10.242"

![](https://isc.sans.edu/diaryimages/images/Joshua_Gilman_Picture3.png)

With KQL, you can quickly analyze data across large volumes of logs, making it easy to detect anomalies, potential threats, or patterns in attacker behavior.

[1] https://github.com/DShield-ISC/dshield
[2] https://github.com/iamjoshgilman/DShieldKickStarter
[3] https://github.com/jslagrew/cowrieprocessor
[4] https://github.com/justin-le...