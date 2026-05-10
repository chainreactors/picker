---
title: Ai+burpsuite插件实现自动化漏洞挖掘图文
url: https://mp.weixin.qq.com/s/Gt8ov9ZvNiN6_HM6zhfUaw
source: Doonsec's feed
date: 2026-05-09
fetch_date: 2026-05-10T05:33:22.262125
---

# Ai+burpsuite插件实现自动化漏洞挖掘图文

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ic8BH9EFusn7DyX38spfWUUvZhvCqqySuPZZQnXVte3a7wO93iadypRBgTA6s1yRsm1hhxG3c5qx73iafq9MEIdURD2wvhgPuMR0icNZzUr3Tmw/0?wx_fmt=jpeg)

# Ai+burpsuite插件实现自动化漏洞挖掘图文

原创

三呼呼
三呼呼

古月安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

### 使用小龙虾[kali+openclaw+qq机器人实现自动化安装图文教程](https://mp.weixin.qq.com/s?__biz=Mzk5MDI5NDAyMw==&mid=2247485871&idx=1&sn=b20a8f664110edc9321334518289a540&scene=21#wechat_redirect) 从这里开始。当然可以换成其他工具

### 比如直接使用opencode(https://opencode.ai/)。

### 添加 MCP 工具

默认情况下OpenClaw 本身不支持直接调用 MCP 协议，但可以通过官方推荐的`MCPorter`工具作为中间层来接入外部 MCP 服务

#### 安装 MCPorter

打开终端，使用后面的命令进行安装：npm i -g mcporter，如果提示命令未找到，需要检查 Node.js 环境变量或重新安装node.js。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ic8BH9EFusn7Mwd3kzl6gZAUQibTwur9hzaLvatq88AeNHSiaSWicFttic80CDxJhZjibY9WK2cBCad42mmHEOXARjMs2mjdtOC0Ok0uwXQOORWVo/640?wx_fmt=other&from=appmsg)

#### 配置 MCPorter

安装完成之后，就需要配置mcp服务了。

```
mcporter config add <service-name> --url <mcp-service-url>
```

将 <service-name> 替换为自定义名称，<mcp-service-url> 替换为 MCP 服务地址（如 Burp MCP 的 http://127.0.0.1:9876/sse）

bp-mcp服务下载地址：

https://github.com/six2dez/burp-ai-agent/releases/tag/v0.6.0

![](https://mmbiz.qpic.cn/mmbiz_jpg/ic8BH9EFusn70wbML1URLSzyLVgVE8r3J1xPrPWPs4q4KmKdAzSTsCgPST9Z5bo8eZtzDicwug6nQI1XBictlxss3f5E7pe7gricWwokLsEV8n0/640?wx_fmt=other&from=appmsg)

**burpsuit AI Agent接入**

接下来可以在openclaw.json中加入mcp服务，当然也可以让Agent帮我们完成，比如通过聊天：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ic8BH9EFusn4Ij8iajd4ZzkIsicjkLNdTFI9Vkq2kfPKqCI2icLQWYUDjA3P5qlHfY5ic5ttSKKALgFYzhLk7RDQibnicJNQgnlktXJIjUVbPrJSIQ/640?wx_fmt=other&from=appmsg)

完成添加，在openclaw.json中查看：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ic8BH9EFusn4qPC7B7qJFh0Tjo5e2shNskurzGHDWz3srenWvwBf4MZw1nafWEDAGMMu3OibzD6vadQgArJb55KmfXTF4664ia5YLxIrPUibQ2E/640?wx_fmt=other&from=appmsg)

这样就完成了一个burpsuit的mcp工具，该工具可以自动进行漏洞挖掘，具体可参考上面github。

现在来启动这个burpsuit的AI插件。首先是下载：https://github.com/six2dez/burp-ai-agent/releases/tag/v0.6.0

然后在burpsuit的extensions中添加：选中下载的jar文件即可--前置条件java version 21+

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ic8BH9EFusn60lgRICjjTVgFIFmaA0cdMYeRz0wOjicZopFVdN9vNaKxIibhT4xkLBCs9YUooOyREVEXibk6LpOWusPyhl7aoiabOU00ZrJthop0/640?wx_fmt=other&from=appmsg)

启动之后是这样的：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ic8BH9EFusn6q8hIz3WCK7AEymtCjyniaZs03Exs1LPLibvslUG2jUxzVjQnVyo8Y6s5rG4C0kvxS0iaI0sqibgzbHqUc4I4U9SqKCV5UeDPvfw8/640?wx_fmt=other&from=appmsg)

但是有很多模块是未开启状态，可根据自己得需求开启，但是有一定得风险，一定要确保操作可控

![](https://mmbiz.qpic.cn/mmbiz_jpg/ic8BH9EFusn7pllrXl9peJ2hlvBxujLRBdtAmaaOR7qNCap3B6UPcjUDg7XcAbGH9IJ28BkAdKAEPmEkdMcibF3sqrKU7baE2NwltiaYGWd7kA/640?wx_fmt=other&from=appmsg)

表示成功启动了mcp服务。现在尝试让小龙虾通过mcp服务，调用burpsuit进行自动化的渗透测试。现在聊天框中看下连接成功没：直接问是否可以连接burpsuit的mcp服务

![](https://mmbiz.qpic.cn/mmbiz_jpg/ic8BH9EFusn7KEc2pRTpaX4Vroz6S0dEkUs1Algpk3Ticquo7GibAialiaqUyUZP6nOgQaHBUavHOPrdYNNFosxT4T7VhrbW8ZxblT3BohOOyF5Q/640?wx_fmt=other&from=appmsg)

**bp自动化**

得到结果，现在我们通过qq机器人的方式来进行调用。现在启用一个测试网站，然后代理设置好，并且访问下，让burpsuit抓取到这个站点的流量。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ic8BH9EFusn7kibQmnic6rtiaX7x2KSakMHup8arJI1Jj7chD4DlkLyDKhnrynWeVspM8AYqeVa9lwhYXicibRybiaHCtlpb5xMWMXYRc7HBXQ86ec/640?wx_fmt=other&from=appmsg)

然后发起测试流程

![](https://mmbiz.qpic.cn/mmbiz_jpg/ic8BH9EFusn4otsibz4R2CrBEx9dbNKrX79gDk5MA7ljrdLaXRpoeod2BsCNuWm8ibxf6y6pmwfBlvAAjRiay96rNAMCRdOgw0IR3DBlsSAe6FI/640?wx_fmt=other&from=appmsg)

等几分钟之后结果：

![](https://mmbiz.qpic.cn/mmbiz_jpg/ic8BH9EFusn6fic4IGzvbZT79zvGY1eFHKOCbSBYoOXcWAajicW6MxickZc1ywibMWSFPhK9wMjUrkFFlSCXCz0WMfN4NUX1nyBFzFSLwI1ziaI9s/640?wx_fmt=other&from=appmsg)

发现弱口令进一步测试

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ic8BH9EFusn58vDRYRATVjN4ygBBtxvSJLHgvormT1jlUMIhbGgFHCYBsBNaf9wVtFrDic10d5GsDRB90qdMzXmJQ5M4icFITKib3nXhkJ0jvgI/640?wx_fmt=other&from=appmsg)

因为不是所有的的测试步骤都会返回，我们看看返回的一些关键内容：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ic8BH9EFusn6CggliaCOGIjsiaeicEgJTea7Slgn06TRsnAJ5ZI6sib0zM6MoiajEDppM3ZCRaFQ76KHcfPRPzTaDPeQ3fXjiavlE0AEmmG6bz6poo/640?wx_fmt=other&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ic8BH9EFusn5aYUQ91JWNU95n7KHsOIrick3abX5FCYibHkWW3aO0qaJFTlibmtyBsJibKnWHsnKg9YpuiacT4UptXJicSYtFoYUraoF0FV4Zia1Xow/640?wx_fmt=other&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/ic8BH9EFusn6FQqByDHYBoib9H26nyeOE7PljDcBnV9ZCMJI6V3mPoWokU5qtfoYwVE5ibibL7OZ42L5ZicXia0NrNj2s3eUvrFpxV6icsp6yteY6k/640?wx_fmt=other&from=appmsg)

写入成功，然后几分钟之后测试结束得到如下结果：

![](https://mmbiz.qpic.cn/mmbiz_jpg/ic8BH9EFusn4Ndm0bicQV5s29vicRnYeYwOg8kLXm8XZndDnQibFMCciaoW1hoxIE7XtjZP4QSE033liaudlLO7YqnFKHQyJwlz6Ly7wQ2azUYzLw/640?wx_fmt=other&from=appmsg)

然后我们通过它给的shell路径看看：成功执行。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ic8BH9EFusn5OXkBJthspicuS2NVKib8U4QK2WxCn6xDUJpNKdFd5UEpiam3RiavEhgD5jFFqumSy0iaqibzDeFc0gp0I934rgoXlysz3bAzttAdOY/640?wx_fmt=other&from=appmsg)

到这里就基本上结束了小龙虾加burpsuit ai agent的组合使用。现在就可以通过qq机器人发送url地址，然后等着结果了。

当然你可以把他做成一个skills，比如这样，直接在聊天窗口中说就行，将这个mcp 做成一个skills，小龙虾就会帮你完成：

![](https://mmbiz.qpic.cn/mmbiz_jpg/ic8BH9EFusn7DUQTO4j0Fkc4lAvdnNlAlprr1ThEKdlj2EcnZY0kO7nM9z6c1NR1BaaIEKOHCUTvEuVYt92tSCXCeib4Ot7JU7icyVianic65icVs/640?wx_fmt=other&from=appmsg)

但是这个MCP工具并不是全自动化的，它是个半自动化的，它需要根据你的burpsuit中已经存在的http请求来进行测试。也就是我们要先通过代理在抓包到需要测试的URL的流量，才能让它帮我们进行分析。如下图：

![](https://mmbiz.qpic.cn/mmbiz_jpg/ic8BH9EFusn6Gr7qBpibd6Q0IDsBBK1pKiahd6qaSq7oEViaPkiclibX7IG0O9k2vu0R840g2s4r21aw6etwbibRsyYVvRbuwNJiaV1H5E2uK6VbdME/640?wx_fmt=other&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ic8BH9EFusn6YsCqicjs1Pta0nJXkjCUib9CbDj301AF6vgKHIjol4K4Kbk4uTA7xD65lDtPILmlFneO4vwDHkL3RsWqmZZ1F3Wyibs5Rfp8zAU/640?wx_fmt=other&from=appmsg)

如果需要全自动，还需要接入浏览器的MCP，让AI控制浏览器，自动访问，点击，burpsuit抓包，然后burpsuit的ai agent才能进行漏洞测试。比如这样：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ic8BH9EFusn57hhsETmkumtFuL504fFz5Rw3Q14oL1ZhncWRia8XQABvaFNwpHxErulhayt5iaFhz7iajzu6LGS6PCkNoKZrHibdGppg4F63UXc4/640?wx_fmt=other&from=appmsg)

就可以自动化得到一个skills

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ic8BH9EFusn6DK5JMGQ5He45w4nz9DNc7D5Q4AG4ibW0OhAufVXXwlmpLqJQKGJnBShfJ3FqAnK11dAP7Kr8Lvr9uezicTuoCUkuOkVlWxKkzA/640?wx_fmt=other&from=appmsg)

现在再来试试这个skills得效果。

启动测试

![](https://mmbiz.qpic.cn/mmbiz_jpg/ic8BH9EFusn6QEEwGflgdibzUvc3LuXjwSO8RSdNOLX9tlLG4XNFUXAptn8VNUEF6jibZMAMZicKSo8wUMiaFYiaBuW0YoHAFhuVoeXIcMUecgEOQ/640?wx_fmt=other&from=appmsg)

得到第一阶段结论：

肯定不够得继续：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ic8BH9EFusn4PjxotfOOj0uZaEVhHvCoAibo9USygIyxhozhOSX2cfATgicXwicUaushwLlUJQ1NpRUkn61d78VsyWAut9URkfssKJ2sZXwQ0Lw/640?wx_fmt=other&from=appmsg)

最终拿下系统权限。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ic8BH9EFusn5hSTm7tbjb5qEDkzcAObODWa6KBtQp2ygfQRc86MKxI5iccZhT2UeAk0JzMSLDHgy2Ko70pw55LZZxvlAUEDg0LXXtwicQNtmtM/640?wx_fmt=other&from=appmsg)

当然这些其实都可以写在skiils得.md文件中，比如当发现弱口令自动登入，进行下一步测试，就可以不用持续对话。

总结

AI能力逐渐增加，对于我们安全从业者来说，学会如何利用AI提升效率以及漏洞得检出率才是下一步得关键。如何整合各种现有工具，让他们拥抱AI，解放双手，比如上面得例子，基本不用任何代码，纯靠提示词就能完成各种配置，并能自动化得完成渗透测试任务。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/ic8BH9EFusn6laib0NayIA3gCkJG6mXnQgRoISeSA6PicZWZsLHEiawqxREwpue5KlIIR4KVxibNywk55dfAFq4AGt6X47bsmK8ibAiaqTHdIBHVmI/0?wx_fmt=png)

古月安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/ic8BH9EFusn6laib0NayIA3gCkJG6mXnQgRoISeSA6PicZWZsLHEiawqxREwpue5KlIIR4KVxibNywk55dfAFq4AGt6X47bsmK8ibAiaqTHdIBHVmI/0?wx_fmt=png)

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