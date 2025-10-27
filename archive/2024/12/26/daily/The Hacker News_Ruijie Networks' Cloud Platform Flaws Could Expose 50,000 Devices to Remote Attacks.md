---
title: Ruijie Networks' Cloud Platform Flaws Could Expose 50,000 Devices to Remote Attacks
url: https://thehackernews.com/2024/12/ruijie-networks-cloud-platform-flaws.html
source: The Hacker News
date: 2024-12-26
fetch_date: 2025-10-06T19:40:12.421175
---

# Ruijie Networks' Cloud Platform Flaws Could Expose 50,000 Devices to Remote Attacks

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

# [Ruijie Networks' Cloud Platform Flaws Could've Exposed 50,000 Devices to Remote Attacks](https://thehackernews.com/2024/12/ruijie-networks-cloud-platform-flaws.html)

**Dec 25, 2024**Ravie LakshmananCloud Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj4nLqT0UlQ1hS2pWjtqKTAliPXimWqJuI3ExBa3pY8lmRLMYdkbpSIpNl3dW32-1BswViwAt8y7r04nTaEPiWkwkYqTKcX77E1sczxiJY_VtuI8aLf_-EZHHwr7ZV9g-1bHlXeigzb7P-feUBM2EKyqL7YOHAxtnXoXBi-nN1QWlk5koo4KhhAFc2ZPkyp/s790-rw-e365/hackers.png)

Cybersecurity researchers have discovered several security flaws in the cloud management platform developed by Ruijie Networks that could permit an attacker to take control of the network appliances.

"These vulnerabilities affect both the Reyee platform, as well as Reyee OS network devices," Claroty researchers Noam Moshe and Tomer Goldschmidt [said](https://claroty.com/team82/research/the-insecure-iot-cloud-strikes-again-rce-on-ruijie-cloud-connected-devices) in a recent analysis. "The vulnerabilities, if exploited, could allow a malicious attacker to execute code on any cloud-enabled device, giving them the ability to control tens of thousands of devices."

The operational technology (OT) security company, which carried out an in-depth research of the Internet of Things (IoT) vendor, said it not only identified 10 flaws but also devised an attack called "Open Sesame" that can be used to hack into an access point in close physical proximity over the cloud and gain unauthorized access to its network.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Of the [10 vulnerabilities](https://www.cisa.gov/news-events/ics-advisories/icsa-24-338-01), three of them are rated Critical in severity -

* **CVE-2024-47547** (CVSS score of 9.4) - Use of a weak password recovery mechanism that leaves the authentication mechanism vulnerable to brute force attacks
* **CVE-2024-48874** (CVSS score of 9.8) - A server-side request forgery (SSRF) vulnerability that could be exploited to access internal services used by Ruijie and their internal cloud infrastructure via AWS cloud metadata services
* **CVE-2024-52324** (CVSS score: 9.8) - Use of an inherently dangerous function that could allow an attacker to send a malicious MQTT message which could result in devices executing arbitrary operating system commands

Claroty's research also found that it's easy to break MQTT authentication by simply knowing the device's serial number (CVE-2024-45722, CVSS score: 7.5), subsequently exploiting the access to Ruijie's MQTT broker in order to receive a full list of all cloud-connected devices' serial numbers.

"Using the leaked serial numbers, we could generate valid authentication credentials for all cloud-connected devices," the researchers said. "This meant that we could perform a wide range of denial-of-service attacks, including disconnecting devices by authenticating on their behalf, and even sending fabricated messages and events to the cloud; sending false data to users of these devices."

The knowledge of the device serial number could further be weaponized to access all MQTT message queues and issue malicious commands that would then get executed on all cloud connected devices (CVE-2024-52324).

That's not all. An attacker who is physically adjacent to a Wi-Fi network that uses Ruijie access points could also extract the device's serial number by intercepting the raw Wi-Fi beacons, and then leverage the other vulnerabilities in MQTT communication to achieve remote code execution. The Open Sesame attack has been assigned the CVE identifier CVE-2024-47146 (CVSS score: 7.5).

Following responsible disclosure, all the identified shortcomings have been fixed by the Chinese company in the cloud and no user action is required. About 50,000 cloud connected devices are estimated to have been potentially impacted by these bugs.

"This is another example of weaknesses in so-called internet-of-things devices such as wireless access points, routers, and other connected things that have a fairly low barrier to entry on to the device, yet enable much deeper network attacks," the researchers said.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The disclosure comes as security form PCAutomotive flagged 12 vulnerabilities in the MIB3 infotainment unit used in certain Skoda cars that malicious actors could chain together to achieve code execution, track the cars' location in real-time, record conversations via the in-car microphone, take screenshots of the infotainment display, and even exfiltrate contact information.

The flaws (from CVE-2023-28902 through CVE-2023-29113) permit attackers to "gain code execution on the MIB3 infotainment unit over Bluetooth, elevate privileges to root, bypass secure boot to gain persistent code execution, and control infotainment unit via DNS channel every time the car starts," PCAutomotive researchers [said](https://www.blackhat.com/eu-24/briefings/schedule/#over-the-air-compromise-of-modern-volkswagen-group-vehicles-42466).

The discovery adds to [nine other flaws](https://pcautomotive.com/vulnerabilities-in-skoda-and-volkswagen-vehicles) (from CVE-2023-28895 through CVE-2023-28901) identified in the MIB3 infotainment unit in late 2022 that could allow attackers to trigger a denial-of-service, bypass UDS authentication, and obtain vehicle data -- namely, mileage, recent trip duration, and average and max.=imum speed of the trip -- by knowing only VIN number of a vehicle.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](...