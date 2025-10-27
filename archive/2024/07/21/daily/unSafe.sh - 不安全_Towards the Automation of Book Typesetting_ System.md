---
title: Towards the Automation of Book Typesetting: System
url: https://buaq.net/go-251623.html
source: unSafe.sh - 不安全
date: 2024-07-21
fetch_date: 2025-10-06T17:39:22.384052
---

# Towards the Automation of Book Typesetting: System

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/f5e1e2170d569a33eab103dbe5b29380.jpg)

Towards the Automation of Book Typesetting: System

Authors:(1) Sérgio M. Rebelo, University of Coimbra, Centre for Informatics and Systems of the Uni
*2024-7-20 20:0:19
Author: [hackernoon.com(查看原文)](/jump-251623.htm)
阅读量:6
收藏*

---

**Authors:**

(1) Sérgio M. Rebelo, University of Coimbra, Centre for Informatics and Systems of the University of Coimbra, Department of Informatics Engineering, Coimbra, Portugal and a Corresponding author;

(2) Tiago Martins, University of Coimbra, Centre for Informatics and Systems of the University of Coimbra, Department of Informatics Engineering, Coimbra, Portugal and a Corresponding author;

(3) Diogo Ferreira, University of Coimbra, Centre for Informatics and Systems of the University of Coimbra, Department of Informatics Engineering, Coimbra, Portugal and a Corresponding author;

(4) Artur Rebelo, University of Coimbra, Centre for Informatics and Systems of the University of Coimbra, Department of Informatics Engineering, Coimbra, Portugal.

## Table of Links

* [Abstract and 1. Introduction](http://hackernoon.com/preview/lqc7s9McIHaOSRbs4etl?ref=hackernoon.com)
* [Computational Approaches in Editorial Design](http://hackernoon.com/preview/n4YJ8uNNtVENT42MTngG?ref=hackernoon.com)
* [System](http://hackernoon.com/preview/KxgVbk3GearXCPnUwwZw?ref=hackernoon.com)
* [Experimentation and Discussion](http://hackernoon.com/preview/1Jl6aqDrMKXoqy164QTd?ref=hackernoon.com)
* [Conclusion](http://hackernoon.com/preview/k2YGlvEzOHfyIx8SDqpq?ref=hackernoon.com)
* [Acknowledgments and References](http://hackernoon.com/preview/HCmbATb4UUH04uNfqFk4?ref=hackernoon.com)

## 3. System

We developed a computer system to automatically typeset books from content provided by the user. This system is developed as a computer script that operates inside Adobe InDesign software which is popular among graphic designers working in the field of typography. We idealised and implemented the system to take advantage of the typeset functionalities supplied with InDesign, which can be controlled via scripting. By integrating the system with InDesign, we allow users to generate design variations and easily edit them within a familiar working environment. One can find demonstration videos in the supplementary files. To install the system in the InDesign environment, the user only needs to copy the folder that contains the system files to the scripts folder in the application directory. To facilitate access to the system, we also made available a script that creates a dedicated tab for the system in the InDesign navigation menu. The system installation files and source code are available at https://cdv.dei.uc.pt/2019/scriptedpages. [1]

In the following subsections, we describe the user interface of the system and explain how its engine works.

### 2.1 Interface

Figure 2 shows different snapshots of the user interface built to enable the interactive control of the inner workings of the system. The user interface is structured in a series of five tabs. In each tab, one can set specific properties of the composition or let the system choose automatically based on a set of predefined rule-based values for those properties.

The first interface tab “Document” (Figure 2a) concerns the structural characteristics of the document. It allows the user to set the page size, margins, number of columns and gutter. There is also an option to import settings stored in a file.

In the second tab “Input” (Figure 2b), the user provides the content of the book to be typeset. To that end, the interface offers two options. The first option is to load a Microsoft Word file containing only text, text and images, or only images. The second option is to load a Microsoft Word file containing only the text and a folder containing the images. For this second option, the place where each image should be inserted must be identified in the text using a tag @imageFileName@, which will be replaced by the image with the same name contained in the loaded folder. In addition, the user can choose whether to generate a table of contents and/or colophon for the book. The last option of this tab allows the user to select the language of the input text so that it is possible to correctly hyphenate words.

The third tab “Styles” (Figure 2c) concerns the definition and mapping of paragraph styles. The user has three options to choose from. The first option is to keep the styles imported from the input Word document. The second option is to map each style of the input document to another paragraph style selected, manually or randomly, from a list created from all fonts installed on the computer, while keeping the remaining paragraph attributes. The last option is to let the system generate the styles, suggesting font combinations based on the rules entered in the system (these rules are explained in the next subsection).

In the fourth tab “Experimental” (Figure 2d), the user can toggle experimental features that can be applied to the generated book. In the presented version of the system, there are four experimental features: (i) draw a colour background on half of each book page; (ii) draw a colour gradient along the inner and/or outer margins of the pages; (iii) apply a random indentation to each text paragraph; and (iv) make the cover title as large as possible. The purpose of these features is to increase the uniqueness of the resulting designs. The user can also opt to let the system randomly choose if any experimental features should be applied by selecting the checkbox “Surprise me.” Furthermore, new features can be implemented and added to the system at any time.

After interacting with these four tabs of settings, the user can start creating book designs by clicking on the button “Create” located at the bottom right corner of the interface. This button will start the engine of the system which will automatically create a new InDesign document and typeset a new book from the content and settings chosen by the user.

Once the typeset process is complete, the result is presented to the designer as an editable InDesign document. From that moment on, the user can, for instance: (i) adopt the generated book as a final design; (ii) use the generated book as a starting design from which the designer can make any changes or refinements needed; or (iii) continue to use the system to generate more designs until a more suitable design is found.

![Figure 2. Snapshots of the system, showing the five different tabs of the user interface: (a) Document, (b) Input, (c) Styles, (d) Experimental and (e) Properties. Demonstration videos of the system can be found in the supplementary files.](https://hackernoon.imgix.net/images/fWZa4tUiBGemnqQfBGgCPf9594N2-zj830nm.png?auto=format&fit=max&w=1080)

There is another interface tab, entitled “Properties” (Figure 2e), which not only overviews the settings used in the generation of a book but also enables the user to save those settings to a file. Later, this settings file can be imported to the system using the first interface tab, as mentioned earlier. This functionality can be useful, for example, to facilitate the typeset of different books using the same settings. This last tab is only accessible after a book is generated. After the generation, it is also made visible a button that enables the user to generate a new book, maintaining the same input document and predefined settings.

### 2.2 Engine

The system operates based on a series of typographic rules, styles and principles (Table 1) which were identified and collected from lite...