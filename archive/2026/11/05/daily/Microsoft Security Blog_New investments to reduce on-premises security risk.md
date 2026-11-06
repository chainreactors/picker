---
title: New investments to reduce on-premises security risk
url: https://techcommunity.microsoft.com/blog/microsoft-security-blog/new-investments-to-reduce-on-premises-security-risk/4570381
source: Microsoft Security Blog
date: 2026-11-05
fetch_date: 2026-11-06T08:39:43.198395
---

# New investments to reduce on-premises security risk

Open Side Menu

[Skip to content](#main-content)[![Microsoft Community Hub](https://techcommunity.microsoft.com/t5/s/gxcuf89792/m_assets/themes/customTheme1/favicon-1730836271365.png?time=1730836274203)](/)

[Tech Community](/)[Community Hubs](/Directory)

[Products](/)

[Topics](/)

[Blogs](/Blogs)

[Events](/Events)

[Skills Hub](/category/skills-hub)

[Community](/)

[Register](/t5/s/gxcuf89792/auth/oidcss/sso_login_redirect/provider/default?referer=https%3A%2F%2Ftechcommunity.microsoft.com%2Fblog%2Fmicrosoft-security-blog%2Fnew-investments-to-reduce-on-premises-security-risk%2F4570381)[Sign In](/t5/s/gxcuf89792/auth/oidcss/sso_login_redirect/provider/default?referer=https%3A%2F%2Ftechcommunity.microsoft.com%2Fblog%2Fmicrosoft-security-blog%2Fnew-investments-to-reduce-on-premises-security-risk%2F4570381)

1. [Microsoft Community Hub](/)
3. [Communities](/category/communities)[Products](/category/products-services)[Microsoft Security](/category/microsoft-security)
5. [Microsoft Security Community](/category/microsoft-security-product)
7. [Microsoft Security Community Blog](/category/microsoft-security-product/blog/microsoft-security-blog)

## Blog Post

![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00NTcwMzgxLXA1OThxbA?revision=13&image-dimensions=2000x2000&constrain-image=true)

Microsoft Security Community Blog

4 MIN READ

# New Investments to Reduce On-Premises Security Risk

[![PaulLorimer's avatar](https://techcommunity.microsoft.com/t5/s/gxcuf89792/m_assets/avatars/default/avatar-1.svg?image-dimensions=50x50)](/users/paullorimer/1505575)

[PaulLorimer](/users/paullorimer/1505575)

![Icon for Microsoft rank](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/cmstNC05WEo0blc?image-dimensions=100x16&constrain-image=true)Microsoft

Nov 05, 2026

On-premises servers can be essential to business operations, but they are increasingly attractive targets to attackers. AI can help less-skilled actors analyze software, develop malicious tools, and repeat attack workflows at greater speed and scale, shortening the window between exposure and exploitation. Organizations need to strengthen security faster without disrupting the critical workloads they rely on.

Today, we’re announcing a new on-premises security initiative, initially focused on server workloads. The initiative brings together guidance, [migration](https://learn.microsoft.com/microsoft-365/fasttrack/data-migration), and product investments to help customers understand and prioritize risk, reduce their on-premises footprint wherever possible, and strengthen critical workloads that need to remain. Guidance for the initiative will soon be available through [Secure Now](https://sip.security.microsoft.com/secure-now), which also includes our AI readiness checklist in Microsoft Security Exposure Management and guidance for strengthening foundational security.

|  |  |  |
| --- | --- | --- |
| **Understand**  Identify the most important on-premises risks and prioritize actions customers can take now. | **Reduce**  Move workloads to Microsoft 365 where possible to take advantage of cloud-based security, resilience, and continuous innovation. | **Secure**  Strengthen critical workloads that need to remain on-premises and reduce the manual work required to keep them secure. |

This approach starts with understanding where to focus—and extends to making supported on-premises products more secure by default.

##### **Modernize where you can, and strengthen the security of what must remain.**

### **Making supported on-premises workloads more secure by default**

Within the Secure pillar of the on-premises security initiative, we’re also hardening the products themselves through On-Premises Baseline Security Mode, starting with [supported](https://learn.microsoft.com/lifecycle/products/) Exchange Server, SharePoint Server, and Skype for Business Server workloads.

##### **On-Premises Baseline Security Mode**

On-Premises Baseline Security Mode is designed to make the default security posture stronger—reducing the number of recommended security settings administrators must configure and maintain manually. For supported on-premises server workloads, it starts with a validated and tested secure-by-default configuration from initial deployment, while preserving administrator control. Building on protections available today, it progressively establishes and maintains more of the recommended security posture through the products themselves, adapting the baseline as threats and Microsoft security guidance evolve.

The result is less manual effort and a stronger security posture maintained increasingly through the products themselves. We’re advancing this work across three areas: Patch, Configure, and Protect.

![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00NTcwMzgxLTA2NDVTRQ?image-dimensions=796x530&revision=13)Figure 1: On-Premises Baseline Security Mode builds on capabilities available today across Patch, Configure, and Protect, with greater automation and stronger defaults coming over time.

##### **Patch: close known vulnerabilities faster**

The need is clear in our deployment data: many Exchange Server deployments are not running the current security update, including a substantial share on unsupported versions. Closing this protection gap requires both releasing fixes faster and helping customers apply them sooner.

**Today.** Since September 2026, Microsoft has released not only Critical but also Important security updates outside the traditional Patch Tuesday schedule when faster action is needed, helping customers address known vulnerabilities sooner.

**Next.** In Q1 calendar year 2027, we’re targeting automatic application of security updates after a fixed period following release in connected SharePoint Server, Exchange Server, and Skype for Business Server environments.

**Release fixes faster, then help those fixes reach servers faster.**

##### **Configure: make the safer posture easier to maintain**

Security requires more than current software. Configuration and permissions can drift over time, creating gaps between the intended security posture and the environment administrators are operating. Customers need a clearer way to identify those gaps, establish recommended settings, and maintain them as environments evolve.

**Today.** Tenant Configuration Management can help customers assess supported SharePoint, Exchange, and Skype for Business Server environments and identify where permissions are broader than intended.

**Next.** In Q1 2027, we plan to introduce hardened default configurations for SharePoint Server, Exchange Server, and Skype for Business Server, moving from identifying configuration risk toward establishing Microsoft-recommended security settings by default. We also plan to identify configuration drift so administrators can see when environments move away from that baseline.

**Make the safer configuration easier to establish and harder to unintentionally lose.**

##### **Protect: reduce exposure when threats can’t wait for a patch**

Some threats emerge before a permanent security update is available and fully deployed. During that window, customers need mitigations that can reduce exposure quickly without replacing the underlying security update.

**Today.** Emergency Mitigation Service can automatically apply interim mitigations for certain emerging vulnerabilities, helping reduce exposure while a permanent security update is prepared and deployed. Mitigation addresses the immediate risk; the security update addresses the underlying vulnerability.

**Next.** In December 2026, we plan to introduce Emergency Mitigation Service 2.0 for Exchange Server and Skype for Business Server, enabling it by default and expanding the security mitigations it can apply. In January 2027, we are planning to extend Emergency Mitigation Service 2.0 to cover SharePoint Server.

**When threats move faster, protection needs to move faster too.**

#...