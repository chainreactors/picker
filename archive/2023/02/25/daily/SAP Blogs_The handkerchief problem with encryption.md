---
title: The handkerchief problem with encryption
url: https://blogs.sap.com/2023/02/24/the-handkerchief-problem-with-encryption/
source: SAP Blogs
date: 2023-02-25
fetch_date: 2025-10-04T08:03:56.340371
---

# The handkerchief problem with encryption

* [SAP Community](/)
* [Groups](/t5/groups/ct-p/groups)
* [Interest Groups](/t5/interest-groups/ct-p/interests)
* [Application Development and Automation](/t5/application-development-and-automation/gh-p/application-development)
* [Blog Posts](/t5/application-development-and-automation-blog-posts/bg-p/application-developmentblog-board)
* The handkerchief problem with encryption

Application Development and Automation Blog Posts

Learn and share on deeper, cross technology development topics such as integration and connectivity, automation, cloud extensibility, developing at scale, and security.

All communityThis groupBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/application-developmentblog-board/article-id/46903&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

#### We have launched new [Developer forums/groups](https://community.sap.com/t5/developers/ct-p/developers) in the SAP Community. If you are here to publish developer- or SAP-technology related blog posts, please check out our new groups instead. You can find more information about the developer forums in this [What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147).

Read only

## [The handkerchief problem with encryption](/t5/application-development-and-automation-blog-posts/the-handkerchief-problem-with-encryption/ba-p/13557149)

![patrickboch](https://avatars.profile.sap.com/f/6/idf6143391748ca7e02d8d3cbf1b1c722e1421224959f4cf676cef357a936fb8b4_small.jpeg "patrickboch")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[patrickboch](https://community.sap.com/t5/user/viewprofilepage/user-id/727153)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=application-developmentblog-board&message.id=46903)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/application-developmentblog-board/article-id/46903)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13557149)

‎2023 Feb 24
6:01 PM

[10
Kudos](/t5/kudos/messagepage/board-id/application-developmentblog-board/message-id/46903/tab/all-users "Click here to see who gave kudos to this post.")

1,082

* SAP Managed Tags
* [Security](https://community.sap.com/t5/c-khhcw49343/Security/pd-p/49511061904067247446167091106425)

* [Security

  Topic](/t5/c-khhcw49343/Security/pd-p/49511061904067247446167091106425)

View products (1)

When we speak to customers about security, we often hear the requirement for “more encryption”. Which makes sense, doesn’t it? After all, with todays’ encryption algorithms, anyone who is able to steal encrypted data cannot really do anything with them without asking a supercomputer - who then would be busy decrypting for the next 7 million years (only to come up with the answer “42”). Well, unfortunately it’s not that easy.

And when I’m saying encryption is not easy, I’m not even referring to the differences in asymmetric vs. symmetric encryption or the different types of encryption algorithms (we’ll get into details of those in future posts). I will not even go into the details of different layers where encryption is important. Rather, for the purposes of this article, I’d like to view the encryption from the perspective of the application.

Firstly, it's important to understand that – quite understandably – vendors like to promote their solution as having superior encryption. The reality is quite different, however. One reason for this is the standardization of encryption, a second reason can be found within the nature of todays’ application architecture and the third reason doesn’t even have to do anything with encryption or even technology, for that matter.

The first reason is quickly covered: any technology solution today does not exist in a vacuum. On the contrary, in a highly connected world, solutions need to be able to communicate, even when encrypted data is involved. Hence, most encryption is standardized and pressed into three letter acronyms such as TLS, SSL or AES.

Secondly, viewing encryption from an application perspective: It would obviously best if the application could process data even when it is encryption and only the decrypted values would be displayed in the User Interface (UI side encryption). Put differently: it would be great if the application knew that

*PQPM7aCOxurcuhlI7Exdjw==*

multiplied with

*BrDwPV2s6Xri6jndOt4NYg==*

equals

*O0HrSmCSBNW6ugKA7N2ZMg==*

You already see the problem? Any application knows that 6 x 7 = 42 – the same example I used above, but encrypted. However, in order to be able to perform this calculation, the application needs to know the key the plain text was encrypted with.

> *Side note: Theoretically this is even possible without the application knowing the key. The term for this is “homomorphic encryption”, but it’s light years away from being commercially viable.*

In other words: the application – at some point – needs to decrypt the data, and doing so requires the encryption key. So far for the theory, now let’s see what this means in a typical solution architecture today.

The real question customers should ask is: Who do they want to protect against and "how do bad actors retrieve their precious data" or "who are these bad actors anyway?". Some examples:

* If you implement filesystem encryption and database volume encryption (often referred to “transparent data encryption”, or TDE), you are protecting against the administrator of the infrastructure (i.e. they will not be able to view the data in plain text). However, the database admin or the application admin will still be able to see the data.

* If you want to prevent the database admin to see data, you will need to implement application side encryption. This encrypts data within the database but is transparent to the application. In other words, depending on their access rights, application users might still be able to see the data.

* If you want to make absolutely sure that the application administrator also doesn’t view any data, you will have to resort to the UI-side encryption which I mentioned above – which, however, makes a processing of data impossible.

And now we’re finally getting to the heart of the matter.

Application Side encryption means that encrypted data is sent to the application and will stay encrypted until the application actually uses the data. If the data is used, the application will decrypt it, process it, and encrypt it again after use. This particular process – simplified – requires two things:

1. The database needs to support it

2. The application needs (a function) to support it.

Modern databases, such as SQL Server, Oracle Database or SAP HANA provide this support – and if you were to write a new application on top of either one of these databases, you can implement this support on the application side, too.

However, complex applications (MS dynamics, Oracle ERP and also SAP ERP) which have been around before databases supported that kind of encryption do not support application side encryption.

Is it possible to implement such a function in an “aged” application? It sure is – but it’s simply too much effort: these complex applications contain millions of lines of codes, with a similar number of dependencies within the code, so it would probably take years – even for corporations the size of Microsoft, Oracle or SAP – to implement full application side encryption.

Nevertheless, you sometimes hear the phrase “Microsoft (or Oracle) are able to provide this level of encryption”. And you might be surprised that I see this phrase as...