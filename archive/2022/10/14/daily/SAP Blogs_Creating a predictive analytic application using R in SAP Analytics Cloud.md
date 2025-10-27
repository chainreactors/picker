---
title: Creating a predictive analytic application using R in SAP Analytics Cloud
url: https://blogs.sap.com/2022/10/13/creating-a-predictive-analytic-application-using-r-in-sap-analytics-cloud/
source: SAP Blogs
date: 2022-10-14
fetch_date: 2025-10-03T19:49:33.154419
---

# Creating a predictive analytic application using R in SAP Analytics Cloud

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Creating a predictive analytic application using R...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/155916&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Creating a predictive analytic application using R in SAP Analytics Cloud](/t5/technology-blog-posts-by-members/creating-a-predictive-analytic-application-using-r-in-sap-analytics-cloud/ba-p/13523483)

![danishmeraj](https://avatars.profile.sap.com/d/b/iddb2cfdeb96c693738e11426808246b9f36b70fae67976670055df13ff4605896_small.jpeg "danishmeraj")

[danishmeraj](https://community.sap.com/t5/user/viewprofilepage/user-id/810158)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=155916)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/155916)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13523483)

‎2022 Oct 13
11:16 PM

[10
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/155916/tab/all-users "Click here to see who gave kudos to this post.")

4,080

* SAP Managed Tags
* [Machine Learning](https://community.sap.com/t5/c-khhcw49343/Machine%2520Learning/pd-p/240174591523510321507492941674121)
* [SAP Analytics Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Cloud/pd-p/67838200100800006884)
* [SAP Analytics Cloud, augmented analytics](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Cloud%252C%2520augmented%2520analytics/pd-p/2221d1b0-d759-4b24-9333-f72da4d263da)
* [SAP Analytics Cloud, analytics designer](https://community.sap.com/t5/c-khhcw49343/SAP%2520Analytics%2520Cloud%252C%2520analytics%2520designer/pd-p/3f33380c-8914-4b7a-af00-0e9a70705a32)
* [SAP Predictive Analytics](https://community.sap.com/t5/c-khhcw49343/SAP%2520Predictive%2520Analytics/pd-p/73555000100800000084)

* [SAP Analytics Cloud

  SAP Analytics Cloud](/t5/c-khhcw49343/SAP%2BAnalytics%2BCloud/pd-p/67838200100800006884)
* [SAP Predictive Analytics

  SAP Predictive Analytics](/t5/c-khhcw49343/SAP%2BPredictive%2BAnalytics/pd-p/73555000100800000084)
* [Machine Learning

  Topic](/t5/c-khhcw49343/Machine%2BLearning/pd-p/240174591523510321507492941674121)
* [SAP Analytics Cloud, analytics designer

  Software Product Function](/t5/c-khhcw49343/SAP%2BAnalytics%2BCloud%25252C%2Banalytics%2Bdesigner/pd-p/3f33380c-8914-4b7a-af00-0e9a70705a32)
* [SAP Analytics Cloud, augmented analytics

  Software Product Function](/t5/c-khhcw49343/SAP%2BAnalytics%2BCloud%25252C%2Baugmented%2Banalytics/pd-p/2221d1b0-d759-4b24-9333-f72da4d263da)

View products (5)

In my previous **[blog](https://blogs.sap.com/2022/09/12/automated-machine-learning-automl-using-analytic-application/)**, I discussed an algorithm for creating a risk prediction tool by combining machine learning and an aggregation algorithm. In this blog, I will take a different approach to creating a predictive analytic application, leveraging the R interface in the SAP analytics cloud. You can follow along with me in this blog to achieve similar results.

**Data:** The data used for this demonstration is publicly available and easily accessible. You can download the data from [**here.**](https://www.scribbr.com/statistics/multiple-linear-regression/)

You can also read the blog **[here](https://www.scribbr.com/statistics/multiple-linear-regression/)**to get the basic information regarding multiple linear regression. Additionally, it will provide the background of the data used in this demonstration.

**Data Model:** Let's start by creating a data model using the dataset. In this step, the data model is created in the SAC modeller. We will add a column, i.e., the date dimension, using the calculated column formula. It will allow us to create a planning model.

***Note:** It is not mandatory to have a planning model to create an analytic application. I chose a planning model, thinking if, in future, I decided to write a blog about making the analytic application demonstrated in this blog more interactive, this blog would still be relevant.*

![](/legacyfs/online/storage/blog_attachments/2022/10/4-17.png)

*Figure 1: The figure shows the data in SAC modeller; Source: Author’s own illustration.*

**Configuring R widget:** In this step, the data source is configured in the R widget as shown in the below figure:

![](/legacyfs/online/storage/blog_attachments/2022/10/7.1.png)

*Figure 2: The figure shows the input data in R visualization widget; Source: Author’s own illustration.*

**Scripting in R:** After configuring the data source, we will leverage the scripting capability of R to train a machine-learning model.

First, we will load some of the required packages to our R environment and create a data frame of the source data. as shown in the below code snippet.

```
library(ggplot2)

library(dplyr)

df<- HeartData

head(df)

summary(df)
```

After that, we will check the correlation between different variables. The code snippet below shows the step to perform the correlation.

```
#Check correlation between two independent variables

cor(df$biking, df$smoking)

#Histogram for heart disease

hist(df$heart.disease)
```

For reproducing the results, I have set the seed to 1. It helps in reproducing similar results, as shown in this blog.

The next step is data partitioning. The data is divided into two parts. i.e., Training and Testing. In this example, 70% of the dataset is used for training and 30% of the data for testing purposes.

```
#make this example reproducible

set.seed(1)

sample <- sample(c(TRUE, FALSE), nrow(df), replace=TRUE, prob=c(0.7,0.3))

train  <- df[sample, ]

test   <- df[!sample, ]

#Training

heart.disease.lm<-lm(heart.disease ~ biking + smoking, data = train)

#Summary of Training

summary <-summary(heart.disease.lm)

summary

#Prediction using the test data

heart.disease.predictions <- predict(heart.disease.lm,test)
```

After training the model on the training dataset, the model is tested to make a prediction using the test dataset. The "cbind" function is used to creates a table of the testing results, which contains actual and predicted values from the testing phase. It gives an overview of the model's performance on the training dataset. as shown in below code snippet.

```
#creating a result table using column bind function

results <- cbind(heart.disease.predictions,test$heart.disease) #Taking the predicted values and actual values of test data

colnames(results)<- c('predicted', 'actual') #Naming the columns of the result

results <-as.data.frame(results)

#Visualising the result of actual test value and predicted test values

head(results)
```

The next step is retrieving the parameters from the trained model and using these parameters in the analytic designer environment to leverage this mathematical formula for prediction.

To retrieve the values from the summary of training data, as shown in the figure 3. We need to create a matrix of coefficients from the summary of the training data. It will allow us to retrieve the required parameters from this matrix. After retrieving the par...