---
title: FastLinLog - 轻量级Linux 日志安全分析工具
url: https://mp.weixin.qq.com/s/-jXp5gK5inBC3LNooqSnzw
source: Doonsec's feed
date: 2026-01-17
fetch_date: 2026-01-18T03:37:35.127878
---

# FastLinLog - 轻量级Linux 日志安全分析工具

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/XZByrJJ6uUxBnTBQHXzHFT9vic6F2aDf5qlymtHuUn1shJSXPBetuj8ic1OKSUxPKaQP3GnO4FOf9ickjEicGNWWyQ/0?wx_fmt=jpeg)

# FastLinLog - 轻量级Linux 日志安全分析工具

原创

vam876
vam876

W小哥

![]()

在小说阅读器中沉浸阅读

#

![](https://mmbiz.qpic.cn/mmbiz_png/XZByrJJ6uUxBnTBQHXzHFT9vic6F2aDf5xRNAfICaZsmVUUr5FtYfjZSXqPxnSRFic83Zz9WHqkgicI83LX0qoyibA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/XZByrJJ6uUxBnTBQHXzHFT9vic6F2aDf5qIrct7USbOOoD9P9fvERgL5FRCa85AFiadeUWgswn1yt7woArZqEIog/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/XZByrJJ6uUxBnTBQHXzHFT9vic6F2aDf5xRNAfICaZsmVUUr5FtYfjZSXqPxnSRFic83Zz9WHqkgicI83LX0qoyibA/640?wx_fmt=png)

## FastLinLog如何提升分析效率？

做Linux安全运维、攻防排查、应急响应，难免面临下面痛点：

·日志文件杂乱无章：xxx.log、xxx.log.1、xxx.log.2 分散存放，分析时要逐个处理，重复劳动累到吐；

·多服务器分析混乱：多台服务器日志分析，反复切换日志文件，手忙脚乱；

·日期识别踩坑不断：很多日志没有年份信息，跨年度分析时日期错乱，排查方向直接跑偏，手动调整工作繁琐；

·关键信息难挖掘：想找暴力破解、异常登录、权限变更等风险点，靠命令行筛选半天，还容易遗漏；

·分析结果无直观展示：一堆零散的日志文本，安全态势、攻击趋势没法可视化呈现，汇报全靠嘴说；

·中文事件映射：内置了100+中文事件映射，权限变更、密码修改、sudo执行一目了然

·AI分析赋能：Linux日志看不懂？一键将一条或者多条日志发送给AI分析。

![](https://mmbiz.qpic.cn/mmbiz_png/XZByrJJ6uUxBnTBQHXzHFT9vic6F2aDf529uPmGXGuOzWKTGicYgOlwgCnZQSOEClv1JpYdBWRK1IdSFWCk9zoqQ/640?wx_fmt=png)

**苦Linux日志安全分析久矣？告别 grep/awk/sed 组合拳折磨，安全日志秒级解析，安全风险一键洞察。现在，FastLinLog 一站式解决所有问题！集成AI能力，搭配专属提示词与上下文工程，把复杂的日志分析变成"点一点"的简单操作！**

![](https://mmbiz.qpic.cn/mmbiz_png/XZByrJJ6uUxBnTBQHXzHFT9vic6F2aDf5xRNAfICaZsmVUUr5FtYfjZSXqPxnSRFic83Zz9WHqkgicI83LX0qoyibA/640?wx_fmt=png)

## 核心功能 异于传统命令行分析

### 智能日志聚合 告别零散混乱

自动帮你"整理"日志，省去80%的准备工作：

·同类日志自动合并：针对轮转生成的xxx.log、xxx.log.1、xxx.log.2系列文件，以及按日期命名的xxx.log-20241215等格式日志，可自动识别归属为同一类日志完成聚合分析，全程无需手动归类整理；

·按IP自动分类归档：导入日志后，自动在 logs 目录下按主机IP创建分类文件夹，不同服务器的日志分门别类存放，折叠展开自由切换，查找某台主机的日志一眼就能找到；

·灵活导入方式：支持手动打开单个日志文件、选择整个文件夹批量导入，不管是本地日志还是从服务器下载的日志包，都能快速处理。

### 智能日期识别 告别分析跑偏

彻底解决日志无年份、日期错乱的痛点：

·基于文件名智能识别：自动解析日志文件名中的日期信息（如 secure-20241215、auth.log.2024-12-15），精准补全年份；

·时间轴自动校准：不同格式、不同时间段的日志，自动按时间轴排序整合，跨年度、跨月份分析再也不会出现日期混乱的问题。

### 可视化分析仪表盘 安全态势一目了然

把枯燥的日志变成直观的图表，关键信息不遗漏：

·核心态势概览：成功/失败登录次数、唯一登录用户数、唯一来源IP数、风险事件数一键查看；

·Top排行榜：自动统计活跃用户TOP10、来源IP TOP10、失败登录用户TOP10、攻击IP TOP10，可疑对象一眼锁定；

·多维度时间趋势：支持12小时、日、周、月、年5种时间粒度切换，直观查看登录趋势、攻击频率变化，轻松发现异常波动；

·多维度分布图表：事件类型（登录、权限变更、程序执行等），全面掌握日志核心信息。

![](https://mmbiz.qpic.cn/mmbiz_png/XZByrJJ6uUxBnTBQHXzHFT9vic6F2aDf51II97puDZpjiaMM1U6iaJPAkOzb8G9IP3CmIPW1JQx0cGdcI1Ieg9GYg/640?wx_fmt=png)

### 深度交互分析 精准定位问题

![](https://mmbiz.qpic.cn/mmbiz_png/XZByrJJ6uUxBnTBQHXzHFT9vic6F2aDf5Osrvnn99xAxdunhV7gOQrFiaWGBwRsrI4YpKzCuQm1iczSyLYgNiaOQAw/640?wx_fmt=png)

比命令行筛选高效10倍，精准挖掘关键信息：

·点击穿透溯源：点击任意IP、用户名，立即展示该对象的所有相关日志事件，完整还原操作轨迹；

·多条件组合过滤：支持按时间范围、操作结果（成功/失败）、事件类型（登录、异常退出、权限变更）等多条件组合筛选，精准锁定目标；

·全文搜索：输入关键词（如"sudo""failed""invalid user"），秒级检索，关键信息瞬间定位；

·数据溯源清晰：每一条分析结果都标注来源日志文件，聚合关系、数据出处一目了然，排查有据可依。

·时间范围筛选：支持自定义时间区间选择，深度洞察攻击痕迹

·多条件筛选： 多字段关联搜索，精准溯源

### 基于上下文工程知识库的AI分析 懂日志更懂安全

内置专属上下文工程知识库，无需额外配置，打开就能用的AI日志分析师！适配Linux日志场景，支持批量日志分析：

·实时对话解读：遇到看不懂的日志条目，直接复制给AI，秒级给出清晰解读，包括日志类型、关键信息、可能的风险等级；

·一键风险研判：选中可疑日志片段，点击"AI分析"，自动识别安全风险（如暴力破解尝试、异常权限操作），并给出排查建议；

·批量日志关联分析：支持选中多条日志批量提交AI分析，自动关联同一IP、同一用户、同一时间段的所有日志，还原完整操作链路，精准定位攻击路径与风险蔓延范围；

·

### 全面日志类型支持 覆盖所有核心场景

| 日志类型 | 说明 | 格式 | 解析能力 |
| --- | --- | --- | --- |
| **audit** | Linux系统审计日志（权限变更、文件操作等） | 文本 | 深度解析，提取关键操作详情 |
| **secure** | CentOS/RHEL系列安全认证日志 | 文本 | 深度解析，精准识别登录/认证事件 |
| **auth** | Debian/Ubuntu系列认证日志 | 文本 | 深度解析，适配不同发行版格式 |
| **btmp** | 失败登录记录 | 二进制 | 完整解析，提取失败用户名/IP/时间 |
| **wtmp** | 登录/注销记录（含成功登录） | 二进制 | 完整解析，还原登录会话信息 |
| **lastlog** | 用户最后登录记录 | 二进制 | 完整解析，快速查看用户登录状态 |

**正式版将支持更多的日志**

## 3步上手 零门槛

### 方式一：直接运行（推荐，小白友好）

1.下载 `FastLinuxLog.exe`（Windows）；

2.双击运行程序，无需安装任何依赖；

3.点击"刷新按钮"，即可加载logs目录下的日志；点击"打开日志"，选择单个日志文件，自动开始聚合分析，坐等结果！

### 方式二：从源码运行（开发者/进阶用户，暂未开源）

```
# 注：项目当前处于完善阶段，暂未开源# 开源后将同步发布完整源码与克隆地址# 如需体验，可通过方式一下载编译后程序运行# 使用PyInstaller打包，可以使用技术手段获取源码
```

### 推荐日志目录结构（自动识别，无需手动整理）

```
logs/
```

```
├── 10.10.10.49/           # 自动按服务器IP分类
```

```
│   ├── audit/
```

```
│   │   └── audit.log
```

```
│   ├── secure/
```

```
│   │   ├── secure
```

```
│   │   ├── secure.1
```

```
│   │   └── secure-20241215  # 带日期的日志
```

```
│   └── wtmp/
```

```
│       └── wtmp
```

```
├── 10.10.10.50/           # 另一台服务器日志
```

```
│   └── ...
```

```
└── local/                  # 本地主机日志
```

```
    └── auth.log
```

**提示：** 将日志放到程序运行目录的logs目录下，即使你的日志目录不规范，程序也能自动识别分类，推荐结构只是让分析更清晰！

关注公众号回复“20260117”获取工具地址。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/XZByrJJ6uUzKsSv7UficCMvNU3C1Khiayp4iabicKicKVePCZbMlUKFfStk6mX3Hpf6kh5Zl6vcUoOqGcELngiazX8rg/0?wx_fmt=png)

W小哥

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/XZByrJJ6uUzKsSv7UficCMvNU3C1Khiayp4iabicKicKVePCZbMlUKFfStk6mX3Hpf6kh5Zl6vcUoOqGcELngiazX8rg/0?wx_fmt=png)

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