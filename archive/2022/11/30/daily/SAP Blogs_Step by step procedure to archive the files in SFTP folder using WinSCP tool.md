---
title: Step by step procedure to archive the files in SFTP folder using WinSCP tool
url: https://blogs.sap.com/2022/11/29/step-by-step-procedure-to-archive-the-files-in-sftp-folder-using-winscp-tool/
source: SAP Blogs
date: 2022-11-30
fetch_date: 2025-10-04T00:04:24.686951
---

# Step by step procedure to archive the files in SFTP folder using WinSCP tool

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Step by step procedure to archive the files in SFT...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/161858&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Step by step procedure to archive the files in SFTP folder using WinSCP tool](/t5/technology-blog-posts-by-sap/step-by-step-procedure-to-archive-the-files-in-sftp-folder-using-winscp/ba-p/13561924)

![Krishnakumar_Sukumaran85](https://avatars.profile.sap.com/3/6/id36668215eea042655cdd2283c6cab7bcf758f7bc7c325bb99fca6c39dd9b9ae6_small.jpeg "Krishnakumar_Sukumaran85")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Krishnakumar\_Sukumaran85](https://community.sap.com/t5/user/viewprofilepage/user-id/44512)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=161858)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/161858)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13561924)

‎2022 Nov 29
9:10 PM

[3
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/161858/tab/all-users "Click here to see who gave kudos to this post.")

4,608

* SAP Managed Tags
* [SAP Cloud Integration for data services](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520Integration%2520for%2520data%2520services/pd-p/67838200100800005117)

* [SAP Cloud Integration for data services

  SAP Integration Suite](/t5/c-khhcw49343/SAP%2BCloud%2BIntegration%2Bfor%2Bdata%2Bservices/pd-p/67838200100800005117)

View products (1)

Hello Everyone!

Here I am, again sharing some more knowledge on the Cloud Integration topic. This blog is about achieving files, not in the Agent server but in the SFTP folder! Are you excited? Let’s continue then.

## Introduction:

When you really need to archive the files? This is a valid question when you are using the file as Sources to your Interfaces. Normally, which ever program generates this file will overwrite it, correct? But what if there is a timestamp associated with the file name? Here, the file name changes in every extraction, and it will create multiple files in the folder. Or sometimes customer wants to archive it for error handling checks. Whatever be the reason, it is possible with WinSCP tool. Is there a straight way to do this from Post load script? You can explore on that, but this is a workaround.

## Prerequisite:

You need the Agent active and running, SFTP connections details and a valid credentials, SFTP datastore created and tested and WinSCP tool is installed in the Agent server. A folder created in the Agent server which is added in the Whitelisted Directories. You can check my other blog [here](https://blogs.sap.com/2022/11/24/step-by-step-procedure-to-establish-ci-ds-to-sftp-file-server-connection/) to learn how to create an SFTP datastore.

## Read the file with timestamp:

First, how will you read a file which has a timestamp associated with the name? Normally, we give the filename as it is, and interface will read the file. But when the filename has a timestamp, it changes in each extraction, and we don’t know it. The solution is, create a global variable and use a wildcard character in the name and we use \* for this.

For example, let the filename be Location\_20221129103000.csv. Create a global variable $G\_FILENAME and assign the value in the Preload script as ‘Location\_\*.csv’ and use it in the data flow. This will read the Location\_20221129103000.csv file and load the data. But there is a problem associated with this. Since the timestamp is different in each extraction, it create multiple files with name starting as ‘Location\_’ i.e., Location\_20221129103000.csv in the first run and Location\_20221129103500.csv in the second run and so on. So, when you run the interface, it will pick up all the files which starts with ‘Location\_’ since we use wildcard in the name and end up loading the same data again with the new file. So, in this case archiving is a must. Let’s see how to do that in the below sections.

## Archive the files:

I have already provided the link on how to create the SFTP datastores in the Prerequisite section. Please follow that and create the datastores. Then create your interface based on the requirement. Since you use the SFTP folder as Source, you already be using a tool like WinSCP or Cyberduck to access these folders. Create the Archived folder in the SFTP server preferably in the same folder. Here you can archive individual files or a bunch of files in to same or different folders. Here I am explaining how to use WinSCP tool to archive a single file where the Agent is installed in a Windows server and the SFTP folder is in a Linux server.

First, go to the Agent server and create a folder called ‘File\_Archive’ and this folder should be whitelisted. This is the place where you are going to keep your archiving codes. You need to create two files, the first one is to write the code to move the file to the Archived folder and the second one is to call this first file using WinSCP tool.

1. The first file is a txt file, and you can name it as per your interface. Fill it up with the below code and replace the texts in <> with the SFTP details.

*# Connect to SFTP server using a password*

open sftp://<user>:<password>@<SFTP server name> -hostkey="ssh-rsa 2048 <Host key Fingerprint>"

*# Move file*

mv <File name with folder path> <Archived folder path>

*# Exit WinSCP*

exit

A simple example will be as follows.

open sftp://user:password@example.com -hostkey="ssh-rsa 2048 xxxxxxxxxxx..."

Since we have timestamp in the filename, you can use the wildcard character in the filename.

2. The second file is a bat file, and name it like the first file. Fill it up with the below code and replace the texts in <> with the SFTP details.

*[@echo](/t5/user/viewprofilepage/user-id/3847) off*

winscp.com /script=<First file name.txt with folder path>

Since you are keeping this file in a different folder other than the WinSCP installation folder, include the folder path of WinSCP installation folder like "C:\Program Files (x86)\WinSCP\winscp.com" in double quotes and there shouldn’t be a space after the /script=.

Please note, here the Agent is installed in a Windows server. If the Agent is installed in a Linux server, you need to make the changes for that especially the backslash.

Now you have created both the txt and bat files in the Agent server, the next step is to call them from the Post load script of the interface.

Use the below script to execute the bat file in the Post load Script.

$G\_STATUS = exec('bat file name with the folder path', ' ', 8);

Here we use the Flag value as 8 so that it returns the concatenation of the return code and the standard error.

Yes, you have completed the steps to archive the files in SFTP folder and now run your interface and test whether the archiving is working. If you use the WinSCP tool to access the files, refresh the folder if the file is still showing there.

## Conclusion:

After reading th...