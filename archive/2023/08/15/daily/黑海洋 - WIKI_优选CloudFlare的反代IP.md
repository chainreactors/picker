---
title: 优选CloudFlare的反代IP
url: https://blog.upx8.com/3777
source: 黑海洋 - WIKI
date: 2023-08-15
fetch_date: 2025-10-04T12:02:40.777698
---

# 优选CloudFlare的反代IP

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 优选CloudFlare的反代IP

发布时间:
2023-08-14

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
32704

在目前，由于优选 CF 的 IP 已被越来越多人滥用，导致某国防火墙已经开始重点关照。这时候我们就得找一些官方未公开的 IP 进行优选。不过，有些 IP 应该是为了某些服务，把自己反代到 CF 的服务器上，所以说我们得到了反代的 CF 的 IP 地址。幸运的是，经过某大佬的扫描和整理，我们可以得到了一些反代了 CF 的 IP 地址列表。这篇文章中我来和大家一起来教大家如何优选 CF 的反代 IP。

## 准备材料

* CloudFlareST 优选程序
* CF 的反代 IP

## 注意事项

请勿滥用！

## 优选步骤

1. 打开 [https://zip.baipiao.eu.org](https://blog.upx8.com/go/aHR0cHM6Ly96aXAuYmFpcGlhby5ldS5vcmcv) ，下载大佬每日更新的反代 CF 的 IP 列表

[![](https://cdn.jsdelivr.net/gh/Misaka-blog/imgs@main/20230801113749.png)](https://cdn.jsdelivr.net/gh/Misaka-blog/imgs%40main/20230801113749.png)

2. 在这里可以看到有根据 IP 的 ASN 和地区来排列的列表 txt 文件

[![](https://cdn.jsdelivr.net/gh/Misaka-blog/imgs@main/20230801113848.png)](https://cdn.jsdelivr.net/gh/Misaka-blog/imgs%40main/20230801113848.png)

> 文件名格式：`ASN(或地区)-0/1-端口号.txt`

3. 将反代 CF 的 IP 覆盖 CloudFlareST 优选程序的 `ip.txt` 文件中。注意不要留空行

[![](https://cdn.jsdelivr.net/gh/Misaka-blog/imgs@main/20230801114050.png)](https://cdn.jsdelivr.net/gh/Misaka-blog/imgs%40main/20230801114050.png)

4. 在优选程序的目录下，打开命令行。然后使用以下命令进行优选SHELL

> .\CloudflareST.exe -tp 端口 -url https://hkcs.cloudflarest.link -sl 3 -tl 200 -dn 5
>
> 可以根据自己的实际需要，修改运行命令的参数（详情可看 CloudFlareST 项目的 README）

5. 稍等片刻，可以看到优选程序此时已经优选出速度优质的反代 CF 的 IP 了。

[![](https://cdn.jsdelivr.net/gh/Misaka-blog/imgs@main/20230801114836.png)](https://cdn.jsdelivr.net/gh/Misaka-blog/imgs%40main/20230801114836.png)

[取消回复](https://blog.upx8.com/3777#respond-post-3777)

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