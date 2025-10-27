---
title: CAP: GraphQL as new protocol
url: https://blogs.sap.com/2023/03/18/cap-graphql-as-new-protocol/
source: SAP Blogs
date: 2023-03-19
fetch_date: 2025-10-04T10:02:26.011718
---

# CAP: GraphQL as new protocol

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* CAP: GraphQL as new protocol

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/160491&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [CAP: GraphQL as new protocol](/t5/technology-blog-posts-by-members/cap-graphql-as-new-protocol/ba-p/13552575)

![jhodel18](https://avatars.profile.sap.com/b/8/idb8ec2bceaa1ea6338b462cd520e0c94f5828817f260d6b0c6344fd9d6977cf6b_small.jpeg "jhodel18")

[jhodel18](https://community.sap.com/t5/user/viewprofilepage/user-id/6257)

Active Contributor

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=160491)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/160491)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13552575)

‎2023 Mar 18
7:39 AM

[6
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/160491/tab/all-users "Click here to see who gave kudos to this post.")

6,455

* SAP Managed Tags
* [SAP Cloud Application Programming Model](https://community.sap.com/t5/c-khhcw49343/SAP%2520Cloud%2520Application%2520Programming%2520Model/pd-p/9f13aee1-834c-4105-8e43-ee442775e5ce)
* [Node.js](https://community.sap.com/t5/c-khhcw49343/Node.js/pd-p/723714486627645412834578565527550)

* [Node.js

  Programming Tool](/t5/c-khhcw49343/Node.js/pd-p/723714486627645412834578565527550)
* [SAP Cloud Application Programming Model

  Software Product Function](/t5/c-khhcw49343/SAP%2BCloud%2BApplication%2BProgramming%2BModel/pd-p/9f13aee1-834c-4105-8e43-ee442775e5ce)

View products (2)

I've been looking into SAP Graph and GraphQL for quite some time now, and out of curiosity, I tried to look into CAP if it already supports GraphQL, and lucky enough CAP just recently started supporting GraphQL by releasing [@cap-js/graphql](https://www.npmjs.com/package/%40cap-js/graphql?activeTab=readme) which acts as a [GraphQL adapter](https://cap.cloud.sap/docs/node.js/protocols#graphql-adapter).

In this blog post, I will be giving a quick introduction to GraphQL in CAP.

![](/legacyfs/online/storage/blog_attachments/2023/03/capgraphql.png)

## Set up GraphQL adapter

---

Technically the adapter is very easy to set up. It is very straightforward to follow the instructions mentioned in the [@cap-js/graphql](https://www.npmjs.com/package/%40cap-js/graphql?activeTab=readme) node module, but for the sake of completeness, I will mention it here as well.

* Add the GraphQL adapter to your CAP project:

```
> npm install @cap-js/graphql
```

|
 **NOTE:** The adapter is relatively new (3 months old at the time this blog post is written) so make sure your cap node modules are up to date - **[@Sisn](/t5/user/viewprofilepage/user-id/1387241)/cds** and **[@Sisn](/t5/user/viewprofilepage/user-id/1387241)/cds-dk**. |

* Register GraphQL adapter in your projects `package.json`:

```
{

  "cds": {

    "protocols": {

      "graphql": { "path": "/graphql", "impl": "@cap-js/graphql" }

    }

  }

}
```

## Testing the GraphQL endpoint

---

Run the CAP application as usual using `cds watch` terminal command and the GraphQL endpoint will be available at:

```
http://localhost:4004/graphql
```

* Testing via the built-in GraphiQL client

![](/legacyfs/online/storage/blog_attachments/2023/03/graphiql-testing-2.png)

* Testing via Postman client

![](/legacyfs/online/storage/blog_attachments/2023/03/postman-testing.png)

* To learn more about the query features of GraphQL, head to <https://graphql.org>.

I'm sharing here my CAP project if you want to follow exactly the testing samples I provided above:

* <https://github.com/jcailan/cap-fe-samples>

## Closing

---

GraphQL protocol is very much a welcome addition to the already formidable features offered by the CAP framework. It acts as a complementary to OData V4 as another option as a query language. And although it still missing some capabilities (as mentioned in the [limitations section](https://www.npmjs.com/package/%40cap-js/graphql?activeTab=readme) of the GraphQL adapter), it already looks promising to use productively especially if you prefer using GraphQL protocol.

~~~~~~~~~~~~~~~~

Appreciate it if you have any comments, suggestions, or questions. Cheers!~

* [graphql](/t5/tag/graphql/tg-p/board-id/technology-blog-members)

1 Comment

You must be a registered user to add a comment. If you've already registered, sign in. Otherwise, register and sign in.

* [Comment](/plugins/common/feature/oidcss/sso_login_redirect/providerid/sap_ids_prompt?redirectreason=permissiondenied&referer=https%3A%2F%2Fcommunity.sap.com%2Ft5%2Ftechnology-blog-posts-by-members%2Fcap-graphql-as-new-protocol%2Fba-p%2F13552575%23comment-on-this)

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin

Related Content

* [Looking for Payload Structure for AI Adapter's with Request Payload Source as Exchange Body](/t5/technology-q-a/looking-for-payload-structure-for-ai-adapter-s-with-request-payload-source/qaq-p/14233049)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  Wednesday
* [How to use Version Management with Github Repository](/t5/technology-blog-posts-by-sap/how-to-use-version-management-with-github-repository/ba-p/13811133)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  Tuesday
* [Vibe Coding with MCP Servers & SAP AI Core: Toward "Coding by Conversation"](/t5/technology-q-a/vibe-coding-with-mcp-servers-amp-sap-ai-core-toward-quot-coding-by/qaq-p/14230581)
  in [Technology Q&A](/t5/technology-q-a/qa-p/technology-questions)  Monday
* [Join SAPUI5 Sessions at SAP TechEd 2025](/t5/technology-blog-posts-by-sap/join-sapui5-sessions-at-sap-teched-2025/ba-p/14227900)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  Monday
* [Optimizing SAP Analytics Cloud – Best Practices and Performance](/t5/technology-blog-posts-by-sap/optimizing-sap-analytics-cloud-best-practices-and-performance/ba-p/14229397)
  in [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)  a week ago

Top kudoed authors

| User | Count |
| --- | --- |
| [![WouterLemaire](https://avatars.profile.sap.com/9/5/id95a688fa6b84e4186cabf39d7a83127ea90dd51dd190d355416d56f7d3a5be56_small.jpeg "WouterLemaire")  ![SAP Mentor](/html/@F4C200E47DAE3459A6BD3FBB7F9955B8/rank_icons/mentor-rank-16x16.svg "SAP Mentor") WouterLemaire](/t5/user/viewprofilepage/user-id/9863) | 6 |
| [![rajarajeswari_kaliyaperum](https://avatars.profile.sap.com/c/1/idc10d67889f40de37cfb340af4a802e39952419bdc3ee1ba9dd6000bf645e35b6_small.jpeg "rajarajeswari_kaliyaperum")  rajarajeswari\_kaliyaperum](/t5/user/viewprofilepage/user-id/654809) | 4 |
| [![kartheekkkota](https://avatars.profile.sap.com/2/d/id2d7e639322351b2b6b5a2b0a8d59075fd847a612a238bd7704e00c54f4a4e975_small.jpeg "kartheekkkota")  kartheekkkota](/t5/user/viewprofilepage/user-id/227849) | 4 |
| [![Sandra_Rossi](https://avatars.profile.sap.com/5/a/id5ade69af148fee003e69a3410fe4ea7d8d92f9f0535ff49f640e7d27e69ef...