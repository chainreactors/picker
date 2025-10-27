---
title: Enhancement Implementation in Payment Formats in Contract Accounts Receivable and Payable (FI-CA)
url: https://blogs.sap.com/2022/10/24/enhancement-implementation-in-payment-formats-in-contract-accounts-receivable-and-payable-fi-ca/
source: SAP Blogs
date: 2022-10-25
fetch_date: 2025-10-03T20:46:49.146399
---

# Enhancement Implementation in Payment Formats in Contract Accounts Receivable and Payable (FI-CA)

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* Enhancement Implementation in Payment Formats in C...

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/49621&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Enhancement Implementation in Payment Formats in Contract Accounts Receivable and Payable (FI-CA)](/t5/enterprise-resource-planning-blog-posts-by-sap/enhancement-implementation-in-payment-formats-in-contract-accounts/ba-p/13544638)

![TrangNguyen](https://avatars.profile.sap.com/2/7/id276fe89ae9637441820b980444464805c5da3dc3b5c1eacee428c6a7ad598a3b_small.jpeg "TrangNguyen")

![Advisor](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Advisor")
[TrangNguyen](https://community.sap.com/t5/user/viewprofilepage/user-id/14194)

Advisor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=49621)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/49621)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13544638)

‎2022 Oct 24
6:11 PM

[5
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/49621/tab/all-users "Click here to see who gave kudos to this post.")

4,417

* SAP Managed Tags
* [SAP S/4HANA](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA/pd-p/73554900100800000266)

* [SAP S/4HANA

  SAP S/4HANA](/t5/c-khhcw49343/SAP%2BS%25252F4HANA/pd-p/73554900100800000266)

View products (1)

In SAP, we are delivering solutions for processing credit transfer and direct debit requests to simplify your communication with banks using SAP S/4HANA via Payment Formats. With Payment Formats, you can flexibly adjust the content of payment media file as needed. You can find out further details related to Payment Formats in SAP [here](https://blogs.sap.com/2020/04/28/payment-formats-in-sap/), focusing on **Outgoing Formats** sections. About Payment Formats in FI-CA, refer to the blog post [Payment Formats in Contract Accounting in SAP S/4HANA](https://blogs.sap.com/2021/02/12/payment-formats-in-contract-accounting-in-sap-s-4hana/)  to learn more.

In this blog post, you can learn about the newly developed BAdIs and the functionalities regarding enhancement implementation in Payment Formats in FI-CA.

***Payment process in FI-CA***

![](/legacyfs/online/storage/blog_attachments/2022/10/1dia-1.png)

## Business Case

Previously, the enhancement spot can be implemented by following implicit enhancement which is predefined by SAP in the source code. By following the implicit enhancement, customers have to compose their own solutions in ABAP language with specific requirements. However, from now, you can use the new BAdIs developed by SAP to create your own enhancement implementation without using implicit enhancement. Within the newly delivered BAdIs, you are eligible to adjust the customer reference fields in order to define your own business logic. Meanwhile, you can also use your custom payment formats and implement it with standard procedure.

## About the BAdIs

The BAdIs supports extensibility in Payment Formats with the help for data collection before reaching the format structured in DMEEX. You can modify the source of data according to the legal requirements defined by specific countries/regions or remarks from customers.
In the enhancement spot ES\_FKK\_PAYM you can use the following two BAdIs for different purposes:

* BADI\_FKK\_ADJUST\_PAYM\_DATA\_C with method FILL\_CUSTOMER\_REFERENCE\_FIELD allows you to fill the specific customer-defined fields.
* BADI\_FKK\_ADJUST\_PAYM\_CUST with method SET\_ORIGINAL\_FORMAT allows you to reuse SAP delivered payment format implementation to fill “User-Defined Fields".

Within the BAdI, you can modify ZREF fields in FPAYHX structure and ZREF fields in paid item structure (FPAYP). For adjusting the payment item, the BAdI offers you 10 user Z REF fields range from 'ZREF01’ to ‘ZREF10’, each consisting of maximum 132 characters. Therefore, you can implement the enhancement for payment formats by filling those customer reference fields in the Z namespace.

## Implementation of BADI\_FKK\_ADJUST\_PAYM\_DATA\_C

By implementing this BAdI, you can fill the specific fields based on your business requirements.

1. In transaction **SE18**, enter **ES\_FKK\_PAYM** in **Enhancement Spot**, choose **Display.**
2. Creating a new enhancement by right-clicking BADI\_FKK\_ADJUST\_PAYM\_DATA\_C, choose**Create BAdI** **Implementation** then select **Create Enhancement Implementation**.
3. Fill in the name for your new enhancement in **Enhancement Implementation** field and a brief explanation in **Short Text** → **Enter** to create a new enhancement.![](/legacyfs/online/storage/blog_attachments/2022/10/2blog.png)
4. After that, you will see **Object Editing: Initial Screen** pops up to inform that enhancement object is saved in customer namespace. **Enter** to continue creation.
5. In the **Create Object Directory Entry** dialog box, save your entry locally in **Local Object →** Press Now your new enhancement is generated in the Enhancement spot.
6. Create BAdI implementation
   Double click on new enhancement generated. Complete all essential information:
   * **BAdI Implementation:** enter name for the BAdI
   * **Description**: briefly describe the BAdI
   * **Implementing Class**: define implementing class![](/legacyfs/online/storage/blog_attachments/2022/10/3-blog.png)
   * **Enter** to continue creation.
7. Modify the Enhancement Implementation
   In order to modify the enhancement implementation, you need to compose your own code and define your own logic.
   * To write your own code, double click on **Implementing Class** → Choose method **IF\_FKK\_PAYM\_DATA\_C****~****FILL\_CUSTOMER\_REFERENCE\_FIELD** → Write your own implementation.
     ![](/legacyfs/online/storage/blog_attachments/2022/10/4blog.png)
   * You can also refer to the sample code provided by SAP through Example classes. Example classes can be found under Enhancement spot **ES\_FKK\_PAYM →** BAdI Definition **BADI\_FKK\_ADJUST\_PAYM\_DATA\_C →** Implementation Example Classes **CL\_FKK\_PAYM\_IMP\_C\_EX**![](/legacyfs/online/storage/blog_attachments/2022/10/5blog.png)
8. Activate BAdI implementation.
9. Change Filter Values.

+ Go to **Filter Values**. Switch to Edit Mode → Choose **Combination** then add the value.

+ Change value filter

  1. **Value 1**: Enter the payment format name.
  2. **Comparator 1**: Specify condition as ''='' to apply payment format, which means that if the format matches the payment format name, the method will be executed.
  3. **Filter**: Format.
  4. **Enter**

![](/legacyfs/online/storage/blog_attachments/2022/10/6blog.png)Now you have your new BAdI implementation created. To generate a payment medium format file, link the standard DMEEX tree to the newly created payment format and assign it to a payment method. Further details about the process can be obtained in blog post [Payment Formats in Contract Accounting in SAP S/4HANA](https://blogs.sap.com/2021/02/12/payment-formats-in-contract-accounting-in-sap-s-4hana/)

## Imple...