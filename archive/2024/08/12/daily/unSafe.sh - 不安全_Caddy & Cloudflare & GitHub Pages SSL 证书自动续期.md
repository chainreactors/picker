---
title: Caddy & Cloudflare & GitHub Pages SSL 证书自动续期
url: https://buaq.net/go-255435.html
source: unSafe.sh - 不安全
date: 2024-08-12
fetch_date: 2025-10-06T18:01:27.693155
---

# Caddy & Cloudflare & GitHub Pages SSL 证书自动续期

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

![](https://8aqnet.cdn.bcebos.com/24453a0459adf876e847422bb4cd9df8.jpg)

Caddy & Cloudflare & GitHub Pages SSL 证书自动续期

*2024-8-11 21:33:37
Author: [programlife.net(查看原文)](/jump-255435.htm)
阅读量:22
收藏*

---

* [Categories](https://programlife.net/categories/)
* [Archives](https://programlife.net/archives/)
* [Tags](https://programlife.net/tags/)
* [About](https://programlife.net/about/)
* [Sitemap](https://programlife.net/sitemap.xml)

Posted on

2024-08-11

|

In

[Default](https://programlife.net/categories/Default/)

想给网站套个免费的 Cloudflare CDN，如何让 Caddy 和 GitHub Pages 各自自动续期 SSL 证书？

## 0x01. 预期效果

本文想要达到的预期效果如下：

* 主域名（Blog）
  + 绑定 GitHub Pages 服务，SSL 证书由 GitHub 负责管理（由 Let’s Encrypt 签发）
  + Cloudflare 仅负责 DNS 解析，不提供 CDN 服务
* 其他二级域名
  + Caddy 负责为二级域名提供 SSL 证书申请和续期（由 Let’s Encrypt 签发）
  + Cloudflare 负责 DNS 解析，同时提供 CDN 服务

注意，套上 CDN 之后，Cloudflare 给网站绑定的 SSL 证书是由 Google Trust Services 颁发的，这跟 Caddy 向 Let’s Encrypt 申请的 SSL 证书不是同一个，这也是**套上 CDN 之后，Caddy 在默认情况下无法自动给证书续期**的原因。

![Cloudflare CDN SSL 证书由 Google Trust Services 颁发](https://programlife.net/uploads/202408/google-trust-services-ssl-certificate.webp)

## 0x02. GitHub Pages 设置

域名（如主域名以及 `www`）绑定 GitHub Pages 之后，SSL 证书是由 GitHub 来管理的，所以在 Cloudflare 设置 DNS 时，只能设置为 `DNS only`，不能设置为 `Proxied`，否则 GitHub 就无法正常去检测我们的 SSL 证书的状态，证书自动续期就更是不可能的事情了。

## 0x03. Cloudflare 设置

除了绑定到 GitHub Pages 的域名之外，剩下的域名如果需要使用 Cloudflare 提供的 CDN 服务，那么在 DNS 设置中选定 `Proxied`。同时，还需要将 SSL/TLS encryption mode 设置为 `Full (strict)`，除了解决浏览器提示 `ERR_TOO_MANY_REDIRECTS`（**重定向次数过多**）错误问题之外，`strict` 模式还提供端到端加密以及严格的证书校验机制。

![Cloudflare SSL/TLS encryption mode](https://programlife.net/uploads/202408/cloudflare-ssl-encryption-mode.webp)

## 0x04. Caddy 设置

前面提到过，在给二级域名套上 Cloudflare 的 CDN 之后，浏览器访问域名时，看到的 SSL 证书是由 Google Trust Services 颁发的，而 Caddy 则是向 Let’s Encrypt 申请 SSL 证书，所以默认情况下，Caddy 无法正常检测我们的 SSL 证书的状态（类似 GitHub Pages）。

### 4.1 替换 Caddy

1. 从 <https://caddyserver.com/download> 下载一个带 `dns.providers.cloudflare` 插件的 Caddy（注意勾选正确的操作系统）
2. 给下载下来的 Caddy 添加执行权限，并替换服务器上原有的 Caddy（可以先做一个备份）
3. 给 Caddyfile 添加配置（可以是全局配置，也可以是针对单个域名的配置）

全局配置：直接在文件头部添加

```
{
    acme_dns cloudflare Cloudflare_API_Token
}
```

针对单个域名的配置：在域名配置下添加

```
tls {
    dns cloudflare Cloudflare_API_Token
}
```

### 4.2 创建 Cloudflare API Token

打开 [https://dash.cloudflare.com/profile/api-tokens，选择](https://dash.cloudflare.com/profile/api-tokens%EF%BC%8C%E9%80%89%E6%8B%A9) Create Token，选择 Edit zone DNS 模板，增加如下两个权限：

| api\_token\_resources | api\_token\_permissions | api\_token\_permissions\_options |
| --- | --- | --- |
| Zone | DNS | Edit |
| Zone | DNS | Read |

其他选项使用默认设置，即可创建 Cloudflare API Token，注意这个 Token 只会显示一次，之后不会再显示。

### 4.3 测试 Caddy

执行如下命令，可以查看 Caddy 运行时的日志，包括那些域名的 SSL 证书会被自动续期，以及 SSL 证书的申请状态等。

```
service caddy stop
caddy run --config /etc/caddy/Caddyfile
```

注意，绑定在 GitHub Pages 上的域名，不会被 Caddy 管理（因为在 Caddyfile 里面是没有也不能配置这个域名的）。

## 0x05. References

1. <https://acytoo.com/ladder/set-caddy-cloudflare-cdn/>

文章来源: https://programlife.net/2024/08/11/caddy-cloudflare-github-pages-ssl-certificates-renewal/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)