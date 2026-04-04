---
title: Kubernetes forensics 13 what the container
url: https://synacktiv.com/publications/kubernetes-forensics-13-what-the-container
source: Instapaper: Unread
date: 2026-04-03
fetch_date: 2026-04-04T04:17:56.099794
---

# Kubernetes forensics 13 what the container

[Aller au contenu principal](kubernetes-forensics-13-what-the-container#main-content)

[Rechercher](../search)

Switch Language

FrenchToggle Dropdown

* French
* [English](../en/node/1320)

* [RSS](/en/feed/lastblog.xml)
* [Github](https://github.com/Synacktiv)
* [Twitter](https://twitter.com/synacktiv)
* [Linkedin](https://fr.linkedin.com/company/synacktiv)

[![Accueil](/sites/default/files/logo_synacktiv_blanc.webp)](../index "Accueil")

* [Notre Offre](../notre-offre)
  + [Test dâintrusion / Red Team](../prestations/test-dintrusionred-team)
  + [RÃ©ponse aux incidents](../prestations/reponse-aux-incidents)
  + [Reverse-engineering](../prestations/reverse-engineering)
  + [DÃ©veloppement](../notre-equipe/developpement)
  + [Produits](../produits/kraqozorus)
  + [CSIRT](../csirt)
* [Formations](../offres/formations)
* [Nous rejoindre](../nous-rejoindre)
* [Publications](../nos-publications)
  + [Articles](../publications)
  + [Avis de sÃ©curitÃ©](../advisories)
  + [Ressources](../ressources)
* [La sociÃ©tÃ©](../la-societe)
* [Contact](../contact)

* [RSS](/en/feed/lastblog.xml)
* [Github](https://github.com/Synacktiv)
* [Twitter](https://twitter.com/synacktiv)
* [Linkedin](https://fr.linkedin.com/company/synacktiv)

# Kubernetes forensics 1/3 : what the container ?

RÃ©digÃ© par
Noam Leipold - 26/03/2026 - dans
CSIRT
- [TÃ©lÃ©chargement](kubernetes-forensics-13-what-the-container)

En 2025, le CSIRT Synacktiv a observÃ© une augmentation significative des attaques et des compromissions ciblant les environnements Kubernetes. Le constat est que ces attaques sont vouÃ©es Ã  continuer de se multiplier au mÃªme rythme que la technologie elle-mÃªme. Afin de mieux comprendre le fonctionnement d'un cluster Kubernetes et comment investiguer lors d'un incident de sÃ©curitÃ©, nous avons dÃ©cidÃ© de travailler sur une sÃ©rie d'articles consacrÃ©e Ã  la forensique Kubernetes. Celui-ci est le premier de la sÃ©rie, et se concentre sur la technologie sous-jacente des conteneurs.

Vous souhaitez amÃ©liorer vos compÃ©tences ? DÃ©couvrez nos sessions de **formation** ! [En savoir plus](../offres/formations)

## Introduction

Kubernetes s'est imposÃ© comme la solution d'orchestration des infrastructures cloud-native modernes, gÃ©rant le dÃ©ploiement et la mise Ã  l'Ã©chelle d'applications Ã  grande ampleur. Des entreprises de toutes tailles montent Ã  bord du navire Kubernetes, attirÃ©es par les promesses d'une scalabilitÃ© infinie et de coÃ»ts de calcul optimisÃ©s.

En rÃ©alitÃ©, la situation est un peu plus complexe. Il est vrai que Kubernetes a beaucoup Ã  offrir en termes de dÃ©ploiement d'un grand nombre d'applications dans un environnement (souvent) entiÃ¨rement managÃ©. Pouvoir se concentrer sur des tÃ¢ches productives plutÃ´t que de gÃ©rer une douzaine de serveurs est primordial pour une jeune structure disposant de peu de temps et de ressources humaines.

Les clusters Kubernetes ne sont pas sans dÃ©fauts, ils sont complexes et difficiles Ã  administrer. Ce qu'ils offrent en fonctionnalitÃ©s et en facilitÃ© d'utilisation se paie par une couche technique complexe qui est, le plus souvent, encore abstraite et obscure pour les personnes qui l'utilisent.

Dans une quÃªte permanente de simplicitÃ©, les plus grands fournisseurs cloud tendent Ã  proposer une interface toujours plus simple pour dÃ©ployer et utiliser les ressources Kubernetes via leurs consoles en ligne. Ainsi, il est possible de crÃ©er un compte puis d'utiliser directement l'une des nombreuses offres Kubernetes managÃ©es : AKS pour Azure, EKS pour AWS ou GKE pour Google Cloud et de dÃ©ployer des applications conteneurisÃ©es.

D'un point de vue forensique, l'architecture distribuÃ©e de la plateforme, la variÃ©tÃ© de ses composants et la nature volatile de ses charges de travail compliquent considÃ©rablement la collecte et la prÃ©servation des artÃ©facts forensiques. Mais Ã§a, ce sera pour une prochaine fois.

Dans cet article, nous allons revenir aux fondamentaux du fonctionnement de Kubernetes. Quelles sont les couches techniques, qu'est-ce qu'un conteneur, comment fonctionnent-ils, autant de questions auxquelles nous rÃ©pondrons ici.

## Qu'est-ce qu'un conteneur ?

Remontons un peu dans le temps.

Vous venez de vous rÃ©veiller, nous sommes en fÃ©vrier 2009, vous arrivez au travail. Le nouveau logiciel monolithique de planification des ressources d'entreprise (ERP) doit Ãªtre dÃ©ployÃ© en production. Il a 524 dÃ©pendances, cinq bases de donnÃ©es, deux reverse proxies (??). L'installation prend cinq heures, plante Ã  mi-chemin une fois sur deux sans option de rÃ©cupÃ©ration. Ã chaque fois, il faut rÃ©installer le serveur parce que, pour une raison inconnue, les dÃ©pendances finissent par casser OpenSSH. AprÃ¨s deux semaines d'enfer, vous y parvenez enfin, le logiciel est prÃªt pour la production.

Maintenant, avanÃ§ons dans le temps, nous sommes en 2026, imaginez que vous puissiez empaqueter votre logiciel dans une petite coquille, qui inclurait toutes les dÃ©pendances, tous les services annexes. Ce *conteneur* pourrait embarquer tout ce dont vous avez besoin pour faire tourner le nouvel ERP en production, sur n'importe quel serveur, Ã  n'importe quel moment. Vous pouvez exÃ©cuter le *conteneur* sur n'importe quel serveur et redÃ©marrer tous les services avec une seule commande. Si l'installation Ã©choue, vous pouvez le supprimer et en relancer un nouveau avec un correctif. L'hÃ´te resterait le mÃªme, tout serait *contenu*. Chaque *conteneur* serait isolÃ© de tous les autres tournant sur le mÃªme hÃ´te.

Les conteneurs apportent une couche d'abstraction aux systÃ¨mes de base sur lesquels ils s'exÃ©cutent. Ils permettent aux applications, de toute nature, d'Ãªtre contraintes par un ensemble de limites, sans la surcharge qu'imposent les machines virtuelles traditionnelles.

### Conteneurs vs Machines Virtuelles

Une idÃ©e reÃ§ue courante est que ces deux outils, les conteneurs et les machines virtuelles (VMs), sont identiques. Ce n'est pas le cas.

Une machine virtuelle peut Ãªtre reprÃ©sentÃ©e comme une boÃ®te, tout comme un conteneur. Mais lÃ  oÃ¹ un conteneur ne contient que l'application nÃ©cessaire et ses dÃ©pendances, une machine virtuelle contient l'intÃ©gralitÃ© du systÃ¨me d'exploitation. Un conteneur s'exÃ©cute sur l'hÃ´te via un **moteur de conteneurs** (Docker, Podman), la machine virtuelle tourne sur un hyperviseur (Hyper-V, VMWare vSphere, libvirt, etc.).

![Architecture typique des machines virtuelles](/sites/default/files/inline-images/what-is-vm_2.webp)

Architecture typique des machines virtuelles â Source : <https://www.docker.com/resources/what-container/>

La machine virtuelle offre une meilleure isolation, mais est le plus souvent plus volumineuse, plus lente Ã  l'exÃ©cution et impose davantage de surcharge. Un conteneur est plus lÃ©ger, plus facile Ã  dÃ©ployer, Ã  dÃ©marrer et Ã  arrÃªter Ã  volontÃ©, et trivial Ã  recrÃ©er si nÃ©cessaire.

![Architecture typique de conteneurs](/sites/default/files/inline-images/what-is-container_1.webp)

Architecture typique des conteneurs â Source :Â <https://www.docker.com/resources/what-container/>

### SpÃ©cifications des conteneurs

Les conteneurs peuvent Ãªtre utilisÃ©s sur un large Ã©ventail de systÃ¨mes d'exploitation et de hardware. Presque toutes les applications publiÃ©es sous forme de conteneurs peuvent tourner n'importe oÃ¹. Cela est dÃ» Ã  la spÃ©cification OCI.

OCI signifie **Open Container Initiative**. C'est une structure de gouvernance rattachÃ©e Ã  la Linux Foundation qui maintient des standards ouverts pour les conteneurs. Elle a Ã©tÃ© crÃ©Ã©e en 2015, principalement parce que Docker Ã©tait devenu le standard de facto et que l'industrie souhaitait que les formats de conteneurs et les runtimes ne soient pas contrÃ´lÃ©s par une seule entreprise.

L'OCI maintient trois spÃ©cifications :

* **SpÃ©cification du runtime** : dÃ©finit comment exÃ©cuter un conteneur. Elle dÃ©crit ce qu'un runtime de conteneurs doit attendre ...