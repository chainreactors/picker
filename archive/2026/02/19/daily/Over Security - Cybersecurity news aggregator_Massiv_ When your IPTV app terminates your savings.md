---
title: Massiv: When your IPTV app terminates your savings
url: https://www.threatfabric.com/blogs/massiv-when-your-iptv-app-terminates-your-savings
source: Over Security - Cybersecurity news aggregator
date: 2026-02-19
fetch_date: 2026-02-20T04:07:45.550021
---

# Massiv: When your IPTV app terminates your savings

[Skip to content](#main-content)

[![threatfabric-logo-light](https://www.threatfabric.com/hubfs/Threatfabric/logos/threatfabric-logo-light.svg "threatfabric-logo-light")](//www.threatfabric.com)

[![threatfabric-logo-light](https://www.threatfabric.com/hubfs/Threatfabric/logos/threatfabric-logo-light.svg "threatfabric-logo-light")](//www.threatfabric.com)

* OUR SOLUTIONS
  + [Mobile Threat Intelligence (MTI)](https://www.threatfabric.com/mti)
  + [Fraud Risk Suite (FRS)](https://www.threatfabric.com/frs)
* [PARTNERS](https://www.threatfabric.com/partners)
* [WEBINARS](https://www.threatfabric.com/webinars)
* [ARTICLES](https://www.threatfabric.com/blogs)
* RESOURCES
  + [DATASHEETS & REPORTS](https://www.threatfabric.com/resources)
  + [IN THE NEWS](https://www.threatfabric.com/news)
  + [FUSION FIRESIDE](https://www.threatfabric.com/fusion-fireside)
* [Contact](https://www.threatfabric.com/contact)
* [Linkedin](https://www.linkedin.com/company/threatfabric)
* [Twitter](https://twitter.com/threatfabric)
* [Jobs](https://www.threatfabric.com/jobs)
* [Privacy](https://www.threatfabric.com/privacy)
* [Intel/PGP](https://www.threatfabric.com/contact)

[Contact](https://www.threatfabric.com/contact)

Research

## Massiv: When your IPTV app terminates your savings

19 February 2026

![](https://www.threatfabric.com/hubfs/TF_IPTV4.jpg)

### Jump to

Modern mobile threat landscape offers multiple malware families used by lots of single threat actors or organised criminal groups. They are constantly on the lookout for the ways to deliver the Trojans to the victims in the most natural, smooth and unsuspicious way. A modern Android banking Trojan, which is usually distributed through side-loading, must convincingly masquerade as a legitimate application so that it does not raise suspicion and persuades victims to proceed with the installation.

Recent research performed by our Mobile Threat Intelligence (MTI) team revealed yet another Android banking Trojan. We decided to name it Massiv, after one of its components. This new threat, while only seen in a limited number of rather targeted campaigns, already poses great risk to the users of mobile banking, allowing its operators to remotely control infected devices and perform Device Takeover attacks with further fraudulent transactions performed from victim's banking accounts. The distribution of Massiv highlights another rising trend observed on the mobile threat landscape - threat actors masquerade their malware as IPTV applications, targeting users looking for the online TV applications.

Key takeaways of this report are:

* Massiv is a **new Device Takeover malware family** without direct links to other known threats.
* Its remote control capabilities lead to confirmed fraudulent cases in **southern Europe.**
* **IPTV applications** are increasingly used as masquerading for mobile threats distribution.

## Massiv Attacks

Being a modern banking malware family, Massiv supports all the necessary features to be a "successful" threat. It is a powerful tool to perform fraud on mobile devices, equipped with overlay functionality, keylogging, and SMS/Push message interception to obtain sensitive data. Besides that, it is a fully functional remote-control tool, providing its operator with direct access to the victim's device.

![Slide1-Feb-18-2026-10-26-56-8271-AM](https://www.threatfabric.com/hs-fs/hubfs/Slide1-Feb-18-2026-10-26-56-8271-AM.png?width=3840&height=2160&name=Slide1-Feb-18-2026-10-26-56-8271-AM.png)

### Digital state is opening doors

Overlay attacks serve as an early-stage technique leveraged by Massiv operators to facilitate fraudulent activity. Just like other banking malware families, Massiv monitors applications launched on infected devices and shows a fake overlay if a targeted application is launched by the victim. The fake screen mimics the UI of the original application and asks user to enter credentials and other sensitive information, like credit card details.

Interestingly, one of the campaigns of Massiv, analyzed by our analysts, targeted Portuguese government application gov.pt, asking the victim for phone number and PIN code. This application serves as a digital identity wallet for Portugal. Criminals are likely targeting it to further use victim’s details to bypass KYC verification that could be done via this application.

It also connects with another service, Chave Móvel Digital, a Portuguese digital authentication and signature system that allows citizens to securely access public and private online services. This includes interacting with online banking, meaning that it can also be used to access the victim’s banking account and perform and approve fraudulent transactions.

![Slide2-Feb-18-2026-10-26-57-0045-AM](https://www.threatfabric.com/hs-fs/hubfs/Slide2-Feb-18-2026-10-26-57-0045-AM.png?width=3840&height=2160&name=Slide2-Feb-18-2026-10-26-57-0045-AM.png)

MTI research identified cases where new accounts were opened in the name of the victim (user of the infected device) in new banks and services (not used by the victim). Since those accounts are fully under fraudster control, they can further use them as a part of money laundering scheme as well as getting loans and cashing out the money, leaving unsuspecting victim in debts in the bank they never opened account themselves.

### Taking over the device

Having the credentials and other sensitive data stolen with overlays and keylogging, Massiv further provides the operator with remote access to the infected device. The *FuncVNC* class implements a remote visual monitoring and interaction capability built on top of Android’s AccessibilityService. Its functionality establishes a control channel that allows a remote operator to both observe and manipulate the device’s user interface in near real time.

All communication is performed over a WebSocket channel, which acts as the command-and-control (C2) transport for both inbound commands and outbound UI data.

Following the modern trend, Massiv supports 2 modes of operation during a remote control session: screen streaming and UI-tree mode. Screen streaming mode relies on MediaProjection API, effectively sharing the screen content with the remote operator.

![code](https://www.threatfabric.com/hs-fs/hubfs/code.png?width=1336&height=906&name=code.png)

However, some applications implement protection against screen capture. To bypass it, Massiv uses so-called UI-tree mode - it traverses AccessibilityWindowInfo roots and recursively processes AccessibilityNodeInfo objects to build a JSON representation of:

* Visible text and content descriptions
* Class names of UI elements
* Screen coordinates (bounds)
* Interaction flags (clickable, editable, focused, enabled)

Only nodes deemed “important” (visible and interactive or text-bearing) are exported, reducing noise and focusing on actionable interface elements. This produces a structured interface model rather than raw screenshots. That allows the operator to:

* Identify specific buttons, input fields, or prompts
* Understand layout positions
* Automate interactions based on element attributes.

Massiv implements a set of supported actions that can be performed by the remote operator. The remote control commands supported are listed in the [Appendix](#Remote-control-commands).

## The scariest movie you'll watch

In the campaign observed by MTI, Massiv is masquerading as IPTV application. These types of applications provide access to online TV services. There are multiple services that provide this - including some that might violate copyright policies, thus not allowed to be distributed via official Google Play Store. In general, users of IPTV applications are used to the fact that these applications are distributed outside of the official store, usually through their own websites or Telegram channels.

![Slide3-Feb-18-2026-10-26-57-0185-AM](https://www.threatfabric.com/hs-fs/hubfs/Slide3-Feb-18-2026-10-26-57-0185-AM.png?width=3840&...