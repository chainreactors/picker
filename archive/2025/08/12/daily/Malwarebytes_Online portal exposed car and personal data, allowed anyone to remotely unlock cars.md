---
title: Online portal exposed car and personal data, allowed anyone to remotely unlock cars
url: https://www.malwarebytes.com/blog/news/2025/08/online-portal-exposed-car-and-personal-data-allowed-anyone-to-remotely-unlock-cars
source: Malwarebytes
date: 2025-08-12
fetch_date: 2025-10-07T00:47:40.123254
---

# Online portal exposed car and personal data, allowed anyone to remotely unlock cars

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

![car dealership](https://www.malwarebytes.com/wp-content/uploads/sites/2/2025/08/open-car-door.png?w=1200)

[News](https://www.malwarebytes.com/blog/category/news)
| [Privacy](https://www.malwarebytes.com/blog/category/privacy)

# Online portal exposed car and personal data, allowed anyone to remotely unlock cars

Posted: August 11, 2025
 by [Pieter Arntz](https://www.malwarebytes.com/blog/authors/metallicamvp)

A carmaker’s online dealership portal has been found leaking the private information and vehicle data of its customers. This also meant that anyone with access could remotely break into a car.

Researcher Eaton Zveare shared his discovery with [TechCrunch](https://techcrunch.com/2025/08/10/security-flaws-in-a-carmakers-web-portal-let-one-hacker-remotely-unlock-cars-from-anywhere). Although he said he has chosen not to disclose the vendor’s name, he revealed that it is a well-known automaker with several popular sub-brands and more than 1,000 dealerships across the United States.

Zveare says it wasn’t easy to find the flaw, but once he did, it allowed him to modify the code at the portal’s login page so he could bypass the login security checks. This permitted him to create a new national administrator account.

Not only did this allow him to access all the data of these dealerships, he also found a national consumer lookup tool that allowed any logged-in portal user to look-up the vehicle and driver data of that carmaker.

Real life tests learned that taking a vehicle’s unique identification number (VIN) from the windshield of a car allowed anyone with access to the portal to look up the name of the owner. It was also possible to pair any vehicle with a mobile account which could then be used to remotely control a car’s functions, such as unlocking the vehicle.

Since both a VIN or someone’s first and last name were enough to find and transfer ownership of an account to one under control of an attacker, they would—at least—be able to open the car and steal everything inside. The researcher did not test whether he was able to drive away in it.

Although he found no evidence of anyone else exploiting the flaw, the portals were a security nightmare waiting to happen. It even allowed administrator accounts, such as the one he was able to create, access to other dealer systems as if they were that user without needing their logins, and found personally identifiable customer data, some financial information, and telematics systems that allowed the real-time location tracking of rental or courtesy cars.

As we have said [before](https://www.malwarebytes.com/blog/news/2024/01/fcc-wants-cars-to-make-life-harder-for-stalkers), this is exactly the sort of thing the Federal Communications Commission (FCC) wants car manufacturers to make harder for stalkers, not easier.

Zveare will be [presenting his findings at Defcon](https://media.defcon.org/DEF%20CON%2033/DEF%20CON%2033%20presentations/Eaton%20Zveare%20Roshan%20Piyush%20-%20Unexpected%20Connections%20How%20a%20vulnerability%20in%20obscure%20dealer%20software%20could%20have%20unlocked%20your%20car%20from%20anywhere.pdf). He reported the bugs he found to the car maker, and says it took them a week to fix them.

## Tips to keep a stalker from tracking your car

Not all cars offer these options, and the tips may not apply to your situation, but here are some general tips for people that are afraid they are the target of a stalker:

* Use the navigation app on your phone (such as Google Maps, Waze, etc), rather than the one built into your car.
* Do not store places you visit regularly in the car’s navigation.
* Consider using a [VPN](https://www.malwarebytes.com/vpn) when you connect to you...