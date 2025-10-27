---
title: Researchers Uncover Custom Backdoors and Spying Tools Used by Polonium Hackers
url: https://thehackernews.com/2022/10/researchers-uncover-custom-backdoors.html
source: The Hacker News
date: 2022-10-14
fetch_date: 2025-10-03T19:53:23.876922
---

# Researchers Uncover Custom Backdoors and Spying Tools Used by Polonium Hackers

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

# [Researchers Uncover Custom Backdoors and Spying Tools Used by Polonium Hackers](https://thehackernews.com/2022/10/researchers-uncover-custom-backdoors.html)

**Oct 13, 2022**Ravie Lakshmanan

[![Polonium Hackers](data:image/png;base64... "Polonium Hackers")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiBgmXCpgiSBakIaqgkrYaph9kagWeoYBUpMjW8QzIWv_JQo8aFwx__C1_c3483veSIhWjhlQ_ZANvT8LT1TX-GDmuP-Xq9_bldi8yn56ZsxnHtzeGlF1TF5AcFKQAsRY137ErdsbctczjbV1CROoBXNRUR04PPEswkDJfT7-A9lVlQUyPhwBxF5Z6V/s790-rw-e365/hacker.jpg)

A threat actor tracked as Polonium has been linked to over a dozen highly targeted attacks aimed at Israelian entities with seven different custom backdoors since at least September 2021.

The intrusions were aimed at organizations in various verticals, such as engineering, information technology, law, communications, branding and marketing, media, insurance, and social services, cybersecurity firm ESET said.

[Polonium](https://thehackernews.com/2022/06/microsoft-blocks-iran-linked-lebanese.html) is the chemical element-themed moniker given by Microsoft to a sophisticated operational group that's believed to be based in Lebanon and is known to exclusively strike Israeli targets.

Activities undertaken by the group first came to light earlier this June when the Windows maker disclosed it suspended more than 20 malicious OneDrive accounts created by the adversary for command-and-control (C2) purposes.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Core to the attacks has been the use of implants coined CreepyDrive and CreepyBox for their ability to exfiltrate sensitive data to actor-controlled OneDrive and Dropbox accounts. Also deployed is a PowerShell backdoor dubbed CreepySnail.

ESET's latest discovery of five more previously undocumented backdoors brings into focus an active espionage-oriented threat actor that's constantly refining and retooling its malware arsenal.

[![Polonium Hackers](data:image/png;base64... "Polonium Hackers")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEinjbrz1feZ1mOYUQLA9eoE1-0_UPnKTSCRSuSxi33uTpRbIM0jHIBPfpCbo1TEFutdr4pE9mUa9PEDUK62y8VH43Onyq_2K_7ZqQgbIBokpvEOAMA1_trieRT0sziL8fshD7C6bPiVwLbyNHUSxms7TtBV7m0XvRpbvRX-4K5RWh4NLjBsL4w3gFwD/s790-rw-e365/spying-tool.jpg)

"The numerous versions and changes Polonium introduced into its custom tools show a continuous and long-term effort to spy on the group's targets," ESET researcher Matías Porolli [said](https://www.welivesecurity.com/2022/10/11/polonium-targets-israel-creepy-malware/). "The group doesn't seem to engage in any sabotage or ransomware actions."

The list of bespoke hacking tools is as follows -

* **CreepyDrive/CreepyBox** - A PowerShell backdoor that reads and executes commands from a text file stored on OneDrive or Dropbox.
* **CreepySnail** - A PowerShell backdoor that receives commands from the attacker's own C2 server
* **DeepCreep** - A C# backdoor that reads commands from a text file stored in Dropbox accounts and exfiltrates data
* **MegaCreep** - A C# backdoor that reads commands from a text file stored in Mega cloud storage service
* **FlipCreep** - A C# backdoor that reads commands from a text file stored in an FTP server and exfiltrates data
* **TechnoCreep** - A C# backdoor that communicates with the C2 server via TCP sockets to execute commands and exfiltrate data
* **PapaCreep** - A C++ backdoor that can receive and execute commands from a remote server via TCP sockets

PapaCreep, spotted as recently as September 2022, is a modular malware that contains four different components that are designed to run commands, receive and send commands and their outputs, and upload and download files.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The Slovak cybersecurity firm said it also uncovered several other modules responsible for logging keystrokes, capturing screenshots, taking photos via webcam, and establishing a reverse shell on the compromised machine.

[![Polonium Hackers](data:image/png;base64... "Polonium Hackers")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj_G2xCaRWQsdodeps-0xkG3hHj5n5yCg1vU5f4n55zCZY-h-OgtrYPj03qcZYZGu9a-saKONiFsjoXiXQ0GPBC3EfxDJZZ1I4UyArpYe_OKTNXXb6U-L_D-KP0cIVEtjTo5pO3CQtrbyPMCrbtp-Yf1XdbZxVWDf63VF7cezfJwv9eI35xh7uhd4zn/s790-rw-e365/data.jpg)

Despite the abundance of malware utilized in the attacks, the initial access vector used to breach the networks is currently unknown, although it's suspected that it may have involved the exploitation of VPN flaws.

"Most of the group's malicious modules are small, with limited functionality," Porolli [said](https://www.eset.com/int/about/newsroom/press-releases/research/iran-affiliated-apt-group-polonium-targets-israel-with-creepy-backdoors-and-abuses-popular-cloud-ser/). "They like to divide the code in their backdoors, distributing malicious functionality into various small DLLs, perhaps expecting that defenders or researchers will not observe the complete attack chain."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[ESET](https://thehackernews....