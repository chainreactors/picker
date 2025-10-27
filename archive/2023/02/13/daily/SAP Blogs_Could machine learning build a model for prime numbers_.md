---
title: Could machine learning build a model for prime numbers?
url: https://blogs.sap.com/2023/02/12/could-machine-learning-build-a-model-for-prime-numbers/
source: SAP Blogs
date: 2023-02-13
fetch_date: 2025-10-04T06:27:59.075190
---

# Could machine learning build a model for prime numbers?

* [SAP Community](/)
* [Groups](/t5/groups/ct-p/groups)
* [Interest Groups](/t5/interest-groups/ct-p/interests)
* [Application Development and Automation](/t5/application-development-and-automation/gh-p/application-development)
* [Blog Posts](/t5/application-development-and-automation-blog-posts/bg-p/application-developmentblog-board)
* Could machine learning build a model for prime num...

Application Development and Automation Blog Posts

Learn and share on deeper, cross technology development topics such as integration and connectivity, automation, cloud extensibility, developing at scale, and security.

All communityThis groupBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/application-developmentblog-board/article-id/47300&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

#### We have launched new [Developer forums/groups](https://community.sap.com/t5/developers/ct-p/developers) in the SAP Community. If you are here to publish developer- or SAP-technology related blog posts, please check out our new groups instead. You can find more information about the developer forums in this [What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147).

Read only

## [Could machine learning build a model for prime numbers?](/t5/application-development-and-automation-blog-posts/could-machine-learning-build-a-model-for-prime-numbers/ba-p/13565895)

![Sergiu](https://avatars.profile.sap.com/6/6/id666110d2809f26186859acb7fa943251af0e5f23a6fdb99098d163da3650c006_small.jpeg "Sergiu")

[Sergiu](https://community.sap.com/t5/user/viewprofilepage/user-id/43076)

Contributor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=application-developmentblog-board&message.id=47300)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/application-developmentblog-board/article-id/47300)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13565895)

‎2023 Feb 12
11:32 AM

[3
Kudos](/t5/kudos/messagepage/board-id/application-developmentblog-board/message-id/47300/tab/all-users "Click here to see who gave kudos to this post.")

2,498

* SAP Managed Tags
* [Machine Learning](https://community.sap.com/t5/c-khhcw49343/Machine%2520Learning/pd-p/240174591523510321507492941674121)
* [Python](https://community.sap.com/t5/c-khhcw49343/Python/pd-p/f220d74d-56e2-487e-8e6c-a8cb3def2378)
* [Artificial Intelligence](https://community.sap.com/t5/c-khhcw49343/Artificial%2520Intelligence/pd-p/c3c3a408-33ea-4c2a-ae6f-05461e76982d)

* [Machine Learning

  Topic](/t5/c-khhcw49343/Machine%2BLearning/pd-p/240174591523510321507492941674121)
* [Artificial Intelligence

  Product Category](/t5/c-khhcw49343/Artificial%2BIntelligence/pd-p/c3c3a408-33ea-4c2a-ae6f-05461e76982d)
* [Python

  Programming Tool](/t5/c-khhcw49343/Python/pd-p/f220d74d-56e2-487e-8e6c-a8cb3def2378)

View products (3)

When we think about a prime number we do it in terms of divisibility properties.

[**Wikipedia**](https://en.wikipedia.org/wiki/Prime_number). A prime number (or a prime) is a natural number greater than 1 that is not a product of two smaller natural numbers. A natural number greater than 1 that is not prime is called a composite number.

I participated in the [SAP HANA ML Challenge – Employee Churn](https://blogs.sap.com/2022/11/07/sap-community-call-sap-hana-cloud-machine-learning-challenge-i-quit-how-to-prevent-employee-churn/) ![:robot_face:](/html/@B0226AE784E14A7D818BCDB1442049A2/emoticons/1f916.png ":robot_face:") and I came in [second place](https://blogs.sap.com/2022/12/22/sap-hana-cloud-machine-learning-challenge-2022-the-winners-are/) ![:trophy:](/html/@941BA57C60D60715FBDFDADC4079725D/emoticons/1f3c6.png ":trophy:").
Discover [**the blog**](https://blogs.sap.com/2023/01/09/sap-hana-cloud-machine-learning-challenge-i-quit-understanding-metrics/) I wrote about the challenge and the solution.

The classification stuck in my head for a while and then one day the prime number problem popped up. ![:light_bulb:](/html/@FF87431363E2E23D7F621C3734E062B4/emoticons/1f4a1.png ":light_bulb:")

Machine learning doesn't solve all problems, but it's worth exploring if it can.

[**Lex Fridman post:**](https://www.linkedin.com/feed/update/urn%3Ali%3Aactivity%3A7028046139127959552)

"Humans are an API to ChatGPT.
ChatGPT is an API to Python.
Python is an API to C.
C is an API to assembly.
Assembly is an API to binary.
***Binary is an API to physics.***
Physics is an API to the machine that runs the universe.

It's computation all the way down."

Can we express the prime number property as a classification problem?

## Table of content

[1. Intervals with prime numbers](#cp01)
[2. Intervals with the last digit of the prime](#cp02)
[3. Conversion of class into binary](#cp03)
[4. Conversion of intervals into binary](#cp04)
[5. Splitting binary intervals into columns](#cp05)
[6. Reorganizing data with sliding windows](#cp06)
[7. Building the models with sliding windows](#cp07)
[7.1 Model classification report](#cp08)
[7.2 Model confusion matrix](#cp09)
[7.3 Prediction classification report](#cp10)
[7.4 Prediction confusion matrix](#cp11)
[8. Building models with a validation data set](#cp12)
[8.1 Model classification report](#cp13)
[8.2 Model confusion matrix](#cp14)
[8.3 Prediction classification report](#cp15)
[8.4 Prediction confusion matrix](#cp16)
[8.5 Model performance](#cp17)
[9. Building models with early stopping](#cp18)
[9.1 Model classification report](#cp19)
[9.2 Model confusion matrix](#cp20)
[9.3 Prediction classification report](#cp21)
[9.4 Prediction confusion matrix](#cp22)
[9.5 Model performance](#cp23)
[10. Conclusion and further steps](#cp24)
[11. Building LSTM model with sliding windows](#cp25)

In the blog, I will only go through the main parts. The entire [code is on GitHub](https://github.com/itsergiu/ml-prime-numbers/blob/main/ml%20prime%20number%20v2.0.ipynb), published with my last run.

# 1. Intervals with prime numbers

Let’s try the re-definition of a prime number as a classification problem in binary form.

A prime number could end with [1, 3, 7, 9].  Examples by intervals:

In the interval from 10 to 19 primes are: 11, 13, 17, 19

In the interval from 20 to 29 primes are 23, 29.

```
1->[11, 13, 17, 12]

2->[23, 29]
```

# 2. Intervals with the last digit of the prime

The combination [1, 3, 7, 9] is the pattern the class I have to predict.

```
1->[1, 3, 7, 9]

2->[3, 9]
```

# 3. Conversion of class into binary

If prime 1, else 0.

```
1->[1, 1, 1, 1]

2->[0, 1, 0, 1]
```

# 4. Conversion of intervals into binary

Conversion of class as a list into a string.

```
00000000000001->1111

00000000000010->0101
```

# 5. Splitting binary intervals into columns

```
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]->[1111]

[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]->[0101]
```

# 6. Reorganizing data with sliding windows

That shifts the previous interval and previous prime class. The [sliding window](https://machinelearningmastery.com/xgboost-for-time-series-forecasting/) can include any number of subsequent previous rows.

```
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]->[1111]

[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1], # previous row

[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]->[0101] # current row and class to predict
```

# 7. Building the models with sliding windows

Fit with all train data without a validation data set

```
# In 93:

%%time

n_shifts = 24

for i_shift in range(1, n_shifts):
```

```
# Out 93:

model score: 0.521 prediction score: 0.250 shift: 001     (9983, 14) (16, 14) (9983,) (16,)

model score: 0.730 prediction score: 0.375 shift: 002     (998...