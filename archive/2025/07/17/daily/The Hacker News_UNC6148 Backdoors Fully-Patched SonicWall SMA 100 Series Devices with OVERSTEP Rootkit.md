---
title: UNC6148 Backdoors Fully-Patched SonicWall SMA 100 Series Devices with OVERSTEP Rootkit
url: https://thehackernews.com/2025/07/unc6148-backdoors-fully-patched.html
source: The Hacker News
date: 2025-07-17
fetch_date: 2025-10-06T23:55:28.151882
---

# UNC6148 Backdoors Fully-Patched SonicWall SMA 100 Series Devices with OVERSTEP Rootkit

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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [UNC6148 Backdoors Fully-Patched SonicWall SMA 100 Series Devices with OVERSTEP Rootkit](https://thehackernews.com/2025/07/unc6148-backdoors-fully-patched.html)

**Jul 16, 2025**Ravie LakshmananVulnerability / Cyber Espionage

[![Hacking SonicWall SMA 100 Series Devices](data:image/png;base64... "Hacking SonicWall SMA 100 Series Devices")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiDteWJXj8rzKBMIKCi5ikfj2MUefFMEAniiLqXLvf7wWSWsYYusLRg1IbkCSIre2kBl1hJd3znVdgdTSOVYDFxSm2z41AS4MsJG2dBgQctj05q3OF9iFTsFqThrsrGRlCfGgYL_7jT-yEu3uVlElffovZI1KALMLH7mLIHfcYfJ92M8y3GNABN0klHWEDN/s790-rw-e365/sma.jpg)

A threat activity cluster has been observed targeting fully-patched [end-of-life](https://www.sonicwall.com/support/product-lifecycle-tables/Secure-Mobile-Access-100-Series/Hardware) SonicWall Secure Mobile Access (SMA) 100 series appliances as part of a campaign designed to drop a backdoor called **OVERSTEP**.

The malicious activity, dating back to at least October 2024, has been [attributed](https://cloud.google.com/blog/topics/threat-intelligence/sonicwall-secure-mobile-access-exploitation-overstep-backdoor) by the Google Threat Intelligence Group (GTIG) to a hacking crew it tracks as **UNC6148**. The number of known victims is "limited" at this stage.

The tech giant assessed with high confidence that the threat actor is "leveraging credentials and one-time password (OTP) seeds stolen during previous intrusions, allowing them to regain access even after organizations have applied security updates."

"Analysis of network traffic metadata records suggests that UNC6148 may have initially exfiltrated these credentials from the SMA appliance as early as January 2025."

The exact initial access vector used to deliver the malware is currently not known due to the steps taken by the threat actors to remove log entries. But it's believed that access may have been gained through the exploitation of known security flaws such as [CVE-2021-20035](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2021-0022), [CVE-2021-20038, CVE-2021-20039](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2021-0026), [CVE-2024-38475](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2024-0018), or [CVE-2025-32819](https://psirt.global.sonicwall.com/vuln-detail/snwlid-2025-0011).

Alternately, the tech giant's threat intelligence team theorized that the administrator credentials could've been obtained through information-stealing logs or acquired from credential marketplaces. However, it said it didn't find any evidence to back up this hypothesis.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Upon gaining access, the threat actors have been found to establish an SSL-VPN session and spawn a reverse shell, although how this was achieved remains a mystery given that shell access should not be possible by design on these appliances. It's believed that it may have been pulled off by means of a zero-day flaw.

The reverse shell is used to run reconnaissance and file manipulation commands, not to mention export and import settings to the SMA appliance, suggesting that UNC6148 may have altered an exported settings file offline to include new rules so that their operations are not interrupted or blocked by the access gateways.

The attacks culminate in the deployment of a previously undocumented implant named OVERSTEP that's capable of modifying the appliance's boot process to maintain persistent access, as well as credential theft and concealing its own components to evade detection by patching various file system-related functions.

This is achieved by implementing a usermode rootkit through the hijacked standard library functions open and readdir, allowing it to hide the artifacts associated with the attack. The malware also hooks into the write API function to receive commands from an attacker-controlled server in the form of embedded within web requests -

* **dobackshell**, which starts a reverse shell to the specified IP address and port
* **dopasswords**, which creates a TAR archive of the files /tmp/temp.db, /etc/EasyAccess/var/conf/persist.db, and /etc/EasyAccess/var/cert, and save it in the location "/usr/src/EasyAccess/www/htdocs/" so that it can be downloaded via a web browser

"UNC6148 modified the legitimate RC file '/etc/rc.d/rc.fwboot' to achieve persistence for OVERSTEP," GTIG said. "The changes meant that whenever the appliance was rebooted, the OVERSTEP binary would be loaded into the running file system on the appliance."

Once the deployment step is complete, the threat actor then proceeds to clear the system logs and reboots the firewall to activate the execution of the C-based backdoor. The malware also attempts to remove the command execution traces from different log files, including httpd.log, http\_request.log, and inotify.log.

"The actor's success in hiding their tracks is largely due to OVERSTEP's capability to selectively delete log entries [from the three log files]," Google said. "This anti-forensic measure, combined with a lack of shell history on disk, significantly reduces visibility into the actor's secondary objectives."

Google has evaluated with medium confidence that UNC6148 may have weaponized an unknown, zero-day remote code execution vulnerability to deploy OVERSTEP on targeted SonicWall SMA appliances. Furthermore, it's suspected that the operations are carried out with the intent to facilitate data theft and extortion operations, and even ransomware deployment.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

This connection stems from the fact that one of the organizations that was targeted by UNC6148 was posted on the data leak site operated by World Leaks, an extortion gang run by individuals previously associated with the Hunters International ransomware scheme. It's worth noting that Hunters International recently [shuttered](https://thehackernews.com/2025/07/weekly-recap-chrome-0-day-ivanti.html#:~:...