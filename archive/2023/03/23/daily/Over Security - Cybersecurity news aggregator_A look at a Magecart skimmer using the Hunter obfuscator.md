---
title: A look at a Magecart skimmer using the Hunter obfuscator
url: https://www.malwarebytes.com/blog/threat-intelligence/2023/03/hunter-skimmer
source: Over Security - Cybersecurity news aggregator
date: 2023-03-23
fetch_date: 2025-10-04T10:24:23.889963
---

# A look at a Magecart skimmer using the Hunter obfuscator

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

![A look at a Magecart skimmer using the Hunter obfuscator](https://www.malwarebytes.com/wp-content/uploads/sites/2/2023/03/asset_upload_file87801_262493.jpg?w=736)

[Threat Intel](https://www.malwarebytes.com/blog/category/threat-intel)

# A look at a Magecart skimmer using the Hunter obfuscator

Posted: March 21, 2023
 by [Jérôme Segura](https://www.malwarebytes.com/blog/authors/jeromesegura)

Threat actors are notorious for trying to hide their code in various ways, from binary packers to obfuscators. On their own, these tools are not always malicious as they can also be be used by companies or individuals who wish to keep their work safe from piracy, but overall they tend to be largely abused.

In the case of credit card skimmers in client-side attacks, obfuscators are a common occurrence as they can make code identification more difficult. Defenders typically have the choice to either rely on the browser’s debugger and step through the code, or can statically try to reverse it. The latter tends to be quite time consuming, but the former can often problematic if the malware author adds anti-debugging routines.

Today, we look at a Magecart skimmer that uses Hunter, a PHP Javascript obfuscator. During our investigation, we were able to discover a number of domains all part of the same infrastructure with custom skimmers for several Magento stores.

## Initial injection on e-commerce sites

The attack relies on 2 steps: the first one is code injected inside the website’s source that calls out a remote URL. That URL in turn, loads the skimmer within the payment checkout process.

We notice a large blurb of code that contains some static elements and others that are uniquely generated. The ‘*eval*‘ portion of the code is a clear giveaway that the random looking string is being processed dynamically to return some instructions.

![](https://www.malwarebytes.com/wp-content/uploads/sites/2/2023/03/easset_upload_file46265_262493_e.png)

The function (h,u,n,t,e,r) helps us to identify that this obfuscator is called Hunter and [available on GitHub](https://github.com/nicxlau/hunter-php-javascript-obfuscator). To decode the obfuscated string, we can simply write out the content of *eval* and we obtain a single line of JavaScript pointing to a URL.

![](https://www.malwarebytes.com/wp-content/uploads/sites/2/2023/03/easset_upload_file26904_262493_e.png)

This URL contains code that has been obfuscated with Hunter once again. This time, once we deobfuscate it, we see what appears to be HTML code with forms referring to credit card fields. This is the actual skimmer.

## Skimmer at checkout page

When a victim who’s shopping at a compromised online store goes to check out, there will be additional fields injected in the contact form that aren’t normally there. Below is the legitimate checkout page of a store without the skimmer being loaded:

![](https://www.malwarebytes.com/wp-content/uploads/sites/2/2023/03/easset_upload_file76770_262493_e.png)

We can see that the payment process is on the bottom right hand side. In contrast, this is what the same page looks like when the skimmer is loaded:

![](https://www.malwarebytes.com/wp-content/uploads/sites/2/2023/03/easset_upload_file4736_262493_e.png)

Additional fields were inserted between the shopper’s email address and name. In this case, the threat actor didn’t do a very good job because the fields are in English while the rest is in Spanish.

The credit card data to be stolen is encoded, then stored inside a cookie and subsequently exfiltrated via a POST request.

![easset_upload_file21336_262493_e](https://www.malwarebytes.com/wp-content/uploads/sites/2/2023/03/easset_upload_file21336_262493_e.p...