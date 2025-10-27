---
title: PHP邮件自定义发送API接口带多种邮件模板
url: https://blog.upx8.com/3141
source: 黑海洋 - WIKI
date: 2022-12-11
fetch_date: 2025-10-04T01:12:33.610099
---

# PHP邮件自定义发送API接口带多种邮件模板

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# PHP邮件自定义发送API接口带多种邮件模板

发布时间:
2022-12-10

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
10499

可以用于对接不支持邮件推送的系统如”哪吒探针“，使其能够发送邮件告警，也可以用做其他用途，附带多种邮件模板请自行参照源码的注释修改。

### 安装

需要 PHP > 7.2，上传至你网站目录的任意位置，根据注释修改成你邮箱服务商的 SMTP 信息即可使用。

![](//imgsrc.baidu.com/imgad/pic/item/d21b0ef41bd5ad6e12e89229c4cb39dbb7fd3ce4.jpg)

### 请求示例

```
https://你的域名/mail-api/?address=收件邮箱&nickname=发件人昵称&title=邮件标题&content=邮件内容
```

### 邮件模板

参照`邮件模板使用示例`自行修改，然后替换到 `<<<EOF` 和 `EOF` 之间即可，当然这些邮件模板你也可以用到其他系统中，比如 `WordPess`。下面是一些模板的展示图：

![](//imgsrc.baidu.com/imgad/pic/item/738da9773912b31bb27e3beac318367adbb4e1e7.jpg)

### 下载地址：[https://github.com/Fog-Forest/scripts/tree/main/mail-api](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL0ZvZy1Gb3Jlc3Qvc2NyaXB0cy90cmVlL21haW4vbWFpbC1hcGk)

### 参考：[PHPMailer](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL1BIUE1haWxlci9QSFBNYWlsZXI)

[取消回复](https://blog.upx8.com/3141#respond-post-3141)

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