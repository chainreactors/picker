---
title: Apache OpenNLP 曝出一组高危漏洞，包括XXE注入
url: https://mp.weixin.qq.com/s/Zn_l-GnWSbj8jIY2dumfnw
source: Doonsec's feed
date: 2026-05-04
fetch_date: 2026-05-05T05:01:49.112344
---

# Apache OpenNLP 曝出一组高危漏洞，包括XXE注入

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6N9HCJpmz1EwlybibWmEhnRQPlxmDibiat2icibfGiauk9OjWh0TXpZCWdYtibWfj29dpSOkCdX0WnzvCMLy8Wia52SliagWNgYy4BrMIc8/0?wx_fmt=jpeg)

# Apache OpenNLP 曝出一组高危漏洞，包括XXE注入

原创

A译
A译

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> **导语**：Apache OpenNLP 是 Java 生态中常用的自然语言处理库，被大量企业用于文本解析、实体识别等场景。2026年5月2日安全社区披露该库存在多个漏洞——拒绝服务、权限提升、XXE，三类攻击面同时存在。在生产环境中使用 OpenNLP 的团队，需要立即评估风险。

---

这次披露了三个 CVE，影响版本为 OpenNLP up to 2.5.8 以及 3.0.0-M2。

CVE-2026-42440 是拒绝服务漏洞。AbstractModelReader 在处理恶意构造的模型文件时，可能导致服务崩溃。攻击者只需提供一个畸形的模型文件，触发异常后目标系统的处理线程会中断。对于依赖 OpenNLP 做实时文档处理的服务，这等同于一次精准的 DoS 攻击。无需认证，只需能向目标提交模型文件即可触发。

CVE-2026-42027 是权限提升漏洞。Model Manifest ExtensionLoader 在解析模型清单文件时存在权限提升路径。这个漏洞的利用前提是攻击者能够在目标系统上部署恶意模型文件——一旦成功加载，可能突破当前运行账户的权限限制执行更高权限操作。在多租户环境或内容处理平台中风险较高。

CVE-2026-40682 是 XXE 外部实体注入，这是最值得关注的。Dictionary Parser 在解析 XML 格式的字典文件时，未正确禁用外部实体引用。攻击者可以通过构造包含 `SYSTEM` 或 `ENTITY` 引用的恶意 XML 文件，诱使解析器读取服务器本地文件或发起内部网络请求。

![Apache OpenNLP XXE漏洞示意图](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6O1MlaZ9zn4rSCstcyIbuEDoEzcibXe5MuJCNtIwZ8fMQwprk38fyo0cKbRjAChA7k31LfMHlfEPKwCMRSP8bTDI3FH5IibFdeicQ/640?wx_fmt=png "Apache OpenNLP XXE漏洞示意图")

典型攻击 payload 是这样的：

```
<!DOCTYPE dictionary [
  <!ENTITY xxe SYSTEM "file:///etc/passwd">
]>
<dictionary>
  <entry>
    <word>&xxe;</word>
  </entry>
</dictionary>
```

当 OpenNLP 的 Dictionary Parser 加载这个文件时，`/etc/passwd` 的内容会被嵌入到解析结果中，攻击者间接获取了本地文件读取能力。如果你的 OpenNLP 部署允许用户上传或配置字典文件，这就是一个直接的 RCE 路径。

OpenNLP 在企业中的典型使用场景包括：文档处理平台自动提取合同和报告中的关键信息、客服系统的 NLP 驱动意图识别和自动回复、内容审核的文本分类和敏感词检测、以及搜索引擎的文本预处理和索引优化。如果模型文件和字典文件来自不可信来源（如用户上传），则直接面临漏洞利用风险。

建议相关团队立即检查自身场景，及时关注 Apache OpenNLP 官方安全公告获取修复版本。临时缓解措施包括：对所有外部提供的模型和字典文件进行格式校验；在解析 XML 前确保禁用外部实体引用；OpenNLP 运行账户不应拥有敏感文件读取权限；将解析服务运行在独立容器或沙箱中限制横向移动能力。

**版权声明**：本文由华盟网原创发布，保留所有权利。配图由华盟网授权使用。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

黑白之道

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

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