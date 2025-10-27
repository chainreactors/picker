---
title: Securely publish an application in SAP BTP under your own domain
url: https://blogs.sap.com/2023/01/05/securely-publish-an-application-in-sap-btp-under-your-own-domain/
source: SAP Blogs
date: 2023-01-06
fetch_date: 2025-10-04T03:09:15.644522
---

# Securely publish an application in SAP BTP under your own domain

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Securely publish an application in SAP BTP under y...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/162519&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Securely publish an application in SAP BTP under your own domain](/t5/technology-blog-posts-by-members/securely-publish-an-application-in-sap-btp-under-your-own-domain/ba-p/13564122)

![Sudhir_Lenka](https://avatars.profile.sap.com/5/b/id5b1278b90f00ae44c254fdf47d34d0910fa96d91b60b2ec3cf677e6dadfd2e20_small.jpeg "Sudhir_Lenka")

[Sudhir\_Lenka](https://community.sap.com/t5/user/viewprofilepage/user-id/208695)

Contributor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=162519)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/162519)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13564122)

‎2023 Jan 05
11:41 PM

[5
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/162519/tab/all-users "Click here to see who gave kudos to this post.")

2,075

* SAP Managed Tags
* [SAP BTP Security](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%2520Security/pd-p/842ea649-eeef-464c-b80c-a64b03e40158)
* [SAP Cloud Application Programming Model](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520Application%2520Programming%2520Model/pd-p/9f13aee1-834c-4105-8e43-ee442775e5ce)
* [SAP BTP, Cloud Foundry runtime and environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%252C%2520Cloud%2520Foundry%2520runtime%2520and%2520environment/pd-p/73555000100800000287)

* [SAP BTP, Cloud Foundry runtime and environment

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%25252C%2BCloud%2BFoundry%2Bruntime%2Band%2Benvironment/pd-p/73555000100800000287)
* [SAP Cloud Application Programming Model

  Software Product Function](/t5/c-khhcw49343/SAP%2BCloud%2BApplication%2BProgramming%2BModel/pd-p/9f13aee1-834c-4105-8e43-ee442775e5ce)
* [SAP BTP Security

  Software Product Function](/t5/c-khhcw49343/SAP%2BBTP%2BSecurity/pd-p/842ea649-eeef-464c-b80c-a64b03e40158)

View products (3)

We have developed and deployed an application in **SAP BTP (Cloud Foundry)** for one of our clients, this application is developed in **Java Spring Boot, SAP UI5 and SAP HANA**. The requirement was to expose the application under customer domain and not with the SAP BTP provided default domain, so we used SAP’s Custom Domain server, it is one of the services provided by SAP in BTP landscape. Here I am gonging to highlight our learning and experience on SAP’s Custom Domain service.

**What is custom domain**

When you host/deploy an application in BTP it would be accessible with the default sub domain provided by the cloud vendor. But as an application owner we never want our application to be accessible via default sub domain provided by cloud vendor, we would want our application to be accessible under our own domain. Custom domain helps to exposure our cloud application under our own domain.

**What is custom domain service in BTP**

SAP provides many services in BTP, Custom Domain service is one of the services which helps customers to configure and publicly exposure their application under their own domain. By using this service, subaccount owners can make their SAP BTP applications accessible via a custom domain that is different from the default one (hana.ondemand.com) - for example, [www.myapp.com](http://www.myapp.com).

**Features**

* Access to your domain: Configure your application with a name that is easily recognizable by your customers and users.

* Application identity protection: Upload a TLS/SSL certificate to help secure your application identity and the data transmitted between the browser and your application

**Environment**

Custom Domain service runs in both Cloud Foundry and Neo environments.

**Use Cases**

Any PaaS or SaaS customer in SAP BTP would require this service to expose their **application**/ **subscribed service** securely under their own domain.

**Process to create a custom domain for your application**

1. Subscribe to the Custom Domain Manager by using the SAP BTP cockpit in the **Instances and Subscriptions** section in your subaccount.

2. Create a new instance and configure it by logging into Custom Domain Manager.

**Tools required for SAP Cloud Foundry**

You need the Cloud Foundry CLI and the Custom Domain CLI plugin to use the Custom Domain service.

**Secure your application**

To make sure that your domain is trusted, and all your application data is protected, you have to get an appropriate TLS/SSL certificate from a Certificate Authority (CA). Determine the domains you want to be protected by this certificate. One certificate can be valid for a number of domains and subdomains, but you can also use a dedicated certificate for each domain

* Standard certificate - A standard certificate protects one domain, for example. <www.myapp.com>.

* Wildcard certificate - A wildcard certificate secures multiple applications of a domain, for example, \*.myapp.com covers any application under the domain myapp.com, like a.myapp.com, but not the domain myapp.com itself.

In our case we have used CA signed wildcard certificate for an application deployed in SAP Cloud Foundry, I am going to touch upon the steps.

We have used Cloud Foundry command line interface (CLI) to mange the SSL certificate for our custom domain.

1. Generate the Certificate Signing Request (CSR) for your domain by using CLI. While creating CSR, we would need to provide few important information and generate a private key.

```
cf custom-domain-create-key my-domain-key "CN=*.myapp.com, O=Organization, OU =Address, L=Address-2, ST=Address-3, C=Address-3" "myapp.com" "*.myapp.com"
```

2. Download the CSR (.pem) from CLI and share with authority for signing.

```
cf custom-domain-get-csr my-domain-key csr.pem
```

3. Once signed certificate is received from CA then we would need upload and activate it to BTP through CLI.

4. Upload the new certificate.

```
cf custom-domain-upload-certificate-chain my-domain-key NewCertificate.pem
```

5. Activate uploaded certificate.

```
cf custom-domain-activate my-domain-key "*.myapp.com" "myapp.com"
```

We would need to renew the certificate before it gets expired, while renewing please make sure you use a new private key while generating the CSR file and delete the old private key when new certificate is uploaded and activated.

**Graphical overview**

![](/legacyfs/online/storage/blog_attachments/2023/01/Process.png)

* [customdomain](/t5/tag/customdomain/tg-p/board-id/technology-blog-members)
* [ssl](/t5/tag/ssl/tg-p/board-id/technology-blog-members)

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fsecurely-publish-an-application-in-sap-btp-under-your-own-domain%2...