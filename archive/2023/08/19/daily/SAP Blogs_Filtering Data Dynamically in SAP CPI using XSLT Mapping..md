---
title: Filtering Data Dynamically in SAP CPI using XSLT Mapping.
url: https://blogs.sap.com/2023/08/18/filtering-data-dynamically-in-sap-cpi-using-xslt-mapping./
source: SAP Blogs
date: 2023-08-19
fetch_date: 2025-10-04T11:59:50.502652
---

# Filtering Data Dynamically in SAP CPI using XSLT Mapping.

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Filtering Data Dynamically in SAP CPI using XSLT M...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/164864&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Filtering Data Dynamically in SAP CPI using XSLT Mapping.](/t5/technology-blog-posts-by-members/filtering-data-dynamically-in-sap-cpi-using-xslt-mapping/ba-p/13577820)

![rasesh_thakkar](https://avatars.profile.sap.com/3/8/id38a857d2cf3fdd1a5f574230558509dc677018cc7c5dcef69c47640a9416d386_small.jpeg "rasesh_thakkar")

[rasesh\_thakkar](https://community.sap.com/t5/user/viewprofilepage/user-id/156441)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=164864)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/164864)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13577820)

‎2023 Aug 18
10:00 PM

[13
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/164864/tab/all-users "Click here to see who gave kudos to this post.")

20,660

* SAP Managed Tags
* [SAP SuccessFactors Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Platform/pd-p/73555000100800000775)
* [Cloud Integration](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Integration/pd-p/67837800100800006801)
* [SAP Cloud Platform, industry edition, client libraries](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520Platform%252C%2520industry%2520edition%252C%2520client%2520libraries/pd-p/73555000100800000218)

* [Cloud Integration

  SAP Integration Suite](/t5/c-khhcw49343/Cloud%2BIntegration/pd-p/67837800100800006801)
* [SAP SuccessFactors Platform

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BPlatform/pd-p/73555000100800000775)
* [SAP Cloud Platform, industry edition, client libraries

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BCloud%2BPlatform%25252C%2Bindustry%2Bedition%25252C%2Bclient%2Blibraries/pd-p/73555000100800000218)

View products (3)

Hello All,

Greetings for the Day!!

You may have encountered various scenarios where you configured more than three filters and created different paths yet performed the same task in all these paths. The first filter has the department equal to HR, while the others correspond to Finance, Sales, and Audit, respectively. Even though the data processing occurs in different paths, the same task is being executed in each path.

![](/legacyfs/online/storage/blog_attachments/2023/08/Blog-1-2.png)

Complex Integration

As you can see above, the integration appears complex. The architect responsible for the integration would be able to debug it, but it might be a bit time-consuming for other architects to understand the process of the above integration. Validating all the integration steps, by reviewing each one and either removing or adding filter criteria, would also increase the complexity of the integration.

It will also impact the performance of the integration, as it involves multiple steps that need to be executed. This will subsequently increase the processing time of the integration. The API calls made by the above integration will raise the load on the SuccessFactors system due to multiple API calls being made for performing the same task.

![](/legacyfs/online/storage/blog_attachments/2023/08/Blog-2-1.png)

Simplified Integration

**Solution:**

To reduce the complexity of integration and decrease the processing time, as well as to alleviate the load on the SuccessFactors API, we can utilize the 'XSLT Mapping' function within the integration. This function enables us to filter data, map fields, and execute necessary distinct functions.

What is XSLT Mapping?

XSLT (Extensible Stylesheet Language Transformations) mapping in SAP CPI refers to the process of using XSLT to transform and map data between different formats during integration scenarios. XSLT is a language used to transform XML documents into various formats.

In the context of SAP CPI, XSLT mapping allows you to:

1. Transform Data: Convert XML data from the source format to the target format using XSLT templates. This is particularly useful when you need to map data from one XML structure to another.

2. Perform Complex Mapping: XSLT provides a powerful way to perform complex transformations, conditional mapping, and data enrichment during integration.

Overall, XSLT mapping is a powerful tool in SAP CPI that enables you to manage complex data transformations and mappings in integration scenarios, easing seamless communication between different systems with varying data formats.

**Methodology:**

In this scenario, we are going to filter out cost centers and calculate the sum of course costs for all the users, storing it as Total Cost. Generally, most customers have multiple cost centers within their organization, and many new cost centers are created and removed from the system at regular intervals.

Ideally, it is not feasible to have multiple filters and add them manually when new cost centers are created or deleted post Go-Live.

We are going to use “*group by*” function which is a mechanism in XSLT mapping that allows you to group and aggregate data based on specific criteria. This is particularly useful when you’re dealing with XML data and need to perform operations on grouped data sets.

Here's how the "group by" function works in XSLT within the context of SAP CPI:

1. Grouping Data : The "group by" function lets you group XML elements based on a common attribute or element value. This means that elements with the same value for the specified attribute or element are treated as a group.

2. Aggregating Data : Once the data is grouped, you can use aggregate functions (like sum, count, average, etc.) to perform calculations on the elements within each group. This allows you to calculate values for each group separately.

3. Output Transformation : After grouping and aggregating, you can define how the resulting grouped and aggregated data should be transformed into the desired output format.

Here's a simplified example of how you might use the "group by" function in XSLT within SAP CPI:

```
<!-- Group employees by Cost Center -->

<xsl:for-each-group select="{Entity Name} /{Entity Name}" group-by="{Enter Field to Filter}">

                <CostCenter ><xsl:value-of select="current-grouping-key()" /></CostCenter>

<!-- Calculate the Total Cost within the Cost Center -->

                <Total_Cost><xsl:value-of select="sum(current-group()/{Enter Field to Sum})"/></Total_Cost>
```

Suppose you have the below input XML data having Cost Center Details:

```
Input XML :

<CostDetails>

    <CostDetails>

        <externalCode>1982</externalCode>

        <cust_costcenter>3748</cust_costcenter>

        <course_cost>960</course_cost>

    </CostDetails>

    <CostDetails>

        <externalCode>1984</externalCode>

        <cust_costcenter>3748</cust_costcenter>

        <course_cost>850</course_cost>

    </CostDetails>

    <CostDetails>

        <externalCode>1986</externalCode>

        <cust_costcenter>374...