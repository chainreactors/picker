---
title: Detection of Vulnerabilities in JavaScript Libraries
url: https://buaq.net/go-145783.html
source: unSafe.sh - 不安全
date: 2023-01-17
fetch_date: 2025-10-04T04:02:06.521345
---

# Detection of Vulnerabilities in JavaScript Libraries

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

![](https://8aqnet.cdn.bcebos.com/0ad9e766acb87d7c01f3d1d4118e4420.jpg)

Detection of Vulnerabilities in JavaScript Libraries

JavaScript is a popular programming language which is an integral component while developing in
*2023-1-16 19:46:18
Author: [blog.qualys.com(查看原文)](/jump-145783.htm)
阅读量:27
收藏*

---

JavaScript is a popular programming language which is an integral component while developing interactive and dynamic web applications. It allows developers to create engaging and responsive user interfaces, handling complex web page elements, enhancing the overall functionality of the application. According to [W3Techs statistics](https://w3techs.com/technologies/details/cp-javascript), 98% of all the websites use JavaScript as client-side programming language.

To further simplify the web development process and make it efficient, Web developers frequently use JavaScript library, a collection of pre-written JavaScript codes that can be easily integrated with application projects. These libraries can provide a variety of benefits such as performance improvement, cross-browser compatibility and best practices to follow the latest development trends.

![Qualys WAS](https://ik.imagekit.io/qualys/wp-content/themes/qualys2020/image/app-icons/was.svg)

#### Free Trial

However, as the use of JavaScript libraries have grown over time, so have the potential security issues associated with it. Hence, it is imperative to manage and maintain these libraries. Some of the most common vulnerabilities associated with libraries are the Injection attacks such as Cross-site scripting (XSS) and SQL Injection.

[Qualys Web Application Scanning](https://www.qualys.com/apps/web-app-scanning/) offers a complete solution to keep track of JavaScript libraries used in a web application and detect known security vulnerabilities associated with it. Successful detection will help customers to manage libraries efficiently, further identify and remediate the issues with detailed vulnerability scan report.

## JavaScript Frameworks

[Qualys WAS](https://www.qualys.com/apps/web-app-scanning/) detects majority of the JavaScript libraries used widely by web applications. Listed below are a subset of some popular supported frameworks:

* AngularJS
* jQuery
* Lodash
* Moment.js
* React
* Vue.js

Customers can get more information regarding JavaScript libraries used in their web application using the following Information Gathering QIDs:

* 150176 – In-scope JavaScript Libraries Detected
* 150545 – JavaScript Library Loaded via External Server
* 150621 – List of JavaScript Links

## Detecting JavaScript Library Vulnerabilities with Qualys WAS

Until December 2022, all scans against the web applications would report JavaScript library vulnerabilities under QID 150162.

To improve reporting and management of the detections, the vulnerabilities in each library are reported in a dedicated QID.

List of new QIDs for Vulnerable libraries that have been supported thus far:

* 151000 Vulnerable JavaScript Library Detected – AngularJS
* 151001 Vulnerable JavaScript Library Detected – Backbone
* 151002 Vulnerable JavaScript Library Detected – Bootstrap
* 151003 Vulnerable JavaScript Library Detected – CKEditor
* 151005 Vulnerable JavaScript Library Detected – Coveo JS
* 151006 Vulnerable JavaScript Library Detected – Dojo
* 151007 Vulnerable JavaScript Library Detected – DOMPurify
* 151008 Vulnerable JavaScript Library Detected – DWR
* 151009 Vulnerable JavaScript Library Detected – easyXDM
* 151010 Vulnerable JavaScript Library Detected – Ember.js
* 151011 Vulnerable JavaScript Library Detected – Ext JS
* 151012 Vulnerable JavaScript Library Detected – flowplayer
* 151013 Vulnerable JavaScript Library Detected – Handlebars
* 151014 Vulnerable JavaScript Library Detected – jPlayer
* 151015 Vulnerable JavaScript Library Detected – jQuery
* 151016 Vulnerable JavaScript Library Detected – jQuery Migrate
* 151017 Vulnerable JavaScript Library Detected – jQuery Mobile
* 151018 Vulnerable JavaScript Library Detected – jQuery PrettyPhoto
* 151019 Vulnerable JavaScript Library Detected – jQuery UI
* 151022 Vulnerable JavaScript Library Detected – Knockout
* 151024 Vulnerable JavaScript Library Detected – Lodash
* 151025 Vulnerable JavaScript Library Detected – Moment.js
* 151026 Vulnerable JavaScript Library Detected – Mustache
* 151028 Vulnerable JavaScript Library Detected – Next.js
* 151029 Vulnerable JavaScript Library Detected – Plupload
* 151030 Vulnerable JavaScript Library Detected – Prototype
* 151031 Vulnerable JavaScript Library Detected – React
* 151034 Vulnerable JavaScript Library Detected – TinyMCE
* 151035 Vulnerable JavaScript Library Detected – URI.js
* 151037 Vulnerable JavaScript Library Detected – Vue.js
* 151038 Vulnerable JavaScript Library Detected – YUI

Below is an example to highlight detection of latest CVE vulnerabilities on an application running outdated **Moment.js** JavaScript library using its dedicated QID 151025:

[![](https://ik.imagekit.io/qualys/wp-content/uploads/2023/01/momentkb.jpg)](https://ik.imagekit.io/qualys/wp-content/uploads/2023/01/momentkb.jpg)

QID 151025: Vulnerable JavaScript Library Detected – Moment.js

Once the QID is successfully detected by Qualys WAS, the user shall see CVE-2022-24785 and CVE-2022-31129 vulnerability details including its solution flagged in the vulnerability scan report, as shown here:

[![](https://ik.imagekit.io/qualys/wp-content/uploads/2023/01/momentreport.jpg)](https://ik.imagekit.io/qualys/wp-content/uploads/2023/01/momentreport.jpg)

## Solution

Customers are advised to upgrade to the latest version of the respective JavaScript Library to ensure they are up-to-date and secure.

In the vulnerability scan report users will have access to detailed vulnerability information along with their remediation guidelines as provided by the vendor.

Refer to the following blog for additional information regarding JavaScript libraries in the scanned web application: <https://blog.qualys.com/qualys-insights/2022/10/12/creating-awareness-of-external-javascript-libraries-in-web-applications>

## Contributors

**Sheela Sarva**, Director, Quality Engineering, Web Application Security, Qualys

![Qualys WAS](https://ik.imagekit.io/qualys/wp-content/themes/qualys2020/image/app-icons/was.svg)

#### Free Trial

文章来源: https://blog.qualys.com/vulnerabilities-threat-research/2023/01/16/detection-of-vulnerabilities-in-javascript-libraries
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)