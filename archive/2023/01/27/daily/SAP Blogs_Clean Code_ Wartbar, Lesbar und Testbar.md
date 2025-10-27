---
title: Clean Code: Wartbar, Lesbar und Testbar
url: https://blogs.sap.com/2023/01/26/clean-code-wartbar-lesbar-und-testbar/
source: SAP Blogs
date: 2023-01-27
fetch_date: 2025-10-04T04:58:05.786157
---

# Clean Code: Wartbar, Lesbar und Testbar

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Clean Code: Wartbar, Lesbar und Testbar

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/159422&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Clean Code: Wartbar, Lesbar und Testbar](/t5/technology-blog-posts-by-sap/clean-code-wartbar-lesbar-und-testbar/ba-p/13554815)

![haeuptle](https://avatars.profile.sap.com/d/0/idd099b643170a795cffeb57f54e74f97436f5a5f26bb8d41fc62037e69aae99a0_small.jpeg "haeuptle")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[haeuptle](https://community.sap.com/t5/user/viewprofilepage/user-id/40145)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=159422)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/159422)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13554815)

‎2023 Jan 26
5:55 PM

[8
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/159422/tab/all-users "Click here to see who gave kudos to this post.")

3,499

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [Java](https://community.sap.com/t5/c-khhcw49343/Java/pd-p/615693459582413452469752593601406)
* [JavaScript](https://community.sap.com/t5/c-khhcw49343/JavaScript/pd-p/506421944534752500398156104608974)
* [Open Source](https://community.sap.com/t5/c-khhcw49343/Open%2520Source/pd-p/b2aac474-1581-4b1b-8932-de5f60b52558)
* [SAPUI5](https://community.sap.com/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)
* [Research and Development](https://community.sap.com/t5/c-khhcw49343/Research%2520and%2520Development/pd-p/708931460062032886984100414137377)

* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)
* [Java

  Programming Tool](/t5/c-khhcw49343/Java/pd-p/615693459582413452469752593601406)
* [JavaScript

  Programming Tool](/t5/c-khhcw49343/JavaScript/pd-p/506421944534752500398156104608974)
* [SAPUI5

  Programming Tool](/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)
* [Research and Development

  Topic](/t5/c-khhcw49343/Research%2Band%2BDevelopment/pd-p/708931460062032886984100414137377)
* [Open Source

  Programming Tool](/t5/c-khhcw49343/Open%2BSource/pd-p/b2aac474-1581-4b1b-8932-de5f60b52558)

View products (6)

Clean Code ist ein Begriff, der Software beschreibt, die einfach zu lesen, zu verstehen, zu warten und zu testen ist. In diesem Blog möchte ich einige wichtige Prinzipien zusammenfassen, um Anfängern einen Einstieg in das Thema zu ermöglichen. Außerdem soll der Blog eine Verbindung zum Style Guide Repository, den Büchern und aktuellen Initiativen herstellen, zu denen Experten beitragen können. Wenn Sie kein Update zu Clean Code, Testautomatisierung, Communities of Practice, Entscheidungsfindung, Testbarkeit und anderen technischen / handwerklichen / architektonischen Themen verpassen wollen, [abonnieren Sie den brandneuen Newsletter](https://ecosystem4engineering.substack.com/p/collaboration-on-improving).

Der Artikel ist eine Übersetzung von [Clean Code: Writing maintainable, readable and testable code](https://blogs.sap.com/2022/12/21/clean-code-writing-maintainable-readable-and-testable-code/), um die deutschsprachige Zielgruppe noch besser zu erreichen.

## Was macht Clean Code aus?

Um Clean Code zu erhalten, muss man eine Reihe von Best Practices und Standards befolgen, z. B. aussagekräftige Namen verwenden, Funktionen klein und konzentriert halten und sparsam mit Kommentaren umgehen. Eine Codebasis, die lesbar und wartbar ist, ist für eine nachhaltige Entwicklung unerlässlich. Die Bücher Clean Code von Robert C. Martin, Code Complete von Steve McConnell, The Pragmatic Programmer von David Thomas/Andy Hunt und einige andere Bücher enthalten viele Best Practices und Beispiele für Clean Code.

### Was ist nicht Clean Code?

Nicht Clean Code ist ein Code, der schwer zu lesen, zu verstehen und zu pflegen ist. Er kann schlecht organisiert sein, verwirrende oder irreführende Namen haben, inkonsistent gestaltet sein und andere Probleme aufweisen, die die Arbeit mit ihm erschweren.

Einige Beispiele für unsauberen Code können sein:

* Code mit langen, komplexen Funktionen, die schwer zu verstehen, zu testen und zu warten sind.

* Code mit schlechten Namenskonventionen, z. B. Variablen mit kurzen, nicht beschreibenden Namen oder Funktionen mit Namen, die ihren Zweck nicht genau wiedergeben.

* Code mit inkonsistenter Gestaltung, z. B. inkonsistente Einrückung oder Abstände, die das Lesen und Verstehen erschweren können.

* Code mit unnötigem oder redundantem Code, der die Wartung und das Verständnis erschwert.

* Code, der die Testautomatisierung erschwert, z. B. statische Kopplung zwischen Klassen.

Insgesamt ist Code, der nicht clean ist, oft anfälliger für Fehler und Bugs und kann zeitaufwändiger sein, da er mehr Aufwand zum Verstehen, Testen und Warten erfordert.

![](/legacyfs/online/storage/blog_attachments/2023/01/CleanCodeComic.png)

Clean Code Comic

**Clean Code: Code Quality von xkcd.com/1513/ unter [Creative Commons BY-ND 2.5](https://xkcd.com/license.html)**

### Vorteile von Clean Code

Das Schreiben von Clean Code hat viele Vorteile, unter anderem:

* Verbesserte Lesbarkeit und Verständlichkeit: Clean Code ist leichter zu lesen und zu verstehen, was Entwicklern die Anpassung, Fehlersuche und Wartung erleichtern kann.

* Geringeres Risiko von Fehlern und Bugs: Clean Code ist im Allgemeinen zuverlässiger und weniger fehleranfällig, da er leichter zu verstehen, zu testen und zu warten ist.

* Höhere Produktivität: Clean Code ist einfacher und schneller zu bearbeiten, was die Produktivität und Effizienz der Entwickler steigern kann. [Laut einer Metastudie kann unsauberer Code mehr als 15 Mal mehr Fehler enthalten und die Produktivit...](https://www.linkedin.com/posts/klaus-h%C3%A4uptle-951a0349_according-to-a-meta-study-unhealthy-code-activity-6999048527821557760-mrWr?utm_source=share&utm_medium=member_desktop).

* Verbesserte Anpassungs- und Entwicklungsfähigkeit: Sauberer, modularer Code lässt sich leichter ändern und aktualisieren, so dass sich die Software im Laufe der Zeit weiterentwickeln und an veränderte Anforderungen anpassen kann.

* Verbesserte Teamzusammenarbeit: Clean Code ist für Teammitglieder leichter zu verstehen und zu bearbeiten, was die Zusammenarbeit und Kommunikation innerhalb des Teams verbessern kann.

* Bessere langfristige Wartbarkeit: Clean Code lässt sich im Laufe der Zeit leichter warten und aktualisieren, was Zeit und Ressourcen sparen kann. Außerdem verringert sich das Risiko, wenn Ingenieure zu anderen Projekten wechseln oder das Unternehmen verlassen.

* Verbesserte Wiederverwendung von Code: Clean, modularer Code lässt sich leichter wiederverwenden und in verschiedenen Kontexten neu einsetzen, was Zeit und Ressourcen sparen kann.

* Bessere Leistung: Clean Code ist im Allgemeinen effizienter und kann schnelle...