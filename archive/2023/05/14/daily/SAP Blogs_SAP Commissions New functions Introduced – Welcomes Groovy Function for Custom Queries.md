---
title: SAP Commissions New functions Introduced – Welcomes Groovy Function for Custom Queries
url: https://blogs.sap.com/2023/05/13/sap-commissions-new-functions-introduced-welcomes-groovy-function-for-custom-queries/
source: SAP Blogs
date: 2023-05-14
fetch_date: 2025-10-04T11:38:06.646186
---

# SAP Commissions New functions Introduced – Welcomes Groovy Function for Custom Queries

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Human Capital Management](/t5/human-capital-management/ct-p/hcm)
* [HCM Blog Posts by SAP](/t5/human-capital-management-blog-posts-by-sap/bg-p/hcm-blog-sap)
* SAP Commissions New functions Introduced - Welcome...

Human Capital Management Blog Posts by SAP

Learn directly from SAP experts through blogs that deliver practical guidance and opportunities to deepen your expertise.

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/hcm-blog-sap/article-id/5877&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Commissions New functions Introduced - Welcomes Groovy Function for Custom Queries](/t5/human-capital-management-blog-posts-by-sap/sap-commissions-new-functions-introduced-welcomes-groovy-function-for/ba-p/13554338)

![Yogananda](https://avatars.profile.sap.com/5/9/id59e1da3a3dca34a1bd12f9d987d3cdb668e528e343194e20fc715b0bc28cc49b_small.jpeg "Yogananda")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Yogananda](https://community.sap.com/t5/user/viewprofilepage/user-id/75)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=hcm-blog-sap&message.id=5877)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/hcm-blog-sap/article-id/5877)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13554338)

‎2023 May 13
12:15 PM

[5
Kudos](/t5/kudos/messagepage/board-id/hcm-blog-sap/message-id/5877/tab/all-users "Click here to see who gave kudos to this post.")

1,306

* SAP Managed Tags
* [SAP SuccessFactors Incentive Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Incentive%2520Management/pd-p/73555000100800001602)

* [SAP SuccessFactors Incentive Management

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BIncentive%2BManagement/pd-p/73555000100800001602)

View products (1)

In this post I'd like to present you with new functions got introduced which you can evaluate the deseried output via Groovy language with supporting one of import package.

You can use the Groovy Function to build a Custom Query Function. This feature helps build logic for input parameters, for example, formatting input data.

![](/legacyfs/online/storage/blog_attachments/2023/05/28d9091bd673dd281308643226b240ae.png)

## What is Groovy?

Groovy is an object-oriented programming language that is both static and dynamic. It can be used both as a programming language and as a scripting language for Java. Groovy is a pleasant language to develop in, as it reduces huge amounts of boilerplate code including no semi colons, no getters/setters, type inference, null safety, elvis operators and much, much more.

That’s not to say you’re not permitted to use Java notation if you so choose, though. Interestingly, most Java code will compile in groovy so it has a low bar for entry into the language.  It’s become a mature choice that developers trust when Java verbosity hurts and dynamic typing isn’t an issue.

---

### Practical examples for Evaluating Functions through Formulas

![](/legacyfs/online/storage/blog_attachments/2023/05/2023-05-13_12-52-38.png)

|  |
| --- |
| Currently, the usage of Groovy Function is supported only for importing below packages only.  import java.text.\*;   import java.math.\*;    **Not Supported packages**    import groovy.json.JsonSlurper   import java.util.HashMap;   import groovy.transform.Field;   import groovy.json.JsonOutput;  import groovy.xml.XmlUtil; |

![](/legacyfs/online/storage/blog_attachments/2023/05/2023-05-13_12-55-03.png)

The groovy function must have a main method with the signature def main($1, $2, $3, $4, $5, $6, $7, $8, $9)

Following is an example of a Groovy Function to format the input parameter to a text string:

```
import java.text.*

 def main($1, $2, $3, $4, $5, $6, $7, $8, $9) {

  DecimalFormat df = new DecimalFormat("#,###.00");

  if ($1 == 'TEXT') {

    if ($3[0] == null){

      return null

    } else {

      def s = $3[0].toString()

      return s.substring(0, s.indexOf('.'))

    }

  } else if ($1 == 'DATE'){

    if ($7 == null){

      return '01/01/2200'

    } else {

      SimpleDateFormat sm = new SimpleDateFormat('MM/dd/yy')

      return sm.format($7)

    }

  } else if ($1 == 'QUANTITY'){

    if ($3[0] == null){

      return '0.00'

    } else {

      return df.format($3[0].setScale(2, java.math.RoundingMode.CEILING))

    }

  } else if ($1 == 'MONEY'){

    if ($3[0] == null){

      return '$0.00'

    } else {

      return '$' + df.format($3[0].setScale(2, java.math.RoundingMode.CEILING))

    }

  } else if ($1 == 'PERCENT'){

    if ($3[0] == null){

      return '0.00%'

    } else {

      return $3[0].multiply(new BigDecimal(100)).setScale(2, java.math.RoundingMode.CEILING).toString()+'%'

    }

  } else {

    return ''

  }

}
```

You can add this function to the CS\_PlugInQuery with the insert SQL as follows:

```
INSERT INTO CS_PLUGINQUERY (tenantId, name, query) VALUES ( '0504', 'FORMAT MONEY',

'import java.text.*

 def main($1, $2, $3, $4, $5, $6, $7, $8, $9) {

  DecimalFormat df = new DecimalFormat("#,###.00");

  if ($1 == ''TEXT'') {

    if ($3 == null){

      return null

    } else {

      def s = $3[0].toString()

      return s.substring(0, s.indexOf(''.''))

    }

  } else if ($1 == ''DATE''){

    if ($7 == null){

      return ''01/01/2200''

    } else {

      SimpleDateFormat sm = new SimpleDateFormat(''MM/dd/yy'')

      return sm.format($7)

    }

  } else if ($1 == ''QUANTITY''){

    if ($3[0] == null){

      return ''0.00''

    } else {

      return df.format($3[0].setScale(2, java.math.RoundingMode.CEILING))

    }

  } else if ($1 == ''MONEY''){

    if ($3[0] == null){

      return ''$0.00''

    } else {

      return ''$'' + df.format($3[0].setScale(2, java.math.RoundingMode.CEILING))

    }

  } else if ($1 == ''PERCENT''){

    if ($3[0] == null){

      return ''0.00%''

    } else {

      return $3[0].multiply(new BigDecimal(100)).setScale(2, java.math.RoundingMode.CEILING).toString()+''%''

    }

  } else {

    return ''''

  }

}');
```

Use the Evaluate function in the Credit Rule and specify the name of the query![](/legacyfs/online/storage/blog_attachments/2023/05/2023-05-13_12-50-52.png)

### Bonus Level

If you're stuck with groovy programming language or syntax or to write your own logic, Ask your questions or explain the code using Prompts which ChatGPT will try to help you out.

I have provided you sample examples from above code to understand "MONEY" format in Groovy script![](/legacyfs/online/storage/blog_attachments/2023/05/2023-05-13_13-58-18.png)

Evaluate through Groovy IDE which comes in handy for your testing.. so you can validate your code with right results .. Once your code is working fine, you can insert into Plugin table.![](/legacyfs/online/storage/blog_attachments/2023/05/2023-05-13_13-53-48.png)

---

### Best Practice

+ Use the context variable (Example: $periodStartDate, $periodEndDate) instead of the parameter variable ($1 to $8) if possible. This will perform better because it doesn't need to process the input parameter. It will also make your query less dependent on the user provided value, which can be changed.

+ Provide default value for your...