---
title: One-API 对接 MiniMax
url: https://buaq.net/go-174298.html
source: unSafe.sh - 不安全
date: 2023-08-13
fetch_date: 2025-10-04T11:58:50.573745
---

# One-API 对接 MiniMax

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

![](https://8aqnet.cdn.bcebos.com/34d29b8bd23c10b3230e48df581853fb.jpg)

One-API 对接 MiniMax

0.One-API: https://github.com/songquanpeng/one-apiMiniMax: https://api.minimax.chat/ 转发器
*2023-8-12 19:47:31
Author: [www.zhaoj.in(查看原文)](/jump-174298.htm)
阅读量:37
收藏*

---

0.One-API: <https://github.com/songquanpeng/one-api>

MiniMax: <https://api.minimax.chat/>

转发器源码：<https://github.com/glzjin/ChatProxy-MiniMax>

1.在自己的机器上用 Docker 进行部署。

```
docker run -p 127.0.0.1:3004:8000 --name minimax-proxy -d glzjin/chatproxy-minimax
```

2. 可以设置反代。（可选）

参考 Caddyfile 内容：

```
minimax-api.*.com {
    tls /etc/caddy/ssl/*.com_server.crt.pem /etc/caddy/ssl/*.com_server.key.pem
    reverse_proxy http://127.0.0.1:3004 {
        header_up Host minimax-api.*.com
    }
}
```

3.在 [One API](https://github.com/songquanpeng/one-api) 中进行渠道设置。

![](https://www.zhaoj.in/wp-content/uploads/2023/08/169184074771753052532b40c188975c941b293cb1-1024x718.png)

注意密钥由两部分组成，API Key 在前, Group ID 在后，中间竖线分割。

模型说明：

* “abab5-chat”: abab5-chat模型
* “abab5.5-chat”: abab5.5-chat模型
* “abab5.5-chat-pro”: abab5.5-chat，但走 pro 接口调用 <https://api.minimax.chat/document/guides/chat-pro?id=64b79fa3e74cddc5215939f4>，可以进行函数调用。

4.设置倍率。

![](https://www.zhaoj.in/wp-content/uploads/2023/08/1691840780774a0541a05cf62a8b697d4d64ceab9f.png)

5.Enjoy it.

![](https://www.zhaoj.in/wp-content/uploads/2023/08/16918407968a111b73ab2aeb3878ce91d7f5eb1ffd-1024x459.png)
![](https://www.zhaoj.in/wp-content/uploads/2023/08/169184080150f9595eacc24b0cec8087cdd9bda495-1024x223.png)

文章来源: https://www.zhaoj.in/read-8839.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)