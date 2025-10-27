---
title: Blocklist in Sekoia
url: https://blog.sekoia.io/blocklist-in-sekoia/
source: Over Security - Cybersecurity news aggregator
date: 2024-12-04
fetch_date: 2025-10-06T19:41:24.249725
---

# Blocklist in Sekoia

### Log in

Username or Email Address

Password

[ ]  Remember Me

 [Forgot password?](https://blog.sekoia.io/wp-login.php?action=lostpassword)

### Search the site...

Search for

* All categories
* [Threat Research & Intelligence](https://blog.sekoia.io/category/threat-research/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [SOC Insights & Other News](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Detection Engineering](https://blog.sekoia.io/category/detection-engineering/)

####

Reset

[![logo sekoia.io blog light](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2023/03/cropped-logo-sekoia-io-blog-light.png)](https://blog.sekoia.io/)

* [Threat Research](https://blog.sekoia.io/category/threat-research/)
* [Detection](https://blog.sekoia.io/category/detection-engineering/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [Other](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Sign up](https://go.sekoia.io/Preference-center-EN.html)
* [About Sekoia.io](https://www.sekoia.io/en/about/)
  + [TDR Team](https://www.sekoia.io/en/about-threat-detection-research-team/)
  + [AI-SOC platform](https://www.sekoia.io/en/homepage/)
  + [Interactive demo](https://sekoia.storylane.io/share/8zdjfok9atpn)
  + [Contact Us](https://www.sekoia.io/en/contact/)

* [Threat Research](https://blog.sekoia.io/category/threat-research/)
* [Detection](https://blog.sekoia.io/category/detection-engineering/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [Other](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Sign up](https://go.sekoia.io/Preference-center-EN.html)
* [About Sekoia.io](https://www.sekoia.io/en/about/)
  + [TDR Team](https://www.sekoia.io/en/about-threat-detection-research-team/)
  + [AI-SOC platform](https://www.sekoia.io/en/homepage/)
  + [Interactive demo](https://sekoia.storylane.io/share/8zdjfok9atpn)
  + [Contact Us](https://www.sekoia.io/en/contact/)

Log in

[SOC Insights & Other News](https://blog.sekoia.io/category/soc-insights-other-news/ "SOC Insights & Other News")

# Implementing blocklists in the Sekoia SOC platform

[![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2023/04/logo-sekoia-symbol-6.png)](#molongui-disabled-link)

[SEKOIA.IO](#molongui-disabled-link)
December 3 2024

0

3 minutes reading

On a calm Friday afternoon, rumors of a new active threat starts hitting the various social network websites. Your CSIRT team starts checking the private channels they have with other CERTs and starts compiling a list of Indicators of Compromise (IoCs). After careful consideration, they decided to block all communications with these IoCs on the company’s firewalls. However the network administrator is off, enjoying an early week-end with his family.

Your security analysts might also be providing IoCs, through their investigation of alerts or incidents: they can come across specific technical artifacts such as IP addresses, domain names or URLs that characterize the presence of a threat to your information system. After proper qualification, these artifacts could become IoCs and could be leveraged proactively in security solutions to enhance detection and/or prevention.

Minemeld would have been my top choice to implement a blocklist in a centralized tool and distribute easily the content to third party solutions, but it has been announced as end of life by Palo Alto in 2021 and the public repository has been archived in 2023.

Let’s see how we can implement a blocklist using the Sekoia SOC platform capabilities!

## Using Sekoia’s IOC Collections as blocklists

![Using Sekoia IoC Collections as blocklists](data:image/svg+xml...)![Using Sekoia IoC Collections as blocklists](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2024/12/image1xxx-1024x575.png)

In the Sekoia SOC platform, custom IoCs can be stored in IoC Collections: they are defined in STIX format, linked to threats and possess validity dates allowing analysts to provide context around the IoCs and reduce the risk of false positives.

A security analyst can create a detection rule to detect these IoCs in the events collected in the Sekoia SOC platform, [perform threat hunting](https://blog.sekoia.io/hunting-for-iocs-from-singles-searches-to-an-automated-and-repeatable-process/) through the telemetry reports or automatically: Sekoia.io’s solution includes an automatic retro hunt engine searching through all the events stored in the platform for any new indicator added to an IoC Collection.

This centralized storage of IoCs is also key to ease lives of security analysts, network engineers and system administrators for proactively blocking threats as the Sekoia SOC platform allows to disseminate the blocklist content into various third-party solutions. Using the validity dates and revocation features of IOC Collections, security analysts can also easily extend the retention period of an IoC in a blocklist or remove them from the blocklist.

![IoCs shared by another CERT](data:image/svg+xml...)![IoCs shared by another CERT](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2024/12/image2xzfazf-1024x515.png)

Sekoia’s recommendation is to create one IOC Collection per IOC type that will be disseminated to third party solutions, to ease the integration in these tools and the maintainability of the IOC collections.

Finally, security analysts can enrich and grow IOC Collections quickly from Alerts using the pre-built playbook templates available in the Sekoia SOC platform.

![Add Destination IP address to IoC collection](data:image/svg+xml...)![Add Destination IP address to IoC collection](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2024/12/image3zczfezgzg-1024x920.png)

## Implementing the blocklist in a network firewall

The easiest option to perform automatic blocking of IP addresses on network firewalls is to use the native firewall capabilities to retrieve external lists. Depending on the vendor, the functionality can take various names : External Dynamic List (Palo Alto), Custom Intelligence Feed (CheckPoint), External Block List (Fortinet)…

The IoC Collection content can be retrieved in various formats to meet the network firewalls specifications: our [public documentation](https://docs.sekoia.io/xdr/usecases/playbook/implement_blocklist/) describes how an IoC Collection can be retrieved.

## Implementing the blocklist in third party solutions using playbook actions

The Sekoia SOC platform also comes with a native SOAR engine, allowing security analysts to launch automations manually or automatically on Alerts or Incidents, without having to switch to another solution or interface.

These automation features can also be used to retrieve the IoCs in the IoC Collection and push them to various security solutions such as EDR (CrowdStrike, SentinelOne, …) or SWG solutions (Zscaler).

Some of these solutions allow to define expiration dates on imported indicators – others do not, which can lead to some difficulties in maintaining the list of indicators. When the appropriate API endpoints are available, specific calls to these APIs were implemented in the automation action code to remove expired indicators from the third party solutions. You can check the code of our automation actions in our public [Github repository](https://github.com/SEKOIA-IO/automation-library/).

## Wrapping it up

Automating blocklist implementation across various security solutions is a great way to save time it takes for security analysts, network engineers and system administrators to put protective measures in place when facing a threat.

The native capabilities of the Sekoia SOC Platform allow you to implement this automated process without having to rely on an intermediary solution.

[Read more in our public documentation!](https://docs.sekoia.io/xdr/usecases/playbook/implement_blocklist/)

Share

[Blocklist](https://blog.sekoia.io/tag/blocklist/)
[Detection](https...