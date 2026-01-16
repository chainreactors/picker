---
title: 开源 | 告别重复对接，这款消息推送平台全渠道搞定
url: https://mp.weixin.qq.com/s/mzUTIxu0LIR2ZVsXIeYLHw
source: Doonsec's feed
date: 2026-01-15
fetch_date: 2026-01-16T03:26:07.623355
---

# 开源 | 告别重复对接，这款消息推送平台全渠道搞定

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/OsuOF7sibMYthnKx52q5PuDW2FjyrUJliaU1ZXUuv3IibFeZoWic2Ys072Yf6raT2AaObC5gRGkibU8WYQ1TAVpvKSg/0?wx_fmt=jpeg)

# 开源 | 告别重复对接，这款消息推送平台全渠道搞定

原创

didiplus
didiplus

攻城狮成长日记

![]()

在小说阅读器中沉浸阅读

在日常开发和运维中，你可能遇到过需要通过不同渠道（如邮件、钉钉、企业微信等）发送不同类型消息的情况。每当有新需求时，都需要重新编写对接逻辑；一旦某个部分变化，整个项目代码都要调整。这导致代码中出现大量重复的“消息发送”片段，增加了维护难度。此外，不同团队对通信渠道的偏好也使得单独为每种功能开发接口变得低效且容易出错。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/OsuOF7sibMYthnKx52q5PuDW2FjyrUJliarX4WUSK50KNgY8xiarOND9AMiam3iaZIZMFRR9ia6CvVRJicicCdrFuuiblNg/640?wx_fmt=png&from=appmsg)

好消息是，现在有一种工具可以解决这些问题——`Message Nest`。它是一个专为整合多种消息推送方式而设计的开源平台。通过`Message Nest`，你可以实现一次配置、多端分发，并支持灵活复用，从而简化开发流程，提高工作效率，增强系统的稳定性和可维护性。

### 前端

前端使用**Vue 3 + TypeScript + Vite** 技术栈，配合 **TailwindCSS** 与 **shadcn-vue**，界面干净利落，操作逻辑简单清晰。推送任务、模板管理、发送日志等功能统一集中在一个控制台中，日常使用非常顺手。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/OsuOF7sibMYthnKx52q5PuDW2FjyrUJliaKLtR5C4vT5rcRsFb4aeY2v5BzLSmsoY56JaFgRiahJs30oBf3JQ3EQw/640?wx_fmt=png&from=appmsg)

开发阶段支持热更新，调试高效；上线后既可以前后端一体化部署，也能拆分为前后端分离模式，适配不同团队的开发和部署习惯。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/OsuOF7sibMYthnKx52q5PuDW2FjyrUJliaKYZNc8iczpKARV587LUevpicsD9o3undZMhew0cGcBVY28Qxu0mPfHDw/640?wx_fmt=png&from=appmsg)

### 后端

后端基于 **Go + Gin + GORM** 构建，运行稳定、性能开销低。系统提供「任务」与「模板」两种消息推送模式：任务模式适合一次性动态消息，模板模式通过占位符复用内容，降低业务耦合。内置 **JWT 鉴权、异步发送、日志与审计机制**，消息流转清晰可追溯，适合生产环境使用。

## 核心能力一览

### ✅ 多渠道整合

内置支持多种通知方式：

* 邮件
* 钉钉
* 企业微信
* 微信测试公众号
* 自定义`Webhook`
* 站内消息

一个系统，统一管理。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/OsuOF7sibMYthnKx52q5PuDW2FjyrUJlia8ayWPfjPibENUXich3qXwxicEtlINEJGhoAaULcYQTTrzNzE00gxdlwSg/640?wx_fmt=png&from=appmsg)

### 模板化管理

消息内容不再写死在代码里：

* 一次定义
* 多处调用
* 支持占位符动态替换

运营或产品人员也能直接修改文案，**开发不再被反复打断。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/OsuOF7sibMYthnKx52q5PuDW2FjyrUJliajiaZSkdnib3JOEpCEblhIJXVVHoTcFYEWCxLn2rfRNAKy2GOcSg71SZw/640?wx_fmt=png&from=appmsg)

### 动态接收者 & 群发支持

支持灵活指定接收人列表，轻松应对群发邮件、批量公众号通知等场景。

### @提醒能力

在钉钉/企业微信中，可：

* @ 指定手机号
* @ 指定用户 ID
* @ 全体成员

告警场景非常实用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/OsuOF7sibMYthnKx52q5PuDW2FjyrUJliaUfaL8kia4SdbpCZQnKauWxPlyuF5ex616IcGF1qZy7crXExicEYmSHgw/640?wx_fmt=png&from=appmsg)

### 数据统计&可视化

内置消息统计能力，可查看：

* 发送成功率
* 渠道分布
* 失败情况

![](https://mmbiz.qpic.cn/sz_mmbiz_png/OsuOF7sibMYthnKx52q5PuDW2FjyrUJliaRVoxXY8D0bjVbia8WxHzTb4PScguKxFSiar2ia94XrOFg00uicj9nsnbYw/640?wx_fmt=png&from=appmsg)

## 部署方式

提供多种部署方式，无论是个人尝试还是正式投入使用，都能满足需求。

### 直接运行

使用最新的`Release`打包的可执行文件部署，无需部署前端页面。

* 下载Release

访问GitHub Releases[1] 下载最新的系统版本对应的release，然后解压。

* 创建数据库

新建一个`MySQL`数据库（或使用SQLite）。

* 配置文件

新建conf文件夹，或者重命名项目中`conf/app.example.ini`为`conf/app.ini`，然后修改配置。

```
1[app]

2JwtSecret = message-nest

3LogLevel = INFO

4

5[server]

6RunMode = release

7HttpPort = 8000

8ReadTimeout = 60

9WriteTimeout = 60

10; 注释EmbedHtml，启用单应用模式

11; EmbedHtml = disable

12

13[database]

14; 关闭SQL打印

15; SqlDebug = enable

16

17; Type = sqlite

18Type = mysql

19User = root

20Password = Aa123456

21Host = vm.server

22Port = 3308

23Name = yourDbName

24TablePrefix = message_
```

* 启动项目

直接运行可执行文件，项目会自动创建表和账号。

```
1# Windows

2./Message-Nest.exe

3

4# Linux/Mac

5./Message-Nest
```

### Docker 部署

* 准备配置文件

新建 `conf/app.ini` 文件

```
1[app]

2JwtSecret = message-nest

3LogLevel = INFO

4

5[server]

6RunMode = release

7; docker模式下端口配置文件中只能为8000

8HttpPort =8000

9ReadTimeout =60

10WriteTimeout =60

11; 注释EmbedHtml，启用单应用模式

12; EmbedHtml = disable

13

14[database]

15; 关闭SQL打印

16; SqlDebug =enable

17

18; Type = sqlite

19Type = mysql

20User = root

21Password = Aa123456

22Host = vm.server

23Port =3308

24Name = yourDbName

25TablePrefix = message_
```

* 启动容器

```
1docker run --rm-ti\

2-p8000:8000 \

3-v /your/path/conf:/app/conf \

4  ghcr.io/engigu/message-nest:latest
```

|  |
| --- |
| 推荐文章  [NeuraPress开源推荐:专为公众号打造的Markdown排版神器](https://mp.weixin.qq.com/s?__biz=MjM5OTc5MjM4Nw==&mid=2457389484&idx=1&sn=73024c47a829efeeb7b323fe8541f54b&scene=21#wechat_redirect)  [写FastAPI项目前必读：这份开源最佳实践让你少踩 90% 的坑！](https://mp.weixin.qq.com/s?__biz=MjM5OTc5MjM4Nw==&mid=2457389398&idx=1&sn=85ab8110f9bc258cb64a6375c57aa9ad&scene=21#wechat_redirect)  [复习太难？我做了个刷题网站，效率直接翻3 倍！](https://mp.weixin.qq.com/s?__biz=MjM5OTc5MjM4Nw==&mid=2457389450&idx=1&sn=7cf9fa9c581517880ef107db52248eb0&scene=21#wechat_redirect)  [远程办公救星！用code-server打造你的专属云端IDE](https://mp.weixin.qq.com/s?__biz=MjM5OTc5MjM4Nw==&mid=2457389420&idx=1&sn=ae8126f8140f041db68bf3dcd9476031&scene=21#wechat_redirect) |

---

**外部链接参考**

1. https://github.com/engigu/Message-Push-Nest/releases

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/OsuOF7sibMYtLPfoEoNn5zJQjy6nMKW0GVf41zsKNsIVKdWJsxm2gSyIToAJOFI8x2wryVm4GqQib0ibno9KzEa9A/0?wx_fmt=png)

攻城狮成长日记

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/OsuOF7sibMYtLPfoEoNn5zJQjy6nMKW0GVf41zsKNsIVKdWJsxm2gSyIToAJOFI8x2wryVm4GqQib0ibno9KzEa9A/0?wx_fmt=png)

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