---
title: Shadow IT: The Initial Access You Didn’t Log
url: https://blog.sekoia.io/shadow-it-the-initial-access-you-didnt-log/
source: Over Security - Cybersecurity news aggregator
date: 2026-03-06
fetch_date: 2026-03-07T03:56:45.603714
---

# Shadow IT: The Initial Access You Didn’t Log

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

# Shadow IT: The Initial Access You Didn’t Log

[![](data:image/svg+xml...)![](https://secure.gravatar.com/avatar/28c7f8195a566b04453ac6788eb103d6eb119e36e8d17886f6057379433ab6b0?s=52&d=mm&r=g)](#molongui-disabled-link)

[David Greenwood](#molongui-disabled-link)
March 6 2026

0

5 minutes reading

In multiple incident response engagements over the past few years, one detail keeps repeating: the first compromised system wasn’t the one the SOC was watching. It wasn’t visible in the EDR console, it wasn’t tracked in the CMDB, and it wasn’t in scope for vulnerability management. It was real infrastructure owned by the organization but operationally invisible. Threat actors didn’t need to evade detection because they operated where detection didn’t exist. This is the practitioner reality of shadow IT, and if you read enough intrusion reports, from ransomware playbooks to cloud compromise research, the pattern becomes difficult to ignore.

Across investigations, the same root cause appears again and again: attackers map organizations differently than defenders do. Security teams typically map managed endpoints, production infrastructure, sanctioned SaaS platforms, and ingested telemetry sources. Attackers map everything externally attributable to the organization, domains, certificates, SaaS tenants, repositories, exposed services, and legacy infrastructure. The difference between those two maps is shadow IT, and adversaries actively search that gap because it offers legitimacy, low monitoring, and minimal resistance.

What follows are not theoretical risks, but recurring intrusion patterns documented in threat intelligence reporting and incident response.

---

## The Visibility Gap: Defender Map vs Attacker Map

Most SOC architectures are inward-facing: endpoints, AD, production servers, sanctioned SaaS, and log pipelines. Attackers start outward-facing: DNS history, certificate transparency logs, BGP allocations, public cloud resources, SaaS tenant sprawl, GitHub organizations, and forgotten edge systems. Shadow IT lives in the delta between those two views. Every intrusion case below is simply a different way attackers exploit that gap.

### Case 1: Unmanaged Edge Infrastructure as Ransomware Entry

![](data:image/svg+xml...)![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2026/03/ChatGPT-Image-Mar-3-2026-12_12_36-PM-1024x683.png)

Joint advisories from CISA and the FBI across 2023–2024 repeatedly warned that ransomware affiliates were gaining initial access through unpatched VPN appliances, exposed Citrix gateways, and legacy remote access infrastructure. Groups such as LockBit and BlackCat were observed exploiting edge systems that still authenticated users and routed traffic but no longer had EDR, SIEM ingestion, or patch ownership.

The attack chain is operationally simple: internet scanning identifies a vulnerable edge device; exploitation yields remote access; credentials are harvested; lateral movement proceeds using legitimate domain accounts; ransomware deployment follows weeks later. The diagram above is intentionally simple because the attack is simple. The complexity lies not in exploitation but in the fact that the compromised device was never in monitoring scope.

From the SOC perspective, detection begins only after domain activity becomes noisy. By then, the attacker has already established persistence.

### Case 2: Cloud Storage Repurposed as Attacker Infrastructure

![](data:image/svg+xml...)![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2026/03/ChatGPT-Image-Mar-3-2026-12_14_39-PM-1024x683.png)

After the [Capital One breach](https://www.justice.gov/usao-wdwa/pr/seattle-tech-worker-arrested-data-theft-affecting-capital-one) and subsequent IAM-focused investigations, incident response reporting, particularly from Mandiant, has repeatedly documented attackers discovering organization-owned storage and using it as operational infrastructure. The pattern is consistent: enumerate exposed buckets; extract configuration data; use storage for staging; exfiltrate data over legitimate HTTPS to a company-owned endpoint.

From the SOC console, the traffic appears as encrypted outbound communication to a trusted domain. No malicious destination. No obvious C2 infrastructure. The diagram illustrates why this works: the exfiltration path never leaves “trusted” cloud infrastructure. If the bucket was never registered in the asset inventory, there is no baseline, no monitoring, and no alerting. The breach path is not just misconfiguration; it is a failure to map cloud surface area continuously.

### Case 3: OAuth Persistence in an Unmanaged Tenant

![](data:image/svg+xml...)![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2026/03/ChatGPT-Image-Mar-3-2026-12_16_35-PM-1024x683.png)

In 2023, [Microsoft disclosed activity linked to Storm-0558 involving forged authentication tokens and unauthorized access to cloud email systems](https://www.microsoft.com/en-us/security/blog/2023/12/12/threat-actors-misuse-oauth-applications-to-automate-financially-driven-attacks/?utm_source=chatgpt.com). While that campaign relied on advanced token abuse, broader identity threat reporting continues to highlight OAuth abuse as a durable persistence mechanism.

The operational pattern in unmanaged tenants is straightforward: compromise a user; register an OAuth application; grant delegated API permissions; maintain access independent of password resets. The diagram above shows why SOCs often miss this: activity occurs entirely at the identity and API layer. There is no malware, no suspicious process tree, and no endpoint telemetry trigger. If the tenant itself is outside monitoring scope, the attack chain unfolds invisibly.

Shadow IT here is identity surface area expanding faster than governance.

### Case 4: Developer Ecosystem to Cloud Compromise

![](data:ima...