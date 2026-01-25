---
title: 微软给FBI解锁疑犯笔记本
url: https://mp.weixin.qq.com/s/vIC5AgNvpsfYRPGrS-GfFg
source: Doonsec's feed
date: 2026-01-24
fetch_date: 2026-01-25T03:50:23.699800
---

# 微软给FBI解锁疑犯笔记本

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sY7YiaX0Dh2jMiciaYaEcONhqM5G8IqkIJM5diarJ36jrlibIEbUIRH1TIyw8wxrtIXsUdou2TnTqmhsks5S3OcgS5g/0?wx_fmt=jpeg)

# 微软给FBI解锁疑犯笔记本

原创

二道
二道

二道情报贩子

![]()

在小说阅读器中沉浸阅读

2026年1月23日，福布斯率先报道，微软应美国联邦调查局（FBI）要求，提供了BitLocker恢复密钥，成功解锁三台涉嫌案件的嫌疑人笔记本硬盘，助力联邦层面的刑事调查。TechCrunch随后跟进此事，进一步披露事件细节，引发行业对用户数据隐私与执法配合边界的讨论。

据微软向福布斯透露，其每年平均接收约20次类似的执法机构密钥调取请求，此次事件并非个例，而是微软常规配合执法的一部分。

BitLocker是微软自Windows Vista起推出的全盘加密工具，目前已成为现代Windows设备数据安全的核心组件，其关键特性与当前使用现状如下：

1. 默认启用与强制化趋势：多数Windows电脑默认开启BitLocker全盘加密，可保护设备锁定或关机状态下的数据不被未授权访问；且Win11 24H2及后续版本中，该功能已成为“必选项”——用户在首次开机（OOBE界面）联网并登录微软账户时，即便家庭版系统，BitLocker也会自动开启。

2. 恢复密钥存储机制：默认情况下，BitLocker恢复密钥会自动上传至微软云服务器，这一设计虽为用户遗忘密钥时提供“兜底”，但也使微软具备了向执法机构提供密钥的基础条件。

3. 核心安全功能：支持与硬件TPM（可信平台模块）芯片结合，实现物理层面的数据保护；用户可额外设置启动PIN、USB密钥等解锁方式，进一步提升加密安全性，不过这些附加防护无法阻止微软通过云存储的恢复密钥绕过解锁。

此次密钥调取与美国关岛“疫情失业救助计划（Pandemic Unemployment Assistance）欺诈案”相关，多名嫌疑人被指利用该计划实施诈骗。当地媒体此前已对案件有过报道：

• 关岛《太平洋每日新闻》（Pacific Daily News）去年曾提及，执法部门已向微软出具针对嫌疑人硬盘的搜查令；

• 关岛另一媒体Kandit News在2025年10月报道，FBI在扣押三台加密笔记本（BitLocker加密）半年后，才正式申请到调取密钥的 warrant（司法令状）。

• 微软向福布斯确认，公司会在收到合法司法文件后，向执法机构提供BitLocker恢复密钥，此次操作符合其既定的执法配合政策。

约翰·霍普金斯大学密码学专家马修·格林（Matthew Green）在社交平台Bluesky发文，直指事件暴露的核心风险：

• 云密钥安全漏洞：微软云基础设施近年来多次遭遇恶意黑客攻击，若黑客突破防护获取存储的BitLocker恢复密钥，再结合对硬盘的物理接触，即可解密用户数据；

• 行业落后性批评：“2026年，这些风险早已被行业熟知，微软在保护用户关键密钥上的无能，正使其逐渐脱离行业主流水平。”

事件引发讨论：

BitLocker默认将密钥上传至微软云的设计，是否在“用户隐私保护”与“执法配合便利性”之间失衡？一方面，执法机构需通过密钥获取犯罪证据；另一方面，普通用户的数据安全因“云存储密钥”面临潜在风险，且多数用户可能未意识到自己的加密密钥并非完全由自己掌控。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sY7YiaX0Dh2jMiciaYaEcONhqM5G8IqkIJMu7icaicWibqvxS5o5hUoEUqVrXK6QcAbwxNic0ibmxdglmsJdibHMjOkLhTA/640?wx_fmt=jpeg)

2024年8月，微软曾因BitLocker相关问题引发大规模“蓝屏事件”：在修复BitLocker安全漏洞的过程中，因固件兼容性问题，大量设备触发BitLocker恢复模式，用户需手动输入恢复密钥才能启动系统，最终微软不得不撤回该补丁，并建议用户采用手动缓解措施。这一事件也暴露了BitLocker在系统更新中的稳定性风险。

个人用户防护建议：手动管理BitLocker恢复密钥，避免默认上传微软云（可选择打印存储或存入安全的本地设备）；开启TPM芯片与启动PIN双重防护，降低密钥被调取后的风险；关注微软安全补丁动态，避免因补丁问题触发恢复模式。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/sY7YiaX0Dh2iaS8mtrK1dUrIzGbM7UYdiajsuibtSMXj2aYsQnZ5mwhTupx5rDHVU4n7XlXghkUcecCfeuCX0icJMoA/0?wx_fmt=png)

二道情报贩子

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/sY7YiaX0Dh2iaS8mtrK1dUrIzGbM7UYdiajsuibtSMXj2aYsQnZ5mwhTupx5rDHVU4n7XlXghkUcecCfeuCX0icJMoA/0?wx_fmt=png)

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