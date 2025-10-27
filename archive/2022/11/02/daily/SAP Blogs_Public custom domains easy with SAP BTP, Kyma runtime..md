---
title: Public custom domains easy with SAP BTP, Kyma runtime.
url: https://blogs.sap.com/2022/11/01/public-custom-domains-easy-with-sap-btp-kyma-runtime./
source: SAP Blogs
date: 2022-11-02
fetch_date: 2025-10-03T21:31:41.453402
---

# Public custom domains easy with SAP BTP, Kyma runtime.

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Public custom domains easy with SAP BTP, Kyma runt...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/153209&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Public custom domains easy with SAP BTP, Kyma runtime.](/t5/technology-blog-posts-by-sap/public-custom-domains-easy-with-sap-btp-kyma-runtime/ba-p/13536720)

![quovadis](https://avatars.profile.sap.com/5/f/id5f0d9937a29017f07c2dd14f033b8d49b11261952ae7ce68ec448c7d5c66f338_small.jpeg "quovadis")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[quovadis](https://community.sap.com/t5/user/viewprofilepage/user-id/743)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=153209)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/153209)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13536720)

‎2022 Nov 01
8:09 PM

[11
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/153209/tab/all-users "Click here to see who gave kudos to this post.")

5,545

* SAP Managed Tags
* [SAP BTP, Kyma runtime](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%252C%2520Kyma%2520runtime/pd-p/73554900100800003012)

* [SAP BTP, Kyma runtime

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%25252C%2BKyma%2Bruntime/pd-p/73554900100800003012)

View products (1)

|
 [![](/legacyfs/online/storage/blog_attachments/2021/06/SAP_Business_Technology_Platform_R.png)](https://www.sap.com/products/business-technology-platform.html) |

|
 ![](/legacyfs/online/storage/blog_attachments/2022/10/gateway-2.png)   Using istio gateways, gardener dns and kyma dashboard components |
 This brief is to demonstrate how SAP BTP, Kyma runtime makes it *easy* to set up an **istio** [**gateway**](https://istio.io/latest/docs/reference/config/networking/gateway/) with a **wildcard public custom domain.**      ---      Pre-requisistes:    * access to a **registrar** with a registered public domain you own  * access to one of SAP BTP, Kyma runtime-supported **[DNS providers.](https://github.com/gardener/external-dns-management#external-dns-management)**  * cluster-admin access to SAP BTP, Kyma Runtime (**SKR**) kubernetes cluster |

# Putting it all together

For the sake of this brief  I have picked two different public domains registrars, namely Google Domains and Gandi.net and two different external DNS providers, namely: Google Cloud DNS and Azure DNS.

When you [provision](https://help.sap.com/docs/BTP/65de2977205c403bbc107264b8eccf4b/09dd313bf6644250a14f8f38c3d644c0.html) a kyma cluster it gets assigned a secure wildcard public domain name, for instance: `.kyma.ondemand.com`, which is entirely managed by SAP.

The built-in `kyma-system/kyma-gateway` is configured with this default domain.

Likewise, your kyma cluster's API server, namely: `<https://api.<shoot-name>.kyma.ondemand.com>`, is bound to that domain as well. Thus, a cluster domain **cannot** be changed once a cluster has been provisioned.

Q. But what if you wanted to have your own domain with a kyma cluster gateway?  In other words, [how to set up a domain for workloads across a kyma cluster](https://kyma-project.io/docs/kyma/latest/03-tutorials/00-api-exposure/apix-02-setup-custom-domain-for-workload)?

A. Here you go. You will need to accomplish these three tasks, namely:

|
 [Task **A**](#taskA). Bring your own domain (**BYOD**)    * Custom domains are important when it comes to security, identity protection and commercial branding.  * Most likely your business already owns registered domains dedicated to cloud applications.         ---      [Task **B**](#taskB). Set up the domain with an external DNS provider ([Google CloudDNS](https://github.com/gardener/external-dns-management/blob/master/docs/google-cloud-dns/README.md) and [Azure DNS](https://github.com/gardener/external-dns-management/blob/master/docs/azure-dns/README.md))    * That includes bringing the DNS servers names to your registrar and granting API access to a DNS zone resources to enable DNS provisioning automation on kyma side.         ---      [Task **C**](#taskC). Configure SAP BTP, Kyma runtime (SKR) cluster DNS resources [automation](https://kyma-project.io/docs/kyma/latest/03-tutorials/00-api-exposure/apix-02-setup-custom-domain-for-workload).    * SAP BTP,Kyma runtime (SKR) inherits the [DNS](https://www.cloudflare.com/en-ca/learning/dns/what-is-dns/) resources automation from [Gardener](https://github.com/gardener/external-dns-management#external-dns-management), albeit this is transparent for SKR users.  * The centrally hosted [kyma dashboard](https://dashboard.kyma.cloud.sap/) has a built-in secrets editor that implements a number of presets including the secret presets for all supported external DNS providers. |

I shall endeavour to walk you step by step throughout each of these three tasks. However, if you are network-fluent and have complied with the Task A and Task B requirements, you may jump directly to [Task C](#taskC).

## Task A. Bring Your Own Domain (BYOD).

|
 The BYOD refresher:    * SAP BTP, Kyma Runtime (SKR), with its built-in automation support of major public DNS providers, makes it easy to **BYOD** a domain to a kyma cluster.  * A BYOD domain must have been registered with a domain registrar. You must have access to your domain's DNS settings in the registrar's admin console.  * BYOD domains will be made *accessible* to kyma cluster resources via one of the supported DNS providers. However, you still retain full **ownership**. **liability** and **responsibility** of any of these domains. |

### 1a. Custom domains with Google Domains

Google Domains is a domain registrar. For instance, you may look up your registered domain names at: `<https://domains.google.com/registrar/>`

However, Google Domains is **not** a DNS (domain name service) [provider](https://stackexchange.github.io/dnscontrol/provider-list) per se. Thus you will need to bring in the DNS servers names from your established external DNS provider.

|
 **Steps** |
 **Google Domains registered domain's custom DNS settings** |

|
 Goto DNS settings and switch to Custom name servers.    Please make sure the domain, you are about to modify the DNS settings of, is not used for your websites or email.    However, If that were the case, you might want to register a different domain dedicated to your kyma workloads |
 ![](/legacyfs/online/storage/blog_attachments/2022/10/Registrar0.png) |

|
 The custom name servers will come from either the Google Cloud DNS or Azure DNS provider.    As Google Domains does not support APIs you will have apply them manually. |
 ![](/legacyfs/online/storage/blog_attachments/2022/10/Registrar1.png) |

|
 After saving the new DNS settings these will be effective after a short while. |
 ![](/legacyfs/online/storage/blog_attachments/2022/10/Registrar2.png) |

### 1b. Custom domains with Gandi.net

[Gandi.net](https://www.gandi.net/en-US) is a popular domain registrar and a DNS provider. H...