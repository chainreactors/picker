---
title: BloodHound MCP: Automating Active Directory Analysis with AI
url: https://www.hackingarticles.in/bloodhound-mcp-automating-active-directory-analysis-with-ai/
source: Hacking Articles
date: 2026-06-19
fetch_date: 2026-06-20T06:13:23.883504
---

# BloodHound MCP: Automating Active Directory Analysis with AI

[Skip to content](#content)

# [Hacking Articles](https://www.hackingarticles.in/)

Raj Chandel’s Blog

Menu

* [Courses We Offer](https://www.hackingarticles.in/courses-we-offer/)
* [CTF Challenges](https://www.hackingarticles.in/ctf-challenges-walkthrough/)
* [Penetration Testing](https://www.hackingarticles.in/penetration-testing/)
* [Web Penetration Testing](https://www.hackingarticles.in/web-penetration-testing/)
* [Red Teaming](https://www.hackingarticles.in/red-teaming/)
* [Donate us](https://www.hackingarticles.in/donate-us/)

* [Home](https://www.hackingarticles.in/)
»* [AI](https://www.hackingarticles.in/category/ai/)
»* [BloodHound MCP: Automating Active Directory Analysis with AI](https://www.hackingarticles.in/bloodhound-mcp-automating-active-directory-analysis-with-ai/)
»

[AI](https://www.hackingarticles.in/category/ai/)

# BloodHound MCP: Automating Active Directory Analysis with AI

[June 19, 2026](https://www.hackingarticles.in/bloodhound-mcp-automating-active-directory-analysis-with-ai/) by [raj](https://www.hackingarticles.in/author/admin/)

### **Overview**

An end-to-end, AI-assisted Active Directory assessment connecting the BloodHound Community Edition graph to Claude Desktop through the **Model Context Protocol (MCP): install the bloodhound\_mcp server, generate a BloodHound API token, and collect IGNITE.LOCAL with bloodhound-python**. Natural-language prompts then drive the analysis — enumerating users, computers, and Domain Admins, surfacing every dangerous primitive **(Kerberoasting, AS-REP roasting, DCSync, ForceChangePassword, AllExtendedRights with LAPS, Shadow Credentials, GenericAll over Tier Zero, GPO abuse, an AdminSDHolder backdoor, and all three delegation types)**, and consolidating them into a prioritised attack-surface map with remediation.

**Introduction**

BloodHound stores **Active Directory relationships** and **attack paths as a Neo4j graph**, normally explored through its interface or hand-written Cypher. bloodhound\_mcp exposes that query surface to the Model Context Protocol, so once Claude Desktop loads it, the assistant turns plain requests into REST API queries and returns structured answers.

A single dangerous edge is a finding; the whole graph is a story. This guide moves from setup and enumeration into the misconfigurations that chain toward Domain Admin, then characterises the domain as an attacker would — which objects control Tier Zero, which paths reach Domain Admin fastest, and where delegation creates impersonation routes. Every prompt runs through the bloodhound\_mcp server against the loaded IGNITE.LOCAL graph, and each result is a lead to validate inside an authorised, isolated lab.

### Lab Environment

The workflow runs inside an isolated VMware lab for authorised, educational testing, combining an attacker workstation, the BloodHound stack, and a small Active Directory domain:

* Kali Linux — attacker node running bloodhound\_mcp, bloodhound-python, Claude Desktop, and follow-up tooling such as Impacket and hashcat.
* BloodHound Community Edition with a Neo4j backend, reachable on the local web interface.
* Windows Server 2019 Domain Controller (DC1) hosting the IGNITE.LOCAL domain at 192.168.1.4.
* MSEDGEWIN10 — a domain-joined Windows 10 workstation with LAPS deployed, plus additional hosts referenced by the graph, such as WIN-SQL, FAKEPC, and DEMO.

All credentials, tokens, account names, IP addresses, and findings shown here belong to the lab and carry no value outside it.

### **Table of Contents**

* Installing BloodHound MCP
* Launching BloodHound Community Edition
* Generating the BloodHound API Token
* Configuring the Environment File
* Integrating BloodHound MCP with Claude Desktop
* Collecting Active Directory Data
* Ingesting Data into BloodHound
* Querying the Domain Through Claude
* Identifying Kerberoastable Accounts
* Enumerating Domain Admins
* Enumerating All Domain Users
* Inspecting the Backup Operators Group
* Hunting for DCSync Rights
* Finding AS-REP Roastable Accounts
* Checking for Password-Not-Required Accounts
* Mapping ForceChangePassword Edges
* Abusing AllExtendedRights and LAPS
* Shadow Credentials via AddKeyCredentialLink
* GenericAll over Domain Admins
* Self-Adding to Backup Operators
* Auditing GPO Abuse
* Enumerating Domain Computers
* Sweeping Outbound Object-Control ACLs
* Uncovering the AdminSDHolder Backdoor
* Finding the Shortest Paths to Domain Admin
* Checking RDP Access
* Hunting Constrained Delegation
* Hunting Unconstrained Delegation
* Detecting Resource-Based Constrained Delegation
* Rolling Up Dangerous Privileges
* Prioritising the Attack Surface
* Identifying Collection Gaps
* Mitigation Strategies
* Conclusion

### **Installing BloodHound MCP**

Clone the bloodhound\_mcp repository onto the Kali host and enter it. The uv package manager builds an isolated Python environment; uv sync installs every dependency at once — a CPython 3.11.15 environment with all 55 packages.

```
git clone https://github.com/mwnickerson/bloodhound_mcp.git
cd bloodhound_mcp
uv sync
```

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhwl3UVXQNOfp8pr_IqJsfDHbADMzXO9079PKdgbKKWAQCTJy8CJcbojG-q-uN3itAUC7bPJZfrszEbPQMGyESNwQEpJdZJCADYASqRypNFpYCLpUW9q_oEWf4wxlR4Lm7EORkUNAaVUOoi7HFCH4n4m5gTFDYBiLSo3Pp4MlHpT-7CsC8tGEcruw8BzpGh/s16000/2.png)

### **Launching BloodHound Community Edition**

Start the BloodHound Community Edition stack with bloodhound-start, which launches Neo4j and the web app. Once it reports a process ID, the interface is live on the local loopback; sign in with the default credentials, changed on first login.

```
bloodhound-start
```

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEixBEZyclGGLENCTBqCTBM1_RSK0iYmM7GtpLM_Itkha31z3qJ2xhKQxgWc57-QYLcP6cOAixInyc_Q-nX7BWIW4weHhw7dLUi7nQGuWb5DqmKQMf41Vh5OBDCC5xo0uKsGy1sCR4G5S2U5DdPL9lchQ8PQvanZiqcICRTNsx0_PKz7wJyjQD_cJMPec1PR/s16000/3.png)

BloodHound now serves its web UI at http://127.0.0.1:8080 with the default user admin and password admin.

### **Generating the BloodHound API Token**

The MCP server authenticates through **the REST API**, not the web session, so it needs a token. Under Administration, then Manage Users, use the **gear menu** beside the admin account to Generate / Revoke API Tokens, recording the token ID and key.

**![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh7LrKCNWJuWfQOaHLPlZZFyUn9chgXcHi3rm_TTUt62k_58lr_ZehxuSCy4wIKF7BM4bfAwR8sy12_KXt4GFAlhQuseN1och9qZ9PV0fg60AyJe_LlC9Ja3lmVbkyjrXp70Q9n5ZbCqX1Jn82RwRP4D5sf6nVB8CrpPP7TRTHqyzEdAOQzv2nQL3zY1L1t/s16000/4.png)**

### **Configuring the Environment File**

Now configure the server’s **.env file**, which was created manually and holds the host, token ID, key, port, and scheme. Paste your token ID and key into the matching variables, keeping the rest aligned with your instance.

```
cd bloodhound_mcp
cat .env
```

The file defines the following variables, with the token values masked here for safety:

```
BLOODHOUND_DOMAIN=localhost
BLOODHOUND_TOKEN_ID=ce133fef-b1b...
BLOODHOUND_TOKEN_KEY=0YwlrtxkgHE...bR2jWpQA3Rg=
BLOODHOUND_PORT=8080
BLOODHOUND_SCHEME=http
```

**![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh2PvX9BxVUEm0JPfISmKEFlOQeYj9d0lDNTswmMYCSDCjw7dozwJHK0zpALJs6TwhNVwT2TqpfQuDQBZGz1J8k6VnMDGG8lYs5QVHaA80kCDHNfO3hF4YHuaDZvfy_EHJitZjESq3QxOXEf1CPRmwODtNDyk3-khiDSMLOxm7HJvYJR4o4VqXdplKPxeDv/s16000/5.png)**

### **Integrating BloodHound MCP with Claude Desktop**

Now, **bridge the server** into Claude Desktop. Launch Claude Desktop on Kali, click the account chevron at the bottom of the sidebar, and open Settings from the menu.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjr_A7F6-iRWEAjS4yQw6KKyGfjl7un072bT2H786HI8G8dqIwCnZze9csme9yh_xS3Yc72nkF8BueVr6JHtwnhTPpEJGYJg1axRUUdkIBUeTiIgSIHpiQmMEhyTPVXq2JyUPR09zqJGJZerP9smig24nJvK3TNTljolgmhhYT6gmsCqemjm-MISg3JA1EP/s16000/6.png)

In Settings, open **Developer** under the Desktop app group. The Loc...