---
title: Don’t Let Your Domain Name Become a “Sitting Duck”
url: https://krebsonsecurity.com/2024/07/dont-let-your-domain-name-become-a-sitting-duck/
source: Krebs on Security
date: 2024-08-01
fetch_date: 2025-10-06T18:08:18.999278
---

# Don’t Let Your Domain Name Become a “Sitting Duck”

Advertisement

[![](/b-sysdig/1.png)](https://content.foleon.com/sysdig/sysdig-cloud-defense-report-2025/?utm_source=krebs-on-security&utm_medium=display&utm_campaign=aware_amer_the-right-way_na_ung_display&utm_content=AD000460_1240x110)

Advertisement

[![](/b-knowbe4/37.jpg)](https://www.knowbe4.com/resources/kits/cybersecurity-awareness-month?utm_source=Krebs&utm_medium=display&utm_campaign=cybersecurityawarenessmonth&utm_content=hrm+)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Don’t Let Your Domain Name Become a “Sitting Duck”

July 31, 2024

[27 Comments](https://krebsonsecurity.com/2024/07/dont-let-your-domain-name-become-a-sitting-duck/#comments)

More than a million domain names — including many registered by Fortune 100 firms and brand protection companies — are vulnerable to takeover by cybercriminals thanks to authentication weaknesses at a number of large web hosting providers and domain registrars, new research finds.

![](https://krebsonsecurity.com/wp-content/uploads/2024/07/duckstarget.png)

Your Web browser knows how to find a site like example.com thanks to the global [Domain Name System](https://en.wikipedia.org/wiki/Domain_Name_System) (DNS), which serves as a kind of phone book for the Internet by translating human-friendly website names (example.com) into numeric Internet addresses.

When someone registers a domain name, the registrar will typically provide two sets of DNS records that the customer then needs to assign to their domain. Those records are crucial because they allow Web browsers to find the Internet address of the hosting provider that is serving that domain.

But potential problems can arise when a domain’s DNS records are “lame,” meaning the authoritative name server does not have enough information about the domain and can’t resolve queries to find it. A domain can become lame in a variety of ways, such as when it is not assigned an Internet address, or because the name servers in the domain’s authoritative record are misconfigured or missing.

The reason lame domains are problematic is that a number of Web hosting and DNS providers allow users to claim control over a domain *without accessing the true owner’s account at their DNS provider or registrar*.

If this threat sounds familiar, that’s because it is hardly new. Back in 2019, KrebsOnSecurity wrote about thieves employing this method to seize control over thousands of domains registered at GoDaddy, and using those [to send bomb threats and sextortion emails](https://krebsonsecurity.com/2019/01/bomb-threat-sextortion-spammers-abused-weakness-at-godaddy-com/) (GoDaddy says they fixed that weakness in their systems not long after that 2019 story).

In the 2019 campaign, the spammers created accounts on GoDaddy and were able to take over vulnerable domains simply by registering a free account at GoDaddy and being assigned the same DNS servers as the hijacked domain.

Three years before that, the same pervasive weakness was described in a blog post by security researcher **Matthew Bryant**, who showed how one could [commandeer at least 120,000 domains](https://thehackerblog.com/the-orphaned-internet-taking-over-120k-domains-via-a-dns-vulnerability-in-aws-google-cloud-rackspace-and-digital-ocean/) via DNS weaknesses at some of the world’s largest hosting providers.

Incredibly, new research jointly released today by security experts at **Infoblox** and **Eclypsium** finds this same authentication weakness is still present at a number of large hosting and DNS providers.

“It’s easy to exploit, very hard to detect, and it’s entirely preventable,” said **Dave Mitchell**, principal threat researcher at Infoblox. “Free services make it easier [to exploit] at scale. And the bulk of these are at a handful of DNS providers.”

## SITTING DUCKS

[Infoblox’s report](https://blogs.infoblox.com/threat-intelligence/who-knew-domain-hijacking-is-so-easy/) found there are multiple cybercriminal groups abusing these stolen domains as a globally dispersed “traffic distribution system,” which can be used to mask the true source or destination of web traffic and to funnel Web users to malicious or phishous websites.

Commandeering domains this way also can allow thieves to impersonate trusted brands and abuse their positive or at least neutral reputation when sending email from those domains, as we saw in 2019 with the GoDaddy attacks.

“Hijacked domains have been used directly in phishing attacks and scams, as well as large spam systems,” reads the Infoblox report, which refers to lame domains as “**Sitting Ducks**.” “There is evidence that some domains were used for Cobalt Strike and other malware command and control (C2). Other attacks have used hijacked domains in targeted phishing attacks by creating lookalike subdomains. A few actors have stockpiled hijacked domains for an unknown purpose.”

Eclypsium researchers [estimate](https://eclypsium.com/blog/ducks-now-sitting-dns-internet-infrastructure-insecurity/) there are currently about one million Sitting Duck domains, and that at least 30,000 of them have been hijacked for malicious use since 2019.

“As of the time of writing, numerous DNS providers enable this through weak or nonexistent verification of domain ownership for a given account,” Eclypsium wrote.

The security firms said they found a number of compromised Sitting Duck domains were originally registered by brand protection companies that specialize in defensive domain registrations (reserving look-alike domains for top brands before those names can be grabbed by scammers) and combating trademark infringement.

For example, Infoblox found cybercriminal groups using a Sitting Duck domain called **clickermediacorp[.]com**, which was a CBS Interactive Inc. domain initially registered in 2009 at GoDaddy. However, in 2010 the DNS was updated to DNSMadeEasy.com servers, and in 2012 the domain was transferred to **MarkMonitor**.

Another hijacked Sitting Duck domain — **anti-phishing[.]org** — was registered in 2003 by the **Anti-Phishing Working Group** (APWG), a cybersecurity not-for-profit organization that closely tracks phishing attacks.

In many cases, the researchers discovered Sitting Duck domains that appear to have been configured to auto-renew at the registrar, but the authoritative DNS or hosting services were not renewed.

The researchers say Sitting Duck domains all possess three attributes that makes them vulnerable to takeover:

1) the domain uses or delegates authoritative DNS services to a different provider than the domain registrar;
2) the authoritative name server(s) for the domain does not have information about the Internet address the domain should point to;
3) the authoritative DNS provider is “exploitable,” i.e. an attacker can claim the domain at the provider and set up DNS records without access to the valid domain owner’s account at the domain registrar.

![](https://krebsonsecurity.com/wp-content/uploads/2024/07/sittingduckattack.png)

Image: Infoblox.

How does one know whether a DNS provider is exploitable? There is a frequently updated list published on **GitHub** called “[Can I take over DNS](https://github.com/indianajson/can-i-take-over-dns?tab=readme-ov-file),” which has been documenting exploitability by DNS provider over the past several years. The list includes examples for each of the named DNS providers.

In the case of the aforementioned Sitting Duck domain clickermediacorp[.]com, the domain appears to have been hijacked by scammers by claiming it at the web hosting firm **DNSMadeEasy**, which is owned by **Digicert**, one of the industry’s largest issuers of digital certificates (SSL/TLS certificates).

In an interview wit...