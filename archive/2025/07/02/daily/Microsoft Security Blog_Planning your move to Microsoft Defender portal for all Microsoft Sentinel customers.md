---
title: Planning your move to Microsoft Defender portal for all Microsoft Sentinel customers
url: https://techcommunity.microsoft.com/blog/microsoft-security-blog/planning-your-move-to-microsoft-defender-portal-for-all-microsoft-sentinel-custo/4428613
source: Microsoft Security Blog
date: 2025-07-02
fetch_date: 2025-10-06T23:39:43.273400
---

# Planning your move to Microsoft Defender portal for all Microsoft Sentinel customers

[Skip to content](#main-content)[![Brand Logo](https://techcommunity.microsoft.com/t5/s/gxcuf89792/m_assets/themes/customTheme1/favicon-1730836271365.png?time=1730836274203)](/)

[Tech Community](/)[Community Hubs](/Directory)

[Products](/)

[Topics](/)

[Blogs](/Blogs)[Events](/Events)

[Microsoft Learn](/category/MicrosoftLearn)

[Community](/)

[Register](/t5/s/gxcuf89792/auth/oidcss/sso_login_redirect/provider/default?referer=https%3A%2F%2Ftechcommunity.microsoft.com%2Fblog%2Fmicrosoft-security-blog%2Fplanning-your-move-to-microsoft-defender-portal-for-all-microsoft-sentinel-custo%2F4428613)[Sign In](/t5/s/gxcuf89792/auth/oidcss/sso_login_redirect/provider/default?referer=https%3A%2F%2Ftechcommunity.microsoft.com%2Fblog%2Fmicrosoft-security-blog%2Fplanning-your-move-to-microsoft-defender-portal-for-all-microsoft-sentinel-custo%2F4428613)

1. [Microsoft Community Hub](/)
3. [Communities](/category/communities)[Products](/category/products-services)[Microsoft Security](/category/microsoft-security)
5. [Microsoft Security](/category/microsoft-security-product)
7. [Microsoft Security Community Blog](/category/microsoft-security-product/blog/microsoft-security-blog)

## Blog Post

![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00NDI4NjEzLVdsRDdaSw?revision=5&image-dimensions=2000x2000&constrain-image=true)

Microsoft Security Community Blog

5 MIN READ

# Planning your move to Microsoft Defender portal for all Microsoft Sentinel customers

[![TomerBrand's avatar](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/dS04NjI0Mi1iMDNhOG8?image-coordinates=0%2C408%2C3840%2C4248&image-dimensions=50x50)](/users/tomerbrand/86242)

[TomerBrand](/users/tomerbrand/86242)

![Icon for Microsoft rank](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/cmstNC05WEo0blc?image-dimensions=100x16&constrain-image=true)Microsoft

Jul 01, 2025

In November 2023, Microsoft [announced](https://techcommunity.microsoft.com/blog/microsoftsentinelblog/introducing-a-unified-security-operations-platform-with-microsoft-sentinel-and-d/3983341) our strategy to unify security operations by bringing the best of XDR and SIEM together. Our first step was bringing Microsoft Sentinel into the Microsoft Defender portal, giving teams a single, comprehensive view of incidents, reducing queue management, enriching threat intel, streamlining response and enabling SOC teams to take advantage of Gen AI in their day-to-day workflow. Since then, considerable progress has been made with thousands of customers using this new unified experience; to enhance the value customers gain when using Sentinel in the Defender portal, multi-tenancy and multi-workspace support was added to help customers with more sophisticated deployments.

Our mission is to unify security operations by bringing all your data, workflows, and people together to unlock new capabilities and drive better security outcomes. As a strong example of this, last year we added extended posture management, delivering powerful posture insights to the SOC team. This integration helps build a closed-loop feedback system between your pre- and post-breach efforts. Exposure Management is just one example. By bringing everything together, we can take full advantage of AI and automation to shift from a reactive to predictive SOC that anticipates threats and proactively takes action to defend against them.

Beyond Exposure Management, Microsoft has been constantly innovating in the Defender experience, adding not just SIEM but also Security Copilot. The Sentinel experience within the Defender portal is the focus of our innovation energy and where we will continue to add advanced Sentinel capabilities going forward.

Onboarding to the new unified experience is easy and doesn’t require a typical migration. Just a few clicks and permissions. Customers can continue to use Sentinel in the Azure portal while it is available even after choosing to transition.

**Today, we’re announcing that we are moving to the next phase of the transition with a target to retire the Azure portal for Microsoft Sentinel by July 1, 2026.  Customers not yet using the Defender portal should plan their transition accordingly.**

![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00NDI4NjEzLUpTMTk1Wg?image-dimensions=999x545&revision=5)*Microsoft Sentinel in the Microsoft Defender portal*
> *“Really amazing to see that coming, because cross querying with tables in one UI is really cool! Amazing, big step forward to the unified [Defender] portal.”*
>
> ***Glueckkanja AG***
>
> *“The biggest benefit of a unified security operations solution (Microsoft Sentinel + Microsoft Defender XDR) has been the ability to combine data in Defender XDR with logs from third party security tools. Another advantage developed has been to eliminate the need to switch between Defender XDR and Microsoft Sentinel portals, now having a single pane of glass, which the team has been wanting for some years.”*
>
> ***Robel Kidane, Group Information Security Manager, Renishaw PLC***

##### **Delivering the SOC of the future**

Unifying threat protection, exposure management and security analytics capabilities in one pane of glass not only streamlines the user experience, but also enables Sentinel customers to realize security outcomes more efficiently:

* **Analyst efficiency**: A single portal reduces context switching, simplifies workflows, reduces training overhead, and improves team agility.

* **Integrated insights**: SOC-focused case management, threat intelligence, incident correlation, advanced hunting, exposure management, and a prioritized incident queue enriched with business and sensitivity context—enabling faster, more informed detection and response across all products.

* **SOC optimization**: Security controls that can be adjusted as threats and business priorities change to control costs and provide better coverage and utilization of data, thus [maximizing ROI from the SIEM](https://learn.microsoft.com/en-us/azure/sentinel/soc-optimization/soc-optimization-access?tabs=defender-portal).

* **Accelerated response**: AI-driven detection and response which [reduces mean time to respond (MTTR) by 30%](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/final/microsoft-brand/documents/Generative-AI-and-Security-Operations-Center-Productivity-Evidence-from-Live-Operations_v2.5-FINAL.pdf), [increases security response efficiency by 60%](https://www.microsoft.com/en/customers/story/1797704796946869974-qnet-microsoft-copilot-for-security-retailers-en-hong-kong-sar), and enables embedded Gen AI and agentic workflows.

##### **What’s next: Preparing for the retirement of the Sentinel Experience in the Azure Portal**

Microsoft is committed to supporting every single customer in [making that transition](https://learn.microsoft.com/azure/sentinel/move-to-defender) over the next 12 months. Beginning July 1, 2026, Sentinel users will be automatically redirected to the Defender portal.

After helping thousands of customers smoothly make the transition, we recommend that security teams begin planning their migration and change management now to ensure continuity and avoid disruption. While the technical process is very straightforward, we have found that early preparation allows time for workflow validation, training, and process alignment to take full advantage of the new capabilities and experience.

##### **Tips for a Successful Migration to Microsoft Defender**

1. *Leverage Microsoft’s help*:

Leverage [Microsoft documentation](https://learn.microsoft.com/en-us/unified-secops-platform/), [instructional videos](https://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.youtube.com%2Fplaylist%3Flist%3DPL3ZTgFEc7Lyska6WLWBzc8sob-kYA2jPj&data=05%7C02%7Ccsatish%40microsoft.com%7Cc219b9e1b8fb4d7a5ece08dda990041e%7C72f988bf86f141af91ab2d7cd011db47%7C1%7C0%7C638853158322245922%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLj...