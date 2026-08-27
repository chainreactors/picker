---
title: 【漏洞预警】Redis 又双叒爆高危 TLS Pending-List UAF 漏洞，已公开完整EXP，速修！（已复现）
url: https://mp.weixin.qq.com/s/HrOvkBMJHANWmIjqyegTwQ
source: Doonsec's feed
date: 2026-08-26
fetch_date: 2026-08-27T12:11:27.152602
---

# 【漏洞预警】Redis 又双叒爆高危 TLS Pending-List UAF 漏洞，已公开完整EXP，速修！（已复现）

# 【漏洞预警】Redis 又双叒爆高危 TLS Pending-List UAF 漏洞，已公开完整EXP，速修！（已复现）

华顺信安威胁情报中心

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# ****▌漏洞描述****

Redis 常被用于缓存、会话管理、消息队列和实时业务数据处理，部分企业会为跨机房、云上或公网访问场景启用 TLS。公开材料显示，Redis 的 TLS Pending-List 处理逻辑存在 Use-After-Free 缺陷。

Redis 官方修复提交确认该缺陷会造成服务进程崩溃。公开 PoC 项目则声明，在特定 Redis 8.8.0、TLS 配置及权限条件下，可进一步造成以 `redis-server` 进程权限执行代码。应按高风险问题处置，但不能将公开复现实验环境直接等同于所有 Redis 部署均可被利用。

|  |  |  |
| --- | --- | --- |
| 受影响分支 | 公开材料列举的受影响版本 | 修复版本 |
| 8.10.x | `< 8.10.1` | `>= 8.10.1` |
| 8.8.x | `< 8.8.2` | `>= 8.8.2` |
| 8.6.x | `< 8.6.6` | `>= 8.6.6` |
| 8.4.x | `< 8.4.6` | `>= 8.4.6` |
| 8.2.x | `< 8.2.9` | `>= 8.2.9` |
| 7.4.x | `< 7.4.11` | `>= 7.4.11` |
| 7.2.x | `< 7.2.16` | `>= 7.2.16` |
| 6.2.x | `< 6.2.24` | `>= 6.2.24` |

说明：上述分支范围来自公开预警材料，官方修复提交可确认 `src/tls.c` 中的 Pending-List UAF 已被修复。公开材料暂未给出与该 TLS 问题绑定的 CVE 编号，因此不应将其评分与既有 Redis CVE 混用。

# ******▌利用条件******

利用条件：目标启用 Redis TLS 服务；攻击者能够从网络访问该 TLS 监听端口；并且能够建立连接、通过认证及 ACL 获得漏洞链所需命令权限。

大致利用链路：TLS 连接进入待处理队列 -> 服务端处理连接读取事件 -> 某连接关闭过程移除另一待处理连接节点 -> 遍历逻辑继续引用已释放节点 -> 触发 UAF，造成服务崩溃；公开 PoC 声明在特定构建和配置下可进一步实现进程级代码执行。

# ******▌威胁状态分析******

该问题对公网 TLS Redis、跨云互联缓存节点、遗留测试环境和由第三方维护的实例更具风险。TLS 的启用本身不代表服务安全，若 Redis 端口可被非受信网络访问，且认证、ACL 或客户端证书校验配置宽松，攻击面会显著扩大。公开渠道已公开完整EXP利用代码，建议按高优先级处置。

通过 FOFA 测绘可以看到，截至 2026 年 8 月 26 日，全球暴露在公网的 Redis 相关资产约为 2,000,648 条，涉及 1,272,914 个独立 IP，其中美国的资产占比较高。

![](https://mmbiz.qpic.cn/mmbiz_png/iaPgUxMqaSAjuv2UnDL1DrBBpYlDqYshpx3mSX0eEhG1RmJXvY2qSEIbwugn1olfWL48tAw1El24fgx1mZKoibZUJnV2AicbFpYushT928XqYs/640?wx_fmt=png&from=appmsg)

# ******▌排查和修复建议******

* 盘点所有 `redis-server` 实例，确认实际版本、是否编译或启用 TLS、TLS 监听地址及可达网络范围。
* 优先排查公网、云安全组、跨区域互联、历史测试和第三方维护资产，避免仅核查主业务集群。
* 按所属分支升级至表中修复版本或更高版本；已停止维护的分支应制定迁移或下线计划。

* 收紧 Redis ACL，按业务最小权限授权，移除不必要的高危命令权限和共享管理员账号。
* 对无法立刻升级的实例，临时通过网络访问控制、客户端证书校验和命令 ACL 降低暴露面；这些措施不能替代版本修复。

* 修复后复测版本、TLS 配置和各类遗留节点，确认容器镜像、从库及灾备节点同步完成升级。

# ******▌产品支持情况******

华顺信安安全研究团队已成功复现该漏洞。

![](https://mmbiz.qpic.cn/mmbiz_png/iaPgUxMqaSAju35OOHUUaTF9AKKdibZsYXsKfotHegwPyKCRDFRCjW2BJUCy5qSwdhSYKjicY7r2dJhMpB27JzCaCBJVKFhq0gTakQrjibrUkBs/640?wx_fmt=png&from=appmsg)

华顺信安安全产线产品已支持 Redis 相关产品组件暴露面风险资产规则识别，可用于辅助完成资产定位与修复排查。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaPgUxMqaSAhOdmsZzs7QhCLhBLokHHPNxxZIUmGRsPT5QErIBD2J93jGe7MeVtrMsmVn3DGMrkB540jKRv1LGHPibfMQ3KIbVA8ib0oNd4iaLY/640?wx_fmt=png&from=appmsg)

# ******▌参考******

* https://github.com/v12-security/pocs/tree/main/redis/server\_ssl
* https://github.com/redis/redis/commit/6d088c335d5c3ec49a6c28486140b498e70b7834

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/iaPgUxMqaSAiaGSMGlL1tDCIKobjY6yE5QEzLH0piaDOsHs2Cp8EpNt4wRwG8gsHJ0Hwh5YhqY8JH3C7sQP04paoyhbPPZxVqf5wscbwLRSiaZw/640?wx_fmt=other&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaPgUxMqaSAg3rbmrt8b5zVrvNlbMAkBc3icQPjPy59bgFWKA58EWheMcnn9ibZ0nOEuqa9DouhMHpm0cRZdJHGADKb6gwk73jy6J4rW1do1YU/640?wx_fmt=other&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

预览时标签不可点

修改于

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/iaPgUxMqaSAgSZ8kG6XSXjCxBibx0ptvia0wlqy8WngVzGH1dngS2WeUwXXde2k5X4U8pE4HfcFkb3GphRPNJhI4dbhibYASkakicMqPKw4jvgz4/0?wx_fmt=png)

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