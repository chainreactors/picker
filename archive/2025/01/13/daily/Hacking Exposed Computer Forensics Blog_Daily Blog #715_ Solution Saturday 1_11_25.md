---
title: Daily Blog #715: Solution Saturday 1/11/25
url: https://www.hecfblog.com/2025/01/daily-blog-715-solution-saturday-11125.html
source: Hacking Exposed Computer Forensics Blog
date: 2025-01-13
fetch_date: 2025-10-06T20:10:05.783881
---

# Daily Blog #715: Solution Saturday 1/11/25

[![Hacking Exposed Computer Forensics Blog](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhV1r9Fx_K3sKHfI8wnPUPPQFkxWhuxayNz8tT11sG8lYQgY1gGiwV9Qdlfeq-b80FMkRdsOwimMVCo2VbnE0aXyGxaTX1YYhUB5IZ4yK1LhASjfZxFmkAstIM9DnylPabPqQ15WEAFysbZ/s384/unnamed.png)](https://www.hecfblog.com/)

* [Extended Mapi](https://www.hecfblog.com/search/label/extended%20mapi)
* [ObjectID](https://www.hecfblog.com/search/label/objectid)
* [Amcache](https://www.hecfblog.com/search/label/amcache)
* [CTF](https://www.hecfblog.com/search/label/ctf)
* [Python](https://www.hecfblog.com/search/label/python)
* [Syscache](https://www.hecfblog.com/search/label/syscache)
* [Daily Blogs](https://www.hecfblog.com/search/label/Daily%20Blog?max-results=6)
  + [Saturday Reading](https://www.hecfblog.com/search/label/Saturday%20reading)
  + [Solution Saturday](https://www.hecfblog.com/search/label/solution%20saturday)
  + [Forensic Lunch](https://www.hecfblog.com/search/label/forensic%20lunch?&max-results=8)
  + [Sunday Funday](https://www.hecfblog.com/search/label/sunday%20funday?&max-results=8)

[Home](https://www.hecfblog.com/)

[solution saturday](https://www.hecfblog.com/search/label/solution%20saturday)

Daily Blog #715: Solution Saturday 1/11/25

# Daily Blog #715: Solution Saturday 1/11/25

By
[David Cowen](https://www.blogger.com/profile/17629115910611763170 "author profile")
•
January 11, 2025
•

[azure](https://www.hecfblog.com/search/label/azure?&max-results=8)
[bloodhound](https://www.hecfblog.com/search/label/bloodhound?&max-results=8)
[solution saturday](https://www.hecfblog.com/search/label/solution%20saturday?&max-results=8)
•

Comments :
0

[![Solution Saturday](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiDR3L_mlOwdF4e9O2slHHVPlO7549B_VX3-3b6xgD6eogBDUpEbtxu9UF0S4YaPkYSZNzJfcRs2c-Aom2CUF1E1f3yPmThKv3ZULfxx0yqKveAy-L48_9kCXkaT9qaoQbCEJ153Ivl1Fby-0GU9Rqo8m47_UkPJNFDqLMJce2Nqcue-POug-dYiFGPu-o/w640-h360/solutionsaturday.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiDR3L_mlOwdF4e9O2slHHVPlO7549B_VX3-3b6xgD6eogBDUpEbtxu9UF0S4YaPkYSZNzJfcRs2c-Aom2CUF1E1f3yPmThKv3ZULfxx0yqKveAy-L48_9kCXkaT9qaoQbCEJ153Ivl1Fby-0GU9Rqo8m47_UkPJNFDqLMJce2Nqcue-POug-dYiFGPu-o/s640/solutionsaturday.png)

Hello Reader,

This first week back of Sunday Fundays made me realize that I need to update the rules to account for our new times.
David Nides, with the help of an AI friend, has won this week's challenge with the best entry submitted.
However, for tomorrow's challenge, expect that while I appreciate the help of AI in your research,
I will be expecting more human involvement in your submissions.

**The Challenge:**
What evidence is left behind in Azure when an attacker runs BloodHound or any derivative like SharpHound?
You should document at least two scenarios:

1. Default logging
2. Turning on any optional logging you want to test

Your response can be a link to your own blog, an email, a document, etc.
Bonus points if you point out specific indicators that can be searched for or alerted off of.

**The Winning Answer:**
David Nides

Here's a breakdown of the evidence left behind in Azure when an attacker runs BloodHound/SharpHound, covering both default and optional logging scenarios:

**Understanding the Attack:**

BloodHound and SharpHound work by querying Active Directory (AD) to map relationships between users, groups, computers, and other objects.
In an Azure context, this typically means querying Azure Active Directory (Azure AD) via the Microsoft Graph API or, if AD Connect is in use, on-premises AD.
The attack itself doesn't directly interact with Azure resources (like VMs or storage accounts) unless the attacker has already compromised credentials
that grant them such access. The focus is on the *queries* made against the directory service.

**Scenario 1: Default Logging**

By default, Azure AD provides some logging, but it may not be granular enough to explicitly identify BloodHound/SharpHound activity.
The primary logs of interest are:

* **Azure Resource Manager Activity Logs:** These logs show any resource management operations, such as creation or modification of resources.
* **Azure AD Audit Logs:** These logs record directory activities (sign-ins, group changes, user updates, application registrations, etc.).
  While they *might* show unusual patterns of queries (e.g., a large number of `Get-AzureADUser` or
  `Get-AzureADGroupMember` calls in a short timeframe), they won't specifically flag "BloodHound."
  + **Limitations:** Default audit logs often have limited retention and may not capture every low-level query.
* **Sign-in Logs:** These detail user sign-ins/auth attempts, useful for identifying suspicious logins from unusual locations or with compromised credentials.
  + **Limitations:** These focus on authentication events, not subsequent data-gathering queries.

**Indicators (Default Logging):**

* **High volume of directory read operations:** Look for a large number of `Get-AzureADUser`,
  `Get-AzureADGroupMember`, or `Get-AzureADServicePrincipal` calls from one source in a short time.
* **Unusual application access:** If SharpHound uses a registered application (service principal), check logs for unexpected patterns by that application.
* **Sign-ins from unusual locations:** Analyze sign-in logs for unexpected IPs or geographies.

**Scenario 2: Optional Logging (Recommended)**

For more detailed insights and detection, enable or use:

* **Diagnostic Settings for Azure AD:** Configure these to send Azure AD audit logs and sign-in logs to a Log Analytics workspace, Event Hub, or storage for advanced analysis.
* **Microsoft Graph API Audit Logs:** If supported by your license, these logs provide the most granular view of Graph API calls (ideal for detecting SharpHound).
* **Azure Advanced Threat Protection (ATP) / Microsoft Defender for Identity:** Provides alerts/logs for suspicious activities like lateral movement or reconnaissance.
* **Azure Security Center (Defender for Cloud):** Offers a unified view of security alerts and recommendations.
* **Azure Monitor / Sentinel:** Aggregates logs and allows custom queries/detections for enumeration activities.

**Indicators (Optional Logging):**

* **Specific Graph API queries:** Look for `/users/{id}/memberOf`, `/groups/{id}/members`, etc.
* **Large numbers of requests:** A sudden spike to Graph API endpoints suggests enumeration.
* **User agent strings:** Can reveal known SharpHound signatures (though attackers may spoof).
* **Unusual sign-in patterns:** Sign-ins from unknown locations or devices deviating from normal user behavior.
* **Excessive directory queries:** A high volume of *read*-based requests can indicate reconnaissance.
* **Changes to directory roles/groups:** Any unexpected role or group membership changes might indicate privilege escalation attempts.
* **Alerts from Azure ATP/Security Center/Sentinel:** Check these products for out-of-the-box or custom detection rules that spot enumeration behavior.

**Sample KQL for Detection:**

```
AuditLogs
| where OperationName has "Get-AzureADGroupMember"
| summarize count() by CallerIpAddress, UserDisplayName, TimeGenerated
| where count_ > 100
| render table
```

**Key Takeaways:**

* Default logging is limited. Enable diagnostic settings and centralize logs for better visibility.
* Detect enumeration via patterns of directory queries rather than a specific "BloodHound" signature.
* Graph API audit logs (when available) are your best bet for catching SharpHound usage.
* Correlate logs with other security signals (threat intel, endpoint alerts, etc.) for a fuller defense.

Also Read: [Forensic Lunch 1/10/25 with Ryatt Roesrma talking about fine tuning AI models](https://www.hecfblog.com/2025/01/daily-blog-714-forensic-lunch-11025.html)

#### Post a Comment

[Newer Post](https://www.hecfblog.com/2025/01/daily-blog-716-sunday-funday-11225.html "Newer Post")

[Older Post](https://www.hecfblog.com/2025/01/daily-blog-714-forensic-lunc...