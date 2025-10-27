---
title: Enforce Mitigation for High & Medium Level Risks in Access Request Management (ARM)
url: https://blogs.sap.com/2023/06/25/enforce-mitigation-for-high-medium-level-risks-in-access-request-management-arm/
source: SAP Blogs
date: 2023-06-26
fetch_date: 2025-10-04T11:46:07.409329
---

# Enforce Mitigation for High & Medium Level Risks in Access Request Management (ARM)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Financial Management](/t5/financial-management/ct-p/financial-management)
* [Financial Management Blog Posts by Members](/t5/financial-management-blog-posts-by-members/bg-p/financial-management-blog-members)
* Enforce Mitigation for High & Medium Level Risks i...

Financial Management Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/financial-management-blog-members/article-id/5412&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Enforce Mitigation for High & Medium Level Risks in Access Request Management (ARM)](/t5/financial-management-blog-posts-by-members/enforce-mitigation-for-high-medium-level-risks-in-access-request-management/ba-p/13568921)

![GRCwithRaghu](https://avatars.profile.sap.com/7/7/id772587455edc1c5e55b64d4ce19c2eed1722f9d090ea73746ad6211a060eb753_small.jpeg "GRCwithRaghu")

[GRCwithRaghu](https://community.sap.com/t5/user/viewprofilepage/user-id/600573)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=financial-management-blog-members&message.id=5412)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/financial-management-blog-members/article-id/5412)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13568921)

‎2023 Jun 25
2:19 PM

[2
Kudos](/t5/kudos/messagepage/board-id/financial-management-blog-members/message-id/5412/tab/all-users "Click here to see who gave kudos to this post.")

5,148

* SAP Managed Tags
* [Governance, Risk, Compliance (GRC) and Cybersecurity](https://community.sap.com/t5/c-khhcw49343/Governance%252C%2520Risk%252C%2520Compliance%2520%28GRC%29%2520and%2520Cybersecurity/pd-p/237150e2-6555-4a16-b49e-e93dbf1891da)
* [SAP Access Control](https://community.sap.com/t5/c-khhcw49343/SAP%2520Access%2520Control/pd-p/01200615320800000796)
* [SAP Access Control for SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520Access%2520Control%2520for%2520SAP%2520S%252F4HANA/pd-p/73554900100800000773)

* [SAP Access Control

  SAP Access Control](/t5/c-khhcw49343/SAP%2BAccess%2BControl/pd-p/01200615320800000796)
* [SAP Access Control for SAP S/4HANA

  SAP Access Control](/t5/c-khhcw49343/SAP%2BAccess%2BControl%2Bfor%2BSAP%2BS%25252F4HANA/pd-p/73554900100800000773)
* [Governance, Risk, Compliance (GRC) and Cybersecurity

  Product Category](/t5/c-khhcw49343/Governance%25252C%2BRisk%25252C%2BCompliance%2B%252528GRC%252529%2Band%2BCybersecurity/pd-p/237150e2-6555-4a16-b49e-e93dbf1891da)

View products (3)

Access Request Management (ARM) ensures secure and controlled access to sensitive systems and data within organizations. To implement an effective risk management strategy, it is essential to identify and mitigate authorization risks. However, have you ever been required to mitigate only high and medium risks and ignore low ones? This blog discusses a solution to validate and enforce mitigation of high and medium risks in ARM and the importance of mitigating them.

If your requirement is to validate and enforce mitigation of other risk types, the decision table can be tweaked depending on your business requirements.

**Why High & Medium SoD Risks Deserve Priority Attention?**

There are several critical factors that organizations must consider when mitigating high and medium segregation of duties (SoD) risks:

* **Impact on Critical Business Processes**: Often, high and medium SoD risks exist within critical business processes that directly affect an organization's operations, finances, and compliance. A failure to mitigate these risks can lead to severe consequences, such as financial loss, disruptions in operations, and non-compliance with regulatory requirements.

* **Increased Likelihood of Fraud**: High and medium SoD risks are more likely to be exploited by malicious individuals for fraudulent purposes. It involves access to sensitive systems, data manipulation, and control over key financial functions. Leaving these risks unmitigated leaves the organization vulnerable to fraud and compromises its financial integrity.

* **Compliance Requirements**: Due to their impact on financial reporting, data privacy, and security, regulatory frameworks and industry standards often prioritize mitigating high and medium SoD risks. An organization's reputation can be damaged if it does not comply with these requirements. Legal consequences, fines, and penalties can result from non-compliance.

* **Magnitude of Potential Losses**: The potential losses associated with high and medium SoD risks are greater than those associated with low-level risks. Data breaches, unauthorized access, and financial misstatements resulting from these risks can cause significant financial damage, operational disruptions, and irreparable brand damage.

* **Resource Optimization**: Mitigating high and medium SoD risks allows organizations to allocate their limited resources more efficiently. A more efficient allocation of time, budget, and personnel can be achieved by prioritizing the risks that are most likely and have the highest impact.

While low-level SoD risks should not be ignored completely, mitigation efforts should be prioritized based on the likelihood and impact of risks, with high and medium risks being the primary focus to ensure effective risk management within the organization.

Before you start implementing the solution, note that the default mitigation policy in the BRFplus Configuration in SPRO Settings  Governance, Risk and Compliance  Access Control  Maintain AC Applications and BRFplus Function Mapping can be enabled to enforce mitigation of all the risks along with the Task setting “Approve Despite of Risks”. This can be disabled (unchecked) so that the stage owner can’t approve the request.

Removing these will allow the approver to approve any request without a mitigation.

**How to achieve?**

The purpose of creating this BRFplus rule is to determine which risks require mitigation and which risks do not. Ensure that the default BRF+ Mitigation Policy is maintained and associated with MSMP Process ID in SPRO Settings as shown in figure 1.0

![](/legacyfs/online/storage/blog_attachments/2023/06/BRF-Function-ID-Screen-1.png)

Figure 1.0 - BRF Function ID Screen

Copy the Default BRFplus Mitigation Policy Rule ID from the SPRO Settings and open the BRFplus Rule ID in Expert Mode using BRFplus transaction code. (You may need to search it from the existing objects).

**Creating a Decision Table to define the Mitigation Policy Rules**

Under the Function: MITIGATION\_POLICY\_FUNCTION, change the Mode to “Functional and Event Mode” and create the Decision Table in Top Expression, as shown in figure 1.1.

![](/legacyfs/online/storage/blog_attachments/2023/06/Setting-up-Function-Mode-for-MITIGATION_POLICY_FUNCTION.png)

Figure 1.1 – Setting up Function Mode for MITIGATION\_POLICY\_FUNCTION

Once the Function Mode is changed, Click on Top Expression, choose Create, Decision Table and enter the details as shown below in figure 1.2:

![](/legacyfs/online/storage/blog_attachments/2023/06/Decision-Table-definition-screen.png)

Figure 1.2 – Decision Table definition screen

Click “Create And Navigate To Object” and Navigate to Table settings in Decision Table.
Select the Result Data Object as “Mitigate Risk” and define the Condition & Result Columns as shown below and click “OK”....