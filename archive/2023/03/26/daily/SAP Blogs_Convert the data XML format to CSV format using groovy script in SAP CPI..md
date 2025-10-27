---
title: Convert the data XML format to CSV format using groovy script in SAP CPI.
url: https://blogs.sap.com/2023/03/25/convert-the-data-xml-format-to-csv-format-using-groovy-script-in-sap-cpi./
source: SAP Blogs
date: 2023-03-26
fetch_date: 2025-10-04T10:42:39.480641
---

# Convert the data XML format to CSV format using groovy script in SAP CPI.

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Convert the data XML format to CSV format using gr...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/161745&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Convert the data XML format to CSV format using groovy script in SAP CPI.](/t5/technology-blog-posts-by-members/convert-the-data-xml-format-to-csv-format-using-groovy-script-in-sap-cpi/ba-p/13559780)

![Chandranath73](https://avatars.profile.sap.com/1/0/id10798bf2c8df867749c519d3f0592156e890aa9722e611468948d1b9a808c6a0_small.jpeg "Chandranath73")

[Chandranath73](https://community.sap.com/t5/user/viewprofilepage/user-id/148585)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=161745)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/161745)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13559780)

‎2023 Mar 25
6:28 PM

[8
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/161745/tab/all-users "Click here to see who gave kudos to this post.")

13,625

* SAP Managed Tags
* [Cloud Integration](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Integration/pd-p/67837800100800006801)

* [Cloud Integration

  SAP Integration Suite](/t5/c-khhcw49343/Cloud%2BIntegration/pd-p/67837800100800006801)

View products (1)

### **Introduction:-**

Converting an XML file to CSV format is a common task in data integration and processing workflows. SAP Cloud Platform Integration (CPI) is a cloud-based integration service that makes it easy to create data processing pipelines using a variety of components and languages.

In this blog post, I will show you how to use Groovy script in CPI to convert XML to CSV with a comma separator. The script will iterate through all elements in the XML file and extract the element names and values to create a CSV file.

### Importance:-

In CPI we already have one standard function to convert the data XML to CSV format but that function doesn't work properly all the time.

In my case, I have one XML input file there have some different types of data:- String("Hebrew" language) data, numeric data, String ("English" language) data and some date functions.

when I convert the data with a standard function the field data are sorted. Therefore, I write a groovy script that helps to convert the data without any issues.

### Objective:-

I will use a simple example XML file and show how to write a Groovy script that converts it to a CSV file. I will also show the  output file after converting the data.

##### Input file:-

```
<root>

  <row>

    <UserId>100</UserId>

    <Name>Lionel Messi</Name>

    <DOB>1987-06-24</DOB>

    <Phone>0524389823</Phone>

    <Email>lm10@gmail.com</Email>

 </row>

 <row>

    <UserId>105</UserId>

    <Name>Cristiano Ronaldo</Name>

    <DOB>1985-02-05</DOB>

    <Phone/>

    <Email>cr7@gmail.com</Email>

  </row>

  <row>

    <UserId>115</UserId>

    <Name>Kylian Mbappe</Name>

    <DOB>1998-12-20</DOB>

    <Phone>062-47788354</Phone>

    <Email/>

  </row>

</root>
```

**Groovy Script:-**

```
import com.sap.gateway.ip.core.customdev.util.Message

import java.nio.charset.StandardCharsets

import java.io.OutputStreamWriter

import groovy.xml.*

def Message processData(Message message) {

    def payload = message.getBody(java.lang.String.class)

    def root = new XmlParser().parseText(payload)

    def csv = new StringWriter()

    // Write header row

    root.children().first().children().each { field ->

        csv.write(field.name())

        if (field != root.children().first().children().last()) {

            csv.write(',')

        }

    }

    csv.write('\n')

    // Write data rows

    root.children().each { record ->

        record.children().each { field ->

            csv.write(field.text())

            if (field != record.children().last()) {

                csv.write(',')

            }

        }

        csv.write('\n')

    }

    message.setBody(csv.toString())

    return message

}
```

In this script, we start by importing the necessary libraries for processing the message payload and parsing XML.

The Message class is used to represent the input and output messages in CPI. The java.nio.charset.StandardCharsets and java.io.OutputStreamWriter classes are used to specify the character encoding and output format for the CSV file. The groovy.xml.\* classes are used for parsing the input XML file.

We then define a process Data function that takes a Message object as input and returns a modified Message object.

Inside the function, we get the payload of the message as a string and parse it into an XML document using XmlParser().

The **XmlParser** class parses the input XML file and returns a **groovy.util.Node** object, which represents the root node of the XML file.Then initializes a **StringWriter** object, which is used to store the CSV output.

The script then iterates through the elements in the XML file to extract the element names and values and write them to the CSV output. First, the script writes the header row of the CSV file:

```
root.children().first().children().each { field ->

    csv.write(field.name())

    if (field != root.children().first().children().last()) {

        csv.write(',')

    }

}

csv.write('\n')
```

This code block uses the children() method to iterate through the child nodes of the root node. The first() method is used to get the first child node, which is assumed to contain the header row of the CSV file. The children() method is called again to iterate through the child nodes of the header row node. For each child node, the element name is extracted using the name() method and written to the CSV output. If the current child node is not the last child node, a comma separator is also written to the CSV output.

The script then writes the data rows of the CSV file:

```
root.children().each { record ->

    record.children().each { field ->

        csv.write(field.text())

        if (field != record.children().last()) {

            csv.write(',')

        }

    }

    csv.write('\n')

}
```

This code block uses the children() method to iterate through each child node of the root node. For each child node, the script iterates through its child nodes to extract the element values and write them to the CSV output. The text() method is used to extract the element value. If the current child node is not the last child node, a comma separator is also written to the CSV output. After all the data rows are written to the CSV output, the StringWriter object is converted to a String object and set as the output message body.

Output:-

```
UserId,Name,DOB,Phone,Email

100,Lionel Messi,1987-06-24,0524389823,lm10@gmail.com

105,Cristiano Ronaldo,1985-02-05,,cr7@gmail.com

115,Kylian Mbappe,1998-12-20,062-47788354,
```

### Conclusion:-

In this blog post, I have shown how to use Groovy script in CPI to convert an XML file to a CSV file with a comma separator. The script uses the **XmlParser** class to parse the XML input and extract the e...