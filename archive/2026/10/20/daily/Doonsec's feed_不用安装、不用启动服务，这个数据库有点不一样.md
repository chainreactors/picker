---
title: 不用安装、不用启动服务，这个数据库有点不一样
url: https://mp.weixin.qq.com/s/F5ok-lHC0vkXGFlYQmKyuQ
source: Doonsec's feed
date: 2026-10-20
fetch_date: 2026-10-21T06:48:22.743969
---

# 不用安装、不用启动服务，这个数据库有点不一样

# 不用安装、不用启动服务，这个数据库有点不一样

原创

didiplus
didiplus

攻城狮成长日记

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

技术科普预计阅读 7 分钟 · 共 2600 字

不用安装、不用启动服务，这个数据库有点不一样

轻量级数据库入门指南

#SQLite#MySQL#嵌入式数据库#WAL

READING PATH

阅读路线

6 个章节

01

SQLite 是什么？和 MySQL 有什么不同？

-

02

最特别的地方：数据库就是一个文件

-

03

没有服务端，它如何保证数据安全？

-

04

SQLite 为什么这么流行？

-

05

SQLite 能替代 MySQL 吗？

-

06

写在最后

嵌入式零部署单文件跨平台ACID 事务

你有没有想过，数据库一定要安装服务端、配置端口、创建账号才能使用吗？其实，还有一种数据库，不需要单独启动服务，不需要开放数据库端口，甚至可以直接嵌入程序。它的数据库通常就是一个普通文件。复制文件，就能迁移数据；打开程序，就能执行 SQL。它就是 SQLite。

从手机应用到桌面软件，从浏览器到物联网设备，这个体积小巧的数据库，早已成为软件世界里的重要基础组件。今天，我们就聊聊：SQLite 到底是什么？它为什么这么流行？又为什么不能完全替代 MySQL？

CHAPTER 01

**01****SQLite 是什么？和 MySQL 有什么不同？**

`SQLite`是一个使用`C`语言编写的嵌入式关系型数据库引擎。理解它，最重要的是两个字：嵌入。

我们平时使用`MySQL`，通常需要启动一个独立的数据库服务，应用程序通过网络连接发送`SQL`，再由数据库服务执行并返回结果。`SQLite`则把数据库引擎直接集成到应用程序中。

![](https://mmbiz.qpic.cn/mmbiz_png/kztGyHFwmfyU2GW3YWOmgqicgLJG2JyK5WLbbNBWZddcRZavG4Wib98M7wkicvPiaX46VcianFeLwBQaHTFBr49tf75BA7g00q12wjQxh0PHo6GA/640?wx_fmt=png&from=appmsg)

两者最大的区别，不是 SQL 能力，而是运行架构。SQLite 不需要额外的数据库服务进程，程序可以直接调用引擎完成数据读写。这意味着部署更简单、运行环境更轻量，特别适合本地数据存储。

核心特征

嵌入，而非连接

#零服务进程#函数调用#本地读写

SQLite 把数据库引擎编译进程序本身，没有独立服务进程，没有网络协议开销，读写数据就是一次函数调用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kztGyHFwmfww4WlE2kGf9McrEXfFa9DrVwoFqsVhLEH8sBm9g0VpG6RcRDUh9dpypdFVWN5b8DWHnf7O1tQoicN417wayd1LnV51ehEibNA80/640?wx_fmt=png&from=appmsg)

CHAPTER 02

**02****最特别的地方：数据库就是一个文件**

假设你的程序创建了一个名为 app.db 的数据库。

text

my-app/

├── main.py

├── config.json

└── app.db

这个 `app.db` 就可以保存表、索引、视图、触发器以及相关数据。没有复杂的部署流程，也不需要专门维护数据库服务。SQLite 还支持标准的 SQL 操作：

01

标准 SQL 操作

sql

CREATE TABLE users (

id INTEGER PRIMARY KEY,

name TEXT NOT NULL

);

INSERT INTO users (name)

VALUES ('张三');

SELECT \* FROM users;

02

Python 几行代码搞定

python

import sqlite3

conn = sqlite3.connect("app.db")

conn.execute("""

CREATE TABLE IF NOT EXISTS users (

id INTEGER PRIMARY KEY,

name TEXT NOT NULL

)

""")

conn.execute(

"INSERT INTO users (name) VALUES (?)",

("张三",)

)

conn.commit()

conn.close()

运行程序，数据库文件就可以自动创建。这也是 SQLite 最吸引开发者的地方：**不用先搭建一套数据库环境，就能拥有一个支持 SQL 的数据存储引擎。**

不过要注意，数据库是文件，不代表可以在使用过程中随意复制。尤其在 WAL 模式 下，部分已提交的数据可能还保存在关联日志文件中。备份时应优先使用 SQLite 备份接口，确保数据一致。

CHAPTER 03

**03****没有服务端，它如何保证数据安全？**

数据库最怕什么？数据写到一半，程序突然崩溃，甚至设备直接断电。SQLite 通过事务、日志和底层存储机制，尽可能保证数据库的一致性与可靠性。这里重点认识两个概念。

01

事务：要么成功，要么回滚

例如，转账需要同时扣除一方的余额，并增加另一方的余额。

sql

BEGIN;

UPDATE accounts

SET balance = balance - 100

WHERE id = 1;

UPDATE accounts

SET balance = balance + 100

WHERE id = 2;

COMMIT;

如果事务没有成功提交，SQLite 可以根据事务机制回滚未提交的修改，避免业务操作只完成一半。

TRANSACTION

事务执行流程

|  |  |  |  |
| --- | --- | --- | --- |
| 1  BEGIN  开启事务，进入原子操作边界 | 2  UPDATE  执行多条 SQL 修改数据 | 3  COMMIT  全部成功则提交，写入持久化 | 4  ROLLBACK  任一步失败则回滚，数据恢复原状 |

02

WAL：先写日志，再合并数据

WAL 的全称是 Write-Ahead Logging，即预写日志。它的基本思路是：先把修改写入日志，事务提交后再择机将相关数据合并回主数据库文件。

WAL

WAL 工作流程

|  |  |  |
| --- | --- | --- |
| 1  写日志  修改先追加到 app.db-wal 文件 | 2  提交  事务提交后数据可被读取 | 3  Checkpoint  择机将日志合并回 app.db 主文件 |

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kztGyHFwmfyyhcfakvdWx120noKPYGy8yX0CdibibsfiaZHZfYxx7cYyg9w9bTDERJ6vkt2luGxYUuQlY5ibic5tUWOSbib2gGc6OpPeKRIYpUPXc/640?wx_fmt=png&from=appmsg)

WAL 模式能够改善读写并发体验，但并不意味着可以无限并发写入。**同一数据库文件在同一时刻仍然只能有一个写事务。**此外，断电后的持久性还取决于同步设置、文件系统和存储设备等因素。事务机制能够显著提高可靠性，但不代表可以省略备份。

CHAPTER 04

**04****SQLite 为什么这么流行？**

答案很简单：轻量、方便、适用范围广。它尤其适合以下场景。

TYPICAL SCENARIOS

SQLite 的五大典型应用场景

1

手机应用

保存本地结构化数据、缓存和历史记录

2

桌面软件

存储用户配置、书签、任务记录和本地业务数据

3

物联网设备

网络中断时先保存采集数据，联网后再同步

4

自动化工具

保存执行状态、任务结果和运行记录

5

测试开发

快速创建数据库环境，减少额外的部署工作

例如，一台部署在偏远地区的采集设备，网络断开后仍然可以把数据写入本地 SQLite，等网络恢复后再上传服务器。

![](https://mmbiz.qpic.cn/mmbiz_png/kztGyHFwmfwIe2Kv9LZC3CRVia4MUZRgh32vk81MmDKUxplSmiaUA5x9OAKzugyOHUibPImDHqSY2bMa1XrepqUM8V2DuS51cHwibXqd9mlPsgU/640?wx_fmt=png&from=appmsg)

需要强调的是，SQLite 本身是数据库引擎，并不是自带远程同步能力的完整平台。离线数据上传、冲突处理和失败重试，仍然需要应用程序自行设计。

CHAPTER 05

**05****SQLite 能替代 MySQL 吗？**

这是最值得关注的问题。答案是：**有些场景可以，有些场景不应该。**

| 对比维度 | SQLite | MySQL |
| --- | --- | --- |
| 运行方式 | 嵌入应用程序 | 通常运行独立服务 |
| 部署难度 | 简单，通常只需引擎和数据库文件 | 需要部署和管理服务 |
| 远程访问 | 本身不提供传统数据库服务器接口 | 原生支持客户端网络连接 |
| 并发写入 | 同一数据库文件同一时刻一个写事务 | 支持多事务并发写入 |
| 典型场景 | 本地应用、桌面软件、嵌入式设备 | Web 系统、共享业务数据库 |

推荐

适合 SQLite 的场景

#个人工具#桌面程序#本地采集

个人工具、桌面程序、本地数据采集应用——单机使用、部署从简、数据量可控。

慎选

适合 MySQL / PostgreSQL 的场景

#多实例#高并发#远程访问

多个服务实例共访问、大量并发写入、远程访问、集中权限管理、高可用需求——架构层面需要独立数据库服务。

另外，不建议把`SQLite`数据库文件直接放到网络文件系统上，供多台机器同时读写。这种部署方式可能受到文件锁和文件系统行为的影响。

选数据库，不要只看功能多少，更要看架构是否匹配业务。

CHAPTER 06

**06****写在最后**

`SQLite`并不是一个简化版的玩具数据库。它支持事务、索引、视图、触发器、窗口函数以及`JSON`相关功能，能够胜任大量实际的数据存储任务。

事务索引视图触发器窗口函数JSON

它真正的优势，是把数据库引擎嵌入应用程序，让本地数据存储变得简单、轻量。但它也有自己的边界：高并发写入、多机共享和集中式数据库管理，并不是它最擅长的方向。

本地存储，可以优先考虑`SQLite`；集中式业务数据库，则需要结合业务评估`MySQL`或`PostgreSQL`。

下次开发一个小工具时，不妨先问自己：我真的需要专门搭建一台数据库服务器吗？也许，一个小小的 SQLite 文件，就足以解决问题。

互动话题

你在工作中用过 SQLite 吗？

评论区分享你的使用场景

感谢你的阅读与支持！

关注「攻城狮成长日记」，一起把复杂的技术问题讲明白

· 点赞 ·

喜欢就点个赞吧

· 转发 ·

分享给更多朋友

· 推荐 ·

推荐给身边的人

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