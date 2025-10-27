---
title: 新型Gorilla安卓恶意软件窃取短信验证码
url: https://blog.upx8.com/4761
source: 黑海洋 - Wiki
date: 2025-04-22
fetch_date: 2025-10-06T22:06:56.909183
---

# 新型Gorilla安卓恶意软件窃取短信验证码

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 新型Gorilla安卓恶意软件窃取短信验证码

发布时间:
2025-04-21

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
74911

![](https://cdn.skyimg.de/up/2025/4/21/e8cv8o.webp)

网络安全领域近期出现一种名为"Gorilla"的新型安卓恶意软件，专门设计用于拦截包含一次性密码（OTP）的短信。

该恶意软件在后台隐蔽运行，通过滥用安卓权限系统获取受感染设备的敏感信息。初步分析表明，Gorilla主要针对银行客户和Yandex等流行服务用户，并对窃取的短信进行分类以便攻击者利用。

## 技术实现机制

该恶意软件利用READ\_PHONE\_STATE和READ\_PHONE\_NUMBERS等关键安卓权限，获取SIM卡信息并读取受感染设备的电话号码。

安装后，Gorilla通过WebSocket协议建立与C2（命令与控制）基础设施的持久连接，连接格式为"ws://$URL/ws/devices/?device\_id=$android\_id&platform=android"，保持与操作者的持续通信。这种连接方式使恶意软件能够实时接收指令并外泄敏感数据。

研究人员发现，Gorilla采用非常规技术规避检测：避免使用需要REQUEST\_INSTALLED\_PACKAGES权限的getInstalledPackages或getInstalledApplications API，转而查询启动器意图来确定软件包名称、应用名称和版本信息，从而在保持低调的同时收集已安装应用信息。

## 攻击目标与数据分类

恶意软件的C2面板显示其运作相当精密，窃取的短信被系统性地归类为"银行"和"Yandex"等标签，表明其针对金融信息和流行服务的定向攻击策略。这种分类使攻击者能快速识别并利用拦截消息中的有价值验证码和敏感信息。

Gorilla通过一系列后台服务保持持久运行，即使用户未主动使用设备也能持续运作。为符合安卓要求，这些服务使用startForeground API和FOREGROUND\_SERVICE权限显示通知，将其恶意活动伪装成合法系统进程。

## 技术分析：指令结构与功能

该恶意软件的指令结构包含三种主要操作类型：

![](https://cdn.skyimg.de/up/2025/4/21/bjyevc.webp)

操作类型（来源：Catalyst）

1. "device\_info"指令：提取并传输受感染设备的详细信息
2. "update\_settings"指令：当前仅记录接收情况，但可能用于远程配置恶意软件行为
3. "send\_sms"指令：允许攻击者从受感染设备向指定接收者发送自定义内容的短信

```
// Gorilla恶意软件中的指令处理结构
// 三种主要指令类型：
device_info // 传输设备信息
update_settings // 当前未激活但记录接收情况
send_sms // 允许远程发送指定内容的短信
```

## 潜在扩展功能

虽然当前主要利用短信拦截功能，但Gorilla包含的组件表明其功能可能进一步扩展。未使用的WebViewActivity类尤其值得关注，该组件通常用于渲染HTML内容，银行类恶意软件常用其显示仿冒页面以窃取银行凭证或信用卡信息。

恶意软件还包含一个目前未激活的持久化机制USSDReceiver类，该组件设计用于监听"\*#0000#"拨号代码并在检测到时启动MainActivity。虽然当前未注册激活，但该机制可能为攻击者提供额外方法确保恶意软件在被清除后仍能保持运行。

**参考来源：**

> [New Gorilla Android Malware Intercept SMS Messages to Steal OTPs](https://blog.upx8.com/go/aHR0cHM6Ly9jeWJlcnNlY3VyaXR5bmV3cy5jb20vbmV3LWdvcmlsbGEtYW5kcm9pZC1tYWx3YXJlLWludGVyY2VwdC1zbXMtbWVzc2FnZXMv)

[取消回复](https://blog.upx8.com/4761#respond-post-4761)

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