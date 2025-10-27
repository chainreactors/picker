---
title: How Oxy uses hooks for maximum extensibility
url: https://buaq.net/go-165934.html
source: unSafe.sh - 不安全
date: 2023-05-27
fetch_date: 2025-10-04T11:37:12.238938
---

# How Oxy uses hooks for maximum extensibility

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

![](https://8aqnet.cdn.bcebos.com/86cdf23bac0c4fe136db8c32a909f7d5.jpg)

How Oxy uses hooks for maximum extensibility

Loading...
*2023-5-26 21:0:17
Author: [blog.cloudflare.com(查看原文)](/jump-165934.htm)
阅读量:27
收藏*

---

Loading...

* [![Will Bartlett](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2023/05/me.jpg)](https://blog.cloudflare.com/author/wbartlett/)
* [![Fisher Darling](https://blog.cloudflare.com/cdn-cgi/image/width=62,height=62/http://blog.cloudflare.com/content/images/2023/05/IMG_0873-copy-1.jpg)](https://blog.cloudflare.com/author/fisher/)

![How Oxy uses hooks for maximum extensibility](https://blog.cloudflare.com/content/images/2023/05/image4-2-1.png)

We recently [introduced Oxy](https://blog.cloudflare.com/introducing-oxy/), our Rust framework for building proxies. Through a YAML file, Oxy allows applications to easily configure listeners (e.g. IP, [MASQUE](https://blog.cloudflare.com/unlocking-quic-proxying-potential/), HTTP/1), telemetry, and much more. However, when it comes to application logic, a programming language is often a better tool for the job. That’s why in this post we’re introducing Oxy’s rich [dependency injection](https://en.wikipedia.org/wiki/Dependency_injection) capabilities for programmatically modifying all aspects of a proxy.

The idea of extending proxies with scripting is well established: we've had great past success with [Lua in our OpenResty/NGINX deployments](https://blog.cloudflare.com/pushing-nginx-to-its-limit-with-lua/) and there are numerous web frameworks (e.g. [Express](https://expressjs.com/en/guide/using-middleware.html)) with middleware patterns. While Oxy is geared towards the development of [forward proxies](https://www.cloudflare.com/learning/cdn/glossary/reverse-proxy/), they all share the model of a pre-existing request pipeline with a mechanism for integrating custom application logic. However, the use of Rust greatly helps developer productivity when compared to embedded scripting languages. Having confidence in the types and mutability of objects being passed to and returned from callbacks is wonderful.

Oxy exports a series of hook traits that “hook” into the lifecycle of a *connection*, not just a request. Oxy applications need to control almost every layer of the [OSI model](https://www.cloudflare.com/en-gb/learning/ddos/glossary/open-systems-interconnection-model-osi/): how packets are received and sent, what tunneling protocols they could be using, what HTTP version they are using (if any), and even how DNS resolution is performed. With these hooks you can extend Oxy in any way possible in a safe and performant way.

First, let's take a look from the perspective of an Oxy application developer, and then we can discuss the implementation of the framework and some of the interesting design decisions we made.

## Adding functionality with hooks

Oxy’s dependency injection is a barebones version of what Java or C# developers might be accustomed to. Applications simply implement the start method and return a struct with their hook implementations:

```
async fn start(
    _settings: ServerSettings<(), ()>,
    _parent_state: Metadata,
) -> anyhow::Result<Hooks<Self>> {
    Ok(Hooks {
        ..Default::default()
    })
}
```

We can define a simple callback, `EgressHook::handle_connection`, that will forward all connections to the upstream requested by the client. Oxy calls this function before attempting to make an upstream connection.

```
#[async_trait]
impl<Ext> EgressHook<Ext> for MyEgressHook
where
    Ext: OxyExt,
{
    async fn handle_connection(
        &self,
        upstream_addr: SocketAddr,
        _egress_ctx: EgressConnectionContext<Ext>,
    ) -> ProxyResult<EgressDecision> {
        Ok(EgressDecision::ExternalDirect(upstream_addr))
    }
}

async fn start(
    _settings: ServerSettings<(), ()>,
    _parent_state: Metadata,
) -> anyhow::Result<Hooks<Self>> {
    Ok(Hooks {
        egress: Some(Arc::new(MyEgressHook)),
        ..Default::default()
    })
}
```

Oxy simply proxies the connection, but we might want to consider restricting which upstream IPs our clients are allowed to connect to. The implementation above allows everything, but maybe we have internal services that we wish to prevent proxy users from accessing.

```
#[async_trait]
impl<Ext> EgressHook<Ext> for MyEgressHook
where
    Ext: OxyExt,
{
    async fn handle_connection(
        &self,
        upstream_addr: SocketAddr,
        _egress_ctx: EgressConnectionContext<Ext>,
    ) -> ProxyResult<EgressDecision> {
        if self.private_cidrs.find(upstream_addr).is_some() {
            return Ok(EgressDecision::Block);
        }

        Ok(EgressDecision::ExternalDirect(upstream_addr))
    }
}
```

This blocking strategy is crude. Sometimes it’s useful to allow certain clients to connect to internal services – a [Prometheus](https://prometheus.io/docs/introduction/overview/) scraper is a good example. To authorize these connections, we’ll implement a simple Pre-Shared Key (PSK) authorization scheme – if the client sends the header `Proxy-Authorization: Preshared oxy-is-a-proxy`, then we’ll let them connect to private addresses via the proxy.

To do this, we need to attach some state to the connection as it passes through Oxy. Client headers only exist in the HTTP CONNECT phase, but we need access to the PSK during the egress phase. With Oxy, this can be done by leveraging its Opaque Extensions to attach arbitrary (yet fully typed) context data to a connection. Oxy initializes the data and passes it to each hook. We can mutate this data when we read headers from the client, and read it later during egress.

![](https://blog.cloudflare.com/content/images/2023/05/download-18.png)

```
#[derive(Default)]
struct AuthorizationResult {
    can_access_private_cidrs: Arc<AtomicBool>,
}

#[async_trait]
impl<Ext> HttpRequestHook<Ext> for MyHttpHook
where
    Ext: OxyExt<IngressConnectionContext = AuthorizationResult>,
{
    async fn handle_proxy_connect_request(
        self: Arc<Self>,
        connect_req_head: &Parts,
        req_ctx: RequestContext<Ext>,
    ) -> ConnectDirective {
        const PSK_HEADER: &str = "Preshared oxy-is-a-proxy";

        // Grab the authorization header and update
        // the ingress_ctx if the preshared key matches.
        if let Some(authorization_header) =
          connect_req_head.headers.get("Proxy-Authorization") {
            if authorization_header.to_str().unwrap() == PSK_HEADER {
                req_ctx
                    .ingress_ctx()
                    .ext()
                    .can_access_private_cidrs
                    .store(true, Ordering::SeqCst);
            }
        }

        ConnectDirective::Allow
    }
}
```

From here, any hook in the pipeline can access this data. For our purposes, we can just update our existing `handle_connection` callback:

```
#[async_trait]
impl<Ext> EgressHook<Ext> for MyEgressHook
where
    Ext: OxyExt<IngressConnectionContext = AuthorizationResult>,
{
    async fn handle_connection(
        &self,
        upstream_addr: SocketAddr,
        egress_ctx: EgressConnectionContext<Ext>,
    ) -> ProxyResult<EgressDecision> {
        if self.private_cidrs.find(upstream_addr).is_some() {
            if !egress_ctx
                .ingress_ctx()
                .ext()
                .can_access_private_cidrs
                .load(Ordering::SeqCst)
            {
                return Ok(EgressDecision::Block);
            }
        }

        Ok(EgressDecision::ExternalDirect(upstream_addr))
    }
}
```

This is a somewhat cont...