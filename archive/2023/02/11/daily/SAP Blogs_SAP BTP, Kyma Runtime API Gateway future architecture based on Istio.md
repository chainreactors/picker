---
title: SAP BTP, Kyma Runtime API Gateway future architecture based on Istio
url: https://blogs.sap.com/2023/02/10/sap-btp-kyma-runtime-api-gateway-future-architecture-based-on-istio/
source: SAP Blogs
date: 2023-02-11
fetch_date: 2025-10-04T06:19:26.240893
---

# SAP BTP, Kyma Runtime API Gateway future architecture based on Istio

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* SAP BTP, Kyma Runtime API Gateway future architect...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/163519&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP BTP, Kyma Runtime API Gateway future architecture based on Istio](/t5/technology-blog-posts-by-sap/sap-btp-kyma-runtime-api-gateway-future-architecture-based-on-istio/ba-p/13567213)

![strekm](https://avatars.profile.sap.com/0/c/id0ce40f5c90aa7473a478866fe6b7f9288a0ab5cb8a2ed12181128419d72d3031_small.jpeg "strekm")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[strekm](https://community.sap.com/t5/user/viewprofilepage/user-id/45483)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=163519)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/163519)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13567213)

‎2023 Feb 10
8:31 PM

[9
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/163519/tab/all-users "Click here to see who gave kudos to this post.")

4,695

* SAP Managed Tags
* [SAP BTP, Kyma runtime](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%252C%2520Kyma%2520runtime/pd-p/73554900100800003012)

* [SAP BTP, Kyma runtime

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%25252C%2BKyma%2Bruntime/pd-p/73554900100800003012)

View products (1)

I'm part of the Kyma team responsible for API Exposure topics. My team and I work on providing a convenient, reliable, and secure way to expose workloads. In this blog post, I would like to share our plan for redesigning APIRule CR and explain how the new version affects the components backing up API Gateway.

## Background

The API Gateway component is a Kubernetes controller responsible for watching the APIRule CR and creating the subresources needed to expose and secure a workload. The API Gateway controller utilizes Istio VirtualService and ORY Oathkeeper Rule under the hood. As of Kyma 2.2 ORY stack, Hydra and Oathkeeper are deprecated, and Istio CRs will provide the equivalent functionalities. The new solution based on Istio will improve the stability and reliability of an exposed workload as well as simplify the API Gateway architecture.

## Current architecture

The current architecture uses VirtualService and Rule CRs. Therefore, the API Gateway component has dependencies to both the Istio component and the ORY Oathkeeper component. If a workload owner decides to secure their workload using the OAuth2 client, the ORY Hydra OAuth2 server dependency must also be created.

![](/legacyfs/online/storage/blog_attachments/2023/02/api-gateway-deps.png)

The following chart shows the flow of exposing and securing a workload. Let's see how each dependency is used. When the user deploys their workload and wants to expose and secure it, they create Istio Gateway CR and proceed to create APIRule CR, which is processed by the API Gateway controller. The API Gateway controller creates Istio VirtualService to expose a workload and ORY Oathkeeper Rule to secure the workload. Depending on the requirements, the user willing to access the workload might need to issue a token. They can utilize an ORY Hydra opaque token or a JWT OIDC-compliant provider, for example, SAP Cloud Identity Services - Identity Authentication. ORY Hydra OAuth2Client CR and credentials used to issue a token from ORY Hydra need to be created. Finally, the workload can be accessed using the token. To learn about JWT's best practices, read [this blog post](https://kyma-project.io/blog/2023/1/12/jwt-best-practices/).

![](/legacyfs/online/storage/blog_attachments/2023/02/oauth2-flow.png)

When the user sends a request with the token to the workload, the request reaches Istio Ingress Gateway first. Istio Ingress Gateway forwards this request to the ORY Oathkeeper component - a reverse proxy responsible for authorizing incoming requests. ORY Oathkeeper checks the existing rules. When it finds a matching rule, it validates and authorizes the request. The successfully authorized request is forwarded to the workload.

![](/legacyfs/online/storage/blog_attachments/2023/02/jwt-flow.png)

## Where are we heading?

Our goal is to provide a component that will enable users to expose their workloads reliably and securely. The research we conducted on available solutions convinced us that it is time to part ways with ORY stack and start using Istio - the component which Kyma already provides. The APIRule JWT handler's implementation based on ORY Oauthkeeper Rule will be replaced with the implementation based on Istio AuthorizationPolicy and RequestAuthentication CRs. APIRule OAuth2 handler's implementation will be replaced with Istio's external authorization functionality utilizing the oauth2-proxy component.

![](/legacyfs/online/storage/blog_attachments/2023/02/api-gateway-future-deps.png)

The following diagram showcases the API Gateway controller, which creates the resources related to Istio. The user creates an application using the OICD-compliant provider of their choice, configured by the administrator in the oauth2-proxy component being part of the Istio external authorizer.

![](/legacyfs/online/storage/blog_attachments/2023/02/oauth2-future.png)

In the future, Istio Ingress Gateway will be responsible for authorization in the JWT flow. It will validate the token against the configuration defined in RequestAuthentication CR and authorize the request as described in AuthorizationPolicy CR. If allowed, the request will be forwarded to the workload.

![](/legacyfs/online/storage/blog_attachments/2023/02/jwt-future.png)

Leveraging Istio saves us one hop to the additional component and makes the processing of requests faster. By removing ORY Oathkeeper, we simplify complexity and improve the stability of the API Gateway component. Adding oauth2-proxy managed by the Kyma Istio component will facilitate exposing and securing Kiali, Grafana, and Jaeger and enable using them in the OAuth2 scenario with API Gateway.

## How do we get there?

Improving the architecture of the API Exposure functionalities necessitates a few profound changes. We plan to introduce the changes in phases in order to reduce the risk they might entail. We will support and guide our customers at every step of the process. We are actively working on the alternative implementation of the APIRule JWT handler based on Istio AuthorizationPolicy and RequestAuthentication CRs. We consider JWT best practices on the token verifier side and identify the breaking changes. Our goal is to release this implementation as early as possible so that users can start testing it as soon as possible and we can collect feedback and features requests. The changes will be released as a feature available for users who want to participate in early adoption. In parallel, we are working on alternatives for the ORY Hydra component, which will be followed by the changes to the APIRule OAuth2 handlers. All the improvements will b...