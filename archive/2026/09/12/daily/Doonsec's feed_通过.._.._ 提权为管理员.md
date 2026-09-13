---
title: 通过../../ 提权为管理员
url: https://mp.weixin.qq.com/s/yw1jHVLyNLRE7wasNkyztw
source: Doonsec's feed
date: 2026-09-12
fetch_date: 2026-09-13T06:57:09.294575
---

# 通过../../ 提权为管理员

# 通过../../ 提权为管理员

Adhamkhairy
Adhamkhairy

漏洞集萃

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

> **本公众号所发布的文章内容仅供学习与交流使用，禁止用于任何非法用途；如有侵权烦请告知，我们会立即删除并致歉，谢谢**

在测试一个私有漏洞赏金计划时，我遇到了一个

```
作者: Adhamkhairy
原文链接: https://infosecwriteups.com/to-admin-for-a-bounty-b946f781607f
```

该目标承担着两个角色。

**管理员：**设置、用户管理、计费、促销。基本上涵盖了整个应用程序。大约**有 150 个接口**。

**观众：**看几篇资料就回家吧。**10 个端点**。猜猜哪个是我的账号。

有140个端点我不被允许触碰。这一差距并非限制，而是一份待办事项清单。

## 没人会发帖提到的无聊部分

那么，以下就是我实际所做的，我想如实相告，因为大多数技术报告都会跳过这部分，直接切入巧妙的有效载荷。

我在第二个租户上创建了一个管理员账户，逐一测试了每个功能，并记录了 Burp 捕获到的所有请求。随后，我提取了**浏览器的**会话 cookie，将其添加到这 150 个请求中，然后逐一重放了这些请求。

就这么简单。不需要定制工具，也不需要 12 个阶段的重构流程。只需一个查看器 cookie 和大量右键点击操作。

Press enter or click to view image in full size

![](https://mmbiz.qpic.cn/mmbiz_png/jow1el0IZibyMUDUGvR6WmLHPiaq4j0Jgwrvyx7I9jMVmy80CWwEWsZw1wvD8TWJ7eRPVf32p4ZTSRcyciaq3eFlTHpM7c9EfgyhLcEthkUNzs/640?wx_fmt=png&from=appmsg)

我知道我应该重命名这些标签页，把重点放在寻找伴侣上

其中149人给出了相同的回答：

```
HTTP/1.1 403 Forbidden
.........
.........
.........
.........

{"error":"Insufficient permissions"}
```

一遍又一遍又一遍。到了一定时候，你就不去看回复内容了，而是开始根据状态码列的颜色来匹配模式。而这正是容易漏看细节的时候，所以我强迫自己放慢速度，认真查看每一条。

幸好我这么做了，因为137号是绿色的。

## 第 0 步：回答者

```
POST /api/admin/action HTTP/1.1
Host: app.example.com
Cookie: session=<viewer_session>
Content-Type: application/x-www-form-urlencoded

Action=ViewSettings
```

```
HTTP/1.1 200 OK
.......
.......
.......

{"success":true,"settings":{...}}
```

一位查看者刚刚读取了存储库设置。

这已经算是一份报告了。访问控制存在漏洞，仅具有只读权限的角色也能访问管理员功能，写份报告，领走 500 美元的 Medium 漏洞赏金，然后继续前进。

但这件事总让我觉得有些别扭。

再看一下这个请求。其中既没有资源 ID，也没有对象引用，更没有查询条件。整个请求就是**字符串中**一个 VERB 动词 。 `Action=ViewSettings`……服务器接收一个名称，然后……就执行那个名称所代表的操作了吗？

如果那是一个普通的 `switch`语句或白名单，那也行，无所谓。但它看起来不像一个 switch 语句。看起来像是将该值**拼接**成了某个东西 。

而且，那些被拼接进路径中的元素是可以遍历的。

## 第一步：最愚蠢的测试

在采取任何巧妙措施之前，我想先弄清楚到底是哪一种情况：白名单还是路径解析。

于是，我发送了能想到的最没用的有效载荷。

```
POST /api/admin/action HTTP/1.1
Cookie: session=<viewer_session>
.......
.......
.......

Action=./ViewSettings
```

```
HTTP/1.1 200 OK
.......
.......
.......

{"success":true,"settings":{...}}
```

### Still **200**。

而这就是整个研究结果，就浓缩在这个一个字符里。

`./ViewSettings`这不是**一个有效的操作名称**。如果后端将我的输入与允许字符串列表进行比对，这会立即被拒绝，因为它根本不在列表中。没有任何一种情况会允许白名单接受它。

但 `./`表示“同一目录，不移动”。这是一个无操作。对于**路径解析器**而言， `./ViewSettings`和 `ViewSettings`指的是同一个位置。

服务器将它们视为同一个地方。

所以它是一条路径。它从来都不是一个操作名称，而是一段被附加到某个内部 URL 上的路径，并在内部调用发出之前被解析。

## 第 2 步：走上去

现在我不再去猜测动作名称了。我正在进行导航。

如果 `./`问题解决了， `../`就解决了。向上提升一级，然后回到管理员所在的位置：

```
POST /api/admin/action HTTP/1.1
Cookie: session=<viewer_session>
..........
..........
..........

Action=../admin/viewsettings
```

```
HTTP/1.1 200 OK
```

无论内部基数是什么，它最终都简化成了类似于以下的形式：

```
/internal/action/../admin/viewsettings
        ↓
/internal/admin/viewsettings
```

又是两百。

到了这一步，我已经完全不在乎设置了。设置从来都不是最终目标。真正的收获在于：我现在能够**以**内部 API 的身份 ，从一个查看者会话中向内部 API 发送请求，而无论另一端是什么服务，它都完全不知道是查看者在操控。

## 第3步：我一直致力于实现的这一步

还记得我在“无聊阶段”映射的那些管理路由吗？其中一个是晋升端点。它在路径中接受一个用户 ID，并将该用户晋升为管理员。

向上两层到达 API 根目录，然后直接进入：

```
POST /api/admin/action HTTP/1.1
Host: app.example.com
Cookie: session=<viewer_session>
Content-Type: application/x-www-form-urlencoded
..........
..........
..........

Action=../../api/admin/promote/<my_user_id>
```

```
HTTP/1.1 200 OK
..........
..........
..........

{"message":"User promoted to admin successfully"}
```

刷新了仪表盘。

管理员。**$X,000。**

> *顺便提个让我忍俊不禁的小插曲：几个月前，在****回应 FahemSec 的****挑战时，我几乎用了完全一样的手法*`userId`*，通过遍历一个机器人的*`参数转换为`*/api/admin/promote/。真心向他们致敬，他们的挑战绝非那种“谜题盒”式的无稽之谈，而是基于真实应用中实际存在的错误构建的。我记得当时还想，这种代码绝对没人会部署。结果，真有人把它部署了。*

## 为什么这招真的奏效了

两个不同的错误，而你都需要**这两个**错误。

**Action 值被直接放入路径中，未进行任何清理。**既未进行规范化处理，也未去除 `../`，也没有针对已知操作名称的允许列表检查。该开发者显然认为，该值只会是其自身前端发送的字符串之一。

**内部调用默认被视为可信。**公共网关正确地执行了角色验证，这就是为什么 149 个端点返回了 403 错误。但其背后的服务间调用完全跳过了这一验证，因为显然内部调用者已经获得了授权。因此，当我能够发起内部请求时，我以“非特定用户”的身份预先通过身份验证，而后端将此识别为“可信”。

仅凭其中任何一种情况都能应付。如果进入一个仍会检查角色的服务，你什么也得不到。一个可信的内部网状网络，如果其中没有用户控制的路由，你什么也得不到。将这两者结合起来，一个只读账户就能给自己写入管理员角色。

## 我想让你从中得到的启示是

这个漏洞最巧妙之处就在于它只有一个字符长。 `.`

真正发现问题的原因在于，系统重新播放了 150 个带有错误 Cookie 的请求，并且在第 118 个请求时没有走神。

当第一个端点响应时，报告已经生成——仅凭“查看器读取管理员设置”这一事实本身就已成立。那$X,000 的奖励，源于我多问了一个问题，即询问它*为何*会响应，而不是直接截图显示 200 状态码并点击提交。这与我获得的第一笔赏金时的直觉如出一辙：当时也是在回过头来再次向该端点发起请求后，一个“中等”级别的漏洞才最终转化为实际的奖金。

不要止步于最初的200。这200只是门，而不是房间。

觉得本文内容对您有启发或帮助？
点个**关注➕**，获取更多深度分析与前沿资讯！

👉 往期精选

[逻辑漏洞：邮箱注册 tips #11](https://mp.weixin.qq.com/s?__biz=MzkxNjc0ODA3NQ==&mid=2247485053&idx=1&sn=518c8e66c4b2fdf4eb7a0c57c8a28005&scene=21#wechat_redirect)

[非常用403绕过 Tips](https://mp.weixin.qq.com/s?__biz=MzkxNjc0ODA3NQ==&mid=2247485249&idx=1&sn=42308de5857f3dd4f4d1414e94169dab&scene=21#wechat_redirect)

[Android IPC 漏洞利用系列](https://mp.weixin.qq.com/s?__biz=MzkxNjc0ODA3NQ==&mid=2247485391&idx=1&sn=5092c4204d9910fa5b514d8dba7bb3b5&scene=21#wechat_redirect)

[新技术绕过文件上传](https://mp.weixin.qq.com/s?__biz=MzkxNjc0ODA3NQ==&mid=2247485346&idx=1&sn=c35a5732cb610a100e608d249c56fd3b&scene=21#wechat_redirect)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Y5LD4fX7WOLRgzxswNMosdb4HdiarwSPg43TDHTKMwbX8kaRZ8iajLgxTBVuwFBynCicFAmAvfvapPCydNnZKwgpw/0?wx_fmt=png)

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