---
title: How to Send Email Notifications from an Emarsys Automation Program via a Webhook
url: https://blogs.sap.com/2023/08/19/how-to-send-email-notifications-from-an-emarsys-automation-program-via-a-webhook/
source: SAP Blogs
date: 2023-08-20
fetch_date: 2025-10-04T11:59:14.148618
---

# How to Send Email Notifications from an Emarsys Automation Program via a Webhook

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [CRM and Customer Experience](/t5/crm-and-customer-experience/ct-p/crm)
* [CRM and CX Blog Posts by Members](/t5/crm-and-cx-blog-posts-by-members/bg-p/crm-blog-members)
* How to Send Email Notifications from an Emarsys Au...

CRM and CX Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/crm-blog-members/article-id/6446&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How to Send Email Notifications from an Emarsys Automation Program via a Webhook](/t5/crm-and-cx-blog-posts-by-members/how-to-send-email-notifications-from-an-emarsys-automation-program-via-a/ba-p/13579659)

![canakalin](https://avatars.profile.sap.com/f/9/idf9d49010b7ad4c27b337c3e223430f0a311d082c4efb690e1323441b5042a364_small.jpeg "canakalin")

[canakalin](https://community.sap.com/t5/user/viewprofilepage/user-id/42523)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=crm-blog-members&message.id=6446)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/crm-blog-members/article-id/6446)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13579659)

‎2023 Aug 19
7:00 PM

[4
Kudos](/t5/kudos/messagepage/board-id/crm-blog-members/message-id/6446/tab/all-users "Click here to see who gave kudos to this post.")

2,697

* SAP Managed Tags
* [SAP Integration Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integration%2520Suite/pd-p/73554900100800003241)
* [SAP Emarsys API](https://community.sap.com/t5/c-khhcw49343/SAP%2520Emarsys%2520API/pd-p/0baac4a2-791a-429e-a5aa-a3e5f327a77d)
* [SAP Emarsys Tactics](https://community.sap.com/t5/c-khhcw49343/SAP%2520Emarsys%2520Tactics/pd-p/5072f9b0-8b7f-44d9-a020-a2113cf68d8e)
* [Cloud Integration](https://community.sap.com/t5/c-khhcw49343/Cloud%2520Integration/pd-p/67837800100800006801)
* [Customer Experience](https://community.sap.com/t5/c-khhcw49343/Customer%2520Experience/pd-p/cae17fd6-917e-483d-881a-502155cade3c)
* [SAP Emarsys](https://community.sap.com/t5/c-khhcw49343/SAP%2520Emarsys/pd-p/73554900100800003661)

* [Cloud Integration

  SAP Integration Suite](/t5/c-khhcw49343/Cloud%2BIntegration/pd-p/67837800100800006801)
* [Customer Experience

  Topic](/t5/c-khhcw49343/Customer%2BExperience/pd-p/cae17fd6-917e-483d-881a-502155cade3c)
* [SAP Integration Suite

  SAP Integration Suite](/t5/c-khhcw49343/SAP%2BIntegration%2BSuite/pd-p/73554900100800003241)
* [SAP Emarsys API

  Additional Software Product](/t5/c-khhcw49343/SAP%2BEmarsys%2BAPI/pd-p/0baac4a2-791a-429e-a5aa-a3e5f327a77d)
* [SAP Emarsys Tactics

  Additional Software Product](/t5/c-khhcw49343/SAP%2BEmarsys%2BTactics/pd-p/5072f9b0-8b7f-44d9-a020-a2113cf68d8e)
* [SAP Emarsys

  Software Product](/t5/c-khhcw49343/SAP%2BEmarsys/pd-p/73554900100800003661)

View products (6)

**The Business Requirement:**

Our imaginary customer utilizes an Emarsys Contact Form on their main website as a contact form. We can also use custom forms but this is a topic of another blog. After a contact fills out the form, an automation program is triggered with a Form Entry Point. The contact enters the automation program. As you see from the contact form below, there is a field as the topic of request and this field determines the choice of department that the contact wants to reach.

Our customer requires that for some departments, we need to send departmental email notifications to different departmental email inboxes. For example, if the contact chooses HR as the topic of request, an email should be sent to the HR department. And, Emarsys doesn’t provide this functionality as standard. And in Emarsys, only the contact who enters the program can receive emails from Emarsys with a “Send Email” channel node.

Firstly, It would be better to explain how Emarsys Forms behave. All the information on the form has an equivalent field on the contact database. Let's say, salutation is a standard field on the contact object. But the topic of request and comment fields are custom fields. When the contact fills out the form, the information basically is going to be saved to the contact's fields. And you can use these fields to send emails or create leads on c4c via a webhook. If a contact is already existing with the email address, they update the fields but if no contact exists with that email address, a new contact is created. Basically, the standard field "email" is the unique identifier for the contacts in the Emarsys Forms.

![](/legacyfs/online/storage/blog_attachments/2023/08/form1-1.png)

As you see in the automation program below, the contact can choose to contact with HR or Finance department, in this case, we want to send all the information that the contact has filled out on the forms to these departments. Or if the contact chooses the Sales department, we can create a lead on C4C. The real use cases can be much more complicated. That is why, I am showing a simple use case here to help us focus on our real topic which is sending departmental notifications.

![](/legacyfs/online/storage/blog_attachments/2023/08/automation2.png)

**Steps to do:**

1. Creation of the Webhook

On the Webhook Creation page, we need to create the payload with the contact fields and map these payload fields to the Emarsys contact fields. You can refer to the screenshot below:

![](/legacyfs/online/storage/blog_attachments/2023/08/webhook3.png)

The payload would look like this if the webhook is triggered:

Example JSON payload:

{  "salutation": "1",  "first\_name": "Can",  "last\_name": "Akalin",  "email": "canakalin@test.com",  "company": "Test Co",  "your\_department": "3",  "website": "[www.test.com](http://www.test.com)",  "zipcode": "34655",  "street": "Kozyatağı",  "house\_number": "3121",  "city": "Istanbul",  "country": "178",  "phone": "+9055555555",  "topic\_of\_request": "HR",  "comment": "I want to contact to HR department",  "notification\_email": "test@outlook.com",  "contact\_form": "Contact Form"}

![](/legacyfs/online/storage/blog_attachments/2023/08/iflow2.png)

And also after we complete the iflow design and deploy it. We need to put a runtime endpoint here to be able to trigger the iflow. And of course the basic authentication details.

**Steps to do before designing the iflow:**

1. Outlook(my preferred Email Service Provider) connection to Integration Suite will be needed. A test Outlook account will be used for testing purposes. Later on, you can use your real email inbox.

**OUTLOOK SMTP:** smtp.office365.com

Port: 587

Proxy Type: Internet

Protection: STARTTLS

2. Integration Suite’s “Test Connectivity” Functionality can be used to validate the certificates for Outlook. Later on, these certificates will be added to *Manage Security -->**Keystore* in the Integration Suite. Screenshot below:

![](/legacyfs/online/storage/blog_attachments/2023/08/certificate1.png)

3. Click add --> Certificate. And then upload the certificates that you have downloaded from the Connectivity Test.

![](/legacyfs/online/storage/blog_attachments/2023/08/certificate2.png)

![](/legacyfs/online/storage/blog_attachments/2023/08/addcertificate-1.png)

4. Let's say we have an Outlook inbox with an email inbox like "test@outlook.com" and a password. We need to define this password in Manage Security --> Security Material of Integration Suite as we did something similar for the certi...