---
title: AutoJack: How a single page can RCE the host running your AI agent
url: https://www.microsoft.com/en-us/security/blog/2026/06/18/autojack-single-page-rce-host-running-ai-agent/
source: Microsoft Security Blog
date: 2026-06-19
fetch_date: 2026-06-20T06:13:23.258851
---

# AutoJack: How a single page can RCE the host running your AI agent

[Skip to content](#wp--skip-link--target)

[Skip to main content](#mainContent)

[![Microsoft](https://uhf.microsoft.com/images/microsoft/RE1Mu3b.png)](https://www.microsoft.com)
[Security](https://www.microsoft.com/en-us/security)

[Microsoft Defender](https://www.microsoft.com/en-us/security/business/microsoft-defender)
[Microsoft Entra](https://www.microsoft.com/en-us/security/business/microsoft-entra)
[Microsoft Intune](https://www.microsoft.com/en-us/security/business/microsoft-Intune)
[Microsoft Purview](https://www.microsoft.com/en-us/security/business/microsoft-purview)
[Microsoft Security Copilot](https://www.microsoft.com/en-us/security/business/ai-machine-learning/microsoft-security-copilot)
[Microsoft Sentinel](https://www.microsoft.com/en-us/security/business/siem-and-xdr/microsoft-sentinel)
[View all products](https://www.microsoft.com/en-us/security/view-all-products)

[AI-powered cybersecurity](https://www.microsoft.com/en-us/security/business/solutions/generative-ai-cybersecurity)
[Cloud security](https://www.microsoft.com/en-us/security/business/solutions/cloud-security)
[Data security & governance](https://www.microsoft.com/en-us/security/business/solutions/data-security-governance)
[Identity & network access](https://www.microsoft.com/en-us/security/business/solutions/identity-access)
[Privacy & risk management](https://www.microsoft.com/en-us/security/business/solutions/privacy-risk-management)
[Security for AI](https://www.microsoft.com/en-us/security/business/solutions/security-for-ai%20%20%20)
[Small and medium business](https://www.microsoft.com/en-us/security/small-medium-business)
[Unified SecOps](https://www.microsoft.com/en-us/security/business/solutions/ai-powered-unified-secops-platform)
[Zero Trust](https://www.microsoft.com/en-us/security/business/zero-trust)
[Pricing](https://www.microsoft.com/en-us/security/pricing-overview)
[Services](https://www.microsoft.com/en-us/security/services)
[Partners](https://www.microsoft.com/en-us/security/business/partnerships)
[Why Microsoft Security](https://www.microsoft.com/en-us/security/why-microsoft-security)

[Cybersecurity awareness](https://www.microsoft.com/en-us/security/business/cybersecurity-awareness)
[Customer stories](https://www.microsoft.com/en-us/customers/search?filters=product%3Amicrosoft-security)
[Security 101](https://www.microsoft.com/en-us/security/business/security-101)
[Product trials](https://www.microsoft.com/en-us/security/business/get-started/start-free-trial)
[How we protect Microsoft](https://www.microsoft.com/en-us/insidetrack)

[Industry recognition](https://www.microsoft.com/en-us/security/business/reports-analysis/industry-recognized-cybersecurity-leader)
[Microsoft Security Insider](https://www.microsoft.com/en-us/security/security-insider/)
[Microsoft Digital Defense Report](https://www.microsoft.com/en-us/security/security-insider/threat-landscape/microsoft-digital-defense-report-2025)
[Security Response Center](https://www.microsoft.com/en-us/msrc/)

[Microsoft Security Blog](https://www.microsoft.com/en-us/security/blog/)
[Microsoft Security Events](https://www.microsoft.com/en-us/events/search-catalog?filters=topic%3Asecurity&scenario=events)
[Microsoft Tech Community](https://techcommunity.microsoft.com/t5/security-compliance-and-identity/ct-p/MicrosoftSecurityandCompliance)

[Documentation](https://learn.microsoft.com/en-us/security/)
[Technical Content Library](https://learn.microsoft.com/en-us/security)
[Training & certifications](https://learn.microsoft.com/en-us/learn/topics/sci?wt.mc_id=techcom_header-webpage-m365)

[Compliance Program for Microsoft Cloud](https://www.microsoft.com/en-us/security/business/services/compliance-program-microsoft-cloud)
[Microsoft Trust Center](https://www.microsoft.com/en-us/trust-center)
[Security Engineering Portal](https://www.microsoft.com/en-us/securityengineering)
[Service Trust Portal](https://servicetrust.microsoft.com/)
[Microsoft Secure Future Initiative](https://www.microsoft.com/en-us/trust-center/security/secure-future-initiative)
[Business Solutions Hub](https://www.microsoft.com/en-us/microsoft-cloud/solutions)
[Contact Sales](https://www.microsoft.com/en-us/security/business/get-started/contact-us)
[Start free trial](https://www.microsoft.com/en-us/security/business/get-started/start-free-trial)

[Microsoft Security](https://www.microsoft.com/en-us/security)
[Azure](https://azure.microsoft.com/en-us/)
[Dynamics 365](https://dynamics.microsoft.com/en-us/)
[Microsoft 365](https://www.microsoft.com/en-us/microsoft-365/business/)
[Microsoft Teams](https://www.microsoft.com/en-us/microsoft-teams/group-chat-software)
[Windows 365](https://www.microsoft.com/en-us/windows-365)

[Microsoft AI](https://www.microsoft.com/en-us/ai?icid=DSM_AllCommercial_AI)
[Azure Space](https://azure.microsoft.com/en-us/solutions/space/)
[Mixed reality](https://www.microsoft.com/en-us/mixed-reality/windows-mixed-reality)
[Microsoft HoloLens](https://www.microsoft.com/en-us/hololens)
[Microsoft Viva](https://www.microsoft.com/en-us/microsoft-viva)
[Quantum computing](https://azure.microsoft.com/en-us/solutions/quantum-computing/)
[Sustainability](https://www.microsoft.com/en-us/sustainability/)

[Education](https://www.microsoft.com/en-us/education)
[Automotive](https://www.microsoft.com/en-us/industry/automotive)
[Financial services](https://www.microsoft.com/en-us/industry/financial-services/banking)
[Government](https://www.microsoft.com/en-us/industry/government)
[Healthcare](https://www.microsoft.com/en-us/industry/health/microsoft-cloud-for-healthcare)
[Manufacturing](https://www.microsoft.com/en-us/industry/manufacturing/microsoft-cloud-for-manufacturing)
[Retail](https://www.microsoft.com/en-us/industry/consumer-goods)

[Find a partner](https://partner.microsoft.com/en-US/)
[Become a partner](https://partner.microsoft.com/en-US/membership/cloud-solution-provider)
[Partner Network](https://partner.microsoft.com/en-us/membership)
[Microsoft Marketplace](https://marketplace.microsoft.com?icid=DSM_AllCommercial_Marketplace&ocid=cmm3c8ee9bs)
[Software companies](https://www.microsoft.com/software-development-companies?icid=DSM_AllCommercial_SoftwareCompanies&ocid=cmm3c8ee9bs)

[Blog](https://blogs.microsoft.com/)
[Microsoft Advertising](https://about.ads.microsoft.com/en-us?s_cid=dig-src_uhfcomm)
[Developer Center](https://developer.microsoft.com/en-us/)
[Documentation](https://learn.microsoft.com/docs/)
[Events](https://www.microsoft.com/en-us/events)
[Licensing](https://www.microsoft.com/en-us/licensing/)
[Microsoft Learn](https://learn.microsoft.com/)
[Microsoft Research](https://www.microsoft.com/en-us/research/)

[View Sitemap](https://www.microsoft.com/en-us/sitemap)

![](https://www.microsoft.com/en-us/security/blog/wp-content/themes/security-blog-2025/dist/images/single-bg.jpg)

![](https://www.microsoft.com/en-us/security/blog/wp-content/themes/security-blog-2025/dist/images/single-bg-dark.jpg)

1. [Home](https://www.microsoft.com/en-us/security/blog/)
2. AutoJack: How a single page can RCE the host running your AI agent

Search

![Graphic featuring a lock icon representing adversarial and abuse of AI.](https://www.microsoft.com/en-us/security/blog/wp-content/uploads/2026/03/MS_Actional-Insights_Adversarial-AI.jpg)

* [Research](https://www.microsoft.com/en-us/security/blog/content-type/research/)
* June 18
* 17 min read

# AutoJack: How a single page can RCE the host running your AI agent

By [Microsoft Defender Security Research Team](https://www.microsoft.com/en-us/security/blog/author/windows-defender-research/ "Posts by Microsoft Defender Security Research Team")

## Listen to this post

/

1x

[![Copilot logo](https://www.microsoft.com/en-us/security/blog/wp-content/mu-plugins/ms-core/dist/svg/copilot-logo.svg)](https://azure.microsoft.com/en-us/products/cognitive-services/text-to-speech)
Powered by Microsoft Copilot

---

## Share

* [Link copied to clipboard!](https://www.microsoft.com/en-us/se...