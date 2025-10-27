---
title: Cloudflare Zaraz supports JSONata
url: https://buaq.net/go-170581.html
source: unSafe.sh - 不安全
date: 2023-06-28
fetch_date: 2025-10-04T11:44:19.745018
---

# Cloudflare Zaraz supports JSONata

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

![](https://8aqnet.cdn.bcebos.com/2b33d3e0e4e67aeaee0f295add043df6.jpg)

Cloudflare Zaraz supports JSONata

Loading...
*2023-6-27 21:0:56
Author: [blog.cloudflare.com(查看原文)](/jump-170581.htm)
阅读量:19
收藏*

---

Loading...

* [![Yo'av Moshe](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2021/11/IMG_4345-01-01.jpeg)](https://blog.cloudflare.com/author/yoav/)

![Cloudflare Zaraz supports JSONata](https://blog.cloudflare.com/content/images/2023/06/image1-44.png)

Cloudflare users leverage Zaraz for loading their third-party JavaScript tools. Tools like analytics, conversion pixels, widgets and alike, [load faster and safer when loaded through Zaraz](https://blog.cloudflare.com/cloudflare-acquires-zaraz-to-enable-cloud-loading-of-third-party-tools/).

When configuring a tool in Zaraz, users can specify the payload to be included when sending information to it. This allows for the transmission of more detailed data. For example, when sending the "Button Clicked" event to Google Analytics, users can include additional information such as the ID of the button element and the content of the `user_id` cookie at the time of the button press. In Zaraz, users have the flexibility to add as many fields as desired when configuring the action.

Typically, information reaches Zaraz through the execution of `zaraz.track("event name", { properties })` within the website's code. The `properties` object can contain relevant details that will be sent to third-party tools, such as the button ID in the previous example. However, there are cases where users may need to process and manipulate the information before sending it to their third-party tools.

To address this requirement, we recently introduced [Worker Variables](https://blog.cloudflare.com/dynamic-data-collection-with-zaraz-worker-variables/), which enables users to send information to a Cloudflare Worker, perform manipulations on it, and return a modified value. This feature offers immense power and flexibility. For instance, users can communicate with their backend server to retrieve data and leverage JavaScript to perform necessary calculations. With Worker Variables, users have access to a fully-featured Worker, opening up endless possibilities.

However, feedback from our users highlighted the need for a middle-ground solution. Sometimes, the data manipulation required is minor, and employing a Cloudflare Worker might feel like overkill. It is in response to this feedback that we decided to integrate with [JSONata](https://jsonata.org/).

### What is JSONata?

JSONata calls itself a JSON query and transformation language. While some developers may already be familiar with jq, the command-line JSON processor, JSONata offers similar features with a syntax that we believe is more intuitive and easier to understand. Since JSONata is a JavaScript library, it was very easy to integrate into Cloudflare Zaraz.

Let’s say we have JSON document like the following:

```
{
  "name": "Jane Smith",
  "address": {
    "street": "123 High St",
    "city": "London"
  },
  "pets": [
    { "type": "hamster", "name": "Rex" },
    { "type": "parrot", "name": "Milo" },
    { "type": "parrot", "name": "Alfie" }
  ]
}
```

With JSONata, with JSONata, one can run interesting queries on the document:

```
$count(pets) // 3

address.city // London

pets[type="parrot"].name // ["Alfie", "Milo"]
```

The JSONata documentation includes many examples for what you do with it, and there’s even [a playground](https://try.jsonata.org/) where you can try your JSONata queries live.

### Using JSONata with Zaraz

JSONata has been tightly integrated with Cloudflare Zaraz, allowing you to leverage its capabilities in the fields of all Actions, Triggers, and Variables. Before diving into writing your JSONata expressions, it's essential to understand the JSON document you'll be working with.

Similar to Worker Variables or the HTTP Request tool, JSONata has access to the Zaraz Context. This object contains information from your `zaraz.track()` and `zaraz.ecommerce()` calls, as well as automatically gathered data by Zaraz, such as the current page URL, cookies, page title, user-agent string, and more. You can find the complete reference for this object in [the Zaraz documentation](https://developers.cloudflare.com/zaraz/reference/context/).

Using your JSONata query is straightforward once you are familiar with it. To incorporate the query into your field content, simply enclose it within double curly brackets. The expression will be passed to JSONata along with the Zaraz Context object, and the resulting value will be used for the field.

Let's explore two examples from our documentation. Often, there's a need to convert a string to lowercase, such as when comparing it to another value in a regular expression. Suppose the original string is derived from a cookie named `loggedIn`, that specifies if the current user is logged in. In that case, we can use JSONata to transform the value to lowercase using the expression $lowercase(system.cookies.loggedIn). If we want to use this expression within a trigger, we navigate to the Zaraz dashboard and choose our trigger, locate the relevant match rule, and enter {{ $lowercase(system.cookies.loggedIn) }} as the value. Now, the cookie value will be compared in its lowercase format.

![](https://blog.cloudflare.com/content/images/2023/06/image2-39.png)

You can also run simple calculations. Assuming you are using `zaraz.track()` to send the cart content like this:

```
zaraz.track("Cart Viewed",
  {  products:
	[
	{
  	sku: '2671033',
  	name: 'V-neck T-shirt',
  	price: 14.99,
  	quantity: 3
	},{
  	sku: '2671034',
  	name: 'T-shirt',
  	price: 10.99,
  	quantity: 2
	},
	],
  }
);
```

If the field in which you want to include the total sum of all products, you will enter {{ $sum(client.products.(price \* quantity)) }}. This will multiply the price of each product by its quantity, and then sum up the total.

![](https://blog.cloudflare.com/content/images/2023/06/image3-31.png)

### Start using JSONata today

JSONata support is available to all Zaraz users at no cost, and it is enabled automatically for all websites. Start using JSONata today to send finely tuned data to your providers or APIs with minimal code and zero maintenance for your data infrastructure. If you need any help - join [our Discord channel](https://discord.gg/2TRr6nSxdd)!

We protect
[entire corporate networks](https://www.cloudflare.com/network-services/),
help customers build
[Internet-scale applications efficiently](https://workers.cloudflare.com/),
accelerate any
[website
or Internet application](https://www.cloudflare.com/performance/accelerate-internet-applications/),
[ward off DDoS
attacks](https://www.cloudflare.com/ddos/), keep
[hackers at
bay](https://www.cloudflare.com/application-security/),
and can help you on
[your journey to Zero Trust](https://www.cloudflare.com/products/zero-trust/).

Visit [1.1.1.1](https://1.1.1.1/) from any device to get started with
our free app that makes your Internet faster and safer.

To learn more about our mission to help build a better Internet, [start here](https://www.cloudflare.com/learning/what-is-cloudflare/). If you're looking for a
new career direction, check out [our open
positions](https://cloudflare.com/careers).

[Zaraz](https://blog.cloudflare.com/tag/zaraz/)
[JSONata](https://blog.cloudflare.com/tag/jsonata/)

文章来源: http://blog.cloudflare.com/zaraz-adds-jsonata-support/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan...