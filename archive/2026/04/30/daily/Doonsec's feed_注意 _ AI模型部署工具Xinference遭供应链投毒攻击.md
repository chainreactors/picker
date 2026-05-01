---
title: 注意 | AI模型部署工具Xinference遭供应链投毒攻击
url: https://mp.weixin.qq.com/s/YKQGvbwSQfDK-OE8wqt28A
source: Doonsec's feed
date: 2026-04-30
fetch_date: 2026-05-01T05:36:30.204188
---

# 注意 | AI模型部署工具Xinference遭供应链投毒攻击

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LJwWAbW20Cia3XTKbVuGLUPMWlge3UHTtX4Vv8It0VoPngiaBmEibEIeMCh1KsFJEZibpSkicKOtpjicxlVS4iaA2FwSq9Bnd6fenrzJ8nHUTM0FaI/0?wx_fmt=jpeg)

# 注意 | AI模型部署工具Xinference遭供应链投毒攻击

中国信息安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

[![](https://mmbiz.qpic.cn/mmbiz_gif/LJwWAbW20ChOhrO8sO0HcgPW3eCRfFBdMTgmvTTQFpq0jtS1dfVyIbkgXxYssxdw9pibCa9q15iciaomMVuXVxnk22YK1rtjS2JmM48XHNWZ3Y/640?wx_fmt=gif&from=appmsg)](https://cisat.cn/all/14915419?from_tag=1)

监测发现，近期AI模型部署工具Xinference遭供应链投毒攻击。攻击者向Python官方软件包仓库PyPI（Python Package Index）上传了包含恶意代码的Xinference软件包，用户安装受影响的软件包或者在代码文件中引入Xinference时，恶意代码将自动执行。攻击者可窃取云平台凭据、API密钥、数据库密码、加密货币钱包和环境变量等敏感信息，并发送至远程命令与控制服务器。

一、影响范围

2026年4月安装或升级Xinference的用户，主要影响Xinference 2.6.0、2.6.1、2.6.2三个版本。

二、处置建议

一是排查使用版本。检查本地Xinference版本，若已安装恶意版本，建议立即卸载并回退至2.5.0及以下安全版本，同步清理项目目录及site-packages下相关可疑文件或缓存文件。二是更新敏感凭证。立即更新受感染环境中使用的AWS/GCP等云服务凭证、代码仓库Token、数据库链接、API密钥、SSH密钥等敏感凭证，阻断攻击者非法利用路径。三是强化安全认证。对云控制台、代码仓库、包管理平台等关键系统账号启用多因素认证，降低凭证被滥用风险。四是开展安全排查。封禁恶意域名whereisitat.lucyatemysuperbox.space及其解析IP地址，排查云平台、版本控制系统等异常操作日志，同步排查受影响主机是否存在异常内网扫描、SSH连接记录和新增计划任务，及时处置安全风险。五是提升安全意识。近期AI应用频遭投毒攻击，建议广大用户做好安全防护，严防个人信息和重要数据泄露造成重大损失。

（来源：国家网络安全通报中心）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LJwWAbW20CjauiaQEcdBr1THD0oeQicYZKaT1MUmOoRibicxklQ98OMQwMNGL44An2lBEoibzqr6Y2gvRKWpuSVdPeIn3QtmflEBmDic1ib0C69AsI/640?wx_fmt=png&from=appmsg)

[![](https://mmbiz.qpic.cn/mmbiz_png/LJwWAbW20CjCmAhdiczQ05Uiayj6ZundjbnF9P0jaBWaYuXIvjic2f5x33kgArwp83HunhsuG27dmZibKTWiaP8CcJxYWia5bWW0RNzy77CPvaNQ0/640?wx_fmt=png&from=appmsg)](https://cisat.cn/)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/1brjUjbpg5xcg6pmGiagMsJTqnHObJGHSj6TEe6InbwlHLIxFVhPohvicQibAcuia5wDEoRISsAkUyYPUB06cU9mibw/0?wx_fmt=png)

中国信息安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/1brjUjbpg5xcg6pmGiagMsJTqnHObJGHSj6TEe6InbwlHLIxFVhPohvicQibAcuia5wDEoRISsAkUyYPUB06cU9mibw/0?wx_fmt=png)

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