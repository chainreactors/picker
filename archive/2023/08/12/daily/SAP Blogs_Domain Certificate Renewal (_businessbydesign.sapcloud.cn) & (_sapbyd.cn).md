---
title: Domain Certificate Renewal (*businessbydesign.sapcloud.cn) & (*sapbyd.cn)
url: https://blogs.sap.com/2023/08/11/domain-certificate-renewal-businessbydesign.sapcloud.cn-sapbyd.cn/
source: SAP Blogs
date: 2023-08-12
fetch_date: 2025-10-04T12:01:22.104809
---

# Domain Certificate Renewal (*businessbydesign.sapcloud.cn) & (*sapbyd.cn)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Domain Certificate Renewal (\*businessbydesign.sapc...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/54486&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Domain Certificate Renewal (\*businessbydesign.sapcloud.cn) & (\*sapbyd.cn)](/t5/enterprise-resource-planning-blog-posts-by-sap/domain-certificate-renewal-businessbydesign-sapcloud-cn-sapbyd-cn/ba-p/13577128)

![shilpa_prakaash1](https://avatars.profile.sap.com/2/e/id2ef83d7077e83e20d4b63ffaf0b9f4c0e77685b6fe04bc40ed8315521ee89184_small.jpeg "shilpa_prakaash1")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[shilpa\_prakaash1](https://community.sap.com/t5/user/viewprofilepage/user-id/743485)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=54486)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/54486)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13577128)

‎2023 Aug 11
7:51 PM

[2
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/54486/tab/all-users "Click here to see who gave kudos to this post.")

2,010

* SAP Managed Tags
* [SAP Business ByDesign](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520ByDesign/pd-p/01200615320800000691)

* [SAP Business ByDesign

  SAP Business ByDesign](/t5/c-khhcw49343/SAP%2BBusiness%2BByDesign/pd-p/01200615320800000691)

View products (1)

**Background**

The existing server certificate for domain \*businessbydesign.sapcloud.cn and \*sapbyd.cn will be renewed as it is going to expire on 10th Oct, 2023.

**Scope**

You will be affected if either of the below scenarios are applicable to you:

* Your browser does not have DigiCert Certificates.

* You have an inbound/outbound communication integration to your Byd product.

**Impact**

If you have third party integrations like web services/APIs in your Business ByDesign tenant, you may be required to update the domain certificate. These updates should be conducted by your internal IT resources, with the new certificate information that could be found below*.*

**Download new certificate**

Below are the steps to download new certificate:

* Kindly click on [download](https://eur03.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.digicert.com%2Fsecure%2Fdownload-certificate%2Fcvlz40gw93jlhbrzbxll59hxn5xgt4y%3Fproduct_name_id%3Dssl_securesite_flex%26product_type%3Dsecuresite_ssl_certificate%26platform%3D2&data=05%7C01%7Chridesh.kumar01%40sap.com%7C11edcabcd3394b36d07f08db9815bc0c%7C42f7676cf455423c82f6dc2d99791af7%7C0%7C0%7C638270991332215354%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&sdata=dP%2F7r%2Ffxc5S2uYbX%2BBPfJvhU6mIwzvyinuuaWwVvKjA%3D&reserved=0) link. You will be redirected to Digi Cert Website, here ensure Combined Certificate Files is set as shown below.

![](/legacyfs/online/storage/blog_attachments/2023/08/Image-1.1.png)

* Click download as shown below.

![](/legacyfs/online/storage/blog_attachments/2023/08/Image-1.2.png)

* A zip file by name: star\_businessbydesign\_sapcloud\_cn\_482414768 would be downloaded.

* Please unzip this file and we can see required certificate: **star\_businessbydesign\_sapcloud\_cn.crt.**

![](/legacyfs/online/storage/blog_attachments/2023/08/Image-1.3.png)

**FAQs**

**1) What are these certificates used for?**
These certificates are used for the SSL/TLS handshake that any system using the ‘secure’ protocol does before allowing connection to/from the system. In our case, SAP Business ByDesign uses the ‘secure’ HTTPS protocol and hence the SSL handshake is must for any system to connect to these URLs.

**2) Are the new certificates known to modern web browsers?**
DigiCert Root Certificates are automatically recognized by all common web browsers, mobile devices, and mail clients, therefore for browser scenarios there is nothing to do. The same is true if one relies on the standard sapjvm trust list.
The CA root certificate is included in:

* SAP JVM patch level 8.1.035 or 7.1.054

* Cloud Foundry buildpack SAP-Java (sap\_java\_buildpack) version 1.6.15

**3) How do I download or install the certificate?**
You must have admin access to the server where you need to install the certificate. If you do not have access to your company’s SSL server, notify your IT team and provide them the respective certificate download link from the above table.

**4) How do Import Single Certificate in SAP CPI Key Store?**
Follow the steps mentioned in the [link](https://help.sap.com/viewer/368c481cd6954bdfa5d0435479fd4eaf/Cloud/en-US/03cf78a217574e7abd75bfbba990c085.html?q=import%20certificate).

**5) How to check the certificate in my browser trust list?**
Navigate to chrome://settings and scroll down to ‘Advanced’.

* Under “Privacy and Security,” click “Manage Certificates.”

* On the popup that was launched, select “Trusted Root Certification Authorities’. The certificate will be displayed there.

**6) How to import the certificate into my browser?**
**Procedure**

* Open the browser.

* Click Customize and control Google Chrome button in the upper right corner.

* Choose Settings. …

* Under Privacy and security section, click More. …

* Click Manage certificates, The new window will appear. …

* Choose Trusted Root Certification Authorities tab.

* Click Import. …

* In the opened window, click Next.

**7) I notice a discrepancy in the validity start date and end date mentioned in this knowledge article table and my downloaded certificate. What does this indicate?**
Sometimes, due to time zone difference, you may see a different date in the downloaded certificate. There is no impact on the certificate update activity due to this. You will be renewing the certificate well in advance, before the certificate expiry date.

Please do share feedback and your thoughts in the comment section below.
You can also refer SAP Business ByDesign environment.
Topic page: (<https://community.sap.com/topics/business-bydesign>)
Post and answer questions (<https://answers.sap.com/tags/01200615320800000691>)
Read other posts on the topic (<https://blogs.sap.com/tags/01200615320800000691/>)

Labels

* [Product Updates](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap/label-name/product%20updates)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-sap%2Fdomain-certificate-renewal-businessbydesign-sapcloud-cn-sapbyd-cn%2Fba-p%2F13577128%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [T-code S\_P00\_07000134 report displays withholding tax certificate nos twice](/t5/enterprise-resourc...