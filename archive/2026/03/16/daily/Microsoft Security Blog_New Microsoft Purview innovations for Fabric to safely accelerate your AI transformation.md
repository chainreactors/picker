---
title: New Microsoft Purview innovations for Fabric to safely accelerate your AI transformation
url: https://techcommunity.microsoft.com/blog/microsoft-security-blog/new-microsoft-purview-innovations-for-fabric-to-safely-accelerate-your-ai-transf/4502156
source: Microsoft Security Blog
date: 2026-03-16
fetch_date: 2026-03-17T04:10:41.490580
---

# New Microsoft Purview innovations for Fabric to safely accelerate your AI transformation

[Skip to content](#main-content)[![Brand Logo](https://techcommunity.microsoft.com/t5/s/gxcuf89792/m_assets/themes/customTheme1/favicon-1730836271365.png?time=1730836274203)](/)

[Tech Community](/)[Community Hubs](/Directory)

[Products](/)

[Topics](/)

[Blogs](/Blogs)[Events](/Events)

[Skills Hub](/category/skills-hub)

[Community](/)

[Register](/t5/s/gxcuf89792/auth/oidcss/sso_login_redirect/provider/default?referer=https%3A%2F%2Ftechcommunity.microsoft.com%2Fblog%2Fmicrosoft-security-blog%2Fnew-microsoft-purview-innovations-for-fabric-to-safely-accelerate-your-ai-transf%2F4502156)[Sign In](/t5/s/gxcuf89792/auth/oidcss/sso_login_redirect/provider/default?referer=https%3A%2F%2Ftechcommunity.microsoft.com%2Fblog%2Fmicrosoft-security-blog%2Fnew-microsoft-purview-innovations-for-fabric-to-safely-accelerate-your-ai-transf%2F4502156)

1. [Microsoft Community Hub](/)
3. [Communities](/category/communities)[Products](/category/products-services)[Microsoft Security](/category/microsoft-security)
5. [Microsoft Security](/category/microsoft-security-product)
7. [Microsoft Security Community Blog](/category/microsoft-security-product/blog/microsoft-security-blog)

## Blog Post

![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00NTAyMTU2LUhDZ0V3UA?revision=2&image-dimensions=2000x2000&constrain-image=true)

Microsoft Security Community Blog

5 MIN READ

# New Microsoft Purview innovations for Fabric to safely accelerate your AI transformation

[![darrenportillo's avatar](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/dS0yMzM0NjQ3LTU1NzgzM2k4QTNFQTlGM0I1MTRDNTJB?image-dimensions=50x50)](/users/darrenportillo/2334647)

[darrenportillo](/users/darrenportillo/2334647)

![Icon for Microsoft rank](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/cmstNC05WEo0blc?image-dimensions=100x16&constrain-image=true)Microsoft

Mar 16, 2026

As organizations adopt AI, security and governance remain core primitives for safe AI transformation and acceleration. After all, data leaders are aware of the notion that:

**Your AI is only as good as your data.**

Organizations are skeptical about AI transformation due to concerns of sensitive data oversharing and poor data quality. In fact, 86% of organizations lack visibility into AI data flows, operating in darkness about what information employees share with AI systems [[1]](#community-4502156-_ftn1). Compounding on this challenge, about 67% of executives are uncomfortable using data for AI due to quality concerns [[2].](#community-4502156-_ftn2) The challenges of data oversharing and poor data quality requires organizations to solve these issues seamlessly for the safe usage of AI. Microsoft Purview offers a modern, unified approach to help organizations secure and govern data across their entire data estate, in particular best in class integrations with M365, Microsoft Fabric, and Azure data estates, streamlining oversight and reducing complexity across the estate.

At FabCon Atlanta, we’re announcing new Microsoft Purview innovations for Fabric to help seamlessly secure and confidently activate your data for AI transformation. These updates span data security and data governance, granting Fabric users to both

1. Discoverrisks and prevent data oversharing in Fabric
2. Improve governance processes and data quality across their data estate

**1. Discover risks and prevent data oversharing in Fabric**

As data volume increases with AI usage, Microsoft Purview secures your data with capabilities such as Information Protection, Data Loss Prevention (DLP), Insider Risk Management (IRM), and Data Security Posture Management (DSPM). These capabilities work together to secure data throughout its lifecycle and now specifically for your Fabric data estate. Here are a few new Purview innovations for your Fabric estate:

**Microsoft** **Purview DLP policies to prevent data leakage for Fabric Warehouse and KQL/SQL DBs**

Now generally available, Microsoft Purview DLP policies allow Fabricadmins to prevent data oversharing in Fabric through policy tip triggering when sensitive data is detected in assets uploaded to Warehouses. Additionally, in preview, Purview DLP enables Fabric admins to restrict access to assets with sensitive data in KQL/SQL DBs and Fabric Warehouses to prevent data oversharing. This helps admins limit access to sensitive data detected in these data sources and data stores to just asset owners and allowed collaborators. These DLP innovations expand upon the depth and breadth of existing DLP policies to ensure sensitive data in Fabric is protected.

![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00NTAyMTU2LWhUcTJ1Sg?image-dimensions=999x508&revision=2)

***Figure 1. DLP restrict access preventing data oversharing of customer information stored in a KQL database.***

**Microsoft Purview** **Insider Risk Management (IRM)** **indicators for Lakehouse, IRM data theft quick policy for Fabric, and IRM pay-as-you-go usage report for Fabric**

Microsoft Purview Insider Risk Management is now generally available for Microsoft Fabric extending its risk-detection capabilities to Microsoft Fabric lakehouses (in addition to Power BI which is supported today) by offering ready-to-use risk indicators based on risky user activities in Fabric lakehouses, such as sharing data from a Fabric lakehouse with people outside the organization . Additionally, IRM data theft policy is now generally available for security admins to create a data theft policy to detect Fabric data exfiltration, such as exporting Power BI reports. Also, organizations now have visibility into how much they are billed with the IRM pay-as-you-go usage report for Fabric, providing customers with an easy-to-use dashboard to track their consumption and predictability on costs.

![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00NTAyMTU2LUJ1UkFtWg?image-dimensions=999x561&revision=2)

***Figure 2. IRM identifying risky user behavior when handling data in a Fabric Lakehouse.***

![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00NTAyMTU2LXhLTkNPUw?image-dimensions=999x561&revision=2)

***Figure 3. Security admins can create a data theft policy to detect Fabric data exfiltration.***

![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00NTAyMTU2LUExUUpjUw?image-dimensions=999x624&revision=2)

***Figure 4. Security admins can check the pay-as-you-go usage (processing units) across different workloads and activities such as the downgrading of sensitivity labels of a lakehouse through the usage report.***

**Microsoft Purview for all Fabric Copilots and Agents**

Microsoft Purview currently provides capabilities in preview for all Copilots and Agents in Fabric. Organizations can:

* **Discover data risks** such as sensitive data in user prompts and responses and receive recommended actions to reduce these risks.
* **Detect and remediate** **oversharing risks** with Data Risk Assessments on DSPM, that identify potentially overshared, unprotected, or sensitive Fabric assets, giving teams clear visibility into where data exposure exists and enabling targeted actions—like applying labels or policies—to reduce risk and ensure Fabric data is AI‑ready and governed by design.
* **Identify risky AI usage** with Microsoft Purview Insider Risk Management to investigate risky AI usage, such as an inadvertent user who has neglected security best practices and shared sensitive data in AI.
* **Govern AI usage** with Microsoft Purview Audit, Microsoft Purview eDiscovery, retention policies, and non-compliant usage detection.

![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00NTAyMTU2LXltdEQ3cg?image-dimensions=999x602&revision=2)

***Figure 5. Purview DSPM provides admins with the ability to discover data risks such as a user’s attempt to obtain historical data within a data agent in the Data Science workload in Fabric. DSPM subsequently provides actions to solve this risk.***

N...