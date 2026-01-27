---
title: 警惕！GNU Inetutils telnetd 9.8分高危漏洞来袭，附批量可视化检测工具
url: https://mp.weixin.qq.com/s/zt3kp5jevfqQTdEPR97UPg
source: Doonsec's feed
date: 2026-01-26
fetch_date: 2026-01-27T03:36:16.870693
---

# 警惕！GNU Inetutils telnetd 9.8分高危漏洞来袭，附批量可视化检测工具

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/704aYL39zURfzJBKWT0QKjAggMhLBo5CnzLMkicbkSFSibhpMK8yhtibxbTuhhD9jibbvgYkFNibibTU8VwpXaNyOgsA/0?wx_fmt=jpeg)

# 警惕！GNU Inetutils telnetd 9.8分高危漏洞来袭，附批量可视化检测工具

原创

灵泽
灵泽

灵泽安全团队

![]()

在小说阅读器中沉浸阅读

************-----------****

**工具简介**

-----------********

🔥 CVE-2026-24061 GUI检测与利用工具

这款工具专为CVE-2026-24061漏洞打造，采用图形化界面设计，无需复杂命令行操作，即可实现漏洞扫描、批量利用等核心功能。该漏洞源于GNU Inetutils telnetd的身份验证逻辑缺陷：telnetd会将客户端传递的USER环境变量直接转发给login程序，而当注入`USER='-f root'`时，login程序会触发免密登录机制，攻击者直接获取root权限。

⚠️ 关键说明：

- 影响范围：GNU Inetutils 系列 telnetd 服务

- 危害等级：严重（直接获取root权限，无权限边界）

- 修复建议：通过包管理器将 GNU Inetutils 升级至 2.7 以上版本。

************-----------****

**功能特性**

-----------********

🔍 漏洞扫描：全面覆盖，高效检测

- 多目标支持：单个IP、IP范围、CIDR网段全兼容

- 灵活导入：支持从TXT文件批量导入目标列表，适配大规模排查场景

- 高并发优化：最大支持1000线程并发扫描，扫描速度可按需调节

- 结果可视化：表格化展示目标主机、端口、漏洞状态，详细信息一目了然

- 报告导出：支持CSV/文本格式导出扫描结果，便于审计归档

⚡ 漏洞利用：一键拿权，交互便捷

- 批量管理：自动汇总漏洞目标，支持多终端同时连接

- 交互式Shell：连接成功后直接获得root权限终端，命令执行结果实时反馈

- 会话管理：标签页切换多会话，支持断开重连、命令历史回溯

- 极简操作：双击目标即可建立连接，无需记忆复杂payload

🎨 现代化UI：新手友好，体验流畅

- 暗色主题：护眼设计，长时间操作不疲劳

- 状态提示：实时显示扫描进度、连接状态、命令执行日志

- 容错机制：自动跳过超时、连接被拒的目标，任务不中断

- 日志追溯：完整记录操作过程，便于问题排查

************-----------****

**工具使用**

-----------********

🔧 前置准备

1. 环境要求：Windows 10/11 系统，Python 3.8+，建议4GB以上内存

2. 安装依赖：

```
# 克隆项目后进入目录pip install -r requirements.txt
```

3. 运行工具：

```
python cve_2026_24061_gui.py
```

📝 操作步骤

1. 漏洞扫描流程

- 添加目标：在输入框填写目标（支持多种格式），点击「添加目标」；或通过「文件导入」加载批量IP

- 配置参数：默认端口23（可自定义），并发线程100（1-1000可调）

- 启动扫描：点击「开始扫描」，实时查看扫描结果

- 导出报告：扫描完成后，点击「导出报告」保存结果

2. 漏洞利用流程

- 切换标签：点击「漏洞利用」，左侧显示已发现的漏洞目标列表

- 建立连接：双击目标IP:端口，自动完成payload注入与连接

- 执行命令：在终端输入框输入命令，按Enter或点击「执行」即可

- 关闭会话：点击标签页关闭按钮或「断开」，安全终止连接

************-----------****

**运行示例**

-----------********

![](https://mmbiz.qpic.cn/sz_mmbiz_png/704aYL39zURfzJBKWT0QKjAggMhLBo5C9jhIFX1fb7SaD54S92j4QIxiaice7jL7AiaxnzQn65kj6QtVr3ibU4Y3Rg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/704aYL39zURfzJBKWT0QKjAggMhLBo5CDw7eLJoFcoIntd4XARZHARjxXiafTAKDZUTdhLrXWmK5ZOrUW2WsGBg/640?wx_fmt=png&from=appmsg)

************-----------****

**下载地址**

-----------

关注公众号回复：260126********

**************-----------**

**免责声明**

**-----------**

文章所涉及内容，仅供安全研究与教学之用，由于传播、利用本文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任。************

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/704aYL39zUTenmVEUkwk7YdtlPKgKb5jfhEgibUVbUUraqWiaCELZuFYL7dPibRjiaN6Cprib7u23Dbayc8Gjee46ug/0?wx_fmt=png)

灵泽安全团队

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/704aYL39zUTenmVEUkwk7YdtlPKgKb5jfhEgibUVbUUraqWiaCELZuFYL7dPibRjiaN6Cprib7u23Dbayc8Gjee46ug/0?wx_fmt=png)

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