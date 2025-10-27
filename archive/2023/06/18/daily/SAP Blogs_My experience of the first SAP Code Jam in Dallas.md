---
title: My experience of the first SAP Code Jam in Dallas
url: https://blogs.sap.com/2023/06/17/my-experience-of-the-first-sap-code-jam-in-dallas/
source: SAP Blogs
date: 2023-06-18
fetch_date: 2025-10-04T11:45:46.103853
---

# My experience of the first SAP Code Jam in Dallas

* [SAP Community](/)
* [Groups](/t5/groups/ct-p/groups)
* [Activity Groups](/t5/activity-groups/ct-p/activities)
* [SAP CodeJam](/t5/sap-codejam/gh-p/code-jam)
* [Blog Posts](/t5/sap-codejam-blog-posts/bg-p/code-jamblog-board)
* My experience of the first SAP Code Jam in Dallas

SAP CodeJam Blog Posts

Check out SAP CodeJam blog posts to get updates and learn from attendees, instructors, and experts. Share your own expertise with the community.

All communityThis groupBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/code-jamblog-board/article-id/597&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [My experience of the first SAP Code Jam in Dallas](/t5/sap-codejam-blog-posts/my-experience-of-the-first-sap-code-jam-in-dallas/ba-p/13563035)

![SergioG_TX](https://avatars.profile.sap.com/9/2/id92bc2ff8ac19a7df140625dde4eca4181cb1b20d70c265d007ba33edfbeef8a3_small.jpeg "SergioG_TX")

![SAP Champion](/html/@B3DACAC6163F980483AC32558EB69695/rank_icons/champion-rank-16x16.svg "SAP Champion")
[SergioG\_TX](https://community.sap.com/t5/user/viewprofilepage/user-id/39917)

SAP Champion

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=code-jamblog-board&message.id=597)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/code-jamblog-board/article-id/597)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13563035)

‎2023 Jun 17
10:45 PM

[5
Kudos](/t5/kudos/messagepage/board-id/code-jamblog-board/message-id/597/tab/all-users "Click here to see who gave kudos to this post.")

1,087

* SAP Managed Tags
* [SAP CodeJam](https://community.sap.com/t5/c-khhcw49343/SAP%2520CodeJam/pd-p/523757421691906837442183267052576)

* [SAP CodeJam

  Event](/t5/c-khhcw49343/SAP%2BCodeJam/pd-p/523757421691906837442183267052576)

View products (1)

## Hello community,

I would like to share my experience of the first SAP Code JAM in Dallas, TX (held at the SAP Plano office) were not only we had our first Code JAM ever, but also the Developer Advocates presented their first dual topic Code Jam; #RAP and #CAP.

![](/legacyfs/online/storage/blog_attachments/2023/06/logo.jpg)

The event was organized by the developer advocates rich.heilman , thomas.jung and riley.rainey  This event came up during one of the Linked in posts from Rich asking the community where they would want to have the next code jam. I responded, Dallas, as I would like to see more community growth. I do not see enough active participants as I notice in other cities around the world. Without hesitation, I immediately got response from Rich, so I started helping promote the event. I have been leading the [Dallas SAP community group](https://groups.community.sap.com/t5/dallas/gh-p/dallas) but I also notice lack of awareness and participation there. If you’re reading this blog and you’re from Dallas or nearby, please join the group and help with ideas on SIT, Code Jams, Stammtisch or any other community event you would like to participate or lead. After all, this is from the community to the community.

Getting back to the event details, we had a mix of talented people ranging in experience from various industries such as Oil and gas, DoD, utilities, communication media; independent consultants,  and even a UTD college senior participant putting his time in to get to know the topics as well as other community members.

### **ABAP and RAP**

The first half of the event started with Rich explaining #RAP, a little history of the ABAP stack and then a demonstration of how to work with RAP.

![](/legacyfs/online/storage/blog_attachments/2023/06/RAP-img-scaled.jpg)

There was an exercise for learning ABAP as a pre-requisite to get more familiar with RAP.  The exercise is found on a free git repo here <https://github.com/SAP-samples/abap-exercises-codejam>

What I learned from the RAP session:

* Eclipse with ADT plugin is how ABAP and RAP is developed; should you need Fiori development, you may use the BAS or VS code with its required plugins

* A BTP instance was required to perform the exercise. We used the local tier one

* The exercise required to authenticate against the BTP account using the provided key (from the git repo) and then we created local packages for our project.

-We started by creating a Hello World program – this is the step where I became an expert – jk -

Then, we created class methods, service definitions, service bindings and finally consumed the data from the browser. There were 4 or 5 exercises in the git repo instructions and in my opinion they were easy to follow – for someone like me without background in ABAP.

![](/legacyfs/online/storage/blog_attachments/2023/06/rap.jpg)

### **CAP, BTP, BAS**

The next presentation of the day was done by Thomas and it was about the CAP (cloud application programming model). Thomas showed similarities between CAP and RAP when it comes to data modeling using CDS (Core Data Services).

![](/legacyfs/online/storage/blog_attachments/2023/06/thomas.png)

Both, Rich and Thomas showed the preview Fiori app that can be generated from the OData metadata and annotations. The CAP project instructions can be found in the public git repo --> <https://github.com/SAP-samples/cap-hana-exercises-codejam>.

Thomas also showcased the use of the terminal window building the cap application, connecting to the HANA database using the plugin icon, deploying the changes using the rocket icon - all these neat tools already available from the Business Application Studio.

I did not participate in this exercise because I had already done it; read more about it next --> [my blog about CAP](https://blogs.sap.com/2023/04/14/my-head-is-on-the-cloud-my-learnings-about-capm/)

### **CAP / RAP and Event Mesh**

Next, after we completed the exercises, we had a bonus example/demo of how RAP and CAP can easily interact with [Event Mesh](https://help.sap.com/docs/SAP_EM/bf82e6b26456494cbdd197057c09979f/df532e8735eb4322b00bfc7e42f84e8d.html) . It was easy to see how from ABAP, the program raises an event and that event is invoked from the ABAP stack. The same concept was shown to listen for the event on a function.

From CAP, Thomas also showed a NodeJs script invoking the same event. It was neat to see how the events can be invoked from both programing models.

![](/legacyfs/online/storage/blog_attachments/2023/06/codejammers.jpg)

### **Questions from the audience**

During the presentations, some participants shared some of the following questions:

* Where can someone learn CAP – <https://cap.cloud.sap/docs/get-started/jumpstart>, there is also a youtube channel for the developer news - <https://www.youtube.com/watch?v=ZnzO-0UftgI&t=23s>

* Similarities of CAP and RAP – CDS, annotations, XSOData, RESTful API – explained by both Rich and Thomas

* What’s the best way to learn CAP? – there is no single site to learn this programming model. It requires knowledge from JavaScript, NodeJS, understanding the cloud foundry hierarchy, security model, tools (BAS or VS code)

* What is better CAP or RAP? [probably the question everyone has, sometimes not asked] it really depends on what is available in your company, what is supported by the system and most importantly, the developers available.

* How can CAP call Event Mesh – Thomas showed it – here is some additional documentation <https://cap.cloud.sap/docs/guides/messaging/#add-or-update-reviews>

### **Final thoughts**

I went to the event knowing t...