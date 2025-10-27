---
title: Stop Fraudsters at the Front Door with Device and Behavioural Intelligence
url: https://www.threatfabric.com/blogs/stop-fraudsters-at-the-front-door-with-device-behavioural-intelligence
source: Over Security - Cybersecurity news aggregator
date: 2025-09-24
fetch_date: 2025-10-02T20:35:37.248657
---

# Stop Fraudsters at the Front Door with Device and Behavioural Intelligence

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

## Stop Fraudsters at the Front Door with Device and Behavioural Intelligence

23 September 2025

![](https://www.threatfabric.com/hubfs/TF_Blog_FrontDoor.jpg)

### Jump to

As digital fraud surges worldwide, criminals continue to need homes for stolen funds. Traditional identity-based controls during user onboarding are not bullet-proof. By layering in device and behavioural intelligence at the start of the application journey, AML and Fraud teams can gain early visibility of potentially fraudulent applications, avoiding costly eID&V checks and protecting the financial institution from downstream risk.

## You wouldn’t give a stranger the key to your house…

Application fraud has become one of the fastest-growing threats in digital banking. Fraudsters exploit remote banking channels to create new accounts using stolen or fabricated identities, often as a precursor to money laundering, mule activity, and large-scale financial crime.

Three of the most prevalent types are:

* **Stolen identity applications**, where criminals use real consumer details purchased from dark web marketplaces or stolen in data breaches to open accounts.

* **Synthetic identity applications**, where fraudsters blend genuine and fictitious personal information (e.g., real SSN + fake name) to build “credit-worthy” profiles undetected.

* **First-party fraud**, where fraudsters socially engineer victims to open mule accounts with their genuine details.

 The scale is staggering. According to the 2024 LexisNexis True Cost of Fraud study, identity fraud losses in the U.S. alone surpassed $43 billion last year, with synthetic identity fraud accounting for nearly 20% of all credit charge-offs. In the UK, according to CIFAS Fraudscape 2025, identity fraud is now 60% of all fraud filed to the National Fraud Database.

This isn’t just about financial losses. Every fraudulent account opened erodes brand trust, increases compliance risk, and strains the efficiency of KYC and AML programmes.

## Not all bots are built equal

One of the key reasons application fraud is accelerating is the industrialisation of attacks. Fraudsters no longer need to complete forms manually. Instead, they deploy bot frameworks and automated scripts to flood application portals at scale.

What’s concerning is that bots are not just used in fraudulent sessions. Many banks and FinTechs also see bots in legitimate customer journeys — for example, price comparison tools, automated account aggregators, or customer device security apps. Distinguishing between “good bot” and “bad bot” traffic is increasingly difficult, leaving legacy fraud controls under strain.

The result? Traditional application fraud controls, focused on identity attributes and credit bureau checks, are being overwhelmed. Fraudsters can inject thousands of fraudulent applications into the funnel, waiting for the few that slip past filters.

## Devices and behaviours betray intent

To fight back, banks are increasingly turning to device intelligence and behavioural analytics to spot fraudsters at the digital front door, before costly eID&V checks and onboarding begin.

### Device Intelligence

 Fraudster devices often “look” different to those of genuine customers. Technical anomalies include:

* **Presence of emulation software** simulating a mobile device on a desktop.
* **Camera injection apps** used to bypass KYC controls.
* **Remote access tools (RATs)** enabling multiple operators to use the same device.
* **Multiple fresh installs**, rooted devices, or exotic configurations rarely seen in legitimate customers.

### Behavioural Analytics

Even when fraudsters try to mimic normal user devices, their digital behaviour often betrays them:

* **High application familiarity** - fraudsters race through forms quicker than genuine users.
* **Low input familiarity** - data fields like name, address, or DOB are typed slowly or segmented, unlike a real user who has muscle memory for their own details.
* **Excessive copy-paste usage** - often from stolen identity files into application fields.
* **Frequent tab switching** - to reference stolen data.
* **Inconsistent typing cadence** - with bursts of fast input and sudden pauses.

When combined, these signals provide a powerful “behavioural fingerprint” to separate genuine applicants from fraudulent ones, without relying solely on identity data.

At ThreatFabric, we have started to use advanced **Deep Learning models** for behavioural modelling, which significantly outperform the tree-based models used by the rest of the market. Deep Learning has several advantages:

* **Feature extraction**: Unlike traditional feature engineering, deep networks automatically learn hierarchical representations of user behaviour.
* **Temporal modelling**: Neural networks and attention-based models effectively capture long-term dependencies in user sessions.
* **Greater generalization**: Training on massive datasets (~100M+ sessions) enables the model to identify subtle behavioral patterns that are difficult to extract with manual feature engineering.

This results in greater model accuracy and precision, leading to fewer false declines and fewer fraudsters slipping through the net.

A necessary (and beautiful) property of these models is that they require no understanding of expected behaviour at a user-level. They are instead trained on an application-level, based on previously seen genuine and fraudulent applications.

## Balancing user privacy with fraud detection

A common misconception is that the above techniques require deep inspection of personal data. In reality, Personally Identifiable Information (PII) is not necessary for effective device and behavioural risk detection.

The system does not need to know that the applicant’s name is “Jamie Smith”. Instead, it only needs to understand that the name was entered in an unusual way — e.g. the typing cadence was unusual, or the name was copied and pasted.

Device risk detections can be deployed in a privacy-preserving architecture using heuristic Edge AI. Applications running on a user’s device are only flagged to the backend if they match against a database of known risky apps (such as emulators or RATs). In this way, solutions are not intrusively collecting data on user’s installed applications.

As a European company with GDPR-regulated financial institutions using our technology, ThreatFabric has built our solutions with compliance and privacy embedded in every design decision. We are one of the few solutions in the market which do not require any user PII.

## The business case: Reduce costly eID&V checks, onboard good users quicker and stop fraudsters at the front door

The business case for deploying device and behavioural intelligence is compelling:

* **Cost efficiency:** Every fraudulent applicant stopped at the top of t...