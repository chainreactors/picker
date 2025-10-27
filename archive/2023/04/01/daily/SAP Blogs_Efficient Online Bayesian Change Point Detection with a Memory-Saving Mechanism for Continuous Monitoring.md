---
title: Efficient Online Bayesian Change Point Detection with a Memory-Saving Mechanism for Continuous Monitoring
url: https://blogs.sap.com/2023/03/31/efficient-online-bayesian-change-point-detection-with-a-memory-saving-mechanism-for-continuous-monitoring/
source: SAP Blogs
date: 2023-04-01
fetch_date: 2025-10-04T11:20:43.256383
---

# Efficient Online Bayesian Change Point Detection with a Memory-Saving Mechanism for Continuous Monitoring

* [SAP Community](/)
* [Developers](/t5/developers/ct-p/developers)
* [Artificial Intelligence](/t5/artificial-intelligence/gh-p/ai)
* [Blogs Posts](/t5/artificial-intelligence-blogs-posts/bg-p/aiblog-board)
* Efficient Online Bayesian Change Point Detection w...

Artificial Intelligence Blogs Posts

All communityThis groupBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/aiblog-board/article-id/295&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Efficient Online Bayesian Change Point Detection with a Memory-Saving Mechanism for Continuous Monitoring](/t5/artificial-intelligence-blogs-posts/efficient-online-bayesian-change-point-detection-with-a-memory-saving/ba-p/13561926)

![former_member732760](https://avatars.profile.sap.com/former_member_small.jpeg "former_member732760")

[former\_member732760](https://community.sap.com/t5/user/viewprofilepage/user-id/732760)

Discoverer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=aiblog-board&message.id=295)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/aiblog-board/article-id/295)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13561926)

‎2023 Mar 31
9:46 PM

[1
Kudo](/t5/kudos/messagepage/board-id/aiblog-board/message-id/295/tab/all-users "Click here to see who gave kudos to this post.")

1,889

* SAP Managed Tags
* [Machine Learning](https://community.sap.com/t5/c-khhcw49343/Machine%2520Learning/pd-p/240174591523510321507492941674121)

* [Machine Learning

  Topic](/t5/c-khhcw49343/Machine%2BLearning/pd-p/240174591523510321507492941674121)

View products (1)

Change point detection in time series data plays a crucial role across various domains. In a previous [blog post](https://blogs.sap.com/2021/03/24/bayesian-change-point-dectection-under-complex-time-series-in-python-machine-learning-client-for-sap-hana/), we showcased the application of Bayesian Change Point Detection using the [Python machine learning client for SAP HANA](https://help.sap.com/doc/1d0ebfe5e8dd44d09606814d83308d4b/2.0.05/en-US/hana_ml.html)(hana-ml). However, this method primarily focuses on analyzing complete time series data, and its robust decomposition capabilities can demand significant computational resources. To address the increasing need for continuous monitoring and efficient change point identification in time series data, we are thrilled to introduce our novel approach: Online Bayesian Change Point Detection with Memory-Saving Mechanism.

In this blog post, you will learn:

* How does the memory-saving mechanism work.

* How to apply online change point detection in hana-ml to extract the change point continuously.

# Introduction

Contrary to the offline version, online Bayesian change point detection does not rely on decomposition techniques. It emphasizes causal predictive filtering, a method that generates an accurate distribution of the upcoming, unseen data point in the sequence using only the information from previously observed data.

In conventional methods for continuous change point detection in the incoming time series, we rely on models that incorporate the entire historical dataset. However, this approach leads to a significant issue: as the volume of data increases, the model size grows excessively large, requiring substantial time to read and output the model repeatedly in a tabular format. Consequently, this method becomes inefficient for online scenarios.

Based on our experiments, we have determined that an efficient strategy is to remove all historical data before the most recent change point. In the upcoming section, we will provide step-by-step instructions on implementing this approach with two datasets—one originating from a simulated scenario and the other from a real-world example.

# Examples

All source code in examples of the following context will use [Python machine learning client](https://help.sap.com/doc/1d0ebfe5e8dd44d09606814d83308d4b/2.0.05/en-US/hana_ml.html) for [SAP HANA Predictive Analsysi Library(PAL)](https://help.sap.com/docs/HANA_CLOUD_DATABASE/319d36de4fd64ac3afbf91b1fb3ce8de/c9eeed704f3f4ec39441434db8a874ad.html).

## Connect to SAP HANA

```
import hana_ml

from hana_ml import dataframe

cc = dataframe.ConnectionContext(address='', port=30x15, user='', password='')#account details omitted
```

### Use Case I:  Mocking Data

In this use case, we will focus on continuously detecting the change points in the mocking data.

![](/legacyfs/online/storage/blog_attachments/2023/03/mocking_data.png)

The simulated dataset consists of two segments: the first segment has a length of 40, and the second spans 60 units. These segments are separated by a red vertical line in the graph. The data is stored in two separate database tables named 'PAL\_ONLINE\_BCPD\_MOCK\_TBL\_PART1' and 'PAL\_ONLINE\_BCPD\_MOCK\_TBL\_PART2'. To create corresponding hana\_ml.DataFrame objects for these tables, we can utilize the table() function of the ConnectionContext.

```
mocking_df_part1 = cc.table('PAL_ONLINE_BCPD_MOCK_TBL_PART1')

mocking_df_part2 = cc.table('PAL_ONLINE_BCPD_MOCK_TBL_PART2')
```

First, we create two OnlineBCPD objects: one with the memory-saving feature and another without it. This is managed by a parameter called 'prune':

```
from hana_ml.algorithms.pal.tsa.changepoint import OnlineBCPD

obcpd_with_prune    = OnlineBCPD(threshold=0.5, prune=True)

obcpd_without_prune = OnlineBCPD(threshold=0.5, prune=False)
```

Then we use them to find the change points in the first part:

```
model_with_prune, cp_part1_with_prune = obcpd_with_prune.fit_predict(data=conn.table("PAL_ONLINE_BCPD_MOCK_TBL_PART1"), model=None)

model_without_prune, cp_part1_without_prune = obcpd_without_prune.fit_predict(data=conn.table("PAL_ONLINE_BCPD_MOCK_TBL_PART1"), model=None)
```

And we will get two output tables from each OnlineBCPD object, let's print the length of each model:

```
print("The length of the model with prune is {}\nand the legnth of model without prune is {}".format(len(model_with_prune.collect()), len(model_without_prune.collect())))
```

The *collect()* function of *hana\_ml.DataFrame* can help to fetch data from database and you will see the output like this:

### ![](/legacyfs/online/storage/blog_attachments/2023/03/Screenshot-2023-03-29-at-13.23.25.png)

By setting 'prune=True', the model will consume less memory while executing the algorithm.

Afterwards, we print the change point table:

```
print(cp_part1_with_prune.collect())

print(cp_part1_without_prune.collect())
```

and we will see the output like this:

![](/legacyfs/online/storage/blog_attachments/2023/03/Screenshot-2023-03-29-at-13.27.08.png)

which shows that the results are the same under both settings regarding parameter 'prune'.

Further, we are to use the pruned model to detect the second part:

```
model_with_prune, cp_part2 = obcpd_with_prune.fit_predict(data=conn.table("PAL_ONLINE_BCPD_MOCK_TBL_PART2"), model=model_with_prune)

print(cp_part2.collect())
```

The results should be like this:

![](/legacyfs/online/storage/blog_attachments/2023/03/Screenshot-2023-03-29-at-13.39.53.png)

Finally, we plot all the change points in the original graph by orange vertical lines:

![](/legacyfs/online/storage/blog_attachments/2023/03/9c482cc8-7a5b-449c-b464-c0b53116f02e.png)

It's done! All the change points in two continuous segements have be detected.

### Use Case II: Real World Sensor Data

In this example, we hav...