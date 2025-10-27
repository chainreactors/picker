---
title: Situation Handling – Case Notification for Managing Financial Transactions
url: https://blogs.sap.com/2022/12/02/situation-handling-case-notification-for-managing-financial-transactions/
source: SAP Blogs
date: 2022-12-03
fetch_date: 2025-10-04T00:23:30.201454
---

# Situation Handling – Case Notification for Managing Financial Transactions

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Situation Handling – Case Notification for Managin...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/162979&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Situation Handling – Case Notification for Managing Financial Transactions](/t5/technology-blog-posts-by-sap/situation-handling-case-notification-for-managing-financial-transactions/ba-p/13565672)

![betty_guedez](https://avatars.profile.sap.com/6/4/id6449d6b8141a821fda645f6ef666e242a6846bcdd6a775b0bbf0f3c3330f5b69_small.jpeg "betty_guedez")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[betty\_guedez](https://community.sap.com/t5/user/viewprofilepage/user-id/329280)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=162979)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/162979)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13565672)

‎2022 Dec 02
10:59 PM

[11
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/162979/tab/all-users "Click here to see who gave kudos to this post.")

2,240

* SAP Managed Tags
* [Situation Handling](https://community.sap.com/t5/c-khhcw49343/Situation%2520Handling/pd-p/db4786c7-74ce-4e4a-91f2-027a57fa3921)
* [SAP Fiori for SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori%2520for%2520SAP%2520S%252F4HANA/pd-p/73555000100800000131)
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)
* [SAP S/4HANA Cloud Private Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Private%2520Edition/pd-p/5c26062a-9855-4f39-8205-272938b6882f)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)
* [SAP Fiori for SAP S/4HANA

  SAP Fiori](/t5/c-khhcw49343/SAP%2BFiori%2Bfor%2BSAP%2BS%25252F4HANA/pd-p/73555000100800000131)
* [Situation Handling

  Additional Software Product](/t5/c-khhcw49343/Situation%2BHandling/pd-p/db4786c7-74ce-4e4a-91f2-027a57fa3921)
* [SAP S/4HANA Cloud Private Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPrivate%2BEdition/pd-p/5c26062a-9855-4f39-8205-272938b6882f)

View products (4)

**Product Information**

**Betty Guedez**

**December 2nd 2022**

**Situation Handling – Case Notification for Managing Financial Transactions**

**Updated as of releases****SAP S/4HANA 2022 and******SAP S/4HANA Cloud 2208****

Hello there!

I am Betty Guedez, Finance Product Expert at SAP S/4HANA RIG and I come back today with another Situation Handling scenario, this time of interest to Treasury and Risk Management Back Office and Front Office responsible teams.

For those who interact with Treasury, Financial Investments and Market Rates, uncertainty is a feeling they would prefer not to have in a million years. In fact, receiving precise information of any fact that can have any kind of influence in the value of a financial asset is critical. The difference between a big gain and the most dramatic loss could be an event that was missed or underestimated.

Today we will use a typical example of a Spot Forex Transaction.

This is one of the most popular financial transactions in a Treasury department. Typical steps on an operation like this are as follows:

. Once availability for financial investments has been determined, a front office clerk seeks and finds rates, conditions and in general, terms that apply to the transaction. Chooses the one that suits better the financial policy and proceeds to close the deal, creating a For Ex transaction in the system.

. A confirmation letter (or deal ticket) is usually exchanged between parties. There could also be an internal letter issued at this point, for audit and control purposes. Sometimes, correspondences are handled by another clerk, especially when volumes are high.

. Now, the sooner the better, a Back Office clerk proceeds to review the conditions (rate, amounts, delivery date) and settles the transaction (this is usually assumed as a verification step). Once settled, the transaction is ready for the next step, which is posting to G/L.

. A payment clerk is usually in charge of processing payment requests and bank mandates, as agreed on the confirmation letter.

Depending on the company size and liquidity level, portfolio rules and market offer, the number of   transactions to process in the system could be high. Bear in mind that in Treasury departments, running against time is part of daily life.

As there are people in different roles (and probably different locations as well) taking part in the end-to-end process of a financial agreement like this, an automated way to notify everybody when they need to take actions with one (or many) transaction is of great help in a hectic dynamic of a Treasury department.

Does the scope of actions that can be taken include more activities than sending Correspondences, Review and Settle contracts, trigger Payments Requests?

Yes, it does. A financial transaction is a deal where periodic activities must also be executed, to receive funds, to make payments and so on. Financial investments also have a lifetime cycle with maturities that need to be handled in time, as well.

Also, period end closing adds more tasks to this business process.

Is it a Business Workflow the only way to keep everybody aware that there are transactions waiting for an action?

No, there are also some other options that fall into the Intelligent Technologies category and Situation Handling belongs to this set of tools.

What do we have in Situation Handling for this?

Starting SAP S/4HANA Cloud 2208, we have more scenarios to cover different needs in a variety of business scenarios.

The new template FIN\_TRM\_FINTRANS\_PROCG is available in the Manage Situation Types app and allows configuration experts to create a new situation type, to inform specific groups of users when a financial transaction requires their action, like Settlement, Posting, Expiration, Maturity.

![](/legacyfs/online/storage/blog_attachments/2022/12/Notifications-on-My-Home-screen.png)

Notifications on My Home

How do we activate these notifications?

Situation Template FIN\_TRM\_FINTRANS\_PROCG (Category FSCM\_TRM) is the one to configure to receive these notifications in our Fiori Launchpad.

First, access Fiori app [F2412 Manage](https://fioriappslibrary.hana.ondemand.com/sap/fix/externalViewer/#/detail/Apps('F2412')/S22OP) [Teams and Responsibilities](https://fioriappslibrary.hana.ondemand.com/sap/fix/externalViewer/#/detail/Apps('F2412')/S22OP) in which you will define who will receive alerts on this business activity.

On the first screen, hit Create.

Creation screen is now displayed. Proceed assigning a name to your Team

![](/legacyfs/online/storage/blog_attachments/2022/12/Manage-Teams-and-Responsibilities-Initial-1.png)

Manage Teams and Responsibilities - Definition

Let’s say our receivers are Back Office guys, that need to be notified every ...