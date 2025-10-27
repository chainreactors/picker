---
title: Using HANA Cloud, data lake Files with a Jupyter Notebook and PySpark
url: https://blogs.sap.com/2022/11/09/using-hana-cloud-data-lake-files-with-a-jupyter-notebook-and-pyspark/
source: SAP Blogs
date: 2022-11-10
fetch_date: 2025-10-03T22:14:58.779489
---

# Using HANA Cloud, data lake Files with a Jupyter Notebook and PySpark

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Using SAP HANA Cloud, data lake Files with a Jupyt...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/163521&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Using SAP HANA Cloud, data lake Files with a Jupyter Notebook and PySpark](/t5/technology-blog-posts-by-sap/using-sap-hana-cloud-data-lake-files-with-a-jupyter-notebook-and-pyspark/ba-p/13567227)

![former_member804450](https://avatars.profile.sap.com/former_member_small.jpeg "former_member804450")

[former\_member804450](https://community.sap.com/t5/user/viewprofilepage/user-id/804450)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=163521)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/163521)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13567227)

‎2022 Nov 09
8:34 PM

[7
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/163521/tab/all-users "Click here to see who gave kudos to this post.")

3,938

* SAP Managed Tags
* [SAP HANA Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%2520Cloud/pd-p/73554900100800002881)
* [Python](https://community.sap.com/t5/c-khhcw49343/Python/pd-p/f220d74d-56e2-487e-8e6c-a8cb3def2378)
* [SAP HANA Cloud, data lake](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%2520Cloud%252C%2520data%2520lake/pd-p/7efde293-f35d-4737-b40f-756b6a798216)

* [SAP HANA Cloud

  Software Product](/t5/c-khhcw49343/SAP%2BHANA%2BCloud/pd-p/73554900100800002881)
* [Python

  Programming Tool](/t5/c-khhcw49343/Python/pd-p/f220d74d-56e2-487e-8e6c-a8cb3def2378)
* [SAP HANA Cloud, data lake

  Software Product Function](/t5/c-khhcw49343/SAP%2BHANA%2BCloud%25252C%2Bdata%2Blake/pd-p/7efde293-f35d-4737-b40f-756b6a798216)

View products (3)

**To best follow this post and try things out yourself, you should:**

1. Have some basic knowledge of the Python programming language (PySpark)

1. Have a Data Lake instance provisioned and configured. [configure the HANA Data Lake File Container](https://help.sap.com/docs/SAP_HANA_DATA_LAKE/b239ed4bb73a4f07886657e237f1875f/afe91bfba419464a84b7a05e7960d6f9.html).

1. Have the Instance ID for your Data Lake Instance.

1. Have access to a Jupyter notebook ([io](https://jupyter.org/)).

**Overview:**

Data Lake Files includes a driver which enables access to the file system directly from Spark.   It implements the Hadoop FileSystem interface to allow platforms and applications in the Hadoop ecosystem to work with data lake Files for data storage. In this blog, we will get to see how we can easily configure and establish a connection with HDLFS and see how to write, read and delete a file from within the Files store.

**Step 1:** **Download the Data Lake Files Spark Driver from:**

+ The data lake Client install can be installed using the steps outlined in [SAP HANA Cloud, Data Lake Client Interfaces](https://help.sap.com/docs/SAP_HANA_DATA_LAKE/b239ed4bb73a4f07886657e237f1875f/8753952e16c74d0c9cf1a18c7cd97c96.html?state=DRAFT&version=2022_4_QRC). Once the data lake client is installed, the hdlfs spark driver is in the **HDLFS folder**.

![](/legacyfs/online/storage/blog_attachments/2022/11/image1-5.png)

+ Also, one can download the driver directly from [SAP HANA Data Lake Files Client Library](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fsearch.maven.org%2Fartifact%2Fcom.sap.hana.datalake.files%2Fsap-hdlfs) on Maven.org.

**Step 2: Set up the Connection From Jupyter to HANA Cloud, data lake Files**

As part of [configuring access to Data Lake Files](https://help.sap.com/docs/SAP_HANA_DATA_LAKE/b239ed4bb73a4f07886657e237f1875f/afe91bfba419464a84b7a05e7960d6f9.html), you will create a client certificate and key. To communicate with data lake Files from your Jupyter notebook, the *client.crt* and *client.key* must be provided in a keystore package, and this package needs to be uploaded onto your Jupyter notebook instance.

Here is an example of how you can generate a Create a**. pkcs12 package** from your client certificate and key using Openssl:

openssl pkcs12 \

-export \

-inkey </path/to/client-key-file> \

-in </path/to/client-certificate-file> \

-out </path/to/client-keystore.p12> \

-password pass:<password-p12-file> \

This is how it will look in the Command prompt:

![](/legacyfs/online/storage/blog_attachments/2022/11/image2-4.png)

Once this is done, the. pkcs12 file will be created in the given path. It will look something like below.  Keep a note of the keystore password, as you will need it later.

![](/legacyfs/online/storage/blog_attachments/2022/11/image3-4.png)

Now, we upload the. pkcs12 file and the Spark Driver from HDLFS directory to the Jupyter notebook instance.

Click on the **upload** arrow, and then upload the 2 files. This will get uploaded to the workbook home.

![](/legacyfs/online/storage/blog_attachments/2022/11/image4-4.png)

**Step 3: Understand the Code to configure and setup a connection with the HANA Data Lake Files Store**

**The entire code will be at the "bottom of the post". You can paste it into code blocks in your notebook to execute it.**

The below code block shows how to configure and setup a connection with the HANA Data Lake Files Store.

![](/legacyfs/online/storage/blog_attachments/2022/11/image5-6.png)

In the following code block, it is explained ***how to setup the SSL configuration, the Operations config, Driver's configuration and format of the URI.***

***Note:*** *To reference a particular parameter property, we call the sc.jsc.hadoopConfiguartion().set() to set Sparks Global Hadoop Configuration. “\_jsc” is the **Java Spark Context** which is a proxy into the SparkContext in that JVM.*

**# ----- ssl configuration ----** *it will define the location of the client keystore, the password of the client keystore and the type of the truststore file.*

sc.\_jsc.hadoopConfiguration().set("fs.hdlfs.ssl.keystore.location", keystoreLocation)

sc.\_jsc.hadoopConfiguration().set("fs.hdlfs.ssl.keystore.password", keystorePwd)

sc.\_jsc.hadoopConfiguration().set("fs.hdlfs.ssl.keystore.type", "PKCS12")

**# ----- operations configuration ----** *it is going to configure the operations parameters where the CREATE Mode is set to be DEFAULT which will read, write and delete files*

sc.\_jsc.hadoopConfiguration().set("fs.hdlfs.operation.create.mode", "DEFAULT")

**# ----- driver configuration ----** *An implementation of org.apache.hadoop.fs.FileSystem targeting SAP HANA Data Lake Files. To allow Spark to load the driver, specify the configuration parameters to make the system aware of the new hdlfs:// scheme for referring to files in data lake Files.*

sc.\_jsc.hadoopConfiguration().set("fs.AbstractFileSystem.hdlfs.impl", "com.sap.hana.datalake.files.Hdlfs")

sc.\_jsc.hadoopConfiguration().set("fs.hdlfs.impl", "com.sap.hana.datalake.files.HdlfsFileSystem")

sc.\_jsc.hadoopConfiguration().set("mapreduce.fileoutputcommitter.algorithm.version","2")

**#--- uri is in format hdlfs://<filecontainer>.<endpointSuffix>/path/to/file ----** *Once the driver is known to Spark, ...