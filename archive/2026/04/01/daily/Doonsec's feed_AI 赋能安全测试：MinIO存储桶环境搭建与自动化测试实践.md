---
title: AI 赋能安全测试：MinIO存储桶环境搭建与自动化测试实践
url: https://mp.weixin.qq.com/s/RSHlnPwsT7dc-YqxMUEW4w
source: Doonsec's feed
date: 2026-04-01
fetch_date: 2026-04-02T04:21:42.846610
---

# AI 赋能安全测试：MinIO存储桶环境搭建与自动化测试实践

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/xY9ZTT0gDw5K5aH9rAhlKicc1tBj5rnxDW0arRZkLuYIwy7TYC5j5iaV4bgXmQDbsUb8UPUicweDpTmjibvDw8m7p1XNGauI678WPrx99j2APbE/0?wx_fmt=jpeg)

# AI 赋能安全测试：MinIO存储桶环境搭建与自动化测试实践

原创

huan666
huan666

huan666

![]()

在小说阅读器中沉浸阅读

一、前言

本文重点讲解针对性检测 Skill 的自动化生成方法，详解 MinIO 存储桶漏洞环境的搭建流程，并实现基于 AI 的漏洞自动化扫描检测，只是提供一种思路，具体流程还需优化。

二、MinIO存储桶漏洞环境搭建

使用Linux kali系统部署靶场环境

1、桌面创建MinIO目录用于存放安装包和数据文件

![](https://mmbiz.qpic.cn/mmbiz_png/xY9ZTT0gDw5CSYHu6xnd3d2G5ALSFepnWMd128GMibyXrFBvZzwiahzvibjUBa43JbghEciaQx8ib3ENh0nkr9Bh49q2tI1ibsNF3ppdmDFGa2tmQ/640?wx_fmt=png&from=appmsg)

2、下载MinIO服务端和客户端，并赋予执行权限

```
# 下载 Linux amd64 版本服务端wget https://dl.min.io/server/minio/release/linux-amd64/minio# 赋予执行权限chmod +x minio
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xY9ZTT0gDw4NTl2XL9K7RWds3cjxVvkVHwzp6cDFNtSOoJyUbN9nvicicSLNIO7pLY3Hm43r7DJzwkeN3x2ibgFGpA3jfbfBxS3AHJ9iaOTE8c0/640?wx_fmt=png&from=appmsg)

```
# 下载 Linux amd64 版本客户端wget https://dl.min.io/client/mc/release/linux-amd64/mc# 赋予执行权限chmod +x mc
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xY9ZTT0gDw6xsNmnU67GGfJVPno56YEQHXiaE7HrmP5hZLEvUEkicQTrkQeibSUzpMbldmIiaRibxbRQzQ2ibMJkCdLpYuXqx1GVkAickpRicWA229E/640?wx_fmt=png&from=appmsg)

3、启动MinIO服务端

./minio server ./data --console-address ":9001" --address ":9000"

* `./data`

  ：存储桶数据目录（自动创建）
* `--console-address ":9001"`

  ：管理控制台端口（浏览器访问 `http://IP:9001` 登录）
* `--address ":9000"`

  ：S3 API / 文件访问端口（匿名访问用这个端口）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xY9ZTT0gDw77bFsakhBno3rLzZE9973CtqAWYXcQIudlbB5dag85Ym6CtU9PyCUQZzJPbN5kX6x90uyibWeqJvWAicsePseJJ1Lx1nf13nhF4/640?wx_fmt=png&from=appmsg)

4、访问管理控制台，默认账号密码：minioadmin/minioadmin

![](https://mmbiz.qpic.cn/mmbiz_png/xY9ZTT0gDw6HRibFv9pIQoFhIO4uEicvia2B7b9V0ExbfBetcc9suZWYbpf27yibqrZibzOM7r9ot1kQ2pKArftLsN5oD72yc4QXIicwHT039xQfo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/xY9ZTT0gDw61icG1CBjfR90tGGTcc9SLRpibEBKjW7qNceyZCUpibsFDprsLCT5Yy43S2y5flAQ0gFKD5YSialhaHOxAkkVadRppkrQlV7fDC78/640?wx_fmt=png&from=appmsg)

5、点击左侧菜单Create Bucket创建存储桶

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xY9ZTT0gDw4qG3eBtF3Dms0aX5hT8VoBhrh3wvyic3wEfXgibSxMcicLoRmKU3TO64FD2sW09COWBBOibPHkd0IAPI1HCMhvic1xibhmGdRics6HS0/640?wx_fmt=png&from=appmsg)

点击Upload上传测试文件

![](https://mmbiz.qpic.cn/mmbiz_png/xY9ZTT0gDw5SFAFR3pibqQ439QVgvqfxGIjib0ictm3rKIvx2ZU9h8XicAfxroyDV6fYYElXrpsR0lJq4GWBWkOOic4iceYiabdT7ia6MdqypcOskibU/640?wx_fmt=png&from=appmsg)

6、配置匿名访问策略，之前启动服务的窗口不要动，重新开启一个窗口

命令运行不了就用过AI格式化一下格式

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xY9ZTT0gDw74PQIH6TbL9ny05r0xLJiaVaLYMTTicb2pbnG2sJzTSKAqXjm4byzA2Pds7k9zct42d2Kd6ldKxoLRadynb3qGuBlBchY1YMcEs/640?wx_fmt=png&from=appmsg)

```
# 进入 MinIO 目录cd ~/Desktop/MinIO# 1. 重新绑定客户端（确保连接正常）./mc alias set myminio http://192.168.29.147:9000 minioadmin minioadmin# 2. 给桶设置完全公开权限（包含目录列表+文件下载，解决点文件夹无反应）./mc anonymous set public myminio/anquanceshi# 3. 验证权限（必须返回 `public`，否则配置失败）./mc anonymous get myminio/anquanceshi# 4. 重启 MinIO 服务，让配置 100% 生效./mc admin service restart myminio
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xY9ZTT0gDw6hdyIgY6X7afmAJvAOmFBps0eIxXksDibO4j5uKOFick09371AEJDSohSb9YVaRKKP4kqBJ7ady7ZOcAXhgQEoiarzXctNXQFhpI/640?wx_fmt=png&from=appmsg)

7、匿名访问anquanceshi存储桶

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xY9ZTT0gDw7mibgrwbyJeiaE7rOyHjCFKtibeTMrJN0hOWdgricHAD06q7ukpW8OXPYico5pC6cqkSicOzDQruOmwrbvTFtIQGQItY6ItRqaJqjIE/640?wx_fmt=png&from=appmsg)

截止到这里漏洞环境搭建完毕。

三、案例演示

https://github.com/anthropics/skills/tree/main/skills/skill-creator

Trae相关的使用教程参考[基于Trae的AI自动化安全测试实战总结](https://mp.weixin.qq.com/s?__biz=MzkzMjk5MDU3Nw==&mid=2247484740&idx=1&sn=3a62e0cc4905d77278ea557791c2c20e&scene=21#wechat_redirect)

我们可借助 Trae 调用 skill-creator，快速生成MinIO 存储桶漏洞检测专用 Skill，实现一次生成、多次复用。本文仅提供技术实现思路，在实际使用过程中，仍需不断迭代优化 Skill 规则与检测逻辑，从而更精准地发现 MinIO 存储桶相关安全漏洞。

skill-creator：Anthropic 官方提供的 Skill 开发助手。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xY9ZTT0gDw5yWboekTEfqLuFotibqKia40icM9R60Mc5FBJrbCB5H8qrRBdOOgq6UlKjmCObfM8EBxTJDh7gLFJdXKjAjdQNtAwvI2ibCwb3LPY/640?wx_fmt=png&from=appmsg)

生成MinIO漏洞检测skill如下：

![](https://mmbiz.qpic.cn/mmbiz_png/xY9ZTT0gDw6vULuDWOTkxsxe62OXAfgqKwzTIBM3BNMxSznmJcnbmbZKiaufc9TRicyBicCrgLxWmbR6gEtibYCjYIoncAWEm3YEeAsjQNCkDIc/640?wx_fmt=png&from=appmsg)

Trae导入minio-vulnerability-scanner

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xY9ZTT0gDw6MOAyDcI2fX3Ilblrwhe1LZETzmnxYibFc7u05ZIM3rKRTeC7nHVKaNnaVNdhxOK09fOWBbXibLscNiaNfuB7szmczZuWUVcdcBo/640?wx_fmt=png&from=appmsg)

调用minio-vulnerability-scanner进行漏洞扫描

![](https://mmbiz.qpic.cn/mmbiz_png/xY9ZTT0gDw5E4N02riaxIZp2PlNtug6iaZ2HvGry9B63OhoEPEAkP7wRf53qf5lwbkonkUr7Or2gutQ1hIjyhtRaHDzxgnkKCibruRnhrGGe2E/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xY9ZTT0gDw7VXsZFO0s0m2RS2F9vnVyZj9dnfRG7ZiadPkTQLV1VUib86c4RKX0ghpIvxAStMcZGEvrzJeXTpMqr6niasxJQaH1yFJmjoia0CPU/640?wx_fmt=png&from=appmsg)

访问/anquanceshi路径，成功匿名访问存储桶

![](https://mmbiz.qpic.cn/mmbiz_png/xY9ZTT0gDw5FehST4WGn7iagILVEibPAqKiaoPTE3I3gTm0jKRIscHUEwmy57rJgibrwewIOcrJdviaANIUaRRykNnODQk4bQKRd9IpcIUdb510k/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/xY9ZTT0gDw6icA95A0DazyibBuBlgxdu0I7Uur9m9tX1sdyI3HkB0MSnTicBxt0hWuSGAm7f3bVUWzO1xGDMlWcNSGYJaqrWJefgrlYtJFCpDY/0?wx_fmt=png)

huan666

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/xY9ZTT0gDw6icA95A0DazyibBuBlgxdu0I7Uur9m9tX1sdyI3HkB0MSnTicBxt0hWuSGAm7f3bVUWzO1xGDMlWcNSGYJaqrWJefgrlYtJFCpDY/0?wx_fmt=png)

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