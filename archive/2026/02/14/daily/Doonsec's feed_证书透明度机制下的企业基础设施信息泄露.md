---
title: 证书透明度机制下的企业基础设施信息泄露
url: https://mp.weixin.qq.com/s/DEzdrVF06vKP8yJrqc0DhA
source: Doonsec's feed
date: 2026-02-14
fetch_date: 2026-02-15T04:24:50.063887
---

# 证书透明度机制下的企业基础设施信息泄露

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/h4gtbB74nSj0giben3dRIu9IqwPKia7Vic1I82yIQvSDlI6ZuIWle5INFQEnLL1lrMicoictQnEY35lNU84MOXy2A4dMNG2m3I4sglgnb1QnicTVY/0?wx_fmt=jpeg)

# 证书透明度机制下的企业基础设施信息泄露

latedeployment
latedeployment

securitainment

![]()

在小说阅读器中沉浸阅读

| 原文链接 | 作者 |
| --- | --- |
| https://latedeployment.github.io/posts/certificate-transparency-info-leaks/ | latedeployment |

*这是 Certificate Transparency 系列的第二部分。*

证书透明度日志正在泄露公司的重要信息，原因在于公司 IT 或 DevOps 团队对此缺乏了解，或完全没有意识到这个问题。

# 概述

正如第一部分 Certificate Transparency 101 中所解释的，证书透明度将所有受信任 SSL 证书的详细信息公开，供任何人查看。虽然这有助于浏览器验证 CA 颁发的证书信息，但它同样也让攻击者能够获取关于公司基础设施的重要信息。

*虽然我不想展示具体证据，但我只想说，我检查过的大多数网络安全初创公司都在通过证书透明度泄露其整个基础设施信息。*

# 为什么要创建子域名

公司购买了自己的域名，假设是 `example.com`。他们通过 HTTPS 提供服务，因此必须获取证书。在 *Let's Encrypt*出现之前，公司需要花钱购买一年期的证书。虽然费用不算很高，但也足以限制公司签发证书的数量。当公司发展壮大后，为了简化内部基础设施布局，通常会使用子域名将内部服务器与用户界面分离，于是我们开始看到 `app.example.com`、`login.example.com`等子域名。

*Let's Encrypt*允许免费生成证书，前提是申请者能够证明其控制着请求证书的域名。具体来说，当为 `newcert.example.com`申请证书时，\_Let's Encrypt\_ 会向该特定域名发出一个验证挑战，服务器必须正确响应以证明控制权。关于验证方法的更多细节，请参见 Let's Encrypt challenge types。

随着公司发展，DevOps 团队可能会要求对其管理的子域名拥有更多控制权。例如，如果公司开发了一项日志存储服务，就会创建 `logs.example.com`子域名。这样做是为了方便——理论上他们可以使用任意名称，比如 `wolf.example.com`或 `simba.example.com`，但他们选择了 `logs`，因为更易读、更好记。

一段时间后，公司将拥有以下子域名：

* `example.com`

  - 主网站
* `login.example.com`

  - 身份验证方法，认证服务器在此
* `app.example.com`

  - 登录后的用户界面在此
* `logs.example.com`

  - 用户将日志上传到此网站

随着公司进一步发展，可能会有面向不同客户的多个 UI，这时可能会安装通配符证书，让 `*.console.example.com`同时服务 `customerA.console.example.com`和 `customerB.console.example.com`。但 *Let's Encrypt*不支持这种方式，所以公司必须从销售\_通配符证书\_的机构购买。由于价格昂贵，DevOps 团队会选择继续使用 \_Let's Encrypt\_，为每个客户单独签发证书。

因此，现在公司拥有以下带有证书的子域名：

* `example.com`

  - 主网站
* `login.example.com`

  - 身份验证方法，认证服务器在此
* `app.example.com`

  - 登录后的用户界面在此
* `logs.example.com`

  - 用户将日志上传到此网站
* `customerA.console.example.com`

  - 客户 A 的 UI
* `customerB.console.example.com`

  - 客户 B 的 UI

# Kubernetes

随着公司发展 (或者但愿不是从一开始就这样……)，它将开始使用 Kubernetes，因为 Kubernetes 使得启动新服务变得极其简单，每个服务都会拥有自己的内部子域名。

在内部，各团队会推动拥有自己的部署区域，比如 `staging`或 `dev`，这在 K8s 中非常容易实现。于是 `staging.api.example.com`或 `staging.app.example.com`就会被创建出来。

随着公司部署流程变得越来越复杂，公司将开始使用像 `cert-manager`这样的工具。一旦部署完成，整个证书和子域名的创建流程就实现了自动化，几乎不再需要人工干预。

# DNS 信息

只要子域名仅存在于 `DNS`中，要获取公司信息就只能通过字典爆破来发现。也就是说，你必须向 DNS 服务器逐一查询 `app.example.com`或 `ui.example.com`，才能了解某个公司域名下存在哪些子域名。

# 信息泄露

正如第一部分 Certificate Transparency 101 中所描述的，为域名签发的每一张证书都会被\_永久\_存储在证书透明度日志中。

诚然，`app.example.com`作为泄露信息并没有什么意义，但 `sailpoint.example.com`或 `okta.example.com`呢？这就是关于该公司是否使用或集成了 SailPoint 或 Okta 的重要情报。

由于 DevOps 团队对证书公开日志记录机制缺乏了解，大量公司因为使用 `k8s`+ `cert-manager`+ *Let's Encrypt*的组合，将\_整个基础设施信息\_拱手泄露。

当我联系 *Let's Encrypt*时，他们基本上告诉我：人们应该自己意识到这个问题，这是他们自己的责任。

借助一个名为 crt.sh 的网站，任何人都可以查询任意域名，网站会导出该公司的全部基础设施信息。了解一家公司运作方式的侦察阶段，只需一次搜索就能完成。

# 利用 LLM 总结子域名泄露

让情况雪上加霜的是，LLM 现在无处不在。查询 `crt.sh`，截取域名只保留子域名列表，然后让 LLM 用类似以下的提示词来总结公司基础设施：

```
You are a cybersecurity and infrastructure analyst.
Analyze the provided list of subdomains and generate a concise summary of the company's infrastructure.
Identify patterns such as:
- Cloud providers (aws, azure, gcp, cloudflare, etc.)
- Development/staging/production environments
- Services and technologies (api, mail, vpn, jenkins, gitlab, etc.)
- Geographic regions
- Third-party integrations
- Security-related services
- Customer Names?

Provide a structured summary with bullet points.
```

将子域名列表附上后，就能得到一份几乎描述了整个公司基础设施、客户名称以及所用工具的摘要。

# 公司泄露信息的示例

* 环境详情
* 服务器布局
* 内部工具
* 外部集成
* 客户名称

你与那家大型未公开公司合作的 *3.0*版新集成？发布前就已泄露。

你高度机密的客户名称？即使签了 NDA 也照样泄露。

你的认证服务器名称？泄露了。

你的监控工具和调试方式？泄露了。

*这些都是不应对外部世界可见的重要信息。*

如果你使用了上述任何工具，至少应该知道这些信息是公开的。

---

> 免责声明：本博客文章仅用于教育和研究目的。提供的所有技术和代码示例旨在帮助防御者理解攻击手法并提高安全态势。请勿使用此信息访问或干扰您不拥有或没有明确测试权限的系统。未经授权的使用可能违反法律和道德准则。作者对因应用所讨论概念而导致的任何误用或损害不承担任何责任。

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCOSzVJlQkf89Vd656PRcKTQzzdNktnMJbmEYjZwfCOG7Y5qIwOvnIPVEPXAKzWb9D4t5SdUCy4gCg/0?wx_fmt=png)

securitainment

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCOSzVJlQkf89Vd656PRcKTQzzdNktnMJbmEYjZwfCOG7Y5qIwOvnIPVEPXAKzWb9D4t5SdUCy4gCg/0?wx_fmt=png)

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