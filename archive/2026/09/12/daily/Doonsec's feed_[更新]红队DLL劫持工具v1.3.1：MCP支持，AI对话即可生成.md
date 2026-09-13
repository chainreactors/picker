---
title: [更新]红队DLL劫持工具v1.3.1：MCP支持，AI对话即可生成
url: https://mp.weixin.qq.com/s/zijrAB_gKIG74znpDU5c8A
source: Doonsec's feed
date: 2026-09-12
fetch_date: 2026-09-13T06:58:26.750861
---

# [更新]红队DLL劫持工具v1.3.1：MCP支持，AI对话即可生成

# [更新]红队DLL劫持工具v1.3.1：MCP支持，AI对话即可生成

原创

陆安予
陆安予

白帽子安全笔记2.0

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

## 一、这是什么？

这是一个高级红队演练工具，用于自动化实现DLL劫持相关技术，这次更新将带来AI支持的部分，门槛从0再次降到0，没有人比你更懂DLL劫持。

本次更新内容如下：

* • 1.MCP接口

## 二、更新细节

### 1.MCP支持

1.菜单栏-MCP服务-启用之后，工具的全部能力（包括解析、生成编译、远程注入、混淆等都可以由支持 MCP 的客户端（如 Claude Code、Claude Code Desktop）直接调用，不再需要人工在界面上逐步操作。

![MCP服务](https://mmbiz.qpic.cn/sz_mmbiz_png/ibXL9MCj2GqOCPJcrJBSbVTdjWjaOCAWFcDe6l8QbCkEsCG6f8hk6iaKiccMHYDN1kcr45icdC8Mxt6Abib41XicVuoP0CLcNwobBEp4Ntjbne8M8/640?wx_fmt=png&from=appmsg "null")

MCP服务

2.第二步，复制配置:

![MCP配置](https://mmbiz.qpic.cn/sz_mmbiz_png/ibXL9MCj2GqO2yia1ALWTtaLdSljj6PRYWoRJygFuibmgWgUdVYrXECVK8HXXf5CP8prtmUG5kwQuLaL70rCvLzy99wffdb48jj3v1kkuhBiazo/640?wx_fmt=png&from=appmsg "null")

MCP配置

3.接下来新建.mcp.json文件或加入其中即可

```
1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

{
  "mcpServers": {
    "burp": {
      "command": "java",
      "args": [
          "-jar",
          "C:\\Users\\rapid\\AppData\\Roaming\\BurpSuite\\mcp-proxy\\mcp-proxy-all.jar",
          "--sse-url",
          "http://127.0.0.1:9876"
      ]
    },
    "dll-tools": {
      "type": "http",
      "url": "http://127.0.0.1:8765/mcp"
    }
  }
}
```

接下来在Agent中说（以Claude Code为例）：

`生成一套DLL侧载我看下，exe是vlc.exe   DLLl是libvlc.dll  载荷是calc.bin`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibXL9MCj2GqOSZNCB9W7WfXg0FjJicIiap0q9tib2ejDmzysuMHB2T59x9jAOsd3ic8cK6sFZQ06l7bSlHXfcJcayzgQnlSTianTngWT8ptzaNeVw/640?wx_fmt=png&from=appmsg "null")

`使用混淆，使用注入远程进程`

![混淆与远程进程](https://mmbiz.qpic.cn/sz_mmbiz_png/ibXL9MCj2GqMajbfwRhTePBSDGLM80oAGK9fmQpJoIsnhYAoK8wc1w7EoLAw4avNRLaiaujHcFco2Rg1m2yG7ak9FvJMXpYRYia0MWAiaCZHXyw/640?wx_fmt=png&from=appmsg "null")

混淆与远程进程

或者两句话一起说，AI自然懂你的意思，它将调用工具相应功能。文件在当前目录sideload\_out下。

![](https://mmbiz.qpic.cn/mmbiz_png/ibXL9MCj2GqMMjhXQEicriczbJQGFHWLHZz7GHxgEDQ7bficdKTQIYsHpVVjNBSQtCltAEU81I7g1JHhicUkvibwV5ekkurJjHENIuRw0VyicnOSnA/640?wx_fmt=png&from=appmsg "null")

> 该版本已更新至项目目录，用户可前往下载。

## 三、总结

本次加入的MCP接口，让整套流程不再依赖人工操作，任何能连通该端口的主机都可以调用工具链。

## 四、免责声明

本文涉及方案仅限合法授权的安全研究、渗透测试用途，使用者须确保符合《网络安全法》及相关法规。具体条款如下：

1.仅可用于已获得书面授权的目标系统测试；
2.遵守法律法规，不得用于侵犯他人隐私或数据窃取；

本人不承担因用户滥用本软件导致的任何后果。使用即视为同意并接受上述条款。

---

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ibXL9MCj2GqM0QSEUqWHz3BBibqxHbxaC5wibm9paYNX1cJYtzWM4k6eibECJN0DQ2t8WFbiaPsorl4kibSB0hMqdpYmN1TTXHicgnCdSGNSomJBjI/0?wx_fmt=png)

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