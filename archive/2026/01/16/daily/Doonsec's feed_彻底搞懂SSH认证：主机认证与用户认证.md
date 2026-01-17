---
title: 彻底搞懂SSH认证：主机认证与用户认证
url: https://mp.weixin.qq.com/s/e7k4uMK967GGD-_9nfaOpw
source: Doonsec's feed
date: 2026-01-16
fetch_date: 2026-01-17T03:25:38.496297
---

# 彻底搞懂SSH认证：主机认证与用户认证

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/hGAb3jria8J37BSTsD0cLIZms4xVDsSPyoibfDc4gVJnQDtDAJbTSmZwxDaUGMwIWdm7HHPZpS51fvvfckqb4tDw/0?wx_fmt=jpeg)

# 彻底搞懂SSH认证：主机认证与用户认证

0xNvyao
0xNvyao

安全随笔

![]()

在小说阅读器中沉浸阅读

|  |
| --- |
| 声明：请勿利用本公众号文章内的相关技术、工具从事非法测试，如因此造成一切不良后果与文章作者及本公众号无关！ |

大家对SSH密钥登录过程应该都很熟悉：

* 在客户端通过ssh-keygen生成公私钥对
* 将公钥上传到服务器的/root/.ssh/authorized\_keys文件
* 使用ssh root@x.x.x.x -i 私钥文件，完成登录

但今天我们要深入探讨另一个关键文件/root/.ssh/known\_hosts，以及SSH认证中常被混淆的两个核心概念：主机认证与用户认证。

一、从实验现象说起

实验环境

* 机器1：10.10.10.101（客户端）
* 机器2：10.10.10.102（服务器）

实验步骤

第一步：检查known\_hosts文件

```
[root@server01 ~]# cat /root/.ssh/known_hosts# 空文件，无内容
```

第二步：首次连接目标服务器

```
[root@server01 ~]# ssh user02@10.10.10.102The authenticity of host '10.10.10.102 (10.10.10.102)' can't be established.ED25519 key fingerprint is SHA256:n7D8Nq5sTv2+L5ghdhgDHv0fPIDvg/SW0Cd4s1qQzMpY.This key is not known by any other namesAre you sure you want to continue connecting (yes/no/[fingerprint])? yes
```

输入yes后，通过密码完成登录。

第三步：查看known\_hosts变化

连接成功后，known\_hosts文件增加了三条记录，都是关于10.10.10.102的：

```
10.10.10.102 ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJK8pL+3t1dOq+fZXm2QWEZn21y/mzlWD/fLEH9qQrCC10.10.10.102 ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDaXpV7T6Uk96UhACfTeKJc8tL9zYCisWizeit7VyoVPVg1pCaL+rstNFdJse9J0wYo7U2CJeV+Fj8cJSTpub0LuK+2a9TLHNQZ4JPmWl/9CHZIgOuYCVo8NobfaMIkMJYYv7HSiBEXJX6GG7ma5KwmcbUQ5p9xwczLMPlakXVsxwgl1ytdDE5VyzLD8hBFE2Ih9WX7t1kEw+ILg8KTJGU8hJbySB1jQNRONHt9yNyybBSXGdp5+LQ/R0nN8whDZ5v3t/NZdPB41mkPvO4C7p/WDescWRKEpWVnfRDAQy0wrdMnyYriTjfjywJuQ+j6j2cQfdtKpdfU6eZpO9gcGOH0DB1jW7eerZnTPJZJXV1EVTRfRnahISSNqZu1aeaMphxjYpxgK6asoM7WLIEUC99tKUKW7j2066PDw7OqZlzavwCbYf84AqahD8T2Tmav6Qb4D+43Va+4ee2jZ8Y8X4boIuqBxZJX2glC3RHtcUdTAainPt54n7uR24VjMHA86Y0=10.10.10.102 ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBJ8eRqGWaetbiqRLuJQK0BQ6e5Ge0Zq4mz1i3enVJecmHSGiA62XLeIQjb62bZ4nK+EDlUORd944AvtgH7Mh5k9=
```

二、known\_hosts的核心作用

1. 防止中间人攻击（MITM）

这是known\_hosts最核心的安全功能：

* 首次连接：SSH客户端会询问你是否信任该主机。输入yes后，服务器公钥存入known\_hosts
* 后续连接：SSH会自动比对服务器发来的公钥与known\_hosts中记录的是否一致

安全逻辑：

* 公钥一致 → 连接的是同一台服务器（安全）
* 公钥不一致 → 服务器可能被替换，或存在中间人攻击（危险）

2. 文件格式

每行记录包含三个部分：

```
[主机标识] [算法类型] [公钥字符串]
```

例如：

```
10.10.10.102 ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJK8pL+3t1dOq+fZXm2QWEZn21y/mzlWD/fLEH9qQrCC
```

3、对比机器1的known\_hosts和机器2的/etc/ssh/公钥内容

机器1的known\_hosts：

![](https://mmbiz.qpic.cn/mmbiz_png/hGAb3jria8J37BSTsD0cLIZms4xVDsSPynd3gIdLQvHWj9Tedrd9KgmicPNMcndXLOtaA7jQTJNsdJtK8OlRksEg/640?wx_fmt=png&from=appmsg)

```
AAAAB3NzaC1yc2EAAAADAQABAAABgQDaXpV7T6Uk96UhACfTeKJc8tL9zYCisWizeit7VyoVPVg1pCaL+rstNFdJse9J0wYo7U2CJeV+Fj8cJSTpub0LuK+2a9TLHNQZ4JPmWl/9CHZIgOuYCVo8NobfaMIkMJYYv7HSiBEXJX6GG7ma5KwmcbUQ5p9xwczLMPlakXVsxwgl1ytdDE5VyzLD8hBFE2Ih9WX7t1kEw+ILg8KTJGU8hJbySB1jQNRONHt9yNyybBSXGdp5+LQ/R0nN8whDZ5v3t/NZdPB41mkPvO4C7p/WDescWRKEpWVnfRDAQy0wrdMnyYriTjfjywJuQ+j6j2cQfdtKpdfU6eZpO9gcGOH0DB1jW7eerZnTPJZJXV1EVTRfRnahISSNqZu1aeaMphxjYpxgK6asoM7WLIEUC99tKUKW7j2066PDw7OqZlzavwCbYf84AqahD8T2Tmav6Qb4D+43Va+4ee2jZ8Y8X4boIuqBxZJX2glC3RHtcUdTAainPt54n7uR24VjMHA86Y0=
```

机器2的/etc/ssh/公钥内容（以rsa算法公钥为例）：

![](https://mmbiz.qpic.cn/mmbiz_png/hGAb3jria8J37BSTsD0cLIZms4xVDsSPyryqUuAUicFXK9NR4BuNUcBevkic6je8weq6q70oiaicp9YEBJkbdeRW9iaQ/640?wx_fmt=png&from=appmsg)

```
AAAAB3NzaC1yc2EAAAADAQABAAABgQCyJIV7T6Uk96UhACfTeMJc8tL9zYCisWizeit7VyoVPVg1pCaL+rstNFdJse9J0wYo7U2CJeV+Fj8cJSTpub0LuK+2a9TLHNQZ4JPmWl/9CHZIgOuYCVo8NobfaMIkMJYYv7HSiBEXJX6GG7ma5KwmcbUQ5p9xwczLMPlakXVsxwgl1ytdDE5VyzLD8hBFE2Ih9WX7t1kEw+ILg8KTJGU8hJbySB1jQNRONHt9yNyybBSXGdp5+LQ/R0nN8whDZ5v3t/NZdPB41mkPvO4C7p/WDescWRKEpWVnfRDAQy0wrdMnyYriTjfjywJuQ+j6j2cQfdtKpdfU6eZpO9gcGOH0DB1jW7eerZnTPJZJXV1EVTRfRnahISSNqZu1aeaMphxjYpxgK6asoM7WLIEUC99tKUKW7j2066PDw7OqZlzavwCbYf84AqahD8T2Tmav6Qb4D+43Va+4ee2jZ8Y8X4boIuqBxZJX2glC3RHtcUdTAainPt54n7uR24VjMHA86Y0=
```

经对比完全一致，这就是机器1第一次ssh登陆机器2时，输入yes后，known\_hosts内容写入的内容。

三、主机认证 vs. 用户认证关系

这两个独立的认证阶段是最容易混淆的概念！即使使用密码登录，SSH依然需要进行主机认证。

第一阶段：主机身份认证（Host Authentication）

* 目的：确保你连接的服务器是真实的，而非假冒的
* 对应文件：known\_hosts
* 发生时机：在任何用户认证之前
* 逻辑：服务器发送它的"数字身份证"（公钥）给客户端验证

第二阶段：用户身份认证（User Authentication）

* 目的：证明你有权限访问该服务器

* 方式：

+ 密码认证
+ 密钥认证（使用authorized\_keys）

这就是为什么即使使用密码登录，known\_hosts依然会被更新的原因！

known\_hosts存在三条记录的原因是服务器在/etc/ssh/目录下同时配置了三种主机密钥，上机器2（10.10.10.102）/etc/ssh/目录看一下：

```
root@server02:~# ll /etc/ssh/-rw-------   1 root root    513 Jan  5 01:11 ssh_host_ecdsa_key-rw-r--r--   1 root root    182 Jan  5 01:11 ssh_host_ecdsa_key.pub-rw-------   1 root root    411 Jan  5 01:11 ssh_host_ed25519_key-rw-r--r--   1 root root    102 Jan  5 01:11 ssh_host_ed25519_key.pub-rw-------   1 root root   2610 Jan  5 01:11 ssh_host_rsa_key-rw-r--r--   1 root root    574 Jan  5 01:11 ssh_host_rsa_key.pub
```

客户端在首次连接时，会获取并记录所有可用算法对应的公钥指纹，确保未来连接的最佳兼容性。

最后让大模型帮忙画了一个ssh认证过程的时序图，方便大家的理解：

![](https://mmbiz.qpic.cn/mmbiz_png/hGAb3jria8J37BSTsD0cLIZms4xVDsSPyP0LnWLGktGI9UWkFKA1ms4FeM3Olsf3O6fsHVu1AUBicEibbCgdme2Og/640?wx_fmt=png&from=appmsg)

附上完整的 Mermaid 代码：

```
sequenceDiagram    autonumber    participant C as 客户端 (10.10.10.101)    participant S as 服务端 (10.10.10.102)    Note over C, S: 第一阶段：主机验证与密钥交换    C->>S: TCP 连接请求 (端口 22)    S->>C: 版本协商与算法协商 (KEXINIT)    S->>C: 发送服务器公钥 (来自 /etc/ssh/ssh_host_*_key.pub)
    Note left of C: 1. 检查 ~/.ssh/known_hosts<br>2. 未找到该服务器记录    C-->>User: 警告: "The authenticity of host...继续连接吗?"    User-->>C: 输入 "yes"    C->>C: 将服务器公钥指纹存入 ~/.ssh/known_hosts
    Note over C, S: Diffie-Hellman 密钥交换<br>双方生成相同的【会话密钥】与【Session ID】
    Note over C, S: 第二阶段：用户验证 (已在加密通道中进行)    C->>S: SSH_MSG_USERAUTH_REQUEST (Service: ssh-userauth, User: test02)
    alt 公钥认证 (优先尝试)        C->>S: SSH_MSG_USERAUTH_REQUEST (类型: "publickey", 仅发送公钥指纹)        Note right of S: 检查 ~/.ssh/authorized_keys 是否存在匹配公钥        S->>C: SSH_MSG_USERAUTH_PK_OK (确认公钥可用，要求提供签名)
        C->>C: 使用【私钥】对【Session ID + 认证请求数据】进行签名        C->>S: SSH_MSG_USERAUTH_REQUEST (包含完整公钥和数字签名)
        Note right of S: 使用服务器端公钥验证签名有效性        alt 验证成功            S->>C: SSH_MSG_USERAUTH_SUCCESS        else 验证失败            S->>C: SSH_MSG_USERAUTH_FAILURE (返回可用认证方式)        end
    else 密码认证 (若公钥不可用或验证失败)        S->>C: SSH_MSG_USERAUTH_FAILURE (提示可使用 password 认证)        C->>S: SSH_MSG_USERAUTH_REQUEST (类型: "password", 包含加密密码)        Note right of S: 验证密码 (检查 /etc/shadow 或 PAM)        alt 密码正确            S->>C: SSH_MSG_USERAUTH_SUCCESS        else 密码错误            S->>C: SSH_MSG_USERAUTH_FAILURE        end    end    Note over C, S: 第三阶段：会话建立 (Channel)    C->>S: SSH_MSG_CHANNEL_OPEN (session)    S->>C: SSH_MSG_CHANNEL_OPEN_CONFIRMATION    C->>S: SSH_MSG_CHANNEL_REQUEST (pty-req, 请求伪终端)    S->>C: SSH_MSG_CHANNEL_SUCCESS    C->>S: SSH_MSG_CHANNEL_REQUEST (shell, 开启 Shell)    S->>C: SSH_MSG_CHANNEL_SUCCESS
    S-->>C: 发送 Shell 欢迎语与提示符    Note over C: 显示: test02@hostname:~$
```

四、结语

理解SSH的双重认证机制是保障服务器安全的基础。记住：

* 主机认证确保你连接的是正确的服务器
* 用户认证确保只有授权用户能访问
* 两者缺一不可，且主机认证永远在前

下次看到known\_hosts更新时，你会明白：这不是简单的"记录"，而是SSH在默默为你筑起第一道安全防线。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/hGAb3jria8J1lqvLzNAGw1T8WLuQzh48Fp58MSBwhMMPUFKjEKGKS1KZv1URheiaZFQtvY47PPrJdYugG2bcm8zg/0?wx_fmt=png)

安全随笔

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/hGAb3jria8J1lqvLzNAGw1T8WLuQzh48Fp58MSBwhMMPUFKjEKGKS1KZv1URheiaZFQtvY47PPrJdYugG2bcm8zg/0?wx_fmt=png)

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