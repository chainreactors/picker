---
title: Operation SkyCloak Deploys Tor-Enabled OpenSSH Backdoor Targeting Defense Sectors
url: https://thehackernews.com/2025/11/operation-skycloak-deploys-tor-enabled.html
source: The Hacker News
date: 2025-11-04
fetch_date: 2025-11-05T03:12:47.872183
---

# Operation SkyCloak Deploys Tor-Enabled OpenSSH Backdoor Targeting Defense Sectors

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjMQkm7Ao3yQkNVeqy3au4G4E34VWzSsT55GDPjHHGjbHksJqrJCyM1ChO1hB9WzaFzZcwNTn8fOLN8b3U599XinIlPZBBqNnwZYJFQD0i2dLVdAjszjU-a3Y0iLd5UHOg0H9-IFtS0nGf4MeOGk4NsNNAq-pMpFpi_aZrXHGV7UgoEEOlkFGBW5HOsJFC/s728-e100/zz--header-d.png)](https://thehackernews.uk/zz--header-d)

# [Operation SkyCloak Deploys Tor-Enabled OpenSSH Backdoor Targeting Defense Sectors](https://thehackernews.com/2025/11/operation-skycloak-deploys-tor-enabled.html)

**Nov 04, 2025**Ravie LakshmananMalware / Cyber Espionage

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj6ok6aAygeqft712J7YEd_aBpjlL3SNlIraKZ2za1SW5EEy9HaK6k9fvrr-9WQVO3mbummfoqwbXUg-gbcXAYakGZTCjG3B1q6ur-9JEDP-krL8iq2nv53HY-DTSWSQEdQf1VO2S0msbO2Jj5ict0EjSES6j7nPpgX1Qz5nnN540Gy5EAiwBxidEff3gWe/s790-rw-e365/russian.jpg)

Threat actors are leveraging weaponized attachments distributed via phishing emails to deliver malware likely targeting the defense sector in Russia and Belarus.

According to multiple reports from [Cyble](https://cyble.com/blog/weaponized-military-documents-deliver-backdoor/) and [Seqrite Labs](https://www.seqrite.com/blog/operation-skycloak-tor-campaign-targets-military-of-russia-belarus/), the campaign is designed to deploy a persistent backdoor on compromised hosts that uses OpenSSH in conjunction with a customized Tor hidden service that employs [obfs4](https://github.com/Yawning/obfs4) for traffic obfuscation.

The activity has been codenamed **Operation SkyCloak** by Seqrite, stating the phishing emails utilize lures related to military documents to convince recipients into opening a ZIP file containing a hidden folder with a second archive file, along with a Windows shortcut (LNK) file, which, when opened, triggers the multi-step infection chain.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/zz--inside-d)

"They trigger PowerShell commands which act as the initial dropper stage where another archive file besides the LNK is used to set up the entire chain," security researchers Sathwik Ram Prakki and Kartikkumar Jivani said, adding the archive files were uploaded from Belarus to the VirusTotal platform in October 2025.

One such intermediate module is a PowerShell stager that's responsible for running anti-analysis checks to evade sandbox environments, as well as writing a Tor onion address ("yuknkap4im65njr3tlprnpqwj4h7aal4hrn2tdieg75rpp6fx25hqbyd[.]onion" to a file named "hostname" in the "C:\Users\<Username>\AppData\Roaming\logicpro\socketExecutingLoggingIncrementalCompiler\" location.

As part of its analysis checks, the malware confirms that the number of recent LNK files present on the system is greater than or equal to 10 and verifies that the current process count exceeds or equals 50. If either of the conditions is not met, the PowerShell abruptly ceases execution.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg8Fafn0jnnaLZzBZGKyhycKgmVgTGUAYwDbCCrTZTKr81UdXg6HeFRD9gWmOj8KutJG_hRpObwxGB9Lx_w0Hzn8k3Twgyj8fdfkqqhjsgVoCmAv108OijuIEXfuI8ThCT_n5kGvTlYMxObWfe8667Yvhs5pWh34vRV3MoBITnMEPJ7TxCeXC6qiE-Tf3iv/s790-rw-e365/tor.jpg)

"These checks serve as environmental awareness mechanisms, as sandbox environments typically exhibit fewer user-generated shortcuts and reduced process activity compared to genuine user workstations," Cyble said.

Once these environmental checks are satisfied, the script proceeds to display a PDF decoy document stored in the aforementioned "logicpro" folder, while setting up persistence on the machine using a scheduled task under the name "githubdesktopMaintenance" that runs automatically after user logon and runs at regular intervals every day at 10:21 a.m. UTC.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhATy-g2vky5ZW29LPeol9gSbcKen84Xv9y7mwDCo22mI3voLxGRYrXHKr2sE3ZN9bQ3SDH4czy5xANg6R6kGTkcXtKKpad9pd3_jBVwNggjIQTBQGyuB3FwCIo5NuR1Wed9Fcb9S1U1HUXIRN0Z3wtPVog2yGYWVOgeDa1o-1DWynHNCrbySEnnd00DtBF/s790-rw-e365/zip.png)

The scheduled task is designed to launch "logicpro/githubdesktop.exe," which is nothing but a renamed version of "sshd.exe," a legitimate executable associated with OpenSSH for Windows," allowing the threat actor to establish an SSH service that restricts communications to pre-deployed authorized keys stored in the same "logicpro" folder.

Besides enabling file transfer capabilities using SFTP, the malware also creates a second scheduled task that's configured to execute "logicpro/pinterest.exe," a customized Tor binary used to create a hidden service that communicates with the attacker's .onion address by obfuscating the network traffic using obfs4. Furthermore, it implements port forwarding for multiple critical Windows services such as RDP, SSH, and SMB to facilitate access to system resources through the Tor network.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/endpoint-protect-d)

Once the connection is successfully established, the malware exfiltrates system information, in addition to a unique .onion URL hostname identifying the compromised system by means of a curl command. The threat actor ultimately gains remote access capabilities to the compromised system upon receipt of the victim's .onion URL through the command-and-control channel.

While it's currently not clear who is behind the campaign, both security vendors said it's consistent with Eastern European-linked espionage activity targeting defense and government sectors. Cyble has assessed with medium confidence that the attack shares tactical overlaps with a prior campaign mounted by a threat actor tracked by CERT-UA under the moniker [UAC-0125](https://thehackernews.com/2024/12/uac-0125-abuses-cloudflare-workers-to.html).

"Attackers access SSH, RDP, SFTP, and SMB via concealed Tor services, enabling full system control while preserving anonymity," the company added. "All communications are directed through anonymous addresses using pre-installed cryptographic keys."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more excl...