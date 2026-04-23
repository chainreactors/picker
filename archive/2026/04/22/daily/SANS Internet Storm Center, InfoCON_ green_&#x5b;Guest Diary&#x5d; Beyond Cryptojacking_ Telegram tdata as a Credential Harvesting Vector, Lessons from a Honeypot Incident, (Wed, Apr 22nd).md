---
title: &#x5b;Guest Diary&#x5d; Beyond Cryptojacking: Telegram tdata as a Credential Harvesting Vector, Lessons from a Honeypot Incident, (Wed, Apr 22nd)
url: https://isc.sans.edu/diary/rss/32888
source: SANS Internet Storm Center, InfoCON: green
date: 2026-04-22
fetch_date: 2026-04-23T04:45:14.077406
---

# &#x5b;Guest Diary&#x5d; Beyond Cryptojacking: Telegram tdata as a Credential Harvesting Vector, Lessons from a Honeypot Incident, (Wed, Apr 22nd)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Jesse La Grew](/handler_list.html#jesse-la-grew "Jesse La Grew")

Threat Level: [green](/infocon.html)

* [previous](/diary/32886)
* [next](/diary/32892)

Click HERE to learn more about classes Jesse is teaching for SANS

# [[Guest Diary] Beyond Cryptojacking: Telegram tdata as a Credential Harvesting Vector, Lessons from a Honeypot Incident](/forums/diary/Guest%2BDiary%2BBeyond%2BCryptojacking%2BTelegram%2Btdata%2Bas%2Ba%2BCredential%2BHarvesting%2BVector%2BLessons%2Bfrom%2Ba%2BHoneypot%2BIncident/32888/)

**Published**: 2026-04-22. **Last Updated**: 2026-04-22 00:03:04 UTC
**by** [L. Carty, SANS.edu BACS Student](/handler_list.html#l.-carty,-sans.edu-bacs-student) (Version: 1)

[0 comment(s)](/diary/Guest%2BDiary%2BBeyond%2BCryptojacking%2BTelegram%2Btdata%2Bas%2Ba%2BCredential%2BHarvesting%2BVector%2BLessons%2Bfrom%2Ba%2BHoneypot%2BIncident/32888/#comments)

[This is a Guest Diary by L. Carty, an ISC intern as part of the SANS.edu Bachelor's Degree in Applied Cybersecurity (BACS) program [1].]

## Introduction

A few weeks ago, my honeypot logged an incident that changed how I think about modern attacks. A threat actor broke into my system using weak SSH credentials and immediately started running commands. What started as a routine resource-hijacking attempt was followed by credential harvesting targeting Telegram Desktop session data.

This incident isn't just another story about cryptocurrency mining malware. It's a window into how modern threat actors are evolving their tactics - chaining initial access with credential theft to enable persistent, multi-layered exploitation. The commands I observed tell a story of methodical reconnaissance, from checking for competing miners to hunting for Telegram's tdata directory.

In this post, I'll walk through what I found, explain why the **`tdata`** folder is so valuable to threat actors, and share practical ways to protect it and manage your sessions.

## The Attack Chain: A Conceptual Overview

Before diving into the actual commands, let's establish what we're looking at. Modern attacks rarely consist of a single malicious action and instead follow a progression. Below is the attack chain and corresponding MITRE ATT&CK Techniques. [2]

1. **Initial Access** – Weak SSH credentials, phishing, or vulnerabilities [/T1110/001/](https://attack.mitre.org/techniques/T1110/001/)
2. **Reconnaissance** – System enumeration, identifying valuable targets [/T1082/](https://attack.mitre.org/techniques/T1082/) [/T1083/](https://attack.mitre.org/techniques/T1083/)
3. **Credential Harvesting** – Extracting session tokens, passwords, or authentication data [/T1555/](https://attack.mitre.org/techniques/T1555/) [/T1005/](https://attack.mitre.org/techniques/T1005/)
4. **Account Takeover** – Using stolen credentials for further access [/T1078/](https://attack.mitre.org/techniques/T1078/)
5. **Exploitation** – Social engineering, lateral movement, or monetization [/T1041/](https://attack.mitre.org/techniques/T1041/)

What made this particular attack notable was the explicit targeting of Telegram's local session data. Threat actors aren't just after CPU cycles anymore—they're after persistent access through compromised accounts that can be leveraged for ongoing exploitation.

## The Evidence: Live from the Honeypot

The following commands were captured in the honeypot's SSH logs immediately after the threat actor gained access. They show the threat actor’s intent to map the system, check for competition, and locate the **`tdata`** directory.

### Commands Captured

* `/ip cloud print`
* `ifconfig`
* `uname -a cat /proc/cpuinfo #looks to have an issue with cloudflare`
* `ps | grep '[Mm]iner' ps -ef | grep '[Mm]iner'`
* `ls -la ~/.local/share/TelegramDesktop/tdata /home/*/.local/share/TelegramDesktop/tdata /dev/ttyGSM* /dev/ttyUSB-mod* /var/spool/sms/* /var/log/smsd.log /etc/smsd.conf* /usr/bin/qmuxd /var/qmux_connect_socket /etc/config/simman /dev/modem* /var/config/sms/*`
* `locate D877F783D5D3EF8Cs`
* `echo Hi | cat -n`

### A Command Timeline Visualization

`[Initial SSH Access]
         |
_________V_________________________________________________________
| RECONNAISSANCE PHASE                                            |
| • /ip cloud print → MikroTik RouterOS status,configuration      |
| • ifconfig → Network interface enumeration                      |
| • uname -a → OS/kernel identification                           |
| • cat /proc/cpuinfo → Hardware capability assessment            |
___________________________________________________________________
         |
_________V_________________________________________________________
| MINER DETECTION                                                 |
| • ps | grep '[Mm]iner' → Check for competing miners             |
| • ps -ef | grep... → Full process list scan                     |
__________________________________________________________________
         |
_________V_________________________________________________________
| CREDENTIAL HARVESTING                                           |
| • ls -la .../tdata → Locate Telegram session directory          |
| • /home/*/... → Wildcard search for user accounts               |
| • /dev/ttyGSM*, etc. → Modem/SMS 2FA bypass attempts            |
___________________________________________________________________
         |
_________V_________________________________________________________
| EXFILTRATION PREPARATION                                        |
| • locate D877F783... → Specific tdata folder lookup             |
| • echo Hi | cat -n → Shell verification                         |
| • [Compress & upload] → Likely next step (not captured)         |
__________________________________________________________________`

### Operational Context: Connecting the Dots

While the timeline shows what happened, understanding the why requires looking at the attack from a strategic view. Each command serves a specific purpose in a larger plan.

The initial reconnaissance (**`ifconfig, uname -a`**) was an attempt to confirm the system had the processing power to support a cryptominer and the network connectivity to send data out. Next came the miner detection phase (**`ps | grep`**). If the threat actor found an existing miner, they would need to remove those processes to free up resources and avoid conflicts before installing their own.

The next set of commands gets interesting as the threat actor shifts focus to Telegram Desktop **`tdata`**. This move reveals that stealing CPU cycles is a short-term gain, whereas stealing the Telegram session is a long-term asset. The threat actor searched for modem devices and SMS logs to get around the victim's two-factor authentication (2FA). This ensured that even if the stolen session stopped working, the threat actor could still reset the account password via SMS to take full control. This shows a clear shift from just using someone's computer for a quick profit to stealing their digital identity for long-term use.

## Deep Dive: The Critical Risk of tdata Exposure

Understanding why the **`tdata`** folder is so valuable is essential for defense. This directory contains the session data that authenticates the user to Telegram's servers.

### The Mechanics of Session Theft

According to an Imperva Threat Research report from 2025 regarding the sale of Telegram identities [3], copying the tdata folder to another machine grants a threat actor **full access to the victim's Telegram account without needing the phone number or two-factor authentication code**.

The session information stored in **`tdata`** acts as persistent login credentials. Because the authentication tokens are self-contained within the folder, the threat actor doesn't need to re-authenticate or bypass 2FA. They simply need to move the folder to a machine where they can run Telegram.

This flexibility is what makes the attack s...