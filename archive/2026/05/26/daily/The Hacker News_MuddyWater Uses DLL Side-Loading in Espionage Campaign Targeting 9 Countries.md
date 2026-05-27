---
title: MuddyWater Uses DLL Side-Loading in Espionage Campaign Targeting 9 Countries
url: https://thehackernews.com/2026/05/muddywater-uses-dll-side-loading-in.html
source: The Hacker News
date: 2026-05-26
fetch_date: 2026-05-27T06:12:48.821106
---

# MuddyWater Uses DLL Side-Loading in Espionage Campaign Targeting 9 Countries

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyqUz0-ifa8jE9rCzud3wzxmhcuzTp1VOWFEvGMoZXDYfaB_4459fPyvyQw7wvAnzjzDL09PkyJM83QGheO69fC3esg1WA7WnJ89i_t_q3K8DxYmgV__QujU8RWRnCK4MpbKqu8nwuMFfLaiRVHy_ov7IZ16hoKI3rIu-5BcISmqXPjlQU7N0sa4lWI-n-/s728-e100/wiz-d.png)](https://thehackernews.uk/wiz-ai-state-d)

# [MuddyWater Uses DLL Side-Loading in Espionage Campaign Targeting 9 Countries](https://thehackernews.com/2026/05/muddywater-uses-dll-side-loading-in.html)

**Ravie Lakshmanan**May 26, 2026Cyber Espionage / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgkb692n4xA8jDUKZCkwPSIXqiyTaEk_bQhrNaZj33tRhusSP40-iwlk5x7iblb9M63WKWVbj8Gm6oPJZY3bm602-qFyLLnRXuCKsl40iAZG_5-ehqlQ4CYaO442hgo4FBKrspLCO4r_ET1U4U3fPCKCYOc7DFuDn_mv7ZzbzH_IC0NAt2HVVSxwIBNOruk/s1700-e365/cyber-espionage.jpg)

The Iranian hacking group known as **[MuddyWater](https://thehackernews.com/2026/05/muddywater-uses-microsoft-teams-to.html)** has been linked to a new campaign affecting at least nine organizations across nine countries on four continents in the first quarter of 2026.

The activity targeted industrial and electronics manufacturing, education and public-sector bodies, financial services, and professional services, per the Threat Hunter Team from Symantec and Carbon Black. Among the victims is a major South Korean electronics manufacturer, with the attackers spending a week inside its network in February 2026.

Also singled as part of the sprawling espionage effort were an international airport in the Middle East, Southeast Asian industrial manufacturers, and a Latin American financial-services provider.

"The attackers relied heavily on DLL side-loading using legitimately signed Fortemedia (fmapp.exe) and SentinelOne (sentinelmemoryscanner.exe) binaries to execute malicious DLLs while masquerading as benign software," Broadcom's cybersecurity teams [said](https://www.security.com/threat-intelligence/iran-seedworm-electronics).

The use of "fmapp.exe" to sideload "fmapp.dll" was previously documented by Group-IB in connection with another MuddyWater campaign codenamed [Operation Olalampo](https://thehackernews.com/2026/02/muddywater-targets-mena-organizations.html). According to [Huntress](https://www.huntress.com/blog/muddywater-attack-chain), the DLL contains code to connect to an attacker-controlled IP address ("157.20.182[.]49").

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlabz-vpn-risk-2026-d)

On the other hand, the abuse of "sentinelmemoryscanner.exe" - a binary associated with a security product - is assessed to be a deliberate choice, as it can bypass signature-based detection. It's designed to sideload a rogue DLL named "sentinelagentcore.dll."

Both the DLLs embed an open-source tool called [ChromElevator](https://github.com/xaitax/Chrome-App-Bound-Encryption-Decryption) to siphon passwords, cookies, and payment card data from Chromium-based browsers, effectively getting around App-Bound Encryption ([ABE](https://thehackernews.com/2024/08/google-chrome-adds-app-bound-encryption.html)) protections.

A noteworthy aspect of the attacks is the use of Node.js scripts to launch PowerShell code responsible for carrying out discovery and information gathering operations. In at least one instance, the attackers have been found to stage the stolen data on sendit[.]sh, a public file-transfer service.

"A node.exe-based implant chain was used to drop PowerShell scripts that performed reconnaissance, screenshot capture, SAM hive theft, privilege escalation, and SOCKS5 reverse-proxy tunnelling," Symantec and Carbon Black said.

Also delivered are the two aforementioned DLL side-loading pairs to provide attackers with a covert tunnel to relay traffic and launch **ChromElevator**. The attacks are also characterized by efforts to dump credentials that would allow them to move laterally across the networks.

In the intrusion targeting the South Korean electronics manufacturer, MuddyWater is believed to have repeatedly carried out PowerShell-based reconnaissance, as well as re-execute the two binaries to ensure it retains access to the compromised host. The initial access vector used to breach the organization is unknown.

"The cadence is again consistent with implant-driven activity rather than continuous operator presence," the researchers said. "Its campaign history shows a clear move towards quieter, more disciplined operations. None of these techniques is individually novel, but in combination they provide more evidence of a significant step up in operational hygiene from the Seedworm that we knew of two or three years ago."

The development comes as the European Council [imposed](https://www.consilium.europa.eu/en/press/press-releases/2026/03/16/cyber-attacks-against-the-eu-and-its-member-states-council-sanctions-three-entities-and-two-individuals/) sanctions against Iranian company Emennet Pasargad for hacking a Swedish SMS service, accessing the contents of a French subscriber database and putting it up for sale, and for spreading disinformation via compromised advertising billboards during the 2024 Paris Olympic Games.

The company, per the U.S. State Department, goes by the name Shahid Shushtari and is affiliated with Iran's Islamic Revolutionary Guard Corps Cyber-Electronic Command (IRGC-CEC). It's tracked under the monikers Cobalt Obelisk, Cotton Sandstorm, Haywire Kitten (formerly ChaoticOrchestra), Marnanbridge, and UNC5866.

"Shahid Shushtari members have caused significant financial damage and disruption to U.S. businesses and government agencies through coordinated cyber and cyber-enabled information operations," the State Department [noted](https://thehackernews.com/2025/12/weekly-recap-usb-malware-react2shell.html#:~:text=U%2ES%2E%20State%20Department%20Offers%20%2410m%20Reward%20for%20Iranian%20Hacker%20Duo) in December 2025. "These campaigns have targeted multiple critical infrastructure sectors, including news, shipping, travel, energy, financial, and telecommunications in the United States, Europe, and the Middle East."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

Iran-backed hackers have also been tied to an exfiltration campaign aimed at organizations in the U.S., Israel, Saudi Arabia...