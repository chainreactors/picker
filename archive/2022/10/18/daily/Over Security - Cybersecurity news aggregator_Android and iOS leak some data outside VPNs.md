---
title: Android and iOS leak some data outside VPNs
url: https://www.malwarebytes.com/blog/news/2022/10/android-and-ios-suffer-from-leaky-tunnels
source: Over Security - Cybersecurity news aggregator
date: 2022-10-18
fetch_date: 2025-10-03T20:09:37.600219
---

# Android and iOS leak some data outside VPNs

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

![A VPN tunnel](https://www.malwarebytes.com/wp-content/uploads/sites/2/2022/10/asset_upload_file19347_241248.jpg?w=736)

[News](https://www.malwarebytes.com/blog/category/news)

# Android and iOS leak some data outside VPNs

Posted: October 16, 2022
 by [Christopher Boyd](https://www.malwarebytes.com/blog/authors/cboyd)

Virtual Private Networks (VPNs) on [Android](https://www.malwarebytes.com/cybersecurity/basics/how-to-clean-your-phone-from-virus) and iOS are in the news. It’s been discovered that in certain circumstances, [some of your traffic is leaked](https://mullvad.net/en/blog/2022/10/10/android-leaks-connectivity-check-traffic/) so it ends up outside of the safety cordon created by the VPN.

Mullvad, the discoverers of this Android “feature” say that it has the potential to cause someone to be de-anonymised (but only in rare cases as it requires a fair amount of skill on behalf of the snooper). At least one Google engineer claims that this isn’t a major concern, is intended functionality, and will continue as is for the time being.

## MUL22-03

The Android discovery, currently named MUL22-03, is not the VPN’s fault. The transmission of data outside of the VPN is something which happens quite deliberately, to all brands of VPN, and not as the result of some sort of terrible hack or [exploit](https://www.malwarebytes.com/exploits). Although the full audit report has not yet been released, the information available so far may be worrying for some. According to the report, Android sends “connectivity checks” (traffic that determines if a connection has been made successfully) outside of whichever VPN tunnel you happen to have in place.

Perhaps confusingly, this also occurs whether or not you have “Block connections without VPN” or even “Always on VPN” switched on, which is (supposed) to do what you’d expect given the name. It’s quite reasonable to assume a setting which says one thing will not in fact do the opposite of that thing, so what is going on here?

The leakage arises as a result of certain special edge case scenarios, in which case Android will override the various “Do not do this without a VPN” settings. This would happen, for example, with something like a captive portal. A [captive portal](https://en.wikipedia.org/wiki/Captive_portal) is something you typically access when joining a network—something like a hotspot sign-in page stored on a gateway.

Why? Because VPNs run on top of whatever Internet-connected network you are on, so you have to join a network before you can establish your VPN connection. Anything that happens before you establish your VPN connection can’t be protected by it.

As per [Bleeping Computer](https://www.bleepingcomputer.com/news/google/android-leaks-some-traffic-even-when-always-on-vpn-is-enabled/), this leakage can include DNS lookups, [HTTPs](https://www.malwarebytes.com/zero-day) traffic, [IP addresses](https://www.malwarebytes.com/cybersecurity/basics/what-is-ip-address) and (perhaps) NTP traffic (Network Time Protocol, a protocol for synchronising net-connected clocks).

Mullvad VPN first reported this a documentation issue, and then [asked](https://issuetracker.google.com/issues/250529027?pli=1) for a way to “…disable connectivity checks while ‘Block connections without VPN’ (from now on lockdown) is enabled for [a VPN](https://www.malwarebytes.com/what-is-vpn) app.”

Google’s [response](https://issuetracker.google.com/issues/250529027?pli=1), via its issue tracker was “We do not think such an option would be understandable by most users, so we don’t think there is a strong case for offering this.”

According to Google, disabling connectivity checks is a non-starter for four reasons: VP...