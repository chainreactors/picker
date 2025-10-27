---
title: 基于cloudflare worker的telegraph图床
url: https://buaq.net/go-256719.html
source: unSafe.sh - 不安全
date: 2024-08-18
fetch_date: 2025-10-06T18:02:14.536266
---

# 基于cloudflare worker的telegraph图床

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

基于cloudflare worker的telegraph图床

基于cloudflare worker的telegraph图床，支持图片压缩！项目地址：https://github.com/0-RTT/telegra
*2024-8-17 23:23:57
Author: [www.upx8.com(查看原文)](/jump-256719.htm)
阅读量:9
收藏*

---

基于cloudflare worker的telegraph图床，支持图片压缩！

项目地址：<https://github.com/0-RTT/telegraph>

⚠️需要网络能够访问telegraph

支持黏贴上传，压缩上传，无服务器部署！

复制worker.js代码，修改第二行example.com为你的自定义域名即可！

支持配置多接口，修改代码中的interfaceConfigs和getImageURL即可！ responseData返回的是接口的json内容

下载源码，将文件上传到网站目录，访问域名即可！

配置自己的反代域名 修改nginx配置

```
location /file {
            proxy_pass https://telegra.ph/file;
}
```

修改api/api.php文件第6行中的域名即可！

`docker pull baipiaoo/telegraph:latest`

`docker run -p 8080:80 -d --restart=always baipiaoo/telegraph`

复制功能由`navigator.clipboard`实现，需使用 HTTPS 协议！

```
    location / {
        proxy_pass http://localhost:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
```

文章来源: https://www.upx8.com/4286
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)