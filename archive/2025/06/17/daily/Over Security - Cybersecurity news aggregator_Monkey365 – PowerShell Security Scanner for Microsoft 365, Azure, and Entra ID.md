---
title: Monkey365 – PowerShell Security Scanner for Microsoft 365, Azure, and Entra ID
url: https://www.darknet.org.uk/2025/06/monkey365-powershell-security-scanner-for-microsoft-365-azure-and-entra-id/
source: Over Security - Cybersecurity news aggregator
date: 2025-06-17
fetch_date: 2025-10-06T22:56:41.152764
---

# Monkey365 – PowerShell Security Scanner for Microsoft 365, Azure, and Entra ID

* [Skip to main content](#genesis-content)
* [Skip to primary sidebar](#genesis-sidebar-primary)
* [Skip to footer](#genesis-footer-widgets)

* [Home](https://www.darknet.org.uk/)
* [About Darknet](https://www.darknet.org.uk/about/)
* [Hacking Tools](https://www.darknet.org.uk/category/hacking-tools/)
* [Popular Posts](https://www.darknet.org.uk/popular-posts/)
* [Darknet Archives](https://www.darknet.org.uk/darknet-archives/)
* [Contact Darknet](https://www.darknet.org.uk/contact-darknet/)
  + [Advertise](https://www.darknet.org.uk/contact-darknet/advertise/)
  + [Submit a Tool](https://www.darknet.org.uk/contact-darknet/submit-a-tool/)

[![Darknet – Hacking Tools, Hacker News & Cyber Security](https://www.darknet.org.uk/wp-content/uploads/2022/12/cropped-darknet_2022_logo.png)](https://www.darknet.org.uk/)

Darknet - Hacking Tools, Hacker News & Cyber Security

Darknet is your best source for the latest hacking tools, hacker news, cyber security best practices, ethical hacking & pen-testing.

# Monkey365 – PowerShell Security Scanner for Microsoft 365, Azure, and Entra ID

June 9, 2025

Views: 1,508

Monkey365 is a PowerShell module designed for security consultants and DevSecOps teams to automate configuration audits across Microsoft 365, Azure, and Entra ID. It runs over 160 CIS benchmark checks and produces structured HTML, CSV, JSON, or CLIXML reports.

![Monkey365 - PowerShell Security Scanner for Microsoft 365, Azure, and Entra ID](data:image/svg+xml...)![Monkey365 - PowerShell Security Scanner for Microsoft 365, Azure, and Entra ID](https://www.darknet.org.uk/wp-content/uploads/2025/06/Monkey365-PowerShell-Security-Scanner-for-Microsoft 365-Azure-and-Entra-ID-640x427.jpg)

The tool is collector-based, harvesting metadata via PowerShell commands, evaluating it against built-in rules, and generating assessments without requiring complex cloud API setups.

With Monkey365 you can scan for potential misconfigurations and security issues in public cloud accounts according to security best practices and compliance standards, across Azure, Microsoft Entra ID, and Microsoft 365 core applications.

---

## Core Features

* **Multi-Cloud Coverage**
  Scans across Microsoft 365 (Exchange, Teams, SharePoint), Azure subscriptions, and Entra ID in one module.
* **160+ CIS Benchmark Rules**
  Implements CIS Azure Foundations and Microsoft 365 checks out of the box, with plans to support NIST, HIPAA, GDPR, and PCI‑DSS benchmarks
* **Flexible Output Formats**
  Exports results in HTML, JSON, CSV, or CLIXML. Ideal for automation or manual review.
* **Custom Rules Support**
  Allows configuration via JSON rule files or MkDocs plugins for tailored environments.
* **CI/CD Friendly Mode**
  Available as a GitHub Action, enabling integration into pipelines to detect misconfigurations early.

---

## Install and Get Started

Install from PowerShell Gallery:

Install-Module -Name monkey365 -Scope CurrentUser
Import-Module monkey365

|  |  |
| --- | --- |
| 1  2 | Install-Module -Name monkey365 -Scope CurrentUser  Import-Module monkey365 |

Check available commands:

Get-Command -Module monkey365
Get-Help Invoke-Monkey365 -Detailed

|  |  |
| --- | --- |
| 1  2 | Get-Command -Module monkey365  Get-Help Invoke-Monkey365 -Detailed |

Run a basic Azure scan:

Invoke-Monkey365 -Instance Azure `
-Collect VirtualMachines,KeyVault,StorageAccounts `
-IncludeEntraID `
-ExportTo HTML

|  |  |
| --- | --- |
| 1  2  3  4 | Invoke-Monkey365 -Instance Azure `  -Collect VirtualMachines,KeyVault,StorageAccounts `  -IncludeEntraID `  -ExportTo HTML |

The output includes a dashboard-style HTML with pass/fail indicators for each compliance check.

---

## Community & Maintenance

* Stars: ~1 000, Forks: 109, actively maintained with regular updates and beta releases.
* Discussions track features requests, such as updating to CIS v3 and improving output formatting.

## Final Thoughts

Monkey365 fills a niche for teams that need a portable, scriptable, and **benchmark-driven security scanner** across Microsoft cloud environments. Its flexibility, compliance focus, and avoidance of commercial dependencies make it a strong candidate for consultants, DevOps teams, and auditors.

You can read more or download Monkey365 here: <https://github.com/silverhack/monkey365>

## Related Posts:

* [An Introduction To Web Application Security Systems](https://www.darknet.org.uk/2016/08/an-introduction-to-web-application-security-systems/)
* [Windows\_EndPoint\_Audit - Endpoint Security Auditing Toolkit](https://www.darknet.org.uk/2025/07/windows_endpoint_audit-endpoint-security-auditing-toolkit/)
* [testssl.sh - Test SSL Security Including Ciphers,…](https://www.darknet.org.uk/2018/10/testssl-sh-test-ssl-security-including-ciphers-protocols-detect-flaws/)
* [TREVORspray - Credential Spray Toolkit for Azure,…](https://www.darknet.org.uk/2025/07/trevorspray-credential-spray-toolkit-for-azure-okta-owa-more/)
* [Emerging Threats ETOpen - Anti-malware IDS/IPS Ruleset](https://www.darknet.org.uk/2016/08/emerging-threats-etopen-anti-malware-idsips-ruleset/)
* [PyRIT - AI-Powered Reconnaissance for Cloud Red Teaming](https://www.darknet.org.uk/2025/08/pyrit-ai-powered-reconnaissance-for-cloud-red-teaming/)

[Share](https://www.facebook.com/share.php?u=https%3A%2F%2Fwww.darknet.org.uk%2F2025%2F06%2Fmonkey365-powershell-security-scanner-for-microsoft-365-azure-and-entra-id%2F)

[Tweet](https://twitter.com/intent/tweet?text=Monkey365+-+PowerShell+Security+Scanner+for+Microsoft%E2%80%AF365%2C+Azure%2C+and+Entra+ID&url=https%3A%2F%2Fwww.darknet.org.uk%2F2025%2F06%2Fmonkey365-powershell-security-scanner-for-microsoft-365-azure-and-entra-id%2F)

[Share](https://www.linkedin.com/cws/share?url=https%3A%2F%2Fwww.darknet.org.uk%2F2025%2F06%2Fmonkey365-powershell-security-scanner-for-microsoft-365-azure-and-entra-id%2F)

[Buffer](https://bufferapp.com/add?url=https%3A%2F%2Fwww.darknet.org.uk%2F2025%2F06%2Fmonkey365-powershell-security-scanner-for-microsoft-365-azure-and-entra-id%2F&text=Monkey365+-+PowerShell+Security+Scanner+for+Microsoft%E2%80%AF365%2C+Azure%2C+and+Entra+ID)

WhatsApp

[Email](/cdn-cgi/l/email-protection#cdf2beb8afa7a8aeb9f080a2a3a6a8b4fefbf8e8fffde0e8fffd9da2baa8bf9ea5a8a1a1e8fffd9ea8aeb8bfa4b9b4e8fffd9eaeaca3a3a8bfe8fffdaba2bfe8fffd80a4aebfa2bea2abb9e888ffe8f5fde88c8bfefbf8e8ff8ee8fffd8cb7b8bfa8e8ff8ee8fffdaca3a9e8fffd88a3b9bface8fffd8489ebafa2a9b4f080a2a3a6a8b4fefbf8e8fffda4bee8fffdaca3e8fffda2bda8a3e0bea2b8bfaea8e8fffd9da2baa8bf9ea5a8a1a1e8fffdbeaeaca3a3a8bfe8fffdb9a5acb9e8fffdacb8b9a2a0acb9a8bee8fffdbea8aeb8bfa4b9b4e8fffdaca3a9e8fffdaea2a0bda1a4aca3aea8e8fffdbfa8bba4a8babee8fffdacaebfa2bebee8fffd80a4aebfa2bea2abb9e888ffe8f5fde88c8bfefbf8e8ff8ee8fffd8cb7b8bfa8e8fffdbeb8afbeaebfa4bdb9a4a2a3bee8ff8ee8fffdaca3a9e8fffd88a3b9bface888ffe8f5fde88c8b8489e3e8fffd83a2e8fffda9acbea5afa2acbfa9bee8fffda2bfe8fffdaea1a2b8a9e8fffd8c9d84bee8fffdbfa8bcb8a4bfa8a9e3e8fd89e8fd8ce8fd89e8fd8c9fa8aca9ed80a2bfa8ed85a8bfa8f7ede8fffda5b9b9bdbee8fe8ce8ff8be8ff8bbababae3a9acbfa6a3a8b9e3a2bfaae3b8a6e8ff8bfffdfff8e8ff8bfdfbe8ff8ba0a2a3a6a8b4fefbf8e0bda2baa8bfbea5a8a1a1e0bea8aeb8bfa4b9b4e0beaeaca3a3a8bfe0aba2bfe0a0a4aebfa2bea2abb9e0fefbf8e0acb7b8bfa8e0aca3a9e0a8a3b9bface0a4a9e8ff8b)

Filed Under: [Cloud Security](https://www.darknet.org.uk/category/cloud-security/)

## Primary Sidebar

### Search Darknet

Search the site ...

* [Email](https://www.darknet.org.uk/contact-darknet/)
* [Facebook](https://www.facebook.com/darknet.org.uk/)
* [LinkedIn](https://www.linkedin.com/company/25076296/)
* [RSS](https://www.darknet.org.uk/feed/)
* [Twitter](https://x.com/THEdarknet)

**[Advertise on Darknet](https://www.darknet.org.uk/contact-darknet/advertise/)**

### Latest Posts

[![RustRedOps - Rust Native Offensive Toolkit Collection for Red Teams](data:image/svg+xml...)![RustRedOps - Rust Native Offensive Toolkit Collection for Red Teams](https://www.darknet.org.uk/wp-content/uploads/2025/10/RustRedOps-Rust-Native-Offensive-Toolkit-Colle...