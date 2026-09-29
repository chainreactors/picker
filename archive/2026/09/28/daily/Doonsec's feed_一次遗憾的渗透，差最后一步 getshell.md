---
title: 一次遗憾的渗透，差最后一步 getshell
url: https://mp.weixin.qq.com/s/sXa7B3s81JonmYOIqqbrUg
source: Doonsec's feed
date: 2026-09-28
fetch_date: 2026-09-29T07:38:21.808288
---

# 一次遗憾的渗透，差最后一步 getshell

# 一次遗憾的渗透，差最后一步 getshell

原创

private null
private null

轩公子谈技术

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

这是一次真实环境下的外围打点复盘。过程不算顺，甚至有点折腾，但最后发现的那个"目录穿越"漏洞，配合文件上传，本可以一击毙命——却因为目标环境的一个限制，最终遗憾收场。整个过程记录下来，给同样在路上挖洞的你一个参考。

一、开局不顺：资产是个"空壳"

拿到目标资产，第一件事自然是打开看一眼。

结果点进去是个 H5 页面，前端框架渲染出来了，页面结构也有，但数据全是空的——接口似乎没有返回任何有效内容。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/16lHuWzRRduBzLawfh7kp6q1bUfBBX46gLyS8La5y5OQiciaVhMXvibdiaP4N71SxOJsYMZatR5YTrvaHR1ZLicmBvgmcsqB7HTR5iaSsn84iaO10k/640?wx_fmt=png)

这种"有壳无肉"的站点，常规的接口枚举思路基本走不通。想着既然是 Vue 做的，顺手拼接一下 Vue 路由试试，结果直接报异常。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/16lHuWzRRdtNV15MPJSSDvKEC18x5FA7Ug6uBVUoSRw0wR78AicUfGv5qeFc6BL5enoJ6MgNuOAE7GERFe2UwVvpl9hL419eOTVgpquqLia2k/640?wx_fmt=png)

前端这条路暂时堵死了。

二、换个思路：脚本批量探测出路

既然手动看不出来，那就上脚本批量探测。一轮目录/路径扫描下来，还真扫出来一个上传页面。

![](https://mmbiz.qpic.cn/mmbiz_png/16lHuWzRRdu9AVtgicYYMbxtKIWZYK5M62SxZpVniaJZ5hk1hjkiaWjUZsRp9X7Z8DaiafCHfrSsTrIbVMKkNPpGKFxlmibMx8JheibiaJerocFjug/640?wx_fmt=png)

上传点对于打点来说是个高价值入口，先别急着激动，看看能不能传、传什么。

三、上传点摸后缀：uploadfuzz 登场

直接尝试上传文件，看返回。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/16lHuWzRRdtncxcGmomSnqK7cQWNJsTdZhZkEIA50amleKgf7OVzPx1lSBXIzM39HVZB6RTGLjLpZkgxE5APiccMO0lAAMyX5uyGGcYfduRs/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/16lHuWzRRdszHWkC04q0bpH8Wgtoqd4RzFxqGeialFVsW5bchlN2cF9JiaITMZMRb6Tia4Ewrz9oLVpQoMEfADSYzZIxQNPzNynEvrUSiblZMXE/640?wx_fmt=png)

这里开始上工具。用 uploadfuzz 对上传点做了一轮后缀 fuzz，结果有点微妙：

•jsp 能返回成功，说明后端接受了这个后缀；

•但传上去的 jsp 不解析，无法执行代码；

•折腾下来，只能上传 html。

![](https://mmbiz.qpic.cn/mmbiz_png/16lHuWzRRdvjAekLIJOMEurBB6dVmn6k8zl3zibyrVl6Lx5oBcEG1Kgllny3aTAOd1h7PveIPmOah4KRAMk41UgMML0qWO05IVfeGLmibPqYs/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/16lHuWzRRdt93aXxzoS30icllHQiaf754q4sLSW0ux5jN7UX35gN88hT9WUUQE9M70CzN5U9t8gvxXvbaeEgSuK02ibvYdpKt5doXvqPntM2fs/640?wx_fmt=png)

这就很难受了。上传点明明在手里，jsp 也能传成功，却因为目标把上传目录配置成了不执行脚本（静态资源目录 / 非 Servlet 解析目录），导致"传得上去、跑不起来"，getshell 的第一条路被封死。

四、转移战场：rad 爬虫翻接口

上传这条路走得磕磕绊绊，先放一放，回到 Web 侧用 rad（熊猫头）爬虫深入爬一遍，看看有没有别的接口可以捡漏。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/16lHuWzRRdsic6tD66OcqJY2MdDrdJyzX37zicicoKn9fhEwScvUOyQokjaZWK5tpx30XxwicdtBcDT1zkr2ibicmicEdQmCBEPUaNk0KAkaDzrfkY/640?wx_fmt=png)

爬了一通，结果很打击人——全部 404。要么是路径藏得太深，要么就是这套站点的接口确实不多。

五、峰回路转：上传接口的文件读取

绕了一圈没收获，又回到上传接口。既然能上传，那这个接口背后大概率是一个文件读写的逻辑，会不会同时存在文件读取的入口？

于是试着在上传参数里塞路径，看能不能读出文件。第一次直接构造，结果是 404。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/16lHuWzRRdtp5OlxRcYBBcNMRw8b3r8HCo8URib05wDRoficZRAPZhUN1GuooKiaq8pCmL42ib1UaBnhntgLdiaPAgp4GCMjuO1iatIw4INcc9DRA/640?wx_fmt=png)

404 不代表没戏，反而说明后端对路径做了某种过滤/限制——有校验，才值得继续挖。

琢磨了一会，换了个姿势：保留一级目录前缀，再在后面拼 ../ 试试。

![](https://mmbiz.qpic.cn/mmbiz_png/16lHuWzRRdtKUYdzIDfjmcrbEPBI7ujUpRe7LnibNhmkTRWTO1icXIOmzBcgiaswWibQOPVhXMiaKUxVJSak9t7wharcXq2hPYN1TDmBCvIP0DqQ/640?wx_fmt=png)

结果，成了。

六、漏洞根因：startsWith 校验形同虚设

回头复盘，这里的核心问题就一句话：后端对用户可控的路径，只做了字符串前缀校验，没有做路径规范化。

推测后端代码长这样：

if(!userPath.startsWith("/aaa/")){
    // 拒绝访问
    return;
}

这个校验看起来"限制了目录只能落在 /aaa/ 下面"，但其实是个很典型的绕过点。

我们来走一遍 sink-source 调用链：

1. Source（用户可控输入）

上传接口里，文件名 / 路径参数（比如 filename 或 path）完全由攻击者控制，攻击者可以传 ../../、../ 这类路径片段。

2. 校验层（失效的过滤器）

if(!userPath.startsWith("/aaa/")){
    return;
}

String.startsWith() 做的是纯字符串前缀匹配，它不关心这是什么路径、也不做规范化。所以当你传：

/aaa/../../etc/passwd

的时候，这个字符串的前缀确实是/aaa/，校验直接通过。

3. Sink（危险的文件操作）

校验通过后，路径被拼接到基础目录上，进入真正的文件读写：

File file =newFile(baseDir + userPath);
byte[] content = Files.readAllBytes(file.toPath());// 或 FileInputStream / FileOutputStream

Java 的 File / Path 在解析路径时，会做 . 和 .. 的规范化——/aaa/../ 会被解析为回退一级目录，最终定位到 baseDir 之外的真实路径。

于是：前缀校验通过了，真实读写却已经穿越到了任意目录。

这正是一开始直接拼路径 404、而"保留一级目录再拼 ../"成功的原因——绕过这个 startsWith 校验后，就拿到了任意文件读取的权限。

七、遗憾在哪？

到这里，其实已经拿到了一个很漂亮的洞：文件上传 + 目录穿越 = 任意文件读取。

但遗憾也就卡在这：

1.jsp 不解析。上传点虽然能接受 jsp，但上传目录被配置成不执行脚本，导致无法通过上传直接 getshell；

2.只能传 html，价值有限，最多想到 XSS，但影响面小；

3.任意文件读虽然拿到了，却没能在有限时间内把它进一步链接成 RCE（比如读到数据库配置/密钥后打内网，或者配合其他点在落地）。

离 getshell 就差这"临门一脚"，却因为目标环境的一个限制被拦在门外。这也是为什么我把它叫做"一次遗憾的渗透"——洞是通的，利用链是断的。

八、总结与防御建议

攻击侧复盘：

•资产"空壳"不代表真没接口，脚本批量探测兜底，往往能捡出隐形的上传/管理入口；

•上传点不能执行脚本时，别死磕 getshell，留意接口背后是否还存在文件读取/任意文件操作的逻辑；

•遇到 404 别急着放弃，404 往往意味着"有校验"，而"有校验"就有绕过的空间；

•目录穿越的姿势很多，startsWith 前缀校验是最常见、也最容易绕的一类。

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/BAby4Fk1HQZCDnChGupgZyfRK8Bs8twy3rbw6gic8GAoiaqoIIVarKvqMgQ1vj4t0UyMNdvaIHmTE2XgzeSFn32Q/0?wx_fmt=png)

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