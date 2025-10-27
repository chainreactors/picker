---
title: The Big TIBER Encyclopedia
url: https://blog.nviso.eu/2024/08/29/the-big-tiber-encyclopedia/
source: NVISO Labs
date: 2024-08-30
fetch_date: 2025-10-06T18:03:34.883263
---

# The Big TIBER Encyclopedia

[Skip to content](#content)

[![NVISO Labs](https://blog.nviso.eu/wp-content/uploads/2022/12/cropped-abn-zcrj_400x400-1.png)](https://blog.nviso.eu/)

[NVISO Labs](https://blog.nviso.eu/)

Cyber security research, straight from the lab! 🐀

* [twitter](https://twitter.com/NVISO_Labs)
* [linkedin](https://www.linkedin.com/company/nviso-cyber)
* mail us
* [our company](https://www.nviso.eu)
* [SSO](https://blog.nviso.eu/wp-admin/edit.php)

Menu

* [All](https://blog.nviso.eu/)
* [Blue Team](https://blog.nviso.eu/category/blue-team/)
* [Cloud Security](https://blog.nviso.eu/category/cloud-security/)
  + [AWS](https://blog.nviso.eu/category/cloud-security/aws/)
  + [Azure](https://blog.nviso.eu/category/cloud-security/azure/)
  + [GCP](https://blog.nviso.eu/category/cloud-security/gcp/)
  + [Microsoft 365](https://blog.nviso.eu/category/cloud-security/microsoft-365/)
* [Awareness](https://blog.nviso.eu/category/awareness/)
* [Forensics](https://blog.nviso.eu/category/forensics/)
* Other
  + [Application Security](https://blog.nviso.eu/category/application-security/)
  + [IoT Security](https://blog.nviso.eu/category/iot-security/)
  + [Web Security](https://blog.nviso.eu/category/web-security/)
  + [Industrial Security](https://blog.nviso.eu/category/industrial-security/)
  + [Mobile Security](https://blog.nviso.eu/category/mobile-security/)
  + [Cyber Strategy](https://blog.nviso.eu/category/cyber-strategy/)
  + [Purple Team](https://blog.nviso.eu/category/purple-team/)
  + [Red Team](https://blog.nviso.eu/category/red-team/)
  + [Events](https://blog.nviso.eu/category/events/)

# The Big TIBER Encyclopedia

[Jonas Bauters](https://blog.nviso.eu/author/jonas-bauters/ "Posts by Jonas Bauters")

[Adversary Emulation](https://blog.nviso.eu/category/red-team/adversary-emulation/), [Red Team](https://blog.nviso.eu/category/red-team/), [Purple Teaming](https://blog.nviso.eu/category/purple-teaming/), [Adversary Simulation](https://blog.nviso.eu/category/red-team/adversary-simulation/), [Purple Team](https://blog.nviso.eu/category/purple-team/)

August 29, 2024August 27, 2024
14 Minutes

## An analysis of current TIBER implementations ahead of DORA’s TLPT requirements

# Introduction

TIBER (Threat Intelligence-Based Ethical Red Teaming) is a framework introduced by the European Central Bank (ECB) in 2018 as a response to the increasing number of cyber threats faced by financial institutions. The framework provides a standardized methodology and guidelines for conducting controlled and targeted realistic cyberattack simulations. The key objective of TIBER is to assess and improve the resilience of financial institutions against cyber threats by adopting a proactive approach.

The results of the exercises provide valuable insights into areas that need improvement, enabling organizations to enhance their cyber defenses and better protect themselves against real-world cyber threats.

The European framework is known as TIBER-EU, which can be voluntarily adopted by individual countries, driven by the national competent authority (NCA) for the financial sector of that member state, which is in many cases also the central bank. In the meantime, 16 countries (as well as the ECB, adding up to 17 implementations) have adopted the framework and apply it:

![](https://blog.nviso.eu/wp-content/uploads/2024/08/image-1-913x1024.png)

16 countries having adopted TIBER

As of January 17th, 2025, the DORA regulation will apply for relevant financial entities and ICT third-party service providers. Threat-led Penetration Testing (TLPT) as required by the DORA regulation will be specified in accordance with TIBER-EU and in agreement with the ECB.

The purpose of this blog post is therefore threefold. Firstly, we want to provide an overview of the current country-specific implementations of the TIBER-EU framework and where these implementations may differ (even if only slightly). Secondly, we want to add some lessons learned and personal insights gained from the execution of multiple TIBER engagements over the past few years for different TIBER jurisdictions. These are added in the blue-lined quote boxes. Thirdly, we want to show why TIBER still makes sense ahead of DORA TLPT and will continue to make sense once the regulation is applied.

# Country-specific Guidance

To get started, which countries have their own implementation of the TIBER-EU framework and how is their implementation guidance provided? Note that we also add the TIBER-EU framework documentation as a reference, which should not be considered an implementation document.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Jurisdiction** | **Guidance** **Format** | **Language** | **Latest Version** | **Introduction Date** | **Reference** |
| Europe 🇪🇺 | PDF | EN | May 2018 | May 2018 | [TIBER-EU](https://www.ecb.europa.eu/paym/cyber-resilience/tiber-eu/html/index.en.html) |
| Austria 🇦🇹 | PDF | EN | November 2023 | November 2023 | [TIBER-AT](https://www.oenb.at/en/financial-market/tiber-at.html) |
| Belgium 🇧🇪 | PDF | EN | December 2022 | June 2020 | [TIBER-BE](https://www.nbb.be/en/payments-and-securities/tiber-be-framework) |
| Denmark 🇩🇰 | PDF | EN | December 2021 | December 2018 | [TIBER-DK](https://www.nationalbanken.dk/en/what-we-do/stable-financial-system/cyber-resilience) |
| Finland 🇫🇮 | Web Page | EN | Updated annually | April 2020 | [TIBER-FI](https://www.suomenpankki.fi/en/money-and-payments/tiber-fi-implementation-guideline/) |
| France 🇫🇷 | PDF | EN | January 2024 | January 2024 | [TIBER-FR](https://www.banque-france.fr/en/financial-stability/institutional-framework/payment-systems-market-infrastructures/oversight-cyber-risk) |
| Germany 🇩🇪 | PDF | EN | December 2022 | Summer 2019 | [TIBER-DE](https://www.bundesbank.de/en/tasks/payment-systems/tiber-de/tiber-de-817014) |
| Iceland 🇮🇸 | PDF | EN | June 2023 | February 2023 | [TIBER-IS](https://www.cb.is/financial-stability/oversight-of-financial-market-infrastructures/cyber-resilience-testing/) |
| Ireland 🇮🇪 | PDF | EN | December 2019 | December 2019 | [TIBER-IE](https://www.centralbank.ie/financial-system/operational-resilience-and-cyber/cyber-resilience/tiber-ie) |
| Italy 🇮🇹 | PDF | EN | August 2022 | Early 2020 | [TIBER-IT](https://www.bancaditalia.it/compiti/sispaga-mercati/tiber-it/index.html?com.dotmarketing.htmlpage.language=1&dotcache=refresh) |
| Luxembourg 🇱🇺 | PDF | EN | Not specified | November 2021 | [TIBER-LU](https://www.bcl.lu/fr/systeme_paiement/TIBER-LU/index.html) |
| Netherlands 🇳🇱 | PDF | EN | December 2022 | 2016 | [TIBER-NL](https://www.dnb.nl/en/sector-information/cash-and-payment-systems/tiber-nl/) |
| Norway 🇳🇴 | PDF | EN | October 2022 | May 2021 | [TIBER-NO](https://www.norges-bank.no/en/topics/financial-stability/Prevention/tiber/) |
| Portugal 🇵🇹 | PDF | EN | February 2024 | April 2022 | [TIBER-PT](https://www.bportugal.pt/page/forum-com-industria-para-ciberseguranca-e-resiliencia-operacional?mlid=4582) |
| Romania 🇷🇴 | Web Page PDF | RO EN | May 2022 | May 2022 | [TIBER-RO](https://www.bnr.ro/page.aspx?prid=20937) |
| Spain 🇪🇸 | PDF | EN | January 2022 | December 2020 | [TIBER-ES](https://www.bde.es/bde/en/secciones/servicios/tiber-es-3f6bfe7e907ed71.html) |
| Sweden 🇸🇪 | PDF | EN | Not specified | December 2019 | [TIBER-SE](https://www.riksbank.se/en-gb/financial-stability/the-riksbanks-responsibility-with-regard-to-financial-stability/preventing-financial-crises/the-riksbanks-work-on-cyber-risks/tiber-se/) |

Availability of TIBER guidance

Note that we refer to the country-specific TIBER websites and not directly to the implementation PDFs to avoid dead links as much as possible. However, if you would notice one of the links no longer working, don’t hesitate to reach out so we can update it.

Most countries follow the same approach, i.e. an English guidance PDF. However, there are some exceptions:

* TIBER-FI uses a web page in English
* TIBER-RO uses a web page in Romanian (although a PDF extract is also ava...