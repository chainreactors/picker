---
title: Understanding Classification with Smart Predict
url: https://blogs.sap.com/2023/03/01/understanding-classification-with-smart-predict/
source: SAP Blogs
date: 2023-03-02
fetch_date: 2025-10-04T08:26:38.367189
---

# Understanding Classification with Smart Predict

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Understanding Classification with Smart Predict

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/159844&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Understanding Classification with Smart Predict](/t5/technology-blog-posts-by-members/understanding-classification-with-smart-predict/ba-p/13548502)

![Rasmus](https://avatars.profile.sap.com/c/2/idc2561fe8d71c71578ed33939173867b7a18a405e9d489aced0b7a838d913adcb_small.jpeg "Rasmus")

[Rasmus](https://community.sap.com/t5/user/viewprofilepage/user-id/147073)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=159844)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/159844)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13548502)

‎2023 Mar 01
10:52 PM

[10
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/159844/tab/all-users "Click here to see who gave kudos to this post.")

2,053

* SAP Managed Tags
* [SAP Analytics Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Cloud/pd-p/67838200100800006884)
* [SAP Analytics Cloud for planning](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Cloud%2520for%2520planning/pd-p/819703369010316911100650199149950)

* [SAP Analytics Cloud

  SAP Analytics Cloud](/t5/c-khhcw49343/SAP%2BAnalytics%2BCloud/pd-p/67838200100800006884)
* [SAP Analytics Cloud for planning

  Software Product](/t5/c-khhcw49343/SAP%2BAnalytics%2BCloud%2Bfor%2Bplanning/pd-p/819703369010316911100650199149950)

View products (2)

![](/legacyfs/online/storage/blog_attachments/2023/02/0_banner_final-1.png)

In this blog post, I will explain the machine learning algorithms underlying classification in SAC Smart Predict. The focus will be on building the theoretical framework necessary to truly understand the output produced within SAP Analytics Cloud.

Martin Bregninge's previous post, ‘[Understanding Regression with Smart Predict’](https://blogs.sap.com/2022/05/04/towards-a-visual-understanding-of-regression-with-sac-smart-predict/), shares many similarities with this one, but we have intentionally written both posts to be read and understood independently of the other.

If you have already read the regression-post, many of the concepts discussed here will be familiar to you already. I have included small boxes like this one, describing sections that can be skipped, and providing additional insight by comparing classification to regression.

## The Point of Classification

This section should not be skipped. Note that the setup for classification is the same as regression, except that our target value is a binary dimension instead of a measure.

*Classification* is the task of sorting objects into categories (or *classes*), based on the known values of some *influencer variables* that describe the objects. For example, classification can help us answer such questions as:

+ **“Is this employee in danger of leaving the company?”**

+ **“Is this item from our manufacturing plant faulty?”**

+ **“Is this potential customer going to be interested in our services and thus receptive to our marketing?**

Influencer variables can be both *dimensions* (nominal variables such as the gender of a potential customer) and *measures* (numerical variables such as the temperature at which an item was manufactured). The *target value* must be a dimension, and each possible member of the dimension corresponds to a different category that the object can belong to.

You might notice that all the examples I’ve given are ‘yes/no’-questions – in other words, the target value can only take on two distinct values, such as ‘faulty’ or ‘not faulty’.

I have limited myself to these examples because the algorithm used by SAC Smart Predict performs *binary* classification; we cannot sort objects into more than two categories. Serious as this limitation may seem, it has its benefits. For one, it allows us to easily estimate the probability of belonging to each category (we’ll see how in a minute!) rather than just giving a deterministic classification. If we wish to classify many objects, we can thus sort them in order of probability, allowing us to reformulate our questions slightly:

+ **“Which of our employees are most likely to leave the company?”**

+ **“Which items from our manufacturing plant are most likely to be faulty?”**

+ **“Which potential customers are most likely to be receptive of our marketing?”**

## The Idea Behind Classification

This section can be skipped. In short: We will try to find a function which gives the probability that a certain input belongs to class 1 rather than class 0. Our final classification is based on this probability. Figure 2 illustrates how the classification problem can be reframed as a regression problem.

Throughout this blog post, I will return to the example of using influencer variables *age* and *income* to predict which potential customers are most likely to be receptive to our marketing.

To make our predictions, we will need a large set of labeled training data: people for which we know the influencer variables, and whether they are marketing-receptive or not. We might plot our training data as shown in figure 1(a).

Our goal will be to determine a function, *f*, which – given the *age* and *income* of a person – outputs an estimate of the probability that this person is marketing-receptive. For our toy dataset, one possible function is shown by the background color in figure 1(b). It should be clear for us as humans that this is a reasonable choice of the probability function. In the section on Maximum Likelihood, we will define formally what constitutes the ‘best’ choice, so that a computer can understand it.

For now, just note that (almost) all the marketing-receptive customers are predicted to be likely to be marketing-receptive, and similarly for the unreceptive customers. The model lines up well with reality, so it seems reasonable to expect that it will also make good predictions in new cases.

From the probability function, we can create a *decision boundary* (the black lines in figure 1(b)) which is used to perform the final classification. The decision is made by asking if the probability of being class 1 is above some threshold (in this case 50%).

![](/legacyfs/online/storage/blog_attachments/2023/02/1_Points-1.png)

*Figure 1(a):* *Our training dataset contains 150 people. We know their age, their monthly income, and whether they are marketing-receptive customers or not.*

![](/legacyfs/online/storage/blog_attachments/2023/02/2_Decision_Boundary-2.png)

*Figure 1(b): A reasonable probability function and decision boundary. We will predict customers to be receptive if they are within one of the red areas. Note that not every point is correctly classified – that won’t always be possible.*

Instead of using the background color to represent the probability *f*(***x***) (as in figure 1(b)), we could use a third axis*,* as shown in figure 2. We also group the training examples along the n...