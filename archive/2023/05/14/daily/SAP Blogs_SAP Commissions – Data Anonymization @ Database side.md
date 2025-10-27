---
title: SAP Commissions – Data Anonymization @ Database side
url: https://blogs.sap.com/2023/05/13/sap-commissions-data-anonymization-database-side/
source: SAP Blogs
date: 2023-05-14
fetch_date: 2025-10-04T11:38:09.934357
---

# SAP Commissions – Data Anonymization @ Database side

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Human Capital Management](/t5/human-capital-management/ct-p/hcm)
* [HCM Blog Posts by SAP](/t5/human-capital-management-blog-posts-by-sap/bg-p/hcm-blog-sap)
* SAP Commissions - Data Anonymization @ Database si...

Human Capital Management Blog Posts by SAP

Learn directly from SAP experts through blogs that deliver practical guidance and opportunities to deepen your expertise.

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/hcm-blog-sap/article-id/5799&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Commissions - Data Anonymization @ Database side](/t5/human-capital-management-blog-posts-by-sap/sap-commissions-data-anonymization-database-side/ba-p/13552868)

![Yogananda](https://avatars.profile.sap.com/5/9/id59e1da3a3dca34a1bd12f9d987d3cdb668e528e343194e20fc715b0bc28cc49b_small.jpeg "Yogananda")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Yogananda](https://community.sap.com/t5/user/viewprofilepage/user-id/75)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=hcm-blog-sap&message.id=5799)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/hcm-blog-sap/article-id/5799)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13552868)

‎2023 May 13
8:15 AM

[1
Kudo](/t5/kudos/messagepage/board-id/hcm-blog-sap/message-id/5799/tab/all-users "Click here to see who gave kudos to this post.")

8,628

* SAP Managed Tags
* [SAP HANA Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%2520Cloud/pd-p/73554900100800002881)
* [SAP SuccessFactors Incentive Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Incentive%2520Management/pd-p/73555000100800001602)
* [SAP HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA/pd-p/73554900100700000996)

* [SAP HANA Cloud

  Software Product](/t5/c-khhcw49343/SAP%2BHANA%2BCloud/pd-p/73554900100800002881)
* [SAP SuccessFactors Incentive Management

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BIncentive%2BManagement/pd-p/73555000100800001602)
* [SAP HANA

  Software Product](/t5/c-khhcw49343/SAP%2BHANA/pd-p/73554900100700000996)

View products (3)

# Data Anonymization in SAP HANA

Anonymization methods available in the SAP HANA database allow you to gain statistically valid insights from your data while protecting the privacy of individuals.

## Why Anonymize?

In a data-driven world, a growing amount of business data contains personal or sensitive information. If this data is to be used by applications for statistical analysis, it must be protected to ensure privacy. Trivial modifications to the data like replacing information that directly identifies an individual such as name or social security number (pseudonymization) or simply removing the information is not enough. Re-identification is still possible, for example if additional information is obtained (referred to as a linkage attack).

Unlike masking and pseudonymization, anonymization methods (also called privacy-enhancing methods) provide a more structured approach to modifying data for privacy protection. The quality of such anonymized or privacy-enhanced data is still sufficient for meaningful analysis. Several anonymization methods exist.

SAP HANA supports the methods k-anonymity, l-diversity, and differential privacy. Which method provides the most appropriate level of privacy depends on your data and the potential attack scenarios and attackers.

![](/legacyfs/online/storage/blog_attachments/2023/05/FYHX2HlX0AAeZz2.jpg)

Anonymization Workflow

A data controller – that is someone who determines when and how personal data is accessed and processed – defines an SQL view and configures the parameters of the chosen anonymization method to meet the required privacy level. Access to the anonymized view can then be granted to users using standard SAP HANA authorization mechanisms. An overview of this process is shown below:

![](https://help.sap.com/doc/2f789e82e97d4f4e9416547abfbd012e/2023_1_QRC/en-US/loio1f03221bf98c48b097814e370311ad68_LowRes.png)

# Data Anonymization Methods

Data anonymization methods provide a structured approach to modifying data for privacy protection. SAP HANA supports the data anonymization methods **k-anonymity, l-diversity**, and differential privacy.

## Anonymizing Data in SAP HANA - EXT Schema

Data anonymization can be applied to SQL views, thus enabling analytics on data while still protecting the privacy of individuals.

Create a table in your EXT Schema for your data

```
SET SCHEMA EXT;

CREATE COLUMN TABLE EXT.SALES_EMPLOYEES (

  ID INTEGER NOT NULL PRIMARY KEY GENERATED ALWAYS AS IDENTITY,

  NAME NVARCHAR(50),

  SITE NVARCHAR(20),

  GENDER NVARCHAR(10),

  AGE NVARCHAR(10),

  SALARY DOUBLE

  );
```

Insert your data to your table which contains few PII

```
INSERT INTO SALES_EMPLOYEES VALUES ('Henry Brubaker','Madrid','Male','29',91000);

INSERT INTO SALES_EMPLOYEES VALUES ('Jaylene Jennings','Paris','Female','19',67000);

INSERT INTO SALES_EMPLOYEES VALUES ('Dean Tavalouris','Boston','Male','20',76000);

INSERT INTO SALES_EMPLOYEES VALUES ('Lydia Wong','Dallas','Female','18',81000);

INSERT INTO SALES_EMPLOYEES VALUES ('Harvey Denton','Madrid','Male','19',45000);

INSERT INTO SALES_EMPLOYEES VALUES ('Pamela Doove','Nantes','Female','21',78000);

INSERT INTO SALES_EMPLOYEES VALUES ('Luciana Trujillo','Barcelona','Female','24',92000);

INSERT INTO SALES_EMPLOYEES VALUES ('Demarcus Collins','Bordeaux','Male','18',67000);

INSERT INTO SALES_EMPLOYEES VALUES ('Edward Tattsyrup','Barcelona','Male','18',78000);

INSERT INTO SALES_EMPLOYEES VALUES ('Benjamin Denton','Paris','Male','19',98000);

INSERT INTO SALES_EMPLOYEES VALUES ('Joaquin Barry','Madrid','Male','20',34000);

commit;
```

Create Geography Hierarchy table

```
CREATE COLUMN TABLE EXT.HIER_GEO (

  CHILD NVARCHAR(20),

  PARENT NVARCHAR(20)

  );
```

Insert your Geography data into table.

```
INSERT INTO HIER_GEO VALUES ('Europe', NULL);

INSERT INTO HIER_GEO VALUES ('North America', NULL);

INSERT INTO HIER_GEO VALUES ('Spain', 'Europe');

INSERT INTO HIER_GEO VALUES ('France', 'Europe');

INSERT INTO HIER_GEO VALUES ('USA', 'North America');

INSERT INTO HIER_GEO VALUES ('Canada', 'North America');

commit;
```

Create a view for the Geography Hierarchy

```
CREATE VIEW V_HIER_GEO AS

  SELECT *

    FROM HIERARCHY (

      SOURCE ( SELECT CHILD AS NODE_ID, PARENT AS PARENT_ID FROM HIER_GEO )

      SIBLING ORDER BY PARENT_ID, NODE_ID

      );
```

Create a Function for Age

```
CREATE OR REPLACE FUNCTION EXT.GROUP_AGE (age NVARCHAR(10), level INTEGER)

RETURNS outValue NVARCHAR(50) AS

BEGIN

  DECLARE defineValue INTEGER DEFAULT 5;

  DECLARE interval INTEGER;

  DECLARE rangeFrom INTEGER;

  IF (level > 0) THEN

    interval := defineValue * power(2, level - 1);

    rangeFrom = FLOOR(age / interval) * interval;

    outValue := '[' || rangeFrom || '-' || rangeFrom + interval - 1 || ']';

  ELSE

    outValue := age;

  END IF;

END;
```

Create an anonymized view based on k-anonymity:

```
CREATE VIEW SALES_EMPLOYEES_ANON AS

  SELECT ID, SITE, GENDER, AGE, SALARY

  FROM SALES_EMPLOYEES

  WITH ANONYMIZATION (

    ALGORITHM 'K-ANONYMITY'

    PARAMET...