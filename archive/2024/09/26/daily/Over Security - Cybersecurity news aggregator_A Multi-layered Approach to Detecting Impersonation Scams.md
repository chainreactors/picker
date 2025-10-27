---
title: A Multi-layered Approach to Detecting Impersonation Scams
url: https://www.threatfabric.com/blogs/a-multi-layered-approach-to-detecting-impersonation-scams
source: Over Security - Cybersecurity news aggregator
date: 2024-09-26
fetch_date: 2025-10-06T18:38:57.507747
---

# A Multi-layered Approach to Detecting Impersonation Scams

[Skip to content](#main-content)

[![threatfabric-logo-light](https://www.threatfabric.com/hubfs/Threatfabric/logos/threatfabric-logo-light.svg "threatfabric-logo-light")](//www.threatfabric.com/)

[![threatfabric-logo-light](https://www.threatfabric.com/hubfs/Threatfabric/logos/threatfabric-logo-light.svg "threatfabric-logo-light")](//www.threatfabric.com/)

* OUR SOLUTIONS
  + [Mobile Threat Intelligence (MTI)](https://www.threatfabric.com/mti)
  + [Fraud Risk Suite (FRS)](https://www.threatfabric.com/frs)
* [PARTNERS](https://www.threatfabric.com/partners)
* [WEBINARS](https://www.threatfabric.com/webinars)
* [ARTICLES](https://www.threatfabric.com/blogs)
* RESOURCES
  + [DATASHEETS & REPORTS](https://www.threatfabric.com/resources)
  + [IN THE NEWS](https://www.threatfabric.com/news)
* [Contact](https://www.threatfabric.com/contact)
* [Linkedin](https://www.linkedin.com/company/threatfabric)
* [Twitter](https://twitter.com/threatfabric)
* [Jobs](https://www.threatfabric.com/jobs)
* [Privacy](https://www.threatfabric.com/privacy)
* [Intel/PGP](https://www.threatfabric.com/contact)

[Contact](https://www.threatfabric.com/contact)

Blog

## A Multi-layered Approach to Detecting Impersonation Scams

25 September 2024

![](https://www.threatfabric.com/hubfs/20240924_Blog.jpg)

### Jump to

I am your bank.
I am your police.
I am your lover.

## The Nature and Scale of the Problem

 Scams are a natural evolution of the criminal Modus Operandi: as financial institutions deploy more protective technology, the criminals respond by going low-tech. Social Engineering replaces Exploit Kits.

Impersonation scams are no longer endemic to one region and cost society financially and psychologically while eroding trust in institutions.

In the UK, impersonation scams were the second most costly in 2023, costing UK consumers and businesses £72m in H1. In Norway, DNB reported earlier this year that safe account fraud, another term for an impersonation scam, was the fastest-growing fraud type in the region. In Australia, Aussies lost a staggering $92 million to impersonation scams last year, accounting for more than 70% of reports made to Scamwatch.

With PSD3 soon coming into effect, European financial institutions will be required to reimburse customers in cases where the bank has been spoofed. The article below considers a five-layered approach to turning the tide on impersonation scams.

These scams move geographically, like a bulge in a carpet. Stomp the bulge down, and it will pop up somewhere else, often in unexpected geographical locations.

## A Typical Impersonation Scam

Although no two fraud events are exactly alike, impersonation scams typically follow the following steps:

1. The fraudster contacts the victim over a voice call claiming to be their bank, law enforcement, a utility company, their CEO or any other trusted entity;
2. The fraudster creates a sense of urgency by convincing the victim that their funds are at risk;
3. The fraudster may direct the victim to download a legitimate remote access tool (RAT), such as AnyDesk to gain access to the victim’s device. The fraudster can now perform unauthorised financial transactions or steal identity information for fraudulent purposes;
4. If no RAT was installed, the fraudster would socially engineer the victim over the phone to make an authorised transaction to a mule account controlled by the fraudster.

## Multi-layered Defences Against Impersonation Scams

To pre-empt these low-tech scams, there are 5 layers of defence available:

![TF_DetectingImpersonationScams](https://www.threatfabric.com/hs-fs/hubfs/TF_DetectingImpersonationScams.jpg?width=2880&height=2880&name=TF_DetectingImpersonationScams.jpg)

### Layer 1: Call Intelligence

Identifying when a user is on a call while in a banking session is essential to detecting vishing (voice phishing). ThreatFabric and industry data show that users are only on live calls during 1% of genuine banking sessions. However, alerting on all these sessions would introduce unnecessary noise and therefore additional data is required to separate the signal from the noise.

Two additional signals deliver high predictive power when detecting vishing:

1. **Call duration:** Fraudsters require significant time (often several hours) to build trust and progress their fraud from initial contact to monetization. Excessive call length is a strong signal for vishing.
2. **Call type:** Scam call centres abuse Voice-over-Internet-Protocol (VOIP) technology to hide their true location and identity through a variety of spoofing methods. Detecting WhatsApp, Signal and Telegram calls versus less risky cellular network calls is another strong signal for vishing.

### Layer 2: Remote access & screen-sharing detection

Detecting the presence of a remote access tool (RAT) accurately requires a multi-layered approach. Many commercial RATs (e.g. AnyDesk and TeamViewer) open network ports and therefore can be detected using port scanning technology. However, several ThreatFabric customers report a wave of RAT fraud originating from RATs such as Microsoft Quick Assist which do not open network ports.

These RATs can be detected using sophisticated device indicators, which monitor for anomalies in screen size, resolution, and colour depth as well as behavioural indicators which monitor for frequent mouse overshoots, changes in hit zones and a variety of other behaviours that are specific to RATs.

A ThreatFabric customer recently reported that fraudsters were using developer tools to inject content onto banking websites and convince users that they were truly on the phone with the bank. ThreatFabric has developed a fragment scanning tool to detect modifications like this – an additional risk signal that bank impersonation is in flight.

### Layer 3: Behavioural biometrics

In the case that a RAT is not used in the fraud, there are very few technical indicators to help identify the fraud early in the kill chain. In this case, behavioural biometrics technology which analyses user keystrokes, navigation, mouse movement, touch and rotation behaviour is paramount to detecting coercion or hesitancy. Statistically significant deviations from historical behaviour are a powerful indicator of social engineering, especially when correlated with device risks such as a live, VOIP call and/or live RAT.

However, not all behavioural biometrics technology is built equal. Banks should take care in evaluating different providers by asking questions such as:

* Do behavioural models account for changing user behaviour over time? How?

* Over what period is user behaviour evaluated? Sessions, sub-sessions, key events?

* Are behavioural models off-the-shelf? Are they trained on a user level, application level or both?

Next-generation behavioural biometrics technology uses sophisticated feature engineering and deep learning techniques to minimise false positives, which cripple the return on investment of first-generation tools.

### Layer 4: Real-time payment blocking

The value of detecting early warning signals of impersonation fraud, through the layers above, is limited without a decisioning engine that can:

1. Correlate device, behavioural, customer and transactional risk signals: Overall session risk must be considered holistically by considering all the available data.  Transaction size, velocity, payee relation age and in/out ratios are examples of strong transactional indicators of impersonation fraud. These transaction monitoring signals are supercharged when correlated with device and behavioural intelligence, especially as part of a machine learning model. ThreatFabric customers have experienced Value Detection Rate improvements to as high as 90% when adding device and behavioural intelligence into traditional fraud payments monitoring.
2. Challenge or block transactions in real-time: Once the money has left a victim’s account, recovery of funds is incredibly difficult. Fraudsters launder their p...