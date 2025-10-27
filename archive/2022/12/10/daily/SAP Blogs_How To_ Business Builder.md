---
title: How To: Business Builder
url: https://blogs.sap.com/2022/12/09/how-to-business-builder/
source: SAP Blogs
date: 2022-12-10
fetch_date: 2025-10-04T01:06:00.134135
---

# How To: Business Builder

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* How To: Business Builder

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/162142&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How To: Business Builder](/t5/technology-blog-posts-by-members/how-to-business-builder/ba-p/13561716)

![WH1](https://avatars.profile.sap.com/0/c/id0cc90a8afc189a913430bf835ae50ec2b8d81afb8868324205b7a84a0c604933_small.jpeg "WH1")

[WH1](https://community.sap.com/t5/user/viewprofilepage/user-id/44985)

Discoverer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=162142)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/162142)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13561716)

‎2022 Dec 09
7:04 PM

[5
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/162142/tab/all-users "Click here to see who gave kudos to this post.")

1,511

* SAP Managed Tags
* [SAP Datasphere](https://community.sap.com/t5/c-khhcw49343/SAP%2520Datasphere/pd-p/73555000100800002141)

* [SAP Datasphere

  Software Product](/t5/c-khhcw49343/SAP%2BDatasphere/pd-p/73555000100800002141)

View products (1)

In diesem Blog befassen wir uns mit dem Thema des Business Builder in der SAP Data Warehouse Cloud. Um Ihnen einen kleinen Überblick über die Vorgehensweise und die verschiedenen Funktionen des Business Builder näher zu bringen, versuche ich Ihnen Schritt für Schritt ein kleines Tutorial bereitzustellen, damit Sie als Nutzer der Data Warehouse Cloud für Ihr nächstes PoC gut gewappnet sind.

## New Dimension

Im ersten Schritt erstellen wir eine Dimension. Dimensionen repräsentieren typischerweise Stammdaten wie Produkte, Kunden oder Zeit. Dimensionen mit Attributen müssen erstellt werden, die Sie für ihre Analyse verwenden möchten. Je besser Sie die Dimensionen aufbereiten und die passenden Attribute auswählen, desto variabler wird ihre Datengrundlage für weitere Fragestellungen.

Nachdem Sie im Business Builder sich befinden, klicken Sie auf „New Dimension“, um eine neue Dimension mit festgelegten Attributen und Schlüsseldefinitionen festzulegen.

![](/legacyfs/online/storage/blog_attachments/2022/11/Screenshot-2022-10-05-112933-1.jpg)

Es öffnet sich ein neues Fenster mit der Überschrift „Create New Dimension“. Hier können Sie nun die Datensätze auswählen, die Sie nutzen möchten. Diese müssen vorher im Data Builder hochgeladen und fertig modelliert sein, damit Sie diese auch im Business Builder nutzen können. In meinem Fall wähle ich „Customer Masterdata“.

![](/legacyfs/online/storage/blog_attachments/2022/11/Screenshot-2022-10-05-143654-2.png)

Nun öffnet sich die Allgemeine Infoseite. Hier finden Sie verschiedene Informationen zur Datei wie Name, technischer Name, Datenquelle, Version und den jeweiligen Status der Datei.

![](/legacyfs/online/storage/blog_attachments/2022/11/Screenshot-2022-10-05-143943-1.png)

![](/legacyfs/online/storage/blog_attachments/2022/11/Screenshot-2022-10-05-144012-1.png)

Im nächsten Schritt setze ich Attribute und die Schlüsseldefinitionen fest. Sie haben die Möglichkeit zwischen vorher erkannte Attribute zu wählen oder Sie können eigendefinierte Attribute selbst festlegen und diese dann auch später für ihre Analysen nutzen. Hierfür klicken Sie einfach auf die jeweiligen Reiter und nutzen das Plus Symbol für die eigendefinierten Attribute oder Sie nutzen das Symbol Tabellenerweiterung. Dort befinden sich die Attribute, die Data Warehouse Cloud automatisch erkennt.

![](/legacyfs/online/storage/blog_attachments/2022/11/Screenshot-2022-10-05-161947-2.png)

![](/legacyfs/online/storage/blog_attachments/2022/11/Screenshot-2022-10-05-162109-1.png)

Nachdem Sie die Attribute und Schlüsseldefinitionen festgelegt haben, können Sie diese nun speichern und somit haben Sie die erste Dimension erstellt. Natürlich haben Sie die Möglichkeit diese Dimension weiter zu bearbeiten. Input Parameter, Hierarchien, Assoziationen und Autorisation Szenarien können genutzt werden, um die Dimension weiter aufzubereiten.

## Analytical Dataset

Mit der Erstellung einer Dimension können wir uns nun an die Faktendaten anschauen. Die Faktendaten werden als analytischer Datensatz verwendet und bilden den Kern des Datenmodells. Diese Faktendaten sollten mindestens eine Kennzahl enthalten und die Fremdschlüssel zu der Dimension liefern, die wir vorher angelegt haben und diese wir später in SAP Analytical Cloud analysieren wollen. Zu den Faktendaten können beispielsweise Buchhaltungsdaten aus dem Finanzwesen, Verkaufsdaten, Lieferketten oder Gehaltszahlungen gehören.

Um ein analytisches Dataset zu erstellen, klicken sie auf „New Analytical Dataset“. Wie bei Erstellung der Dimension öffnet sich zuerst ein Fenster, wo Sie wieder ein die zu nutzende Datei auswählen wollen, die Sie im Business Builder bearbeiten müssen. Wie auch hier muss dieser Datensatz vorher im Data Builder vorbereitet und modelliert sein. Nachdem auswählen der Datei, klicken Sie auf „Create“, um fortzufahren.

![](/legacyfs/online/storage/blog_attachments/2022/11/Screenshot-2022-10-05-164318-2.png)

Wie im Kapitel der Dimension, öffnet sich die allgemeine Informationsseite. Auch hier haben Sie die Möglichkeit jeweils den Namen, technischen Namen, die Version und den Status einzusehen und gegeben falls zu ändern.

Im nächsten Schritt definieren wir wieder die verschiedenen Kennzahlen, die wir analysieren wollen, fügen Attribute ein und die Schlüsseldefinitionen.

![](/legacyfs/online/storage/blog_attachments/2022/11/Screenshot-2022-10-05-165228-1.png)

Nun wollen wir diese Faktentabelle, die den Kern unseres Datenmodells ausmacht mit der Dimension, die wir vorher erstellt haben, in Verbindung setzen. Dies können Sie mit dem Reiter „Associations“ machen. Hierbei ist es wichtig darauf zu achten, dass die Schlüsseldefinition, die Sie in der Dimension erstellt haben, auch in der Faktentabelle vorhanden sind, um eine gültige Verbindung zwischen Faktentabelle und Dimension herstellen zu können. Klicken Sie auf den Reiter Associations dann auf das Plus Symbol wählen Sie die Dimension aus mit dem sie die Faktentabelle verbinden möchten und wählen Sie die Schlüsseldefinition aus, die sowohl in der Faktentabelle als auch in der Dimension vorhanden ist. In diesem Fall wäre die richtige Schlüsseldefinition „Costumer\_ID“.

![](/legacyfs/online/storage/blog_attachments/2022/11/Screenshot-2022-10-05-170308-1.png)

![](/legacyfs/online/storage/blog_attachments/2022/11/Screenshot-2022-10-05-170528-2.png)

Sobald Sie die Verbindung zwischen der Dimension und des analytischen Datensets hergestellt haben, durch die Schlüsseldefinition, müssen Sie diese auch noch benennen. Nachdem Sie dies getan haben, klicken Sie auf Save und somit habe Sie in diesem Schritt ein analytisches Datenset mit der Dimension anhand von Schlüsseldefinitionen verbunden.

![](/legacyfs/online/storage/blog_attachments/2022/11/Screenshot-2022-10-06-120801-1.png)

![](/legacyfs/online/storage/blog_attachments/2022/11/Screenshot-2022-10-06-121612-1.png)

## Consumption Model und Perspectives

Im ...