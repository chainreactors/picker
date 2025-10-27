---
title: Unlocking Accurate Forecasts for Lumpy and Intermittent Demand Patterns with SPEC (Stock-keeping-oriented Prediction Error Costs)
url: https://blogs.sap.com/2023/06/28/how-to-forecast-for-lumpy-and-intermittent-demand-forecasts-using-stock-keeping-oriented-prediction-error-costs-spec/
source: SAP Blogs
date: 2023-06-29
fetch_date: 2025-10-04T11:47:32.896889
---

# Unlocking Accurate Forecasts for Lumpy and Intermittent Demand Patterns with SPEC (Stock-keeping-oriented Prediction Error Costs)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Supply Chain Management](/t5/supply-chain-management/ct-p/scm)
* [SCM Blog Posts by Members](/t5/supply-chain-management-blog-posts-by-members/bg-p/scm-blog-members)
* Unlocking Accurate Forecasts for Lumpy and Intermi...

Supply Chain Management Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/scm-blog-members/article-id/4490&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Unlocking Accurate Forecasts for Lumpy and Intermittent Demand Patterns with SPEC (Stock-keeping-oriented Prediction Error Costs)](/t5/supply-chain-management-blog-posts-by-members/unlocking-accurate-forecasts-for-lumpy-and-intermittent-demand-patterns/ba-p/13548007)

![lingaiahvanam](https://avatars.profile.sap.com/9/a/id9a103559b0b2077adf9665cbe1698840749299e43e04ee57fa3ba7f7f6b8376b_small.jpeg "lingaiahvanam")

![SAP Champion](/html/@B3DACAC6163F980483AC32558EB69695/rank_icons/champion-rank-16x16.svg "SAP Champion")
[lingaiahvanam](https://community.sap.com/t5/user/viewprofilepage/user-id/613)

SAP Champion

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=scm-blog-members&message.id=4490)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/scm-blog-members/article-id/4490)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13548007)

‎2023 Jun 28
10:43 PM

[7
Kudos](/t5/kudos/messagepage/board-id/scm-blog-members/message-id/4490/tab/all-users "Click here to see who gave kudos to this post.")

4,273

* SAP Managed Tags
* [SAP Integrated Business Planning for demand](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integrated%2520Business%2520Planning%2520for%2520demand/pd-p/ef3d81c2-849e-4189-8aca-d26b9f4aa268)
* [SAP Integrated Business Planning for sales and operations](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integrated%2520Business%2520Planning%2520for%2520sales%2520and%2520operations/pd-p/ff8b7b2c-f548-4d7c-bd78-eba4d1920785)
* [SAP Demand Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Demand%2520Management/pd-p/01200615320800000690)
* [SAP Integrated Business Planning](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integrated%2520Business%2520Planning/pd-p/67838200100800006742)
* [SAP Supply Chain Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520Supply%2520Chain%2520Management/pd-p/01200615320800000492)

* [SAP Demand Management

  SAP Demand Management](/t5/c-khhcw49343/SAP%2BDemand%2BManagement/pd-p/01200615320800000690)
* [SAP Integrated Business Planning

  SAP Integrated Business Planning](/t5/c-khhcw49343/SAP%2BIntegrated%2BBusiness%2BPlanning/pd-p/67838200100800006742)
* [SAP Supply Chain Management

  SAP Supply Chain Management](/t5/c-khhcw49343/SAP%2BSupply%2BChain%2BManagement/pd-p/01200615320800000492)
* [SAP Integrated Business Planning for demand

  Additional Software Product](/t5/c-khhcw49343/SAP%2BIntegrated%2BBusiness%2BPlanning%2Bfor%2Bdemand/pd-p/ef3d81c2-849e-4189-8aca-d26b9f4aa268)
* [SAP Integrated Business Planning for sales and operations

  Additional Software Product](/t5/c-khhcw49343/SAP%2BIntegrated%2BBusiness%2BPlanning%2Bfor%2Bsales%2Band%2Boperations/pd-p/ff8b7b2c-f548-4d7c-bd78-eba4d1920785)

View products (5)

![](/legacyfs/online/storage/blog_attachments/2023/06/Time-Series.png)

Accurate forecasts of product demand play a crucial role in optimizing logistics and production operations in both the short and long term. Therefore, achieving the highest possible level of prediction accuracy is highly desirable. To effectively train predictive models and ensure optimal performance, it is essential to assess the deviation between the forecasted demand and the actual demand using an appropriate metric.

However, the selection of a metric becomes critical as it should accurately represent the prediction error. If an unsuitable metric is utilized, the predictive models will not be adequately optimized, leading to inaccurate predictions. Conventional metrics such as Mean Absolute Percentage Error (MAPE) or Root Mean Square Error (RMSE), although widely used, may not be suitable for evaluating forecasting errors, particularly for demand patterns characterized by sporadic or intermittent occurrences. These conventional metrics often fail to adequately account for factors such as temporal shifts (i.e., prediction occurring before or after actual demand) or cost-related considerations.

To address these limitations, a novel metric that goes beyond statistical considerations and incorporates relevant business aspects. By combining statistical analysis with business-related factors, proposed metric offers a more comprehensive evaluation of forecasting accuracy. To validate the effectiveness of this metric.

## **Introduction**

The choice of forecasting method depends on evaluating which approach best suits the problem at hand. Therefore, it is essential to assess the performance of forecasting methods and evaluate predictions using various accuracy measures that have been proposed and extensively discussed over the past few decades. However, there is no universally optimal performance metric that can be universally applied to all types of forecasting problems.

Depending on the selected metric, forecasts can yield significantly different performances, making accurate evaluation challenging. Furthermore, some metrics are not suitable for certain types of data. For instance, the mean absolute percentage error (MAPE) produces infinite or undefined values when actual values are zero or close to zero, which is often the case in certain applications. Consequently, many existing metrics work well with smooth and linear patterns but become less accurate or even unusable when dealing with intermittent patterns, which is frequently observed in product demand forecasting due to occurrences of zero values.

The evaluation of forecasts for stock-keeping units using traditional accuracy metrics can lead to misleading conclusions, highlighting the need to develop appropriate error measures that incorporate additional factors in industries where intermittent demand is prevalent. Intermittent demand is characterized by non-demand intervals, while lumpy demand exhibits large fluctuations in the size of demand occurrences.

## **Stock-keeping-oriented Prediction Error Costs (SPEC)**

To address the limitations of existing metrics in analyzing demand patterns with frequent zero values, a new metric that considers both the shortcomings mentioned earlier and economic factors.

The purpose of this new metric is to measure the accuracy of predictions by comparing the actual demand with the forecast in terms of the costs incurred over the forecast period. There are costs associated with keeping inventory in the warehouse. The longer the inventory stays and the greater the quantity, the higher the stock-keeping costs. Additionally, there are opportunity costs when customer orders cannot be fulfilled due to unavailability of items in the warehouse. The proposed metric should be zero for a perfect prediction that optimally manages storage, and as the deviation from the perfect prediction increases, the metric should reflect the costs of the misprediction.

By using SPEC, it becomes possible to measure forecasts in two dimensions, considering both the magnitude and the timing. In situations wher...