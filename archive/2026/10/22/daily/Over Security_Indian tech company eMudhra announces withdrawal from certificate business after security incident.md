---
title: Indian tech company eMudhra announces withdrawal from certificate business after security incident
url: https://therecord.media/indian-tech-company-announces-withdrawal-certificate-business-incident
source: Over Security
date: 2026-10-22
fetch_date: 2026-10-23T06:46:30.468855
---

# Indian tech company eMudhra announces withdrawal from certificate business after security incident

![](https://recordedfuture.matomo.cloud/matomo.php?idsite=2&rec=1)

[![Cyber Security News  | The Record](https://cms.therecord.media/uploads/The_Record_Centered_9b27d79125.svg)](/)

* [Leadership](/news/leadership)
* [Cybercrime](/news/cybercrime)
* [Nation-state](/news/nation-state)
* [Influence Operations](/news/influence-operations)
* [Technology](/news/technology)

* [Cyber Daily®](https://therecord.media/subscribe)
* [Click Here Podcast](/podcast)

Go

Subscribe to The Record

[✉️ Free Newsletter](/subscribe)

![digital](https://cms.therecord.media/uploads/large_vulnerability_digital_64411ae86a.jpg)

Image: Getty via Unsplash+

[Jonathan Greig](/author/jonathan-greig)October 22nd, 2026

# Indian tech company eMudhra announces withdrawal from certificate business after security incident

One of the only Indian root certificate authorities trusted by major web browsers said it is withdrawing from the global certificate business after facing significant backlash over a security incident this week.

The company, eMudhra, said it was voluntarily withdrawing from the global SSL/TLS certificate business after the private keys of eight of its intermediate certificates were found to be weak, prompting browsers like [Firefox](https://groups.google.com/a/mozilla.org/g/dev-security-policy/c/0R3XLJL6FuE/m/Kp1v6CPuAAAJ?pli=1), Apple and [Chrome](https://blog.google/security/protecting-chrome-and-android-users-from-compromised-emudhra-intermediate-ca-certificates/) to block the certificates.

According to Google, [Mozilla](https://blog.mozilla.org/security/2026/10/20/protecting-firefox-users-following-the-compromise-of-emudhra-intermediate-certificates/) and several other companies, the keys could allow attackers to issue fraudulent HTTPS certificates for websites they do not control. An attacker who could intercept a user’s connection could use those certificates to impersonate websites and potentially read or modify traffic.

Cloudflare [explained](https://blog.cloudflare.com/emudhra-certificate-compromise/) that the certificates were widely trusted by their own system as well as browsers and operating systems. Because of the weak keys, any attacker could create a forged certificate for any domain and use it to impersonate servers to intercept or modify traffic.

The issue was publicized by cybersecurity researcher Scott Helme, who [published](https://scotthelme.co.uk/eight-bits-of-trust-emudhras-ca-keys-cracked-in-milliseconds/) a blog saying that instead of a random 384-bit number, one of the private keys was just the number four. Others were simply 56 and 115.

eMudhra [said](https://emudhra.com/en/post/certificate-security-incident) this week that the certificates were created during a ceremony in April 2025 and the ”problem was a flaw in one step of the ceremony procedure.” The issue went undetected for 18 months and survived two independent audits before a researcher reverse engineered the weak keys, the company said.

eMudhra’s chairman, V. Srinivasan, said on Thursday that the company revoked the affected certificates within 14 hours of their discovery and claimed there were no compromises or data breaches as a result of the issue.

India’s Ministry of Electronics and IT [said](https://x.com/goi_meity/status/2112914708261179404) it is investigating the incident but defended the company, arguing that “some social media accounts are indulging in fear mongering about the impact of this incident.”

CERT-IN [warned](https://www.cert-in.org.in/s2cMainServlet?pageid=PUBVLNOTES02&VLCODE=CIAD-2026-0050) in its own alert that an attacker able to exploit the compromised private keys could "potentially impersonate legitimate websites or intercept or modify data exchanged between users and servers, potentially facilitating credential theft, sensitive data exposure and financial fraud."

They added that the ability to issue fraudulent certificates would also enable malicious software to appear to be digitally signed by a trusted publisher.

## Withdrawing

In the announcement of its withdrawal from the certificate business, Srinivasan said it only accounted for 1% of the company’s revenue but became increasingly costly due to compliance requirements and “complexity.”

Srinivasan blamed “social media amplification” for the increased scrutiny around the company. eMudhra said it will work with browser programs and customers to transition them to other options.

“Revocation and certificate status services will keep running until every issued certificate has expired or been replaced. eMudhra will complete its remaining commitments to the browser root programs, including a full root-cause report,” the company said.

Google noted that eMudhra has committed to working with impacted subscribers to migrate customers off of the impacted root but said it is “closely investigating the ongoing inclusion of eMudhra's remaining CA certificates in the Chrome Root Store.”

Brian Fox, co-founder of cybersecurity firm Sonatype, told Recorded Future News that the issue goes far beyond browsers because certificate trust stores are embedded in dozens of products.

Each may require its own update, rebuild or release, and most organizations don’t have an inventory of where they live, he said.

“That makes this a software supply chain problem, not just a certificate revocation event. The fixes started shipping within days, but finding and adopting them is now the challenge,” he said.

“The long tail will be older releases, forgotten containers, embedded devices, and vendor tools that carry their own certificate bundles. Although now revoked, the original eMudhra-issued intermediates were not due to expire until April 2040, and outdated clients that do not process revocation information may continue trusting the affected chains until they are updated.”

* [Cybercrime](/news/cybercrime)
* [Industry](/)
* [News](/ukraine-says-starshield-working-again-after-disruption)

[![Recorded Future](https://cms.therecord.media/uploads/2025_0514_Record_Ads_300x1050_1_0f2f11757e.png)](https://www.recordedfuture.com/?utm_source=therecord&utm_medium=referral&utm_content=post-sidebar-ad)

[![Recorded Future](https://cms.therecord.media/uploads/2025_0514_Record_Ads_970x250_1_d144dbf901.png)](https://www.recordedfuture.com/?utm_source=therecord&utm_medium=referral&utm_content=post-footer-ad)

No previous article

No new articles

[![Jonathan Greig](https://cms.therecord.media/uploads/DSC_0283_1_a6f4e4e315.jpg)](/author/jonathan-greig)

[Jonathan Greig](/author/jonathan-greig)

is a Breaking News Reporter at Recorded Future News. Jonathan has worked across the globe as a journalist since 2014. Before moving back to New York City, he worked for news outlets in South Africa, Jordan and Cambodia. He previously covered cybersecurity at ZDNet and TechRepublic.

## Briefs

* [23andMe successor settles with California for $6 million over cybersecurity failings October 20th, 2026](/23andme-california-data-breach-settlement)
* [Ahold Delhaize confirms 'malicious actions' behind cyber outages affecting grocery brandsOctober 19th, 2026](/ahold-delhaize-cyberattack-grocery)
* [Hackers steal customer data from major Russian hosting provider FirstVDSOctober 19th, 2026](/russia-cyberattack-firstvds-cloud)
* [Proofpoint lines up $6.3 billion deal for Varonis’ data securityOctober 16th, 2026](/proofpoint-varonis-cybersecurity-acquisition)
* [North Macedonian police arrest alleged administrator behind OLVX cybercrime marketOctober 14th, 2026](/olvx-cybercrime-marketplace-arrest-north-macedonia)
* [Russian travel booking platform suspends reservations after cyberattackOctober 14th, 2026](/russia-anywayanyday-travel-website-cyberattack)
* [Ledger says hardware implant in cryptocurrency wallets stole recovery phrasesOctober 13th, 2026](/ledger-cryptocurrency-wallet-implant-theft)
* [South African clothing retailer Foschini Group investigating cyberattack on British fashion brandsOctober 13th, 2026](/foschini-group-south-africa-c...