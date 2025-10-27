---
title: Telegram 把飞机电报当成无限网盘使用
url: https://blog.upx8.com/3661
source: 黑海洋 - WIKI
date: 2023-06-29
fetch_date: 2025-10-04T11:48:57.813219
---

# Telegram 把飞机电报当成无限网盘使用

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# Telegram 把飞机电报当成无限网盘使用

发布时间:
2023-06-28

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
23626

![](https://img.imgdd.com/f210f3.4f9aad90-3149-41b2-9218-6db7df058069.png)

## 预览

预览中的速度已经达到了代理的限制，同时**速度取决于你是否是付费用户**

**![](https://ghproxy.com/github.com/iyear/tdl/raw/master/img/preview.gif)**

## 说明

`Telegram`下载上传都有速率限制，此工具采用多线程并发，可以加速下载上传速度。
`Telegram`群组目前可以设置禁止下载转发，此工具不受此限制，可以下载限制内容。
适用于：`Linux` `MacOS` `Windows`
`GitHub`项目：[https://github.com/iyear/tdl](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2l5ZWFyL3RkbA)

## 安装方法

按照系统下载相应版本并解压

```
# 下载 Linux_64 版本
wget https://github.com/iyear/tdl/releases/download/v0.5.5/tdl_Linux_64bit.tar.gz

# 解压
tar -zxvf tdl_Linux_64bit.tar.gz

# 赋予执行权限
chmod +x tdl

# 查看帮助
./tdl -h
```

```
下载 Linux_arm64 版本
wget https://github.com/iyear/tdl/releases/download/v0.5.5/tdl_Linux_arm64.tar.gz

# 解压
tar -zxvf tdl_Linux_arm64.tar.gz

# 赋予执行权限
chmod +x tdl

# 查看帮助
./tdl -h
```

## 使用

命令中的`sunpma`修改为自己的电报`ID`

```
# 设置用户空间
./tdl -n sunpma

# 登陆Telegram
./tdl login -n sunpma
```

输入用户`ID`后再输入电话号码，最后在已登录的`Telegram`中接受验证码后输入即可；
![](https://img.imgdd.com/f210f3.7a329d9f-8f63-417c-b19b-3823510d3f78.png)

## 下载

```
# 下载帮助
./tdl dl -h

# 下载链接，每多一个链接就多一个-u，多线程-t，默认8线程，设置代理--proxy
./tdl dl url -n sunpma -u https://t.me/sunpma/888 -u https://t.me/sunpma/999 -t 16 --proxy
socks5://localhost:1080
```

## 上传

默认上传到收藏夹

```
# 上传帮助
./tdl up -h

# 上传路径-p，包括文件-e
./tdl up -n sunpma --proxy socks5://localhost:1080 -p /path/to/file -e .so -t 16
```

## 环境变量

可以通过设置环境变量来避免每次都输入相同的参数值。

**注意：所有环境变量的值都比命令行参数的优先级低。**

命令行参数含义: [flags](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2l5ZWFyL3RkbC9ibG9iL21hc3Rlci9kb2NzL2NvbW1hbmQvdGRsLm1kI29wdGlvbnM)

| 环境变量 | 命令行参数 |
| --- | --- |
| TDL\_NS | `-n/--ns` |
| TDL\_PROXY | `--proxy` |
| TDL\_DEBUG | `--debug` |
| TDL\_SIZE | `-s/--size` |
| TDL\_THREADS | `-t/--threads` |
| TDL\_LIMIT | `-l/--limit` |
| TDL\_NTP | `--ntp` |
| TDL\_RECONNECT\_TIMEOUT | `--reconnect-timeout` |
| TDL\_TEMPLATE | dl `--template` |

## 数据

你的账号数据会被存储在 `~/.tdl` 目录下。

日志文件会被存储在 `~/.tdl/log` 目录下。

## 命令

前往 [docs](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2l5ZWFyL3RkbC9ibG9iL21hc3Rlci9kb2NzL2NvbW1hbmQvdGRsLm1k) 查看完整的命令文档。

## 最佳实践

如何将封禁的风险降至最低？

* 导入官方客户端会话登录。
* 使用默认的下载和上传参数。不要设置过大的 `threads` 和 `size`。
* 不要在多个设备同时登录同一个账号。
* 不要短时间内下载或上传大量文件。
* 成为 Telegram 会员。?

## 疑难解答

**Q: 为什么输入命令后没有任何反应？为什么日志中有 'msg\_id too high' 的错误？**

A: 检查是否需要使用代理（使用 `proxy` 参数）；检查系统的本地时间是否正确（使用 `ntp` 参数或校准系统时间）

如果都没有用，使用 `--debug` 参数再次运行，然后提交一个 issue 并将日志粘贴到 issue 中。

**Q: Telegram 桌面客户端在使用 tdl 后无法正常工作？**

A: If your desktop client can't receive messages, load chats, or send messages, you may encounter session conflicts.

A: 如果桌面客户端无法接收消息、加载聊天或发送消息，那么可能是会话冲突导致的。

你可以尝试使用 `tdl` 重新登录，并在 ”logout“ 部分选择 `YES`，这将分离 `tdl` 和桌面客户端的会话。

**Q: 如何将会话迁移到另一台设备？**

A: 你可以使用 `tdl backup` 和 `tdl recover` 命令来导出和导入会话。更多细节请参阅 [迁移](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL2l5ZWFyL3RkbC9ibG9iL21hc3Rlci9SRUFETUVfemgubWQjJUU4JUJGJTgxJUU3JUE3JUJC) 部分。

## FAQ

**Q: 这是一种滥用行为吗？**

A: 不是。下载和上传速度受服务器端限制。由于官方客户端的下载速度通常不会达到最高限制，所以开发了这个工具来实现最高速度的下载。

**Q: 这会导致封禁吗？**

A: 不确定。所有操作都不涉及敏感的行为，例如主动向其他人发送消息。但是，使用长期使用的帐户进行下载和上传操作更安全。

 -----------------------------------------

```

```

[取消回复](https://blog.upx8.com/3661#respond-post-3661)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2024 黑海洋. All rights reserved.
[看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号") [Sitemap](sitemap.xml?type=index "Sitemap")