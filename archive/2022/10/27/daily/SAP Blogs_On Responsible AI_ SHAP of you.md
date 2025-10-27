---
title: On Responsible AI: SHAP of you
url: https://blogs.sap.com/2022/10/26/on-responsible-ai-shap-of-you/
source: SAP Blogs
date: 2022-10-27
fetch_date: 2025-10-03T21:00:22.770955
---

# On Responsible AI: SHAP of you

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* On Responsible AI: SHAP of you

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160658&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [On Responsible AI: SHAP of you](/t5/technology-blog-posts-by-members/on-responsible-ai-shap-of-you/ba-p/13553641)

![leojmfrancia60](https://avatars.profile.sap.com/5/7/id5718db71ef1a48c6bd7b78e9f4396e71c41e127a0197ae32522cfb69e243122e_small.jpeg "leojmfrancia60")

[leojmfrancia60](https://community.sap.com/t5/user/viewprofilepage/user-id/40845)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160658)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160658)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13553641)

‎2022 Oct 27
12:42 AM

[8
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160658/tab/all-users "Click here to see who gave kudos to this post.")

1,921

* SAP Managed Tags
* [Machine Learning](https://community.sap.com/t5/c-khhcw49343/Machine%2520Learning/pd-p/240174591523510321507492941674121)
* [SAP Analytics Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Cloud/pd-p/67838200100800006884)
* [SAP Data Intelligence](https://community.sap.com/t5/c-khhcw49343/SAP%2520Data%2520Intelligence/pd-p/73555000100800000791)
* [SAP HANA Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%2520Cloud/pd-p/73554900100800002881)
* [Artificial Intelligence](https://community.sap.com/t5/c-khhcw49343/Artificial%2520Intelligence/pd-p/c3c3a408-33ea-4c2a-ae6f-05461e76982d)
* [SAP AI Core](https://community.sap.com/t5/c-khhcw49343/SAP%2520AI%2520Core/pd-p/73554900100800003641)
* [SAP HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA/pd-p/73554900100700000996)

* [SAP Analytics Cloud

  SAP Analytics Cloud](/t5/c-khhcw49343/SAP%2BAnalytics%2BCloud/pd-p/67838200100800006884)
* [SAP HANA

  Software Product](/t5/c-khhcw49343/SAP%2BHANA/pd-p/73554900100700000996)
* [Machine Learning

  Topic](/t5/c-khhcw49343/Machine%2BLearning/pd-p/240174591523510321507492941674121)
* [SAP Data Intelligence

  SAP Data Intelligence](/t5/c-khhcw49343/SAP%2BData%2BIntelligence/pd-p/73555000100800000791)
* [Artificial Intelligence

  Product Category](/t5/c-khhcw49343/Artificial%2BIntelligence/pd-p/c3c3a408-33ea-4c2a-ae6f-05461e76982d)
* [SAP HANA Cloud

  Software Product](/t5/c-khhcw49343/SAP%2BHANA%2BCloud/pd-p/73554900100800002881)
* [SAP AI Core

  SAP Business AI](/t5/c-khhcw49343/SAP%2BAI%2BCore/pd-p/73554900100800003641)

View products (7)

**Interesting fact:** [SHAP](https://shap.readthedocs.io/en/latest/index.html) (more on this below) and Ed Sheeran's "Shape of you" (needs no introduction) were both released in 2017.

**An even more interesting fact:** [Christian Klein recently spoke about Responsible AI](https://www.linkedin.com/posts/business-roundtable_responsible-ai-christian-klein-ceo-member-activity-6985682816365649920-yd89?utm_source=share&utm_medium=member_desktop), emphasizing that while AI addresses the greatest challenges of our time like carbon footprint minimization and scaling of aid, we need to ensure that it is used in a fair, transparent, and compliant way. You can find more details on [SAP's Global AI Ethics Policy here](https://www.sap.com/documents/2022/01/a8431b91-117e-0010-bca6-c68f7e60039b.html).

This blog might be interesting to you if:

* You want to read more about responsible AI, and how it can be delivered through explainable AI

* You would like to see some examples and watch-outs in using explainable AI, specifically SHAP (more on this below)

* Most importantly, you are curious how you can use and extend SHAP explanations in enterprise use cases

### 1. Explainability Explained

Explainable AI can be defined as being able to understand the predictions made by AI. A sample case is being able to see why a predictive model has assessed that a group of students will most likely fail the school year based on assessments of school work, attendance, background, etc. Responsible AI, on the other hand, is **identifying** what could go wrong **early** in the design phase, i.e. a [premortem](https://en.wikipedia.org/wiki/Pre-mortem). Back to the student example, the initial use case can cause discrimination or even worsen the situation for the student; the use case can be changed into an automated creation of study materials or activities that students may consider to improve their grades. Explainable AI can also be responsible AI when values such as sustainability and human-centric design are considered early in the process.

There are tools that provide [explainable AI](https://en.wikipedia.org/wiki/Explainable_artificial_intelligence), with **[SHAP](https://shap.readthedocs.io/en/latest/index.html)** (SHapley Additive exPlanations) being one of the approaches in identifying correlations/explanations on outcomes of predictions. With SHAP, think about each output of a prediction as a **game** with variables (e.g. duration, quantity, frequency, etc.) as the **players**. The SHAP output for an observation shows which players made the most impact on the game result (e.g. in a positive or negative in a binary classification).

An example of a SHAP plot can be seen below on customer churn, i.e. if a customer will discontinue their phone plans (image credit: [Yifei Huang](https://towardsdatascience.com/demystify-your-ml-model-with-shap-fc191a1cb08a)). You can click on the image to enlarge the text. In summary, the SHAP plot shows:

* Scaled values (0 as lowest, 1 as highest) of the variables in the dataset, i.e. pink for high and blue for low. For example, if total\_day\_charge has 100 as the highest, it will be plotted as a pink dot in and if the lowest value is 1, it will be plotted as a blue dot. Values in-between will follow the color gradient shown on the right

* Variable values that influence churn, by looking at the dots on the positive X-axis (on the right)

* Variable values that influence not churning, by looking at the dots on the negative X-axis (on the left)

* **As an example, high values of total\_day\_charge (pink dots) are correlated to customer churn (plotted on the right, positive X-axis)**

![](/legacyfs/online/storage/blog_attachments/2022/10/SHAP-Sample-5.png)

Sample SHAP plot

There are great SAP Blogs that talk about SHAP in technical detail (see section 3). The remainder of this blog talks about the implications of using SHAP and our responsibility to build on top of it to provide the best outcome to our customers and achieve responsible AI.

So how *does* SHAP help in achieving responsible AI?

### 2. Explainability Encountered

When I was working on a customer churn business problem for a global business, one of the initial models we created had country and region as the variables. We anticipated that this would be an issue; as anecdotally, we have observed that one region showed high churn rates. With our suspicions backed by our testing, we removed variables such as country and region as these are areas ...