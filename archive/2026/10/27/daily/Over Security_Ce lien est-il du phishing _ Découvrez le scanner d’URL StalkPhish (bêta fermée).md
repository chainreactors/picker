---
title: Ce lien est-il du phishing ? Découvrez le scanner d’URL StalkPhish (bêta fermée)
url: https://stalkphish.com/2026/10/27/scanner-url-stalkphish-beta/
source: Over Security
date: 2026-10-27
fetch_date: 2026-10-28T07:49:13.897400
---

# Ce lien est-il du phishing ? Découvrez le scanner d’URL StalkPhish (bêta fermée)

[Aller au contenu](#main)

[![StalkPhish](/_astro/logo-black.CenBZhy0_18YWso.webp)](/fr/)

[StalkPhish.io](/fr/products/)

* [Présentation de la plateformeFonctionnalités, cas d’usage et intégrations](/fr/products/stalkphish-io/)
* [Web SearchRecherche gratuite sur stalkphish.io, sans compte](https://www.stalkphish.io)
* [TarifsOffres et essai gratuit de 7 jours, sur stalkphish.io](https://www.stalkphish.io/pricing/)
* [Documentation de l’APIRéférence de l’API REST, sur stalkphish.io](https://www.stalkphish.io/documentation/fullapi/)

[Open source](/fr/community/)

* [PhishingKit-Yara-RulesRègles YARA pour identifier les kits de phishing](/fr/products/phishingkit-yara-rules/)
* [StalkPhish-OSSLe traqueur de kits de phishing](/fr/products/stalkphish/)
* [PhishingKitHunterRepérez les kits qui réutilisent les fichiers de votre site](/fr/products/phishingkithunter/)
* [Le Dico du ScamGlossaire de l’argot des escrocs francophones](/fr/products/dico-du-scam/)
* [Tous nos projets sur GitHub](https://github.com/t4d)

[Blog](/fr/blog/)

[Entreprise](/fr/about/)

* [À propos](/fr/about/)
* [Dans les médias](/fr/press-media/)
* [Contact](/fr/contact/)
* [Mentions légales](/fr/legal-notice/)

[en](/2026/10/27/stalkphish-url-scanner-beta/?lang=en "English version")[Essayer StalkPhish.io](https://www.stalkphish.io)

[StalkPhish.io](/fr/products/)[Présentation de la plateforme](/fr/products/stalkphish-io/)[Web Search ↗](https://www.stalkphish.io)[Tarifs ↗](https://www.stalkphish.io/pricing/)[Documentation de l’API ↗](https://www.stalkphish.io/documentation/fullapi/)

[Open source](/fr/community/)[PhishingKit-Yara-Rules](/fr/products/phishingkit-yara-rules/)[StalkPhish-OSS](/fr/products/stalkphish/)[PhishingKitHunter](/fr/products/phishingkithunter/)[Le Dico du Scam](/fr/products/dico-du-scam/)[Tous nos projets sur GitHub ↗](https://github.com/t4d)

[Blog](/fr/blog/)

[Entreprise](/fr/about/)[À propos](/fr/about/)[Dans les médias](/fr/press-media/)[Contact](/fr/contact/)[Mentions légales](/fr/legal-notice/)

[Essayer StalkPhish.io ↗](https://www.stalkphish.io)

1. [StalkPhish](/fr/)
2. /
3. [Blog](/fr/blog/)
4. /
5. [phishing](/fr/category/phishing/)

Thomas Damonneville·27 octobre 2026·6 min de lecture

# Ce lien est-il du phishing ? Découvrez le scanner d’URL StalkPhish (bêta fermée)

[StalkPhish.io](/fr/category/stalkphish-io/)[phishing](/fr/category/phishing/)[tool](/fr/category/tool/)[threat analysis](/fr/category/threat-analysis/)[hunting](/fr/category/hunting/)[soc](/fr/category/soc/)[CERT](/fr/category/cert/)[CSIRT](/fr/category/csirt/)

![Résultat d’analyse du scanner d’URL StalkPhish : 93/100, CRITICAL](/_astro/scan-cover.B9D498uY_Z22JqCB.webp)

Un lien arrive par SMS, par e-mail ou sur une messagerie, et il faut décider vite s’il s’agit de phishing. L’ouvrir dans un navigateur est risqué, et souvent inutile : les pages de phishing actuelles sont protégées par des **filtres de trafic** qui montrent la vraie page à la victime ciblée, et quelque chose d’inoffensif à tous les autres, à commencer par les analystes et leurs outils.

C’est pour ce problème que nous avons conçu le **[scanner d’URL StalkPhish](https://scan.stalkphish.io/)**. Il repose sur le même moteur de détection que [StalkPhish.io](/fr/products/stalkphish-io/), notre plateforme de détection et d’investigation du phishing, et il est ouvert à un premier groupe de testeurs depuis septembre. Il est encore en **bêta fermée** : pour l’essayer, [demandez-nous un code d’accès](/fr/contact/).

**En bref :**

* Collez une URL suspecte, même neutralisée, et obtenez en quelques secondes un **score de menace de 0 à 100** et un verdict.
* Le scanner **suit toute la chaîne de redirection**, affiche la page dans un vrai navigateur et en garde une capture, depuis une infrastructure isolée.
* Il **détecte le cloaking** : quand les escrocs cachent leur page aux analystes, cette dissimulation devient une preuve.
* Chaque score est accompagné **des signaux qui le justifient** et des données forensiques utiles à un takedown.
* Une **API JSON** permet aux équipes SOC, CERT et anti-fraude de l’intégrer à leurs propres outils.

Pour montrer ce qu’il fait, voici un vrai résultat, section par section : un lien qui ne paie pas de mine, et qui se révèle être un parcours de phishing bien caché.

## D’abord le verdict : un score sur 100

![Score et verdict de l’analyse](/_astro/scan-score.DGWPTElb_aqd6x.webp)

Chaque analyse se termine par un **score de menace de 0 à 100** et un verdict, de *VERY LOW* à *CRITICAL*. Plus le score est élevé, plus il y a d’éléments en faveur du phishing : ce n’est pas un score de confiance. Celle-ci a obtenu **93/100, CRITICAL**, en moins de dix secondes.

Juste en dessous, le scanner dit clairement ce qu’il a pu voir et ce qu’il n’a pas pu voir. Ici, après **10 rebonds**, la destination a répondu, mais sans rien afficher : c’est ainsi qu’un filtre de trafic éconduit un visiteur dont il ne veut pas. Une victime ciblée, elle, aurait été envoyée vers la vraie page. Le scanner ne prétend pas le contraire : ses constats portent sur le parcours et ses hôtes, et il le dit.

Cette transparence compte. Un score faible sur une page injoignable signifie « rien n’a été examiné », pas « rien d’anormal », et le rapport rend la différence visible.

## Ce que le navigateur a vu

![Capture d’écran réalisée par le scanner](/_astro/scan-screenshot.BAHGDkDH_Za41EP.webp)

Le scanner affiche chaque page dans un vrai navigateur et en garde une **capture d’écran**, réalisée depuis une infrastructure isolée : ni votre navigateur ni votre adresse IP ne touchent le site suspect. Ici, la capture montre TikTok, et c’est justement tout l’intérêt : c’est là que le filtre des escrocs a choisi d’envoyer un visiteur qu’il avait identifié comme un analyste.

## Le leurre : du cloaking anti-analyse

![Cloaking anti-analyse détecté](/_astro/scan-cloaking.D2OE8rS9_1i9vKo.webp)

Au lieu de la page de phishing, la chaîne s’est terminée sur `tiktok.com/explore?id=youarecloaked`. Les escrocs ne s’en cachent même pas : *you are cloaked*, « vous êtes masqué ». Cette **redirection leurre** vers un site sans rapport, parfaitement légitime, est la signature du cloaking anti-analyse, et le scanner la traite pour ce qu’elle est : **une preuve**, pas une impasse. Un lien légitime n’a aucune raison d’envoyer les visiteurs automatisés ailleurs.

## Suivre tout le parcours

![Hôtes de la chaîne de redirection](/_astro/scan-chain-hosts.CRAH6yvr_ejp70.webp)

Le lien partait d’un bucket hébergé sur **Google Cloud Storage**, une plateforme de confiance que les escrocs apprécient justement pour son excellente réputation. De là, le visiteur passait d’hôte en hôte :

* un sous-domaine gratuit d’un service de noms de domaine public ;
* un domaine enregistré près de quatre ans plus tôt, recyclé en relais ;
* des domaines de tracking aux combinaisons de mots aléatoires sur des extensions récentes comme `.run` et `.autos`, typiques d’un **système de distribution de trafic** (TDS) ;
* et enfin le leurre.

Chaque hôte est qualifié : point d’entrée, sites légitimes connus, et hôtes inconnus qui n’ont rien à faire au milieu d’une redirection.

![Chaîne de redirection HTTP complète](/_astro/scan-redirect-chain.DX-d9A7U_Z2w9EtW.webp)

La **chaîne de redirection HTTP** complète est conservée, rebond par rebond, avec le code de statut de chaque réponse. Toutes les URL hostiles sont **neutralisées** (`hxxps://…[.]com`) pour ne pas pouvoir être cliquées par erreur quand le rapport est partagé dans un ticket ou une discussion.

## Lire les paramètres des escrocs

![Paramètres décodés de la chaîne de redirection](/_astro/scan-chain-params.By2IiwD8_Zj9pk8.webp)

Les systèmes de distribution de trafic se transmettent des informations d’un rebond à l’autre dans leurs URL, souvent encodées en base64. Le scanner **décode ces paramètres** pour les rendre lisibles : autres domaines de tracking du même réseau, identifiants de campagne, horodatages. Ce sont de précieuses pi...