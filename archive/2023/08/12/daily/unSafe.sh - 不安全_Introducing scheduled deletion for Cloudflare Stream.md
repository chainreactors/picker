---
title: Introducing scheduled deletion for Cloudflare Stream
url: https://buaq.net/go-174277.html
source: unSafe.sh - 不安全
date: 2023-08-12
fetch_date: 2025-10-04T12:00:19.813627
---

# Introducing scheduled deletion for Cloudflare Stream

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

![](https://8aqnet.cdn.bcebos.com/573500e618fec85e2cd9ca5cbe540694.jpg)

Introducing scheduled deletion for Cloudflare Stream

Loading...
*2023-8-11 21:0:45
Author: [blog.cloudflare.com(查看原文)](/jump-174277.htm)
阅读量:16
收藏*

---

Loading...

* [![Austin Christiansen](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2023/08/PFP-1--1-.jpeg)](https://blog.cloudflare.com/author/austin/)
* [![Taylor Smith](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2023/06/IMG_20210814_131541002.jpg)](https://blog.cloudflare.com/author/tsmith/)

![Introducing scheduled deletion for Cloudflare Stream](https://blog.cloudflare.com/content/images/2023/08/Video-Stream-2.png)

Designed with developers in mind, Cloudflare Stream provides a seamless, integrated workflow that simplifies video streaming for creators and platforms alike. With features like [Stream Live](https://blog.cloudflare.com/stream-live-ga/) and [creator management](https://blog.cloudflare.com/stream-creator-management/), customers have been looking for ways to streamline storage management.

Today, August 11, 2023, Cloudflare Stream is introducing scheduled deletion to easily manage video lifecycles from the Stream dashboard or our API, saving time and reducing storage-related costs. Whether you need to retain recordings from a live stream for only a limited time, or preserve direct creator videos for a set duration, scheduled deletion will simplify storage management and reduce costs.

## Stream scheduled deletion

Scheduled deletion allows developers to automatically remove on-demand videos and live recordings from their library at a specified time. Live inputs can be set up with a deletion rule, ensuring that all recordings from the input will have a scheduled deletion date upon completion of the stream.

Let’s see how it works in those two configurations.

## Getting started with scheduled deletion for on-demand videos

Whether you run a learning platform where students can upload videos for review, a platform that allows gamers to share clips of their gameplay, or anything in between, scheduled deletion can help manage storage and ensure you only keep the videos that you need. Scheduled deletion can be applied to both new and existing on-demand videos, as well as recordings from completed live streams. This feature lets you specify a specific date and time at which the video will be deleted. These dates can be applied in the Cloudflare dashboard or via the Cloudflare API.

### Cloudflare dashboard

![](https://blog.cloudflare.com/content/images/2023/08/Screenshot-2023-08-11-at-12.49.57.png)

1. From the Cloudflare dashboard, select **Videos** under **Stream**
2. Select a video
3. Select **Automatically Delete Video**
4. Specify a desired date and time to delete the video
5. Click **Submit** to save the changes

### Cloudflare API

The Stream API can also be used to set the scheduled deletion property on new or existing videos. In this example, we’ll create a direct creator upload that will be deleted on December 31, 2023:

```
curl -X POST \
-H 'Authorization: Bearer <BEARER_TOKEN>' \
-d '{ "maxDurationSeconds": 10, "scheduledDeletion": "2023-12-31T12:34:56Z" }' \
https://api.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/stream/direct_upload
```

For more information on live inputs and how to configure deletion policies in our API, refer to [the documentation](https://developers.cloudflare.com/api/).

## Getting started with automated deletion for Live Input recordings

We love how recordings from live streams allow those who may have missed the stream to catch up, but these recordings aren’t always needed forever. Scheduled recording deletion is a policy that can be configured for new or existing live inputs. Once configured, the recordings of all future streams on that input will have a scheduled deletion date calculated when the recording is available. Setting this retention policy can be done from the Cloudflare dashboard or via API operations to create or edit Live Inputs:

### Cloudflare Dashboard

![](https://blog.cloudflare.com/content/images/2023/08/image3-3.png)

1. From the Cloudflare dashboard, select **Live Inputs** under **Stream**
2. Select **Create Live Input** or an existing live input
3. Select **Automatically Delete Recordings**
4. Specify a number of days after which new recordings should be deleted
5. Click **Submit** to save the rule or create the new live input

### Cloudflare API

The Stream API makes it easy to add a deletion policy to new or existing inputs. Here is an example API request to create a live input with recordings that will expire after 30 days:

```
curl -X POST \
-H 'Authorization: Bearer <BEARER_TOKEN>' \
-H 'Content-Type: application/json' \
-d '{ "recording": {"mode": "automatic"}, "deleteRecordingAfterDays": 30 }' \
https://api.staging.cloudflare.com/client/v4/accounts/<ACCOUNT_ID>/stream/live_inputs/
```

For more information on live inputs and how to configure deletion policies in our API, refer to [the documentation](https://developers.cloudflare.com/api/).

## Try out scheduled deletion today

Scheduled deletion is now available to all Cloudflare Stream customers. Try it out now and join our [Discord community](https://discord.gg/cloudflaredev) to let us know what you think! To learn more, check out our [developer docs](https://developers.cloudflare.com/stream/). Stay tuned for more exciting Cloudflare Stream updates in the future.

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

[Cloudflare Stream](https://blog.cloudflare.com/tag/cloudflare-stream/)
[Video](https://blog.cloudflare.com/tag/video/)
[Developers](https://blog.cloudflare.com/tag/developers/)
[Product News](https://blog.cloudflare.com/tag/product-news/)

Related Posts

July 30, 2021 3:00PM

[## The Cloudflare Startup Enterprise Plan: helping new startups bootstrap](https://blog.cloudflare.com/the-cloudflare-startup-enterprise-plan-helping-new-startups-bootstrap/)

To help early stage startups get going, Cloudflare is giving away one year of the Startup Enterprise plan to all early stage startups in participating accelerator programs....

By

September 30, 2021 1:59PM

[## Serverless Live Streaming with Cloudflare Stream](https://blog.cloudflare.com/stream-live/)

You can now use Cloudflare to do serverless end-to-end live-streaming. Stream Live offers video ingestion, encoding, recording and a player in a single product....

By

November 15, 2022 2:00PM

[## Get started with Cloudflare Workers with ready-made templates](https://blog.cloudflare.com/cloudflare-workers-templates/)

Today, we’re excited to share a collection of ready-made templates to help you build your next application on C...