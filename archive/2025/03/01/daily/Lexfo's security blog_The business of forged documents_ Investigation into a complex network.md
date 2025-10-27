---
title: The business of forged documents: Investigation into a complex network
url: https://blog.lexfo.fr/the-business-of-forged-documents-investigation.html
source: Lexfo's security blog
date: 2025-03-01
fetch_date: 2025-10-06T21:59:29.121376
---

# The business of forged documents: Investigation into a complex network

[BLOG POSTS](/index.html) [CATEGORIES](/categories.html) [ARCHIVES](/archives.html)

[CONTACT US](https://lexfo.fr/contact/)

The business of forged documents: Investigation into a complex network

Fri 28 February 2025 by **Doriane P. & Albert E.** in [CTI](category/cti.html)

# Introduction

In today's digital age, document fraud poses a considerable challenge, affecting both those who commit the fraud and the victims who suffer from it.

False documents can be used for a wide variety of illegal activities, such as providing proof of residence using false water and electricity bills, landing a new job using fake diplomas, opening bank accounts using fraudulent identification papers, and so on.

Contrary to popular belief, obtaining such documents doesn't require advanced artificial intelligence or a journey into the dark web. Many counterfeiting organizations provide their services on both the clear and deep web, often under our very eyes, making access to these falsified documents relatively easy. This article focuses on these two strata of the web.

Our research indicates that, much like threat actors, counterfeiters' infrastructures can be analyzed using various OSINT methodologies. We discovered that several websites and e-mail accounts often seemed to be linked to the same counterfeiter, allowing us to trace their identity.

This article explores the different facets of document fraud, how it operates and highlights the fact that the number of players behind these numerous online stores is relatively small.

# The world of forgers

## Context and reasons for using fakes

Obtaining a forged document has become easy and relatively accessible to many. Using artificial intelligence or tools such as Photoshop, documents can be generated or altered to yield realistic results, mimicking handwriting fonts, official stamps and signatures. For counterfeiters, the primary motivation is easy money. The production and sale of forged documents requires minimal initial investment, especially for exclusively digital versions, and can generate substantial revenues.

Buyers of forged documents have a variety of motivations, including engaging in illegal activities such as identity theft, industrial espionage or even terrorism, as well as using them in everyday life.

Falsified documents can also be used for clandestine operations carried out by state actors or private organizations. As demonstrated by the [case of the North Korean âFake IT workersâ](https://www.reuters.com/technology/north-koreans-use-fake-names-scripts-land-remote-it-work-cash-2023-11-21/), malicious actors can make effective use of fraudulent documents. North Korean IT workers are using fake identities, fictitious LinkedIn profiles, forged documents and interview scripts to secure jobs at Western technology companies. These sophisticated strategies are designed to generate money to finance Pyongyang's nuclear program and carry out industrial espionage.

On a smaller scale, the purchase of false identity documents can be used to bypass KYC (Know Your Customer) identity verification procedures and facilitate banking or financial fraud.

The use of these forgeries is not always confined to criminal activities: some individuals use them to gain otherwise unattainable advantages, such as presenting a false diploma to secure a job. According to a [2024 survey by the French National Commission for Professional Certification (CNCP)](https://www.senat.fr/questions/base/2024/qSEQ241001592.html), some 20,000 fraudulent diplomas are produced in France every year.

"Ready-to-use kit" are sometimes available for sale, enabling prospective tenants to put together an appealing dossier without having the necessary resources. In this example, a "ready-to-use kit" of false documents to obtain a rental apartment:

![](../images/the-business-of-forged-documents-investigation/vente_kit_logement.png)

Example of an announcement for the sale of "ready-to-use kit" of false documents to obtain a rental apartment

The use or fabrication of false documents carries severe legal penalties. In France, these offences are severely punished, with penalties that can increase depending on the circumstances:

Penalties for the user:

* Use of false documents: Up to three years' imprisonment and a â¬45,000 fine.
* Possession of false government documents: Up to two years' imprisonment and a â¬30,000 fine, and up to five years' imprisonment and a â¬75,000 fine if several false documents are held.
* Use of false government documents to obtain a right or identity: up to five years' imprisonment and a â¬75,000 fine.
* Forgery of a public or authentic document: up to ten years' imprisonment and a â¬150,000 fine.

Penalties for counterfeiters:

* Forgery of a document normally issued by a public authority: up to five years' imprisonment and a â¬75,000 fine.
* Forgery of a public or authentic document: up to ten years' imprisonment and a â¬150,000 fine, or up to fifteen years' imprisonment and a â¬225,000 fine if the person is a public official.
* Falsification or fraudulent alteration of private documents (invoices, contracts): Up to three years' imprisonment and a â¬45,000 fine.

It is important to point out that attempts to commit these offences are subject to the same penalties.

## Not-so-hidden platforms

Unexpectedly, the places where fraudulent documents are sold are not confined to obscure sites hosted on the dark web that only accept payments in Monero. On the contrary, the counterfeiters' ecosystem is vast and varied. We've explored the various strata of the web, to get an idea of how the sellers operate.

### Dark Web

Sellers can be found on the dark web, where specialized marketplaces offer forged documents in exchange for cryptocurrencies. The descriptions are often sketchy, and the range of documents is limited.

![](../images/the-business-of-forged-documents-investigation/dw_1.png)![](../images/the-business-of-forged-documents-investigation/dw_2.png)![](../images/the-business-of-forged-documents-investigation/dw_3.png)

These items are handled like any other illegal items on these marketplaces. Since they have been the subject of many other articles, we wonât focus on them here.

### Deep Web

A variety of specialized sellers can be found on less visible parts of the deep web, through messaging platforms or social networks.

A quick search using a few keywords on Snapchat reveals numerous accounts whose explicit names leave no doubt:

![](../images/the-business-of-forged-documents-investigation/snapchat.png)

The same applies to other social networks like Facebook, Telegram, Snapchat, and WeChat, where dozens of sellers can be found using very simple keywords:

![](../images/the-business-of-forged-documents-investigation/facebook.png)![](../images/the-business-of-forged-documents-investigation/telegram.png)

While some may be scams, others boast many satisfied customers and successfully deliver their products.

### Clear Web

Our research has shown that many fraudulent documents are available for sale on websites present on the clear web, the visible part of the Internet, accessible with a basic Google search. The sites resemble typical e-commerce platforms: they are well-detailed, include photos, enable interaction with sellers for inquiries or more personalized products, and accept various payment methods.

![](../images/the-business-of-forged-documents-investigation/google_search.jpg)

![](../images/the-business-of-forged-documents-investigation/fakeid.png)

#### Payment methods

When it comes to payment methods, here too the choices may seem surprising from a security and anonymity point of view.

![](../images/the-business-of-forged-documents-investigation/payment.png)

1. The first category of payment methods includes traditional options like Western Union, bank transfers, Alipay and WeChat. The main drawback of these methods is that they involve intermediaries that are subject to strict regulation...