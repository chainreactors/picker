---
title: SmartBi后台远程代码执行漏洞简单分析
url: https://mp.weixin.qq.com/s/WAmdll1HwytOICUo5iILWA
source: Doonsec's feed
date: 2026-05-22
fetch_date: 2026-05-23T05:37:49.360119
---

# SmartBi后台远程代码执行漏洞简单分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/vOGOib9z4Wz4fl0IBseVZ2A7Feuz0rHHys6oWDMYgkO7jTSuEZsY4Tj7VSaTapPict13ialu7mNKfq3TKPMUxjYEQ/0?wx_fmt=jpeg)

# SmartBi后台远程代码执行漏洞简单分析

原创

莫大130
莫大130

安全逐梦人

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

简单复现一下SmartBi漏洞

影响版本`Smartbi <= 11.0.99471.25193`

## 环境搭建

### 需要的环境

* • 源代码一套（最后给出源码）
* • sqlserver 2016

源码文件结构

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vOGOib9z4Wz4fl0IBseVZ2A7Feuz0rHHyXmLYO2ugibydLYhNFiclz5IEFpPoI428yrnU0qTswID7ol7Y5ytzD4pg/640?wx_fmt=png&from=appmsg)

运行`tomcat\bin\startup.cmd` ,环境就会启动，第一次运行会要求填入sqlserve数据库账户密码

## 代码分析

### 分析jar

搜索jar中存在的关键字 `MetricsModelForVModule` 和 `checkExpression` ，Smartbi-SmartbixSmartbi.jar 中发现该类。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vOGOib9z4Wz4fl0IBseVZ2A7Feuz0rHHy4aSAu3Ej3uNsD3IyTye5rV80u3yXJZ2nIfeSZPPvknZzXgSf441qNw/640?wx_fmt=png&from=appmsg)

使用jd-gui反编译`Smartbi-SmartbixSmartbi.jar`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vOGOib9z4Wz4fl0IBseVZ2A7Feuz0rHHyp0yvO7gBtI3ibgOduX2uh6kaUpibG8gXD8GkmJiagGCzfpZSTYzV2ZEuA/640?wx_fmt=png&from=appmsg)

### 分析触发漏洞点

`checkExpression` 方法 使用了 ScriptEngineManager类 ，ScriptEngine 是一个标准的API（定义在 javax.script 包中），它允许Java程序在运行时嵌入、解析和执行用其他脚本语言（如JavaScript, Python, Ruby等）编写的代码。

```
  public Boolean checkExpression(String nameExpression) {
    StateHolder.toSmartbiX();
    ScriptEngineManagerengineManager=newScriptEngineManager();
    ScriptEngineengine= engineManager.getEngineByName("js");
    try {
      nameExpression = nameExpression.replaceAll("\\[[\\u4e00-\\u9fa5_ a-zA-Z0-9.]*\\]", "(6)");
      engine.eval(nameExpression);
    } catch (ScriptException e) {
      return Boolean.valueOf(false);
    }
    return Boolean.valueOf(true);
  }
```

ScriptEngine.eval() 函数是一个极其危险的函数，会导致命令执行漏洞。

## 漏洞复现

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vOGOib9z4Wz4fl0IBseVZ2A7Feuz0rHHyc6WN9fLwjJlY5dLdwvEWNUM6HGJPJUF1pjZfhickeRGNRwjkuvElQlA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vOGOib9z4Wz4fl0IBseVZ2A7Feuz0rHHyEJM4GCv2AjkMziaB323On1viaExiatFwOwu4TO4rU0qnfnJvUTd74nJdw/640?wx_fmt=png&from=appmsg)

后台回复： `20250827`

## 参考

* • [https://mp.weixin.qq.com/s/aIyGt5OKlYCL-NPfd0G2Jw?scene=1&click\_id=24](https://mp.weixin.qq.com/s?__biz=Mzk0NTQyMjk4Ng==&mid=2247484370&idx=1&sn=be428ab626a8dfdf968d1dc50aab0c27&scene=21&click_id=24#wechat_redirect)
* • https://mrxn.net/jswz/smartbi-authcation-bypass-rce.html

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/vOGOib9z4Wz4WtqwyhjPBg0sibeh77pYj6UtsnINUMt1GX8r79gczh4Tmf7LH2ELB0NZibNjackdUQuLcZukVgSog/0?wx_fmt=png)

安全逐梦人

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/vOGOib9z4Wz4WtqwyhjPBg0sibeh77pYj6UtsnINUMt1GX8r79gczh4Tmf7LH2ELB0NZibNjackdUQuLcZukVgSog/0?wx_fmt=png)

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