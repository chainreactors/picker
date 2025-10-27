---
title: “Keep the core clean” statement considered harmful
url: https://blogs.sap.com/2023/05/05/keep-the-core-clean-statement-considered-harmful/
source: SAP Blogs
date: 2023-05-06
fetch_date: 2025-10-04T11:40:21.267649
---

# “Keep the core clean” statement considered harmful

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* "Keep the core clean" statement considered harmful

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/68449&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## ["Keep the core clean" statement considered harmful](/t5/enterprise-resource-planning-blog-posts-by-members/quot-keep-the-core-clean-quot-statement-considered-harmful/ba-p/13568928)

![woutdejong](https://avatars.profile.sap.com/9/5/id95b0d2a2a931104f6096a1576a3b3b5a25ed64aaff5938185b2dbfaed4c37a07_small.jpeg "woutdejong")

[woutdejong](https://community.sap.com/t5/user/viewprofilepage/user-id/90887)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=68449)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/68449)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13568928)

‎2023 May 05
5:09 PM

[40
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/68449/tab/all-users "Click here to see who gave kudos to this post.")

12,203

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)
* [ABAP Extensibility](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Extensibility/pd-p/338571334339306322581424656448659)
* [SAP ERP Central Component](https://community.sap.com/t5/c-khhcw49343/SAP%2520ERP%2520Central%2520Component/pd-p/01200314690800000122)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)

* [SAP ERP Central Component

  SAP ERP](/t5/c-khhcw49343/SAP%2BERP%2BCentral%2BComponent/pd-p/01200314690800000122)
* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)
* [ABAP Extensibility

  Programming Tool](/t5/c-khhcw49343/ABAP%2BExtensibility/pd-p/338571334339306322581424656448659)

View products (4)

[![](/legacyfs/online/storage/blog_attachments/2023/05/go-to-statement-considered-harmful.png)](https://dl.acm.org/doi/10.1145/362929.362947)

The over-simplified interpretation of "keep the core clean" is considered harmful. Nowadays I still hear a lot of SAP and non-SAP people state that all **custom ABAP code** is polluting the SAP ERP (ECC, S/4) application and should be cleaned, that is, removed or moved somewhere else.

Dogmatically deciding to move custom (ABAP) code elsewhere is a bad and outright costly idea.

Thinking critically how to automate, optimize and/or standardize your processes to achieve business goals in an economically viable way is a good idea, and always has been. This includes what IT tools/capabilities to employ (like custom ABAP code or BTP or new applications and many, many others). But also to look beyond IT at changing the system as a whole, for example modifying subsystems like the organization itself (departments, in- and outsourcing) and the execution of its processes.

Yes, there are trade-offs… Aren't there always?

Fortunately, this nuanced view is already expressed in most blogs about "keep the core clean" out there, ever since former SAP CTO Björn Goerke spoke those (in)famous words on TechEd 2018.

This blog is going to follow that nuanced trend, although it won't look like that at first. Let’s explore "clean core" and its over-simplified interpretation by outlining the context, arguments and consequences. Secondly, I will discuss the nuanced view of SAP (and many others), which SAP-Marketing cannot translate one-on-one into "for custom code, buy more BTP Cloud". All this combined might make you (re?)consider the usefulness of the "clean core"-mantra.

In the initial draft of this blog, I provided too much detail, for example on trade-offs and characteristics (-ilities). In the (near) future, in a follow-up blog I will put in detailed considerations on -ilities and trade-offs, and maybe an architectural fitness function, just plainly ignoring the "clean core"-catchphrase. That will be a lot more boring and theoretical to read, I promise. ![:slightly_smiling_face:](/html/@AB1AFF728742E596A69993DB64EECECF/emoticons/1f642.png ":slightly_smiling_face:")

### The Stage

So what does "keep the core clean" mean?

Some (journalists, analysts, a few SAP-employees, partner employees) have defined/described it as "back to standard application, no over-customization in that application". ChatGPT (version 20230323) describes it as "keeping the central system, or 'core', of an SAP installation as free of customizations as possible", which is a good summary of what was out there on the internet on this topic until the end of 2021. Oh, and for all the ancient SAP consultants (me included) out there, here is some typical SAP-naming-confusion: the SAP-term "customizing" (tcode SPRO) has to do with *configuring* the existing features of an SAP application, while the term "customization" applies to *developing/modifying* features yourself in an application (custom code).

So let me make it a bit more concrete. Here is my interpretation of "core" in the SAP ERP context: it is all software (code) that runs inside the *application boundary* (**AB**) of the ABAP  runtime of S/4, ECC, R/3.

(I'd like to be more precise, ie all objects in ABAP-table TADIR of SAP ERP, but there are some exceptions. For clarity I leave the (HANA-)database runtimes (HDI, or the old repo), and the UI-runtimes (like browser, SAPgui, apps) and designtime-tooling outside this boundary, but with extra cognitive effort these can be incorporated just as well. Higher-level-frameworks and executable models like Workflow and BRF+ are actually part of the AB, although this eventually might end up in philosophical discussions about "configuration" vs "customization" or "what is code?".)

Everything developed inside the AB by the *SAP-company* is considered "clean" according to the over-simplified interpretation above. Customer developed code inside the AB is considered "dirty"; these are all the customizations running inside the AB. I'm not sure where that leaves SAP-certified 3rd-party-addons, let's leave that out for now. So hence the over-simplified statement that started this blog. Hold your horses, I get to the nuanced part later…

Some SAP-customers even take the "clean core" concept a step further by not differentiating on who made the code. These customers have migrated away entirely from applications inside the AB of SAP ERP to "keep the core clean" ("scrape the core clean"?) . For example, a customer can move away from the SAP ERP SD module (Sales & Distribution) to a custom built sales app (or some SaaS-app) and integrate with the SAP "core" application. Maybe SAP itself is cleaning the core, look at SAP HCM (Human Capital Mgmt, aka HR). SAP sort of mostly placed this outside the "core" with its SuccessFactors SaaS (with HR-mini-master inside the "core"-AB to satisfy dependencies of other "core" modules, like Timesheets for example. The results at this ti...