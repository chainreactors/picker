---
title: 我重装了17次OpenClaw，凌晨4点还在翻GitHub，这5个坑你千万别踩
url: https://mp.weixin.qq.com/s/zDbsNtIpRkm_mAgveMDLOQ
source: Doonsec's feed
date: 2026-03-20
fetch_date: 2026-03-21T04:00:12.145545
---

# 我重装了17次OpenClaw，凌晨4点还在翻GitHub，这5个坑你千万别踩

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/x5l8unjI0Uq9ZibmMBWB7Udjbazju9f0BibMn6iba7bTP2KmkRXPDQ8RetVziav7XDaIibyYne5lOrRU8V9PXJX8siajW5rKowoNGt3XNe6n7lFHQ/0?wx_fmt=jpeg)

# 我重装了17次OpenClaw，凌晨4点还在翻GitHub，这5个坑你千万别踩

原创

AI员工1号
AI员工1号

AI员工上线

![]()

在小说阅读器中沉浸阅读

# 我重装了17次OpenClaw，凌晨4点还在翻GitHub，这5个坑你千万别踩

两周。17次重装。50块Token。凌晨4点的报错日志。

我以为我在搭一个AI助手，结果我在给自己挖坑。

飞书机器人跑起来的那一刻，我还截图发了朋友圈，配文"数字员工上岗"。那一刻挺爽的。

然后第二天起床，它死了。不说话了。飞书群里@它，像@一块石头。

这之后的两周，我就是在踩坑、爬出来、再掉进新坑的循环里。现在回想起来，那些凌晨四点的报错日志，都是血泪。

今天这篇文章，把我踩过的所有坑、以及怎么爬出来的，一次性说清楚。

如果你刚装上OpenClaw，或者正准备装，看完这篇能帮你少熬至少五个深夜。

---

## 坑一："临时运行"的幻觉

**症状**：

* 装好OpenClaw，机器人正常回复
* 关掉终端窗口，或者断开SSH，机器人就死了
* 重启电脑/WSL，服务没了

**我当时的反应**：

"卧槽，昨天明明弄好了，今天怎么又要重新配置？"

我反复装了十几次，每次都以为哪里配错了。后来才明白，问题根本不是配置，而是——**我根本没有把它注册成系统服务**。

OpenClaw默认只是"临时运行"。你开着终端，它就在；终端一关，它就跟着死了。

**救急方法**：

装完之后，一定要执行这条命令，把它注册成系统服务：

```
openclaw onboard --install-daemon
```

Linux用户可以用systemd，macOS用LaunchAgent。具体配置可以参考官方文档，但核心就一句话：**别让OpenClaw跟着终端一起死**。

---

## 坑二：配置文件改崩，Token暴涨

**症状**：

* 想换个模型，改了openclaw.json
* 重启后服务起不来，报错一堆
* 或者更隐蔽的：Token消耗异常，一天花了十几块

**我踩过的具体场景**：

第一次我想把模型从Kimi换成百炼的免费API。照着文档改了配置文件，结果服务直接起不来。排查半天发现，百炼的免费版和付费版baseurl不一样：

```
免费版：https://dashscope.aliyuncs.com/compatible-mode/v1
付费版：https://coding.dashscope.aliyuncs.com/v1
```

就这一点点差别，我折腾了两个小时。

还有更坑的。有一次我让AI"帮我优化一下配置文件"，结果它把我整个配置结构改乱了。重启后服务倒是能跑，但Token暴涨——因为AI在每次对话时都把完整的、超长的上下文塞给了模型。

**救急方法**：

1. **改配置前先备份**

   ```
   cp ~/.openclaw/openclaw.json ~/.openclaw/openclaw.json.bak
   ```
2. **用Git做版本控制**

   ```
   cd ~/.openclaw
   git init
   git add .
   git commit -m "备份初始配置"
   ```

   改崩了直接`git checkout .`回滚。
3. **别让AI自己改配置** 这是血泪教训。AI生成的配置不一定符合OpenClaw的schema，改完一定要用`openclaw doctor`检查。

> 配置是系统的骨架，别让AI当骨科医生——它可能会把你的腿接到胳膊上。

---

## 坑三：以为装了就行，其实内存系统更重要

**症状**：

* 重启对话后，AI"失忆"了
* 之前交代过的任务、上下文，全没了
* 每次都要重新交代背景

**我当时的心态**：

"这玩意儿怎么跟鱼一样，七秒记忆？"

其实OpenClaw有记忆系统，但默认的MEMORY.md大多数人要么不写，要么写成流水账，最后变成垃圾堆。

**我的解决方案**：

建立一个分层的记忆架构：

```
MEMORY.md          ← 索引层：只放核心信息和指向
memory/projects.md ← 项目层：每个项目的状态和待办
memory/infra.md    ← 基础设施：服务器配置、API地址
memory/lessons.md  ← 教训层：踩过的坑，按严重程度分级
memory/YYYY-MM-DD.md ← 日志层：每天发生了什么
```

核心思路：**MEMORY.md只做索引，不堆内容**。每次新session只加载索引，需要具体信息时再按需读取。

配合OpenClaw的向量语义检索（memorySearch），效果更好。你说"上次那个部署问题怎么解决的"，AI不需要翻遍所有日志，而是直接定位到具体文件的具体行。

> 好的记忆系统不是让AI记住一切，而是让它知道该在什么时候想起什么。

---

## 坑四：端口占用，Dashboard打不开

**症状**：

* 运行`openclaw dashboard`，给了个链接
* 浏览器打开，一片空白或连接失败
* 或者提示端口被占用

**我当时的排查过程**：

先是发现端口18789被占了。查了一下，是之前没关干净的Node进程。

```
lsof -i :18789
kill -9 <PID>
```

然后Dashboard还是打不开。研究半天才发现，我部署在远程服务器上，Dashboard默认只绑定了127.0.0.1，远程访问不了。

**救急方法**：

1. **端口被占用**

   ```
   lsof -i :18789
   kill -9 <PID>
   ```
2. **远程服务器访问Dashboard** 用SSH隧道：

   ```
   ssh -N -L 18789:127.0.0.1:18789 root@你的服务器IP
   ```

   然后本地浏览器访问`http://localhost:18789`。
3. **或者修改绑定地址** 在openclaw.json里把gateway.bind改成"0.0.0.0"，但**一定要同时配置认证token**，否则裸奔在公网上很危险。

> 端口是门，默认只开给 localhost 是防盗门全开给 0.0.0.0 是不设防——你选哪个？

---

## 坑五：Skill装了一堆，系统越来越慢

**症状**：

* 刚开始很快，后来越来越卡
* 响应时间变长，偶尔还崩溃
* 后台进程越来越多

**我的排查过程**：

用`openclaw logs`看日志，发现每次对话都要加载一堆Skill的上下文。我装了十几个Skill，很多其实根本用不上，但它们在后台一直占着资源。

还有一个坑：有些Skill会频繁调用API，即使你没有主动使用它们。这就是Token莫名其妙消耗的原因之一。

**救急方法**：

1. **只装必要的Skill** 新手建议按这个顺序装：

* skill-commons（安全底座，必装）
* memory（记忆系统）
* openclaw-backup（备份） 其他的等真有需求了再装。

2. **定期清理不用的Skill**

   ```
   openclaw plugin list
   openclaw plugin uninstall <skill-name>
   ```
3. **开启沙箱模式**

   ```
   openclaw config set sandbox true
   ```

   防止Skill做一些出格的操作。

---

## 两周后的我，终于稳定了

现在我的OpenClaw已经稳定运行一个多月，成了真正的"数字员工"。总结一下让我从"玩具"变"工具"的几个关键设置：

| 设置项 | 作用 |
| --- | --- |
| `--install-daemon` | 注册系统服务，重启不掉 |
| Git版本控制 | 配置改崩能回滚 |
| 分层记忆架构 | 对话有连续性，不用反复交代背景 |
| SSH隧道访问Dashboard | 远程管理安全方便 |
| 沙箱模式 | Skill不乱来 |
| 定期备份 | `openclaw backup` 一键救命 |

---

## 最后说两句

OpenClaw是个好东西，但它不是"装完就能用"。它更像是一个毛坯房，需要你花时间去装修、去调教。

那两周踩坑的经历，现在回头看其实挺值的。因为当你把所有坑都踩一遍，你对这个系统的理解就完全不一样了。它不再是黑盒，而是你能掌控的工具。

如果你正在踩坑，希望这篇能帮你少走点弯路。

如果你已经踩完了，欢迎在评论区分享你的"坑"，让更多人看到。

毕竟，开源社区就是这样，一人踩坑，全员避坑。

---

*（觉得有用的话，点个赞或转发给正在折腾OpenClaw的朋友～）*

## 参考链接

* OpenClaw官方文档[1]
* 阿里云部署OpenClaw指南[2]
* OpenClaw问题排查全指南[3]

### 引用链接

[1]OpenClaw官方文档: *https://docs.openclaw.ai*

[2]阿里云部署OpenClaw指南: *https://developer.aliyun.com/article/1716669*

[3]OpenClaw问题排查全指南: *https://www.cnblogs.com/qiniushanghai/p/19692692*

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0Uqrm4gHILLG2gYhHuico1NLxVJaiajoaia7s7y1Iy8wsNOwzmGGFowHyeszUtzrCXpnmKH5C2dwn6wqIByFI4iaxqKBYzqUdd6uL6M/0?wx_fmt=png)

AI员工上线

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/x5l8unjI0Uqrm4gHILLG2gYhHuico1NLxVJaiajoaia7s7y1Iy8wsNOwzmGGFowHyeszUtzrCXpnmKH5C2dwn6wqIByFI4iaxqKBYzqUdd6uL6M/0?wx_fmt=png)

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