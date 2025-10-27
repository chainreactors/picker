---
title: 宝塔面板+Fail2Ban+Cloudflare：实战CC攻击防护指南
url: https://blog.upx8.com/4805
source: 黑海洋 - Wiki
date: 2025-05-21
fetch_date: 2025-10-06T22:27:39.463069
---

# 宝塔面板+Fail2Ban+Cloudflare：实战CC攻击防护指南

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 宝塔面板+Fail2Ban+Cloudflare：实战CC攻击防护指南

发布时间:
2025-05-20

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
60506

### 1. 注册 Cloudflare 帐户并获取全局 API 密钥

首先，你需要注册 Cloudflare 帐户（如果还没有），然后获取全局 API 密钥。按照以下步骤进行：

1. 访问 Cloudflare 官网 [https://www.cloudflare.com/](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuY2xvdWRmbGFyZS5jb20v)，点击 “Sign Up” 进行注册。
2. 注册成功后，在 Cloudflare 控制面板中，转到 "My Profile" 页面。
3. 在 "API Tokens" 部分，点击 "Create Token"。
4. 在 "Create Token" 页面，选择 "Use Cloudflare APIs" 权限，并为该令牌分配名称。
5. 点击 "Continue" 并完成创建，然后复制生成的全局 API 密钥。
   [一键直达](https://blog.upx8.com/go/aHR0cHM6Ly9kYXNoLmNsb3VkZmxhcmUuY29tL3Byb2ZpbGUvYXBpLXRva2Vucw "一键直达")

   ### 2. 安装 aaPanel

确保你的服务器已经安装了 aaPanel。如果还没有安装，可以按照以下步骤进行：

1. 登录到服务器，打开 SSH 终端。
2. 下载并执行 aaPanel 安装脚本：

```
URL=https://www.aapanel.com/script/install_6.0_en.sh && if [ -f /usr/bin/curl ];then curl -ksSO "$URL" ;else wget --no-check-certificate -O install_6.0_en.sh "$URL";fi;bash install_6.0_en.sh aapanel
```

3. 按照安装向导的提示完成安装过程。

### 3. 安装 Fail2Ban

一旦 aaPanel 安装完成，接下来安装 Fail2Ban。你可以通过 aaPanel 的软件商店进行安装：

1. 登录 aaPanel 控制面板。
2. 在左侧菜单中找到并点击 "软件商店"。
3. 在搜索框中输入 "Fail2Ban"，然后点击搜索结果中的 "安装" 按钮进行安装。

### 4. 配置 Fail2Ban

配置 Fail2Ban 以开始保护你的服务器。你可以在 aaPanel 的 Fail2Ban 插件中进行配置：

在 aaPanel 控制面板中，找到并点击 "Fail2Ban"。输入你的邮箱和你的 api

![](https://cdn.skyimg.net/up/2025/5/20/c6755515.webp)

随便便建一个网站规则 建好之后去
`/etc/fail2ban/filter.d/aaP_你的域名_cc.conf` 配置修改为

```
[Definition]
failregex = ^<HOST> .* "(GET|POST|HEAD).*HTTP.*" (404|503) .*$
# failregex = ^<HOST> .* "(GET|POST|HEAD).*HTTP.*" (404|503|444) .*
ignoreregex =.*(robots.txt|favicon.ico|jpg|png)
```

![](https://cdn.skyimg.net/up/2025/5/20/1f8aae21.webp)

在 Fail2Ban 插件中，你可以设置监控的日志文件、定义触发阻止的规则、设置封禁时长等。确保你的设置适合你的服务器需求，并确保包含常见的防御规则。

### 5. 让 Nginx 识别 Cloudflare 的 IP 地址

在你的 Nginx 配置文件中添加以下内容，以允许 Nginx 识别 Cloudflare 的 IP 地址：

![](https://cdn.skyimg.net/up/2025/5/20/f2b19704.webp)

```
set_real_ip_from 103.21.244.0/22;
set_real_ip_from 103.22.200.0/22;
set_real_ip_from 103.31.4.0/22;
set_real_ip_from 104.16.0.0/12;
set_real_ip_from 108.162.192.0/18;
set_real_ip_from 131.0.72.0/22;
set_real_ip_from 141.101.64.0/18;
set_real_ip_from 162.158.0.0/15;
set_real_ip_from 172.64.0.0/13;
set_real_ip_from 173.245.48.0/20;
set_real_ip_from 188.114.96.0/20;
set_real_ip_from 190.93.240.0/20;
set_real_ip_from 197.234.240.0/22;
set_real_ip_from 198.41.128.0/17;
set_real_ip_from 199.27.128.0/21;
set_real_ip_from 2400:cb00::/32;
set_real_ip_from 2606:4700::/32;
set_real_ip_from 2803:f800::/32;
set_real_ip_from 2405:b500::/32;
set_real_ip_from 2405:8100::/32;
set_real_ip_from 2a06:98c0::/29;
set_real_ip_from 2c0f:f248::/32;

real_ip_header CF-Connecting-IP;
```

### 6. 让 Apache 识别 Cloudflare 的 IP 地址

在你的 Apache 配置文件中添加以下内容，以允许 Apache 识别 Cloudflare 的 IP 地址：

```
set_real_ip_from 103.21.244.0/22;
set_real_ip_from 103.22.200.0/22;
set_real_ip_from 103.31.4.0/22;
set_real_ip_from 104.16.0.0/12;
set_real_ip_from 108.162.192.0/18;
set_real_ip_from 131.0.72.0/22;
set_real_ip_from 141.101.64.0/18;
set_real_ip_from 162.158.0.0/15;
set_real_ip_from 172.64.0.0/13;
set_real_ip_from 173.245.48.0/20;
set_real_ip_from 188.114.96.0/20;
set_real_ip_from 190.93.240.0/20;
set_real_ip_from 197.234.240.0/22;
set_real_ip_from 198.41.128.0/17;
set_real_ip_from 199.27.128.0/21;
set_real_ip_from 2400:cb00::/32;
set_real_ip_from 2606:4700::/32;
set_real_ip_from 2803:f800::/32;
set_real_ip_from 2405:b500::/32;
set_real_ip_from 2405:8100::/32;
set_real_ip_from 2a06:98c0::/29;
set_real_ip_from 2c0f:f248::/32;

RemoteIPHeader CF-Connecting-IP
```

### 8. 测试

完成以上步骤后，你的服务器应该能够识别 Cloudflare 的 IP 地址了。你可以通过访问你的网站，并查看 Nginx 和 Apache 的访问日志来验证 IP 地址是否已被正确识别。

### 9. 最佳实践和注意事项

为了最大程度地提高服务器安全性，以下是一些使用 Fail2Ban 的最佳实践和注意事项：

* 定期更新 Fail2Ban 的规则和软件版本以确保最新的安全性。
* 避免封禁自己的 IP 地址。在设置 Fail2Ban 规则时，确保你的 IP 地址不会被错误地封禁。
* 审查封禁的 IP 地址列表，定期清理不再需要封禁的地址。

### 结语

通过在 aaPanel 上配置 Fail2Ban，并让 Nginx 和 Apache 识别 Cloudflare 的 IP 地址，并使用 Cloudflare 的全局 API，你可以有效地保护你的服务器免受恶意攻击的威胁。利用这些简单而强大的工具，加固你的服务器安全，让你的在线业务更加安全可靠。

[取消回复](https://blog.upx8.com/4805#respond-post-4805)

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