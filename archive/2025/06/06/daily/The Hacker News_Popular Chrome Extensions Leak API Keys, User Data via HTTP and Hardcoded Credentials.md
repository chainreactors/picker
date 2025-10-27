---
title: Popular Chrome Extensions Leak API Keys, User Data via HTTP and Hardcoded Credentials
url: https://thehackernews.com/2025/06/popular-chrome-extensions-leak-api-keys.html
source: The Hacker News
date: 2025-06-06
fetch_date: 2025-10-06T22:55:34.953758
---

# Popular Chrome Extensions Leak API Keys, User Data via HTTP and Hardcoded Credentials

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [Popular Chrome Extensions Leak API Keys, User Data via HTTP and Hard-Coded Credentials](https://thehackernews.com/2025/06/popular-chrome-extensions-leak-api-keys.html)

**Jun 05, 2025**Ravie LakshmananBrowser Security / Online Safety

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhURELDep_-JUFaGtyLdoOwugLgIVDRs5RS7QzTdGwyW03bSgXhlp1EPoNYwR7V2lDW3YAr7oPH74HwivaC5uKqjf7YiIzWVGZzNua8K2ayFKY51ox84s9YlkUJ8tQIDQK1L4Y14lLRelaOLsxJ-DD86VsTIu03evrTvfEJf3BlRRSXfeDB4x_cxXjEqZQ/s790-rw-e365/1000108456.jpg)

Cybersecurity researchers have flagged several popular Google Chrome extensions that have been found to transmit data in HTTP and hard-code secrets in their code, exposing users to privacy and security risks.

"Several widely used extensions [...] unintentionally transmit sensitive data over simple HTTP," Yuanjing Guo, a security researcher in the Symantec's Security Technology and Response team, [said](https://www.security.com/threat-intelligence/chrome-extension-leaks). "By doing so, they expose browsing domains, machine IDs, operating system details, usage analytics, and even uninstall information, in plaintext."

The fact that the network traffic is unencrypted also means that they are susceptible to adversary-in-the-middle (AitM) attacks, allowing malicious actors on the same network such as a public Wi-Fi to intercept and, even worse, modify this data, which could lead to far more serious consequences.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The list of identified extensions are below -

* **SEMRush Rank** (extension ID: idbhoeaiokcojcgappfigpifhpkjgmab) and PI Rank (ID: ccgdboldgdlngcgfdolahmiilojmfndl), which call the URL "rank.trellian[.]com" over plain HTTP
* Browsec VPN (ID: omghfjlpggmjjaagoclmmobgdodcjboh), which uses HTTP to call an uninstall URL at "browsec-uninstall.s3-website.eu-central-1.amazonaws[.]com" when a user attempts to uninstall the extension
* **MSN New Tab** (ID: lklfbkdigihjaaeamncibechhgalldgl) and MSN Homepage, Bing Search & News (ID: midiombanaceofjhodpdibeppmnamfcj), which transmit a unique machine identifier and other details over HTTP to "g.ceipmsn[.]com"
* **DualSafe Password Manager & Digital Vault** (ID: lgbjhdkjmpgjgcbcdlhkokkckpjmedgc), which constructs an HTTP-based URL request to "stats.itopupdate[.]com" along with information about the extension version, user's browser language, and usage "type"

"Although credentials or passwords do not appear to be leaked, the fact that a password manager uses unencrypted requests for telemetry erodes trust in its overall security posture," Guo said.

Symantec said it also [identified](https://www.security.com/threat-intelligence/chrome-extension-credentials) another set of extensions with API keys, secrets, and tokens directly embedded in the JavaScript code, which an attacker could weaponize to craft malicious requests and carry out various malicious actions -

* **Online Security & Privacy extension** (ID: gomekmidlodglbbmalcneegieacbdmki), AVG Online Security (ID: nbmoafcmbajniiapeidgficgifbfmjfo), Speed Dial [FVD] - New Tab Page, 3D, Sync (ID: llaficoajjainaijghjlofdfmbjpebpa), and SellerSprite - Amazon Research Tool (ID: lnbmbgocenenhhhdojdielgnmeflbnfb), which expose a hard-coded Google Analytics 4 (GA4) API secret that an attacker could use to bombard the GA4 endpoint and corrupt metrics
* **Equatio – Math Made Digital** (ID: hjngolefdpdnooamgdldlkjgmdcmcjnc), which embeds a Microsoft Azure API key used for speech recognition that an attacker could use to inflate the developer's costs or exhaust their usage limits
* **Awesome Screen Recorder & Screenshot** (ID: nlipoenfbbikpbjkfpfillcgkoblgpmj) and Scrolling Screenshot Tool & Screen Capture (ID: mfpiaehgjbbfednooihadalhehabhcjo), which expose the developer's Amazon Web Services (AWS) access key used to upload screenshots to the developer's S3 bucket
* **Microsoft Editor – Spelling & Grammar Checker** (ID: gpaiobkfhnonedkhhfjpmhdalgeoebfa), which exposes a telemetry key named "StatsApiKey" to log user data for analytics
* **Antidote Connector** (ID: lmbopdiikkamfphhgcckcjhojnokgfeo), which incorporates a third-party library called InboxSDK that contains hard-coded credentials, including API keys.
* **Watch2Gether** (ID: cimpffimgeipdhnhjohpbehjkcdpjolg), which exposes a Tenor GIF search API key
* **Trust Wallet** (ID: egjidjbpglichdcondbcbdnbeeppgdph), which exposes an API key associated with the Ramp Network, a Web3 platform that offers wallet developers a way to let users buy or sell crypto directly from the app
* **TravelArrow** – Your Virtual Travel Agent (ID: coplmfnphahpcknbchcehdikbdieognn), which exposes a geolocation API key when making queries to "ip-api[.]com"

Attackers who end up finding these keys could weaponize them to drive up API costs, host illegal content, send spoofed telemetry data, and mimic cryptocurrency transaction orders, some of which could see the developer's ban getting banned.

Adding to the concern, Antidote Connector is just one of over 90 extensions that use InboxSDK, meaning the other extensions are susceptible to the same problem. The names of the other extensions were not disclosed by Symantec.

Equatio, in a statement shared with The Hacker News, said the Azure API key in question is scoped, rate-limited, and capped at a small USD-value per/month, affecting only the developer.

"This risk was logged in our ISO27001 risk-register at the time of development, and marked as "accepted" given the limited scope," Ryan Graham, chief technology officer at Everway, said. "The feature is used by just 6 users out of 670,000 (in the last 90 days). No user data is exposed or stored, and the function is solely used by the Microsoft Edge version of the extension."

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Trust Wallet also confirmed with the publication that the API key referenced is used only for non-sensitive quote requests...