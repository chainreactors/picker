---
title: Why is Italy a top target for cybercrime?
url: https://www.intel471.com/blog/why-is-italy-a-top-target-for-cybercrime
source: Over Security
date: 2026-11-04
fetch_date: 2026-11-05T08:44:52.331582
---

# Why is Italy a top target for cybercrime?

[![Intel 471](https://cdn.sanity.io/images/fo9xc2x1/production/93fea1393c1c41cc700e939325848b7117804e8f-678x209.png?h=76&fm=webp&fit=max&auto=format)](/)PlatformUse Cases[Why Intel 471](/why-intel-471)ResourcesCompany

Search[Send a request](/company/contact)

# Why is Italy a top target for cybercrime?

Nov 4, 2026

![](https://cdn.sanity.io/images/fo9xc2x1/production/8e17f8259ee64d48b497a899616a4a8af4952a7e-1440x730.png?w=1920&h=800&fm=jpg&q=95&fit=crop&crop=center&auto=format)

*Italy ranks second globally and first in Europe for initial accesses offered for sale in 2026. It was also the fourth most targeted country for ransomware and extortion in 2026. Why? Slow patching makes you an easy target for massive exploitation of known vulnerabilities.*

Initial access refers to compromised accounts, applications, and networks that initial access brokers (IABs) sell to other threat actors through underground cybercrime forums and private negotiations. This allows buyers, including ransomware and data extortion gangs, to gain an intrusion without having to conduct the initial compromise themselves. Our analysts monitor this access market to help assess which Italian organizations are exposed to further intrusion and how actors obtain and commercialize that access.

In our [new report](https://www.intel471.com/resources/whitepapers/initial-access-ransomware-and-vishing-how-threat-actors-are-targeting-italy-in-2026) looking at how threat actors are targeting Italy-based organizations, we found that Italy ranked second globally and first in Europe by the number of initial accesses offered for sale in 2026 in underground markets. Access to Italian organizations represented approximately 7% of all accesses offered worldwide, compared with 30% for the United States. We also found Italy was the fourth most targeted country in the world for ransomware and extortion and the second most targeted country in the European Union, after Germany, and ahead of the United Kingdom.

At a national level, higher rates of internet-connectivity and digitalization of workflows in businesses, hospitals and critical infrastructure increases the attack surface. More software means more vulnerabilities to patch. Wealth and geopolitical status contribute to targeting by both financially motivated and nation-state actors. So, why does Italy rank second globally for initial access offers and so highly as a target of ransomware?

#### **Slow patching puts Italy on attackers’ radar**

Gianluca Tiepolo, Intel 471 cybercrime analyst and author of the report explored what’s behind Italy’s outsized ranking in access offers. For our report, Tiepolo examined how actors packaged and marketed access targeting Italian organizations. He found that 90% of offers were for wholesale access involving multiple targets, while the remaining 10% for a specified target.

Per the report: “The prevalence of wholesale access is consistent with actors acquiring access through repeatable techniques or vulnerabilities in technologies that multiple organizations use. Once an actor develops an effective exploitation method, the actor can apply that method to additional exposed systems without conducting a separate, extensive reconnaissance effort against each organization.”

In simpler terms, the trend points to Italian organizations being easier targets because they’ve been slow to apply updates after security patches become available.

“Italy is very slow at patching and this results in massive exploitation of known vulnerabilities,” says Tiepolo. “The result is that Italy is targeted by wholesale access actors — not because they're particularly interested in Italy, it’s simply opportunistic targeting.”

The data supports this: vulnerability exploitation accounted for 57% of the access in Italy, well ahead of credential-based methods that dominated globally. This trend of lax patching was also evident in the [prevalence of Italian internet-facing services running end-of-life versions of PHP](https://modat.io/blog/php-exposure-before-the-21-oct-2026-security-release/) at the time the critical [PHP2Shell vulnerabilities (](https://www.intel471.com/blog/testing-a-php2shell-exploit-in-the-era-of-ai-hallucinated-pocs)CVE-2026-109618 and CVE-2026-109619) were disclosed. There are no official fixes expected for end-of-life versions of PHP.

"The data we saw last week from PHP2Shell, I think, validates this assessment. Italy is the country in Europe with the largest number of PHP 4, 5, and 7 versions, which are end-of-life," Tiepolo [told Dark Reading](https://www.darkreading.com/cybersecurity-analytics/cyber-vulnerabilities-besiege-italy).

#### **Ransomware: easy access, not just revenue, influences targeting**

Intel 471 identified Italian organizations as about 3% of global ransomware and extortion victims in 2026.

Among Italian victims with revenue estimates, 85% had annual revenue below US $50 million and 60% were below US $10 million. Ransomware activity therefore extended well beyond the large enterprises that tend to attract the most public attention. The prevalence of smaller businesses is consistent with operators selecting targets partly on the basis of available access and the effort required to complete an intrusion, rather than company size alone.

Organizations in the manufacturing and consumer and industrial products sectors together represented 46% of the Italian victims. Industrial products and services, along with retail, wholesale, and distribution, represent the top targeted industries for ransomware and extortion among Italian organizations, reflecting a heavy concentration of attacks across manufacturing and consumer/industrial product sectors. The concentration of victims in these industries makes disruption to enterprise IT a significant business risk even when an intrusion does not directly reach industrial control systems that operate high value production and supply chains.

![](/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Ffo9xc2x1%2Fproduction%2Fd94979486748e10cb972dfb88809e5634d3068c0-1218x784.png%3Fw%3D1218%26fm%3Dwebp%26q%3D90%26fit%3Dmax%26auto%3Dformat&w=3840&q=90)

The revenue category for Italian organizations impacted by ransomware in 2026.

Qilin, The Gentlemen and LockBit 5.0 together accounted for 40% of Italian ransomware activity. All three run as ransomware-as-a-service, where the core operators develop the ransomware and provide the infrastructure used to manage extortion, while affiliates, including IABs, conduct intrusions and deploy the malware in exchange for a share of ransom payments. [Law enforcement disrupted LockBit's infrastructure in 2024](https://www.intel471.com/blog/assessing-the-disruptions-of-ransomware-gangs), yet it returned as LockBit 5.0 and remains active against Italian organizations.

![](/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Ffo9xc2x1%2Fproduction%2F2ab91aa2c69754de5f213760493059eb26488c04-1502x952.png%3Fw%3D1502%26fm%3Dwebp%26q%3D90%26fit%3Dmax%26auto%3Dformat&w=3840&q=90)

Top five ransomware and extortion groups by numbers of claims against Italian organizations, January to September 2026. Source: Intel 471.

The Gentlemen show how operators plan to obstruct recovery. Leaked internal chats that Intel 471 analyzed described efforts to gain administrative access to FortiGate firewalls, take control of ESXi hosts and erase Veeam-managed backups. Anyone running that stack should read it as a map of what attackers want to reach. Our [threat hunting case study on The Gentlemen](https://www.intel471.com/blog/threat-hunting-case-study-the-gentlemen) covers the behaviors in more detail.

Initial access and ransomware trends are just part of the overall threat landscape for Italy-based organizations. [Download the full report](https://www.intel471.com/resources/whitepapers/initial-access-ransomware-and-vishing-how-threat-actors-are-targeting-italy-in-2026) to learn about each RaaS operator’s intrusion and lateral movement techn...