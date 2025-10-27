---
title: Securing Gold : Hunting typosquatted domains during the Olympics
url: https://blog.sekoia.io/securing-gold-hunting-typosquatted-domains-during-the-olympics/
source: Over Security - Cybersecurity news aggregator
date: 2024-09-12
fetch_date: 2025-10-06T18:31:25.531378
---

# Securing Gold : Hunting typosquatted domains during the Olympics

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

[![logo sekoia.io blog light](data:image/svg+xml...)![logo sekoia.io blog light](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2023/03/cropped-logo-sekoia-io-blog-light.png)](https://blog.sekoia.io/)

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

[Threat Research & Intelligence](https://blog.sekoia.io/category/threat-research/ "Threat Research & Intelligence")

# Securing Gold : Hunting typosquatted domains during the Olympics

[![](data:image/svg+xml...)![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2023/04/logo-sekoia-symbol-6.png)](#molongui-disabled-link)

[Maxime A., Amaury G., Coline Chavane and Sekoia TDR](#molongui-disabled-link)
September 11 2024

0

6 minutes reading

Anticipating Paris 2024 Olympics cyber threats, Sekoia.io has conducted **over July and August 2024** a proactive **hunting of Olympics-typosquatted domains** registered by malicious actors – cybercrime related and possibly APT campaigns – in order to detect any kind of operations though the detection of connexion to typosquatted domains (phishing, C2).

This work is complementary to **our general assessment of cyber threats on Paris Olympics**, [published](https://blog.sekoia.io/securing-gold-assessing-cyber-threats-on-paris-2024/) in January 2024. As stated at that time, every Olympic event is a boon for malicious actors, in particular for cybercrime-related, lucrative actors leveraging the Games to conduct campaigns involving phishing attacks, fraud schemes such as fake ticketing or online betting solutions.

We also estimated a risk for state sponsored-related cyber espionage or destructive operations, but **no major incidents** were reported in open source.

In this blogpost, we will expose our hunting techniques and analyse the suspicious domains we detected.

## **Our hunting typosquatted domains process**

Since early June 2024, the Sekoia Threat Detection & Research (TDR) team has been applying a methodology to **detect domain names attempting to fake official websites** responsible for the Paris 2024 Olympic Games. The objective of this monitoring was to **record the opportunistic websites newly registered**, on a day-to-day basis, and to investigate each infrastructure in detail to find malicious activity.

To achieve this, we established a comprehensive list of **legitimate and official domain** names related to the Olympics. In total, we identified over **149 legitimate domain names pertaining to 110 different sectors**. This list includes official websites dedicated to the Olympic Games, institutional entities, media partners, international partners and the cities in France hosting the events.

Based on this, we setted up DNS Fuzzing using the [DNSTwist](https://github.com/elceef/dnstwist) security tool. It is designed to detect typosquatting and phishing attempts by identifying possible permutations of domain names. It generates potential variations of a domain, checks whether these domains are active and inspects SSL certificates. Furthermore, a Censys request has been designed to monitor SSL certificates granted for newly created domains.

```
(
          names:/olympics2024\..*/
          OR names:/jo2024\..*/
          OR names:/olympics2024\..*/
          OR names:/paris2024\..*/
          OR names:/sports.gouv\..*/
          OR names:/pass-jeux\..*/
          OR names:/anticiperlesjeux\..*/
          OR names:/ticketparis2024\..*/
          OR names:/transport-public-paris-2024\..*/
          OR names:/iledefrance-mobilites\..*/
          [...]
)
          AND parsed.validity_period.not_before:[ now-10d TO * ]
```

## **Our results**

From 13 June 2024 to 13 August 2024 – cut-off date for this paper – we found, assessed and monitored through the Sekoia SOC platform **more than 650 typosquatted Paris 2024 domains**. They are all in detection and linked to the STIX Infrastructure object named [Typosquatted domain names for the 2024 Olympic Games](https://app.sekoia.io/objects/infrastructure--40569a77-0f4a-45ba-ac11-88604ce54283), that we created for capitalising.

First, it was interesting to observe a **higher volume** of registration in the **weeks before the Olympics**, with **a spike** on the days before the opening ceremony. We compiled all registration dates in the following scheme.

![Typosquatted domain names for the 2024 Olympic Games.](data:image/svg+xml...)![Typosquatted domain names for the 2024 Olympic Games.](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2024/09/timeline2-1024x741.png)

The spike in registration on the days before the opening ceremony coincided with a worldwide media attention to the incoming event, with the arrival of national teams, athletes and foreign media. It shows the **opportunistic approach** to the majority of Olympics-typostatted domains.
We worked on **sorting the domains** through their **supposed type** of cybercrime-related objectives or lucrative finality.

![Distribution of typosquatted websites types](data:image/svg+xml...)![Distribution of typosquatted websites types](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2024/09/secteurs.png)

### **Ticketing scam**

Among the 650 domains we found and were able to qualify, close to 45% seems to be mimicking a ticketing selling or reselling platform. For example the following tickets.paris2024[.]biz, paris2024.ticket[.]net, tickets.paris2024[.]app, paris2024[.]app or tickets-paris2024[.]org are typosquatting the **official Paris2024 selling platform hosted at https://tickets.paris2024.org/**.

Of note, we observed a **large bulk of simultaneously registered domains**, the same day and with the same registrar. We assess it is **likely a defensive operation from organisers or national partners,** looking to anticipate typosquatting related to ticket scamming. All domains were lookalike, such as tickets.pa4ris2024[.]org, tickets.paaris2024[.]org, tickets.pabis2024[.]org or tickets.padis2024[.]org and probably were registered with a similar technique to DNSTwist described earlier, in order to block similar but malicious domain registration.

### **French official security organisation**

We observed a significant number of typosquatted domains mimicking French official ...