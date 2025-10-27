---
title: AWS S3 Bucket子域接管实现可信钓鱼服务攻击
url: https://mp.weixin.qq.com/s?__biz=MzkyMTI0NjA3OA==&mid=2247489851&idx=1&sn=861f8977b36f279d6a4eb1a4a3c3bf54&chksm=c187d92af6f0503cf733c875c3d171312ff9e5810603b12eb8495c77c6ea06f77703e5b9d7bd&scene=58&subscene=0#rd
source: M01NTeam
date: 2022-10-13
fetch_date: 2025-10-03T19:47:20.362527
---

# AWS S3 Bucket子域接管实现可信钓鱼服务攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/TPGibEO8KBwYLg3ukZeNltdEkYADBuzGj1icsjJFuIa0MjNfEgtAjgHV455C96RHU9IIQ7D4CVZmBDZXicZA1nPOA/0?wx_fmt=jpeg)

# AWS S3 Bucket子域接管实现可信钓鱼服务攻击

原创

天元实验室

M01N Team

![](https://mmbiz.qpic.cn/mmbiz_gif/TPGibEO8KBwYLg3ukZeNltdEkYADBuzGjMIUVpRoicURibXhR5FDJY3pGDibEhHftIMpibOBzEmbgrcP4VPhIrJXYMw/640?wx_fmt=gif)

**情报背景**

随着近些年来企业上云不断加速，相关技术落地成熟，公私有云等平台服务已经广泛应用在了各大业务场景中，企业暴露在公网的云服务数量出现爆发式增长。这些暴露在公网的云服务包含对象存储、弹性计算、云函数、云数据库等，其中不乏包含配置错误与密钥泄露等问题的公开服务，攻击者可轻松利用云服务特性直接利用或者接管对应的云资源，成为其优质的攻击资源。本文以 AWS S3 Bucket 出发，讲述如何利用 S3 对象存储服务，实现可信子域下的钓鱼服务部署。

**01** S3 Bucket 接管

我们在实际访问一些站点时，可能会出现以下的响应结果，其中提示包含 NoSuchBucket 等关键字。

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwYLg3ukZeNltdEkYADBuzGj6micsXZrJLj0I8EIZ61Nq5CqZTeOz8dBUQ58wlKaW1gyS1XlHI1sic8A/640?wx_fmt=png)

查看其 DNS 解析记录可以发现，该域名被 CNAME 记录解析到了 AWS S3 对象存储服务提供的子域名上。

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwYLg3ukZeNltdEkYADBuzGjPxica5UduOd0wj4JfSmJzZKNHoX2iaNInqmlYC1Mm7BvaBK4wbD4mTbg/640?wx_fmt=png)

我们在使用 S3 Bucket 的过程中，AWS 会提供一个专属的域名给用户进行存储桶的访问和使用，如下所示：

* **DOC-EXAMPLE-BUCKET**代表用户自定义的 Bucket Name
* **s3**代表服务类型
* **us-west-2**代表对象存储的区域为美国西部

```
https://DOC-EXAMPLE-BUCKET.s3.us-west-2.amazonaws.com/photos/puppy.jpg
```

而在实际的业务运行过程中，用户可能会将自己的域名 CNAME 到上述域名中，方便在业务中进行使用；由于 Bucket Name 是由用户自定义命名的，当访问一个不存在的 Bucket 时，AWS 就会响应**NoSuchBucket**的状态码，其中 BucketName 标签中的值代表着自定义的存储桶名称，我们可以创建该名称的 S3 Bucket 实现对目标子域的接管。

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwYLg3ukZeNltdEkYADBuzGjEEWnbmOTyIxWBAQaf97tq7rc1oQIU71Nz914oK2HEicdbF4LgdLgPrg/640?wx_fmt=png)

创建时需要注意 存储桶名称 和 AWS区域 都需要与目标 CNAME 的 AWS 子域名保持一致。

成功创建 S3 Bucket 后，再次访问目标子域时，返回的状态码变成了 AccessDenied，表示已经成功接管目标子域，但是默认情况下创建的存储桶不具备公开可读权限。

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwYLg3ukZeNltdEkYADBuzGj3ibkA417RTw0XcHGUJicAnIib3FibxoLNVsG544jsakjR4wribNmqTS1cCg/640?wx_fmt=png)

配置存储桶关闭**阻止所有公开访问**并**配置存储桶策略开启公有读权限**，上传文件进行访问测试。

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::BucketName/*"
        }
    ]
}
```

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwYLg3ukZeNltdEkYADBuzGj44WTy1h0dIj5BtgcNuvHqt04Xu71cxfW9Cs2icT9QgmicRV1iabgHibQ7w/640?wx_fmt=png)

可以看到我们已经成功接管了该子域，此时恶意的攻击者可以利用该可信子域，向目标进行恶意载荷投递、C2通信等攻击行为。

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwYLg3ukZeNltdEkYADBuzGjzx5mZe5HibeobTcGOxOSNTVsZHagAJK0Agn7uqovN4wtg1CdfiaHnEAQ/640?wx_fmt=png)

**02**S3 Bucket 静态页面部署

S3 Bucket 对于上传到其中的 HTML 文件，访问对应的对象 URL 可以直接响应相关的 HTML 页面，因此可以利用该功能实现单个静态页面的部署，直接上传自定义的 HTML 文件到 S3 Bucket。

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwYLg3ukZeNltdEkYADBuzGjwUajTXYicEOmFPqAcF5YTsoaPUKlLicqyle7KXRs0a7B8VSQjb3ZicA5w/640?wx_fmt=png)

访问对应的 URL 可以看到响应的Content-Type为text/html，Server为 AmazonS3。

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwYLg3ukZeNltdEkYADBuzGjhxA1qO8VxJH3wziaEaDf86CCOTgLexn5w2IBMX9oB6SOXMeNrWPVWVA/640?wx_fmt=png)

结合上面的**S3 Bucket 子域接管**和**S3 Bucket静态页面托管**，我们可以通过接管子域来实现到钓鱼页面的访问，达到基于可信子域进行钓鱼的目的。从被钓目标的视角来看，访问的站点可能是自己公司或者其他高可信公司名下的某个子域，具备很强的迷惑性，从而有效的提高钓鱼的成功率。

**03**S3 Bucket 静态站点托管

利用上述的 S3 Bucket 特性，我们可以完成单个静态页面的部署，但是仅是单个静态页面可能会引起目标用户的怀疑，整个钓鱼站点的交互逻辑还是过于简单，例如随便改动访问的目标页面文件，通过响应内容就可能暴露我们使用的是 S3 Bucket 托管的单页面文件。

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwYLg3ukZeNltdEkYADBuzGj9ibsPtRNicRage3qt8A3lbqrVMgkY78CwdIX8icd0Tuxk9NQXohe8q0Bg/640?wx_fmt=png)

那么是否可以基于 S3 Bucket 部署一个交互更加复杂，更加具备迷惑性，并且可以基于可信子域下的钓鱼站点 ？

根据官方文档可以获知，可以使用 S3 Bucket 进行静态站点的托管功能，从而完成 React JS、Vue JS 等框架编写的单页应用程序的部署。

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwYLg3ukZeNltdEkYADBuzGjZvVW1P2LiaOz5xiaN6tHFbrc9Km8BagEjFA6aGx2NruyMAgFNd2EQibIA/640?wx_fmt=png)

攻击者可以结合 S3 Bucket 静态站点配置访问可信子域名时的默认页面、设置自定义的报错页面，以及配置路由重定向等功能，进一步增强整个钓鱼站点的伪装特性，提高社工钓鱼的成功率。

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwYLg3ukZeNltdEkYADBuzGjrxpic4eaBG6Ycr6lt0lBp6lGdN20m34c41BjMLRLxrLIhvo0Tjt5wiaA/640?wx_fmt=png)

AWS 上的每个 S3 Bucket 都可以单独开启静态网站托管的功能，主动开启相关功能后，同样需要配置存储桶的规则开启存储对象的公有读权限。

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwYLg3ukZeNltdEkYADBuzGjiaKahsNrD0r8QicQ66QU9ppRQb5XZesiagLYc99BCQPHavqoxPuMibdXZA/640?wx_fmt=png)

开启该功能以后，访问静态站点需要使用存储桶 AWS 区域上特定的终端节点进行访问，简而言之，我们访问站点的 URL 会有所变化：

```
http://bucket-name.s3-website-us-east-1.amazonaws.com/
```

* **bucket-name**代表用户自定义的存储桶名称，当用户使用自己的域名 CNAME 到 S3 Bucket 时，bucket-name 需要与域名保持一致，AWS 通过 HTTP 请求中的主机名来完成对应存储桶的关联
* **s3-website-us-east-1**代表 s3-website-Region

当访问某些域名出现以下的响应方式时，说明该域名被 CNAME 到了 AWS 具备静态站点托管功能的特定终端节点上：

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwYLg3ukZeNltdEkYADBuzGjYDibTGOyzJJNY7Br4JEH6mv4Ch21MZ1TibAg5S1OVE0NocV9ETHjLhCg/640?wx_fmt=png)

创建与 BucketName 子域名相同名字的 S3 存储桶，完成子域接管，将准备好的单页应用程序上传，配置好**索引文档**和**错误文档**后，直接访问子域名。

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwYLg3ukZeNltdEkYADBuzGjWNL8KrBVcpb3CsxmSC4atjkC5t93D4S8Av6cHYwYDdD7iaFgeh7amFQ/640?wx_fmt=png)

访问不存在的页面。

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwYLg3ukZeNltdEkYADBuzGjIhM6vxf0ltw2dqoeIYMvSXZjCSicAa3anib7FkEtNKmhV3IUnaNjnFAA/640?wx_fmt=png)

可以看到，已经成功接管该子域，并完成静态站点的托管操作。

这里以实战案例为例，尝试部署实际钓鱼场景下的页面进行钓鱼演示，将准备好的钓鱼站点部署到 S3 Bucket Website 中，可以看到此时访问的域名是已经接管的测试域名。

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwYLg3ukZeNltdEkYADBuzGjYRy2utcqDicaRhbzicEnj0dbC5Fl9a1osbssEIIQPqZDkOUswFR3H2eQ/640?wx_fmt=png)

在该页面登录完成后，将直接跳转至真正的邮件登录页面，进入社工钓鱼平台，可以看到已经成功回传了输入的账号密码。

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwYLg3ukZeNltdEkYADBuzGjQlUKhVtgCErAvNoYGow2xxvNdBu8uacGFEkmJiac8gVTmibSwSyYDHTg/640?wx_fmt=png)

**04**检索可接管子域

在上面笔者已经介绍了该如何利用 S3 Bucket 来接管可信的子域，并利用其进行钓鱼页面部署的攻击场景，那么该如何快速寻找符合条件的子域来完成接管 ？

其实可以看到无论是**S3 Bucket**还是**S3 Bucket Website**，我们访问不存在 Bucket Name 的 URL 时，都会有特定的响应结果，结合这个特点，可以利用 Fofa 等网络资产测绘平台来检索符合条件的子域：

* 检索可接管的 S3 Bucket

```
body="<Code>NoSuchBucket</code>" && host!=".amazonaws.com" && host!="aliyuncs.com" && is_domain=true && country="US"
```

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwYLg3ukZeNltdEkYADBuzGj9hs0mBmiboqE07PiaYibadI6tofTn3An1Uq5qe2RaR2m18MFGQetdcBlQ/640?wx_fmt=png)

* 检索可接管的 S3 Bucket Website

```
body="Code: NoSuchBucket" && host!=".amazonaws.com" && host!="aliyuncs.com" && is_domain=true && country="US"
```

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwYLg3ukZeNltdEkYADBuzGj91CQaM8ru5IqkckciaFFIQoZQZElr5a97ktINMiaz5Qv0B3PQfNdR4NQ/640?wx_fmt=png)

可以看到按照特定的条件筛选下来以后，还是有许多可以利用的子域，在这些子域中可以进一步进行筛选和检索，找到符合条件的可接管子域：

* 直接筛选与目标公司具有关联性的域名子域
* 筛选具备高可信价值的域名子域

**05**总结

利用 S3 Bucket 这种方式来接管子域，攻击者充分利用**可信子域**与**S3 Bucket服务**的特性，将其作为优质的攻击资源，可以应用在各类攻击场景中，除了本文中讲述的可信钓鱼外，还可能被用在恶意载荷投递、C2通信等场景中，由于整个通信过程中都在使用可信的子域环境，其天然的具备较强的迷惑性和隐蔽性，为防守者的检测带来一定的挑战。

![](https://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwYLg3ukZeNltdEkYADBuzGjgEzH4w6Kszg2CU2Yje8jQX69Tty7bo4ib0ia7USwXILwibicGC4gSicqT4Q/640?wx_fmt=png)

**绿盟科技天元实验室**专注于新型实战化攻防对抗技术研究。

研究目标包括：漏洞利用技术、防御绕过技术、攻击隐匿技术、攻击持久化技术等蓝军技术，以及攻击技战术、攻击框架的研究。涵盖Web安全、终端安全、AD安全、云安全等多个技术领域的攻击技术研究，以及工业互联网、车联网等业务场景的攻击技术研究。通过研究攻击对抗技术，从攻击视角提供识别风险的方法和手段，为威胁对抗提供决策支撑。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TPGibEO8KBwYLg3ukZeNltdEkYADBuzGjtOjVGTOI3Ijwbqj1sQyqCQNjzReINBBbiaPtkCXCgkGYgzksbgerUDA/640?wx_fmt=jpeg)

**M01N Team公众号**

聚焦高级攻防对抗热点技术

绿盟科技蓝军技术研究战队

![](https://mmbiz.qpic.cn/mmbiz_jpg/TPGibEO8KBwYLg3ukZeNltdEkYADBuzGjnbpIHZgIKrHuSZQuUxNwASJ1fkqkUDBiaC18gaicicicwIrlygLp9iaqk8A/640?wx_fmt=jpeg)

**官方攻防交流群**

网络安全一手资讯

攻防技术答疑解惑

扫码加好友即可拉群

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwa3nTcsDs91X6JY6LnXNhPLatIoU1PEVBLzWXTcnyiahhYUB9hcwX2MJkOmo9NEM2jVO8ib8yutnJxw/0?wx_fmt=png)

M01N Team

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/TPGibEO8KBwa3nTcsDs91X6JY6LnXNhPLatIoU1PEVBLzWXTcnyiahhYUB9hcwX2MJkOmo9NEM2jVO8ib8yutnJxw/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过