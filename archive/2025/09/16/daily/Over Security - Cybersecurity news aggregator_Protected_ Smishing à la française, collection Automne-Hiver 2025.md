---
title: Protected: Smishing à la française, collection Automne-Hiver 2025
url: https://stalkphish.com/2025/09/15/smishing-a-la-francaise-collection-automne-hiver-2025/
source: Over Security - Cybersecurity news aggregator
date: 2025-09-16
fetch_date: 2025-10-02T20:11:57.129401
---

# Protected: Smishing à la française, collection Automne-Hiver 2025

[![StalkPhish – phishing, scam and brand impersonation detection](https://stalkphish.com/wp-content/uploads/2021/03/stalkphish-incl-200x60-txt-white.png)](https://stalkphish.com/)

[StalkPhish – phishing, scam and brand impersonation detection](https://stalkphish.com/)

StalkPhish – We provide B2B tools, data and knowledge for a better phishing and brand impersonation detection.

* [Home](https://stalkphish.com/)
* [Products](https://stalkphish.com/portfolio/products/)
* [Projects](https://stalkphish.com/products/)
  + [PhishingKit-Yara-Rules](https://stalkphish.com/products/phishingkit-yara-rules/)
  + [PhishingKitHunter](https://stalkphish.com/products/phishingkithunter/)
  + [StalkPhish OSS](https://stalkphish.com/products/stalkphish/)
* [Blog](https://stalkphish.com/blog-feed/)
* [Contact](https://stalkphish.com/contact/)
* [About](https://stalkphish.com/about-2/)
* [Press & Media](https://stalkphish.com/press-media/)

* [Twitter](https://twitter.com/Stalkphish_io)
* [LinkedIn](https://www.linkedin.com/company/stalkphish)
* [GitHub](https://github.com/t4d/StalkPhish)
* [Youtube](https://www.youtube.com/channel/UC5hb1CaRdmbSWpN0wTz6SFw)

Show search form
Menu- Select Page -HomeProductsProjects - PhishingKit-Yara-Rules - PhishingKitHunter - StalkPhish OSSBlogContactAboutPress & Media

Search for:

 Hide search form

![StalkPhish - Smishing a la francaise - collection automne-hiver 2025](https://stalkphish.com/wp-content/uploads/2025/09/phishing-francaise-collection-automne-hiver-2025.png?w=1024)

# Smishing à la française, collection Automne-Hiver 2025-2026

Nouvelles techniques de smishing utilisées par les scammers francophones depuis début 2025 pour escroquer leurs victimes.

![StalkPhish's avatar](https://2.gravatar.com/avatar/2ecf84df3d23b66e9e3dc59759be2600c71c9cd576b072248f211024b06278a3?s=35&d=identicon&r=G) By [StalkPhish](https://stalkphish.com/author/stalkphish/)

in [CERT](https://stalkphish.com/category/cert/), [CSIRT](https://stalkphish.com/category/csirt/), [cti](https://stalkphish.com/category/cti/), [Etude](https://stalkphish.com/category/etude/), [investigation](https://stalkphish.com/category/investigation/), [smishing](https://stalkphish.com/category/smishing/), [StalkPhish.io](https://stalkphish.com/category/tool/stalkphish-io/), [threat intelligence](https://stalkphish.com/category/threat-intelligence/)

on [09/15/202509/17/2025](https://stalkphish.com/2025/09/15/smishing-a-la-francaise-collection-automne-hiver-2025-2026/)

[No comments](https://stalkphish.com/2025/09/15/smishing-a-la-francaise-collection-automne-hiver-2025-2026/#respond)

Depuis plusieurs années StalkPhish se renseigne sur l’évolution des réseaux criminels spécialisés dans l’escroquerie, particulièrement les arnaques dites ” au allo” ou “faux conseiller bancaire”, un fléau sur lequel [nous alertons régulièrement](https://stalkphish.com/press-media/).

Depuis le printemps 2025, **nous observons de nouvelles stratégies de communication** utilisées par les *scammers* (les arnaqueurs) pour contourner les systèmes de protection. Ces techniques visent un double objectif : **échapper aux dispositifs de détection** automatisés déployés par les opérateurs téléphoniques, tout en **rendant plus plausibles, plus légitimes, les messages d’arnaque** envoyés aux victimes potentielles.

Nous partageons ici nos analyses pour permettre à chacun.e de mieux reconnaître et déjouer les pièges tendus par ces escrocs.

# Des bases qui perdurent

Depuis des années maintenant les arnaqueurs français/francophones pratiquent l’envoi de liens de phishing, par le biais d’emails, de messageries instantanées ou de SMS comme cette arnaque à la livraison:

![Arnaque livraison](https://stalkphish.com/wp-content/uploads/2025/09/image-3.png?w=1024)

Ce genre de campagne est très courante, cependant elles ont leur limite, notamment la **détection que peuvent pratiquer les opérateurs** que ce soit sur les URLs ou noms de domaine connus comme étant utilisés pour pratiquer des campagnes de phishing, voire sur certains mots ou noms de marques pouvant être utilisés dans des SMS ou emails, les escrocs ont d’ailleurs détecté cette pratique de filtrage:

![Filtrage arnaques](https://stalkphish.com/wp-content/uploads/2025/09/image-4.png?w=755)

---

# Bonjour vous etes chez vous ?

Qui n’a pas reçu ce désormais fameux SMS: “Bonjour vous etes chez vous ?”. Apparues cette année, massivement, **ces campagnes d’arnaque diffèrent des campagnes autrefois habituelles** en appellant une réponse à un premier contact, sans malveillance particulière de prime abord.

Cette campagne consiste à faire répondre la potentielle victime avant d’envoyer un message supplémentaire. Ce second message indique qu’il s’agirait d’un livreur souhaitant livrer un colis “*qui ne rentrait pas dans la boite aux lettres*“… un classique:

![Bonjour vous etes chez vous ?](https://stalkphish.com/wp-content/uploads/2025/09/image.png?w=1024)

C’est dès le troisième échange qu’un lien menant vers un site de phishing – usurpant l’identité de la société Mondial Relay, le plus souvent – est alors envoyé:

![URL SMS phishing](https://stalkphish.com/wp-content/uploads/2025/09/image-1.png?w=1024)

Ce site de phishing est **“protégé” par un *captcha*** afin d’empêcher la récupération d’informations par certains systèmes de détection:

![captcha phishing](https://stalkphish.com/wp-content/uploads/2025/09/image-2.png?w=1024)

Cet enchaînement de “techniques” permet plusieurs choses:

1. De ne pas envoyer directement un lien pouvant être détecté par les opérateurs téléphoniques
2. De lancer un échange avec une potentielle victime qui “accroche” à la tentative d’arnaque
3. De “légitimer” un échange de SMS potentiellement anodin auprès des opérateurs

Cependant, l’envoi massif de SMS avec une même ligne est plus rapidement détectable par l’opérateur émettant ces messages.

Alors que fin 2022 les scammers pouvaient envoyer plusieurs dizaines de milliers de SMS avant détection, avec un taux de récolte de numéros de carte de crédit équivalent à 1% voire 1,5% (voir [notre article de l’époque](https://stalkphish.com/2022/12/19/une-campagne-de-phishing-netflix-societe-generale-ameli-ou-critair-pour-10-euros/)), aujourd’hui si une SIM/eSIM parvient à envoyer **7 à 8000 SMS avant d’être désactivée**, c’est bien le maximum. Les taux de “*rez*” d’informations (les informations volés et exploitables) ont eux aussi **chuté sous le 1%.** La sensibilisation de la population y est aussi sûrement pour quelque chose.

---

# L’appel entrant

Afin d’éviter la détection, **les escrocs tentent de s’adapter**. Pour contrecarrer la détection d’URL les scammers ont mis au point une nouvelle technique appelée “l’appel entrant”.

Cette technique consiste à ne plus envoyer d’URL de phishing, mais un message alarmant de paiement en cours, comme dans cet exemple:

![Appel entrant](https://stalkphish.com/wp-content/uploads/2025/09/image-5.png?w=1024)

Ici plus aucune URL de phishing n’est envoyée, d’ailleurs le déploiement d’un site de phishing n’est même plus nécessaire! **Le scammer demande à être rappelé directement par la victime**.

> le déploiement d’un site de phishing n’est même plus nécessaire!

De fait l’escroc sait qu’il a affaire à une victime déjà conditionnée et peut procéder à la suite de l’arnaque en se faisant passer pour le service anti-fraude de la banque en question: **récupération des informations personnelles, accès au compte bancaire, validation des demandes de virement ou de paiement, etc…**

C’est d’ailleurs un argument régulièrement mis en avant sur les réseaux de ventes de services pour arnaqueurs:

![Offre appel entrant](https://stalkphish.com/wp-content/uploads/2025/09/image-6.png?w=423)

---

# Centres d’appels

A l’image d’arnaques déjà très développées, comme les arnaques au **faux support technique** par exemple, et afin de mener leurs campagnes “d’appels entrants”, les scammers montent de véritables **centres d’appels** à l’aide de services légaux ...