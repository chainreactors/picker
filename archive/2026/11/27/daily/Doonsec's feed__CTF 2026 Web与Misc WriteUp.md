---
title: ?CTF 2026 Web与Misc WriteUp
url: https://mp.weixin.qq.com/s/9du7LbSi9oOyxkwJLFLZqQ
source: Doonsec's feed
date: 2026-11-27
fetch_date: 2026-11-28T09:40:43.767874
---

# ?CTF 2026 Web与Misc WriteUp

# ?CTF 2026 Web与Misc WriteUp

原创

星宇Sec
星宇Sec

星宇Sec

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# QCTF 2026 Web 与 Misc WriteUp

本篇汇总 Web 与 Misc 两个方向的题目。Web 部分覆盖未授权访问、JWT、文件上传、模板注入、反序列化、SSRF 与 XSS 等常见场景；Misc 部分涵盖图片与压缩包分析、流量分析、OSINT、区块链入门、二分搜索及杂项编码。

## 题目概览

### Web

* **Week 1**：[Week 1] Lain OS、[Week 1] 万界宝库、[Week 1] 向宇宙告白、[Week 1] 老叟洗完头、[Week 1] 买不到的FLAG、[Week 1] webgogogo
* **Week 2**：[Week 2] 死信局、[Week 2] 交响乐之雨、[Week 2] 小商店、[Week 2] PixelVault
* **Week 3**：[Week 3] 我的博客只有一位读者、[Week 3] DocHub 留言反馈系统、[Week3] Cowboy Bebop

### Misc

* **W1**：被揉坏的芙芙、零、斯贝家族、ezVCS、Multilingual?、压缩包、练起来~、失窃的数据
* **W2**：据说服务器很干净、中国人能飞、你跑不过我你信吗、ezIcon、Good match、ConfLeak、奇怪的邮件
* **W3**：不想读文献、LetsPR、上链，走起！！！、ezFilter、[TODO] mineGitea、magic\_png 题解
* **W4**：走丢的芙芙、阅川图书馆、Yolo 小商店 （一解）、letsdraw

## Web

### Week 1

#### [Week 1] Lain OS

源码注释：个性化预览走 /?name=<账号> ，内测演示账号是 lain。带 /?name=lain&channel=internal 请求，被 403 挡住——但 403 页面把条件直接写出来了：所需权限knight，当前权限 guest。你只要按提示给你的把cookie 换成role=knight

```
[ HTTP ]
GET /?name=lain&channel=internal HTTP/1.1
Host: 80-35df497f-ccb1-4df3-8434-871159c72033.challenge.ctfplus.cn
Cookie: role=knight
User-Agent: Navi
Connection: close
```

返回包：

```
HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8
Date: Fri, 09 Oct 2026 05:25:55 GMT
Server: Apache/2.4.68 (Debian)
Vary: Accept-Encoding
Connection: close
Content-Length: 7692
<div class="license">
<span class="license-label">授权码</span>
<code class="license-value">flag{c2b344e7-a21f-42ea-a50c-21b472b1ee12}</code>
</div>
```

#### [Week 1] 万界宝库

这道题主要考察了js代码的审计还有前端cookie的伪造题目的两个关键点是：前端公开的收益配置可以通过控制台修改；登录后的 JWT 被放在可读的 vault\_token Cookie 中，且签名密钥藏在购买到的功法内容里。登录后通过f12查看页面代码可以发现app.js中有

```
window.treasuryConfig = {
  incomePerSecond: 10,
};
```

那么我们就可以利用window.treasuryConfig.incomePerSecond = 1000000000 在前端篡改余额。接着可以通过购买地阶功法-破妄获取secret:wanjie123456接着我们尝试购买万界密藏，发现需要会员身份。

通过观察vault\_token 的值可以发现它是JWT格式，此时可以想到上面发现的wanjie123456即为密钥使用在线解析工具发现荷载数据为

```
{
  "sub": "guest",
  "name": "guest",
  "member": false,
  "role": "visitor"
}
```

将其修改为

```
{
  "sub": "guest",
  "name": "guest",
  "member": true,
  "role": "member"
}
```

再用密钥进行伪造，伪造出cookie。此时即可通过身份验证，购买万界秘藏获取flag

#### [Week 1] 向宇宙告白

起因是因为之前挖到一个和短链接系统相关的洞, 觉得很有意思于是就想把这种思路以题目的方式呈现, 但因为设计不当, 导致有点脑洞了(第一步, 进行目录扫描:

![图 001](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQrKeicwrOQ9fRTUf7ELAMn1MYlDxuLwwfWicYyy1icIlaQA8Hhb2nGJBv5Eaanx8ib5d3q5q7k2aq1zB0pfgibhJyHd525FiaibiaAJz58/640?wx_fmt=webp&from=appmsg)

图 001

可以看到比较有意思的是 /robots.txt 和/reset/reset 访问之后显示:

![图 002](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rapaL0gDxQpgkHcF06J4ACjQZQz8N1E03hOMJ1oO8INJ59PfMRDk6aCxCnpObs32jw8kXfqCbzS2KR0Vkk2gicQBTVIa5wZlXKkqqQgSK5YY/640?wx_fmt=webp&from=appmsg)

图 002

这里暂时进不去,我们先放着.

```
/robots.txt得到:
User-agent: *
Disallow: /internal/
Disallow: /admin
```

/admin 访问会显示没有权限进入:

![图 003](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rapaL0gDxQrVIoVPEVOsqGdSFTKvlO9wYMPMmbeTZ7VU5dy09BrVAb9jY1gTeDzN1pv4u4eLDRuIpdQTXiacMj98317icMjTAJ9pnyiaSJ8cM4/640?wx_fmt=webp&from=appmsg)

图 003

先任意注册一个账号进去:

![图 004](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rapaL0gDxQraDrzCGfUOVrwwxms6nFs0wfENZW8Ria1bwoZM9PDeib3xd1AFpXRL6ZeGHvEibISKxKib25jkTQgUEnKTQ2n2NcHRJadibugQ89ZA/640?wx_fmt=webp&from=appmsg)

图 004

以 http://baidu.com 为例, 这里得到了一个短链接:

```
http://localhost:8080/r/q03x
```

![图 005](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rapaL0gDxQpnK1gNsgkEZTyx8dscCNib2lcubvF0RHoiaQFqHu3xOFSia7b6mXSOCgANMYsRsiaFBtlbjzfFgeWKdpnOiaWwS391eVkVr86p3Uug/640?wx_fmt=webp&from=appmsg)

图 005

我们访问这个链接就会发现, 服务会根据这个特定的短码 q03x 从而返回一个302, 需要跳转的资源链接会放在返回包的Location头中:

![图 006](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rapaL0gDxQrNnCZ7lxptOf811kPGa7rZaD1v195cgicKlLUYGtDtibuFn3xiaSfaPuWj8A9UYJn9icHajvA5nnicJf5kGLFzHhmhwSylDP7rNkd0/640?wx_fmt=webp&from=appmsg)

图 006

在 /board 路由下会发现存在一部分已经公开的短码所对应的资源.而我们是否能通过拿到一些其他人自己知道的短码从而看到他们跳转了哪些资源?

![图 007](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQpFQgABCIAa0v2KBCD700Hjvj32iaiaAhl709KVLrv2QJBSD3icJ6eDWYkFOCcuE3d3djWLIibRcARWUy952cXTbpPsMKvibkQLJhJw/640?wx_fmt=webp&from=appmsg)

图 007

四位短码的生成规则是在0-9a-zA-Z中完全随机得到的.总共有62^4 种组合. 所以直接想通过爆破拿到所有不太现实.根据题目描述的提示:宇宙如此之大，但总有我们能够把握的一小部分。虽然我们不能枚举所有的可能, 但由于该短链接系统对应的ID太短, 且这些组合中是有一部分其实是有规律的, 也就是纯数字ID.写脚本如下去爆破:

![图 008](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQourgK15FeknWdecvibG1wiam4vNMufyjkzZl2wcF1JFOaFN5leynKHQ1l58AfwibLxs4839tdkz840LPxibLtibjachtDAZkicoLiaO8/640?wx_fmt=webp&from=appmsg)

图 008

发现7041 得到了一个之前得到的 /reset路由, 且附带了token字段.访问即可更改admin 账号密码.再访问之前拿到的/admin 即可拿到flag:

![图 009](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rapaL0gDxQpPDsxDlH1K3zY9GUjvDsJSuN63WHO7c7O9LyGurXN6VseSCziaZX7G1O6icicmrUXtykCMAiblHBJ0Xw6FLHULpOlPQrw5LnqZbvU/640?wx_fmt=webp&from=appmsg)

图 009

#### [Week 1] 老叟洗完头

这道题我出了大概2周才出完，我原计划是打算让你们探黑盒的，但让ai跑满测试了一下发现它猜不出来，所以加了很多hint，但是我没想到还是做不出来，特别是我都说了要去ctfshow上找，居然还没解，我想有很大一部分人看到题目难度就没去解了。

![图 010](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rapaL0gDxQp7uUToiaaBlz34cUvRql5eMHjVC8oh6cy2YHIdFlzA1XtjzfZoyQHU17QYcNrTqmjmPS6smdL474zbcwQjtnHkjM45VHeeZN7M/640?wx_fmt=webp&from=appmsg)

图 010

打开题目面是这样的，思路可以为后台执行dirsearch 目录爆破，前台我们个人测试常见的名字，像/admin,robots.txt君子协议等

![图 011](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQoLYibJDrP2cfE5xaRFqibibx8kZtSkdv6Lnia4kMaRnY33rf12QASOXS6ViaELMH1eTxN4RYOlZoGfgMSBj3iabCP89q1R3HiadsHzsE/640?wx_fmt=webp&from=appmsg)

图 011

![图 012](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQpIiciabia44hAxqhp9OZ7TOF6KEdLeKmly9Hm1YR01LTibmu9Or7Z6IvjPP8mYXTaN07vBFLYPic49ExSmHib56A4EZVJmxzSF2jIZM/640?wx_fmt=webp&from=appmsg)

图 012

到这里思路就是先测试这三个路径，但是像/upload/就会

![图 013](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQrKJzyXqVAcfc00rgLTiamn28ibSKWfJAfK1tE9k8yCzOaKrkfRy62TQHGW7nWlVEdEZ2RezFgtGXVCrCvRUDhSrfVryaMP1B9fY/640?wx_fmt=webp&from=appmsg)

图 013

然后/backup/弹

![图 014](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQqt1co1dXtIYzW9Z2GPgeKjWiajQHW6gkxVdHlU7ITQ5DWhaph1IiaB6nr7m4WFNgmrAJIqEfWT7QLse9599o6Oy1GAlEou9ggLk/640?wx_fmt=webp&from=appmsg)

图 014

这里发现都不对就注意ad?min.php了，但是你会发现为什么ad?min.php也弹嘲讽面呢这时候就需要知道一个知识了，通配符，glob()匹配文件的时候?作为通配符出现，例如fl??.php，可以匹配fl1a.php,fl2a.php,flag.php当然有些不知道通配符的看到?也许也会猜到

![图 015](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQq67KV3gx9BQE1WvECtDH1VkXPzACvfibfoTHUkckOZ26ReS7ubEjmSJbL0yOw7okia1hPhmLibQ5zaibKjGehwf4WicK2qI7uO6uU8/640?wx_fmt=webp&from=appmsg)

图 015

简单搜集就可以发现题目要求输入为“flie\_get\_contents(secret1)这一步如果想不明白需要加强一下逻辑思维能力了题目提示了secret1是文件要读取，下面if语句又点名trim(file\_get\_contents(..),$code)现在唯一的难点就是waf了，正则几乎将所有可能的payload全部ban了那要如何构造呢学过相似的马上就能想到取反或者三元运算符，当然你没学过我后面也提示了ctfshow

![图 016](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQrDLquB6n2pjwGicEKFnaJZukRgtn2KkrSVibVwmtUCkVSGxhPCOnVHqYE6iccWEhPTxBA88G5ibYyF7fpJibO897BoJSOa13gqemtU/640?wx_fmt=webp&from=appmsg)

图 016

不会的可以去查阅一下web145，这个就是三目运算符构造脚本筛选字符，然后构造payload

```
ad1min.php?v1=1&v2=0&v3=%3F%28%7E%99%96%93%9A%A0%98%9A%8B%A0%9C%90%91%8B%9A%91%8B%8C%29%28%7E%8
C%9A%9C%8D%9A%8B%CE%29%3A
```

![图 017](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQp1icHLiab4t1Fn9BpL0ck8xJkF9CFcajKQM4kW0MuGiabc5wh335Uqibl5uYP3RO0IVoxYP2NKicw0QS8cg5NBibMtu09K4rP2uVyXY/640?wx_fmt=webp&from=appmsg)

图 017

这个时候就得到了第一段密码，而且你也可以注意到多了一个#hint我在后续题目也特地写了hint来避免没看到

![图 018](https://mmbiz.qpic.cn/sz_mmbiz_jpg/rapaL0gDxQp6wAhIWFyFxdBeaNu6vibfm9ia7zVwPTgNUM5EicLGRiaibOMw9EWFLgu3pOJIy5vntibxl1N9sQgawD0GRdYOYn81CwjicSXo6s80QU/640?wx_fmt=webp&from=appmsg)

图 018

像这里，暴露了include.php，而且也提示了php题目发生变化复用第一关原语，把参数从 secret1 改成 hint：得到：密钥就是secret1，异或加密会指引你前行

提示了xor加密，也说明密钥就是刚刚得到的密码

![图 019](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQpIkrBRb3jib73RG6Izgq5uMicWyA4rNc4P1DjCBLlEWljm92ib9IickOeFxkaDsIEenQJLr4iabEpWKDzNTlJlyOIlPWsEyL22Xg34/640?wx_fmt=webp&from=appmsg)

图 019

![图 020](https://mmbiz.qpic.cn/mmbiz_jpg/rapaL0gDxQpbibO24252FllVic57LjoUVCCB5LG18d1yZPcuH3FpFDjsw4iaHbuMILGIvTa3olvJhur73Q6uicTvMt3DibrnXeib0G7DC6KviaYNps/640?wx_fmt=webp&from=appmsg)

图 020

这里解读一下就能知道1. 客户端要上传 XOR 密文；2. 服务端先解密，再检查 JPEG 首尾；3. multipart 原文件名必须以 `.jpg` 结尾；`display_name` 只要求包含 `.jpg`，最终扩展名仍可为 `.php`。原本我是想用gd解析器来的，但最后感觉会有点难就没用，我是想考com段来着的还有二次渲染到这一步就简单了，构造一个木马插入图片之中，只要不破坏jpg结构即可最简单就是头+payload+尾了，直接在FF D9前面插入即可

然后再对完整明文进行xor加密给个示例exp：from pathlib import Path

```
ke...