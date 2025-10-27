---
title: SAP Interfaces & OOP
url: https://blogs.sap.com/2023/02/26/sap-interfaces-oop/
source: SAP Blogs
date: 2023-02-27
fetch_date: 2025-10-04T08:10:56.962577
---

# SAP Interfaces & OOP

* [SAP Community](/)
* [Groups](/t5/groups/ct-p/groups)
* [Interest Groups](/t5/interest-groups/ct-p/interests)
* [Application Development and Automation](/t5/application-development-and-automation/gh-p/application-development)
* [Blog Posts](/t5/application-development-and-automation-blog-posts/bg-p/application-developmentblog-board)
* SAP Interfaces & OOP

Application Development and Automation Blog Posts

Learn and share on deeper, cross technology development topics such as integration and connectivity, automation, cloud extensibility, developing at scale, and security.

All communityThis groupBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/application-developmentblog-board/article-id/46674&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

#### We have launched new [Developer forums/groups](https://community.sap.com/t5/developers/ct-p/developers) in the SAP Community. If you are here to publish developer- or SAP-technology related blog posts, please check out our new groups instead. You can find more information about the developer forums in this [What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147).

Read only

## [SAP Interfaces & OOP](/t5/application-development-and-automation-blog-posts/sap-interfaces-oop/ba-p/13552621)

![sahantissera](https://avatars.profile.sap.com/5/0/id506819b0b7515b47861cd20910ec379f1573b955399685503cfbe84da408a751_small.jpeg "sahantissera")

[sahantissera](https://community.sap.com/t5/user/viewprofilepage/user-id/1646)

Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=application-developmentblog-board&message.id=46674)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/application-developmentblog-board/article-id/46674)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13552621)

‎2023 Feb 26
11:22 AM

[8
Kudos](/t5/kudos/messagepage/board-id/application-developmentblog-board/message-id/46674/tab/all-users "Click here to see who gave kudos to this post.")

34,616

* SAP Managed Tags
* [ABAP Development](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Development/pd-p/833755570260738661924709785639136)

* [ABAP Development

  Programming Tool](/t5/c-khhcw49343/ABAP%2BDevelopment/pd-p/833755570260738661924709785639136)

View products (1)

# Introduction

The reason for writing this post is to provide an overview of how interfaces and OOP concepts can be used in SAP ABAP. Many beginner-level developers working with SAP ABAP may have experience with procedural programming. They may need to be more familiar with OOP concepts like interfaces. By providing a clear explanation of interfaces and how they support OOP programming, readers can better understand how to design and implement modular and maintainable code in SAP ABAP.

SAP ABAP is an object-oriented programming language that supports many OOP concepts, including encapsulation, inheritance, and polymorphism. The Interface is one of the critical tools for implementing these concepts in SAP ABAP.

In this blog post, we'll explore the use of interfaces in SAP ABAP and how they support OOP programming.

In reading this blog, I hope readers can learn:

1. What an interface is and why it's important in OOP programming.

2. How interfaces are defined and implemented in SAP ABAP.

3. Applying interfaces in SAP ABAP can provide standardization, flexibility, modularity, polymorphism, and testability to your code.

4. How to design and implement modular and maintainable code using interfaces and OOP concepts in SAP ABAP.

# What is an Interface?

In OOP programming, an interface is a blueprint or a contract that defines a set of methods that a class must implement. It provides a standard way to define the behaviour of a group of related classes.

# Why Use Interfaces in SAP ABAP?

Interfaces are used in SAP ABAP for several reasons, including:

1. Standardization: Interfaces provide a standard way to define methods that can be used across different classes. This standardization helps to ensure consistency and makes it easier to maintain the code.

2. Flexibility: Interfaces allow you to define a set of methods that a class must implement, but they don't dictate how those methods are implemented. This means you can use different implementations for the same Interface, which gives you more flexibility in designing your code.

3. Modularity: Interfaces help to modularize your code by separating the definition of a method from its implementation. This makes it easier to update or replace the implementation of a method without affecting other parts of the code.

4. Polymorphism: The term polymorphism literally means 'many forms'. Using interfaces, you can allow multiple classes to implement a service differently but using the same.

## What is the difference between an Abstract Class vs an Interface?

* **Multiple Inheritance:**We can achieve multiple inheritances using Interfaces. Since ABAP doesn't support more than one Super class, we can have only one abstract class as a Superclass.

* **New Functionality:**If we add a new method in the Interface, all the implementing classes must implement this method. If we don't implement the method, it will result in a Run-time error. For the Abstract category, if we add a non-abstract way, it's not required to redefine that in each and every inherited class.

* **Default Behavior:**We can have a default behaviour of a non-abstract method in an abstract class. We can't have any implementation in Interface as it only contains the empty stub.

* **Visibility:**All interface components are PUBLIC by default. For the Abstract class, we can set the visibility of each element.

# How to Define an Interface in SAP ABAP?

* In the Repository Browser (transaction SE80), navigate to the package where you want to create an interface.

* In the context menu of the package, choose to Create → Class Library → Interface.
  The Create Interface dialog box appears.or

* You can directly go to the SE24.

* Enter the new class's name according to the [naming conventions](https://help.sap.com/docs/SAP_NETWEAVER_750/bd833c8355f34e96a6e83096b38bf192/92c2b084bc1d11d2958700a0c94260a5.html). The name of the interface should begin with IF\_.
  Example:- ***ZIF\_***.

* In the Description field, enter a short description of the interface.

* Choose Save.

  ![](/legacyfs/online/storage/blog_attachments/2023/02/1-104.png)

  # Summary

  In summary, developers can write more modular, flexible, and maintainable code by leveraging OOP concepts like interfaces in SAP ABAP. By standardizing method definitions across different classes, interfaces can make it easier to maintain code and ensure consistency. Interfaces can also promote flexibility, modularity, and polymorphism and make it easier to test your code.
  In my next blog post, I will explore more complex examples of how interfaces and abstract classes can be used in everyday scenarios.

  You can find more details on the following links:
  [ABAP Topics - SAP Community](https://community.sap.com/topics/abap)
  [Interfaces - Documentation](https://help.sap.com/doc/abapdocu_751_index_htm/7.51/en-us/abeninterfac.htm)

* [abap oop](/t5/tag/abap%20oop/tg-p/board-id/application-developmentblog-board)
* [interface](/t5/tag/interface/tg-p/board-id/application-developmentblog-board)
* [sap abap](/t5/tag/sap%20abap/tg-p/board-id/application-developmentblog-board)
* [se24](/t5/tag/se24/tg-p/board-id/application-developmentblog-board)

6 Comments

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin