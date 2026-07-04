---
title: GitHub 开源 FOFA 桌面客户端 superfofa｜Windows/macOS 全平台可用
url: https://mp.weixin.qq.com/s/hBnivbQq7pUo9XFH0IKf6w
source: Doonsec's feed
date: 2026-07-03
fetch_date: 2026-07-04T05:45:40.531567
---

# GitHub 开源 FOFA 桌面客户端 superfofa｜Windows/macOS 全平台可用

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Iia3YpFmLXXlU0sYCoatZecXAtHq5h2VjJ0zrTKej3LL9pSe5Z2eibfrRtDYCs2yomhXhryVjlH7HnTjIlHEOq7HDQHIW8aEKibKDHOVwA2ukc/0?wx_fmt=jpeg)

# GitHub 开源 FOFA 桌面客户端 superfofa｜Windows/macOS 全平台可用

原创

polite007
polite007

星航安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

最近写了新东西，叫 **super-fofa**。

起因比较简单：我用 FOFA 频率很高，长期下来有一些自己用着不顺手的地方，想按自己的方式重新组织一遍。于是写了个桌面客户端，自己用着合适，打包发出来，给有相似需求的同学用。

## 它是什么

一个跨平台的 FOFA 桌面客户端，macOS 和 Windows 双端原生支持，单文件开箱即用。本地 SQLite 存账号、任务、查询历史，关机重启不丢数据。

界面分五个标签页，逐个说一下。

### 1. 资产搜索

用得最多的一页。多标签页查询、字段预设、历史记录、分页，长查询自动等比放大不截断。结果里点 IP 跳主机画像，点「导出」进批量任务，免去在多个界面间反复切换。

![资产搜索](https://mmbiz.qpic.cn/sz_mmbiz_png/Iia3YpFmLXXlkyGqNFBzXiaQLjIgMO9uDEiaxHeyPJYEZfeAVlR9RwtS1icia0eGVA14txlwANysSDuiaxKKLyTjjITlPHM1HuvpyicCKIPRBlLgTw/640?wx_fmt=png&from=appmsg)

### 2. 查询热搜

聚合了 FOFA 上的热搜查询，可以直接看到当前常见的查询语法，点一下就能用。适合不知道从何下手时找找方向，或者对照别人的思路调整自己的查询。

![资产搜索](https://mmbiz.qpic.cn/sz_mmbiz_png/Iia3YpFmLXXnicdZTcxC5InfjJOlgUSiaJR6gpic7xwoexJ8S6NgIIbcvzXWFIm0yj2yHmBg9oWiblk1KheRG3ttTmrl9YUb5o1cKCtg7jo7KtXA/640?wx_fmt=png&from=appmsg)

### 3. 主机画像

IPv4 主机画像查询，分普通 / 详情双模式，仪表盘式布局：Hero 卡 + KPI + 端口卡片，一屏看全端口、Banner、证书、组件。

> 说明：详情模式对应 FOFA 接口的 `detail=true`，接口本身响应较慢，会出现超时，属正常现象。

![主机画像](https://mmbiz.qpic.cn/mmbiz_png/Iia3YpFmLXXk8plmOJiaLFHAzAoIe3tGVEibibGS1FXcGQxy2zqKRWHb6SbtdMmoDsNXO557ObLfq1Y7dGH0hIqaKzgUvBUic54xr8cGhnRIp2Us/640?wx_fmt=png&from=appmsg)

### 4. 聚合统计

基于查询结果按字段聚合，多字段并行统计，TopN 可调，同时显示占比与计数。做资产分布分析、写报告数据章节时，比在 Excel 里拼透视表快不少。

![聚合统计](https://mmbiz.qpic.cn/sz_mmbiz_png/Iia3YpFmLXXlMDOShNvQWTtb1MWibiaQo1RSvZlBm6PoNNicg8tHcRibibPVZRXicGWyS8iaqztAKkAFrZAf6iaD2cK834Fo26yhyXOUpRdgLmwJ1nUU/640?wx_fmt=png&from=appmsg)

### 5. 批量导出

这个功能是写这个 App 的起点。支持多输入源（FOFA 多语法 / 纯 IP / host / domain）、字段自选、断点续传、暂停 / 恢复 / 重试，最终输出 XLSX。任务中途网络中断或 Key 切换不会从头再来。

![批量导出-任务列表](https://mmbiz.qpic.cn/sz_mmbiz_png/Iia3YpFmLXXkdHibdvj5mtnH1ZJvvoVibNPEicaMhSBqqEtD8bgR0Edibd95nwt5tcibBdPMCOzXkOKTLCWv4JLtWiaPVrRf5Q00XzcRBLQ5ib9ibqKw/640?wx_fmt=png&from=appmsg)

![批量导出-新建任务](https://mmbiz.qpic.cn/mmbiz_png/Iia3YpFmLXXkeasLhxbHWnHyOv4IoYINAVq79npyCK8CnrwvcwamaZmkkXDFqHD57icgrw5P1ECibY0xgrrhLhN4OpWGVYJqTibfADic0qJzLslI/640?wx_fmt=png&from=appmsg)

## 多 Key 管理

做大数据量采集绕不开多账号。super-fofa 的账号管理页支持：

* 多账号录入（FOFA Email + API Key）
* 三种使用模式：顺序轮询 / 单 Key / 多 Key 随机
* 大数据量场景建议选「多 Key 随机」，从有效账号池中随机抽取，分散请求压力
* 可配置 BaseURL 和代理，适配审计环境
* 录入时内置联网检测，Key 状态当场可见

![多 Key 管理](https://mmbiz.qpic.cn/sz_mmbiz_png/Iia3YpFmLXXk1KHVdMAria5guDdPj168qNZxeevk2NCVqZnv4cllmCKolbicicEoOXoGDqkAaFDtwZicTIOuBm24d1wbJmzPF5fE1rhwNedmajRs/640?wx_fmt=png&from=appmsg)

## 上手三步

1. 去 Releases 下载对应平台的压缩包，解压
2. 打开 App →「配置」页 → 新增账号 → 填 Email + API Key → 点「检测」
3. 回到「查询」页，输入 FOFA 语法开搜

没有可用账号时，查询会自动跳到配置页引导添加。

下载地址：`https://github.com/polite-007/superfofa/releases/latest`

| 平台 | 文件 |
| --- | --- |
| macOS Apple Silicon | superfofa-macos-arm64.zip |
| macOS Intel | superfofa-macos-amd64.zip |
| Windows x64 | superfofa-windows-amd64.zip |
| Windows ARM64 | superfofa-windows-arm64.zip |

> macOS 首次打开被 Gatekeeper 拦截：右键 → 打开，一次即可。
> Windows 被 SmartScreen 拦截：「更多信息」→「仍要运行」。

## 几种常见用法

* **大数据量采集**

  ：批量导出 + 多 Key 随机 + 字段精简
* **不知从何查起**

  ：先看热搜页，对照常见语法思路
* **主机信息深挖**

  ：搜索结果中 IP 直接点画像，串联查询链路
* **报告数据章节**

  ：先聚合统计看分布，再批量导出拉明细

## 写在最后

代码暂未公开，但 Releases 会持续更新，Issues 区我也会跟进。有想法、有 bug、有使用问题，直接在 Issues 提就行，我都能看到。

如果你也有类似的需求，欢迎下载试用，顺手给个 Star，这是对我的最大鼓励！

项目地址：`https://github.com/polite-007/superfofa`

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/2PtVLqE2NK8AQeR1NKoF3ye4OHFjUMlQrW8GbOmpmuY1icjPwPFENhWIZWD2HcJNWc9UKNT4l8xxoES0d77th7w/0?wx_fmt=png)

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