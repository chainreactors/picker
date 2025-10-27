---
title: Towards the Automation of Book Typesetting: Computational Approaches in Editorial Design
url: https://buaq.net/go-251622.html
source: unSafe.sh - 不安全
date: 2024-07-21
fetch_date: 2025-10-06T17:39:21.108181
---

# Towards the Automation of Book Typesetting: Computational Approaches in Editorial Design

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

![]()

Towards the Automation of Book Typesetting: Computational Approaches in Editorial Design

Authors:(1) Sérgio M. Rebelo, University of Coimbra, Centre for Informatics and Systems of the Uni
*2024-7-20 20:0:20
Author: [hackernoon.com(查看原文)](/jump-251622.htm)
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

## 2. Computational Approaches in Editorial Design

Systematic approaches have been popular in layout design since the mid-twentieth century when some creative practitioners designed layouts based on grids and the variation of the visual features of typographic elements [4–6]. Some works have explored algorithmic approaches for book layout design. In the 1960s, Gerstner introduced a selective and combinatorial method for the design of graphics, including layouts [7]. Afterwards, he translated it into a logical language that computers could understand in Compendium for Literates: A system of Writing [8]. LeWitt compiled, in 1971, a set of formal instructions to design a conceptual art exhibition catalogue [9]. Already in the 1980s, Knuth and Plass [10] presented a dynamic programming algorithm to page breaks avoiding widows and orphans and employed it to typeset a two-column dictionary. Soon thereafter, Knuth introduced the parametric typeface design language, Metafont [11] and the TeX typesetting system [12], enabling anybody to produce a book using a structural markup language and a set of high-level commands. Cooper and her students, at the Visible Language Workshop, experimented with the generation of layouts, e.g. publications that resulted from the collaboration with IBM [13] and the cover for Design Quarterly 142 [14]. In the mid1990s, Maeda also designed a series of digital booklets, the Reactive Book series, where the graphics are controlled interactively by user input [15].

Nevertheless, in the last two decades, we observed the increasing employment of the use of computational graphic design approaches, especially because of the development of easier-to-use creative code environments [16,17]. A solid overview of the field is presented, for instance, by Reas et al. [6] or Richardson [18]. These approaches have been explored in several artistic and creative domains, including the generation of visual and communication artefacts such as poster designs (e.g. Rebelo et al. [19] or Guo et al. [20]), banners (e.g. Gatarski [21] or Yin et al. [22]), user interfaces (e.g. Quiroz et al. [23] or Amitani et al. [24]), visual identities (e.g. Levin [25] or Neue [26]), type designs (e.g. Ahn & Jin [27] or Martins et al. [28]), among others. In the context of book typesetting, two frameworks are stimulating the adoption of computational practices. The library Basil.js [29] provides friendly and accessible tools for scripting and automation in Adobe InDesign. Then, the opensource framework The Magic Book [30] facilitates the design, production, and self-publishing of books.

Tailor-made procedural and template-based approaches are employed in the generation and definition of layouts, modification of layouts based on their contents and/or inter-relationships between the elements. LettError type design studio used random processes and parametric design methods to design several typographic artefacts such as calendars, type specimens and even their portfolio [31,32]. Oliveira [33] presented a recursive division method to place elements on both one and multiple-column grid layouts. Cleveland [34] proposed a method for generating style-based design layouts that explores the inter-relationships between text and graphics. Also, he presented a system to generate layouts employing these principles. LUST developed a set of scripts to layout and stylise the book “I Read Where I am” informed by its content [35]. Damera-Venkata et al. [36] presented a template-based probabilistic framework for generating document layouts for variable content. Ahmadullin and Damera-Venkata [37] also presented a probabilistic model for newspaper typeset that, based on given content, divides the available layout into regions and optimises the content to fit within these regions. Flipboard developed Duplo [38], a layout engine that creates news magazines adapted to its contents and based on a set of heuristics such as the amount and flux of text or the existence and position of images.

We can also observe the use of Artificial Intelligence approaches for typesetting. Evolutionary computation and greedy approaches have been used to create layouts with varied purposes. For example, Geigel and Loui [39] evolved layouts for photo books by evaluating different aesthetic criteria. Goldenberg [40] employed an evolutionary approach to automatically generate page layouts, minimising the waste of space on the page. Gonzalvez et al. [41] used a greedy simulated annealing algorithm to create multi-column newspaper layouts. Purvis et al. [42] automatically evolved documents using a multi-objective optimisation approach, considering a set of layout constraints and aesthetic measures. Quiroz et al. [43] evolved brochure documents according to user preferences and design guidelines. Strecker and Hennig [44] proposed a grid-based method for newspaper layouts, minimising the wasted space and bearing in mind newspaper design aesthetic measures. Boll et al. [45] and Sandhaus et al. [46,47] evolved photo layouts based on rules of layout design and proposed a method to transform a blog into a photo book considering different aesthetic requirements. Önduygu [48] developed the system Gráphagos that generates compositions through the interactive evolution of specific features of visual elements. Klein [49] developed the tool Crossing, Mixing, Mutating to create variations in a template using genetic operators. Later, an updated version of this tool was released as an InDesign plug-in named Evolving Layout [50]. Lopes et al. [51] developed the system evoDesigner, which automatically creates and evolves designs in the InDesign environment. Recently, Machine Learning approaches have been employed in the layout design field taking into account the relation between elements on layout and the learning of specific typesetting and design styles, e.g. Zheng et al. [52], Li et al. [53], or Kikuchi et al. [54].

Our analysis of the related wor...