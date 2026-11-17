---
title: iOS 内存与诊断取证工具包：DSH 插件（15 个 ios_* 工具 + 右侧栏面板）、MCP server、代码健康扫描
url: https://mp.weixin.qq.com/s/Uu5DoWtkGKMegnMRrHwypQ
source: Doonsec's feed
date: 2026-11-16
fetch_date: 2026-11-17T09:55:26.738894
---

# iOS 内存与诊断取证工具包：DSH 插件（15 个 ios_* 工具 + 右侧栏面板）、MCP server、代码健康扫描

# iOS 内存与诊断取证工具包：DSH 插件（15 个 ios\_\* 工具 + 右侧栏面板）、MCP server、代码健康扫描

jqlong17
jqlong17

夜组安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

免责声明

由于传播、利用本公众号夜组安全所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号夜组安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉。谢谢！**所有工具安全性自测！！！VX：****NightCTI**

朋友们现在只对常读和星标的公众号才展示大图推送，建议大家把**夜组安全**“**设为星标**”，否则可能就看不到了啦！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icZ1W9s2Jp2WrOMH4AFgkSfEFMOvvFuVKmDYdQjwJ9ekMm4jiasmWhBicHJngFY1USGOZfd3Xg4k3iamUOT5DcodvA/640?wx_fmt=png&from=appmsg)

## 工具介绍dsh-ios-diag

> **一个 DeepSeek Harness（DSH）插件**，同时是一个 **stdio MCP server** 和一组命令行工具。 做三件事：**在模拟器上把能测的尽量测完**、**给真机做一次尽可能全的取证**、**把结论变成可交接的报告**。
>
> 对被测项目**只读**：不写它的代码、不写它的基线文档、不要求它加埋点。

![](https://mmbiz.qpic.cn/mmbiz_jpg/WibL3bOeESMJ4OncY3p5Nte807lfnQLu80WwqFwBEGIlUUwfOyucq24icXWqPia898PJbedeRqE7eDrBrPdCP9XB3XOmLoGPgKjQdjIdhY9LQw/640?wx_fmt=webp&from=appmsg)

## 1. 这个项目到底想解决什么

真机测试是一次高成本事件：设备、接线、装包、复现、抓数、传回。人不在电脑边时，这一天就废了。

所以目标不是「再做一个 Instruments」，而是：

| 目标 | 做法 |
| --- | --- |
| 装真机前尽量测完 | 模拟器上的内存曲线、类型下钻、日志、调用栈、pcap 解析、6 项体检 |
| 真机只跑一次 | 一次会话把内存/日志/崩溃/网络/栈都留下，离线分析（进行中） |
| 结论能交接 | 固定六段报告 + 带绝对路径的粘贴消息，开发拿去就能查 |
| 不碰被测项目 | 只读；临时文件写 `$TMPDIR` 并即删；报告写在本仓库 |

一句话：**把「感觉卡」变成「可比较的数字 + 可追溯的记录」。**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/WibL3bOeESMK1KichCIic4wuiaLT8qKn8a1KUbWCrsW9WC498zrZTTArjzAxFjl39T0khgxMqdHhpIRn9pEaMKN7spniasagLKkDVDXfMGddfLUo/640?wx_fmt=webp&from=appmsg)

## 2. 三种用法

| 形态 | 谁用 | 入口 |
| --- | --- | --- |
| **DSH 插件** | DSH 里的 Agent / 右侧栏面板 | 安装后出现 15 个 `ios_*` 工具 + 「内存」面板 |
| **MCP server** | Claude Code / Cursor / 其他 harness | `node bin/mcp.mjs` （stdio） |
| **命令行** | 人 / CI | `npm run health` 、`npm run report`、`npm run handoff` |

三者共用同一份内核（`core/`），工具行为不会分叉。

### 装进 DSH

```
# 在 DSH 里用 plugin_manager：install_bundle，target 指向本目录
# 之后新会话即可看到 ios_* 工具
```

### 接 MCP

```
{
  "mcpServers": {
    "ios-mem": {
      "command": "node",
      "args": ["/Users/ruska/projects/dsh-plugins/dsh-ios-diag/bin/mcp.mjs"]
    }
  }
}
```

> 不要把 MCP 再挂回 DSH：DSH 已经有同名原生工具，挂上去只会多出两份工具和第二个采样进程。

---

## 3. 能力清单（15 个工具）

| 工具 | 平台 | 回答什么问题 |
| --- | --- | --- |
| `ios_mem_targets` | 模拟器 | 哪些模拟器开着、里面哪些 App 在跑（bundleId + pid） |
| `ios_mem_start` / `ios_mem_stop` | 模拟器 | 开始/停止实时采样（默认 1s，保留最近 30 分钟） |
| `ios_mem_status` | 模拟器 | 当前/峰值/均值/增量、涨速、top 类别 |
| `ios_mem_detail` | 模拟器 | 此刻按镜像、按区域标签的排行（谁在吃） |
| `ios_mem_mark` | 模拟器 | 在时间轴打点（配合报告对齐操作） |
| `ios_mem_record` | 真机 | 录一段内存曲线（Activity Monitor，约 1Hz），回放 |
| `ios_mem_types` | 真机 | 录一段 Allocations，按分配类型排行 live bytes（VM 预留单独算） |
| `ios_mem_launch` | 模拟器 | 启动 App |
| `ios_log_query` | 模拟器 | 最近 N 秒的统一日志（`log show --style json`），可 grep |
| `ios_hang_sample` | 模拟器 | 采 N 秒调用栈（`sample`），回答「卡住时在干什么」 |
| `ios_preflight` | 模拟器 | 装真机前体检：6 项 pass/warn/fail + report.md |
| `ios_net_analyze` | 文件 | 解析 pcap → HTTP 请求/响应/WS 帧对象（tshark） |
| `ios_events_export` | 模拟器 | 把样本/打点/日志导出成统一事件表 + 链接 |
| `ios_events_query` | 文件 | 给 id / rpcId 查一跳邻居；链接分事实与推断 |
| （非工具）报告/交接 | 命令行 | `npm run report` / `npm run handoff` |

平台说明：**模拟器**指 App 跑在 Mac 上的模拟器进程；**真机**指 USB 连接的物理设备；**文件**指只处理本地文件，不需要设备。

---

## 4. 给 AI / Agent 的使用指南

### 4.1 典型工作流

```
装真机前    ios_preflight → 有问题先修
           ios_mem_start → 做操作 → ios_mem_mark("进入会话") → ios_mem_status
           → ios_log_query / ios_hang_sample 交叉看
           → ios_events_export → npm run report → npm run handoff
装真机后    ios_mem_record / ios_mem_types（真机录制）
有 pcap     ios_net_analyze → 对象进事件表
```

### 4.2 调用约定

1. \*\*先 `ios_mem_targets`\*\*，拿 `udid + bundleId`（或 pid）。不要猜 pid。
2. **pid 优先，bundleId 兜底**：传 `pid` 最快；只传 `bundleId` 会自动找。
3. **打点要贴着操作**：`ios_mem_start` → 操作 → `ios_mem_mark("刚做了什么")`。没有打点的曲线很难归因。
4. **别重复开采样**：同一时间只保留一个采样环；再次 `start` 会清空上一轮。
5. **真机工具会重新 launch App**（xctrace 的 `--launch`），别在操作中途调用。
6. **报告不要手写数字**：`ios_events_export` → `npm run report`，让规则算。

### 4.3 什么时候该用哪个

| 症状 | 先看 |
| --- | --- |
| 越用越卡 / 转圈 | `ios_hang_sample` （主线程栈）+ `ios_mem_status`（是否持续上涨） |
| 用一会儿闪退 | `ios_preflight` （崩溃项）+ 真机 `ios_mem_record`（是否接近 jetsam） |
| 消息没发出去 / 顺序乱 | `ios_log_query` （grep rpc/timeout）+ `ios_net_analyze`（pcap） |
| 不知道谁吃内存 | `ios_mem_detail` （模拟器）/ `ios_mem_types`（真机） |
| 改动后有没有退化 | `ios_mem_start` 跑同一场景，和上次报告比数量级 |

---

## 5. 数据模型：事件与链接

导出的一轮叫一个 **run**，落在 `docs/measurements/_runs/<时间>/`（不入库）。

```
// events.jsonl：一行一个对象实例
{"ts":"...","type":"mem_sample","id":"mem:1","sessionId":"run:...","rpcId":null,"pid":42,
 "attrs":{"totalMB":50.3,"top":"Malloc Nano"}}

// links.jsonl：一行一条链接实例
{"from":"mem:1","type":"contained_in","to":"run:...","method":"id","confidence":1}
{"from":"mem:21","type":"contained_in","to":"mark:1","method":"time","confidence":0.5}
```

**硬规则**：链接必须带 `method`（`id` = 有身份证的事实，`time` = 时间推断）和 `confidence`。 报告里两者分开展示；把推断当事实，比没有链接更糟。

---

## 6. 报告与交接

```
npm run report -- --run 20261114-1603 --project dsh-pocket-ios --title "内存采样"
npm run handoff -- --report docs/measurements/dsh-pocket-ios/<...>.md
```

* 报告固定六段：元信息 / 摘要 / 数据 / 异常与疑点 / 排查建议 / 复现。
* 交接消息带**绝对路径**，被测项目的 Agent 直接读文件，不用人肉转述。
* 目录约定：`docs/measurements/<项目>/<YYYY-MM-DD-HHMM>-<主题>.md`。

---

## 7. 代码健康扫描

```
npm run health -- --target /path/to/repo --project <slug> [--arch] [--coverage-json x.json] [--gate]
```

五个维度：文件规模（>400 行）、SwiftLint 结构规则、覆盖率（xccov）、未使用代码（Periphery）、 目标仓库自己的架构检查。Periphery 需要一次构建（`--periphery-project` + `--periphery-schemes`）， 本机已装但**真跑未验证**。`--gate` 任一不达标退出 1。对目标仓库只读。

## 工具获取

点击关注下方名片进入公众号

回复关键字【261116】获取下载链接

## 往期精彩

往期推荐

[CVE-2026-98260-小米 17 Pro Max（popsicle）一键 root · KernelSU 越狱模式 | 仅限自己持有并授权的设备](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247498015&idx=1&sn=e2af054c3379f3feb330b2bdee079f89&scene=21#wechat_redirect)

[AgenticPenTest  | Agent 协作渗透测试工作台](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247498014&idx=1&sn=fc8bb3e9c58a1dd597f89e4d015b3526&scene=21#wechat_redirect)

[CTF 线下赛用的离线 PHP 速查手册 | 11,930 条条目、196 条实战技巧、990 个payload、PHP 官方中文手册索引](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247498006&idx=1&sn=4d7a4c451c63c7dc94e9c5cba8cf6683&scene=21#wechat_redirect)

[DSH-purge 优化版：在上游 1.1.90 基础上恢复技能库 23 个技能、POC/EXP 知识库与本地靶场白名单、补齐 nuclei 模板类目](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247497977&idx=1&sn=94578857ff860b90a82631780b5f46a1&scene=21#wechat_redirect)

[最新ARL-Next二开版本 | 现代化资产测绘与漏洞监控平台](https://mp.weixin.qq.com/s?__biz=Mzk0ODM0NDIxNQ==&mid=2247497966&idx=1&sn=05bfdfd33d80077e4233f2176bcd0e38&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/OAmMqjhMehrtxRQaYnbrvafmXHe0AwWLr2mdZxcg9wia7gVTfBbpfT6kR2xkjzsZ6bTTu5YCbytuoshPcddfsNg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&random=0.8399406679299557&tp=webp)

预览时标签不可点

阅读原文

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/icZ1W9s2Jp2VCncNOrB9XcGmp7PvxTwhFI6coLAoicEQxHLUiavS75P3JVKAoEYOvX7LglrJhrt9K1tQU69LGjQGQ/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过