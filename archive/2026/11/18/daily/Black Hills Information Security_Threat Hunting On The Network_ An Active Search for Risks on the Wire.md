---
title: Threat Hunting On The Network: An Active Search for Risks on the Wire
url: https://www.blackhillsinfosec.com/threat-hunting-network/
source: Black Hills Information Security
date: 2026-11-18
fetch_date: 2026-11-19T09:46:02.889711
---

# Threat Hunting On The Network: An Active Search for Risks on the Wire

[Skip to main content](#main-content)

[![BHIS](/uploads/media/bhis-text-bhis-f909d4808e69428ba2547d42a650842f.png)![BHIS](/uploads/media/bhis-text-bhis-light-f0fc7d40d92b4eccb72ef18ffe68bef6.png)](/)

Services

[All Services](/services/ "All Services")

[Penetration Testing](/services/traditional-penetrating-testing/ "Penetration Testing")

[Continuous Penetration Testing](/services/antisoc/ "Continuous Penetration Testing")

[Web Application Testing](/services/web-appllication-testing/ "Web Application Testing")

[ActiveSOC](https://activesoc.blackhillsinfosec.com/ "ActiveSOC")

[Fusion PenTest](/fusion-penetration-testing/ "Fusion PenTest")

[AI Security Assessments](/services/ai-security-assessments/ "AI Security Assessments")

[Incident Response](/services/incident-response/ "Incident Response")

[Blue Team Services](/services/blue-team-services/ "Blue Team Services")

[Blockchain Security](/services/blockchain-security/ "Blockchain Security")

[High-Profile Risk Assessments](/services/high-profile-risk-assessments/ "High-Profile Risk Assessments")

[Complete Service Guide](/services/complete-service-guide/ "Complete Service Guide")

[Governance, Risk and Compliance](/grc/ "Governance, Risk and Compliance")

[Contact Us](/contact-us/ "Contact Us")

About Us

[BHIS Tribe of Companies](/bhis-tribe-of-companies/ "BHIS Tribe of Companies")

[Leadership Team](/about/leadership/ "Leadership Team")

[All Staff](/about/admin-staff/ "All Staff")

[Security Consultants](/about/security-consultants/ "Security Consultants")

[BHIS Privacy Policy](/bhis-online-privacy-policy/ "BHIS Privacy Policy")

Free Resources

[Blogs](/blog/ "Blogs")

[Webcasts](/webcasts/ "Webcasts")

[Free Cyber Security Tools](/free-cybersecurity-tools/ "Free Cyber Security Tools")

[Free Cybersecurity Webcasts](/free-cybersecurity-webcasts/ "Free Cybersecurity Webcasts")

[BHIS Podcasts](/bhis-podcasts/ "BHIS Podcasts")

[RITA](/rita/ "RITA")

Training

[BHIS & Antisyphon Training](/bhis-and-antisyphon-training/ "BHIS & Antisyphon Training")

[Wild West Hackin' Fest](/wild-west-hackin-fest/ "Wild West Hackin' Fest")

Community

[Connect](/community/ "Connect")

[Discord](https://discord.gg/BHIS "Discord")

[LinkedIn](https://www.linkedin.com/company/black-hills-information-security/ "LinkedIn")

[YouTube](https://www.youtube.com/c/BlackHillsInformationSecurity/videos "YouTube")

[Bluesky](https://bsky.app/profile/bhinfosecurity.bsky.social "Bluesky")

[Twitter/X](https://twitter.com/BHinfoSecurity "Twitter/X")

[Upcoming Events](/community/events/ "Upcoming Events")

Fun Stuff

[Backdoors and Breaches](/tools/backdoorsandbreaches/ "Backdoors and Breaches")

[Free Lab Fridays](/free-lab-fridays/ "Free Lab Fridays")

[Merch, Zines & More](/spearphish-general-store/ "Merch, Zines & More")

[PROMPT# Zine](/prompt-zine/ "PROMPT# Zine")

[REKCAH](/rekcah/ "REKCAH")

[Books](/tools/books/ "Books")

[Game of Life](/game-of-life/ "Game of Life")

1. [Home](/)
2. [Blog](/blog)
3. Threat Hunting On The Network: An Active Search for Risks on the Wire

[Network](/blog?topic=Network)[Threat Hunting](/blog?topic=Threat%20Hunting)[Zeek](/blog?topic=Zeek)[RITA](/blog?topic=RITA)[Network Security](/blog?topic=Network%20Security)[Behavioral Analysis](/blog?topic=Behavioral%20Analysis)[Signature-Based Detection](/blog?topic=Signature-Based%20Detection)[Packet Analysis](/blog?topic=Packet%20Analysis)

B

[Betty DuBois](/blog?author=Betty%20DuBois "See all posts by Betty DuBois")Guest Author

![](/uploads/media/an-active-search-for-risks-on-the-wire-45b738a6e79a47b7aad0538ae97935ac.png)

|  |
| --- |
| *This article was originally published in the InfoSec Survival Guide: Teal Book — Threat Hunting. Read it free online [HERE](https://www.blackhillsinfosec.com/prompt-zine/), or grab it on the [Spearphish General Store](https://spearphish-general-store.myshopify.com/collections/infosec-survival-guides) (free digital download or a $1.25 physical copy, your call).* |

All threat hunters are looking for evidence of nefarious activity, hopefully before an incident happens. Threat hunting on the network involves actively searching through packet data for malicious activity. Threat hunting on an endpoint depends more heavily on logs. Think of it as on the wire (or in the air) versus on a host itself. Don’t worry, you don’t have to look through every packet in a pcap file. That would make your head explode!

We would like to think our firewalls and Intrusion Detection/Prevention Systems (IDS or IPS) are blocking all evil traffic from coming in, but those appliances have limits. Adversaries evolve their techniques faster than the static signatures used on our perimeter defenses. Updates from vendors and threat intelligence feeds can’t keep up. A network threat hunter looks for patterns beyond specific byte sequences, file hashes, and documented signature exploits.

In contrast to signatures, behavior analysis lets network threat hunters draw insights from network baselines to understand expected protocols and traffic flows. Threat actors may change their techniques and procedures, but they still have fundamental network behaviors.

### Signature-Based vs Behavioral Analysis in Threat Hunting![](/uploads/content/ce9d6628962448a1a507707d166a59ad.png)

### Common Data Sources

* NetFlow or Internet Protocol Flow Information Export (IPFIX) records
  + Every switch, router, firewall, VPN appliance, IDS/IPS, or other network device capable of exporting flow data should be sending these flow records to the SIEM.
* HTTP/HTTPs Proxy logs for TLS/HTTP headers
* VPN appliance logs for external connections to internal resources
* Full packet captures
  + Pcap files captured from taps or SPAN sessions.

### My Favorite Tools

* NetFlow/IPFIX/logs > SIEM (Wazuh or Graylog) for aggregation and metadata
* Logs and/or packets > Elasticsearch > Kibana for log analysis and visualization
* Packets > Zeek > RITA by Active Countermeasures for full packet capture, indexing, alerting, and search
* Packets > Arkime for full packet capture, indexing, and search
* Packets > Wireshark or TShark for deep analysis

### A Few Additional Indicators

* **Unusual port usage:** services running on non-standard ports.
* **DNS anomalies:** DGA domains, DNS tunneling, or excessive NXDOMAIN responses.
* **Failed authentication attempts:** brute force indicators across multiple systems.
* **Certificate anomalies:** mismatched common names or short validity periods.
* **TLS/SSL anomalies:** weak ciphers, unusual JA3/JA4+ hashes, or certificate chain issues.

### My Favorite Methodologies

* **Crown jewel analysis** — Focus on protecting most critical assets and data.
* **Hypothesis-driven hunting** — Form theories about potential threats and test them.
* **Kill chain mapping** — Identify which attack phase the indicators belong to.
* **Assumed breach methodology** — Operate as though compromise has already occurred.
* Take advantage of established frameworks: MITRE ATT&CK®, Pyramid of Pain, PEAK.

A good network threat hunter is also looking at internal traffic. Is Susie in Accounting supposed to be using SSH to access a server in another country? No. What about Brad in Marketing? Is it normal for him to download multi-gigabyte files from a server in the data center? Maybe. At three o’clock in the morning? Probably not.

Finally, don’t be afraid to dive in. Threat hunting is not just for the most experienced cybersecurity analysts. Start with a single protocol and tools you already have to build confidence.

![](/uploads/media/infosec-survival-guide/infosec-survival-guide-teal-book-threat-hunting-final-c1-13eaa664397244fd88a1dd657307b8dc.png)

---

***Explore the Infosec Survival Guide and more… for FREE!***

*Get instant access to every issue of the Infosec Survival Guide, as well as our self-published infosec zine PROMPT#, and exclusive Darknet Diaries comics — all available at no cost.*

[CHECK OUT ALL ISSUES HERE!](https://www.blackhillsinfosec.com/...