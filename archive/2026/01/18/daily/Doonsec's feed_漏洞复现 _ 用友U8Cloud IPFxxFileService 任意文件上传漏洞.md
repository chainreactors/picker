---
title: 漏洞复现 | 用友U8Cloud IPFxxFileService 任意文件上传漏洞
url: https://mp.weixin.qq.com/s/7oGpjbtH1DhNqt70HwO5PQ
source: Doonsec's feed
date: 2026-01-18
fetch_date: 2026-01-19T03:41:07.329985
---

# 漏洞复现 | 用友U8Cloud IPFxxFileService 任意文件上传漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zBdps5HcBF2lyTia4zbDGBAXb8jGZ45uyRWLTmShyJZibC5XMzIpSEeaZxxV4UcAbEqmbdOoM7I2LPjjR7f5jMhQ/0?wx_fmt=jpeg)

# 漏洞复现 | 用友U8Cloud IPFxxFileService 任意文件上传漏洞

实战安全研究

![]()

在小说阅读器中沉浸阅读

**免责声明**

|  |
| --- |
| ****本文仅用于技术学习和安全研究，请勿使用本文所提供的内容及相关技术从事非法活动，由于传播和利用此文所提供的内容或工具而造成任何直接或间接的****损失****后果，均由使用者本人承担，所产生一切不良后果与文章作者及本账号无关。如内容有争议或侵权，请私信我们！我们会立即删除并致歉。谢谢！**** |

1

**漏洞描述**

用友U8 cloud全部发行版本存在文件上传限制不当漏洞，可造成任意文件上传，进而获取服务器控制权限。

2

**影响版本**

2.0 2.1 2.3 2.5 2.6 2.7 2.65 3.0 3.1 3.2 3.5 3.6 3.6sp 5.0 5.0sp 5.1 5.1sp

3

**fofa语法**

fofa语法

```
app="用友-NC-Cloud"
```

![](https://mmbiz.qpic.cn/mmbiz_png/zBdps5HcBF2lyTia4zbDGBAXb8jGZ45uyqUVDFgNgzO29AqyD84FUG0pCpiaW96O8wGamSQjaRBSYjzMibpzOXpQQ/640?wx_fmt=png&from=appmsg)

4

**漏洞复现**

上传文件

![](https://mmbiz.qpic.cn/mmbiz_png/zBdps5HcBF2lyTia4zbDGBAXb8jGZ45uyGLLycbxj89K7p9F9JUjAeI69GAsQ8WbJ97WLM8N5iayALM8M8U1FHzA/640?wx_fmt=png&from=appmsg)

访问文件

![](https://mmbiz.qpic.cn/mmbiz_png/zBdps5HcBF2lyTia4zbDGBAXb8jGZ45uycHu5aYicNMG2tyiaSWzrDTt7aSeM1tqWgOuAuY9B9RQoicIHyCzhzMeiaA/640?wx_fmt=png&from=appmsg)

5

**检测POC**

nuclei

![](https://mmbiz.qpic.cn/mmbiz_png/zBdps5HcBF2lyTia4zbDGBAXb8jGZ45uygokfKUKDK27lzQT81gXHZZ5tWkcAb7aJNIhm0CcTooZFT9lsEualsw/640?wx_fmt=png&from=appmsg)

afrog

![](https://mmbiz.qpic.cn/mmbiz_png/zBdps5HcBF2lyTia4zbDGBAXb8jGZ45uySXiaxYF6jB1noGNYAIIibCAXn1RwftHqkEK7pwdZrZ46979nRrsAna4Q/640?wx_fmt=png&from=appmsg)

6

**漏洞修复**

1、建议联系厂商打补丁或升级版本。

2、增加Web应用防火墙防护。

3、关闭互联网暴露面或接口设置访问权限。

7

**内部圈子**

**现在已更新POC数量 1600+（中危以上）**

🔥 **1day/Nday 漏洞实战圈上线** 🔥

还在到处找公开漏洞 POC？

这里专注整合全网1day/Nday漏洞复现，一站式解决你的痛点！

🔍 圈子福利

✅ 整合全网 1day/Nday 漏洞POC，附带复现步骤，新手也能快速上手

✅ 每周更新 10-15 个POC测试脚本，经过实测验证，到手就能用

✅ 完美适配 Nuclei 主流扫描工具，脚本无需额外修改，即拿即用

✅ 重磅福利：免登录免费 FOFA 查询，无需账号也能高效资产测绘

✅ 专属权益：提供指纹识别库，指纹库持续更新

💡 适合对象

渗透测试🔹攻防演练🔹安全运维🔹企业自查🔹SRC漏洞挖掘

👉 不管你是参加攻防演练的战队成员（红队/蓝队），或者是做渗透测试的工程师，还是做src漏洞挖掘和企业安全自查的运维人员等职业，这里的资源都能适合你

⚠️ 重要提醒

仅限授权范围内的合法安全测试，严禁用于未授权攻击行为！

本服务为虚拟资源服务，一经购买概不退款，请按需谨慎购买！

现在加入圈子价格是59.9元（交个朋友啦），后面将调整涨价啦。

![](https://mmbiz.qpic.cn/mmbiz_jpg/zBdps5HcBF3oJ7iaibTn5lqn7gNWQtO0Areia3jT8E5TBnUFp0u3Y7hXzbtHyicWAzv9RafOVa4YOby4l5ZGsLTRfw/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/zBdps5HcBF11icZP3IFHQ3V3ayPqKCuRxbljuSc8zianApHibibJQzEG3qXvkW76uWBjvYrGNTZOmcvXTl5K8ely0g/0?wx_fmt=png)

实战安全研究

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/zBdps5HcBF11icZP3IFHQ3V3ayPqKCuRxbljuSc8zianApHibibJQzEG3qXvkW76uWBjvYrGNTZOmcvXTl5K8ely0g/0?wx_fmt=png)

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