---
title: 一款超级无敌的跨平台应急响应自动化分析工具
url: https://mp.weixin.qq.com/s/rgrPapBdp6li7d1ATjzNqw
source: Doonsec's feed
date: 2026-02-18
fetch_date: 2026-02-19T04:19:12.004350
---

# 一款超级无敌的跨平台应急响应自动化分析工具

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/veA9QmcJk5kffqvY2EkSzTcnKgkaiaeeSToUyic9aHYHfh0hmyDKQ2vLGsS4vvIKY2hRhCbMXXB4ly6XKBGsfREw/0?wx_fmt=jpeg)

# 一款超级无敌的跨平台应急响应自动化分析工具

菜狗
菜狗

只会看监控的实习生

![]()

在小说阅读器中沉浸阅读

## 🚀 一句话优势

只用 管理员/Root 权限跑一条命令，日志 + 进程 + 内存 + 网络 + 注册表 全维度扫描，10 分钟生成「老板能看懂」的交互式报告。

## 🎯 核心能力速览

| 维度 | 检测细节 |
| --- | --- |
| **日志审计** | Win 安全日志（RDP 暴力/日志清除/账户异动）；Linux syslog（SSH 爆破/sudo 滥用） |
| **进程 & 内存** | DLL 注入、进程镂空、内存马、隐藏进程、Kernel Module |
| **持久化** | 服务、计划任务、启动项、COM 劫持、WMI Event |
| **网络** | 实时连接、监听端口、C2 通信特征（可对接微步 API 自动标记） |
| **文件系统** | 可疑 PE、无签名驱动、时间戳篡改、敏感目录变更 |
| **MITRE 映射** | 自动关联 TTP，报告内直接显示 ATT&CK ID |

![](https://mmbiz.qpic.cn/sz_mmbiz_png/veA9QmcJk5kffqvY2EkSzTcnKgkaiaeeSWGO925Hxp4ciakRlG4fsdSgu3iaE34slicibS3qiaib1gnEyYicnYRBpbhSug/640?wx_fmt=png&from=appmsg)

## 📊 报告格式（任选其一）

1. HTML – 交互式 Web，左侧树形导航，右侧详情高亮
2. JSON – 结构化，方便 SIEM/SOAR 自动摄取
3. CSV – Excel 直接透视，运维小姐姐也能用

## 🔧 零依赖「抗对抗」架构

1. Windows → 纯 Native API 访问进程/内存/注册表，不碰 Win32k
2. Linux → 直接解析 /proc & kmod，无需额外驱动
3. 插件化 – 50+ 检测插件热插拔，自定义 YAML 即可扩展

## ⚡ 快速开始

```
# ① 下载单文件绿色版（Win/Linux 通用）
wget https://github.com/your-repo/Sentinel/releases/latest/download/sentinel

# ② 赋权 & 运行
chmod +x sentinel && sudo ./sentinel --report html

# ③ 打开报告
firefox Sentinel-Report-$(date +%F).html
```

## 🧪 实战截图（文本版）

```
[✓] Windows Security Log Audit  –  3 可疑登录
[✓] Process Injection Scan      –  1 镂空进程 (PID: 4123)
[✓] Memory Shell Detection      –  0 内存马
[✓] Persistence Check           –  2 异常计划任务
[✓] Network C2 IoC              –  1 微步红线 IP (45.33.12.7)
[✓] MITRE ATT&CK Map            –  T1055, T1053, T1078
```

## 🛠️ 插件示例（新增只需 5 行 YAML）

```
name: detect_hidden_user
desc: 检测 >1000 UID 的隐藏账户
platform: linux
query: |
  awk -F: '$3>=1000 && $3<65534 {print $1}' /etc/passwd
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/veA9QmcJk5kffqvY2EkSzTcnKgkaiaeeS63fIlrV8dqlaDibzibPHP2xCghWticjaDeZBkQUxKKZe3hstLHMqcxBSA/640?wx_fmt=png&from=appmsg)

## 🔐 安全与合规

* 只读运行 – 不会修改任何系统数据
* 本地报告 – 不上传任何信息到外部服务器
* 权限自检 – 启动前提示管理员权限确认，避免误报
* 审计日志 – 所有操作本地留痕，方便内审

## 📈 路线图

* v2.1 – 内存镜像 dump、YARA 规则扫描
* v2.2 – 云端 IoC 订阅、钉钉/飞书机器人推送
* v2.3 – Windows 内核回调 rootkit 检测

## 关注回复Sentinel获取

##

## 低价出售安全证书不限于cisp、pte等请Vme～建了一个项目群，想进群的请回复进群即可

![](https://mmbiz.qpic.cn/sz_mmbiz_png/veA9QmcJk5lzhNyGuZayDXYNGMSSt2Y4jyZLV2iajH8ia4dJQb2KBu2MJj6ZGENtDskIckNqCFktTwxvgPxCQ8VA/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/veA9QmcJk5kUQJmQM134YCWRBafRBbfXz9sIbia1l4QFsiajaOk55RIfHNiaqLnOF3beiciaVvFy1w2jGa5QbGE82Tw/0?wx_fmt=png)

只会看监控的实习生

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/veA9QmcJk5kUQJmQM134YCWRBafRBbfXz9sIbia1l4QFsiajaOk55RIfHNiaqLnOF3beiciaVvFy1w2jGa5QbGE82Tw/0?wx_fmt=png)

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