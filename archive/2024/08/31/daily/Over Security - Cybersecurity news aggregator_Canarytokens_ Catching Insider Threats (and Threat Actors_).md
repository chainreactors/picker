---
title: Canarytokens: Catching Insider Threats (and Threat Actors?)
url: https://dfir.ch/posts/canarytokens/
source: Over Security - Cybersecurity news aggregator
date: 2024-08-31
fetch_date: 2025-10-06T18:08:07.574497
---

# Canarytokens: Catching Insider Threats (and Threat Actors?)

[Home](https://dfir.ch/)
[ ]

Menu

* [Home](/)
* [Posts](/posts/)
* [Talks](/talks/)
* [Tweets](/tweets/)
* |

LIGHT

DARK

# Canarytokens: Catching Insider Threats (and Threat Actors?)

6 May 2024

**Table of Contents**

* [Insider Threat?](#insider-threat)
* [Let me introduce you Canarytokens](#let-me-introduce-you-canarytokens)
* [Excel Canarytoken](#excel-canarytoken)
* [Another story - Elevate Kit from CobaltStrike](#another-story---elevate-kit-from-cobaltstrike)
* [But why?](#but-why)
* [Conclusion](#conclusion)
* [Bottom line](#bottom-line)

## Insider Threat?

We were contacted by a company that regularly sends emails to customers promoting new services and discounts. An Excel is uploaded to a web server, where a job processes the file to create an email per customer, taking the email addresses from the uploaded Excel file.

For a significant period of time, the company has been struggling with a serious issue - its competitors are reaching out to the same customers they intend to contact in the upcoming mailing, often a day or two earlier. This is not an isolated incident. Every customer listed in the Excel sheet for the forthcoming mailing has been contacted earlier by competitors (in plural), posing a significant threat to our customer base.

The customer asked us for advice on finding out whether they face an insider threat selling their data to the competitors or whether the external web server had been hacked (and the newest Excel file is leaking from a web vulnerability or another badly secured access on the webserver).

## Let me introduce you Canarytokens

Canarytokens are decoys that mimic a digital resource on endpoints, servers, or networks to serve as early warning indicators of a security breach or unauthorized access. They are named after canaries used in coal mines to detect toxic gases, where the canary’s death served as a warning sign for the miners to evacuate.

In cybersecurity, canarytokens work similarly by generating alerts when they are triggered. They are designed to look like enticing targets for attackers, such as documents, URLs, email addresses, or other digital assets. When an attacker interacts with or accesses a canarytoken, it triggers an alert, providing defenders with valuable information about potential threats.

Canarytokens come in various forms, including:

* File tokens: Files that, when opened, trigger an alert.
* URL tokens: Unique URLs that, when visited, trigger an alert.
* DNS tokens: Unique DNS records that, when looked up, trigger an alert.
* Email tokens: Email addresses that, when sent a message to, trigger an alert.
* Web bug tokens: Small images or code snippets embedded in web pages or emails that trigger an alert when loaded.
* Sensitive Command Token: This token creates a registry key and sends an alert to you in near real-time that the command of interest has been executed.

One can easily generate a new canarytoken [here](https://canarytokens.org/generate). Figure 1 depicts a subset of the possible token types for a new canarytoken (or configuration).

![Creating a new canarytoken](/images/canary/canarytokens.png "Creating a new canarytoken")

Figure 1: Creating a new canarytoken

For further insights into canarytokens, watch the BlueHat talk [Building a Canarytoken to Monitor Windows Process Execution](https://www.youtube.com/watch?v=iWV6r2YjmTY).

## Excel Canarytoken

Returning to our insider threat or compromised web server case, we planned to generate an Excel canarytoken document, which we will pass on to our client. The client could hand it over to various people in the organization they suspect of wrongdoing or simply upload it to the web server as a preparation for the upcoming emailing to the customers.

![Create a Canarytoken](/images/canary/create_canary.png "Create a Canarytoken")

Figure 2: Create a new Canarytoken Excel file

Creating a new document is trivial, and we can now download our canarytoken document (with the filename hkkmt4dgsx7dm150bffdjhx3s.xlsx).

![Create a Canarytoken](/images/canary/excel_token.png "Create a Canarytoken")

Figure 3: Newly created MS Excel file with a canarytoken inside

The next step, as a test, is to upload our canarytoken Excel file to an [online Excel parsing platform](https://products.conholdate.app/parser/excel). Keep in mind that we uploaded the document to this parser platform for the sake of demonstration. It does not really matter in this case if we open the document on our computer or upload it to such an online parser - we must simulate the opening of the document, check whether the alerting mechanisms (the “canarytoken”) is triggered, and see what the outcome will look like.

![Create a Canarytoken](/images/canary/excel_parser.png "Create a Canarytoken")

Figure 4: Online Excel Parser

And yes, uploading our document to the Excel parsing platform indeed parsed our canarytoken file. A few minutes later, we received a message in our mailbox that someone had opened the document (Figure 5).

![Create a Canarytoken](/images/canary/canarytoken_triggered.png "Create a Canarytoken")

Figure 5: An MS Excel Canarytoken has been triggered

How does that work? XLSX files are the default format for Excel files created in versions of Excel starting from Excel 2007. They are based on the Open XML standard and are essentially a collection of XML files compressed into a ZIP archive:

```
% file hkkmt4dgsx7dm150bffdjhx3s.xlsx
hkkmt4dgsx7dm150bffdjhx3s.xlsx: Microsoft OOXML
```

And we can unzip our document:

```
% unzip hkkmt4dgsx7dm150bffdjhx3s.xlsx
Archive:  hkkmt4dgsx7dm150bffdjhx3s.xlsx
  inflating: [Content_Types].xml
  inflating: _rels/.rels
  inflating: docProps/app.xml
  inflating: docProps/core.xml
  inflating: xl/workbook.xml
  inflating: xl/worksheets/sheet1.xml
  inflating: xl/worksheets/_rels/sheet1.xml.rels
  inflating: xl/drawings/drawing1.xml
  inflating: xl/drawings/_rels/drawing1.xml.rels
  inflating: xl/styles.xml
  inflating: xl/theme/theme1.xml
  inflating: xl/_rels/workbook.xml.rels
```

Looking inside the file \_./xl/drawings/*rels/drawing1.xml.rels*:

```
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image"
Target="http://canarytokens.com/static/hkkmt4dgsx7<redacted>/index.html"
TargetMode="External"/></Relationships>
```

We see a reference to an external image, which is an HTML webpage. It’s not strictly necessary to open the Excel file, the loading of this website alone triggers the canarytoken, which brings another email to our inbox. Equipped with such a document, the customer will find out from which IP address the document is openedâproofing whether the data is indeed stolen or leaked (or not).

## Another story - Elevate Kit from CobaltStrike

The power of canarytokens can also be told in another story: In an investigation last year, we found out that the threat actors executed the elevate command from CobaltStrike to raise the privileges on the beachhead (or at least tried to raise the privileges). The following command (with the corresponding output) was recorded inside the Cobalt Strike logs:

```
elevate uac-schtasks
Tasked Beacon to run windows/beacon_https/reverse_https
(<redacted>) in a high integrity context
```

The elevate command is part of the [ElevateKit](https://github.com/cobalt-strike/ElevateKit) from CobaltStrike: *The Elevate Kit demonstrates how to use third-party privilege escalation attacks with Cobalt Strike’s Beacon payload.* The parameter *uac-schtaks*, passed to the elevate command, runs the Invoke-EnvBypass function from the EmpireProject.

Loading this module on my test machine with activated Defender flags the code immediately as malicious (disable the local antivirus for testing this specific UAC bypass). When I later opened my mailbox, I was surprised to find that a canary token had been t...