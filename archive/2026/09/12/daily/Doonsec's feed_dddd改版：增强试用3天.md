---
title: dddd改版：增强试用3天
url: https://mp.weixin.qq.com/s/BED_2gD7gT4nSK3cLjwotw
source: Doonsec's feed
date: 2026-09-12
fetch_date: 2026-09-13T07:01:08.823686
---

# dddd改版：增强试用3天

# dddd改版：增强试用3天

原创

白帽网安行
白帽网安行

白帽网安行

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

|  |
| --- |
| **声明：**dddd-pro 基于开源项目 SleepingBag945/dddd 做实战增强与持续维护。本文及本公众号发布的所有内容，仅供合法授权的安全测试、研究学习与运维排查使用。请务必遵守当地法律法规，禁止将文中技术用于任何未授权目标。因使用本文内容产生的任何直接或间接后果及损失，均由使用者本人承担，作者及本公众号概不负责。 |

**建议大家把公众号设为星标，否则可能就看不到啦！**因为公众号现在只对常读和星标的公众号才能展示大图推送。操作方法：点击右上角的【...】，然后点击【设为星标】即可。

**1.工具介绍**

dddd-pro 是基于开源项目 dddd带带弟弟 持续增强的实战版扫描工具（更新2026-09-12）我这边不是简单从 Git 里搬几个项目指纹拼进去，也不是纯 AI 堆砌功能，而是围绕真实使用场景，把 PoC、指纹、YAML、workflow 映射 一条一条补出来。

**2.功能亮点**

1.dddd-pro 目前主要做了这些增强：

2.新增并持续补充常用实战指纹与 PoC

3.每一条 PoC、指纹都尽量做过验证

4.修复部分影响实战体验的 bug

5.修复 MySQL 爆破等问题

5.优化 workflow / YAML 映射逻辑，减少误报和无效扫描

6.不堆无用功能，尽量把时间留给真正有价值的检测

7.支持 Windows / Linux 环境使用

相比一直git找指纹的做法，我更看重的是：

1.命中质量

2.扫描效率

3.误报控制

4.不定期持续更新指纹和poc

**3.使用效果**

dddd-pro 更适合下面这些场景：

1.红队打点

2.外网资产梳理

3.内网排查

4.安服项目

5.日常自测

整体思路还是围绕：

资产发现 → 指纹识别 → 漏洞映射 → POC 探测

![](https://mmbiz.qpic.cn/mmbiz_png/gnVEAZsRV1FoCibsOvWRdw9SW958XvbB7agv7ycUHicssz65lYjel8AxtOm4LNtWa8ACQBajSP0xjzPEp1lXek5uiblPY4C8PnB81vcru2ia6VM/640?wx_fmt=png&from=appmsg)

你可以拿我的版本和其它的版本实际对比下：

谁的误报更少

谁的扫描更快

谁的指纹更准

谁的 PoC 更实用

**4.使用建议**

这个版本更建议拿来做实战辅助与项目提效。

建议从 FOFA / Quake / 鹰图 导出资产后，新建 txt 进行导入：

1.更省积分

2.quake支持自动去重

3.更适合批量分组跑

4.也能减少重复探测和无效扫描

IP、IP:端口、URL 也可以直接写入 txt 文件，用 -t 参数直接导入，方便批量处理。

如果你在使用过程中发现误报、漏报，或者有更合适的指纹 / PoC，欢迎直接公众号留言，我会持续修改和补充。

**5.个别案例图**

1.某次攻防jeecg。

![](https://mmbiz.qpic.cn/mmbiz_png/gnVEAZsRV1Hicfibw6V5U5dNI5nR9L5iaJ7rRU41Awt4z8IIExyC3lA9gHwDUf9J3p7YulVCWM9aBFvtAib8VgPia1icIE3x3fEus6g5G6gVcgG1A/640?wx_fmt=png&from=appmsg)

2.二级目录下的nacos。

![](https://mmbiz.qpic.cn/mmbiz_png/gnVEAZsRV1GDEH2nESmO9MmXIOtZVaOLXjzxZe9sU5Jn9uZjlGib53ibndS3qthMTu0rdrchO4eINGia3LutPz2dapqaniamjNg4zkic2X8micgNQ/640?wx_fmt=png&from=appmsg)

3.某src高危1500元，任意文件读取。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gnVEAZsRV1Gh52wcymwiacmqtGwibICz0pjgkX67vA2P6HDt3bUM9IhlIxjd34pUBUp7DuDsb857jV9qdv7YRbV55IoawX3xmrJyGnkQYC7ibw/640?wx_fmt=png&from=appmsg)

4.帆软sql注入

![](https://mmbiz.qpic.cn/mmbiz_png/gnVEAZsRV1FoCibsOvWRdw9SW958XvbB7agv7ycUHicssz65lYjel8AxtOm4LNtWa8ACQBajSP0xjzPEp1lXek5uiblPY4C8PnB81vcru2ia6VM/640?wx_fmt=png&from=appmsg)

**6.反馈与更新建议**

若使用工具时遇到指纹误报、漏报问题，或是有优质指纹、POC 补充素材、功能优化思路，均可在公众号私信留言，我会持续迭代更新工具。

**7.试用、授权与获取方式**

7.1试用

1、新用户可自动试用 3 天，试用到期后需要正版授权。

```
2、正式授权：29 元/年/台。
```

7.2下载方式

**回复关键字【**dddd0912****】获取******下载链接**

7.3授权方式

扫码加入纷传获取正式授权。

![](https://mmbiz.qpic.cn/mmbiz_png/gnVEAZsRV1EH2ryfYJ8U9SDyqkUdO9pK41s4TsTQt8UNkJZBMGxOuM1Q1VKvvHdU96s2OAwNlzsH8AVBQBgHvuAKLgUib3rZN2PWoUl8ssSY/640?wx_fmt=png&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/gnVEAZsRV1HwSichOH56owfxvE0UIoFqFTcDRvApiaNHbQYfLQYhOFjiaQFics2iawpXgqMfDu3EOt975ibJYhDxw7IUjPJPIciaaLBM2fh2d76A28/0?wx_fmt=png)

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