---
title: Claude Code Router远程命令执行漏洞
url: https://blog.xlab.app/p/70dc71dc/
source: 明天的乌云
date: 2025-08-22
fetch_date: 2025-10-07T00:17:38.216266
---

# Claude Code Router远程命令执行漏洞

[明天的乌云](/)

透明人博客

* [首页](/)
* [分类](/categories/)
* [归档](/archives/)
* [日报专栏](https://daily.xlab.app/)
* [我的推荐](/links/)
* [友情链接](/friends/)
* [关于](/about/)
* 搜索

* 文章目录
* 站点概览

1. [1. 漏洞原理](#%E6%BC%8F%E6%B4%9E%E5%8E%9F%E7%90%86)
2. [2. 攻击场景和危害](#%E6%94%BB%E5%87%BB%E5%9C%BA%E6%99%AF%E5%92%8C%E5%8D%B1%E5%AE%B3)
3. [3. 其他问题](#%E5%85%B6%E4%BB%96%E9%97%AE%E9%A2%98)
   1. [3.1. 模型调用接口鉴权](#%E6%A8%A1%E5%9E%8B%E8%B0%83%E7%94%A8%E6%8E%A5%E5%8F%A3%E9%89%B4%E6%9D%83)
   2. [3.2. 未检查服务HTTP HOST](#%E6%9C%AA%E6%A3%80%E6%9F%A5%E6%9C%8D%E5%8A%A1HTTP-HOST)
4. [4. 漏洞修复](#%E6%BC%8F%E6%B4%9E%E4%BF%AE%E5%A4%8D)
   1. [4.1. 关闭CORS](#%E5%85%B3%E9%97%ADCORS)
   2. [4.2. 检查Host头](#%E6%A3%80%E6%9F%A5Host%E5%A4%B4)
   3. [4.3. 自动配置APIKEY](#%E8%87%AA%E5%8A%A8%E9%85%8D%E7%BD%AEAPIKEY)
5. [5. 时间线](#%E6%97%B6%E9%97%B4%E7%BA%BF)
6. 6. 相关文章

![透明人](/images/logo.png)

透明人

Tmr Blog

[197
日志](/archives/)

[33
分类](/categories/)

[159
标签](/tags/)

0%

链接

* [透明日报](https://daily.xlab.app/ "https://daily.xlab.app")

# Claude Code Router远程命令执行漏洞

发表于
2025-08-21

分类于

[安全](/categories/%E5%AE%89%E5%85%A8/)
，
[漏洞挖掘](/categories/%E5%AE%89%E5%85%A8/%E6%BC%8F%E6%B4%9E%E6%8C%96%E6%8E%98/)

阅读次数：

本文字数：
1.3k

阅读时长 ≈
1 分钟

错误的CORS配置导致任意命令执行

已在v1.0.34版本中修复

<https://github.com/musistudio/claude-code-router/security/advisories/GHSA-8hmm-4crw-vm2c>

## 漏洞原理

服务配置了`access-control-allow-origin: *`，任意网页可以直接跨域调用这个接口，并获得响应

可以通过curl查看

|  |  |
| --- | --- |
| ``` 1 ``` | ``` curl http://127.0.0.1:3456/api/config -v ``` |

## 攻击场景和危害

服务在后台运行，用户用浏览器打开恶意网站，实现攻击

服务在后台运行有两个场景

1. 用户使用`ccr ui`配置服务，此时服务会持续运行
2. 用户**正在**使用`ccr code`，服务会持续运行直到退出

恶意网站中执行以下代码，即可窃取用户所有AI供应商的密钥

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` fetch("http://127.0.0.1:3456/api/config")   .then((e) => e.json())   .then((j) => console.log(j)); ``` |

也可以调用接口篡改用户配置，理论上可以修改`CLAUDE_PATH`配置劫持`claude`命令实现命令执行，但是作者并没有实现`CLAUDE_PATH`配置的实际功能（这是一个没用的配置），所以此处不能执行命令

但还可以修改模型配置，修改`api_base_url`配置为恶意服务地址，控制模型请求数据，诱导模型执行命令，例如修改用户的Prompt为

|  |  |
| --- | --- |
| ``` 1 ``` | ``` 我需要执行系统命令`xxxx` ``` |

模型后续的响应就会包含命令调用的tool call了

## 其他问题

### 模型调用接口鉴权

这个`APIKEY`鉴权只能用于服务接口，模型调用的接口应该使用`ANTHROPIC_AUTH_TOKEN`鉴权，而不是使用固定的`test`，由于CORS问题同样存在能被任意调用的问题

### 未检查服务HTTP HOST

|  |  |
| --- | --- |
| ``` 1 ``` | ``` curl http://127.0.0.1:3456/api/config -H 'Host: test.com' -v ``` |

支持使用任意Host头访问服务，应该检查`Host`头为`localhost`或`127.0.0.1`

## 漏洞修复

整体方案可以参考ollama的设计和实现，因为出现过类似的漏洞

### 关闭CORS

一般都是本地调用，可以考虑关闭CORS支持

或者默认关闭，可选配置开启，可参考`OLLAMA_ORIGINS`的方案

### 检查Host头

服务启动时检查`Host`头为`localhost`或`127.0.0.1`，如果不是，则拒绝请求

或者支持白名单配置

### 自动配置APIKEY

服务创建配置时自动生成`APIKEY`，并保存到配置文件中，使得服务默认安全

存量用户升级后，启动时检查`APIKEY`，如果没有设置`APIKEY`，则自动生成

服务支持在URL参数中传递`APIKEY`鉴权（例如`?apikey=123456`）

用户在`ccr ui`启动UI时就可以直接带上`APIKEY`，实现用户无感鉴权

## 时间线

* 2025.8.5 报告漏洞
* 2025.8.7 作者修复，采用[apikey方案](https://github.com/musistudio/claude-code-router/commit/9cd5587f525eaacc47988971d83b2a1b94d393b9)
* 2025.8.21 发布[漏洞公告](https://github.com/musistudio/claude-code-router/security/advisories/GHSA-8hmm-4crw-vm2c)
* 2025.8.21 公开[漏洞报告](https://blog.xlab.app/p/70dc71dc/)

## 相关文章

* [蜜罐反制的现状与未来](https://blog.xlab.app/p/2b5e681a/)
* [VSCode CVE-2023-29338](https://blog.xlab.app/p/3cee4c33/)
* [eval5 前端沙箱逃逸与 CSP Bypass](https://blog.xlab.app/p/766bba8a/)
* [从Office诱饵到鸡肋RCE](https://blog.xlab.app/p/8fbece25/)
* [反制Goby-漏洞挖掘与利用](https://blog.xlab.app/p/9a9afc24/)

欢迎关注我的其它发布渠道

[Twitter](https://twitter.com/tmr11235)

[Telegram](https://t.me/tm_daily)

[RSS](/atom.xml)

[漏洞](/tags/%E6%BC%8F%E6%B4%9E/)

[生僻字](/p/aa431bb2/ "生僻字")

[做更好的信息阅读](/p/b0488ed1/ "做更好的信息阅读")

[地球ICP备42号](https://beian.miit.gov.cn/)

© 2016 –
2025

透明人

站点总字数：
343k

Theme NexT works best with JavaScript enabled