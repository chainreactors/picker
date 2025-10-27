---
title: One-API 对接 OpenRouter.ai
url: https://buaq.net/go-174294.html
source: unSafe.sh - 不安全
date: 2023-08-13
fetch_date: 2025-10-04T11:58:51.205754
---

# One-API 对接 OpenRouter.ai

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

![](https://8aqnet.cdn.bcebos.com/e8e75f3db747e721fcb5248d66328d9f.jpg)

One-API 对接 OpenRouter.ai

0.One-API: https://github.com/songquanpeng/one-apiOpenRouter: https://openrouter.ai/ 有提供 Cla
*2023-8-12 16:31:51
Author: [www.zhaoj.in(查看原文)](/jump-174294.htm)
阅读量:28
收藏*

---

0.One-API: <https://github.com/songquanpeng/one-api>

OpenRouter: <https://openrouter.ai/> 有提供 Claude 之类的接口

1.实测可以配置一下 Caddy 或者其他的反向代理比如 Nginx，让 Caddy 来反代 OpenRouter，加上那边需要的两个头：

Caddyfile

```
openrouter-api.*.com {
    tls /etc/caddy/ssl/*.com_server.crt.pem /etc/caddy/ssl/*.com_server.key.pem
    reverse_proxy https://openrouter.ai {
        header_up Host openrouter.ai
        header_up HTTP-Referer "https://oneapi.*.com"
        header_up X-Title "One API"
    }
}
```

2. 然后 One-API 这样配置即可。

![](https://www.zhaoj.in/wp-content/uploads/2023/08/1691829134fa6e4480445c46f498c52767374fa9a3-1024x747.png)

3. 实测可行。

![](https://www.zhaoj.in/wp-content/uploads/2023/08/169182916532cbeffb83ebdf093cc893ff2e5e1e32-1024x794.png)

4. 别忘了配置倍率。

![](https://www.zhaoj.in/wp-content/uploads/2023/08/169182918305e5ec37e2cc0c4dd3c8588d92d2dc87-1024x333.png)
![](https://www.zhaoj.in/wp-content/uploads/2023/08/16918291937a9ba0b8ffd7110b9f5b98f58d39028a-1024x89.png)

文章来源: https://www.zhaoj.in/read-8829.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)