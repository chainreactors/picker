---
title: 【安服水洞系列】Dify API密钥明文暴露漏洞
url: https://mp.weixin.qq.com/s/T2aLxuN0qYCmEOzvA3kX1Q
source: Doonsec's feed
date: 2026-01-09
fetch_date: 2026-01-10T03:23:41.169215
---

# 【安服水洞系列】Dify API密钥明文暴露漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/kicAxkky0Cy2qR7qKvIoicRUTn5nVbKbClPNCUib1qYzSKQtCicgyX3lUbz3vXTu2McJ1jz8BDet6JxHmK414AZiabQ/0?wx_fmt=jpeg)

# 【安服水洞系列】Dify API密钥明文暴露漏洞

原创

小Tiamo

貔瑞安全实验室

![]()

在小说阅读器中沉浸阅读

### 01 漏洞背景

在 Dify 受影响版本中，`/console/api/workspaces/current/model-providers` 相关接口未对返回的敏感凭据进行脱敏处理。这意味着只要拥有合法的登录会话（Session），即可绕过前端显示逻辑，直接从后端接口调取核心资产信息。

* •

  **风险等级：** 高危
* •

  **涉及信息：** API Key、Secret Key、Base URL 等
* •

  **受影响版本：** v1.10.1 及以下版本

---

### 02 漏洞接口格式

漏洞路径为 Model Providers 列表接口

> `GET/console/api/workspaces/current/model-providers`

---

### 03 漏洞验证流程

#### 仅支持通过管理员安装并配置自定义模型插件（OpenAI-API-compatible等）来获取 Provider 列表中的 API 密钥；系统预置的预定义模型（硅基流动等）暂不支持该功能。

```
GET /console/api/workspaces/current/model-providers HTTP/1.1
Host: 192.168.2.132
Content-Type: application/json
X-CSRF-Token: {csrf_token}
Cookie: access_token={access_token}; csrf_token={csrf_token}
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kicAxkky0Cy2qR7qKvIoicRUTn5nVbKbClb3fWEGKroTKibcdgGuwKOwQvWwvhfw8YmFrEeEIzaBdhCiayZmwAw6Xw/640?wx_fmt=png&from=appmsg)

### 04 安全修复建议

1.为了保障您的模型资产安全，建议立即采取以下措施：

2.版本升级： 请尽快联系运维人员，将 Dify 升级至最新的稳定版本，新版本已对该接口进行了脱敏处理。

3.凭据重置： 如果您的 Dify 实例曾暴露在公网且版本处于风险范围，建议立即在模型供应商后台重置（Rotate）所有的 API Key。

4.安全加固： \* 使用 WAF 限制 /console/api/ 路径的异常访问。

5.为 API Key 设置使用额度限制和来源 IP 白名单。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/kicAxkky0Cy1l079HTZ06SIeNFIpENwuAxwa7JhYX6iaXHVGAViarFdGdpHmsXg9EdbuJ46ru7NVpMwP7ldiaHewdg/0?wx_fmt=png)

貔瑞安全实验室

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/kicAxkky0Cy1l079HTZ06SIeNFIpENwuAxwa7JhYX6iaXHVGAViarFdGdpHmsXg9EdbuJ46ru7NVpMwP7ldiaHewdg/0?wx_fmt=png)

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