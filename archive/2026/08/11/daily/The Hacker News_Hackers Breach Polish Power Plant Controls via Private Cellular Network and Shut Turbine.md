---
title: Hackers Breach Polish Power Plant Controls via Private Cellular Network and Shut Turbine
url: https://thehackernews.com/2026/08/hackers-breach-polish-power-plant.html
source: The Hacker News
date: 2026-08-11
fetch_date: 2026-08-12T04:02:50.565335
---

# Hackers Breach Polish Power Plant Controls via Private Cellular Network and Shut Turbine

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

![cybersecurity](data:image/svg+xml;base64...)

# [Hackers Breach Polish Power Plant Controls via Private Cellular Network and Shut Turbine](https://thehackernews.com/2026/08/hackers-breach-polish-power-plant.html)

**Swati Khandelwal**Aug 11, 2026Critical Infrastructure / Cyber Attack

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhS_4KcVdL2QogjCtjg4yqVFuDNgQ9a8SYCzjsxUKME896DBso0Zwpvb8gH9T5gMPOqM2LU-A-7IyKOqKpKiXgLWAdiABf4RrVvAq9nNpDDC2TNppKWt9RKVXmNr2-Z9Y1kIBNVi8fETA6Aj6K2s_gU0Hmc8CKDi1q1wbqD9G9uUP5cPpuwk5h88mfD9I0/s1700-e365/power-plant.jpg)

Attackers shut down a steam turbine and the process-water treatment system at a Polish combined heat and power plant by coming in over the private cellular network the local grid operator uses to reach remote equipment.

The plant supplies heat to roughly 50,000 residents. Recovery began at about 7:30 a.m. while the intruders were still active inside the network, and customers lost neither heat nor electricity.

[CERT Polska](https://cert.pl/en/posts/2026/08/incident-follow-up-report-energy-sector-2025/) disclosed the December 2025 incident on August 8 after an investigation lasting more than three months. Poland's prime minister had said in January that two CHP plants were hit. This is the second.

The route ran through a private APN, or access point name: a dedicated cellular data network managed by the distribution system operator. A configuration that allowed arbitrary devices on that APN to communicate with one another let the attacker pivot from a compromised wind-farm network to a controller at the CHP plant.

CERT says reaching an industrial control network through a private APN was, to the best of its knowledge, "the first instance of this attack vector being observed in a real-world cyberattack." The wind farm and the plant are separate facilities, and neither of them runs the network that linked them.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/zero-trust-claude-d)

The report does not establish a CVE as the cause of the intrusion, and investigators could not determine whether a vulnerability in the Teltonika router had been exploited, so there is no single software patch to apply.

The WAGO controller reachable through the APN still had default admin credentials, while the private APN allowed client-to-client traffic. CERT's first recommendation is to audit the private APN configuration and switch on client isolation.

It also advises treating the APN as untrusted from the operational technology (OT) side, segmenting and restricting traffic, removing unnecessary management services from APN-reachable interfaces, and changing default credentials.

CERT says its surveys found that Polish organizations running private APNs commonly let any device on the network reach any other. It believes similar configurations are widely deployed in other countries. The router's SSH service, the controller's web interface and the permissive APN were all working as configured.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgNZ8dvvhghnRsEuY461cn16LVXadmiJ0h7AMmlXOY2E9kvZHxV-D3yrtpO7KoCvSduVTclEcq51o0i9wHHcu_dInd4IOT8uvbExar0WuX8h1IeKOtaBLLzMTxObRwIzb8OjW5dUvxAuo10xToPe8BVQvhaxWNEJ_W4GDuiSmmZPikI7ffFA0Y6PwDgxVs/s1700-e365/place.jpg)

The [attack path](https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Follow_up_Report_2025.pdf) began at a wind farm, where a FortiGate device served as both firewall and VPN concentrator. Its VPN was exposed to the internet and allowed accounts without multi-factor authentication. The attacker had administrative privileges on the device and likely used them to obtain VPN credentials that could reach all network segments.

The distribution operator required communications to the substation's remote terminal unit to run over the serial DNP3.0 protocol, and that requirement was met. But no equivalent requirements covered the cellular router's management interface, which sat on a second interface, an Ethernet port connected to a VLAN behind the compromised firewall.

The wind farm met the DNP3.0 requirement it had been given and still supplied the route in. That requirement governed how data travelled, not how the device carrying it was administered.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgaaaNTo25fpAARwoVzM4VqIAWjwIKLoDZST8_-X1-BXA_cAlceqE3bF3HBlMQ72AzBH5XprCWPPnZd6fhg7hgr734JOFYYVOZySAf5D3_DlSI7ydahaQ9cJ1Cp8EFnhBcubQx_k4uCExnHyFnFriw_spOy7j-4qAwdrXuJx2nvf8weGUx9Eh2EEYVIBuA/s1700-e365/attackpath.jpg)

The router was a [Teltonika RUTX50](https://thehackernews.com/2023/05/industrial-cellular-routers-at-risk-11.html) whose default password had been changed during deployment. Investigators recovered repeated successful SSH logins but could not establish how the attacker obtained that password.

As of August 11, The Hacker News reviewed the published vulnerabilities in the router's own firmware and found none that would hand an unauthenticated attacker its password. The two RUT-series flaws in [CISA's 2023 Teltonika advisory](https://www.cisa.gov/news-events/ics-advisories/icsa-23-131-08), CVE-2023-32349 and CVE-2023-32350, both require existing privileges on the device, and the RUTX50's modem flaws cause only denial of service. An unpublished flaw is not ruled out.

Mobile-operator logs led CERT to assess that the attacker most likely used SSH tunneling through the router to reach the private APN. Starting December 18, the attacker scanned the APN and found a WAGO PFC200 controller exposing its web administration interface with default admin credentials. Subsequent SSH activity suggests the service was likely enabled through that interface, and timestamp correlation led CERT to assess that the attacker most likely tunneled through the WAGO into the plant's OT network.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/corelight-d)

On December 25, the attacker successfully connected to three Siemens PLCs over the S7 protocol, activity CERT considers most likely to have been reconnaissance for the later destructive actions.

On December 29, attacker activity inside the CHP network ran from about 5:30 a.m. until about 10:10 a.m., with plant recovery beginning at about 7:30 a.m. A...