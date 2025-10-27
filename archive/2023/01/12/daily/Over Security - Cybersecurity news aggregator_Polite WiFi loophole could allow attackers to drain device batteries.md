---
title: Polite WiFi loophole could allow attackers to drain device batteries
url: https://www.malwarebytes.com/blog/news/2023/01/polite-wifi-loophole-could-allow-attackers-to-drain-device-batteries
source: Over Security - Cybersecurity news aggregator
date: 2023-01-12
fetch_date: 2025-10-04T03:41:36.165279
---

# Polite WiFi loophole could allow attackers to drain device batteries

[Skip to content](#primary)

Search

Search Malwarebytes.com

Search for:

* [Sign In](https://my.malwarebytes.com/en/login)

  [Sign in](https://my.malwarebytes.com/overview)

  [Activate subscription >](https://my.malwarebytes.com/landing/activate)

  [Add devices or upgrade >](https://my.malwarebytes.com/landing/upgrade)

  [Renew subscription >](https://my.malwarebytes.com/landing/manual-renewal)

  [Secure Hub >](https://my.malwarebytes.com/secure-hub)

  [Don’t have an account?
  **Sign up >**](https://my.malwarebytes.com/overview?flow=signup)

  Sign In

[Malwarebytes logo](https://www.malwarebytes.com/blog)

* Personal

  < Products

  **Device Protection & Antivirus**

  + [Premium Security Antivirus](https://www.malwarebytes.com/premium)
  + [Mobile Security for Android & iOS](https://www.malwarebytes.com/mobile)

  **Identity Protection**

  + [Identity Theft Protection](https://www.malwarebytes.com/identity-theft-protection)
  + [Personal Data Remover](https://www.malwarebytes.com/personal-data-remover)
  + [Digital Footprint Scanner](https://www.malwarebytes.com/digital-footprint)

  **Privacy Protection**

  + [Privacy VPN](https://www.malwarebytes.com/vpn)
  + [Browser Guard](https://www.malwarebytes.com/browserguard)
  + [AdwCleaner](https://www.malwarebytes.com/adwcleaner)

  Have a current computer infection?

  [**Free Virus Scan**](https://www.malwarebytes.com/solutions/virus-scanner)

  Worried it’s a scam?

  [**Free Scam Guard tool**](https://www.malwarebytes.com/solutions/scam-guard)

  Try our antivirus with a free, full-featured 14-day trial

  [**Free Antivirus**](https://www.malwarebytes.com/mwb-download)

  Get your free digital security toolkit

  [**Explore all free tools**](https://www.malwarebytes.com/free-tools)

  Find the right cyberprotection for you

  [**Compare plans and pricing**](https://www.malwarebytes.com/pricing)
* Business

  < Business

  **[Teams](https://www.malwarebytes.com/teams)**

  Protect small & home offices – no IT expertise needed

  **[ThreatDown](https://www.threatdown.com/?utm_campaign=mwb-referral&utm_source=malwarebytes.com&utm_medium=referral&utm_content=cta-mb-nav-threatdown)**

  Award-winning endpoint security for small and medium businesses
* Pricing

  < Pricing

  [Personal pricing](https://www.malwarebytes.com/pricing)

  Protect your personal devices and data

  [Small or home office pricing](https://www.malwarebytes.com/pricing/teams)

  Protect your team’s devices and data – no IT skills needed

  [Corporate pricing](https://www.threatdown.com/pricing/?utm_campaign=mwb-referral&utm_source=malwarebytes.com&utm_medium=referral&utm_content=cat-en-us-navbar-pricing-business-pricing-click)

  Explore award-winning endpoint security for your business
* [Partners](https://www.malwarebytes.com/partners)
* Resources

  < Resources

  [![Malwarebytes Labs](https://www.malwarebytes.com/wp-content/uploads/sites/2/2023/07/mwb-labs-159px.svg)](https://www.malwarebytes.com/blog)

  + [Security terms glossary](https://www.malwarebytes.com/glossary)
  + [Threat Center](https://www.malwarebytes.com/blog/threats)
  + [Cybersecurity News](https://www.malwarebytes.com/blog)

  + [About Malwarebytes](https://www.malwarebytes.com/company)
  + [Press](https://www.malwarebytes.com/press/)
  + [Careers](https://www.malwarebytes.com/jobs)

  [Cybersecurity Resource Center](https://www.malwarebytes.com/cybersecurity)

  + [Antivirus](https://www.malwarebytes.com/cybersecurity/basics/antivirus)
  + [Malware](https://www.malwarebytes.com/malware)
  + [Phishing](https://www.malwarebytes.com/phishing)
  + [Ransomware](https://www.malwarebytes.com/ransomware)
  + [Small business hub](https://www.malwarebytes.com/small-business)
  + [See all articles](https://www.malwarebytes.com/cybersecurity)
* Help

  < Support

  [Malwarebytes Help Center](https://help.malwarebytes.com/hc/en-us)

  Malwarebytes and Teams Customers

  [ThreatDown Business Support](https://support.threatdown.com/hc/en-us/?utm_campaign=mwb-referral&utm_source=malwarebytes.com&utm_medium=referral&utm_content=cta-navbar-support-Threatdown-business-click)

  Nebula and Oneview Customers

  [Community Forums](https://forums.malwarebytes.com/)

Free Download

Search
Search

Search Malwarebytes.com

Search for:

![man politely opening car door for a woman](https://www.malwarebytes.com/wp-content/uploads/sites/2/2023/01/asset_upload_file86288_253954.png?w=736)

[News](https://www.malwarebytes.com/blog/category/news)

# Polite WiFi loophole could allow attackers to drain device batteries

Posted: January 10, 2023
 by [Pieter Arntz](https://www.malwarebytes.com/blog/authors/metallicamvp)

Researchers at the University of Waterloo in Ontario have further researched a loophole in the WiFi protocol that was dubbed “polite WiFi”.

Last year the researchers [published](https://dl.acm.org/doi/abs/10.1145/3495243.3560530) a study in which they showed someone could use this loophole to triangulate the location of any WiFi enabled device. Now, they’ve followed up that study to say that someone could also drain the batteries of such device. A further study may involve privacy threats based on interference of the usage of the device with the response time.

## Polite WiFi

A MAC address (media access control address) is a unique identifier assigned to a network interface controller (NIC) for use as a network address in communications within a network segment. This use is common in most IEEE 802 networking technologies, including Ethernet, WiFi, and Bluetooth.

The “polite WiFi” loophole is based on the fact that a WiFi enabled device responds to every correct packet it receives, as long as it is directed at its own MAC address. This means the sending device does not have to be on the same network.

## Wi-Peep

Based on this knowledge and knowing the response time, the researchers built a drone equipped with some readily available parts and sent it out on a scouting mission. Because the drone is on the move it can use triangulation to pinpoint the location of the responding devices.

Within seconds, a burglar equipped with such a device would know with an accuracy of a meter/yard where your WiFi enabled devices like phones, tablets, TVs and other “smart” devices can be found in your home. And, in a similar fashion a criminal could track the movements of security guards inside a bank by following the location of their phones or smartwatches.

## Drained batteries

The goal of the battery draining attack is to drain the battery of a WiFi device by forcing the device to transmit WiFi frames continuously. To execute such an attack, an attacker could send back to back fake 802.11 frames to the target device. This forces the target devices to continuously transmit acknowledgment packets, draining its battery. This could be used in a coordinated attack at CCTV cameras that switch to batteries when the power has been cut.

## Prevention

The attacks based on polite WiFi are based on the fact that WiFi devices have to reply with an Acknowledgment (ACK) signal. The ACK signal is sent by the receiving station (destination) back to the sending station (source) after the receipt of a recognizable block of data of specific size. This is usually the start of a more meaningful conversation, but it doesn’t have to be.

To prevent WiFi devices from responding to signals with a malicious intent the device would have to verify if the frame is legitimate before sending an ACK. Unfortunately, this is not possible due to the WiFi standard timing requirements.

The researchers propose some future changes to the WiFi protocol that make it possible to establish whether a frame is legitimate before the ACK is sent.

And they recommend that WiFi chip manufacturers introduce an artificial, randomized variation in device response time, which would make calculations such as those performed by the Wi-Peep inaccurate.

---

**We don’t just report on threats—we remove them**

Cybersecurity risk...