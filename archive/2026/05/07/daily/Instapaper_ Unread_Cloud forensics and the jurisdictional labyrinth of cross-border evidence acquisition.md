---
title: Cloud forensics and the jurisdictional labyrinth of cross-border evidence acquisition
url: https://andreafortuna.org/2026/05/06/cloud-forensics-jurisdictional-labyrinth/
source: Instapaper: Unread
date: 2026-05-07
fetch_date: 2026-05-08T04:57:00.186898
---

# Cloud forensics and the jurisdictional labyrinth of cross-border evidence acquisition

[Andrea Fortuna](/)
[ ]

[About](/about/)

Tools

[DFIR Toolkit](https://dfir-toolkit.andreafortuna.org)
[OSINT Toolkit](https://osint-toolkit.andreafortuna.org)

# Cloud forensics and the jurisdictional labyrinth of cross-border evidence acquisition

May 6, 2026

by [Andrea Fortuna](/about/)

An Italian public prosecutor opens an investigation into a ransomware attack targeting local healthcare infrastructure. Technical analysis identifies clear attack vectors and digital footprints linked to specific infrastructure. As the investigation progresses, jurisdictional complexity becomes apparent: server logs are stored in a Dublin data center, user metadata resides on U.S.-based servers, and stolen credentials are traded on an underground forum hosted in the Seychelles. A technically routine investigation now spans multiple jurisdictions, each governed by distinct legal frameworks, procedural rules, and sovereignty requirements.

![cover](/assets/2026/cloud-forensics-jurisdictional-labyrinth.jpg)

This scenario reflects the core challenge of modern cloud forensics. Evidence no longer resides in a single physical location with a clear jurisdictional anchor. Instead, it is distributed across global infrastructure where traditional forensic methods confront the realities of international law.

## When the crime scene has no address

Cloud forensics has emerged as a distinct discipline precisely because the traditional approaches to digital investigation break down when applied to cloud environments. The [NIST Cloud Computing Forensic Reference Architecture](https://www.nist.gov/news-events/news/2024/07/nist-cloud-computing-forensic-reference-architecture-sp-800-201), published in July 2024 as Special Publication 800-201, identifies three structural reasons why cloud forensics cannot simply be treated as classical digital forensics deployed in a different environment.

The first reason is the inherent volatility of evidence in cloud systems. In traditional forensics, when an investigator seizes a physical server, the data remains intact until imaged. The acquisition window spans days or even weeks. In cloud environments, the window shrinks to hours. Virtual machines can be terminated, storage volumes deleted, and logs rotated with alarming speed. The default log retention period across many cloud providers is ninety days, after which evidence simply ceases to exist unless specifically preserved.

The second challenge is multitenancy, which renders traditional physical imaging impossible. When multiple customers share the same physical infrastructure, creating a bit-by-bit copy of a storage device would expose other tenants’ data, raising severe privacy and legal concerns. Investigators must rely on logical extractions through APIs, accepting a fundamentally different evidentiary foundation than what courts have traditionally expected from digital forensics.

The third structural difference is the divorce between investigative authority and data location. A prosecutor in Milan might have full authority to investigate crimes under Italian law, but that authority stops at the border. When the data lives in a data center in Dublin, the investigation becomes subject to Irish law, European regulations, and the policies of the cloud service provider. This separation creates what forensic practitioners describe as a jurisdictional labyrinth, where the path to evidence is blocked by legal walls that no technical skill can breach.

These challenges mirror many of the issues faced in [mobile forensics](https://andreafortuna.org/2024/06/12/mobile-forensics-tools-and-techniques/), where investigators must contend with encrypted storage, logical acquisition methods, and evidence that exists partially on the device and partially in cloud-linked accounts. The mobile forensics community has developed workflows for these constraints, but cloud forensics introduces an additional layer of complexity through the involvement of multiple legal jurisdictions that simply do not exist in the mobile context.

## The CLOUD Act and how jurisdiction follows the provider

The legislative landscape shifted dramatically in 2018 when President Trump signed the Clarifying Lawful Overseas Use of Data Act, known as the CLOUD Act, as part of the Consolidated Appropriations Act. The law emerged from a pivotal case, [*United States v. Microsoft Corporation*](https://en.wikipedia.org/wiki/United_States_v._Microsoft_Corporation) (2013–2018), where a New York court ordered Microsoft to produce emails stored in a Dublin data center. Microsoft challenged the warrant, arguing that U.S. law enforcement authority did not extend to data stored on foreign soil. The case reached the Supreme Court, which vacated it in April 2018 after the CLOUD Act rendered the original warrant moot.

The U.S. legislature resolved the conflict with a clear, unambiguous choice. Under the CLOUD Act, jurisdiction follows the provider, not the data. If a U.S.-based service provider holds the data, American authorities can demand it regardless of where the physical servers sit. This represents a fundamental assertion of extraterritorial jurisdiction that has rippled through the global legal community.

The tension becomes immediately apparent when this American law collides with European privacy regulations. Article 48 of the GDPR establishes that any transfer of data to a third country authority requires an international agreement in force, typically a mutual legal assistance treaty (MLAT). A simple foreign warrant or subpoena does not suffice under European law. The data controller must have both a legal basis for processing and an appropriate transfer mechanism, as the [EDPB and EDPS spelled out in their 2019 joint response on the CLOUD Act](https://edps.europa.eu/sites/edp/files/publication/19-07-10_edpb_edps_cloudact_annex_en.pdf), which concluded that compliance with a unilateral foreign order does not constitute a valid transfer mechanism under European law.

The CLOUD Act does provide a pathway through executive agreements that streamline cross-border data requests between trusted partners. As of April 2026, only two such executive agreements are operational: one with the United Kingdom signed in October 2019 and entered into force in October 2022, and another with Australia finalized in January 2024. Negotiations with the European Union have been ongoing, but no agreement has been reached. This creates what many legal scholars describe as an impossible compliance position for cloud service providers.

I explored this conflict in detail in my analysis of the [AWS European Sovereign Cloud](https://andreafortuna.org/2026/01/26/AWS-european-sovereign/), where the technical infrastructure promises European sovereignty while the legal reality remains tethered to U.S. jurisdiction. A provider operating under U.S. law cannot simply ignore a lawful CLOUD Act order without facing contempt charges and substantial penalties, yet complying with such an order for data stored in Europe potentially violates GDPR Article 48. The customer who paid for sovereign cloud services finds their data accessed by a foreign government, precisely the scenario that European data protection law was designed to prevent.

## Budapest and Brussels building the multilateral response

Recognizing that unilateral assertions of jurisdiction were creating more conflict than cooperation, international bodies began developing multilateral frameworks to address cross-border evidence acquisition. Two parallel instruments have emerged, each taking a different approach to the same fundamental problem.

The Second Additional Protocol to the Budapest Convention on Cybercrime (CETS 224) was adopted on November 17, 2021, and opened for signature in Strasbourg in May 2022. This instrument introduces four key mechanisms that represent a significant evolution in international cybercrime cooperation. First, it enables direct cooperation with service providers without rou...