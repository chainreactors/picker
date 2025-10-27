---
title: 继续谈自建Gravatar镜像
url: https://h4ck.org.cn/2022/11/%e7%bb%a7%e7%bb%ad%e8%b0%88%e8%87%aa%e5%bb%bagravatar%e9%95%9c%e5%83%8f/
source: obaby@mars
date: 2022-11-07
fetch_date: 2025-10-03T21:52:04.505736
---

# 继续谈自建Gravatar镜像

[![obaby@mars](/wp-content/uploads/2023/08/logo-pink-small.png)](https://h4ck.org.cn)

Artificial Intelligence / Reverse Engineering / Internet of Things / Full Stack Developer

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

 [Menu](#mobilemenu)

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

[博客相关『Blogger/WordPress』](https://h4ck.org.cn/cats/jyzj/wordp)

# 继续谈自建Gravatar镜像

2022年11月6日
[8 条评论](https://h4ck.org.cn/2022/11/10677#comments)

[![](https://image.h4ck.org.cn/wp-content/uploads/2022/11/d6ebe47cbcb4f3f37dbcd67ca7a17450.png)](https://image.h4ck.org.cn/wp-content/uploads/2022/11/d6ebe47cbcb4f3f37dbcd67ca7a17450.png)

昨天折腾了一天，到晚上的时候发了另外一篇文章《再谈自建Gravatar镜像》，里面胡一派发了一条评论。

[![](https://image.h4ck.org.cn/wp-content/uploads/2022/11/搜狗截图20221106105052.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2022/11/%E6%90%9C%E7%8B%97%E6%88%AA%E5%9B%BE20221106105052.jpg)

觉得有点意思，于是搜索了一下。根据这篇https://lingchenzi.com/2021/10/7026.html文章的方法尝试了一下：

部署成功了，但是实际访问的时候发现系统自动创建的路由small-6.gravatar.workers.dev无法访问。但是貌似在服务器直接测试是通的，后来发现通过绑定域名之后就可以访问了，于是添加了一个[g.obaby.blog](https://g.obaby.blog/) 的域名，现在这个域名可以正常使用了（这个资源是免费的，但是有服务器资源限制，欢迎大家使用）。

测试头像：

```
https://g.obaby.blog/avatar/3a78942c4ddcda86242f20abdacee082?s=50&d=mm&r=g
https://g.obaby.blog/avatar/1fbf51cf49f5c369ad2cd13d76c15c42?s=32&d=mm&r=g
https://g.obaby.blog/avatar/81b9805653d1169927583574d835691b?s=32&d=mm&r=g
```

![avatar](https://g.obaby.blog/avatar/3a78942c4ddcda86242f20abdacee082?s=80&d=mm&r=g)

服务代码（https://github.com/lingchenzi/blog/blob/main/cloudflare-workers-gravatar）：

```
// Website you intended to retrieve for users.
// 替换成你想镜像的站点
const upstream = 'www.gravatar.com'

// Custom pathname for the upstream website.
const upstream_path = '/'

// Website you intended to retrieve for users using mobile devices.
// 替换成你想镜像的站点
const upstream_mobile = 'www.gravatar.com'

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
    '$upstream': '$custom_domain'
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

        if(new_response_headers.get("x-pjax-url")) {
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

**镜像服务器地址：**

**[g.obaby.blog](https://g.obaby.blog/)**

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《继续谈自建Gravatar镜像》](https://h4ck.org.cn/2022/11/10677)
\* 本文链接：<https://h4ck.org.cn/2022/11/10677>
\* 短链接：<https://oba.by/?p=10677>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[Cloudflare](https://h4ck.org.cn/tags/cloudflare)[Cravatar](https://h4ck.org.cn/tags/cravatar)[Gravatar](https://h4ck.org.cn/tags/gravatar)[WordPress](https://h4ck.org.cn/tags/wordpress)

[Previous Post](https://h4ck.org.cn/2022/11/10683)
[Next Post](https://h4ck.org.cn/2022/11/10671)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2023年12月24日

#### [抄作业续章](https://h4ck.org.cn/2023/12/14859)

2010年12月17日

#### [Ticket #11289, IE bug fix Error](https://h4ck.org.cn/2010/12/2259)

2020年9月15日

#### [BuddyPress Theme Remove Sidebar](https://h4ck.org.cn/2020/09/7496)

### 8 comments

1. ![](h...