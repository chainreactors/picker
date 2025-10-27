---
title: Protecting GraphQL APIs from malicious queries
url: https://buaq.net/go-168413.html
source: unSafe.sh - 不安全
date: 2023-06-13
fetch_date: 2025-10-04T11:44:26.438511
---

# Protecting GraphQL APIs from malicious queries

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/620b89a3d8ec089d35b42b0bea5b391d.jpg)

Protecting GraphQL APIs from malicious queries

Loading...
*2023-6-12 21:0:8
Author: [blog.cloudflare.com(查看原文)](/jump-168413.htm)
阅读量:33
收藏*

---

Loading...

* [![John Cosgrove](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2023/03/IMG-9296-smol.jpg)](https://blog.cloudflare.com/author/john-cosgrove/)
* [![Ilya Andreev](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/https://blog-cloudflare-com-assets.storage.googleapis.com/2020/04/IMG-7360-3.jpg)](https://blog.cloudflare.com/author/ilya/)

![Protecting GraphQL APIs from malicious queries](https://blog.cloudflare.com/content/images/2023/06/image1-2.png)

Starting today, Cloudflare’s API Gateway can protect GraphQL APIs against malicious requests that may cause a denial of service to the origin. In particular, API Gateway will now protect against two of the most common GraphQL abuse vectors: **deeply nested queries** and **queries that request more information** than they should.

Typical RESTful HTTP APIs contain tens or hundreds of endpoints. GraphQL APIs differ by typically only providing a single endpoint for clients to communicate with and offering highly flexible queries that can return variable amounts of data. While GraphQL’s power and usefulness rests on the flexibility to query an API about only the specific data you need, that same flexibility adds an increased risk of abuse. Abusive requests to a single GraphQL API can place disproportional load on the origin, abuse [the N+1 problem](https://hygraph.com/blog/graphql-n-1-problem), or exploit a recursive relationship between data dimensions. In order to add GraphQL security features to API Gateway, we needed to obtain visibility *inside* the requests so that we could apply different security settings based on request parameters. To achieve that visibility, we built our own GraphQL query parser. Read on to learn about how we built the parser and the security features it enabled.

### The power of GraphQL

Unlike a REST API, where the API’s users are limited to what data they can query and change on a per-endpoint basis, a GraphQL API offers users the ability to query and change any data they wish with an open-ended, yet structured request to a single endpoint. This open-endedness makes GraphQL APIs very [powerful](https://graphql.org/learn/). Each user can query for a completely custom set of data and receive their custom response in a single HTTP request. Here are two example queries and their responses. These requests are typically sent via HTTP POST methods to an endpoint at /graphql.

```
# A query asking for multiple nested subfields of the "hero" object. This query has a depth level of 2.
{
  hero {
    name
    friends {
      name
    }
  }
}

# The corresponding response.
{
  "data": {
    "hero": {
      "name": "R2-D2",
      "friends": [
        {
          "name": "Luke Skywalker"
        },
        {
          "name": "Han Solo"
        },
        {
          "name": "Leia Organa"
        }
      ]
    }
  }
}
```

```
# A query asking for just one subfield on the same "hero" object. This query has a depth level of 1.
{
  hero {
    name
  }
}

# The corresponding response.
{
  "data": {
    "hero": {
      "name": "R2-D2"
    }
  }
}
```

These custom queries give GraphQL endpoints *more flexibility than conventional REST endpoints*. But this flexibility also means GraphQL APIs can be subject to very different load or security risks based on the requests that they are receiving. For example, an attacker can request the exact same, valid data as a benevolent user would, but exploit the data’s self-referencing structure and ask that an origin return hundreds of thousands of rows replicated over and over again. Let’s consider an example, in which we operate a petitioning platform where our data model contains petitions and signers objects. With GraphQL, an attacker can, in a single request, query for a single petition, then for all people who signed that petition, then for all petitions each of those people have signed, then for all people that signed any of those petitions, then for all petitions that… you see where this is going!

```
query {
 petition(ID: 123) {
   signers {
     nodes {
       petitions {
         nodes {
           signers {
             nodes {
               petitions {
                 nodes {
                    ...
                 }
               }
             }
           }
         }
       }
     }
   }
 }
}
```

A rate limit won’t protect against such an attack because the entire query fits into a single request.

So how can we secure GraphQL APIs? There is little agreement in the industry around what makes a GraphQL endpoint secure. For some, this means rejecting invalid queries. Normally, an invalid query refers to a query that would fail to compile by a GraphQL server and not cause any substantial load on the origin, but would still add noise and error logs and reduce operational visibility. For others, this means creating complexity-based rate limits or perhaps flagging [broken object-level authorization](https://owasp.org/API-Security/editions/2023/en/0xa1-broken-object-level-authorization/). Still others want deeper visibility into query behavior and an ability to validate queries against a predefined schema.

When creating new features in API Gateway, we often start by providing deeper visibility for customers into their traffic behavior related to the feature in question. This way we create value from the large amount of data we see in the Cloudflare network, and can have conversations with customers where we ask: *“Now that you have these data insights, what actions would you like to take with them?”*. This process puts us in a good position to build a second, more actionable iteration of the feature.

We decided to follow the same process with GraphQL protection, with parsing GraphQL requests and gathering data as our first goal.

### Parsing GraphQL quickly

As a starting point, we wanted to collect request query size and depth attributes. These attributes offer a surprising amount of insight into the query – if the query is requesting a single field at depth level 15, is it really innocuous or is it exploiting some recursive data relationship? if the query is asking for hundreds of fields at depth level 3, why wouldn’t it just ask for the entire object at level 2 instead?

To do this, we needed to parse queries without adding latency to incoming requests. We evaluated multiple open source GraphQL parsers and quickly realized that their performance would put us at the risk of adding hundreds of microseconds of latency to the request duration. Our goal was to have a p95 parsing time of under 50 microseconds. Additionally, the infrastructure we were planning to use to ship this functionality has a strict no-heap-allocation policy – this means that any memory allocated by a parser to process a request has to be amortized by being reused when parsing any subsequent requests. Parsing GraphQL in a no-allocation manner is not a fundamental technical requirement for us over the long-term, but it was a necessity if we wanted to build something quickly with confidence that the proof of concept will meet our performance expectations.

Meeting the latency and memory allocation constraints meant that we had to write a parser of our own. Building an entire abstract syntax tree of unpredictable structure requires allocating memory on the heap, and that’s what made conventional parsers unfit for our requirements....