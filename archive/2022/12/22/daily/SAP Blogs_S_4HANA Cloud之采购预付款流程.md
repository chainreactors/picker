---
title: S/4HANA Cloud之采购预付款流程
url: https://blogs.sap.com/2022/12/21/s-4hana-cloud%e4%b9%8b%e9%87%87%e8%b4%ad%e9%a2%84%e4%bb%98%e6%ac%be%e6%b5%81%e7%a8%8b/
source: SAP Blogs
date: 2022-12-22
fetch_date: 2025-10-04T02:13:07.946645
---

# S/4HANA Cloud之采购预付款流程

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by SAP](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap)
* S/4HANA Cloud之采购预付款流程

Enterprise Resource Planning Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-sap/article-id/51260&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [S/4HANA Cloud之采购预付款流程](/t5/enterprise-resource-planning-blog-posts-by-sap/s-4hana-cloud%E4%B9%8B%E9%87%87%E8%B4%AD%E9%A2%84%E4%BB%98%E6%AC%BE%E6%B5%81%E7%A8%8B/ba-p/13556471)

![ecco_liu](https://avatars.profile.sap.com/9/a/id9a5e3aaf023973dbd36b33cdf3a3e9c8abef884bef43ad08075aa9427b58b8ab_small.jpeg "ecco_liu")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[ecco\_liu](https://community.sap.com/t5/user/viewprofilepage/user-id/492951)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-sap&message.id=51260)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-sap/article-id/51260)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13556471)

‎2022 Dec 21
4:40 PM

[4
Kudos](/t5/kudos/messagepage/board-id/erp-blog-sap/message-id/51260/tab/all-users "Click here to see who gave kudos to this post.")

3,853

* SAP Managed Tags
* [SAP S/4HANA Cloud Public Edition Sourcing and Procurement](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition%2520Sourcing%2520and%2520Procurement/pd-p/a906d110-8210-4641-9e54-4744b42f06d0)
* [SAP S/4HANA Cloud Public Edition](https://community.sap.com/t5/c-khhcw49343/SAP%2520S%252F4HANA%2520Cloud%2520Public%2520Edition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)

* [SAP S/4HANA Cloud Public Edition

  SAP S/4HANA Cloud](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition/pd-p/08e2a51b-1ce5-4367-8b33-4ae7e8b702e0)
* [SAP S/4HANA Cloud Public Edition Sourcing and Procurement

  Additional Software Product](/t5/c-khhcw49343/SAP%2BS%25252F4HANA%2BCloud%2BPublic%2BEdition%2BSourcing%2Band%2BProcurement/pd-p/a906d110-8210-4641-9e54-4744b42f06d0)

View products (2)

很多客户有采购预付款的业务需求，比如在供应商正式发货之前需提前支付一定比例的首付款给到供应商。下面我们来看看S/4HANA Cloud中的采购预付款操作流程，希望对您有所帮助。

第一步是使用具有Purchaser采购员权限的账户打开应用“创建采购订单 - 高级”去创建采购订单。填写所有必要的字段，转到“发票”选项卡，然后选择“预付定金类别”“强制性预付款”。输入预付款金额或预付款百分比以及预付款日期并保存采购订单。

![](/legacyfs/online/storage/blog_attachments/2022/12/创建采购订单.jpg)

下一步是通过打开具有角色Accounts Payable Accountant应付账款会计的应用“监控采购订单预付款”来创建预付款请求。输入过滤器值以查找您刚创建的采购订单项目。选择您的采购订单，然后单击“创建预付款申请”按钮。

![](/legacyfs/online/storage/blog_attachments/2022/12/创建预付款申请.jpg)

您将被自动定向到应用“管理供应商预付款申请”。填写必填字段，然后单击“过账”按钮。将显示“成功”屏幕，显示您的日记帐分录编号。

![](/legacyfs/online/storage/blog_attachments/2022/12/管理供应商预付款申请-1.jpg)

![](/legacyfs/online/storage/blog_attachments/2022/12/预付款过账成功.jpg)

下一步是创建预付款。打开具有角色Accounts Payable Accountant应付账款会计的应用“过帐付款”。在标题中填写付款详细信息，按“显示项目”按钮，然后在“打开项目”部分搜索您刚过账的日记帐条目。如果您找不到您的日记账分录，请尝试“选择更多”按钮并调整过滤器设置。

![](/legacyfs/online/storage/blog_attachments/2022/12/过账付款.jpg)

找到日记条目后，按“清算”按钮，然后按“过账”按钮。您将获得一个成功的弹出窗口，其中包含您成功发布的日记帐条目编号。

![](/legacyfs/online/storage/blog_attachments/2022/12/过账付款成功.jpg)

在该步骤之后，您可以过帐收货或直接创建发票，取决于您的采购订单是否勾选了基于收货的发票校验，如果基于收货的发票校验，则需要先收货后进行发票检验；反之，则可以直接基于采购订单进行发票校验而不需要先行收货。

打开应用“创建供应商发票 - 高级”并填写必要的发票数据。引用采购订单后，您应该会看到一个提示预付款的弹出窗口，然后单击“继续”。

![](/legacyfs/online/storage/blog_attachments/2022/12/创建供应商发票.jpg)

点击标题工具栏中的“清算预付款”按钮。将打开“预付定金清算”的弹出窗口，您需要向右滚动以填写输入的金额。输入金额后，选择该行并按“复制”按钮。

![](/legacyfs/online/storage/blog_attachments/2022/12/预付定金清算.jpg)

在填写发票校验所需的数据之后，您可以模拟或过帐发票。发票过账成功之后可以查看生成的会计凭证及分录。

![](/legacyfs/online/storage/blog_attachments/2022/12/供应商发票成功创建.jpg)

S/4HANA Cloud中的采购预付款流程介绍如上，若有相关业务需求，可以在您的系统中进行测试并使用。

感谢您的阅读，请关注我的个人资料以获取未来的博文，也欢迎您在评论区中分享您的反馈或者想法。

Labels

* [Product Updates](/t5/enterprise-resource-planning-blog-posts-by-sap/bg-p/erp-blog-sap/label-name/product%20updates)

* [PSCC\_CCC\_CN](/t5/tag/PSCC_CCC_CN/tg-p/board-id/erp-blog-sap)

5 Comments

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Fenterprise-resource-planning-blog-posts-by-sap%2Fs-4hana-cloud%25E4%25B9%258B%25E9%2587%2587%25E8%25B4%25AD%25E9%25A2%2584%25E4%25BB%2598%25E6%25AC%25BE%25E6%25B5%2581%25E7%25A8%258B%2Fba-p%2F13556471%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Enabling 'Compliance' tab in Purchase order header & Line item in SAP Public cloud](/t5/enterprise-resource-planning-q-a/enabling-compliance-tab-in-purchase-order-header-amp-line-item-in-sap/qaq-p/14234218)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  8 hours ago
* [Value Help in S/4HANA Cloud Public Edition always resets and shows all entries](/t5/enterprise-resource-planning-q-a/value-help-in-s-4hana-cloud-public-edition-always-resets-and-shows-all/qaq-p/14234192)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  8 hours ago
* [How to Be Linking Commercial Invoices Upload to Sales Orders](/t5/enterprise-resource-planning-q-a/how-to-be-linking-commercial-invoices-upload-to-sales-orders/qaq-p/14234159)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  8 hours ago
* [How to trigger HU label print in S/4HANA Cloud Public Edition (API\_FORM\_PRINT\_SRV not available)](/t5/enterprise-resource-planning-q-a/how-to-trigger-hu-label-print-in-s-4hana-cloud-public-edition-api-form/qaq-p/14233989)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  11 hours ago
* [Max line items in service contract in public cloud 2508](/t5/enterprise-resource-planning-q-a/max-line-items-in-service-contract-in-public-cloud-2508/qaq-p/14233931)
  in [Enterprise Resource Planning Q&A](/t5/enterprise-resource-planning-q-a/qa-p/erp-questions)  13 hours ago

Top kudoed authors

| User | Count |
| --- | --- |
| [![thikimanh_hoang](https://avatars.profile.sap.com/6/d/id6d6977dc4ad863422001746d9d6e8c0f5dbd4e0a2c0cc3deb80bd3726f049353_small.jpeg "thikimanh_hoang")  ![Associate](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Associate") thikimanh\_hoang](/t5/user/viewprofilepage/user-id/2233182) | 8 |
| [![Andrew_Ford](https://avatars.profile.sap.com/4/2/id42fc9a5c18fc3229159993bbd8c3abd793e64af5050b65e9a4b850c04ce6bbb7_small.jpeg "Andrew_Ford")  ![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert") Andrew\_Ford](/t5/user/viewprofilepage/user-id/98013) | 8 |
| [![DianaMala](https://avatars.profile.sap.com/6/d/id6db8ca00c3368971fe9ea45165f8ca02b42d3fc0d2b18891c590b300d9206a82_small.jpeg "DianaMala")  ![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert") DianaMala](/t5/user/viewprofilepage/user-id/1565064) | 8 |
| [![FabianAckermann](https://avatars.profile.sap.com/9/f...