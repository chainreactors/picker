---
title: Juice jacking warnings are back, with a new twist
url: https://www.malwarebytes.com/blog/news/2025/06/juice-jacking-warnings-are-back-with-a-new-twist
source: Instapaper: Unread
date: 2025-06-17
fetch_date: 2025-10-06T22:58:10.032953
---

# Juice jacking warnings are back, with a new twist

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

![Public USB charger](https://www.malwarebytes.com/wp-content/uploads/sites/2/2025/06/juice-jacking.png?w=1200)

[News](https://www.malwarebytes.com/blog/category/news)
| [Threats](https://www.malwarebytes.com/blog/category/threats)

# Juice jacking warnings are back, with a new twist

Posted: June 3, 2025
 by [Danny Bradbury](https://www.malwarebytes.com/blog/authors/dbradbury)

Remember juice jacking? It’s a term that crops up every couple of years to worry travelers. This spring has seen another spate of stories, including a new, more sophisticated form of attack. But how much of a threat is it, really?

Juice jacking is where an attacker uses a malicious public USB charger to install [malware](https://www.malwarebytes.com/malware) on, or steal information from, your phone. In theory, the victim plugs their phone into a USB charging port like those found in airports, restaurants or public transportation to top up their battery. The attacker has programmed the charger to start a data connection with the phone, allowing them to perhaps view files or control apps.

Both Apple and [Android](https://www.malwarebytes.com/cybersecurity/basics/how-to-clean-your-phone-from-virus) operating system developer Google coded rudimentary protections against juice jacking into their operating systems years ago. They updated their software so that users would have to approve any request to control the phone via a USB port.

However, as Ars Technica [reported](https://arstechnica.com/security/2025/04/ios-and-android-juice-jacking-defenses-have-been-trivial-to-bypass-for-years/) last week, researchers have found a way past these mechanisms in a new variation on the theme called ChoiceJacking.

Ars offers a detailed technical analysis of the [exploit](https://www.malwarebytes.com/exploits), invented by researchers at Austria’s Graz University of Technology. In short, though, it gives itself permission to control the phone by [spoofing](https://www.malwarebytes.com/spoofing) the user’s button-pressing for them.

Government agencies continue to warn about the risks of juice jacking. The TSA was the most recent, [posting a warning](https://www.facebook.com/TSA/posts/1165260505263651?ref=embed_post) about the issue on Facebook back in March:

> “Hackers can install malware at USB ports (we’ve been told that’s called ‘juice/port jacking’). So, when you’re at an airport do not plug your phone directly into a USB port. Bring your TSA-compliant power brick or battery pack and plug in there.”

The TSA is well-intentioned, but behind the times. The FBI’s Denver office [tweeted](https://x.com/FBIDenver/status/1643947117650538498?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1643947117650538498%7Ctwgr%5Eebc1310d7dd94447b33898cb12d2c64e5c51e557%7Ctwcon%5Es1_&ref_url=https%3A%2F%2Fwww.cbsnews.com%2Fnews%2Ffbi-warns-against-juice-jacking-what-is-it%2F) about this threat back in 2023, and the LA County District Attorney’s office [posted about it](https://da.lacounty.gov/community/fraud-alerts/juice-jacking-criminals-use-public-usb-chargers-steal-data) in 2019.

Researchers have highlighted the threat since at least 2011, when the Defcon conference [installed](https://www.wallofsheep.com/pages/juice) public charging stations that would flash a warning message on peoples’ phones. Since then, others have presented on the possible risks, and enterprising tinkerers have released malicious cables that take control of devices when plugged into them.

## Have any juicers actually been jacked?

The FCC, which has had an advice page about this issue since 2019, [said](https://www.fcc.gov/juice-jacking-tips-to-avoid-it) two years ago that it hadn’t found any real-world attack...