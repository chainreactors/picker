---
title: Accessing SAP HANA Cloud, data lake Files from Python
url: https://blogs.sap.com/2022/12/12/accessing-sap-hana-cloud-data-lake-files-from-python/
source: SAP Blogs
date: 2022-12-13
fetch_date: 2025-10-04T01:17:52.306308
---

# Accessing SAP HANA Cloud, data lake Files from Python

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Accessing SAP HANA Cloud, data lake Files from Pyt...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/157726&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Accessing SAP HANA Cloud, data lake Files from Python](/t5/technology-blog-posts-by-sap/accessing-sap-hana-cloud-data-lake-files-from-python/ba-p/13550158)

![former_member804450](https://avatars.profile.sap.com/former_member_small.jpeg "former_member804450")

[former\_member804450](https://community.sap.com/t5/user/viewprofilepage/user-id/804450)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=157726)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/157726)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13550158)

‎2022 Dec 12
9:55 PM

[5
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/157726/tab/all-users "Click here to see who gave kudos to this post.")

2,570

* SAP Managed Tags
* [SAP HANA Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%2520Cloud/pd-p/73554900100800002881)
* [SAP HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA/pd-p/73554900100700000996)
* [SAP HANA Cloud, data lake](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%2520Cloud%252C%2520data%2520lake/pd-p/7efde293-f35d-4737-b40f-756b6a798216)

* [SAP HANA Cloud

  Software Product](/t5/c-khhcw49343/SAP%2BHANA%2BCloud/pd-p/73554900100800002881)
* [SAP HANA

  Software Product](/t5/c-khhcw49343/SAP%2BHANA/pd-p/73554900100700000996)
* [SAP HANA Cloud, data lake

  Software Product Function](/t5/c-khhcw49343/SAP%2BHANA%2BCloud%25252C%2Bdata%2Blake/pd-p/7efde293-f35d-4737-b40f-756b6a798216)

View products (3)

**To best follow this post and try things out yourself, you should:**

1. Have some basic knowledge of the Python programming language

1. Have a data lake Instance provisioned and configured. For instructions on how to provision an instance one can refer to the following - [Configure the SAP HANA data lake File Container](https://help.sap.com/docs/SAP_HANA_DATA_LAKE/b239ed4bb73a4f07886657e237f1875f/afe91bfba419464a84b7a05e7960d6f9.html). [Managing Data Lake Files | SAP Help Portal](https://help.sap.com/docs/SAP_HANA_DATA_LAKE/b239ed4bb73a4f07886657e237f1875f/afe91bfba419464a84b7a05e7960d6f9.html)

1. Have the REST API Endpoint and Instance ID for your data lake Instance handy.

1. Have access to a Jupyter notebook.

**Overview:**

In this blog, we will learn how to use the SAP HANA data lake REST API to Create/Write, Access/Read and list your files through a python script. The REST API reference documentation link can be found at ([SAP HANA Cloud, Data Lake Files REST API](https://help.sap.com/doc/9d084a41830f46d6904fd4c23cd4bbfa/2022_3_QRC/en-US/html/index.html)), and it may be used to access the file containers of the SAP HANA data lake. The Python demonstrations that follow, however, use some of the most typical endpoints. We will learn how to use a Python http client to fire a http request and then parse a response status and get response body data. In this post on python http module, we will try attempting making connections and making http requests like GET, POST, PUT, DELETE. Let’s get started.

**Step 1: Making a http connection to data lake**

Copy and paste your client.key and client.crt in the relative path where your python script is placed (Home of the Jupyter Notebook).

The first step over here is to import http.client package for making HTTP requests and will set some commonly re-used variables for the API calls. Add the following at the top of a Python script and populate the variables with the proper information for your SAP HANA data lake file container.

We use the http client to get a response and a status from the URL (i.e., FILES REST API)

The code will validate the client certificate and client key too. So, I would recommend to moving the certs into the same directory as your script and just use a relative path.

use "./<certname.crt>" as the filepath when they are in the same directory as your script.

use "./<keyname.key>" as the filepath when they are in the same directory as your script.

![](/legacyfs/online/storage/blog_attachments/2022/12/Picture1-33.png)

**Step 2: Write/Create a file to the data lake File Store**

To Write/Create a file into the data Lake File Store, we will use the PUT request method supported by http.

**PUT http Method**

+ PUT requests are used to change data on the server. It replaces the entire content at a specific location with data from the body payload. If no resources match the request, one will be generated.

+ The PUT method requests that the enclosed entity be stored under the supplied URI. If the URI refers to an already existing resource, it is modified and if the URI does not point to an existing resource, then the server can create the resource with that URI.

The following code sets up the API call to the CREATE endpoint and will upload a file to the folder specified in your SAP HANA data lake File Store.

![](/legacyfs/online/storage/blog_attachments/2022/12/Picture2-16.png)

The above code will create a file in the data lake File Store under the “**test**” directory as “**MYFIRSTAPIFILE**” and the message will be given under the parameter file = “Welcome to the SAP blog about Accessing SAP HANA Cloud, data lake Files from Python”.

***DBX Screenshot***

![](/legacyfs/online/storage/blog_attachments/2022/12/Picture3-14.png)

**Step 3: Access/Read the file that was created above in the data lake File Store**

To Access/Read a file from the data Lake File Store, we will use the GET request method supported by HTTP.

The GET() method sends a GET request to the specified url. GET request is the most common method and is used to obtain the requested data from the specific server.

The get method will display the contents of the file mentioned in the file path (f\_path)

The following code sets up the API call to the OPEN endpoint and will print your file contents.

![](/legacyfs/online/storage/blog_attachments/2022/12/Picture4-11.png)

**Output will be:**

![](/legacyfs/online/storage/blog_attachments/2022/12/Picture5-9.png)

**One can also download the file from DBX and open the file content in notepad**

![](/legacyfs/online/storage/blog_attachments/2022/12/Picture6-8.png)

**Step 4: Print the list of directories/files in your data lake File Store**

The GET() method is also used to specify the directories and all the files present within those directories.

Under the file path (f\_path) we need to mention a “/” which means that the GET request will fetch all the directories and the files within those directories, which are present in the data lake File Store.

The following code sets up the API call to the LISTSTATUS endpoint and will print the list of directories and files in your SAP data lake File Store.

And it will also display the type of the contents. i.e., whether it’s a ***file*** or a ***directory***.

![](/legacyfs/online/storage/blog_attachments/2022/12/Picture7-8.png)

The output will be:

![](...