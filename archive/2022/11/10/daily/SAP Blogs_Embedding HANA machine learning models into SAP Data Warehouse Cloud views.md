---
title: Embedding HANA machine learning models into SAP Data Warehouse Cloud views
url: https://blogs.sap.com/2022/11/09/embedding-hana-machine-learning-models-into-sap-data-warehouse-cloud-views/
source: SAP Blogs
date: 2022-11-10
fetch_date: 2025-10-03T22:14:56.540793
---

# Embedding HANA machine learning models into SAP Data Warehouse Cloud views

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Embedding HANA machine learning models into SAP Da...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/163201&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Embedding HANA machine learning models into SAP Data Warehouse Cloud views](/t5/technology-blog-posts-by-sap/embedding-hana-machine-learning-models-into-sap-data-warehouse-cloud-views/ba-p/13566332)

![stojanm](https://avatars.profile.sap.com/3/6/id361ce097c67aeeea5eac3b8a55380f6f0a6285fe2f96b2e8b16f9cdc4a450d69_small.jpeg "stojanm")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[stojanm](https://community.sap.com/t5/user/viewprofilepage/user-id/39047)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=163201)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/163201)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13566332)

‎2022 Nov 09
9:05 PM

[23
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/163201/tab/all-users "Click here to see who gave kudos to this post.")

9,442

* SAP Managed Tags
* [Machine Learning](https://community.sap.com/t5/c-khhcw49343/Machine%2520Learning/pd-p/240174591523510321507492941674121)
* [SAP Datasphere](https://community.sap.com/t5/c-khhcw49343/SAP%2520Datasphere/pd-p/73555000100800002141)
* [SAP HANA Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%2520Cloud/pd-p/73554900100800002881)

* [Machine Learning

  Topic](/t5/c-khhcw49343/Machine%2BLearning/pd-p/240174591523510321507492941674121)
* [SAP Datasphere

  Software Product](/t5/c-khhcw49343/SAP%2BDatasphere/pd-p/73555000100800002141)
* [SAP HANA Cloud

  Software Product](/t5/c-khhcw49343/SAP%2BHANA%2BCloud/pd-p/73554900100800002881)

View products (3)

In this blog post we describe a simple approach on how data scientists can expose already trained HANA machine learning (ML) models to SAP Data Warehouse Cloud (SAP DWC). Implementing the proposed method allows business analysts to apply ML models on-demand according to their needs (i.e. for generation of reports, dashboards, or other BI activities) in a  "no-code" manner, using the data modeling capabilities of SAP DWC (i.e. the data builder component).

To demonstrate the idea, we train a simple time series forecasting model and expose it for consumption following the proposed approach. The developed model predicts the future number of notifications originating from a shop floor device, based on a dataset containing 2 years of historical data. The model creation is not reviewed in detail here, so if you want to learn more about how to create ML models, make sure to check [the blog post](https://blogs.sap.com/2019/11/05/hands-on-tutorial-machine-learning-push-down-to-sap-hana-with-python/) of andreas.forster and also [the post](https://blogs.sap.com/2021/02/25/hands-on-tutorial-leverage-sap-hana-machine-learning-in-the-cloud-through-the-predictive-analysis-library/) of yannick\_schaper.

## Preparation steps

To start with, we assume that the data needed for machine learning has already been shared in a space in the SAP DWC tenant, which we will call MLSPACE. In addition, a database user, MLUSER, has been created. This user has read access to the MLSPACE as well as read/write access to the open SQL schema MLSPACE#MLUSER.

As a next step, we will review the process from accessing the data, via data modeling up to model creation and exposure for consumption. The figure below shows the main steps (in yellow) in the order they are described in the following sections:

![](/legacyfs/online/storage/blog_attachments/2022/11/Techical_overview-3.png)

Process overview

## 1. Accessing the data

The data scientist can connect to the underlying HANA system using Jupyter Lab and Python with the hana\_ml package and access the open SQL schema of the user:

```
hana_port = 443

hana_user = 'MLSPACE#MLUSER'

hana_password = [YOUR_PASSWORD]

hana_address = [YOUR_DWC_HOST]

# Instantiate connection object

conn = dataframe.ConnectionContext(address = hana_address,

                                   port = 443,

                                   user = hana_user,

                                   password = hana_password)

# Control connection

conn.connection.isconnected()
```

Also the input data located in the read-only schema can be previewed using the following code snippet:

```
df_remote = conn.table('AssetForAnalytics', schema = 'MLSPACE')

df_remote.sort_values('DateTime').head(10).collect()
```

![](/legacyfs/online/storage/blog_attachments/2022/11/Inputtable_Tech.png)

Input data

## 2. Creating the ML model

This step usually involves several iterations to identify the optimal data as well as the features needed for modeling. Furthermore, the model selection and tuning require a substantial amount of work to complete. Since the focus of this blog post is on model sharing, rather than on model creation, these steps are skipped.

So, the data scientist decides to go with Exponential Smoothing from the HANA Predictive Analysis Library (PAL) for the time series forecasting. As an example of a simple data preparation an ID column is generated. Finally the model is created and the fit\_predict() method is called to predict the amount of device notifications from the shop floor for the next 20 time intervals.

```
df_remote = conn.table('AssetForAnalytics', schema = 'MLSPACE')

df_remote_id = df_remote.sort('DateTime').add_id()

#...

from hana_ml.algorithms.pal.tsa.exponential_smoothing

import AutoExponentialSmoothing

autoexpsmooth = AutoExponentialSmoothing(model_selection=True,

                                         forecast_model_name='TESM',

                                         seasonal_period=365,

                                         forecast_num=20)

df_res = autoexpsmooth.fit_predict(df_remote_id, key='ID')
```

## 3. Deploying ML models in a view

To be able to trigger and apply an ML model from SAP DWC the model needs to be embedded into a view. The process to achieve this involves the following two steps:

### 3.1 Creating a table function

The first step is to create a table function, which wraps the call of the apply function of the PAL ML model (here Exponential Smoothing, i.e. \_SYS\_AFL.PAL\_AUTO\_EXPSMOOTH). One can write this call in SQL from scratch or use a handy functionality of the hana\_ml package, which returns the SQL execute statement of the model object. The returned string contains already most of the SQL script required for the table function definition.

```
DO

BEGIN

DECLARE param_name VARCHAR(5000) ARRAY;

DECLARE int_value INTEGER ARRAY;

DECLARE double_value DOUBLE ARRAY;

DECLARE string_value VARCHAR(5000) ARRAY;

param_name[1] := N'MODELSELECTION';

int_value[1] := 1;

...

param_name[2] := N'FORECAST_MODEL_NAME';

...

string_value[2] := N'TESM';

param_name[3] := N'FORECAST_NUM';

int_value[3] := 20;

...

param_name[4] := N'CYCLE';

int_value[4] := 365;

...

param_name[5] := N'TRAINING_R...