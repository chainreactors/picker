---
title: The Detection & Response Chronicles: Exploring Telegram Abuse
url: https://blog.nviso.eu/2025/12/16/the-detection-response-chronicles-exploring-telegram-abuse/
source: NVISO Labs
date: 2025-12-16
fetch_date: 2025-12-17T03:18:45.361451
---

# The Detection & Response Chronicles: Exploring Telegram Abuse

[Skip to content](#content)

[![NVISO Labs](https://blog.nviso.eu/wp-content/uploads/2022/12/cropped-abn-zcrj_400x400-1.png)](https://blog.nviso.eu/)

[NVISO Labs](https://blog.nviso.eu/)

Cyber security research, straight from the lab! 🐀

* [twitter](https://twitter.com/NVISO_Labs)
* [linkedin](https://www.linkedin.com/company/nviso-cyber)
* mail us
* [our company](https://www.nviso.eu)
* [SSO](https://blog.nviso.eu/wp-admin/edit.php)
* Search for:Search Button

Menu

* [All](https://blog.nviso.eu/)
* [Blue Team](https://blog.nviso.eu/category/blue-team/)
* [Cloud Security](https://blog.nviso.eu/category/cloud-security/)
  + [AWS](https://blog.nviso.eu/category/cloud-security/aws/)
  + [Azure](https://blog.nviso.eu/category/cloud-security/azure/)
  + [GCP](https://blog.nviso.eu/category/cloud-security/gcp/)
  + [Microsoft 365](https://blog.nviso.eu/category/cloud-security/microsoft-365/)
* [Awareness](https://blog.nviso.eu/category/awareness/)
* [Forensics](https://blog.nviso.eu/category/forensics/)
* Other
  + [Application Security](https://blog.nviso.eu/category/application-security/)
  + [IoT Security](https://blog.nviso.eu/category/iot-security/)
  + [Web Security](https://blog.nviso.eu/category/web-security/)
  + [Industrial Security](https://blog.nviso.eu/category/industrial-security/)
  + [Mobile Security](https://blog.nviso.eu/category/mobile-security/)
  + [Cyber Strategy](https://blog.nviso.eu/category/cyber-strategy/)
  + [Purple Team](https://blog.nviso.eu/category/purple-team/)
  + [Red Team](https://blog.nviso.eu/category/red-team/)
  + [Events](https://blog.nviso.eu/category/events/)

# The Detection & Response Chronicles: Exploring Telegram Abuse

[Efstratios Lontzetidis](https://blog.nviso.eu/author/efstratios-lontzetidis/ "Posts by Efstratios Lontzetidis")

[Cyber Threats](https://blog.nviso.eu/category/cyber-threats/), [Blue Team](https://blog.nviso.eu/category/blue-team/)

December 16, 2025December 16, 2025
11 Minutes

Adversaries utilizing popular messaging apps throughout different attack phases is nothing new. Telegram in particular has constantly been the subject of abuse by multiple threat actors, favored for its anonymity, accessibility, resilience, and operational advantages. Since the beginning of October 2025, NVISO’s Security Operations Center (SOC) has identified four distinct intrusion attempts involving the abuse of Telegram. These incidents prompted us to take a closer look at the various ways adversaries are leveraging Telegram for malicious activity and provide detection and hunting opportunities.

# Telegram’s Inner Workings

Telegram operates as a cloud-based messaging platform that supports encrypted communication, public and private channels, and a powerful Bot API often leveraged both legitimately and maliciously. Bots are created by registering with [@BotFather](https://core.telegram.org/bots/tutorial), which provides a unique API token enabling programmatic interaction with Telegram servers, while channels allow one-to-many broadcasting, where administrators can post messages to large audiences with granular access control, making them attractive for both coordination and command-and-control. Malware frequently abuses [Telegram’s Bot API](https://core.telegram.org/bots/api#available-methods) due to its reliability, anonymity, and ease of use, often hard-coding bot tokens or channel/chat IDs to interact with the platform through common endpoints such as:

* **/getMe**: To confirm the bot token is valid and retrieve bot identity metadata.
* **/sendMessage**: To exfiltrate text-based data such as system information or keylogs back to the attacker.
* **/sendDocument**: To upload files like screenshots, archives, or log files.
* **/getUpdates**: To poll the Telegram bot’s channel for commands sent by the attacker.
* **/getWebhookInfo**: To check whether a webhook is currently configured, which helps malware determine if the bot token is valid, whether another operator or security researcher has tampered with the bot, or whether updates are being delivered in the expected mode.
* **/deleteWebhook**: To switch the bot from webhook mode back to long-polling via **/getUpdates**, which is easier for malware authors to implement and does not require an exposed web server. Removing the webhook ensures the bot immediately begins receiving attacker commands through polling. **/deleteWebhook?drop\_pending\_updates=true** clears any stored or queued commands that may have accumulated, effectively wiping traces from the bot’s command history and ensuring the malware receives only fresh instructions from the attacker, which reduces noise, hinders analysis, and prevents defenders from seeing previously issued commands.

# Telegram Abuse Use Cases in Campaigns

This section covers different attack phases that involve abusing Telegram, supplemented by examples of recent campaigns.

## Client-Side Success Monitoring

### Lunar Spider Utilizes Telegram for Monitoring FakeCaptcha Victims

In our [previous blog](https://blog.nviso.eu/2025/10/01/lunar-spider-expands-their-web-via-fakecaptcha/), it was discussed how Lunar Spider utilizes Telegram for victim click monitoring on their FakeCaptcha panel delivering Latrodectus. The threat actor utilized JavaScript snippets to uniquely identify visitors and capture their browser information. Ultimately, the threat actors sent the information through Telegram’s **/sendMessage** API endpoint. In this case, the code executed client-side, meaning the browser of the victim performed the communication towards Telegram.

![](https://blog.nviso.eu/wp-content/uploads/2025/12/image-4.png)

TeleCaptcha’s Code Snippet.

## Host-Side Success Monitoring

### DeerStealer Infection Employs Telegram for Notification of Payload Execution

NVISO recently identified a campaign where DeerStealer was distributed by infected websites, masquerading as fake Google Chrome updates.

![](https://blog.nviso.eu/wp-content/uploads/2025/12/DeerStealer.png)

FakeUpdates DeerStealer Campaign Overview.

A trojanized WordPress [plugin](https://www.virustotal.com/gui/file/a656dde8714476da247bce1e04105f85eaf95570011360637dcfa8bb21ef0532) was commonly observed across the affected websites, named [“header-fix-tester”](https://wordpress.org/support/topic/header-fix-tester/), which injects an iframe of the domains `[statswpmy[.]com](https://urlscan.io/result/019ae231-e4fe-72be-a018-b2171f955e4f/)` or `[trackingmyadsas[.]com](https://urlscan.io/result/019aaa51-581b-71e1-8945-54b027fd4a69)`. The campaign started at least as early as September with multiple infected sites active at the time of writing the report.

![](https://blog.nviso.eu/wp-content/uploads/2025/12/image-7-1024x693.png)

Code Snippet from an [Infected Website](https://urlscan.io/result/019ab4d6-d654-7217-ad9c-8cb2d4691d89/dom/).

![](https://blog.nviso.eu/wp-content/uploads/2025/12/image-6.png)

Infected Sites with Header Fix Tester Plugin.

Visitors are lured into downloading Google Chrome updates in a ZIP format and running the included executable. The executable, [after a series of actions](https://app.any.run/tasks/dedd2534-f734-4814-a8d7-13ee92dc5823), loads the final DeerStealer payload using HijackLoader. DeerStealer, first analyzed by [CYFIRMA](https://www.cyfirma.com/research/deerstealer-malware-campaign-stealth-persistence-and-rootkit-like-capabilities/), is a multi-stage infostealer that uses deception, persistence mechanisms, signed binaries, and rootkit-like capabilities to evade detection while exfiltrating sensitive data from compromised systems.

![](https://blog.nviso.eu/wp-content/uploads/2025/12/image-15.png)

Execution [Chain](https://app.any.run/tasks/dedd2534-f734-4814-a8d7-13ee92dc5823) of the EXE file.

This campaign also has unique fingerprints of Telegram utilization. Specifically, a POST request to the **/sendMessage** endpoint via curl is used to send a message to a specific Telegram bot with text indicating actions of the [malware](ht...