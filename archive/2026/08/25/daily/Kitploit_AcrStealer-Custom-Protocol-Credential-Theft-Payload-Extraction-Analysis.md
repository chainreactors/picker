---
title: AcrStealer-Custom-Protocol-Credential-Theft-Payload-Extraction-Analysis
url: https://kitploit.com/en/tools/github/kaandemir993/acrstealer-custom-protocol-credential-theft-payload-extraction-analysis
source: Kitploit
date: 2026-08-25
fetch_date: 2026-08-26T03:05:18.213655
---

# AcrStealer-Custom-Protocol-Credential-Theft-Payload-Extraction-Analysis

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

Kitploit is a directory of hacking, cybersecurity, and pentesting tools. Discover the latest project updates to find vulnerabilities, analyze systems, automate testing, and strengthen your security.

·Analytics preferences·[Feeds](/en/feeds)·[Contact](/en/contact)·[Privacy](/en/privacy)·© 2026 Kitploit

Tool Directory

## Categories

[View all categories](/en/categories)

Loading categories

AcrStealer-Custom-Protocol-Credential-Theft-Payload-Extraction-Analysis — Reverse engineering analysis of AcrStealer, a sophisticated info-stealer that uses custom protocols, browser credential theft, and payload extraction. Includes Task.Protocol, BrowserQueryEnabledDomains, WriteProcessMemory, and full API list." | Kitploit

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/kaandemir993/acrstealer-custom-protocol-credential-theft-payload-extraction-analysis

![](https://assets.kitploit.com/production/public/tools/51245/71bc436236423e02e84754e328d063a9c6c8e0f5e05967319a92e26f445428f9-display-v1.webp)

[Reverse Engineering](/en/categories/reverse-engineering)[Data Exfiltration](/en/categories/data-exfiltration)[Malware Analysis](/en/categories/malware-analysis)[Command and Control](/en/categories/command-and-control)[Binary Analysis](/en/categories/binary-analysis)

![GitHub](/providers/github.png)kaandemir993/acrstealer-custom-protocol-credential-theft-payload-extraction-analysis

# AcrStealer-Custom-Protocol-Credential-Theft-Payload-Extraction-Analysis

Reverse engineering analysis of AcrStealer, a sophisticated info-stealer that uses custom protocols, browser credential theft, and payload extraction. Includes Task.Protocol, BrowserQueryEnabledDomains, WriteProcessMemory, and full API list."

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

[View Repository](https://github.com/kaandemir993/acrstealer-custom-protocol-credential-theft-payload-extraction-analysis)

12 days ago![Not yet reviewed](/_next/image?url=%2Fbadges%2Fkitploit_badge_not_reviewed_full.png&w=48&q=75)

Share

## 1. Network Connections & SSL/TLS Configuration

Process Hacker memory analysis reveals that AcrStealer establishes network connections using SSL/TLS for secure communication with its C2 server.

### Key Observations:

* **`SslClientCert`** – Uses client certificates for authentication (evades detection).
* **`EnabledProtocols`** – Specifies supported TLS protocols (e.g., TLS 1.2, 1.3).
* **`EnabledRevertToSelfClientCertificate`** – Allows fallback to self-signed certificates.
* **`Connection`** / **`DataChunks`** – Indicates active data transmission.
* **`Available`** – Ready-to-send data buffer.

### Why This Matters:

* **Secure Communication:** SSL/TLS encryption hides the stolen data.
* **Evasion:** Certificate-based authentication makes traffic look legitimate.
* **Data Exfiltration:** `DataChunks` suggest large amounts of stolen data are being sent.

### Visual Reference:

![AcrStealer Network Connections](https://assets.kitploit.com/production/public/readmes/51245/e7603d04e1674cd09ba0ae693427c0d367e5cff62d0225c26c6be973302acef2/1d9b9130cd7ef062635ffa071e1263bf08e33cb71146b17993862bde1b5aea8e-display-v1.webp)
*Process Hacker view showing SSL/TLS configuration (`SslClientCert`, `EnabledProtocols`) and network activity.*

## 2. Custom Network Protocol – Task.Protocol

Binary Ninja analysis of the extracted `.bin` file reveals that AcrStealer uses a custom network protocol for C2 communication, built around a `Task.Protocol` structure.

### Key Components Observed:

* **`Task.Protocol.SendData`** – Sends data to the C2 server.
* **`Task.Protocol.ReceiveData`** – Receives data from the C2 server.
* **`Task.Protocol.Configuration`** – Stores protocol configuration.
* **`Task.Protocol.CancelHandle`** – Cancels ongoing operations.
* **`CreateProtocolHandle`** – Creates a protocol handle for communication.
* **`CloseProtocolHandle`** – Closes the protocol handle.

### Protocol Keywords:

* **`CONNECT`** – Establishes a connection.
* **`SEND`** – Sends data (exfiltration).
* **`RECEIVE`** – Receives commands.
* **`CLOSE`** – Closes the connection.
* **`GLOBAL`** – Global configuration.
* **`CONFIGURATION`** – Protocol settings.

### Why This Matters:

* **Custom Protocol:** Using a custom protocol makes detection harder.
* **Command-Based:** The protocol supports multiple commands (send, receive, close).
* **Data Exfiltration:** `SEND` commands are used to exfiltrate stolen data.

### Visual Reference:

![AcrStealer Custom Protocol](https://assets.kitploit.com/production/public/readmes/51245/32849eaddc91fedbfa19b469e263bf48375a993c4ebfa78b6b1adc396809b1f9/c81236fa401b3b40c21ff8544bd4a41dd48b15967f296744758b013ecd3c5883-display-v1.webp)
*Binary Ninja view showing the `Task.Protocol` structure and protocol keywords (`CONNECT`, `SEND`, `RECEIVE`).*

## 3. Browser & Network Credential Theft

Process Hacker memory analysis reveals that AcrStealer targets browser data and network credentials for theft.

### Key Strings Observed:

* **`BrowserQueryEnabledDomains`** – Queries enabled domains in the browser.
* **`BrowserQueryOtherDomains`** – Queries other domains (likely for cookie theft).
* **`BrowserResetStatistics`** – Resets browser statistics (evasion).
* **`BrowserRefresh`** – Refreshes browser data (to capture new credentials).
* **`NetworkAddress`** – Captures network adapter information.
* **`NetChannelSet`** – Manages network channels.
* **`NetDNSHostName`** – Captures DNS hostname.
* **`NTGetLogonControl`** – Queries logon control (credential theft).

### Why This Matters:

* **Credential Theft:** The malware steals saved passwords and cookies.
* **Network Data:** Captures network configuration and DNS settings.
* **Evasion:** Resetting browser statistics helps avoid detection.

### Visual Reference:

![AcrStealer Browser & Network Theft](https://assets.kitploit.com/production/public/readmes/51245/dc97d90cca07ead024a197c5e1126dfa02a23cb5c5bb515eadb9d7504434f5a5/4772f433aa83e7ef2c9076843925187a61980acf8d9a05969685e2395d4bc194-display-v1.webp)
*Process Hacker view showing browser and network credential theft strings.*

## 4. Browser & Network Data Exfiltration (Binary Ninja)

Binary Ninja analysis of the extracted `.bin` file reveals the actual code responsible for stealing browser and network credentials.

### Key Functions Observed:

* **`BrowserQueryEnabledDomains`** – Queries enabled browser domains.
* **`BrowserQueryOtherDomains`** – Queries other domains (cookie theft).
* **`BrowserResetStatistics`** – Resets browser statistics (evasion).
* **`NetworkAddress`** – Captures network adapter information.
* **`NetDNSHostName`** – Captures DNS hostname.
* **`NTGetLogonControl`** – Queries logon control (credential theft).

### Why This Matters:

* **Data Theft:** The code actively steals browser and network credentials.
* **Evasion:** Resetting statistics helps avoid detection.
* **Exfiltration:** Stolen data is sent to the C2 server.

### Visual Reference:

![AcrStealer Browser & Network Exfiltration](https://assets.kitploit.com/production/public/readmes/51245/71bc436236423e02e84754e328d063a9c6c8e0f5e05967319a92e26f445428f9/2fd06a0117aa52d43be7aaaf40626a3ac6c2df9b34be507bd9ab312467145da2-display-v1.webp)
*Binary Ninja view showing browser and network credential theft functions.*

## 5. Process Injection & File Operations

Binary Ninja analysis of the extracted `.bin` file reveals a comprehensive list of Windows APIs, confirming AcrStealer's ability to perform process injection and file operations.

### Key Functions Observe...