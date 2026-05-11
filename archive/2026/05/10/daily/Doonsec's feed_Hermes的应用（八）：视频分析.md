---
title: Hermes的应用（八）：视频分析
url: https://mp.weixin.qq.com/s/TjQ5Na5gLE-b2Xzo-yFqoQ
source: Doonsec's feed
date: 2026-05-10
fetch_date: 2026-05-11T05:51:45.321638
---

# Hermes的应用（八）：视频分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/2PhZXrB0gN5zHRL63Ac4h6VXXrjibricVko7s5Q01hxic2LAoht9BQ475OxzgerUlcf76hTv7Ykicbe439W8JrVfXwceJSyLvcicPicfUAGeRSLBs/0?wx_fmt=jpeg)

# Hermes的应用（八）：视频分析

原创

MicroPest
MicroPest

MicroPest

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

Hermes升级到13后，增加了一个新功能：视频分析。决定试一下，

先在Hermes中切换个视觉LLM，就用QWen3.5-397b-a17b。

上传个测试视频到/home/kali/CVE.mp4。

一会整出了报告：

CVE.mp4 视频内容分析报告

    📋 基本信息

    - 文件路径: /home/kali/CVE.mp4

    - 文件大小: 1.87 MB

    - 时长: 40.5 秒

    - 分辨率: 1152x720 (60fps, H.264)

    - SHA256: a324d81bf4a4321654b3bce7a906c12e8ad942e3c4fa4ef8a269c1bc3243714

    🎬 视频内容概述

    这是一个 vRX 漏洞管理平台 的产品演示视频，展示了 CVE 漏洞的发现、脚本化修复和自动化 remediation 流程。

    📊 关键画面分析

    第 1 秒 - 主仪表板界面

    显示 vRX 平台的主 Dashboard，包含以下模块：

    - 顶部导航: Scripts | Assets | Vuln Discovery | Vuln Remediation | Automation | Reports

    - 资产风险概览:

      - High Risk（高风险）

      - Medium Risk（中风险）

      - Low Risk（低风险）

    - 资产状态: Online / Offline

    - CVE 趋势图: 显示 1144 个资产，266 个新发现

    - 风险地图: 展示攻击面和已知漏洞

    第 10 秒 - 脚本库界面

    显示 CVE 修复脚本列表：

    - CVE-2025-8088: WinRAR 漏洞缓解脚本

    - CVE-2024-30080: Windows MSMQ 相关漏洞修复脚本

      - 功能：禁用 MSMQ 相关服务以减少暴露面

      - 包含检测和修复两个脚本

    - 支持标签筛选和高级搜索

    第 20 秒 - 脚本执行界面

    展示运行脚本的流程：

    - 选择要执行脚本的目标资产

    - 支持批量资产选择

    - 可针对 Windows/Linux/Mac 多平台

    第 30 秒 - 活动日志界面

    显示最近的自动化执行记录：

    - 活动类型: Run Script (Windows/Linux)

    - 漏洞 ID: 822864 等

    - 执行状态: Succeeded / Finished

    - 时间戳: 2025 年 12 月 8 日 03:45PM (GMT-3)

    - 目标资产: MORTEMWIOP 等

    🔍 涉及的关键 CVE

    | CVE 编号 | 描述 | 修复方式 |

    |----------|------|----------|

    | CVE-2025-8088 | WinRAR 漏洞 | 检测 + 缓解脚本 |

    | CVE-2024-30080 | Windows MSMQ 远程代码执行 | 禁用相关服务 |

    🏢 产品信息推断

    vRX 似乎是一个企业级漏洞管理平台，提供：

    1. 资产发现与盘点 - 自动识别在线/离线资产

    2. 漏洞扫描 - 集成 CVE 数据库

    3. 脚本化修复 - 预置/自定义修复脚本

    4. 自动化编排 - 批量执行修复

    5. 合规报告 - 风险趋势、执行日志

    📁 提取的中间文件

    - /tmp/cve\_first\_frame.jpg - 第一帧截图

    - /tmp/frame\_10s.jpg - 第 10 秒帧

    - /tmp/frame\_20s.jpg - 第 20 秒帧

    - /tmp/frame\_30s.jpg - 第 30 秒帧

    - /tmp/ocr\_\*.txt - 各帧 OCR 文本

需要我进一步分析特定帧的详细内容，或者提取更多时间点的画面吗？

好，提取视频第12秒的画面，截图如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2PhZXrB0gN7CIATGX0VcyTcgYiaPVkw911F2WUhImoxGwj0jodZDb3otCwR8wSfRz5pkibEHS8r5ZibQI1ysnOuX5Q6ykZTC7HhojLdZaEoM3I/640?wx_fmt=png&from=appmsg)

看看Hermes的提取结果：

![](https://mmbiz.qpic.cn/mmbiz_png/2PhZXrB0gN7TsW64hBCnEAxg3jA7qYgp7SD1wWNTPLVxqmYIky6BDolSztVj2QeyT94egKaRoHS1g02elIOmib92w5Libib5zgBjRo4zpvXIDU/640?wx_fmt=png&from=appmsg)

12秒的分析截屏和视频一模一样。

Hermes的这个功能还是很不错的。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpI857XC5Kft3W5TyR4cickrqaIUibKveibjF4531l9HGGu8dISFz0Yr6OUkCHfulChWC2acVmh4b39dg/0?wx_fmt=png)

MicroPest

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/2hnvgPYNzpI857XC5Kft3W5TyR4cickrqaIUibKveibjF4531l9HGGu8dISFz0Yr6OUkCHfulChWC2acVmh4b39dg/0?wx_fmt=png)

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