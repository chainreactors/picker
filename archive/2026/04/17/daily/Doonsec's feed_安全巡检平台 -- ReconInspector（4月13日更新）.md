---
title: 安全巡检平台 -- ReconInspector（4月13日更新）
url: https://mp.weixin.qq.com/s/v0kU_8m8iLTqs-EdXv3luw
source: Doonsec's feed
date: 2026-04-17
fetch_date: 2026-04-18T04:29:49.672931
---

# 安全巡检平台 -- ReconInspector（4月13日更新）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/U7LDNXUGXQthWlbAHNhF1w9dK7BOop1Ruv1emErcmnxHibzyjh7nJdwXspAdfJ460m7sRPQ1GzcSGaubRHam4SocT72lflrerGaGyMAhw0Bc/0?wx_fmt=jpeg)

# 安全巡检平台 -- ReconInspector（4月13日更新）

hzhsec
hzhsec

Web安全工具库

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

===================================

**免责声明**

请勿利用文章内的相关技术从事非法测试，由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。工具来自网络，安全性自测，大家都要把工具当做病毒对待，在虚拟机运行。如有侵权请联系删除。个人微信：ivu123ivu

**0x01 工具介绍**

安全巡检平台是我基于原项目持续二次开发后的自用安全工具，整体目标不是做一个大而全的平台，而是把日常巡检里最常用、最容易反复切换的几个环节集中到一个 GUI 里，提升验证效率。当前主要用于：

```
FOFA 资产测绘与结果整理Nuclei 批量扫描与结果查看漏洞模板编写、调试、验证响应包分析、正则验证、AI 辅助生成正则编码解码、哈希计算、HTTP 发包等常用小工具
```

**0x02 安装与使用**

1. FOFA 资产测绘

支持完整 FOFA 语法输入与自动编码

支持分页抓取、总页数获取、结果导出

支持 Cookie 配置与有效性检测

支持结果表格查看、存活探测与筛选整理

支持将结果联动发送给 Nuclei 模块继续验证

更改配置

![](https://mmbiz.qpic.cn/sz_mmbiz_png/U7LDNXUGXQtsl1WnV8xMD78Clr0jq90WDficeooZazTeCc8dibNJOVGOTEHQtiaNmjxmib1z0icktoSmbaib8NBRqQZxzq8JWiazyDGBdXuw7BxurI/640?wx_fmt=png&from=appmsg)

测试fofa爬取免费

![](https://mmbiz.qpic.cn/mmbiz_png/U7LDNXUGXQt2iaDYGdM9psub7ayCyEzqjEs8wvYQ672AsqgiaShoic6VttiavkibHhkL3z16UnsRbYPTQGEZYNZvDyl1VMqqh7oQjE08E18SRiaY8/640?wx_fmt=png&from=appmsg)

2. Nuclei 扫描

支持图形化配置 nuclei 路径、模板目录、输出目录

支持模板树浏览、搜索、勾选、编辑

支持批量目标导入与扫描结果实时展示

支持严重级别区分与结果输出

支持模板验证场景下的目标命中状态显示

![](https://mmbiz.qpic.cn/mmbiz_png/U7LDNXUGXQv5X7sCaxeoXUonH5tgcaHVof1icNVW8icBbwxTLbKTgzBB8v609DEbR3a8NiaNMayOe0VqF776upg1A07Lx7pcREdRTXAACPrbH0/640?wx_fmt=png&from=appmsg)

3. 漏洞模板工作台

支持根据 HTTP 请求/响应包快速生成模板

支持 AI 辅助生成模板

支持 AI 单独生成正则，而不是强依赖整份模板生成

支持正则调试、分组查看、响应样本验证

支持调试响应包查看

支持一键清空 AI 接口、模型、Key 和指令配置

![](https://mmbiz.qpic.cn/sz_mmbiz_png/U7LDNXUGXQtFgBQavROqnJQ6ia6DwcYCfff57O3zoVVm2O8jRKicdNiavsK6jCHnTOaHGVxibZwHL0Dxq1mDEbxpZt0PxXjx9TmicsBk422ukl2A/640?wx_fmt=png&from=appmsg)

4. 小工具集

内置多个常用安全测试辅助工具，通过左侧菜单切换：

| 工具 | 功能说明 |
| --- | --- |
| 🔤 编码/解码 | Base64、URL、Hex、HTML 实体的编码与解码 |
| 🔐 哈希计算 | MD5、SHA1、SHA256、SHA512 一键计算 |
| 📡 HTTP 发包 | 支持自定义方法/Header/Body/代理/SSL 的 HTTP 请求工具 |
| 📋 JSON 格式化 | JSON 美化、压缩、格式校验 |
| 🔗 URL 处理 | URL 结构解析，参数列表展开 |
| ⏱️ 时间戳转换 | Unix 时间戳与日期时间相互转换 |

![](https://mmbiz.qpic.cn/mmbiz_png/U7LDNXUGXQt9fkUibSK9WJ6dnH40sgfayS02MAJ010OxtFmCn48veicLqETt5hicN2lMQ86acsqLWkBSyVSckMD3X0xal4cRhLmhXOPKKYcHEI/640?wx_fmt=png&from=appmsg)

5. 调试与验证增强

修复了调试响应体中 JSON 内容被错误吞掉的问题

优化了目标命中结果和

http://host:port / host:port 的识别

调整了调试弹窗尺寸，避免窗口过大导致难以关闭

简化调试入口，仅保留响应包查看，减少误导

网盘下载链接（一定要在虚拟机运行）：

链接：https://pan.quark.cn/s/f5f7e571cedb

**·****今 日 推 荐****·**

|  |  |
| --- | --- |
| ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/U7LDNXUGXQvfU5QrfyvDI7w4eZELhFwNXOjlicksqBia88sj549GqcvIrANefTSIibVVzibZvkq0Pia4KEw9f6FIz4gIwziaLRUe5qwYmeTl3veE8/640?wx_fmt=jpeg&from=appmsg) | ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8H1dCzib3UibsC4yYFwgTnJrN0q57DearHJhaWSE6XQllpkUviaibg5MqTYgdUQYDNt8ysfV2v6o4jsN34pmq3DAOg/640?wx_fmt=jpeg&from=appmsg) |

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/8H1dCzib3UibvAJDLSoAcyS63uxfNryXVibVJx8MiaiaibYmLj4Zk1fPdTYCsDjIEEoiaF1BPQydFZornyvv10iarEPCkg/0?wx_fmt=png)

Web安全工具库

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/8H1dCzib3UibvAJDLSoAcyS63uxfNryXVibVJx8MiaiaibYmLj4Zk1fPdTYCsDjIEEoiaF1BPQydFZornyvv10iarEPCkg/0?wx_fmt=png)

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