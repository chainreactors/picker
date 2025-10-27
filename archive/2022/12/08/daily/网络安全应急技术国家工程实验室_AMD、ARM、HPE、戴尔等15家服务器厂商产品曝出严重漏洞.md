---
title: AMD、ARM、HPE、戴尔等15家服务器厂商产品曝出严重漏洞
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247533194&idx=3&sn=5aff8415158698c181468f65fd30f3bb&chksm=fa93f44bcde47d5dd8d2ae651793b0189675dd7aaadde80a6d1d585389e6c45dbfb4c9dbad07&scene=58&subscene=0#rd
source: 网络安全应急技术国家工程实验室
date: 2022-12-08
fetch_date: 2025-10-04T00:54:04.847023
---

# AMD、ARM、HPE、戴尔等15家服务器厂商产品曝出严重漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176n1NvL0JsVSB8lNDX2FCGZjHX4GguqGfPf10AzGWf9Jv9YCsBkkRrITo7l5W5FYfGgNGojUYcR79g/0?wx_fmt=jpeg)

# AMD、ARM、HPE、戴尔等15家服务器厂商产品曝出严重漏洞

网络安全应急技术国家工程中心

![](https://mmbiz.qpic.cn/mmbiz_png/GoUrACT176n1NvL0JsVSB8lNDX2FCGZjW7eKHKK7SQ1ibgbicSR1EnUHRCMaDXiav0F1OlNFyiaRhsyv5nU49JX0Rg/640?wx_fmt=png)

全球大量云计算和数据中心正面临一次严峻的服务器供应链安全危机。

American Megatrends的服务器远程管理控制软件MegaRAC BMC近日曝出多个严重漏洞，攻击者可以在特定条件下执行代码、绕过身份验证和执行用户枚举。

据悉，这些漏洞是Eclypsium安全研究人员于2022年8月检查American Megatrends泄漏的专有代码（特别是MegaRAC BMC固件）后发现的。

MegaRAC BMC固件被至少15家服务器制造商使用，包括AMD、Ampere Computing、ASRock、Asus、ARM、Dell EMC、Gigabyte、Hewlett-Packard Enterprise、Huawei、Inspur、Lenovo、Nvidia、Qualcomm、Quanta和Tyan。

**漏洞详情**

Eclypsium发现并报告给American Megatrends和受影响供应商的三个漏洞如下：

* CVE-2022-40259：由于不正确地向用户公开命令，Redfish API存在任意代码执行缺陷。（CVSS v3.1得分：9.9“严重”）
* CVE-2022-40242：系统管理员用户的默认凭据，允许攻击者建立管理外壳。（CVSS v3.1得分：8.3“高”）
* CVE-2022-2827：请求操作缺陷允许攻击者枚举用户名并确定帐户是否存在。（CVSS v3.1得分：7.5“高”）

三个漏洞中最严重的漏洞CVE-2022-40259需要事先至少访问一个低权限帐户才能执行API回调。

Eclypisum说：“唯一的问题是攻击位于路径参数中，但它不是由框架进行URL解码的，因此需要专门设计漏洞利用，使其对每个URL和每个bash shell命令都有效。”

对于CVE-2022-40242的利用，攻击者的唯一先决条件是能够远程访问设备。

**漏洞危害与缓解**

前两个漏洞非常严重，因为攻击者无需进一步升级即可访问管理shell。

如果攻击者成功利用这些漏洞，可能会导致数据操纵、数据泄露、服务中断、业务中断等。

第三个漏洞不会对安全产生重大的直接影响，因为知道目标上存在哪些帐户还不足以造成任何损害。

但是，它会为暴力破解密码或执行凭据填充攻击开辟道路。

Eclypsium在报告中评论说：“由于数据中心倾向于在特定硬件平台上标准化，任何BMC级别的漏洞很可能适用于大量设备，并可能影响整个数据中心及其提供的服务。”

“托管服务和云服务商的服务器组件标准化意味着这些漏洞很容易影响数十万甚至数百万个系统。”

Eclypsium建议系统管理员禁用远程管理选项，并尽可能添加远程身份验证步骤。

此外，管理员应尽量减少Redfish等服务器管理界面的外部暴露，并确保在所有系统上安装最新的可用固件更新。

**报告链接：**

https://eclypsium.com/2022/12/05/supply-chain-vulnerabilities-put-server-ecosystem-at-risk/

原文来源：GoUpSec

“投稿联系方式：010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176njVOPvfib4X3jQ6GIHLtX8SSDvbpmcpr4uu3X7ELG7PDjdaLVeq4Er02ZoicTPvxrC6KCVH3bssUVw/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

网络安全应急技术国家工程中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

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