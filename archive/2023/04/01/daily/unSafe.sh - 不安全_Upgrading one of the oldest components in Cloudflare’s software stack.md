---
title: Upgrading one of the oldest components in Cloudflare’s software stack
url: https://buaq.net/go-156338.html
source: unSafe.sh - 不安全
date: 2023-04-01
fetch_date: 2025-10-04T11:19:28.076415
---

# Upgrading one of the oldest components in Cloudflare’s software stack

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

![](https://8aqnet.cdn.bcebos.com/ebaf34e2c13989f7605949a8c1c158ff.jpg)

Upgrading one of the oldest components in Cloudflare’s software stack

Loading...
*2023-3-31 21:0:0
Author: [blog.cloudflare.com(查看原文)](/jump-156338.htm)
阅读量:21
收藏*

---

Loading...

* [![Maciej Lechowski](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2023/03/picavatar.jpg)](https://blog.cloudflare.com/404/)

![Upgrading one of the oldest components in Cloudflare’s software stack](https://blog.cloudflare.com/content/images/2023/03/image4-23.png)

Cloudflare serves a huge amount of traffic: 45 million HTTP requests per second on average (as of 2023; 61 million at peak) from more than 285 cities in over 100 countries. What inevitably happens with that kind of scale is that software will be pushed to its limits. As we grew, one of the problems we faced was related to deploying our code. Sometimes, a release would be delayed because of inadequate hardware resources on our servers. Buying more and more hardware is expensive and there are limits to e.g. how much memory we can realistically have on a server. In this article, we explain how we optimised our software and its release process so that no additional resources are needed.

In order to handle traffic, each of our servers runs a set of specialised proxies. Historically, they were based on NGINX, but increasingly they [include services created in Rust](https://blog.cloudflare.com/how-we-built-pingora-the-proxy-that-connects-cloudflare-to-the-internet/). Out of our proxy applications, FL (Front Line) is the oldest and still has a broad set of responsibilities.

At its core, it’s one of the last uses of NGINX at Cloudflare. It contains a large amount of business logic that runs many Cloudflare products, using a variety of Lua and Rust libraries. As a result, it consumes a large amount of system resources: up to 50-60 GiB of RAM. As FL grew, it became more and more difficult to release it. The upgrade mechanism requires double the memory (which sometimes is not available) than at runtime. This was causing delays in releases. We have now improved the release procedure of FL, and in effect, removed the need for additional memory during the release process, improving its speed and performance.

## Architecture

To accomplish all of its work, each FL instance [runs many workers (individual processes)](https://www.nginx.com/blog/inside-nginx-how-we-designed-for-performance-scale/). By design, individual processes handle requests while the master process controls them and makes sure they stay up. This allows NGINX to handle more traffic by adding more workers. We take advantage of this architecture.

The number of workers depends on the numbers of total CPU cores present. It’s typically equal to half of the CPU cores available, e.g. on a 128-core CPU we use 64 FL workers.

### So far so good, what's the problem then?

We aim to deploy code in a way that’s transparent to our customers. We want to continue serving requests without interruptions. In practice, this means briefly running both versions of FL at the same time during the upgrade, so that we can flawlessly transition from one version to another. As soon as the new instance is up and running, we begin to shut down the old one, giving it some time to finish its work. In the end, only the new version is left running. NGINX implements this [procedure](https://nginx.org/en/docs/control.html) and FL makes use of it.

After a new version of FL is installed on a server, the upgrade procedure starts. NGINX’s implementation revolves around communicating with the master process using signals. The upgrade process starts by sending the USR2 signal which will start the new master process and its workers.

At that point, as can be seen below, both versions will be running and processing requests. The unfortunate side effect of this is the memory footprint has been doubled.

```
  PID  PPID COMMAND
33126     1 nginx: master process /usr/local/nginx/sbin/nginx
33134 33126 nginx: worker process (nginx)
33135 33126 nginx: worker process (nginx)
33136 33126 nginx: worker process (nginx)
36264 33126 nginx: master process /usr/local/nginx/sbin/nginx
36265 36264 nginx: worker process (nginx)
36266 36264 nginx: worker process (nginx)
36267 36264 nginx: worker process (nginx)
```

Then, the WINCH signal will be sent to the master process which will then ask its workers to gracefully shut down. Eventually, they will all quit, leaving just the original master process running (which can be shut down with the QUIT signal). The successful outcome of this will leave just the new instance running, which will look similar to this:

```
  PID  PPID COMMAND
36264     1 nginx: master process /usr/local/nginx/sbin/nginx
36265 36264 nginx: worker process (nginx)
36266 36264 nginx: worker process (nginx)
36267 36264 nginx: worker process (nginx)
```

The standard NGINX upgrade mechanism is visualised in this diagram:

![](https://blog.cloudflare.com/content/images/2023/03/image5-6.png)

It’s also clearly visible in the memory usage graph below (notice the large bump during the upgrade).

![](https://blog.cloudflare.com/content/images/2023/03/image1-60.png)

The mechanism outlined above has both versions running at the same time for a while. When both sets of workers are running, they are still sharing the same sockets, so all of them accept requests. As the release progresses, ‘old’ workers stop listening and accepting new requests (at that point only the new workers accept new requests). As we release new code multiple times per week, this process is effectively doubling up our memory requirements. At our scale, it’s easy to see how multiplying this event by the number of servers we operate results in an immense waste of memory resources.

In addition, sometimes servers would take hours to upgrade (a concern especially when we need to release something quickly), as we are waiting to have enough memory available to kick off the reload action.

## New upgrade mechanism

We solved this problem by modifying NGINX's method for upgrading executable. Here's how it works.

The crux of the problem is that NGINX treats the entire instance (master + workers) as one. When upgrading, we need to start all the workers whilst all the previous ones are still running. Considering the number of workers we use and how heavy they are, this is not sustainable.

So, instead, we modified NGINX to be able to control individual workers. Rather than starting and stopping them all at once, we can do so by selecting them individually. To accomplish this, the master process and workers understand additional signals compared to the ones NGINX uses. The actual mechanism to accomplish this in NGINX is nearly the same as when handling workers in bulk. However, there’s a crucial difference.

Typically, NGINX's master process ensures that the right number of workers is actually running (per configuration). If any of them crashes, it will be restarted. This is good, but it doesn't work for our new upgrade mechanism because when we need to shut down a single worker, we don't want the NGINX master process to think that a worker has crashed and needs to be restarted. So we introduced a signal to disable that behaviour in NGINX while we're shutting down a single process.

### Step by step

Our improved mechanism handles each worker individually. Here are the steps:

1. At the beginning, we have an instance of FL running 64 workers.
2. Disable the feature to automatically restart workers which exit.
3. Shut down a worker from the first (old) instance of F...