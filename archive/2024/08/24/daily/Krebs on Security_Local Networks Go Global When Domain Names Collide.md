---
title: Local Networks Go Global When Domain Names Collide
url: https://krebsonsecurity.com/2024/08/local-networks-go-global-when-domain-names-collide/
source: Krebs on Security
date: 2024-08-24
fetch_date: 2025-10-06T18:07:51.446834
---

# Local Networks Go Global When Domain Names Collide

Advertisement

[![](/b-gartner/7.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

Advertisement

[![](/b-sysdig/2.png)](https://content.foleon.com/sysdig/sysdig-cloud-defense-report-2025/?utm_source=krebs-on-security&utm_medium=display&utm_campaign=aware_amer_the-right-way_na_ung_display&utm_content=AD000462_1240x160)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Local Networks Go Global When Domain Names Collide

August 23, 2024

[37 Comments](https://krebsonsecurity.com/2024/08/local-networks-go-global-when-domain-names-collide/#comments)

The proliferation of new top-level domains (TLDs) has exacerbated a well-known security weakness: Many organizations set up their internal Microsoft authentication systems years ago using domain names in TLDs that didn’t exist at the time. Meaning, they are continuously sending their Windows usernames and passwords to domain names they do not control and which are freely available for anyone to register. Here’s a look at one security researcher’s efforts to map and shrink the size of this insidious problem.

![](https://krebsonsecurity.com/wp-content/uploads/2024/08/tld-cloud.png)

At issue is a well-known security and privacy threat called “[namespace collision](https://www.computerworld.com/article/3480799/icann-seeks-to-tackle-dns-namespace-collision-risks.html),” a situation where domain names intended to be used exclusively on an internal company network end up overlapping with domains that can resolve normally on the open Internet.

Windows computers on a private corporate network validate other things on that network using a Microsoft innovation called [Active Directory](https://en.wikipedia.org/wiki/Active_Directory), which is the umbrella term for a broad range of identity-related services in Windows environments. A core part of the way these things find each other involves a Windows feature called “[DNS name devolution](https://www.itprotoday.com/security/whats-dns-name-devolution),” a kind of network shorthand that makes it easier to find other computers or servers without having to specify a full, legitimate domain name for those resources.

Consider the hypothetical private network internalnetwork.example.com: When an employee on this network wishes to access a shared drive called “drive1,” there’s no need to type “drive1.internalnetwork.example.com” into Windows Explorer; entering “\\drive1\” alone will suffice, and Windows takes care of the rest.

But problems can arise when an organization has built their Active Directory network on top of a domain they don’t own or control. While that may sound like a bonkers way to design a corporate authentication system, keep in mind that many organizations built their networks long before the introduction of hundreds of new top-level domains (TLDs), like .network, .inc, and .llc.

For example, a company in 2005 builds their Microsoft Active Directory service around the domain **company.llc**, perhaps reasoning that since .llc wasn’t even a routable TLD, the domain would simply fail to resolve if the organization’s Windows computers were ever used outside of its local network.

Alas, in 2018, the .llc TLD was born and began selling domains. From then on, anyone who registered company.llc would be able to passively intercept that organization’s Microsoft Windows credentials, or actively modify those connections in some way — such as redirecting them somewhere malicious.

**Philippe Caturegli**, founder of the security consultancy [Seralys](https://www.seralys.com), is one of several researchers seeking to chart the size of the namespace collision problem. As a professional penetration tester, Caturegli has long exploited these collisions to attack specific targets that were paying to have their cyber defenses probed. But over the past year, Caturegli has been gradually mapping this vulnerability across the Internet by looking for clues that appear in self-signed security certificates (e.g. SSL/TLS certs).

Caturegli has been scanning the open Internet for self-signed certificates referencing domains in a variety of TLDs likely to appeal to businesses, including **.ad, .associates, .center, .cloud, .consulting, .dev, .digital, .domains, .email, .global, .gmbh, .group, .holdings, .host, .inc, .institute, .international, .it, .llc, .ltd, .management, .ms, .name, .network, .security, .services, .site, .srl, .support, .systems, .tech, .university, .win** and **.zone**, among others.

Seralys found certificates referencing more than 9,000 distinct domains across those TLDs. Their analysis determined many TLDs had far more exposed domains than others, and that about 20 percent of the domains they found ending .ad, .cloud and .group remain unregistered.

“The scale of the issue seems bigger than I initially anticipated,” Caturegli said in an interview with KrebsOnSecurity. “And while doing my research, I have also identified government entities (foreign and domestic), critical infrastructures, etc. that have such misconfigured assets.”

## REAL-TIME CRIME

Some of the above-listed TLDs are not new and correspond to country-code TLDs, like **.it** for Italy, and **.ad**, the country-code TLD for the tiny nation of [Andorra](https://en.wikipedia.org/wiki/Andorra). Caturegli said many organizations no doubt viewed a domain ending in .ad as a convenient shorthand for an internal **A**ctive **D**irectory setup, while being unaware or unworried that someone could actually register such a domain and intercept all of their Windows credentials and any unencrypted traffic.

When Caturegli discovered an encryption certificate being actively used for the domain **memrtcc.ad,** the domain was still available for registration. He then learned the .ad registry requires prospective customers to show a valid trademark for a domain before it can be registered.

Undeterred, Caturegli found a domain registrar that would sell him the domain for $160, and handle the trademark registration for another $500 (on subsequent .ad registrations, he located a company in Andorra that could process the trademark application for half that amount).

Caturegli said that immediately after setting up a DNS server for memrtcc.ad, he began receiving a flood of communications from hundreds of Microsoft Windows computers trying to authenticate to the domain. Each request contained a username and a hashed Windows password, and upon searching the usernames online Caturegli concluded they all belonged to police officers in Memphis, Tenn.

“It looks like all of the police cars there have a laptop in the cars, and they’re all attached to this memrtcc.ad domain that I now own,” Caturegli said, noting wryly that “memrtcc” stands for “**Memphis Real-Time Crime Center**.”

Caturegli said setting up an email server record for memrtcc.ad caused him to begin receiving automated messages from the police department’s IT help desk, including trouble tickets regarding the city’s Okta authentication system.

**Mike Barlow**, information security manager for the City of Memphis, confirmed the Memphis Police’s systems were sharing their Microsoft Windows credentials with the domain, and that the city was working with Caturegli to have the domain transferred to them.

“We are working with the Memphis Police Department to at least somewhat mitigate the issue in the meantime,” Barlow said.

Domain administrators have long been encouraged to use **.local** for internal domain names, because this TLD is [reserved for use by local networks](https://en.wikipedia.org/wiki/.local) and cannot be routed over the ope...