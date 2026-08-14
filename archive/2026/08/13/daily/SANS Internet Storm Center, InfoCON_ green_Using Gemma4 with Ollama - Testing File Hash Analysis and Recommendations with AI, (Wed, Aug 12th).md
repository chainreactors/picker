---
title: Using Gemma4 with Ollama - Testing File Hash Analysis and Recommendations with AI, (Wed, Aug 12th)
url: https://isc.sans.edu/diary/rss/33242
source: SANS Internet Storm Center, InfoCON: green
date: 2026-08-13
fetch_date: 2026-08-14T04:01:03.104047
---

# Using Gemma4 with Ollama - Testing File Hash Analysis and Recommendations with AI, (Wed, Aug 12th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Guy Bruneau](/handler_list.html#guy-bruneau "Guy Bruneau")

Threat Level: [green](/infocon.html)

* [previous](/diary/33240)

Click HERE to learn more about classes Guy is teaching for SANS

# [Using Gemma4 with Ollama - Testing File Hash Analysis and Recommendations with AI](/forums/diary/Using%2BGemma4%2Bwith%2BOllama%2BTesting%2BFile%2BHash%2BAnalysis%2Band%2BRecommendations%2Bwith%2BAI/33242/)

**Published**: 2026-08-12. **Last Updated**: 2026-08-13 01:26:53 UTC
**by** [Guy Bruneau](/handler_list.html#guy-bruneau) (Version: 1)

[0 comment(s)](/diary/Using%2BGemma4%2Bwith%2BOllama%2BTesting%2BFile%2BHash%2BAnalysis%2Band%2BRecommendations%2Bwith%2BAI/33242/#comments)

In the past few weeks, I have been using Gemma4 as a Large Language Model (LLM) to see how useful it can be to analyze some of the malware hashes uploaded to the DShield sensor over the past 30 days and figure out how its recommendation can be considered useful about the activity my DShield sensor is collecting and tracking. The model I use for this testing is gemma4:e4b [[2](https://ollama.com/library/gemma4)] using two sites to compare the data against [VirusTotal](https://www.virustotal.com/) and [CyberGordon](https://cybergordon.com/).

The following questions were submitted to Gemma for information:

**Instructions:**

1. Determine if we should be concerned with the volumes or suspicious volumes match indicators of compromise (IoC) or tactics mentioned on the two external websites.
2. Provide a concise comparative analysis and recommendations for action to prevent actors/bots to successfully compromise the sensor.
3. Identify what type of malware family (Popular threat label) the top 3 files are associated with.
4. Highlight potential issues with the top 3 inbound hashes (files) downloaded by actors/bots logged in the sensor and which sites have the most information about this activity.

**Result from the LLM Analysis**

Comparative analysis from Gemma 4 :
 As a cybersecurity analyst, I have analyzed the provided data stream concerning files downloaded by actors/bots to the Cowrie sensors.

**Analysis of Downloaded Hashes** (Top 10 IoCs)

![](https://isc.sans.edu/diaryimages/images/gemma_hashes.png)

**Findings and Analysis**

1. **Volume vs. IoCs vs. Tactics**
The sheer volume of these hashes (126, 110 events) is a major concern. High volumes do not automatically confirm malicious intent, but when coupled with the fact that they are \*downloaded\* from an interactive sensor like Cowrie, it indicates successful actor persistence and data exfiltration attempts.

**Indicators/Tactics**

Indicator of Compromise (IoC): The hashes themselves act as IoCs if they resolve to known malware families or C2 infrastructure components. Since the external sites provided no results, the focus must be on the \*behavior\*—the repeated transfer of these files.
Tactics (MITRE ATT&CK): This activity strongly suggests \*\*Persistence\*\*, \*\*Command and Control (C2)\*\* communication, and potentially \*\*Lateral Movement/Exfiltration\*\*. The actors are not merely querying the system; they are downloading specific files repeatedly.

2. **Comparative Analysis & Recommendations**

| Aspect | VirusTotal (VT) | CyberGordon (CG) | Conclusion / Action Recommendation |
| :--- | :--- | :--- | :--- |
| Data Depth | High-fidelity, integrated threat intelligence from multiple sources (AV engines). Best for direct identification. | Academic/Historical analysis engine. Useful for deep source tracking and niche observations. | VT is superior for immediate threat context; CG offers supporting research. |
| Reliability | Generally reliable, though sometimes slow or requires paid access for full fidelity. | Utility appears high but the provided output is generic (focusing on JS compatibility rather than results). | \*\*Rely primarily on VT/Commercial Threat Feeds.\*\* Do not treat lack of a result as "safe." |
| Missing Data | The provided snippet was boilerplate ("Please enable JavaScript"), meaning we missed vital IoC intelligence. | The provided snippet was generic browser/engine advice, offering no actionable threat intel. | \*\*Critical Action:\*\* Develop a structured workflow to \*ensure\* the results page is fully processed and captured for all 10 hashes. |

**Recommendations for Action** (Preventing Compromise):

1.  Immediate Containment: Treat any machine connected through this sensor as compromised. Isolate the host and initiate forensic imaging immediately.
2.  Mitigation at Sensor Level: Update Cowrie's logging and alerting capabilities to track file \*execution\* attempts, not just downloads. Implement stricter egress filtering on the network hosting the sensors.
3.  Threat Hunting (Proactive): Utilize the Top 10 hashes to query internal Endpoint Detection and Response (EDR) solutions across the entire enterprise, searching for the hash signatures or file names appearing on any system \*outside\* of the sensor environment.
4.  Hardening: Review user access policies and network segmentation rules. The repeated downloading suggests a persistent gap in perimeter controls.

3.**Associated Malware Family** (Top 3 Hashes)

Since no specific threat intelligence results were provided for these hashes, this analysis is based on the pattern of high-volume command-and-control behavior.

1.  197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8: \*\*Botnet/Loader Malware.\*\* The extremely high event count and consistent downloading pattern are classic indicators of a payload being repeatedly delivered, likely by an established botnet or initial access Trojan (RAT).
2.  31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e: \*\*Backdoor/Keylogger.\*\* Similar to the top hash, but potentially representing a specific piece of payload used for data exfiltration (like credentials or session tokens).
3.  94f2e4d8d4436874785cd14e6e6d403507b8750852f7f2040352069a75da4c00: \*\*Credential Stealer/Dropper.\*\* This hash may represent a modular component or a staged payload, designed to "drop" the final malware onto the compromised system after initial access.

4. **Potential Issues with Top 3 Hashes & Best Data Source**

Potential Issue Highlight (Focusing on Behavioral Risk)

The primary issue is not necessarily what the hashes \*are\*, but that they are actively being \*downloaded\* repeatedly by a controlled actor over a sustained period (Top 10). This behavior confirms \*\*successful compromise and established persistence\*\*. The actors have successfully identified data pathways to download their chosen payloads, bypassing existing security controls.

**Comparison of Sites for Top 3**

Given the critical nature of these files:

VirusTotal (VT): Is the preferred source. Despite the provided boilerplate text, VT's strength lies in its aggregation of multiple vendor signatures (AV engines). It provides the highest likelihood of a quick determination whether the hash is \*known malicious\*.
CyberGordon (CG): Is useful as a secondary research source or for understanding the historical context of the observed payload type. Its data output, based on observation and academic logging, might reveal more about \*how\* the file was used in previous compromises, which is valuable for threat hunting.

**Conclusion**

The most reliable actionable intelligence will be obtained by re-querying both sites multiple times to ensure 100% capture of the IoC data. However, \*\*VT provides the immediate signature risk assessment.\*\*

My own conclusion: I think the information provided by Gemma is a nice summary as long as the right tools (sites) are provided that can be used to gather additional information to use to better answer the questions initially asked in the instructions.

The python script used for this test is available [here](https://github.com/bruneaug/DShield-SIEM/tree/main/Ollama).

[1] https://en.wikipedia....