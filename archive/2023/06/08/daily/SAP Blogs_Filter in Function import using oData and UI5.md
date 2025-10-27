---
title: Filter in Function import using oData and UI5
url: https://blogs.sap.com/2023/06/07/filter-in-function-import-using-odata-and-ui5/
source: SAP Blogs
date: 2023-06-08
fetch_date: 2025-10-04T11:47:16.107950
---

# Filter in Function import using oData and UI5

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Filter in Function import using oData and UI5

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160675&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Filter in Function import using oData and UI5](/t5/technology-blog-posts-by-members/filter-in-function-import-using-odata-and-ui5/ba-p/13553729)

![ayaza2894](https://avatars.profile.sap.com/e/9/ide9684720591cf62cd76db729e4c8ad047c0d472b5114270909492a809e73f049_small.jpeg "ayaza2894")

[ayaza2894](https://community.sap.com/t5/user/viewprofilepage/user-id/139457)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160675)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160675)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13553729)

‎2023 Jun 07
11:02 PM

[8
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160675/tab/all-users "Click here to see who gave kudos to this post.")

20,456

* SAP Managed Tags
* [OData](https://community.sap.com/t5/c-khhcw49343/OData/pd-p/551580658536717501828021060147962)
* [SAPUI5](https://community.sap.com/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)
* [SAP Gateway](https://community.sap.com/t5/c-khhcw49343/SAP%2520Gateway/pd-p/01200615320800003185)

* [SAP Gateway

  SAP NetWeaver](/t5/c-khhcw49343/SAP%2BGateway/pd-p/01200615320800003185)
* [OData

  Programming Tool](/t5/c-khhcw49343/OData/pd-p/551580658536717501828021060147962)
* [SAPUI5

  Programming Tool](/t5/c-khhcw49343/SAPUI5/pd-p/500983881501772639608291559920477)

View products (3)

Hi Everyone, I am writing this blog for beginners on how to filter the data using function Import in SAP UI5 using OData which will be helpful for both front end and back end developer.

Function imports are used to do the GET and POST operations for the requirements , which are not possible by the standard operations available in OData.

Sometimes we may want to filter the data based on names or city(non key value), that time we can use function import.

We will implement the function import code inside EXECUTE\_ACTION  method by redefining this method in the DPC Extension class.

Steps to create Function Import as follows.

First we will create function import in odata.

Step1:- Create a table. Use t-code se11

![](/legacyfs/online/storage/blog_attachments/2023/06/pic1.png)

CREATING A TABLE

![](/legacyfs/online/storage/blog_attachments/2023/06/pic2-1.jpg)

enter the info

here we will create field and we will give data element.

![](/legacyfs/online/storage/blog_attachments/2023/06/PIC3-1.jpg)

click on data element of phone.

![](/legacyfs/online/storage/blog_attachments/2023/06/PIC4-2.jpg)

click yes

![](/legacyfs/online/storage/blog_attachments/2023/06/PIC5-2.jpg)

here you have to give domain name.

![](/legacyfs/online/storage/blog_attachments/2023/06/PIC6-1.jpg)

here give data type name and no. of character

then activate it.

![](/legacyfs/online/storage/blog_attachments/2023/06/ALL.png)

Table

we have to go to enhancement category

click on more---extras--- click on Enhancement category.

![](/legacyfs/online/storage/blog_attachments/2023/06/ENHANCE.png)

enhancement of data

![](/legacyfs/online/storage/blog_attachments/2023/06/CANNOT.png)

![](/legacyfs/online/storage/blog_attachments/2023/06/DATACLASS.png)

select data class

now activate the table.

After this, Enter the data in table.

more---utilities---table content---create entries.

![](/legacyfs/online/storage/blog_attachments/2023/06/TABLE-ENTRIES.png)

table entries

![](/legacyfs/online/storage/blog_attachments/2023/06/pic2.jpg)

table data

Step2:- Go to SEGW and create a new project.

Give project name and save in local object or package.

![](/legacyfs/online/storage/blog_attachments/2023/06/pic3.jpg)

project created

![](/legacyfs/online/storage/blog_attachments/2023/06/pic4-1.jpg)

now your project will look like this

Step3:- Right click on Data Model and select import and then select DDIC structure.

![](/legacyfs/online/storage/blog_attachments/2023/06/pic5-1.jpg)

Give Name and table name and click next.

![](/legacyfs/online/storage/blog_attachments/2023/06/pic6.jpg)

![](/legacyfs/online/storage/blog_attachments/2023/06/DDIC.png)

Select table name and click next

![](/legacyfs/online/storage/blog_attachments/2023/06/ISKEY.png)

select is Key and click on finish.

now generate runtime artifacts.

![](/legacyfs/online/storage/blog_attachments/2023/06/runtime.png)

runtime artifacts generated

Step4:- Right Click on data model, select create and then click on function import.

![](/legacyfs/online/storage/blog_attachments/2023/06/fun.png)

Give Function import name and click on continue.

![](/legacyfs/online/storage/blog_attachments/2023/06/pic1-1.png)

Fill like this.

![](/legacyfs/online/storage/blog_attachments/2023/06/pic2.png)

Now project look like this .

Click on function import folder and fill the following.

What you want to search you can give the Name.

![](/legacyfs/online/storage/blog_attachments/2023/06/pic3.png)

After this, generate runtime artifacts.

Step5:- Click on DPC\_EXT and redine EXECUTE\_ACTION.

![](/legacyfs/online/storage/blog_attachments/2023/06/pic4.png)

Write this code in execute\_action method.

Come back to segw.

Click on Service maintanence and register. Give Local and select continue and then select Local package.

![](/legacyfs/online/storage/blog_attachments/2023/06/pic6.png)

After this ,Click on SAP Gateway client and select yes.

Step6:- Give Function Import name followed by what you want to display the data

![](/legacyfs/online/storage/blog_attachments/2023/06/segw.png)

Here I have given Designation=’DEVELOPER’.

So only developer data will be visible.

This is about oData function import.

----------------------------------------------------------------------------------------------------------------------------

Function Import using UI5 in VS code

if you have not installed vs code, install vs code and node js.

open vs code--- click on view---then command palette---then explore and install generator.

![](/legacyfs/online/storage/blog_attachments/2023/06/1-17.png)

install all generator

Step1:- Create new project(click on view---then command palette---click on fiori: open application generator).

![](/legacyfs/online/storage/blog_attachments/2023/06/2-10.png)

select basic

Step2:- Select service of function import.

data source as connect to a system.

system:- destination configuration

service as segw function import service.

![](/legacyfs/online/storage/blog_attachments/2023/06/3-11.png)

click on next.

Give View name and project name and click on finish.

After this project template will be generated.

step3:- First we will create a json model to store the data.

click on model---create a file as data.json

![](/legacyfs/online/storage/blog_attachments/2023/06/json.png)

json model

Configure in manifest.json

![](/legacyfs/online/storage/blog_attachments/2023/06/name.png)

Here “data” is named model.

step4:- in View .

vi...