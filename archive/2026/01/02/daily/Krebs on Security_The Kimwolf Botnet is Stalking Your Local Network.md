---
title: The Kimwolf Botnet is Stalking Your Local Network
url: https://krebsonsecurity.com/2026/01/the-kimwolf-botnet-is-stalking-your-local-network/
source: Krebs on Security
date: 2026-01-02
fetch_date: 2026-01-03T03:23:09.262329
---

# The Kimwolf Botnet is Stalking Your Local Network

Advertisement

[![](/b-knowbe4/44.png)](https://info.knowbe4.com/ai-ksat-demo-kb4-con?utm_source=krebs&utm_medium=display&utm_campaign=aiagent&utm_content=demo)

Advertisement

[![](/b-knowbe4/45.png)](https://info.knowbe4.com/ai-ksat-demo-kb4-con?utm_source=krebs&utm_medium=display&utm_campaign=aiagent&utm_content=demo)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# The Kimwolf Botnet is Stalking Your Local Network

January 2, 2026

[14 Comments](https://krebsonsecurity.com/2026/01/the-kimwolf-botnet-is-stalking-your-local-network/#comments)

The story you are reading is a series of scoops nestled inside a far more urgent Internet-wide security advisory. The vulnerability at issue has been exploited for months already, and it’s time for a broader awareness of the threat. The short version is that everything you thought you knew about the security of the internal network behind your Internet router probably is now dangerously out of date.

![](https://krebsonsecurity.com/wp-content/uploads/2026/01/synthient-kimwolfmap.png)

The past few months have witnessed the explosive growth of a new botnet dubbed **Kimwolf**, which experts say has infected more than 2 million devices globally. The Kimwolf malware forces compromised systems to relay malicious and abusive Internet traffic — such as ad fraud, account takeover attempts and mass content scraping — and participate in crippling distributed denial-of-service (DDoS) attacks capable of knocking nearly any website offline for days at a time.

More important than Kimwolf’s staggering size, however, is the diabolical method it uses to spread so quickly: By effectively tunneling back through various “[residential proxy](https://krebsonsecurity.com/2025/10/aisuru-botnet-shifts-from-ddos-to-residential-proxies/)” networks and into the local networks of the proxy endpoints, and by further infecting devices that are hidden behind the assumed protection of the user’s firewall and Internet router.

Residential proxy networks are sold as a way for customers to anonymize and localize their Web traffic to a specific region, and the biggest of these services allow customers to route their traffic through devices in virtually any country or city around the globe.

The malware that turns an end-user’s Internet connection into a proxy node is often bundled with dodgy mobile apps and games. These residential proxy programs also are commonly installed via **unofficial Android TV boxes** sold by third-party merchants on popular e-commerce sites like **Amazon**, **BestBuy, Newegg**, and **Walmart**.

These TV boxes range in price from $40 to $400, are marketed under [a dizzying range of no-name brands and model numbers](https://github.com/synthient/public-research/blob/main/2026/01/kimwolf/product_devices.csv), and *frequently are advertised as a way to stream certain types of subscription video content for free*. But there’s a hidden cost to this transaction: As we’ll explore in a moment, these TV boxes make up a considerable chunk of the estimated two million systems currently infected with Kimwolf.

[![](https://krebsonsecurity.com/wp-content/uploads/2025/12/u-androidtv-kimwolf.png)](https://krebsonsecurity.com/wp-content/uploads/2025/12/u-androidtv-kimwolf.png)

Some of the unsanctioned Android TV boxes that come with residential proxy malware pre-installed. Image: Synthient.

Kimwolf also is quite good at infecting a range of Internet-connected digital photo frames that likewise are abundant at major e-commerce websites. In November 2025, researchers from **Quokka** published [a report](https://go.quokka.io/hubfs/App-Intel/Technical_Uhale-Digital-Picture-Frame-Security-Assessment.pdf?is=1ef7934f6635b02395adcab09a0c1b24bf0ea745b648bfe87189de8aadc7300b) (PDF) detailing serious security issues in Android-based digital picture frames running the **Uhale app —** including Amazon’s bestselling digital frame as of March 2025.

There are two major security problems with these photo frames and unofficial Android TV boxes. The first is that a considerable percentage of them come with malware pre-installed, or else require the user to download an unofficial Android App Store and malware in order to use the device for its stated purpose (video content piracy). The most typical of these uninvited guests are small programs that turn the device into a residential proxy node that is resold to others.

The second big security nightmare with these photo frames and unsanctioned Android TV boxes is that they rely on a handful of Internet-connected microcomputer boards that have no discernible security or authentication requirements built-in. In other words, if you are on the same network as one or more of these devices, you can likely compromise them simultaneously by issuing a single command across the network.

## THERE’S NO PLACE LIKE 127.0.0.1

The combination of these two security realities came to the fore in October 2025, when an undergraduate computer science student at the **Rochester Institute of Technology** began closely tracking Kimwolf’s growth, and interacting directly with its apparent creators on a daily basis.

**Benjamin Brundage** is the 22-year-old founder of the security firm **Synthient**, a startup that helps companies detect proxy networks and learn how those networks are being abused. Conducting much of his research into Kimwolf while studying for final exams, Brundage told KrebsOnSecurity in late October 2025 he suspected Kimwolf was a new Android-based variant of **Aisuru**, a botnet that was [incorrectly blamed](https://krebsonsecurity.com/2025/10/ddos-botnet-aisuru-blankets-us-isps-in-record-ddos/) for a number of record-smashing DDoS attacks last fall.

Brundage says Kimwolf grew rapidly by abusing a glaring vulnerability in many of the world’s largest residential proxy services. The crux of the weakness, he explained, was that these proxy services weren’t doing enough to prevent their customers from forwarding requests to internal servers of the individual proxy endpoints.

Most proxy services take basic steps to prevent their paying customers from “going upstream” into the local network of proxy endpoints, by explicitly denying requests for local addresses specified in [RFC-1918](https://datatracker.ietf.org/doc/html/rfc1918), including the well-known [Network Address Translation](https://www.geeksforgeeks.org/computer-networks/network-address-translation-nat/) (NAT) ranges 10.0.0.0/8, 192.168.0.0/16, and 172.16.0.0/12. These ranges allow multiple devices in a private network to access the Internet using a single public IP address, and if you run any kind of home or office network, your internal address space operates within one or more of these NAT ranges.

However, Brundage discovered that the people operating Kimwolf had figured out how to talk directly to devices on the internal networks of millions of residential proxy endpoints, simply by changing their **Domain Name System** (DNS) settings to match those in the RFC-1918 address ranges.

“It is possible to circumvent existing domain restrictions by using DNS records that point to 192.168.0.1 or 0.0.0.0,” Brundage wrote in a first-of-its-kind security advisory sent to nearly a dozen residential proxy providers in mid-December 2025. “This grants an attacker the ability to send carefully crafted requests to the current device or a device on the local network. This is actively being exploited, with attackers leveraging this functionality to drop malware.”

As with the digital photo frames mentioned above, many of these residential proxy services run solely on mobile devices that are running some game, VPN or other app with a hidden component that turns...