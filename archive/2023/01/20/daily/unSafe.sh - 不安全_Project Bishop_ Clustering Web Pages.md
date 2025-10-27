---
title: Project Bishop: Clustering Web Pages
url: https://buaq.net/go-146242.html
source: unSafe.sh - 不安全
date: 2023-01-20
fetch_date: 2025-10-04T04:21:17.057066
---

# Project Bishop: Clustering Web Pages

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

![](https://8aqnet.cdn.bcebos.com/35b57098187dbab79c9a47a448e6208d.jpg)

Project Bishop: Clustering Web Pages

Written by Jose Selvi and Thomas AtkinsonIf you are a Machine Learning (ML) enthusiast like
*2023-1-19 22:10:15
Author: [research.nccgroup.com(查看原文)](/jump-146242.htm)
阅读量:21
收藏*

---

Written by Jose Selvi and Thomas Atkinson

If you are a Machine Learning (ML) enthusiast like us, you may recall our blogpost series from 2019 regarding [Project Ava](https://research.nccgroup.com/2019/06/05/project-ava-on-the-matter-of-using-machine-learning-for-web-application-security-testing-part-1-understanding-the-basics-and-what-platforms-and-frameworks-are-available/), which documented our experiments in using ML techniques to automate web application security testing tasks. In February 2020 we set out to build on Project Ava with Project Bishop, which was to specifically look at use of ML techniques for intelligent web crawling. This research was performed by Thomas Atkinson, Matt Lewis and Jose Selvi.

In this blogpost we share some of the preliminary experiments that we performed under Project Bishop, and their results, which may be of interest and use to other researchers in this field.

The main question we sought to answer through our research was whether a ML model could be generated that would provide contextual understanding of different web pages and their functions (e.g., login page, generic web form submission, profile/image upload etc.). The reason for this focus was that we learned under Project Ava, that human-based interaction would first be needed to identify the role/function of a web page, before it could then initiate the appropriate ML-based web application security test (e.g., SQLi, XSS, file upload etc.). Intelligent crawling would minimise the requirement for human interaction and thus maximise the potential level of automation in ML-based web application security testing.

In order to obtain data for use in our experiments, we obtained the popular [Alexa Top 1K](https://github.com/urbanadventurer/WhatWeb/blob/master/plugin-development/alexa-top-1000.txt) (Note: this service has since been retired), which is a list of the most visited websites on the Internet. The initial plan was to obtain information about the main page of each of these websites and to classify them. However, this dataset included URLs, but not the nature or purpose of each one of those websites. For this reason, we decided to focus on finding a good representation of their content and using clustering techniques to find which websites looked most alike.

We created a python tool, which relied on Selenium to visit each one of the target websites and obtain the information that was used later to feed our ML models.

In particular, the following information was obtained:

* Source Code: We used the Selenium’s “page\_source” feature to obtain the source code of the websites. This was stored in a HTML file.

```
sauce = browser.page_source
```

* Screenshot: We used the Selenium’s “save\_screenshot” feature to obtain a screenshot of the website. This was stored in a PNG image.

```
selfie = browser.save_screenshot(name + ".png")
```

* Visual Page Segmentation (VIPS): We used [wushuartgaro’s](https://github.com/wushuartgaro/) python implementation of the Microsoft Visual Page Segmentation ([VIPS](https://github.com/wushuartgaro/VipsPython)) algorithm. This was stored in a JSON data structure, which includes information about how the HTML elements are displayed.

```
file = open("dom.js", 'r')
jscript = file.read()
jscript += '\nreturn JSON.stringify( toJSON( document.getElementsByTagName("BODY")[0] ) );'
jason = browser.execute_script(jscript)
```

The VIPS JSON format includes additional information such as the position and size of each one of the elements in the body, among other characteristics describing how each one of these elements were visualized when they were rendered. An example of this format can be observed bellow:

```
{
    "nodeType": 1,
    "tagName": "a",
    "visual_cues": {
        "bounds": {
            "x": 118,
            "y": 33,
            "width": 80.265625,
            "height": 11,
            "top": 33,
            "right": 198.265625,
            "bottom": 44,
            "left": 118
        },
        "font-size": "11px",
        "font-weight": "700",
        "background-color": "rgba(0, 0, 0, 0)",
        "display": "block",
        "visibility": "visible",
        "text": "Iscriviti a Prime",
        "className": "nav-sprite nav-logo-tagline nav-prime-try"
    },
```

Finally, we combined this output to create our initial dataset, based on the Alexa Top 1K information.

![](https://i0.wp.com/research.nccgroup.com/wp-content/uploads/2023/01/Picture1.png?resize=1024%2C643&ssl=1)

Figure 1 – Dataset including HTML, PNG and JSON files for each website

### Simple Feature Extraction with Unsupervised Convolutional Neural Network (CNN)

One of the re-occurring themes from our background research in Project Bishop was the use of CNNs for feature segmentation. This technique showed potential promise if applied to the screenshots of web pages that we had gathered previously. We experimented with CNNs, using the models developed by Asako Kanezaki presented in her 2018 paper “[Unsupervised image segmentation by backpropagation](https://kanezaki.github.io/pytorch-unsupervised-segmentation/ICASSP2018_kanezaki.pdf%29)”. This approach used a simple unsupervised CNN to automatically extract features from images. Kanezaki found good results when applying this technique to images with large objects like cars, bears, people etc. Some limitations were however observed regarding the style and imagery of some web pages. Below are examples of an input image and output result:

![](https://i0.wp.com/research.nccgroup.com/wp-content/uploads/2023/01/Picture2.png?resize=540%2C455&ssl=1)

Figure 2 – Input web page image

![](https://i0.wp.com/research.nccgroup.com/wp-content/uploads/2023/01/Picture3.png?resize=540%2C455&ssl=1)

Figure 3 – Difficulties with feature extraction on busy/dense backgrounds

As shown in Figure 3, the model focused mainly on large blocks of solid colours and many of the features and finer details required for browsing were lost. This example is a good one as the input data has a particularly busy background that a human can automatically recognise as a background image.

This experiment showed that a simplistic approach such as this focused on too high a level and was also not fit for extracting subtle yet important features.

### Manual Feature Extraction from JSON

We tried to manually extract several features from the information that we had (HTML, DOM, JSON, screenshot-png). From state of the art as seen from our Internet searches, we couldn’t find a reference of features that yielded good results when trying to solve similar problems. Most of the classification problems that we found were based on the textual information contained in the page, which can be used to determine if a page is related to a category such as sports, philosophy or technology. However, the problem we were trying to solve was far different and therefore, those techniques and features were not useful to our research.

As a first approach we focused on the DOM, since the HTML could not contain all the information necessary to represent the rendered page. In particular, the HTML content could not be enough to represent single-page applications, since the same HTML content could result in different rendered pages depending on further connections.

In our first experiment we used the following features extracted...