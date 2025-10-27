---
title: CloudFlare Workers 反代任意网站和挂载单页代码
url: https://blog.upx8.com/3219
source: 黑海洋 - WIKI
date: 2023-02-12
fetch_date: 2025-10-04T06:26:11.077103
---

# CloudFlare Workers 反代任意网站和挂载单页代码

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# CloudFlare Workers 反代任意网站和挂载单页代码

发布时间:
2023-02-11

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
15202

## ![](https://img.imgdd.com/f210f3.e7bc4833-d1f7-45d7-b3c2-ac55a5de1799.png)

## 介绍

`CloudFlare Workers`是一个支持`jsproxy`的无服务器函数服务，提供全球`CDN`支持，免费用户有每天`10万`请求额度；
`CloudFlare`官网：[https://dash.cloudflare.com](https://blog.upx8.com/go/aHR0cHM6Ly9kYXNoLmNsb3VkZmxhcmUuY29tLw)
**记录下一些简单的使用方法，以后再陆续更新；**

## Workers 单页挂载代码

```
addEventListener('fetch', event => {
  event.respondWith(handleRequest(event.request))
})

// HTML代码
let html = `
<!DOCTYPE html>
<html>
  <head><title>Test</title></head>
  <body><div>Hello world!</div></body>
</html>
`;

/**
 * Respond to the request
 * @param {Request} request
 */
async function handleRequest(request) {
  return new Response(html, {
    headers: {
      'Content-Type': 'text/html; charset=UTF-8'
    },
    status: 200
  })
}
```

## Workers 反代任意网站

替换掉其中的`blog.upx8.com`为你需要反代的网址即可；

```
// Website you intended to retrieve for users.
const upstream = 'blog.upx8.com'

// Custom pathname for the upstream website.
const upstream_path = '/'

// Website you intended to retrieve for users using mobile devices.
const upstream_mobile = 'blog.upx8.com'

// Countries and regions where you wish to suspend your service.
const blocked_region = ['KP', 'SY', 'PK', 'CU']

// IP addresses which you wish to block from using your service.
const blocked_ip_address = ['0.0.0.0', '127.0.0.1']

// Whether to use HTTPS protocol for upstream address.
const https = true

// Whether to disable cache.
const disable_cache = false

// Replace texts.
const replace_dict = {
    '$upstream': '$custom_domain',
    '//blog.upx8.com': ''
}

addEventListener('fetch', event => {
    event.respondWith(fetchAndApply(event.request));
})

async function fetchAndApply(request) {
    const region = request.headers.get('cf-ipcountry').toUpperCase();
    const ip_address = request.headers.get('cf-connecting-ip');
    const user_agent = request.headers.get('user-agent');

    let response = null;
    let url = new URL(request.url);
    let url_hostname = url.hostname;

    if (https == true) {
        url.protocol = 'https:';
    } else {
        url.protocol = 'http:';
    }

    if (await device_status(user_agent)) {
        var upstream_domain = upstream;
    } else {
        var upstream_domain = upstream_mobile;
    }

    url.host = upstream_domain;
    if (url.pathname == '/') {
        url.pathname = upstream_path;
    } else {
        url.pathname = upstream_path + url.pathname;
    }

    if (blocked_region.includes(region)) {
        response = new Response('Access denied: WorkersProxy is not available in your region yet.', {
            status: 403
        });
    } else if (blocked_ip_address.includes(ip_address)) {
        response = new Response('Access denied: Your IP address is blocked by WorkersProxy.', {
            status: 403
        });
    } else {
        let method = request.method;
        let request_headers = request.headers;
        let new_request_headers = new Headers(request_headers);

        new_request_headers.set('Host', upstream_domain);
        new_request_headers.set('Referer', url.protocol + '//' + url_hostname);

        let original_response = await fetch(url.href, {
            method: method,
            headers: new_request_headers
        })

        connection_upgrade = new_request_headers.get("Upgrade");
        if (connection_upgrade && connection_upgrade.toLowerCase() == "websocket") {
            return original_response;
        }

        let original_response_clone = original_response.clone();
        let original_text = null;
        let response_headers = original_response.headers;
        let new_response_headers = new Headers(response_headers);
        let status = original_response.status;

        if (disable_cache) {
            new_response_headers.set('Cache-Control', 'no-store');
        }

        new_response_headers.set('access-control-allow-origin', '*');
        new_response_headers.set('access-control-allow-credentials', true);
        new_response_headers.delete('content-security-policy');
        new_response_headers.delete('content-security-policy-report-only');
        new_response_headers.delete('clear-site-data');

        if (new_response_headers.get("x-pjax-url")) {
            new_response_headers.set("x-pjax-url", response_headers.get("x-pjax-url").replace("//" + upstream_domain, "//" + url_hostname));
        }

        const content_type = new_response_headers.get('content-type');
        if (content_type != null && content_type.includes('text/html') && content_type.includes('UTF-8')) {
            original_text = await replace_response_text(original_response_clone, upstream_domain, url_hostname);
        } else {
            original_text = original_response_clone.body
        }

        response = new Response(original_text, {
            status,
            headers: new_response_headers
        })
    }
    return response;
}

async function replace_response_text(response, upstream_domain, host_name) {
    let text = await response.text()

    var i, j;
    for (i in replace_dict) {
        j = replace_dict[i]
        if (i == '$upstream') {
            i = upstream_domain
        } else if (i == '$custom_domain') {
            i = host_name
        }

        if (j == '$upstream') {
            j = upstream_domain
        } else if (j == '$custom_domain') {
            j = host_name
        }

        let re = new RegExp(i, 'g')
        text = text.replace(re, j);
    }
    return text;
}

async function device_status(user_agent_info) {
    var agents = ["Android", "iPhone", "SymbianOS", "Windows Phone", "iPad", "iPod"];
    var flag = true;
    for (var v = 0; v < agents.length; v++) {
        if (user_agent_info.indexOf(agents[v]) > 0) {
            flag = false;
            break;
        }
    }
    return flag;
}
```

[取消回复](https://blog.upx8.com/3219#respond-post-3219)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2024 黑海洋. All rights reserved.
[看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号") [Sitemap](sitemap.xml?type=index "Sitemap")