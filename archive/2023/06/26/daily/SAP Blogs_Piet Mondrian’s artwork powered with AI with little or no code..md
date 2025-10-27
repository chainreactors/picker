---
title: Piet Mondrian’s artwork powered with AI with little or no code.
url: https://blogs.sap.com/2023/06/25/piet-mondrians-artwork-powered-with-ai-with-little-or-no-code./
source: SAP Blogs
date: 2023-06-26
fetch_date: 2025-10-04T11:46:12.861755
---

# Piet Mondrian’s artwork powered with AI with little or no code.

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by SAP](/t5/technology-blog-posts-by-sap/bg-p/technology-blog-sap)
* Piet Mondrian's artwork powered with AI with littl...

Technology Blog Posts by SAP

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-sap/article-id/150862&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Piet Mondrian's artwork powered with AI with little or no code.](/t5/technology-blog-posts-by-sap/piet-mondrian-s-artwork-powered-with-ai-with-little-or-no-code/ba-p/13529861)

![quovadis](https://avatars.profile.sap.com/5/f/id5f0d9937a29017f07c2dd14f033b8d49b11261952ae7ce68ec448c7d5c66f338_small.jpeg "quovadis")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[quovadis](https://community.sap.com/t5/user/viewprofilepage/user-id/743)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-sap&message.id=150862)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-sap/article-id/150862)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13529861)

‎2023 Jun 25
1:21 PM

[2
Kudos](/t5/kudos/messagepage/board-id/technology-blog-sap/message-id/150862/tab/all-users "Click here to see who gave kudos to this post.")

1,276

* SAP Managed Tags
* [SAP BTP, Kyma runtime](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%252C%2520Kyma%2520runtime/pd-p/73554900100800003012)
* [API Management](https://community.sap.com/t5/c-khhcw49343/API%2520Management/pd-p/67838200100800006828)
* [SAP Build Apps](https://community.sap.com/t5/c-khhcw49343/SAP%2520Build%2520Apps/pd-p/6cfd8176-04ae-4548-8f38-158456e1a47a)

* [API Management

  SAP Business Technology Platform](/t5/c-khhcw49343/API%2BManagement/pd-p/67838200100800006828)
* [SAP BTP, Kyma runtime

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%25252C%2BKyma%2Bruntime/pd-p/73554900100800003012)
* [SAP Build Apps

  Additional Software Product](/t5/c-khhcw49343/SAP%2BBuild%2BApps/pd-p/6cfd8176-04ae-4548-8f38-158456e1a47a)

View products (3)

|
 [![](/legacyfs/online/storage/blog_attachments/2021/06/SAP_Business_Technology_Platform_R.png)](https://www.sap.com/products/business-technology-platform.html) |

|
 [![](/legacyfs/online/storage/blog_attachments/2023/05/mug2.png)](https://platform.openai.com/docs/guides/images)  *Image created with DALL·E* |
 Piet Mondrian's artwork.  I have recently attended **HILMA AF KLINT & PIET MONDRIAN** **FORMS OF LIFE** [exhibition](https://www.tate.org.uk/whats-on/tate-modern/hilma-af-klint-piet-mondrian) at [Tate Modern](https://www.tate.org.uk/).     At the end of the exhibition there was a shop where people could buy different memorabilia. There were Piet Mondrian's  t-shirts, socks, mugs and pencils... Well, I bought a t-shirt.    Still, I wanted a Piet Mondrian's mug. However, my kitchen cupboard has no more overflow space...    I had to get creative.... |

Disclaimer:

* The ideas presented in this blog are personal insights thus are not necessarily endorsed by SAP.

* Images/data in this blog post is from personal [SAP BTP Free Tier](https://me.sap.com/) and/or [OpenAI](https://platform.openai.com/account/) accounts. Any resemblance to real data is purely coincidental.

* Access to some online resources referenced in this blog may be subject to a contractual relationship with either SAP and/or OpenAI.

---

* Before going any further, please make yourself familiar and comfortable with the following: [Brand guidelines](https://openai.com/brand#usage-terms), [usage policies](https://openai.com/policies/usage-policies),  [safety measures](https://openai.com/safety) and [DALL-E-2 pre-training mitigations](https://openai.com/research/dall-e-2-pre-training-mitigations)

---

# Putting it all together

Here goes the agenda for this brief.

|
 * [Image generation with DALL·E API.](#dalle-2)  * [**A wish come true. SAP BTP, Kyma runtime serverless to the rescue...**](#wish-come-true)  * **No code today. DALL·E API with SAP API Management**     + [API proxy](#api-proxy)    + [CORS policy](#cors-policy)    + [Streaming and gateway timeout](#streaming-settings)  * **Piet Mondrian's mug with SAP Appgyver / SAP Build Apps**     + [Data source logic](#data-logic)    + [Page logic](#page-logic)    + [SAP Build Apps JS custom code](#custom-code)  * [Quovadis ?](#quovadis) |

## Image generation with DALL·E API.

With [DALL·E API](https://platform.openai.com/docs/guides/images) it is possible to integrate state of the art image generation capabilities directly into apps and products...with little or no code.

## A wish come true. SAP BTP, Kyma runtime serverless to the rescue...

With a few lines of code my wish of owning a digital mug has eventually come true.

```
const { Configuration, OpenAIApi } = require("openai");

const configuration = new Configuration({

  apiKey: process.env.OPENAI_API_KEY,

});

const openai = new OpenAIApi(configuration);

async function PietMondrianMug() {

  try

  {

  const response = await openai.createImage({

    prompt: "create Piet Mondrian mug",

    n: 4, //1,

    size: "1024x1024",

  });

  const data = response.data;

  console.log(data);

  return JSON.stringify(data,0,2);

  }

  catch (err) {

    console.log(err.message);

    return JSON.stringify(err, 0, 2);

  }

}

module.exports = {

  main: async function (event) {

    switch(event.extensions.request.url) {

      case '/mug':

        return PietMondrianMug();

    }

    return "no mug today";

  }

}
```

Here goes the *serverless* payload with 4 mug images:

```
{

  "created": *********,

  "data": [

    {

      "url": "https://***.blob.***/private/org-*****"

    },

################# truncated payload ############################

  ]

}
```

---

## No code today. DALL·E API with SAP API Management

In my quest for simplicity, I personally find [SAP API Management](https://help.sap.com/docs/sap-api-management), part of [SAP BTP platform](https://help.sap.com/docs/btp), one of the best low code/no code API *middlewares* ever.

It allows to create API proxies with built-in [security](https://api.sap.com/package/SecurityBestPractices/policytemplate) and [CORS](https://api.sap.com/package/CrossOriginResourceSharing/policytemplate) policies and even have HTTP [streaming](https://help.sap.com/docs/sap-api-management/sap-api-management/enable-streaming-of-requests-and-responses-in-api-proxy) to cope with the large payloads. With little or no code at all.

### SAP APIM can be used to create an API proxy, as follows:

|
 OpenAPI proxy resources |
 Security policy |

|
 ![](/legacyfs/online/storage/blog_attachments/2023/05/piet14.png) |
 ![](/legacyfs/online/storage/blog_attachments/2023/05/piet15.png) |

The API Keys are stored in a **kvm** ( key value map), as depicted below:

```
<!-- Key/value pairs can be stored, retrieved, and deleted from named existing maps by configuring this policy by specifying PUT, GET, or DELETE operations -->

<!-- https://help.sap.com/viewer/66d066d903c2473f81ec33acfe2ccdb4/Cloud/en-US/b72dc3f262c1441587e76d0e808... -->

<!-- mapIdentifier refers to the name of the key value map -->

<KeyValueMapOperations mapIdentifier="openapi" async...