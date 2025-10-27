---
title: SAP private linky swear with Azure – extending BTP apps with microservices in Azure Kubernetes Service via SAP Private Link
url: https://blogs.sap.com/2022/10/19/sap-private-linky-swear-with-azure-extending-btp-apps-with-microservices-in-azure-kubernetes-service-via-sap-private-link/
source: SAP Blogs
date: 2022-10-20
fetch_date: 2025-10-03T20:23:10.332983
---

# SAP private linky swear with Azure – extending BTP apps with microservices in Azure Kubernetes Service via SAP Private Link

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* SAP private linky swear with Azure – extending BTP...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160006&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP private linky swear with Azure – extending BTP apps with microservices in Azure Kubernetes Service via SAP Private Link](/t5/technology-blog-posts-by-members/sap-private-linky-swear-with-azure-extending-btp-apps-with-microservices-in/ba-p/13549700)

![Martin-Pankraz](https://avatars.profile.sap.com/a/f/idaf076ff2e13cfa1a447d49445c14aade203307d10ab9eaf447b4954caf06d689_small.jpeg "Martin-Pankraz")

![SAP Champion](/html/@B3DACAC6163F980483AC32558EB69695/rank_icons/champion-rank-16x16.svg "SAP Champion")
[Martin-Pankraz](https://community.sap.com/t5/user/viewprofilepage/user-id/143781)

SAP Champion

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160006)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160006)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13549700)

‎2022 Oct 19
1:37 PM

[4
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160006/tab/all-users "Click here to see who gave kudos to this post.")

1,690

* SAP Managed Tags
* [SAP Integration Suite](https://community.sap.com/t5/c-khhcw49343/SAP%2520Integration%2520Suite/pd-p/73554900100800003241)
* [SAP Commerce Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520Commerce%2520Cloud/pd-p/73555000100800001224)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [SAP Commerce Cloud

  Software Product](/t5/c-khhcw49343/SAP%2BCommerce%2BCloud/pd-p/73555000100800001224)
* [SAP Integration Suite

  SAP Integration Suite](/t5/c-khhcw49343/SAP%2BIntegration%2BSuite/pd-p/73554900100800003241)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)

View products (3)

|
 This post is part 9 of a series sharing service implementation experience and possible applications of SAP Private Link Service on Azure.    Find the table of contents and my curated news regarding series updates [here](https://blogs.sap.com/2021/12/29/getting-started-with-btp-private-link-service-for-azure/).    Find the associated GitHub repos [here](https://github.com/MartinPankraz/az-private-linky-aks). |

Dear community,

Continuing with the implementation journey of [SAP Private Link Service](https://help.sap.com/docs/PRIVATE_LINK) (PLS) for Azure we will have a closer look at connecting to your micro-services hosted on [Azure Kubernetes Service](https://learn.microsoft.com/azure/aks/intro-kubernetes) (AKS). Why is this interesting? For example, a Scandinavian customer I recently spoke with, connects their SAP Commerce Cloud privately with their non-btp business extensions using this new BTP service.

![](/legacyfs/online/storage/blog_attachments/2022/10/private-linky-aks-overview.png)

Fig. 1 Architecture overview of example use case with SAP Commerce Cloud extensions hosted on Azure Kubernetes Service

This post focuses on the AKS setup and builds upon [part 1](https://blogs.sap.com/2021/12/01/btp-private-linky-swear-with-azure-how-to-setup-ssl-end-to-end-with-private-link-service/) and [part 2](https://blogs.sap.com/2021/07/13/btp-private-linky-swear-with-azure-business-as-usual-for-iflows/) of the series. Part 1 covers the standard Azure load balancer setup and scope, whereas part 2 sheds light on the connectivity from SAP Integration Suite. Integrators put things together, you know ![:cowboy_hat_face:](/html/@1AC3F2CA7F591A3F01D637C79C341848/emoticons/1f920.png ":cowboy_hat_face:").

#Kudos to [Dennis Menge](https://www.linkedin.com/in/dennis-menge/) who got me up to speed with K8s and Azure Private Link in one Friday afternoon. A skilled, humble, and fun to work with human being. Best combination in an engineer.

#Kudos to Matthias Winzeler and gowrisankar.m2 for the meaningful collaboration. Co-development at its best.

Be aware that the private link setup is done through YAML files instead of the Azure portal UI.

![](/legacyfs/online/storage/blog_attachments/2022/10/private-linky-aks-pinkie.png)

Fig. 2 Illustration of pinkies connecting your AKS-hosted microservice via SAP BTP

# You didn’t know AKS with PLS worked from day one? Here you go…

Azure Kubernetes Service was not listed on the series yet, because it is a standard scenario for the Azure Private Link Service. But since some of the configurations are beefier than a couple of clicks on the portal, it seemed worth spending a post on it.

Wait, not available through the portal??? ![:face_screaming_in_fear:](/html/@EE789A8A23FAA852E0533EA850C280A8/emoticons/1f631.png ":face_screaming_in_fear:")

Yes, we must do what Kubernetes demands! And that is command line usage! 🧙‍![:male_sign:](/html/@E5F727AEF7FF6D941E9FAB20ED79AC19/emoticons/2642.png ":male_sign:")No, really. Since Azure Kubernetes Service will govern your Azure Private Link and configurations, you need to use the famous “**kubectl**”. But don’t worry you will still be able to verify the PLS creation from the Portal. There is a shy![:see_no_evil_monkey:](/html/@D80ABD061424732D3FF9CC3691AE21A9/emoticons/1f648.png ":see_no_evil_monkey:") resource group with prefix ”MC\_” that gets created. More on that further down.

To hit the code ![:oncoming_fist:](/html/@8CE3835801632B29D0D48413A8941701/emoticons/1f44a_1f3fd.png ":oncoming_fist:") without any further reading, jump to the [GitHub repos](https://github.com/MartinPankraz/az-private-linky-aks).

In case you are following along:

1. Start by spinning up an [Azure Kubernetes Service instance](https://learn.microsoft.com/azure/aks/learn/quick-kubernetes-deploy-portal?tabs=azure-cli#create-an-aks-cluster).

|
 **🛈 Note**    The **two** resource groups that were created. One that you individually named that contains your AKS service instance. And second generated one prefixed with “MC\_” that contains the virtual network and VM scale set etc. This second one will also contain your Private Link and load balancer once we progress with the setup. |

2. Clone the [GitHub repos](https://github.com/MartinPankraz/az-private-linky-aks.git) into your environment.

3. Deploy the deployment.yml from the app folder using kubectl command

```
kubectl apply -f deployment.yaml
```

It uses a standard NGINX image from the [Microsoft Container Registry](https://mcr.microsoft.com/), [mounts the working directory](https://github.com/MartinPankraz/az-private-linky-aks/blob/main/app/deployment.yaml#L21) and echoes a simple JSON on each request on port 80.

|
 **🛈 Note**    You may [install kubectl](https://learn.microsoft.com/en-us/azure/aks/tutorial-kubernetes-deploy-cluster?tabs=azure-cli#install-the-kubernetes-cli) locally or use the Azure CLI from the portal, which has kubectl pre-installed. |

Hurray 🥳, we have a running micro-service that cannot be called by anyone. Continue with the servic...