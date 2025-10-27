---
title: ReconAIzer - A Burp Suite Extension To Add OpenAI (GPT) On Burp And Help You With Your Bug Bounty Recon To Discover Endpoints, Params, URLs, Subdomains And More!
url: https://buaq.net/go-170736.html
source: unSafe.sh - 不安全
date: 2023-06-29
fetch_date: 2025-10-04T11:46:39.156549
---

# ReconAIzer - A Burp Suite Extension To Add OpenAI (GPT) On Burp And Help You With Your Bug Bounty Recon To Discover Endpoints, Params, URLs, Subdomains And More!

* [unSafe.sh - õĖŹÕ«ēÕģ©](https://unsafe.sh)
* [µłæńÜäµöČĶŚÅ](/user/collects)
* [õ╗ŖµŚźńāŁµ”£](/?hot=true)
* [Õģ¼õ╝ŚÕÅĘµ¢ćń½Ā](/?gzh=true)
* [Õ»╝Ķł¬](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [ń╝¢ńĀü/Ķ¦ŻńĀü](/encode)
* [µ¢ćõ╗Čõ╝ĀĶŠō](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
ķ╗æÕż£µ©ĪÕ╝Å

![](https://8aqnet.cdn.bcebos.com/08cb6199120a196b28ff62cdee45c03f.jpg)

ReconAIzer - A Burp Suite Extension To Add OpenAI (GPT) On Burp And Help You With Your Bug Bounty Recon To Discover Endpoints, Params, URLs, Subdomains And More!

ReconAIzer is a powerful Jython extension for Burp Suite that leverages OpenAI to help bug b
*2023-6-28 20:30:0
Author: [www.kitploit.com(µ¤źń£ŗÕÄ¤µ¢ć)](/jump-170736.htm)
ķśģĶ»╗ķćÅ:39
µöČĶŚÅ*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEg6fLW5PV92hF9ti7T7QqwxUenYq2OtnARg68xncqcZJdHlfA1kADFnCDZklpYBHqrsEZyO2HF60XUJv1nWxFrq-4Sdfq3nbfMSv1gW_hnUPVWnOxXmD0RPjaYsEAMWMeraEsIBDUhpc6oMooRTNT8ofpDkt89jyMMD2eEva6z5ueBE8PaY_aULJuBX8A=w640-h138)](https://blogger.googleusercontent.com/img/a/AVvXsEg6fLW5PV92hF9ti7T7QqwxUenYq2OtnARg68xncqcZJdHlfA1kADFnCDZklpYBHqrsEZyO2HF60XUJv1nWxFrq-4Sdfq3nbfMSv1gW_hnUPVWnOxXmD0RPjaYsEAMWMeraEsIBDUhpc6oMooRTNT8ofpDkt89jyMMD2eEva6z5ueBE8PaY_aULJuBX8A)

ReconAIzer is a powerful Jython extension for [Burp Suite](https://www.kitploit.com/search/label/Burp%20Suite "Burp Suite") that leverages OpenAI to help bug bounty hunters optimize their [recon](https://www.kitploit.com/search/label/Recon "recon") process. This extension automates various tasks, making it easier and faster for security researchers to identify and exploit vulnerabilities.

Once installed, ReconAIzer add a contextual menu and a dedicated tab to see the results:

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgKSXeNltL-5qjGI0e2zfN6H9i_KldGdyoY01Nq8XOJuTkoMkU7pxAo29uaoSSALbS9Q9f--3t6Wn5MnEElzS-SgNM7Ib_tcrOgkQMjJMcFRCxBMVfiBwdWLXVdWiplrAPiB5gxy-Lb5iD3ixl6MevWKkQSTsylBGiuguebnMlR9HbKp7TlFXM9WjWLrA=w640-h390)](https://blogger.googleusercontent.com/img/a/AVvXsEgKSXeNltL-5qjGI0e2zfN6H9i_KldGdyoY01Nq8XOJuTkoMkU7pxAo29uaoSSALbS9Q9f--3t6Wn5MnEElzS-SgNM7Ib_tcrOgkQMjJMcFRCxBMVfiBwdWLXVdWiplrAPiB5gxy-Lb5iD3ixl6MevWKkQSTsylBGiuguebnMlR9HbKp7TlFXM9WjWLrA)

## Prerequisites

* Burp Suite
* Jython Standalone Jar

## Installation

Follow these steps to install the ReconAIzer extension on [Burp](https://www.kitploit.com/search/label/Burp "Burp") Suite:

### Step 1: Download Jython

1. Download the latest Jython Standalone Jar from the official website: [https://www.jython.org/download](https://www.jython.org/download "https://www.jython.org/download")
2. Save the Jython Standalone Jar file in a convenient location on your computer.

### Step 2: Configure Jython in Burp Suite

1. Open Burp Suite.
2. Go to the "Extensions" tab.
3. Click on the "Extensions settings" sub-tab.
4. Under "Python Environment," click on the "Select file..." button next to "Location of the Jython standalone [JAR](https://www.kitploit.com/search/label/JAR "JAR") file."
5. Browse to the location where you saved the Jython Standalone Jar file in Step 1 and select it.
6. Wait for the "Python Environment" status to change to "Jython (version x.x.x) successfully loaded," where x.x.x represents the Jython version.

### Step 3: Download and Install ReconAIzer

1. Download the [latest release of ReconAIzer](https://github.com/hisxo/ReconAIzer/releases "latest release of ReconAIzer")
2. Open Burp Suite
3. Go back to the "Extensions" tab in Burp Suite.
4. Click the "Add" button.
5. In the "Add extension" dialog, select "Python" as the "Extension type."
6. Click on the "Select file..." button next to "Extension file" and browse to the location where you saved the `ReconAIzer.py` file in Step 3.1. Select the file and click "Open."
7. Make sure the "Load" checkbox is selected and click the "Next" button.
8. Wait for the extension to be loaded. You should see a message in the "Output" section stating that the ReconAIzer extension has been successfully loaded.

Congratulations! You have successfully installed the ReconAIzer extension in Burp Suite. You can now start using it to enhance your bug bounty hunting experience.

Once it's done, you must configure your OpenAI API key on the "Config" tab under "ReconAIzer" tab.

* *Your OpenAI API key can be found here: [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys "https://platform.openai.com/account/api-keys").*

**Feel free to suggest prompts improvements or anything you would like to see on ReconAIzer!**

Happy bug hunting!

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhYeshTiEPmtbhDAKqWf219mx9z_fsqioJpIrAQC-4Ks4cx2LSfdyKRQwI8NuQHNnxsTEos3VNAkie8HMFvPJldK8i0ZXymtfJrMd1tXDi2DwUDxQLT4rjIq969iiwBQ-W-Z6PJ8ZKeJZopmmsP1qVRNjcbQAypbkxSkkW7udrc9AgSlygekG9fno4BCg=w640-h298)](https://blogger.googleusercontent.com/img/a/AVvXsEhYeshTiEPmtbhDAKqWf219mx9z_fsqioJpIrAQC-4Ks4cx2LSfdyKRQwI8NuQHNnxsTEos3VNAkie8HMFvPJldK8i0ZXymtfJrMd1tXDi2DwUDxQLT4rjIq969iiwBQ-W-Z6PJ8ZKeJZopmmsP1qVRNjcbQAypbkxSkkW7udrc9AgSlygekG9fno4BCg)

ReconAIzer - A Burp Suite Extension To Add OpenAI (GPT) On Burp And Help You With Your Bug Bounty Recon To Discover Endpoints, Params, URLs, Subdomains And More!
![ReconAIzer - A Burp Suite Extension To Add OpenAI (GPT) On Burp And Help You With Your Bug Bounty Recon To Discover Endpoints, Params, URLs, Subdomains And More!](https://blogger.googleusercontent.com/img/a/AVvXsEg6fLW5PV92hF9ti7T7QqwxUenYq2OtnARg68xncqcZJdHlfA1kADFnCDZklpYBHqrsEZyO2HF60XUJv1nWxFrq-4Sdfq3nbfMSv1gW_hnUPVWnOxXmD0RPjaYsEAMWMeraEsIBDUhpc6oMooRTNT8ofpDkt89jyMMD2eEva6z5ueBE8PaY_aULJuBX8A=s72-w640-c-h138)
Reviewed by Zion3R
on
8:30ŌĆ»AM
Rating: 5

µ¢ćń½ĀµØźµ║É: http://www.kitploit.com/2023/06/reconaizer-burp-suite-extension-to-add.html
 Õ”éµ£ēõŠĄµØāĶ»ĘĶüöń│╗:admin#unsafe.sh

© [unSafe.sh - õĖŹÕ«ēÕģ©](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [Õ«ēÕģ©ķ®¼Õģŗ](https://aq.mk)
* [µś¤ķÖģķ╗æÕ«ó](https://xj.hk)
* [T00ls](https://t00ls.net)