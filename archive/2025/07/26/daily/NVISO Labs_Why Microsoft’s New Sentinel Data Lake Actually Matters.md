---
title: Why Microsoft’s New Sentinel Data Lake Actually Matters
url: https://blog.nviso.eu/2025/07/25/why-microsofts-new-sentinel-data-lake-actually-matters/
source: NVISO Labs
date: 2025-07-26
fetch_date: 2025-10-06T23:39:43.273400
---

# Why Microsoft’s New Sentinel Data Lake Actually Matters

[Skip to content](#content)

[![NVISO Labs](https://blog.nviso.eu/wp-content/uploads/2022/12/cropped-abn-zcrj_400x400-1.png)](https://blog.nviso.eu/)

[NVISO Labs](https://blog.nviso.eu/)

Cyber security research, straight from the lab! 🐀

* [twitter](https://twitter.com/NVISO_Labs)
* [linkedin](https://www.linkedin.com/company/nviso-cyber)
* mail us
* [our company](https://www.nviso.eu)
* [SSO](https://blog.nviso.eu/wp-admin/edit.php)

Menu

* [All](https://blog.nviso.eu/)
* [Blue Team](https://blog.nviso.eu/category/blue-team/)
* [Cloud Security](https://blog.nviso.eu/category/cloud-security/)
  + [AWS](https://blog.nviso.eu/category/cloud-security/aws/)
  + [Azure](https://blog.nviso.eu/category/cloud-security/azure/)
  + [GCP](https://blog.nviso.eu/category/cloud-security/gcp/)
  + [Microsoft 365](https://blog.nviso.eu/category/cloud-security/microsoft-365/)
* [Awareness](https://blog.nviso.eu/category/awareness/)
* [Forensics](https://blog.nviso.eu/category/forensics/)
* Other
  + [Application Security](https://blog.nviso.eu/category/application-security/)
  + [IoT Security](https://blog.nviso.eu/category/iot-security/)
  + [Web Security](https://blog.nviso.eu/category/web-security/)
  + [Industrial Security](https://blog.nviso.eu/category/industrial-security/)
  + [Mobile Security](https://blog.nviso.eu/category/mobile-security/)
  + [Cyber Strategy](https://blog.nviso.eu/category/cyber-strategy/)
  + [Purple Team](https://blog.nviso.eu/category/purple-team/)
  + [Red Team](https://blog.nviso.eu/category/red-team/)
  + [Events](https://blog.nviso.eu/category/events/)

# Why Microsoft’s New Sentinel Data Lake Actually Matters

[Maxim Deweerdt](https://blog.nviso.eu/author/maxim-deweerdt/ "Posts by Maxim Deweerdt")

[SOC](https://blog.nviso.eu/category/soc/), [Microsoft 365 Defender](https://blog.nviso.eu/category/microsoft-365-defender/), [Blue Team](https://blog.nviso.eu/category/blue-team/), [Sentinel](https://blog.nviso.eu/category/cloud-security/sentinel/), [SIEM](https://blog.nviso.eu/category/siem/), [Cloud Security](https://blog.nviso.eu/category/cloud-security/)

July 25, 2025July 25, 2025
5 Minutes

**From a Cybersecurity Architect Who’s Seen the Struggles Firsthand**

Over the years, we’ve migrated more than a few SIEM environments to Microsoft Sentinel. And no matter how different the organizations were, the same headaches kept showing up:

* 🔍 What logs do we *really* need to keep for detection?
* 💾 What can we *afford* to store long-term?
* 💸 And how do we not break the bank doing it?

Let’s be real, Microsoft Sentinel has always been powerful, but calling it “cost-effective” felt like a bit of a stretch. Especially when it came to storing secondary/compliance log –  the kinds of data you don’t need every day, but desperately want during incident investigations.

In past projects, we used all sorts of workarounds: filtering logs, sampling, dumping less-used data elsewhere. In the most recent months, we heavily relied on Auxiliary logs. It sort of worked but always felt like a compromise.

---

**✨ Now There’s a Better Way**

![](https://blog.nviso.eu/wp-content/uploads/2025/07/image-91.png)

With the new [**Microsoft Sentinel Data Lake**](https://learn.microsoft.com/en-us/azure/sentinel/datalake/sentinel-lake-overview), we have a new approach that allows us to short-circuit the problem.

Instead of cramming everything into the Analytics tier and paying high ingestion + query costs, the Data Lake lets you store huge volumes of data **way more cheaply**. And still access it when you need to.

If you’ve ever had to make that painful choice (*“Can we afford to keep these logs?”*) this is the answer.

**Here’s what I’m seeing in the real world:**

* 💰 **Costs drop significantly:** Based on early testing, we’re seeing around **85% savings** by pushing logs to the Data Lake tier instead of Analytics.
* 🗄️ **Long-term retention is finally realistic:** You can store logs for up to **12 years** without burning your budget.
* 🔎 **Investigations are smoother:** Running historical KQL queries to dig into old incidents is actually doable now, no more *“we didn’t keep those logs”* regrets.

---

**🤔 So What’s the Catch?**

Honestly? Not much, just some trade-offs you need to plan for.

![](https://blog.nviso.eu/wp-content/uploads/2025/07/image-90.png)

The **Analytics tier** is still where your hot data lives: logs you use for real-time detection, alerts, dashboards, and fast queries. That’s not changing.

The **Data Lake tier** is more like cold storage, it’s where your context-rich but high-volume stuff lives: endpoint telemetry, flow data, infrastructure logs, and so on. This is the old “Auxiliary” tier.

**📊 Quick Comparison**

| **Feature** | **Analytics Tier (Hot)** | **Data Lake Tier (Cold)** |
| --- | --- | --- |
| Main Use | Real-time detection, dashboards, threat hunting | Long-term storage, compliance, historical hunting |
| Query Performance | Fast and indexed | Slower (full table scans) |
| Costs | Higher (standard ingestion + query) | Low ingestion, pay-per-query GB scanned |
| Retention | Up to 2 years | Up to 12 years |
| Great For | Azure AD sign-ins, alerts, DNS | EDR logs, network flow, anything high-volume |

The cool part? The two tiers work together. You keep the signal in Analytics, and push the noise (but still important noise) to Data Lake. You can now build queries across the two data tiers. It’s not about logging less, it’s about logging smarter.

---

💬 *“The Sentinel Data Lake isn’t just cheaper storage—it’s the missing piece that lets us keep more context, hunt smarter, and finally stop choosing between cost and visibility.”*
— *Maxim Deweerdt, Solution Architect*

---

**🛠 A Few Tips If You’re Considering the Switch**

Here’s what I’ve learned working with teams making this move:

* ⚡ **Existing logs:** Once you enable Sentinel Data Lake, your existing logs from the Analytics tier are already available there too: no need to duplicate anything.
* 📦 **Auxiliary logs:** If you were already using Auxiliary logs, these will now show up in the new Data Lake tier. No changes needed here. After onboarding, auxiliary log tables are *no longer available in Microsoft Defender Advanced hunting*. Instead, you can access them through data lake exploration KQL queries in the Defender portal.

Also:

* 🕵️ **Historical queries:** You can run KQL queries directly against the Data Lake for threat hunting or investigations. It’s slower than querying hot data, but it works, and it’s a game-changer when you need historical context.
* 🚀 **Promote logs on demand:** You can even temporarily promote logs from cold to hot if you’re working on a specific case and want faster access.

---

**⚠️ Potential Drawbacks of Moving to Sentinel Data Lake**

While Microsoft Sentinel Data Lake brings significant cost savings and long-term retention benefits, there are trade-offs to consider:

* **Data Lake Interactive Queries limitations**: Interactive queries are limited to 30,000 rows or 64 MB of data and timeout after 10 minutes. When selecting a broad time range, your query may exceed these limits. Use KQL jobs for queries that would exceed this limit.
* **Cost Complexity**: The pay-per-query GB pricing model makes cost forecasting harder, and frequent cold-to-hot data promotions can add hidden costs.
* **Tooling & Workflow Adjustments**: After enabling Sentinel Data Lake, Auxiliary logs no longer appear in Defender’s Advanced Hunting. Instead, they can be accessed only via the Data Lake Exploration KQL interface in the Defender portal.
* **Learning Curve**: Analysts need stronger KQL optimization skills to minimize scan costs and improve performance.

**Microsoft Sentinel Data Lake: Pros vs. Cons**

| **✅ Pros** | **⚠️ Cons** |
| --- | --- |
| **85%+ cost savings** compared to Analytics tier for high-volume logs | **Slower queries** due to lack of indexing |
| **Long-term retention (up to 12 years)** | **Pay-per-query costs** add unpredictability |
...