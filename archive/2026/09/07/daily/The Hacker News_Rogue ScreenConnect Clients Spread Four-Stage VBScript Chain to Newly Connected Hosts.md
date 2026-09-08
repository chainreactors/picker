---
title: Rogue ScreenConnect Clients Spread Four-Stage VBScript Chain to Newly Connected Hosts
url: https://thehackernews.com/2026/09/rogue-screenconnect-clients-spread-four.html
source: The Hacker News
date: 2026-09-07
fetch_date: 2026-09-08T06:42:26.835238
---

# Rogue ScreenConnect Clients Spread Four-Stage VBScript Chain to Newly Connected Hosts

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [Rogue ScreenConnect Clients Spread Four-Stage VBScript Chain to Newly Connected Hosts](https://thehackernews.com/2026/09/rogue-screenconnect-clients-spread-four.html)

**Ravie Lakshmanan**Sep 07, 2026Malware / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiWA_nxvqJuKkqq0ab1I-XR1YtpsM6BadhHDNOIheZmBflLWaQ018JFJsAUBVuyWWTYI4pyT8OQNXhui8Annde3SnOIScH9B0ohMq-OzXLjvPeAXQnz4mAUdEMS_07i7gLaWqPVpHaPvyLJdZQKUTs2MLGhjB9UZ0A83CGcSeDCJFKn7hNjiyf6dbzbHogp/s1700-nu-rw-lo-l85-e365/screen.jpg)

Cybersecurity researchers have disclosed details of worm-like activity that abuses ConnectWise ScreenConnect to distribute a malicious Visual Basic Script (VBScript) payload to newly connected systems.

According to [Huntress](https://www.huntress.com/blog/rogue-screenconnect-installations), three unrelated incidents have been found to use diverse initial access methods, namely a Quick Assist tech-support scam, a phishing-delivered MSI installer, and a fake Geek Squad refund form lure, to activate a four-stage VBScript chain that leads to rogue ScreenConnect installations.

However, once the ScreenConnect instances were installed, the cybersecurity company said it observed the clients repeatedly spawning "wscript.exe" to execute VBScripts named 1.vbs, 2.vbs, 3.vbs, and 4.vbs. The incidents were observed in August 2026.

The details of the three attacks are below -

* A social engineering attack that persuaded a user into executing Quick Assist as part of a tech support scam, after which a rogue ScreenConnect remote access client was deployed to contact a command-and-control (C2) server located at "45.13.237[.]190" ("tele-sync.opik[.]net"). Hosted on the IP address is a RAR archive containing the four VBS files.
* An MSI installer ("ScreenConnect.ClientSetup.msi") likely delivered via a phishing attack that deployed a ScreenConnect client configured to communicate with "131.123.40[.]98" on port 8041. The rogue ScreenConnect almost immediately launched the four VBScript files from the ScreenConnect temporary directory.
* A search for a Geek Squad refund form led to the deployment of a rogue ScreenConnect client ("ScreenConnect.Client.exe"), which then connected to "borertors92.anondns[.]net." The session then uses "wscript.exe" to execute the four VBS scripts from the Temp folder.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/trust-world-update-d)

Across these incidents, the attack sequence is said to have followed a four-step process, with each VBScript launching the next and allowing it to progress further -

* **1.vbs**, which profiles the host, checks system resources (e.g., if RAM is over 5 GB), verifies if ScreenConnect is installed, enumerates security products, including Cisco AMP, CrowdStrike, Huntress, Malwarebytes, SentinelOne, Sophos, and Symantec Endpoint Protection, and writes the results of these checks to "%TEMP%\value.txt" in the form a three-bit state variable. For example, the state value "000" indicates no existing ScreenConnect installation, the presence of third-party security processes, and no ScreenConnect clients are installed within the Program Files folder.
* **2.vbs**, which waits for the "%TEMP%\value.txt" file and checks for the presence of the word "abort." If the word does not exist, it downloads a file from Dropbox, decodes its contents, and writes them to "%TEMP%\map.txt." While the text file contents are not executed, the exact nature of the payload retrieved is unclear, as the Dropbox URL is no longer online as of September 2, 2026.
* **3.vbs**, which works similarly to 2.vbs by waiting for "%TEMP%\map.txt" and then proceeds to download the relevant file from the Dropbox link specified in the text file based on the state values set by 1.vbs in "%TEMP%\value.txt" and writes it to "%TEMP%\out.enc."
* **4.vbs**, which waits for the presence of the downloaded "%TEMP%\out.enc" payload and launches a PowerShell script ("%TEMP%\runner.ps1") to decrypt the contents of "%TEMP%\out.enc," write them to "%APPDATA%\Microsoft\Windows\Templates\Classic\sys\_cache.zip," and execute a second-stage PowerShell script ("PyTorchFix.ps1").

At least three different payloads have been detected based on the state value -

* **000** and **001** lead to a user-level ScreenConnect backdoor
* **010** leads to tooling for privilege escalation via a User Account Control ([UAC](https://www.elastic.co/security-labs/threat-command/exploring-windows-uac-bypasses-techniques-and-detection-strategies)) bypass and persistence
* **011** leads to tunneling utilities and a cryptocurrency miner

In addition, "%TEMP%\runner.ps1" takes steps to terminate every "wscript.exe" or "cscript.exe" process, and deletes the staging directory after the final stage is run. The 4.vbs script also writes the four VBScript files to "C:\Users\Public\Libraries\Default\Lib\Lib1" if the value in "%TEMP%\value.txt" is set to 010 or 011.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEibe_tLFJz0oDEAS_WWcbpJjeh5IzzPN2GHyXFTkExOdXBEDkBbNYchcvRZeEatXmNkiSy3FqBhBF2be0mMa5g4rr7RzzGV24mpQ9xcVmaRHhYwmIlzaRWzbYMCu3oyXTiJzDLOMr8LP3UZHg7Ak4bSTZY1jwjxpTOTyE2t5W8vtLLv6bq18mwB3VVEZBsp/s1700-nu-rw-lo-l85-e365/huntress.jpg)

This, in turn, triggers a round of payload deliveries, effectively turning the compromised host into a content-delivery mechanism for the malicious scripts every time the backdoored client observes a new Host connection.

"This creates a worm-like behavior: propagating infections over new ScreenConnect connections. Connecting to an infected ScreenConnect client can cause the server-side Host system to receive and execute the same four-stage VBScript chain," Huntress said. "Later, the client records each ConnectionID to avoid repeatedly targeting the same active session, but then removes that identifier after it disconnects – allowing a later reconnection to trigger the infection again."

"The incidents...