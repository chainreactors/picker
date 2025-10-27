---
title: NTLMRecon - A Tool For Performing Light Brute-Forcing Of HTTP Servers To Identify Commonly Accessible NTLM Authentication Endpoints
url: https://buaq.net/go-162159.html
source: unSafe.sh - 不安全
date: 2023-05-08
fetch_date: 2025-10-04T11:37:10.517063
---

# NTLMRecon - A Tool For Performing Light Brute-Forcing Of HTTP Servers To Identify Commonly Accessible NTLM Authentication Endpoints

* [unSafe.sh - СИЇт«ЅтЁе](https://unsafe.sh)
* [ТѕЉуџёТћХУЌЈ](/user/collects)
* [С╗іТЌЦуЃГТдю](/?hot=true)
* [тЁгС╝ЌтЈиТќЄуФа](/?gzh=true)
* [т»╝Уѕф](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [у╝ќуаЂ/УДБуаЂ](/encode)
* [ТќЄС╗ХС╝аУЙЊ](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
ж╗ЉтцюТеАт╝Ј

![](https://8aqnet.cdn.bcebos.com/a58473b893d4507cc0462bcafee9f546.jpg)

NTLMRecon - A Tool For Performing Light Brute-Forcing Of HTTP Servers To Identify Commonly Accessible NTLM Authentication Endpoints

NTLMRecon is a Golang version of the original NTLMRecon utility written by Sachin Kamath (AK
*2023-5-7 20:30:0
Author: [www.kitploit.com(ТЪЦуюІтјЪТќЄ)](/jump-162159.htm)
жўЁУ»╗жЄЈ:49
ТћХУЌЈ*

---

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEivsd-cOywWpCeIbA52yA5Pqqgfn8-8_rRyh3z5qe2P22T1bj_srgZk12taKTqrrelQKIOgtyvNevuSQABqSt8ZkcrSEdr4nlpn-A5_UMzbm5vQudReaDQKACYbZXcsmEpDvY1yMf_9hJUPfgjNXkoYXBiVQcV5i6fh1XU78wXV7eoc4lu2XYpJKRoPrA/w640-h264/Screen-Shot-2022-11-18-at-12.06.02-PM-768x317.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEivsd-cOywWpCeIbA52yA5Pqqgfn8-8_rRyh3z5qe2P22T1bj_srgZk12taKTqrrelQKIOgtyvNevuSQABqSt8ZkcrSEdr4nlpn-A5_UMzbm5vQudReaDQKACYbZXcsmEpDvY1yMf_9hJUPfgjNXkoYXBiVQcV5i6fh1XU78wXV7eoc4lu2XYpJKRoPrA/s768/Screen-Shot-2022-11-18-at-12.06.02-PM-768x317.png)

NTLMRecon is a Golang version of the original NTLMRecon utility written by Sachin Kamath (AKA pwnfoo). NTLMRecon can be leveraged to perform brute forcing against a targeted webserver to identify common application endpoints supporting NTLM authentication. This includes endpoints such as the Exchange Web Services endpoint which can often be leveraged to bypass multi-factor authentication.

The tool supports collecting metadata from the exposed NTLM [authentication](https://www.kitploit.com/search/label/Authentication "authentication") endpoints including information on the computer name, [Active Directory](https://www.kitploit.com/search/label/Active%20Directory "Active Directory") domain name, and Active Directory forest name. This information can be obtained without prior authentication by sending an NTLM NEGOTIATE\_MESSAGE packet to the server and examining the NTLM CHALLENGE\_MESSAGE returned by the targeted server. We have also published a blog post alongside this tool discussing some of the motiviations behind it's development and how we are approaching more advanced metadata collectoin within Chariot.

We wanted to perform brute-forcing and automated identification of exposed NTLM authentication endpoints within Chariot, our external attack surface management and continuous automated red teaming platform. Our primary backend scanning [infrastructure](https://www.kitploit.com/search/label/Infrastructure "infrastructure") is written in Golang and we didn't want to have to download and shell out to the NTLMRecon utility in Python to collect this information. We also wanted more control over the level of detail of the information we collected, etc.

The following command can be leveraged to install the NTLMRecon utility. Alternatively, you may download a precompiled version of the binary from the releases tab in GitHub.

The following command can be leveraged to invoke the NTLM recon utility and discover exposed NTLM authentication endpoints:

```
NTLMRecon -t https://autodiscover.contoso.com
```

The following command can be leveraged to invoke the NTLM recon utility and discover exposed NTLM endpoints while outputting collected metadata in a JSON format:

```
NTLMRecon -t https://autodiscover.contoso.com -o json
```

Below is an example JSON output with the data we collect from the NTLM CHALLENGE\_MESSAGE returned by the server:

```
{
```

```
Ръю  ~ NTLMRecon -t https://adfs.contoso.com -o json | jq
{
  "url": "https://adfs.contoso.com/adfs/services/trust/2005/windowstransport",
  "ntlm": {
    "netbiosComputerName": "MSFED1",
    "netbiosDomainName": "CONTOSO",
    "dnsDomainName": "corp.contoso.com",
    "dnsComputerName": "MSEXCH1.corp.contoso.com",
    "forestName": "contoso.com"
  }
}
Ръю  ~ NTLMRecon -t https://autodiscover.contoso.com
https://autodiscover.contoso.com/Autodiscover
https://autodiscover.contoso.com/Autodiscover/AutodiscoverService.svc/root
https://autodiscover.contoso.com/Autodiscover/Autodiscover.xml
https://autodiscover.contoso.com/EWS/
https://autodiscover.contoso.com/OAB/
https://autodiscover.contoso.com/Rpc/
Ръю  ~
```

Our methodology when developing this tool has targeted the most barebones version of the desired capability for the initial release. The goal for this project was to create an initial tool we could integrate into Chariot and then allow community contributions and feedback to drive additional tooling improvements or functionality. Below are some ideas for additional functionality which could be added to NTLMRecon:

* Concurrency and Performance Improvements: There could be some additional improvements to concurrency and performance. Currently, the tool sequentially makes HTTP requests and waits for the previous request to be performed.
* Batch Scanning Functionality: Another idea would be to extend the NTLMRecon utility to accept a list of hosts from standard input. One usage scenario for this could be an attacker running a combination of Рђюsubfinder | httpx | NTLMReconРђЮ to enumerate HTTP servers and then identify NTLM authentication endpoints that are exposed externally across an entire attack surface.
* One-off Data Collection Capability: A user may wish to perform one-off data collection targeting a specific endpoint which is currently not supported by NTLMRecon.
* User-Agent Randomization or Control: A user may wish to randomize the user-agents used to make requests. Alternatively when targeting Microsoft Exchange servers sometimes using a user-agent with a mobile client or legacy third-party email client can allow requests to the /EWS/Exchange.asmx endpoint through, etc.

[1] [https://www.praetorian.com/blog/automating-the-discovery-of-ntlm-authentication-endpoints/](https://www.praetorian.com/blog/automating-the-discovery-of-ntlm-authentication-endpoints/ "https://www.praetorian.com/blog/automating-the-discovery-of-ntlm-authentication-endpoints/")

NTLMRecon - A Tool For Performing Light Brute-Forcing Of HTTP Servers To Identify Commonly Accessible NTLM Authentication Endpoints
![NTLMRecon - A Tool For Performing Light Brute-Forcing Of HTTP Servers To Identify Commonly Accessible NTLM Authentication Endpoints](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEivsd-cOywWpCeIbA52yA5Pqqgfn8-8_rRyh3z5qe2P22T1bj_srgZk12taKTqrrelQKIOgtyvNevuSQABqSt8ZkcrSEdr4nlpn-A5_UMzbm5vQudReaDQKACYbZXcsmEpDvY1yMf_9hJUPfgjNXkoYXBiVQcV5i6fh1XU78wXV7eoc4lu2XYpJKRoPrA/s72-w640-c-h264/Screen-Shot-2022-11-18-at-12.06.02-PM-768x317.png)
Reviewed by Zion3R
on
8:30Рђ»AM
Rating: 5

ТќЄуФаТЮЦТ║љ: http://www.kitploit.com/2023/05/ntlmrecon-tool-for-performing-light.html
 тдѓТюЅСЙхТЮЃУ»иУЂћу│╗:admin#unsafe.sh

© [unSafe.sh - СИЇт«ЅтЁе](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [т«ЅтЁежЕгтЁІ](https://aq.mk)
* [ТўЪжЎЁж╗Љт«б](https://xj.hk)
* [T00ls](https://t00ls.net)