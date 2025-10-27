---
title: Microsoft resolves four SSRF vulnerabilities in Azure cloud services
url: https://buaq.net/go-145959.html
source: unSafe.sh - 不安全
date: 2023-01-18
fetch_date: 2025-10-04T04:07:26.348332
---

# Microsoft resolves four SSRF vulnerabilities in Azure cloud services

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

Microsoft resolves four SSRF vulnerabilities in Azure cloud services

Summary Microsoft recently fixed a set of Server-Side Request For
*2023-1-17 22:0:0
Author: [msrc-blog.microsoft.com(查看原文)](/jump-145959.htm)
阅读量:16
收藏*

---

## Summary

Microsoft recently fixed a set of Server-Side Request Forgery (SSRF) vulnerabilities in four Azure services (Azure API Management, Azure Functions, Azure Machine Learning, and Azure Digital Twins) reported by Orca Security. These SSRF vulnerabilities were determined to be low risk as they do not allow access to sensitive information or Azure backend services. Once these SSRF vulnerabilities were reported, Microsoft quickly took the necessary steps to resolve each vulnerability  by implementing additional input validation for the vulnerable URLs.  Microsoft also conducted a thorough investigation and determined that these SSRF vulnerabilities could not be used to access metadata, connect to internal services, access unauthorized data, or obtain cross tenant access. **No customer action is required for the four impacted Azure services.**

The impact of SSRF vulnerabilities can vary depending on the environment but can enable access to sensitive internal endpoints or port scanning. Microsoft has mechanisms in place to prevent privilege abuse such as the unauthorized retrieval of tokens, lateral movement or code execution. As such, these four vulnerabilities did not result in any material impact to Azure services or infrastructure.

## Technical Details

The following are the 4 Azure Services in which SSRF vulnerabilities were reported. Once these were reported, Microsoft engineering and security teams quickly took steps to mitigate these vulnerabilities.

* **Azure Digital Twins:** A SSRF vulnerability was reported on October 8, 2022 in the hosted Digital Twins Explorer. A fix was released on October 17, 2022. Azure Digital Twins has mechanisms to prevent IDMS and wireserver access preventing access other internal Azure services.

* **Azure Functions:** A SSRF vulnerability was reported on November 12, 2022, in Azure Functions Service that could allow an unauthenticated user to request an arbitrary URL allowing an attacker to enumerate local port information. A fix was released on December 9, 2022.

* **API Management:** A SSRF vulnerability reported on November 12, 2022 in Azure API Management Service could allow an authenticated user to request loopback URLs abusing the server. On November 16, 2022, the APIM engineering team completed deploying a fix to sufficiently block access to local ports/resources on the VM.

* **Azure Machine Learning (ML):** The authenticated SSRF vulnerability reported on December 2, 2022 in the machine learning service was assessed to be low risk as it did not leak any sensitive data or tokens and did not enable access to sensitive internal endpoints. The fix was released on December 20, 2022.

## Acknowledgement

We appreciate the opportunity to investigate the findings reported by Orca Security, which helped us further harden the service, and thank them for practicing safe security research under the terms of the [Microsoft Bug Bounty Program](https://www.microsoft.com/en-us/msrc/bounty). We encourage all researchers to work with vendors under [Coordinated Vulnerability Disclosure (CVD)](https://www.microsoft.com/en-us/msrc/cvd) and abide by the [rules of engagement](https://www.microsoft.com/en-us/msrc/pentest-rules-of-engagement) for penetration testing to avoid impacting customer data while conducting security research.

## References

Questions? Open a support case through the Azure Portal at [aka.ms/azsupt](https://ms.portal.azure.com/#view/Microsoft_Azure_Support/HelpAndSupportBlade/~/overview) .

Orca’s blog: [https://orca.security/resources/blog/ssrf-vulnerabilities-in-four-azure-services](https://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Forca.security%2Fresources%2Fblog%2Fssrf-vulnerabilities-in-four-azure-services&data=05%7C01%7Cmaryjen%40microsoft.com%7Cd6067a551f1949d3d6db08daf7879f86%7C72f988bf86f141af91ab2d7cd011db47%7C1%7C0%7C638094459133027517%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&sdata=9wMT6%2FntlOn%2FgY5CHvnn2wDG1S%2Fppx0YGrNHigjXQfY%3D&reserved=0)

文章来源: https://msrc-blog.microsoft.com/2023/01/17/microsoft-resolves-four-ssrf-vulnerabilities-in-azure-cloud-services/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)