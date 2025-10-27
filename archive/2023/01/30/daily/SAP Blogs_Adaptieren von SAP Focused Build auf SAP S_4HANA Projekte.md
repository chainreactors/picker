---
title: Adaptieren von SAP Focused Build auf SAP S/4HANA Projekte
url: https://blogs.sap.com/2023/01/29/adaptieren-von-sap-focused-build-auf-sap-s-4hana-projekte/
source: SAP Blogs
date: 2023-01-30
fetch_date: 2025-10-04T05:10:06.027768
---

# Adaptieren von SAP Focused Build auf SAP S/4HANA Projekte

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Adaptieren von SAP Focused Build auf SAP S/4HANA P...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/161113&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Adaptieren von SAP Focused Build auf SAP S/4HANA Projekte](/t5/technology-blog-posts-by-members/adaptieren-von-sap-focused-build-auf-sap-s-4hana-projekte/ba-p/13556536)

![Daniel_Enderli](https://avatars.profile.sap.com/f/e/idfebfba3ea1ceebf41ddea8cc08c626c2b7468602b70bd873fbaed2d689a7e574_small.jpeg "Daniel_Enderli")

![SAP Champion](/html/@B3DACAC6163F980483AC32558EB69695/rank_icons/champion-rank-16x16.svg "SAP Champion")
[Daniel\_Enderli](https://community.sap.com/t5/user/viewprofilepage/user-id/2995)

SAP Champion

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=161113)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/161113)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13556536)

‎2023 Jan 29
10:28 PM

[4
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/161113/tab/all-users "Click here to see who gave kudos to this post.")

2,074

* SAP Managed Tags
* [SAP Activate](https://community.sap.com/t5/c-khhcw49343/SAP%2520Activate/pd-p/714d86bf-f0de-4038-81e4-25c791c15f0c)
* [SAP Cloud ALM](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520ALM/pd-p/73554900100800002513)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [SAP Solution Manager](https://community.sap.com/t5/c-khhcw49343/SAP%2520Solution%2520Manager/pd-p/01200615320800000636)
* [Focused Build for SAP Solution Manager](https://community.sap.com/t5/c-khhcw49343/Focused%2520Build%2520for%2520SAP%2520Solution%2520Manager/pd-p/bd524d9b-1ee4-452d-a5b4-c25520976179)
* [SOLMAN Project Management](https://community.sap.com/t5/c-khhcw49343/SOLMAN%2520Project%2520Management/pd-p/859834545111167391953063734572784)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP Solution Manager

  SAP Solution Manager](/t5/c-khhcw49343/SAP%2BSolution%2BManager/pd-p/01200615320800000636)
* [SOLMAN Project Management

  Software Product Function](/t5/c-khhcw49343/SOLMAN%2BProject%2BManagement/pd-p/859834545111167391953063734572784)
* [Focused Build for SAP Solution Manager

  Software Product Function](/t5/c-khhcw49343/Focused%2BBuild%2Bfor%2BSAP%2BSolution%2BManager/pd-p/bd524d9b-1ee4-452d-a5b4-c25520976179)
* [SAP Activate

  Services and Support](/t5/c-khhcw49343/SAP%2BActivate/pd-p/714d86bf-f0de-4038-81e4-25c791c15f0c)
* [SAP Cloud ALM

  Software Product](/t5/c-khhcw49343/SAP%2BCloud%2BALM/pd-p/73554900100800002513)

View products (6)

# Einführung

Anhand der Erfahrungen aus mehreren SAP S/4HANA Projekten, kann ich definitiv sagen, dass das Adaptieren von SAP Focused Build auf die SAP S/4HANA Projektmethodik ein wesentlicher Schlüssel zum Erfolg ist.

Egal ob Greenfield, Brownfield oder Selective Data Transition Vorgehen, bei all diesen Ansätzen ist es gleichwohl wichtig, das Thema SAP ALM von Beginn weg und somit frühzeitig mit dem Projekt zu synchronisieren.

***«Involvieren Sie die Verantwortlichen Personen im Projekt und machen Sie diese zu Beteiligten.»***

Je nachdem welche ALM Funktionalitäten und wie tief und integriert sie diese im Projekt einsetzen möchten, fällt die Wahl entweder auf den SAP Solution Manager mit Focused Build oder auf SAP Cloud ALM. Selbstverständlich gibt es oftmals viele weitere unterstützende Werkzeuge, welche für die Planung und Steuerung eines Projektes eingesetzt und auch integriert werden können. Ich fokussiere mich jedoch in diesem Blogpost auf die SAP-zentrischen ALM Werkzeuge. Dabei zeige ich auf, wie diese optimal auf das Projket abzustimmen sind.

## Adaptieren von SAP Focused Build auf SAP S/4HANA Projekte

Als erster Schritt ist es wichtig, dass ein Alignment der Programm-/ Projektplanung mit in diesem konkreten Beispiel SAP Focused Build erfolgt. In der Swisscom haben wir dazu fünf Schritte definiert, um die wesentlichen Fragestellungen für ein effektives Alignment zu beantworten. Das Ziel dieser fünf Schritte ist, sicherzustellen, dass der Focused Build Requirements to Deploy Prozess sauber mit der Projektplanung und Projektsteuerung verzahnt wird.

![](/legacyfs/online/storage/blog_attachments/2023/01/alignment_02-scaled.jpg)

Source: Swisscom, Alignment of SAP Focused Build with SAP S/4HANA Projects

## Festlegen des Projektvorgehensmodells und Nutzung von Beschleunigern

Ebenfalls ist zu Beginn eines Projektes festzulegen, nach welchem Projektvorgehensmodell das SAP S/4HANA Projekt abgewickelt werden soll. Traditionell nach Wasserfall, nach agiler Vorgehensmethodik oder eine Mischung aus Wasserfall und Agil und somit ein Hybrides Modell.

Hierzu existieren von SAP bereits verschiedene Best Practice Ansätze, welche mit überschaubarem Aufwand auf ein eigenes Projekt adaptiert werden können.

![](/legacyfs/online/storage/blog_attachments/2023/01/agile-build.jpg)

Source: SAP, Project procedure and accelerators

## Projekt Setup in Focused Build

Anhand der vorhergehenden Abklärungen und deren Ergebnisse können anschliessend in Focused Build die passenden Strukturen für Projekt, Releases, Cycles, Waves und Sprints abgebildet werden.

Hier ist es wichtig, dass die Plandaten des Projektplan mit den Plandaten in Focused Build synchron gehalten werden.

Ich möchte hier auch nochmals betonen, dass Focused Build sowohl für ein Vorgehen nach Wasserfallmethodik (siehe im Bild Variante 1), wie auch für eine agile Vorgehensmethodik (siehe im Bild Varianten 2 und 3), genutzt werden kann.

![](/legacyfs/online/storage/blog_attachments/2023/01/fb-projects-scaled.jpg)

Source: SAP, Focused Build project variants

## Abgleich der Rollen, Aufgaben und Verantwortungen

Als nächstes müssen die Rollen, Aufgaben, und Verantwortungen abgeglichen werden. In SAP Focused Build existieren vordefinierte Rollen, für welche viele hilfreichen SAP Fiori Apps bereitstehen. Es geht hierbei um den Abgleich der im Projekt definierten Rollen mit den SAP Focused Build Rollen. Jede Rolle hat Schnittstellen zu anderen Rollen. Es ist daher sehr wichtig, auch die Übergabe der einzelnen Lieferobjekte an eine nachfolgende Rolle sauber zu beschreiben.

![](/legacyfs/online/storage/blog_attachments/2023/01/roles.jpg)

Source: Swisscom, Alignment of roles, tasks and responsibilities

## Fokus auf die 10 SAP Quality Principles

Immer hilfreich ist es, sich regelmässig die 10 SAP Quality Principles in Erinnerung zu rufen. Stellen Sie sich selber die Frage, wie sie diese operativ umsetzen möchten. Stellen Sie sich auch die Frage wer für diese Principles verantwortlich ist und wie sie fortlaufend überwacht werden können.

Die nachfolgende Illustration veranschaulicht sehr schön, welche Hilfsmittel von SAP Focused Build welche Quality Prnciples abdecken. Es bedarf also auch hier auf einer tieferen Ebene auf ein Alignment von Quality Principle zu Focused Build Funktionalität.

![](/legacyfs/online/storage/bl...