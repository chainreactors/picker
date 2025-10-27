---
title: 亚马逊云Amazon CloudFront（内容分发网络CDN）免费1TB数据加速教程
url: https://blog.upx8.com/3204
source: 黑海洋 - WIKI
date: 2023-01-30
fetch_date: 2025-10-04T05:10:38.156376
---

# 亚马逊云Amazon CloudFront（内容分发网络CDN）免费1TB数据加速教程

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 亚马逊云Amazon CloudFront（内容分发网络CDN）免费1TB数据加速教程

发布时间:
2023-01-29

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
20119

Amazon CloudFront，是一项快速内容分发网络(CDN)服务，能够以低延迟和高传输速度安全地向全球客户分发数据、视频、应用程序和API。比如我们可以用于网站、S3对象存储的加速，默认CloudFront每个账户拥有每月1TB数据流量。而且，CloudFront网络拥有超过225个节点(PoP)，这些节点通过完全冗余的并行100GbE光纤进行连接，可为终端用户提供超低延迟的性能和高可用性。在提供缓存或动态内容时，CloudFront会自动映射网络状况并智能地路由用户的流量。

![亚马逊云免费CDN开通教程_Amazon CloudFront（内容分发网络CDN）免费1TB数据开通网站加速应用](https://www.laoliublog.cn/wp-content/uploads/2023/01/cloudfront-1.png)

比如我们常用的是给网站或者对象存储S3加速，当然还有负载均衡和一些API调用应用。

![亚马逊云免费CDN开通教程_Amazon CloudFront（内容分发网络CDN）免费1TB数据开通网站加速应用](https://www.laoliublog.cn/wp-content/uploads/2023/01/cloudfront-2.png)

这里我们可以根据提示选择已经创建的源，比如AWS S3或者是输入域名。记住，这个域名不是我们直接加速CDN的域名，而是要指向解析到服务器IP的域名，算是一个跳板。我们需要将这个域名解析到当前的服务器IP。

![亚马逊云免费CDN开通教程_Amazon CloudFront（内容分发网络CDN）免费1TB数据开通网站加速应用](https://www.laoliublog.cn/wp-content/uploads/2023/01/cloudfront-3.png)

输入域名，默认默认检测是否支持HTTP和HTTPS。

![亚马逊云免费CDN开通教程_Amazon CloudFront（内容分发网络CDN）免费1TB数据开通网站加速应用](https://www.laoliublog.cn/wp-content/uploads/2023/01/cloudfront-4.png)

然后我们需要设置缓存行为，包括自动压缩对象、查看器策略，以及允许的HTTP方法，默认也有提供缓存请求策略。

![亚马逊云免费CDN开通教程_Amazon CloudFront（内容分发网络CDN）免费1TB数据开通网站加速应用](https://www.laoliublog.cn/wp-content/uploads/2023/01/cloudfront-5.png)

这里根据我们的项目业务选择节点，默认建议是所有节点。如果有开通WAF安全的也可以选择策略启动，同时如果我们用的HTTPS，也可以选择关联证书。

这里需要注意的是，那我们如何绑定自己的真需要CDN的域名呢？

[![亚马逊云免费CDN开通教程_Amazon CloudFront（内容分发网络CDN）免费1TB数据开通网站加速应用](https://www.laoliublog.cn/wp-content/uploads/2023/01/cloudfront-6.png)](https://www.laoliublog.cn/wp-content/uploads/2023/01/cloudfront-6.png)

在备用域名这里填写的是我们真需要CDN的域名。但是你真添加保存是不可以的，会提示错误。

> To add an alternate domain name (CNAME) to a CloudFront distribution, you must attach a trusted certificate that validates your authorization to use the domain name. For more details, see: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/CNAMEs.html#alternate-domain-names-requirements

我需要到自定义SSL证书中验证域名所有权。

[![亚马逊云免费CDN开通教程_Amazon CloudFront（内容分发网络CDN）免费1TB数据开通网站加速应用](https://www.laoliublog.cn/wp-content/uploads/2023/01/cloudfront-7.png)](https://www.laoliublog.cn/wp-content/uploads/2023/01/cloudfront-7.png)

验证证书成功我们再添加域名是可以的。根据提示我们添加CNAME解析验证当前域名所有权，等待验证完毕才可以继续。

[![](https://www.laoliublog.cn/wp-content/uploads/2023/01/cloudfront-8.png)](https://www.laoliublog.cn/wp-content/uploads/2023/01/cloudfront-8.png)

只有等待SSL认证通过才可以添加域名，否则不会通过。如果我们需要启用自定义的CDN，则需要添加CNAME解析到分配的域名。对应前面的源域名指向源服务器的IP即可。

当然这里还是不够的，我们如果需要解析到网站，还需要在服务器端配置。

Cloudfront会通过443端口和80端口，即https和http协议去请求你的服务器，你必须在你的服务器配置前面所说的CDN套用域名和源域名。我们需要在NGINX配置站点的域名添加解析。

```
server {
    listen 80;
    server_name 1.test.com 2.test.com;
    ……
}
```

类似这样。

这样子，我们的网站就可以通过亚马逊云的CDN起到加速，一般国外的外贸网站用到比较多。对于亚马逊云CDN服务，免费有提供1TB每月的流量，超过是需要额外计费的。

[取消回复](https://blog.upx8.com/3204#respond-post-3204)

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