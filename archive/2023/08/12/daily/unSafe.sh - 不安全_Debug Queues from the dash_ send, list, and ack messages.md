---
title: Debug Queues from the dash: send, list, and ack messages
url: https://buaq.net/go-174276.html
source: unSafe.sh - 不安全
date: 2023-08-12
fetch_date: 2025-10-04T12:00:19.253216
---

# Debug Queues from the dash: send, list, and ack messages

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

![](https://8aqnet.cdn.bcebos.com/fe76a47d57f3522c77b6af5bdb7ffafd.jpg)

Debug Queues from the dash: send, list, and ack messages

Loading...
*2023-8-11 21:1:19
Author: [blog.cloudflare.com(查看原文)](/jump-174276.htm)
阅读量:16
收藏*

---

Loading...

* [![Emilie Ma](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2023/07/DSC_0012---Emilie-Ma.jpg)](https://blog.cloudflare.com/author/emilie/)

![Debug Queues from the dash: Send, list, and ack messages](https://blog.cloudflare.com/content/images/2023/08/image3-1.png)

Today, August 11, 2023, we are excited to announce a new debugging workflow for Cloudflare Queues. Customers using Cloudflare Queues can now send, list, and acknowledge messages directly from the Cloudflare dashboard, enabling a more user-friendly way to interact with Queues. Though it can be difficult to debug asynchronous systems, it’s now easy to examine a queue’s state and test the full flow of information through a queue.

With [guaranteed delivery](https://developers.cloudflare.com/queues/learning/delivery-guarantees/), [message batching](https://developers.cloudflare.com/queues/learning/batching-retries/), [consumer concurrency](https://developers.cloudflare.com/queues/learning/consumer-concurrency/), and more, Cloudflare Queues is a powerful tool to connect services reliably and efficiently. Queues integrate deeply with the existing Cloudflare Workers ecosystem, so developers can also leverage our many other products and services. Queues can be bound to producer Workers, which allow Workers to send messages to a queue, and to consumer Workers, which pull messages from the queue.

We’ve received feedback that while Queues are effective and performant, customers find it hard to debug them. After a message is sent to a queue from a producer worker, there’s no way to inspect the queue’s contents without a consumer worker. The limited transparency was frustrating, and the need to write a skeleton worker just to debug a queue was high-friction.

![](https://blog.cloudflare.com/content/images/2023/08/image7.png)

Now, with the addition of new features to send, list, and acknowledge messages in the Cloudflare dashboard, we’ve unlocked a much simpler debugging workflow. You can send messages from the Cloudflare dashboard to check if their consumer worker is processing messages as expected, and verify their producer worker’s output by previewing messages from the Cloudflare dashboard.

The pipeline of messages through a queue is now more open and easily examined. Users just getting started with Cloudflare Queues also no longer have to write code to send their first message: it’s as easy as clicking a button in the Cloudflare dashboard.

![](https://blog.cloudflare.com/content/images/2023/08/image6.png)

### Sending messages

Both features are located in a new ****Messages**** tab on any queue’s page. Scroll to ****Send message**** to open the message editor.

![](https://blog.cloudflare.com/content/images/2023/08/image1-4.png)

From here, you can write a message and click **Send message** to send it to your queue. You can also choose to send JSON, which opens a JSON editor with syntax highlighting and formatting. If you’ve saved your message as a file locally, you can drag-and-drop the file over the textbox or click **Upload a file** to send it as well.

This feature makes testing changes in a queue’s consumer worker much easier. Instead of modifying an existing producer worker or creating a new one, you can send one-off messages. You can also easily verify if your queue consumer settings are behaving as expected: send a few messages from the Cloudflare dashboard to check that messages are batched as desired.

Behind the scenes, this feature leverages the same pipeline that Cloudflare Workers uses to send messages, so you can be confident that your message will be processed as if sent via a Worker.

### Listing messages

On the same page, you can also inspect the messages you just sent from the Cloudflare dashboard. On any queue’s page, open the **Messages** tab and scroll to **Queued messages**.

If you have a consumer attached to your queue, you’ll fetch a batch of messages of the same size as configured in your queue consumer settings by default, to provide a realistic view of what would be sent to your consumer worker. You can change this value to preview messages one-at-a-time or even in much larger batches than would be normally sent to your consumer.

After fetching a batch of messages, you can preview the message’s body, even if you’ve sent raw bytes or a JavaScript object supported by the [structured clone](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API/Structured_clone_algorithm) algorithm. You can also check the message’s timestamp; number of retries; producer source, such as a Worker or the Cloudflare dashboard; and type, such as text or JSON. This information can help you debug the queue’s current state and inspect where and when messages originated from.

![](https://blog.cloudflare.com/content/images/2023/08/image5-2.png)

The batch of messages that’s returned is the same batch that would be sent to your consumer Worker on its next run. Messages are even guaranteed to be in the same order on the UI as sent to your consumer. This feature grants you a looking glass view into your queue, matching the exact behavior of a consumer worker. This works especially well for debugging messages sent by producer workers and verifying queue consumer settings.

Listing messages from the Cloudflare dashboard also doesn’t interfere with an existing connected consumer. Messages that are previewed from the Cloudflare dashboard stay in the queue and do not have their number of retries affected.

This ‘peek’ functionality is unique to Cloudflare Queues: Amazon SQS bumps the number of retries when a message is viewed, and RabbitMQ retries the message, forcing it to the back of the queue. Cloudflare Queues’ approach means that previewing messages does not have any unintended side effects on your queue and your consumer. If you ever need to debug queues used in production, don’t worry - listing messages is entirely safe.

As well, you can now remove messages from your queue from the Cloudflare dashboard. If you’d like to remove a message or clear the full batch from the queue, you can select messages to acknowledge. This is useful for preventing buggy messages from being repeatedly retried without having to write a dummy consumer.

![](https://blog.cloudflare.com/content/images/2023/08/image4-1.png)![](https://blog.cloudflare.com/content/images/2023/08/image2-3.png)

You might have noticed that this message preview feature operates similarly to another popular feature request for an HTTP API to pull batches of messages from a queue. Customers will be able to make a request to the API endpoint to receive a batch of messages, then acknowledge the batch to remove the messages from the queue. Under the hood, both listing messages from the Cloudflare dashboard and HTTP Pull/Ack use a common infrastructure, and HTTP Pull/Ack is coming very soon!

These debugging features have already been invaluable for testing example applications we’ve built on Cloudflare Queues. At an internal hack week event, we built a web crawler with Queues as an example use-case (check out the tutorial [here](https://developers.cloudflare.com/queues/examples/web-crawler-with-browser-rendering/)!). During development, we took advantage of this user-friendly way to send messages to quickly iterate on a consumer worker before we built a producer worker. As well, when we en...