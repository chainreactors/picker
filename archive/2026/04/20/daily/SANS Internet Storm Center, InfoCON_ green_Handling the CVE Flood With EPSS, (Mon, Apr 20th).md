---
title: Handling the CVE Flood With EPSS, (Mon, Apr 20th)
url: https://isc.sans.edu/diary/rss/32914
source: SANS Internet Storm Center, InfoCON: green
date: 2026-04-20
fetch_date: 2026-04-21T04:51:54.860617
---

# Handling the CVE Flood With EPSS, (Mon, Apr 20th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Xavier Mertens](/handler_list.html#xavier-mertens "Xavier Mertens")

Threat Level: [green](/infocon.html)

* [previous](/diary/32904)

Click [HERE](https://www.sans.org/profiles/xavier-mertens) to learn more about classes Xavier is teaching for SANS

# [Handling the CVE Flood With EPSS](/forums/diary/Handling%2Bthe%2BCVE%2BFlood%2BWith%2BEPSS/32914/)

**Published**: 2026-04-20. **Last Updated**: 2026-04-20 06:43:22 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/Handling%2Bthe%2BCVE%2BFlood%2BWith%2BEPSS/32914/#comments)

Every morning, security people around the world face the same ritual: opening their vulnerability feed to find a lot of new CVE entries that appeared overnight. Over the past decade, this flood has become a defining challenge of modern defensive security. Some numbers[[1](https://www.cvedetails.com/browse-by-date.php)]:

* CVEs published in 2023: 29K+
* CVEs published in 2024: 40K+
* New CVEs per day: ~110
* Exploited in the wild: ~5-7%

The root cause of this explosion is structural: the security research community has grown dramatically, bug bounty programs, automated scanning has industrialised vulnerability discovery, and software supply chains expose orders of magnitude more attack surface than legacy monolithic architectures ever did. And don’t forget AI used more and more to find vulnerabilities!

Every CVE receives a CVSS (Common Vulnerability Scoring System) that is a score between 0 and 10 attempts to express the intrinsic severity of a vulnerability. This score is based on core questions like: How bad it is if exploited? How complex exploitation is? What privileges are required? And what impact on confidentiality, integrity, and availability to expect?

CVSS is a well-designed standard, and is useful. But it remains challenging to perform the initial triage: Which CVEs deserve to be investigated first? A CVSS 9.8 that sits dormant in an obscure software is less dangerous in practice than a CVSS 6.5 actively chained in ransomware campaigns!

The Exploit Prediction Scoring System (EPSS) was developed by FIRST (Forum of Incident Response and Security Teams)[[2](https://www.first.org/epss/)] and has gone through successive iterations since its public launch in 2021, with EPSS v3 released in March 2023 as the current production model. Its design philosophy is fundamentally different from CVSS: instead of rating theoretical impact, EPSS answers a probabilistic question. We already talked about EPSS a long time ago[[3](https://isc.sans.edu/diary/EPSScall%2BAn%2BExploit%2BPrediction%2BScoring%2BSystem%2BApp/28732)] but it does get enough attention from the community (IMHO)

How does it work?

EPSS = P(exploitation within 30 days | CVE is published)
Score range: 0.00001 → 1.0 (probability)
Model: gradient-boosted machine learning (XGBoost)
Input features: ~1,400 signals updated daily
Data sources: exploit databases, darkweb telemetry, threat intel feeds, PoC repositories, NVD metadata

Theory is nice but let’s be more pragmatic! FIRST offers an API to query for EPSS scores:

```

$ curl -s https://api.first.org/data/v1/epss?cve=CVE-2026-23099 | jq .
{
  "status": "OK",
  "status-code": 200,
  "version": "1.0",
  "access": "public",
  "total": 1,
  "offset": 0,
  "limit": 100,
  "data": [
    {
      "cve": "CVE-2026-23099",
      "epss": "0.000180000",
      "percentile": "0.044770000",
      "date": "2026-04-19"
    }
  ]
}
```

How to automate this? Most SIEM or log management solutions can interact with external services through APIs. Let me show you how I enrich my vulnerabilities alert in Wazuh.

I set up an integration[[4](https://documentation.wazuh.com/current/integrations-guide/index.html)] that will query the EPSS score of CVEs detected in my environment:

A Python script will be invoked when a vulnerability is detected (with alert group "vulnerability-detector", the fetched EPSS score will be used to create a new alert with more relevant data:

```

<integration>
  <name>custom-epss</name>
  <group>vulnerability-detector</group>
  <alert_format>json</alert_format>
</integration>
```

The new rules:

```

<group name="epss,vulnerability,enrichment">
  <rule id="120200" level="3">
    <decoded_as>json</decoded_as>
    <field name="integration">epss</field>
    <description>EPSS enrichment event received for $(epss.cve)</description>
    <options>no_full_log</options>
  </rule>

  <rule id="120201" level="5">
    <if_sid>120200</if_sid>
    <field name="epss.risk_label">low</field>
    <description>EPSS: $(epss.cve) — Low exploitation probability (score=$(epss.score_pct)%)</description>
  </rule>

  <rule id="120202" level="9">
    <if_sid>120200</if_sid>
    <field name="epss.risk_label">medium</field>
    <description>EPSS: $(epss.cve) — Medium exploitation probability (score=$(epss.score_pct)%)</description>
  </rule>

  <rule id="120203" level="12">
    <if_sid>120200</if_sid>
    <field name="epss.risk_label">high</field>
    <description>EPSS: $(epss.cve) — High exploitation probability (score=$(epss.score_pct)%)</description>
  </rule>

  <rule id="120204" level="15">
    <if_sid>120200</if_sid>
    <field name="epss.risk_label">critical</field>
    <description>EPSS: $(epss.cve) — CRITICAL exploitation probability (score=$(epss.score_pct)%)</description>
    <group>pci_dss_6.3.3,nist_800_53_SI.2,gdpr_IV_35.7.d,hipaa_164.308.a.5,tsc_CC7.1</group>
  </rule>

  <rule id="120205" level="3">
    <if_sid>120200</if_sid>
    <field name="epss.cached">True</field>
    <description>EPSS: $(epss.cve) — Score served from local cache (age &lt; 24h)</description>
  </rule>
</group>
```

Here is an example of alert:

![](https://isc.sans.edu/diaryimages/images/isc-20260420-2.png)

The script sets the risk based on this:

```

if score >= 0.90:
    return "critical"
if score >= 0.50:
    return "high"
if score >= 0.10:
    return "medium"
return "low"
```

The Python integration script is available here[[5](https://xameco.be/files/custom-epss.py)].

[1] <https://www.cvedetails.com/browse-by-date.php>
[2] <https://www.first.org/epss/>
[3] [https://isc.sans.edu/diary/EPSScall+An+Exploit+Prediction+Scoring+System+App/28732](https://isc.sans.edu/diary/EPSScall%2BAn%2BExploit%2BPrediction%2BScoring%2BSystem%2BApp/28732)
[4] <https://documentation.wazuh.com/current/integrations-guide/index.html>
[5] <https://xameco.be/files/custom-epss.py>

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [Vulnerability](/tag.html?tag=Vulnerability) [EPSS](/tag.html?tag=EPSS) [CVSS](/tag.html?tag=CVSS) [CVE](/tag.html?tag=CVE) [Wazuh](/tag.html?tag=Wazuh)

[0 comment(s)](/diary/Handling%2Bthe%2BCVE%2BFlood%2BWith%2BEPSS/32914/#comments)

Click [HERE](https://www.sans.org/profiles/xavier-mertens) to learn more about classes Xavier is teaching for SANS

* [previous](/diary/32904)

### Comments

[Login here to join the discussion.](/login)

Top of page

×

![modal content]()

[Diary Archives](/diaryarchive.html)

* [![SANS.edu research journal](https://isc.sans.edu/images/researchjournal5.png)](/j/research)
* [Homepage](/index.html)
* [Diaries](/diaryarchive.html)
* [Podcasts](/podcast.html)
* [Jobs](/jobs)
* [Data](/data)
  + [TCP/UDP Port Activity](/data/port.html)
  + [Port Trends](/data/trends.html)
  + [SSH/Telnet Scanning Activity](/data/ssh.html)
  + [Weblogs](/weblogs)
  + [Domains](/data/domains.html)
  + [Threat Feeds Activity](/data/threatfeed.html)
  + [Threat Feeds Map](/data/threatmap.html)
  + [Useful InfoSec Links](/data/links.html)
  + [Presentations & Papers](/data/presentation.html)
  + [Research Papers](/data/researchpapers.html)
  + [API](/api)
* [Tools](/tools/)
  + [DShield Sensor](/howto.html)
  + [DNS Looking Glass](/tools/dnslookup)
  + [Honeypot (RPi/AWS)](/tools/honeypot)
  + [InfoSec Glossa...