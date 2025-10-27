---
title: How to do RSA signature and Base64 by UDF for SAP PO
url: https://blogs.sap.com/2023/03/24/how-to-do-rsa-signature-and-base64-by-udf-for-sap-po/
source: SAP Blogs
date: 2023-03-25
fetch_date: 2025-10-04T10:36:51.945189
---

# How to do RSA signature and Base64 by UDF for SAP PO

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* How to do RSA signature and Base64 by UDF for SAP ...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/162796&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [How to do RSA signature and Base64 by UDF for SAP PO](/t5/technology-blog-posts-by-members/how-to-do-rsa-signature-and-base64-by-udf-for-sap-po/ba-p/13565738)

![tomyoung1](https://avatars.profile.sap.com/0/9/id09046a3ec964ded7f748f5eef58eb2c375a286320ee5b6eb62880ba77c7c5e40_small.jpeg "tomyoung1")

[tomyoung1](https://community.sap.com/t5/user/viewprofilepage/user-id/127456)

Explorer

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=162796)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/162796)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13565738)

‎2023 Mar 24
10:59 PM

[3
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/162796/tab/all-users "Click here to see who gave kudos to this post.")

2,704

* SAP Managed Tags
* [SAP Process Integration](https://community.sap.com/t5/c-khhcw49343/SAP%2520Process%2520Integration/pd-p/01200615320800000719)
* [SAP Process Orchestration](https://community.sap.com/t5/c-khhcw49343/SAP%2520Process%2520Orchestration/pd-p/477916618626075516391832082074785)

* [SAP Process Integration

  SAP NetWeaver](/t5/c-khhcw49343/SAP%2BProcess%2BIntegration/pd-p/01200615320800000719)
* [SAP Process Orchestration

  Software Product](/t5/c-khhcw49343/SAP%2BProcess%2BOrchestration/pd-p/477916618626075516391832082074785)

View products (2)

While doing integration with some soap/rest receiver through SAP PI/PO, they may ask to do RSA signature and Base64 encoding for some of the fields.

The soap/rest receiver should provide the private key to the sender.  When they receive any message with RSA signature by a private key, they will use their own public key to verify the private key to check if the data is sent from a legal sender.

For this kind of requirements, we can do in SAP PI/PO by using Java mapping or UDF.

In this post, I will explain how to use UDF to do RSA signature and Base64.

Before the mapping, the soap/rest receiver should provide the private key to SAP PO.

We are starting at the message mapping as below. (DT MT and SI creation steps are skipped)![](/legacyfs/online/storage/blog_attachments/2023/03/1-11.png)

Figure 1:message mapping

Create the UDF privateKeyEncrypt as below.
![](/legacyfs/online/storage/blog_attachments/2023/03/2-7.png)

*Figure 2:UDF*

The code attached:

public String privateKeyEncrypt(String str, String privateKey, Container container) throws StreamTransformationException{

```
try {

//base64

byte[] decoded = Base64.getDecoder().decode(privateKey);

PrivateKey priKey = KeyFactory.getInstance("RSA").generatePrivate(new PKCS8EncodedKeySpec(decoded));

//RSA

Cipher cipher = Cipher.getInstance("RSA");

cipher.init(Cipher.ENCRYPT_MODE, priKey);

String outStr = Base64.getEncoder().encodeToString(cipher.doFinal(str.getBytes()));

return outStr;

}  catch (Exception e) {

throw new StreamTransformationException(e.getMessage());

}

}
```

Use the UDF for the segment sign. The 2nd input Constant should be the private key provided by the receiver.

![](/legacyfs/online/storage/blog_attachments/2023/03/3-11.png)

*Figure 3: field mapping*

Test:

The string abc will be encrypted and base64 to a different string as below. ![](/legacyfs/online/storage/blog_attachments/2023/03/4-8.png)

*Figure 4: test result*

Please share your feedback or thoughts in a comment

And you can follow the SAP Process Orchestration environment Topic page (<https://community.sap.com/topics/process-orchestration>),
Post and answer questions about SAP Process Orchestration (<https://answers.sap.com/tags/477916618626075516391832082074785>),
and read other posts on the topic (<https://blogs.sap.com/tags/477916618626075516391832082074785/>)

For similar content, please follow my profile(tomyoung1) and I will try to post more in the future.

Thanks!

* [BASE64 Encoder](/t5/tag/BASE64%20Encoder/tg-p/board-id/technology-blog-members)
* [rsa](/t5/tag/rsa/tg-p/board-id/technology-blog-members)
* [sap pipo](/t5/tag/sap%20pipo/tg-p/board-id/technology-blog-members)

2 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fhow-to-do-rsa-signature-and-base64-by-udf-for-sap-po%2Fba-p%2F13565738%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Using Joule’s Async Feature to Communicate with a Custom BTP App](/t5/technology-blog-posts-by-sap/using-joule-s-async-feature-to-communicate-with-a-custom-btp-app/ba-p/14231021)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  Tuesday
* [Issue and Send Verifiable Credentials](/t5/technology-blog-posts-by-sap/issue-and-send-verifiable-credentials/ba-p/14226105)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  a week ago
* [A Comprehensive Guide to Data Migration with the SAP S/4HANA Migration Cockpit](/t5/technology-blog-posts-by-members/a-comprehensive-guide-to-data-migration-with-the-sap-s-4hana-migration/ba-p/14224541)
  in [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)  2 weeks ago
* [Using Technical User in SAP Datasphere Consumption APIs (Client Credentials)](/t5/technology-blog-posts-by-sap/using-technical-user-in-sap-datasphere-consumption-apis-client-credentials/ba-p/14218919)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  2 weeks ago
* [Blog Post : Integrate SAP Document AI with SAP Build Process Automation on a Trial Account](/t5/technology-q-a/blog-post-integrate-sap-document-ai-with-sap-build-process-automation-on-a/qaq-p/14219067)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  2 weeks ago

Top kudoed authors

| User | Count |
| --- | --- |
| [![WouterLemaire](https://avatars.profile.sap.com/9/5/id95a688fa6b84e4186cabf39d7a83127ea90dd51dd190d355416d56f7d3a5be56_small.jpeg "WouterLemaire")  ![SAP Mentor](/html/@F4C200E47DAE3459A6BD3FBB7F9955B8/rank_icons/mentor-rank-16x16.svg "SAP Mentor") WouterLemaire](/t5/user/viewprofilepage/user-id/9863) | 6 |
| [![rajarajeswari_kaliyaperum](https://avatars.profile.sap.com/c/1/idc10d67889f40de37cfb340af4a802e39952419bdc3ee1ba9dd6000bf645e35b6_small.jpeg "rajarajeswari_kaliyaperum")  rajarajeswari\_kaliyaperum](/t5/user/viewprofilepage/user-id/654809) | 4 |
| [![kartheekkkota](https://avatars.profile.sap.com/2/d/id2d7e639322351b2b6b5a2b0a8d59075fd847a612a238bd7704e00c54f4a4e975_small.jpeg "kartheekkkota")  kartheekkkota](/t5/user/viewprofilepage/user-id/22...