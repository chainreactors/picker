---
title: Police Body Camera Apps Sending Data to Cloud Servers Hosted in China Via TLS Port 9091
url: https://cybersecuritynews.com/police-body-camera-apps-sending-data-to-cloud-servers/
source: Instapaper: Unread
date: 2025-09-11
fetch_date: 2025-10-02T19:59:54.248518
---

# Police Body Camera Apps Sending Data to Cloud Servers Hosted in China Via TLS Port 9091

[Linkedin](https://www.linkedin.com/company/cybersecurity-news/ "Linkedin")

[Naver](https://news.google.com/publications/CAAqMggKIixDQklTR3dnTWFoY0tGV041WW1WeWMyVmpkWEpwZEhsdVpYZHpMbU52YlNnQVAB?hl=en-IN&gl=IN&ceid=IN:en "Naver")

[RSS](https://cybersecuritynews.com/feed/ "RSS")

[Twitter](https://twitter.com/The_Cyber_News "Twitter")

* [Home](https://cybersecuritynews.com/)
* [Threats](https://cybersecuritynews.com/category/threats/)
* [Cyber Attacks](https://cybersecuritynews.com/category/cyber-attack/)
* [Vulnerabilities](https://cybersecuritynews.com/category/vulnerability/)
* [Breaches](https://cybersecuritynews.com/category/data-breaches/)
* [Top 10](https://cybersecuritynews.com/category/top-10/)

Search

[![Cyber Security News](https://cybersecuritynews.com/wp-content/uploads/2025/05/Cyber-Security-News-Logo.webp "Cyber Security News")Cyber Security NewsLatest Cyber Security News](https://cybersecuritynews.com/ "Cyber Security News")

Thursday, October 2, 2025

[Linkedin](https://www.linkedin.com/company/cybersecurity-news/ "Linkedin")

[RSS](https://cybersecuritynews.com/feed/ "RSS")

[Twitter](https://x.com/The_Cyber_News "Twitter")

[Google News](https://news.google.com/publications/CAAqMggKIixDQklTR3dnTWFoY0tGV041WW1WeWMyVmpkWEpwZEhsdVpYZHpMbU52YlNnQVAB?hl=en-IN&gl=IN&ceid=IN:en "Google News")[Google News](https://news.google.com/publications/CAAqMggKIixDQklTR3dnTWFoY0tGV041WW1WeWMyVmpkWEpwZEhsdVpYZHpMbU52YlNnQVAB?hl=en-IN&gl=IN&ceid=IN:en)

[![Cyber Security News](https://cybersecuritynews.com/wp-content/uploads/2025/05/Cyber-Security-News-Logo.webp "Cyber Security News")Cyber Security NewsLatest Cyber Security News](https://cybersecuritynews.com/ "Cyber Security News")

* [Home](https://cybersecuritynews.com/)
* [Threats](https://cybersecuritynews.com/category/threats/)
* [Cyber Attacks](https://cybersecuritynews.com/category/cyber-attack/)
* [Vulnerabilities](https://cybersecuritynews.com/category/vulnerability/)
* [Breaches](https://cybersecuritynews.com/category/data-breaches/)
* [Top 10](https://cybersecuritynews.com/category/top-10/)

[Follow on LinkedIn](https://www.linkedin.com/company/cybersecurity-news/ "Follow on LinkedIn")

Search

[Home](https://cybersecuritynews.com/)  [Cyber Security News](https://cybersecuritynews.com/category/cyber-security-news/ "View all posts in Cyber Security News")  Police Body Camera Apps Sending Data to Cloud Servers Hosted in China...

* [Cyber Security News](https://cybersecuritynews.com/category/cyber-security-news/)
* [Threats](https://cybersecuritynews.com/category/threats/)

# Police Body Camera Apps Sending Data to Cloud Servers Hosted in China Via TLS Port 9091

By

[Tushar Subhra Dutta](https://cybersecuritynews.com/author/tushar/)

-

September 9, 2025

[![Police Body Camera Apps Sending Data to Cloud Servers Hosted in China Via TLS Port 9091](https://i3.wp.com/blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhkqURhNNle8TyoLLHo_Q5W3HMP3qWUFDnDUFh7uKYu0_KFMacnFlbOpPvd8YSK0wr4nCUI1hWF9QJtdTZ8lwgkcdoB3avoaoXEAG_STbkqBFSroktHykcCc_wj7-C7zP3-uY8eT9c1DwY9EBVB3oCnPdU0ZgjhjIjvKljWxlurTeJBft_6fJK1HOGi3yQ/s16000/Police%20Body%20Camera%20Apps%20Sending%20Data%20to%20Cloud%20Servers%20Hosted%20in%20China%20Via%20TLS%20Port%209091.webp?w=696&resize=696,0&ssl=1)](https://i3.wp.com/blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhkqURhNNle8TyoLLHo_Q5W3HMP3qWUFDnDUFh7uKYu0_KFMacnFlbOpPvd8YSK0wr4nCUI1hWF9QJtdTZ8lwgkcdoB3avoaoXEAG_STbkqBFSroktHykcCc_wj7-C7zP3-uY8eT9c1DwY9EBVB3oCnPdU0ZgjhjIjvKljWxlurTeJBft_6fJK1HOGi3yQ/s16000/Police%20Body%20Camera%20Apps%20Sending%20Data%20to%20Cloud%20Servers%20Hosted%20in%20China%20Via%20TLS%20Port%209091.webp?w=1600&resize=1600,900&ssl=1)

Police-issued body cameras have become ubiquitous tools for recording law enforcement encounters, yet a recent investigation has uncovered troubling design choices in a budget-friendly system that compromise both privacy and data integrity.

The Viidure mobile application, designed to transfer video evidence from the camera’s onboard Wi-Fi hotspot to cloud servers, was found to communicate over a nonstandard TLS port, directing sensitive information to servers based in China.

This behavior raises significant concerns for departments relying on these devices to produce court-admissible evidence.

Initial traffic captures revealed that the mobile app establishes TLS connections to `app-api.lufengzhe.com:9091`, alongside geolocation API calls to `api.map.baidu.com:443` and `loc.map.baidu.com:443`.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEipmC2jtPWH-t5zhUBKGskrfy4yDkwTFsDenQWUGQvC43vvlNDTbK1t-OYQzmNqI2AAmO5x2OQD1bOO6djX8Pg0IBXHLhUjo8taZD7CqMX1CqZbRyGDbpKLbNoIKl9cRe5zO3cVNevzR0Ol9M1KpCg_tqSPgU_srjJm438ev_WDpYedk2XcISrC5L6mQ2A/s16000/Camera%20(Source%20-%20Brown%20Fine%20Security).webp)

Camera (Source – Brown Fine Security)

Whois queries confirmed that the primary endpoint at 115.175.147.124 is owned by Huawei International Pte. Ltd. and originates from a Chinese network block.

The use of port 9091—uncommon for HTTPS traffic—signals an attempt to obscure routine data flows, potentially evading network-based [monitoring tools](https://cybersecuritynews.com/postgresql-monitoring-tools/).

[![google](https://thecybernews.com/csngoogle.svg
)](https://www.google.com/preferences/source?q=cybersecuritynews.com)

Brown Fine Security analysts [noted](https://brownfinesecurity.com/blog/police-bodycam-data-to-china) that the app’s reliance on improperly validated server certificates enabled a straightforward man-in-the-middle (MitM) attack.

By injecting forged certificates via a custom mitmrouter setup, researchers were able to intercept plaintext HTTP exchanges within the TLS tunnel.

Such misconfigurations not only expose metadata like IMEI numbers and usernames but also threaten the confidentiality of recorded video streams.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiIP8e-rFDMrWNlWb_Boj2kSwjGPmSZqS9nfgrIFyKV15dfcu23YqLcW_h51QoCeuRtH0fzqMR9SyBrWlq1xjBrIyboeGJ-VcixM4dzK9n7gxQl5Og6pABSbmsr26-85fioMlN84qehdzR0ubDHEJCmBjoDAiYAI0WYAAxUqFlT0g7t_gvA_GfH2XCPNTY/s16000/Mitmrouter%20diagram%20(Source%20-%20Brown%20Fine%20Security).webp)

Beyond mere metadata, the intercepted payloads include device identifiers and application version details.

The following snippet illustrates the HTTP POST request captured during the MitM session:-

```
POST /iot/api/v1/version/check HTTP/1.1
Host: app-api.lufengzhe.com:9091
Content-Type: application/json
srapi_imei: 17562212185897060
srapi_time: 1757047550015

{
  "data": [
    {
      "model": "6zhentan_android",
      "version": "v2.7.1.250712",
      "imei": "17562212185897060"
    }
  ],
  "username": "<redacted>"
}
```

## **Infection Mechanism and Data Exfiltration**

The Viidure application does not self-install malware but functions as an inadvertent [exfiltration](https://cybersecuritynews.com/cl0p-ransomware-data-exfiltration-vulnerable/) vector due to its insecure communications design.

Upon pairing with the camera’s hotspot, the app automatically initiates background data uploads without user notification.

TLS connections to the Chinese endpoint are established immediately, transmitting identifying information alongside any captured media metadata.

The use of port 9091 appears deliberate, likely to bypass conventional TLS inspection rules that focus on ports 443 and 8443.

Persistence of this behavior stems from the application’s versioning system. Every time the app checks for updates—triggered at startup and periodically during use—it reaffirms the connection to the malicious endpoint.

Without rigorous certificate validation or user consent dialogs, departmental networks may remain unaware of routine data streams exiting to unauthorized servers.

Security teams should prioritize [network segmentation](https://cybersecuritynews.com/network-security-compliance-checklist/) and deep packet inspection rules that include nonstandard ports to detect and d...