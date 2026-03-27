---
title: Wazuh 实战：Agent 掉线告警从 Level 3 到三层防御体系
url: https://mp.weixin.qq.com/s/O_RDFEbKzI7ypGE_Fc4ebA
source: Doonsec's feed
date: 2026-03-26
fetch_date: 2026-03-27T04:29:09.238527
---

# Wazuh 实战：Agent 掉线告警从 Level 3 到三层防御体系

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/AFibuxM1dR06GibVIvUGbibaibiau6cH1GeGyWyyQ7OxL7ztTLwuZJgX7KuoTbjRm9pLBtlWzFT6nxGeM1eMxFKApr5TZmjJByvbyIWTgiauDeNfc/0?wx_fmt=jpeg)

# Wazuh 实战：Agent 掉线告警从 Level 3 到三层防御体系

原创

imBobby
imBobby

imBobby的自留地

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_jpg/aiarKdLqgA03WnWPAjBGz2B95Oic2vQcyHrMSnXLVg0dq9pdUDGx0zLRJdOibthLbaqrAOQS1C7eNlXTf0oDFRGicQ/640?wx_fmt=webp&from=appmsg)

## 背景：默认配置下，掉线经常“看不见”

Wazuh 内置的 Agent 掉线规则 `504` 默认是 `Level 3`。
在多数生产环境里，这个级别通常低于主告警推送阈值，结果就是 Agent 已经离线，但 SOC 不一定收到通知。

这种默认值并非错误设计。Wazuh 的出发点是控制噪音：短时网络抖动、例行重启都可能导致暂时断连。
但在安全运营视角下，终端失联是需要尽快确认的事件，因为攻击者拿到主机权限后，常见动作之一就是先停掉 Agent。

目标是把“掉线不可见”调整为“1 分钟内可感知”，同时尽量避免误报泛滥。

## 内置规则 503/504 与触发链路

`503/504` 定义如下：

```
<!-- /var/ossec/ruleset/rules/0015-ossec_rules.xml --><rule id="504" level="3">  <if_sid>500</if_sid>  <options>alert_by_email</options>  <match>Agent disconnected</match>  <description>Wazuh agent disconnected.</description></rule>
<rule id="503" level="3">  <if_sid>500</if_sid>  <options>alert_by_email</options>  <match>Agent started</match>  <description>Wazuh agent started.</description></rule>
```

典型触发过程：

1. Agent 心跳超过阈值未到达（默认 `agents_disconnection_time=10m`）
2. Manager 的监控模块将 Agent 标记为 `disconnected`
3. 规则 504 命中，但由于级别低，不一定进入推送链路

## 规则提级：`overwrite` 与子规则的取舍

Wazuh 有两种常见改法。

### 方案 A：`overwrite="yes"` 直接覆盖

```
<rule id="504" level="12" overwrite="yes">  <if_sid>500</if_sid>  <match>Agent disconnected</match>  <description>Wazuh agent disconnected.</description></rule>
```

优点是简单，改动小。
不足是扩展性有限，后续按资产分级、按字段附加条件时可操作空间较小。

### 方案 B：新增子规则继承

```
<group name="custom_agent_disconnect">
  <rule id="100504" level="12">    <if_sid>504</if_sid>    <description>终端掉线告警: Wazuh Agent 已断开连接</description>    <group>agent_disconnect</group>  </rule>
  <rule id="100503" level="12">    <if_sid>503</if_sid>    <description>终端恢复上线: Wazuh Agent 已重新连接</description>    <group>agent_disconnect</group>  </rule>
</group>
```

采用子规则的原因：

1. 便于后续做资产分层（关键资产高等级、普通资产低等级）
2. 更容易追加匹配条件（主机名、分组、日志字段）
3. 不直接改写内置规则，升级兼容性更好管理

例如只对关键节点提到 P0：

```
<rule id="100514" level="12">  <if_sid>504</if_sid>  <match>critical-server</match>  <description>关键资产 Agent 断连</description></rule>
```

## 落地配置与权限

写入规则文件 `/var/ossec/etc/rules/custom_disconnect.xml`：

```
sudo tee /var/ossec/etc/rules/custom_disconnect.xml > /dev/null << 'EOF2'<group name="custom_agent_disconnect">
  <rule id="100504" level="12">    <if_sid>504</if_sid>    <description>终端掉线告警: Wazuh Agent 已断开连接</description>    <group>agent_disconnect</group>  </rule>
  <rule id="100503" level="12">    <if_sid>503</if_sid>    <description>终端恢复上线: Wazuh Agent 已重新连接</description>    <group>agent_disconnect</group>  </rule>
</group>EOF2
sudo chown root:wazuh /var/ossec/etc/rules/custom_disconnect.xmlsudo chmod 640 /var/ossec/etc/rules/custom_disconnect.xml
```

这里把 `503`（恢复上线）同步提级，是为了形成完整生命周期：
“掉线 -> 恢复”能在同一告警通道里闭环，而不是靠人工二次确认。

## 缩短检测窗口：从 10 分钟到 1 分钟

`ossec.conf` 的 `<global>` 段里有两个关键参数：

| 参数 | 默认值 | 作用 |
| --- | --- | --- |
| `agents_disconnection_time` | `10m` | 多久没心跳后标记掉线 |
| `agents_disconnection_alert_time` | `0` | 掉线后多久触发告警 |

可配置为：

```
<global>  <agents_disconnection_time>1m</agents_disconnection_time>  <agents_disconnection_alert_time>0</agents_disconnection_alert_time></global>
```

按默认 10 秒心跳计算，`1m` 等价于连续约 6 次心跳丢失才判定掉线。
这通常可以过滤瞬时网络抖动，同时把响应速度提升到分钟级。

改完后重启：

```
sudo systemctl restart wazuh-manager
```

## 已知盲区：`systemctl stop` 可能不触发 504

生产里最容易被忽略的点，是“优雅停止”路径。
`systemctl stop wazuh-agent` 在 Wazuh 语义中可能被视为正常停机动作，不一定被当作异常断连告警（社区长期讨论见 issue `#15153`）。

这意味着：仅依赖 504 规则时，主动停 Agent 的行为可能被绕过。

## 第二层：Agent 侧 Auditd 审计补位

在 Agent 节点添加命令审计规则，覆盖常见停 Agent 命令：

```
sudo tee /etc/audit/rules.d/wazuh-agent-protection.rules > /dev/null << 'EOF2'-a always,exit -F arch=b64 -S execve -F exe=/usr/bin/systemctl -k wazuh-agent-stop-a always,exit -F arch=b64 -S execve -F exe=/usr/bin/killall -k wazuh-agent-stop-a always,exit -F arch=b64 -S execve -F exe=/usr/bin/pkill -k wazuh-agent-stopEOF2
sudo augenrules --load
```

这样即便后续 Agent 被停止，执行动作本身也会先留下审计轨迹并上报。
这层主要解决“谁执行了停服务命令”的可追溯性问题。

## 第三层：Manager 端轮询兜底

如果攻击者同时干掉 Agent 与审计链路，仍需最后兜底。
可在 Manager 侧每分钟轮询 Agent 状态并推送通知：

```
#!/bin/bash# /usr/local/bin/check-wazuh-agents.sh
AGENT_OUTPUT=$(/var/ossec/bin/agent-control -l 2>&1) || exit 1AGENT_LIST=$(echo "$AGENT_OUTPUT" | grep -E "^\s*[0-9]+" | grep -v "^\s*000")
while IFS= read -r line; do    STATUS=$(echo "$line" | awk '{print $4}')    [[ "$STATUS" != "Disconnected" ]] && [[ "$STATUS" != "Never" ]] && continue
    NAME=$(echo "$line" | awk '{print $2}')    # 在此调用飞书/钉钉/企微 webhook    # 示例: curl -X POST ...done <<< "$AGENT_LIST"
```

通过 `cron` 每分钟执行，可以把“完全离线”场景也纳入检测范围。
如果基础设施已接入 Prometheus，也可使用 `wazuh-prometheus-exporter + Alertmanager` 替代自研脚本。

## 可选补充：Active Response

Wazuh 还可对 504 触发 Active Response，在 Manager 执行自定义通知脚本：

```
<command>  <name>disconnect-handler</name>  <executable>disconnect-handler.sh</executable>  <timeout_allowed>no</timeout_allowed></command>
<active-response>  <disabled>no</disabled>  <command>disconnect-handler</command>  <location>server</location>  <rules_id>504</rules_id></active-response>
```

其中 `<location>server</location>` 是关键配置。
因为离线 Agent 上已无法执行本地动作，通知逻辑必须在 Manager 端完成。

需要注意：Active Response 可以增强通知链路，但无法单独解决 `systemctl stop` 盲区。

## 三层覆盖矩阵

| 场景 | Wazuh 掉线规则 | Auditd 审计 | Manager 轮询 |
| --- | --- | --- | --- |
| `kill -9` 杀进程 | 能检测 | 不能 | 能检测 |
| 网络中断/主机断电 | 能检测 | 不能 | 能检测 |
| Agent 崩溃 | 能检测 | 不能 | 能检测 |
| `systemctl stop` 优雅停止 | 可能漏检 | 能检测 | 能检测 |

三层叠加后，大多数失联路径都能覆盖到至少两条检测链。

## 一次实际排障复盘

策略上线后，凌晨出现两台 Agent 几乎同时掉线。
排查顺序按“多 Agent 同时异常优先看 Manager 侧”执行，先在 Manager 日志发现大量 `Failed to enqueue element`，指向 InventoryHarvester 队列阻塞。
随后在其中一台宿主机定位到 Docker 容器未设置内存限制，触发全局 OOM，连带影响 Agent 进程。

最终修复动作：

1. 为相关容器补齐内存限制
2. 将 `syscollector` 扫描频率从 1 小时调整到 12 小时，降低队列压力
3. 重启 Manager 并确认 Agent 自动重连

这次事件里，分钟级告警到达和“掉线/恢复同通道可见”对排障效率帮助很明显。

## 上线顺序（按步骤）

1. 先完成 `503/504` 提级，确认推送链路打通
2. 再把断连判定窗口缩到 `1m`，观察一周噪音水平
3. 最后补齐 Auditd 与轮询兜底，覆盖优雅停止盲区

这样做的目标不是单纯“拉高告警级别”，而是建立一条可追踪、可闭环、可运营的终端在线性监控链路。

## 参考资料

### Wazuh 官方文档

* Custom Rules - 自定义规则、继承与覆盖
* Global configuration (`ossec.conf`) - 断连判定相关参数
* Active Response - 规则触发后的服务端动作
* Agent connection management - Agent 在线状态机制
* Wazuh API reference - 状态查询与集成接口

### 规则与社区讨论

* 0015-ossec\_rules.xml - 内置规则 `503/504` 源码
* Issue #15153 - `systemctl stop` 相关断连告警讨论
* Issue #33543 - 按断连时长分级告警的需求讨论
* Issue #9352 - 覆盖 `504` 等级的实践讨论
* Issue #15215 - 原生 Prometheus 指标能力讨论

### 可选工具

* wazuh-prometheus-exporter - 将 Agent 状态接入 Prometheus/Alertmanager

![](https://mmbiz.qpic.cn/mmbiz_jpg/AFibuxM1dR04rxib2QvmsExNpEVQU8GxOS1JVRLwycs1fZy4KJDdp3k0b0K4ZqzH2MyV6gmtLhUdGwhpTxKmiaPy3icvxIcLly7hqL9SSR4m0bQ/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aiarKdLqgA02QQHicBbXAm5hBjbFa2s2Yd38IQr3UDPrm7EfOdmSMLCvSRgVPsVR0YoIMcYwoaBmrqpwvwbhOvag/0?wx_fmt=png)

imBobby的自留地

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aiarKdLqgA02QQHicBbXAm5hBjbFa2s2Yd38IQr3UDPrm7EfOdmSMLCvSRgVPsVR0YoIMcYwoaBmrqpwvwbhOvag/0?wx_fmt=png)

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