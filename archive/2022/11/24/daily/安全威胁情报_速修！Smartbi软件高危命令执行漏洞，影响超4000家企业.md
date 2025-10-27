---
title: 速修！Smartbi软件高危命令执行漏洞，影响超4000家企业
url: https://mp.weixin.qq.com/s?__biz=MzI5NjA0NjI5MQ==&mid=2650175034&idx=1&sn=e409660353cc61a0e6f4c5a3369eeb11&chksm=f4488d86c33f049066b9b734f4b5fc12ccf26e67fcf88d4547cf973c83715a5fd79b5e009ea9&scene=58&subscene=0#rd
source: 安全威胁情报
date: 2022-11-24
fetch_date: 2025-10-03T23:39:39.568437
---

# 速修！Smartbi软件高危命令执行漏洞，影响超4000家企业

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Yv6ic9zgr5hTwk4JxyWhcuXp88ZXqN4CVyokhX7noRpXce9hfHy0hMsOk3Ld9AGich8zLsDSECP53Adup4gMsURA/0?wx_fmt=jpeg)

# 速修！Smartbi软件高危命令执行漏洞，影响超4000家企业

原创

微步情报局

微步在线

![](https://mmbiz.qpic.cn/mmbiz_jpg/Yv6ic9zgr5hTwk4JxyWhcuXp88ZXqN4CVx0xuRjqGOy84Lf0dtUMFhCmia0mCwYrgCTMb9LghuCJSxFhq8JMwbOg/640?wx_fmt=jpeg)

**漏洞概况**

近日，微步在线通过“X漏洞奖励计划”获取到Smartbi商业智能软件命令执行漏洞的相关漏洞情报，**微步TDP已经于2022年9月起支持对该0day漏洞的检测**。

据微步X企业版资产测绘信息来看，目前至少有超过100个IP地址（企业）受此漏洞影响，据Smartbi官网信息，有超过4000家企业使用了Smartbi商业智能软件，其中包括世界500强中近半数的中国企业，覆盖金融、地产、制造、零售、教育、政府、医疗等60+行业，影响范围极其广泛。

**经微步技术团队验证**：

Smartbi商业智能软件未对JDBC的db2做过滤，通过构建恶意指令能够实现命令执行。目前Smartbi已经发布修复该漏洞后的最新版本10.5.8，其他版本的软件均受此漏洞影响，建议相关用户更新至最新版本。

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMIAbEUHQSx1MAicRPdJuQFehiaoAX5q8KHZBWmRaDz0DX7TfnpM39YxddJfongq7FWDKGcWn12EyzNQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hTwk4JxyWhcuXp88ZXqN4CVpoqlxX2Xkw39KTkR8icbYqnfvbhCYtUggLH1jhEdeADS2SjwWJibqFIQ/640?wx_fmt=png)

**漏洞评估**

**影响软件：**Smartbi商业智能BI软件

**公开程度：**PoC未公开

**利用条件：**无权限要求

**交互要求：**0-click（零点击）

**漏洞危害：**高危、命令执行

**影响范围：**<10.5.8 (最新版)

**修复方案**

**1. 缓解措施**

配置 WAF 规则，对数据包中有 clientRerouteServerListJNDIName 关键字数据包过滤。

**2. 官方修复方案**

进入 https://www.smartbi.com.cn/patchinfo 获取厂商发布的 V10.5.8 的补丁包，进行升级即可。

**3. 部署 TDP 预防更多 0day**

拨打 400-030-1051 咨询 TDP 威胁感知平台详情，或通过文末二维码预约 TDP 免费试用。

**时间线**

2022.08  微步“X漏洞奖励计划”获取该漏洞相关情报

**2022.09  TDP支持检测**

2022.10  X企业版、OneEDR、OneSIG支持检测

2022.11  报送监管、厂商、漏洞情报订阅客户

**2022.11  厂商发布补丁**

### 2022.11  微步情报局发布通告

---

**安全传送门**

Free Trial

扫码立即体验TDP

↓↓↓

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hTwk4JxyWhcuXp88ZXqN4CVHpdxh1YD0Kv9VqeSsmywmmBJfPCS89SibcZOF7enNtoQ2RW3uzyEppQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hTIdM9koHZFkrtYe5WU5rHxSDicbiaNFjEBAs1rojKGviaJGjOGd9KwKzN4aSpnNZDA5UWpY2E0JAnNg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

400-030-1051

---

· END ·

点击下方名片，关注我们

觉得内容不错，就点下“**赞**”和“**在看**”

如果不想错过新的内容推送，可以设为**星标**![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hTYyCkc91euAiaGULJSbiaHricFHs2dd2sib20WTJKwHYD90Jia9HCKxnmJUwnkicGU7rVP3EYCVh3dMnng/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)哦

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hTHHXF0GLtxEgadu9UKHf9JTdE1CrfxkZCYbPIbkQu1Xz1ia8YKicACMrHQkq7rTll3LKJGRhyibGpcA/0?wx_fmt=png)

微步在线

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hTHHXF0GLtxEgadu9UKHf9JTdE1CrfxkZCYbPIbkQu1Xz1ia8YKicACMrHQkq7rTll3LKJGRhyibGpcA/0?wx_fmt=png)

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