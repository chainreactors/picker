---
title: 【域名劫持事件】某社区卫生服务中心公众号某个功能点居然跳转黄色网站？
url: https://mp.weixin.qq.com/s/4ATK2cNyC0S2bGFJPpMKHQ
source: Doonsec's feed
date: 2026-06-18
fetch_date: 2026-06-19T07:01:37.766911
---

# 【域名劫持事件】某社区卫生服务中心公众号某个功能点居然跳转黄色网站？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Iv8D5nD32icKscSH5Z8pl6MdKZKj7BzAp5FW2RtfxOlsAV36fWDwu24TECqcbL0Dhg3RS4ibZNeZcIqQS2w81kUa41LAgt8rIol8F1JBIB9oE/0?wx_fmt=jpeg)

# 【域名劫持事件】某社区卫生服务中心公众号某个功能点居然跳转黄色网站？

原创

金夏
金夏

金夏安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

免责声明

本文仅用于技术学习和讨论。请勿使用本文所提供的内容及相关技术从事非法活动，由于传播、利用此文所提供的内容或工具而造成的任何直接或者间接的后果及损失，均由使用者本人负责，所产生的一切不良后果均与文章作者及本账号无关，本次测试仅供学习使用。如有内容争议或侵权，请及时私信我们！我们会立即删除并致歉。谢谢！

---

**一、事件描述**

```
经一个朋友反馈，盐湖区某个卫生服务中心遭到黑产团伙攻击
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Iv8D5nD32icJI6QBwOdo6EuwOnabUgg70wErJRAU2ia9fp7G6VnzibqcfZ0DHVjlnn9WNEpaZJBVpcpWXWPAvEtz8ibLc546bpf2QOdKdzjaaZ0/640?wx_fmt=png&from=appmsg)

```
来到公众号页面点击发消息
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Iv8D5nD32icKYribKUQAYrZ7HQr5620yaaRUaAHg9LacA6tnyQibJzPrSz9ynw8T0oJFzbDmohDp2jNYiczH6xia7A75vicicI2DoN6U8iaicIAOiaqbw/640?wx_fmt=png&from=appmsg)

```
点击社区网点然后点旧版商城
```

![](https://mmbiz.qpic.cn/mmbiz_png/Iv8D5nD32icJh7HKHUPjKH6ghK7G7oJwanMKllSfaAwglqw5hAhicLx90ooSX08p5DGDKn6EiaQjDRfscS2QWwc2ZUtVlH3v2ibIIaJ80a1wGJ4/640?wx_fmt=png&from=appmsg)

```
跳转到黄色网站
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Iv8D5nD32icJMjomOmlolqpwkVBk9lD7yCyqKlnqAMgcscsIicIOibhaxkhXTWPBRtfCRKPfZGzdFHEVU4Bf4g5iaDiaPF2icZY4kuxDHYZqeku5I/640?wx_fmt=png&from=appmsg)

```
经查询，域名未备案
```

![](https://mmbiz.qpic.cn/mmbiz_png/Iv8D5nD32icK3boIWBMd3aD4tzpeLZ45dxqOdUUPVb2f0JYymWEETymfsRmy0mpBULHvAGLaiaXEk5pjpV8M3CmUDC2nrEBa3nrBaQRTftnRY/640?wx_fmt=png&from=appmsg)

### 二、基础溯源

---

###

发现一个色情视频导航站：`http://www.xxxx.net/app/index.php?i=42&c=entry&eid=172`

该网站为典型的色情资源聚合平台，通过盗版影视内容吸引流量。经过查询，我们重构了该网站的基础设施全貌：

![](https://mmbiz.qpic.cn/mmbiz_png/Iv8D5nD32icK2WJKLic4onW0BMVrvyLvIbzv8RATrcTe6apF5mElMfdX8IzBSYHb3eR01xryJzqkiaiavtH2tBvnrxsVTGicz6b51ROcGAHfRNFg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Iv8D5nD32icJOB8iaiaFctB85S27J1oA5Fz2Op9oIrpicQKWsOqKI5fAw7QuAHDGYUGw8LWbmR5icr4g74F4wYQ6NutZdFHvOLrEUCCoASpqJMrI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Iv8D5nD32icJEEGAkUmnBgvKV6lL4lkzaXa5HIuI9vv81dEoFF8Vwm1icoI0CibgAyEF2cGo0FpVoJnVfG1ysibmAsBsb9lDWBmW5oiauuayejTs/640?wx_fmt=png&from=appmsg)

**网站特征：**

* 页面标题伪装为“RC391AV”（模仿AV番号）
* 页面包含大量色情视频分类标签
* 技术框架为 **微擎（WeEngine）CMS**（国内常用的微信公众号管理系统）
* 内容为盗链/采集，不生产原创内容
* 无ICP备案

值得注意的是，该域名注册于 **香港防弹注册商 Hongkong Kouming International Limited**，使用 **Cloudflare DNS** 隐藏源站IP，所有运营者联系信息均被隐私保护服务完全隐藏，隐匿手段非常成熟。

### 三、域名基础信息分析

#### 3.1 WHOIS 注册信息

| 属性 | 值 |
| --- | --- |
| **域名** | `xxx.net（域名违规就不发出来了）` |
| **注册商** | Hongkong Kouming International Limited（IANA ID: 3972） |
| **注册日期** | 2025-11-28 19:12:38 UTC |
| **到期日期** | 2026-11-28 19:12:38 UTC |
| **域名状态** | ok（正常） |
| **DNS服务器** | `ARYANNA.NS.CLOUDFLARE.COM` / `DEREK.NS.CLOUDFLARE.COM` |
| **注册人邮箱** | `https://www.kouming.com/domain/disclosure`（完全隐藏） |

**关键发现：**

* **注册商 Hongkong Kouming International Limited** 在圈内以“宽松”著称，常被用于注册敏感/灰色产业域名，属于“防弹型”域名注册商。域名持有者通过该注册商的隐私保护服务，将全部联系信息隐藏。
* 域名仅注册 **1年**（2025-11-28 至 2026-11-28），典型的 **短期投机** 行为——这类色情站运营周期普遍较短，随时准备“弃号跑路”。
* 使用 **Cloudflare DNS** 隐藏真实源站服务器IP，同时提供CDN加速和DDoS防护，进一步增加溯源难度。

#### 3.2 历史解析记录追踪

通过微步在线获取的DNS解析历史：

| 时间 | 解析IP | 地理位置 | 运营商 |
| --- | --- | --- | --- |
| **2026-01-23** | `104.21.42.199` | 美国 | Cloudflare |
|  | `172.67.165.145` | 美国 | Cloudflare |
| **2025-09-18** | `204.11.56.37` | 美国德州达拉斯 | Confluence Networks Inc |
| **2024-09-25** | `149.104.190.212` | 中国香港 | Nebula Global LLC |
| **2024-02-03** | `38.60.80.218` | 美国加州洛杉矶 | FASTNET DATA INC |
| **2022-09-24** | `38.85.209.15` | 美国加州洛杉矶 | Cogent Communications |
| **2022-07-11** | `47.91.170.222` | 中国香港 | **阿里云** |
| **2021-07-23** | `60.205.215.97` | 中国北京 | **阿里云** |
| **2021-07-07** | `47.91.170.222` | 中国香港 | **阿里云** |
| **2017-12-30** | `60.205.215.97` | 中国北京 | **阿里云** |
| **2016-07-30** | `60.205.11.167` | 中国北京 | **阿里云** |

**关键发现：**

* 该域名 **2016-2022年** 曾长期托管在 **阿里云（北京/香港）** 节点。2025年9月后切换至境外节点（美国/Cloudflare）。
* 2025年9月后完全使用 **Cloudflare CDN**，源站IP被彻底隐藏，无法直接定位源站服务器。
* IP地址在 **中国北京、中国香港、美国德州、美国加州** 多地切换，反映运营者有意识地利用多地域基础设施规避监管。

### 四、技术架构分析

#### 4.1 CMS识别：微擎（WeEngine）

URL结构分析：

```
http://www.xxx.net/app/index.php?i=42&c=entry&eid=172
```

* `/app/index.php` — 微擎标准入口
* `i=42` — 公众号/应用ID
* `c=entry` — 控制器参数
* `eid=172` — 入口ID

**微擎（WeEngine）** 是国内常用的 **微信公众号/小程序管理系统**，通常用于搭建微信营销、分销商城、知识付费等应用。色情站使用微擎有两种可能：

1. 利用微擎的 **支付模块** 实现会员付费观看
2. 利用微擎的 **分销体系** 发展下线推广

#### 4.2 内容特征

页面中的分类标签：

```
高清...标签内容违规就不放出来了
```

* 内容来源为 **盗链/采集**，不生产原创内容
* 页面包含 **诱导付费** 和 **广告变现** 模块
* 大量分类标签为 **引流关键词**

### 五、隐蔽性设计

| 手段 | 说明 |
| --- | --- |
| **防弹注册商** | Hongkong Kouming International Limited，监管宽松，常被灰色产业使用 |
| **WHOIS隐私保护** | 全部注册人信息通过 `domain/disclosure` 完全隐藏 |
| **Cloudflare DNS** | 隐藏真实源站IP，提供CDN加速和DDoS防护 |
| **短期域名注册** | 仅注册1年，随时准备弃号 |
| **多地域IP切换** | 北京→香港→美国德州→洛杉矶→Cloudflare多地切换 |
| **无ICP备案** | 未在国内备案，避开监管 |
| **微擎CMS** | 可利用微信支付/分销体系变现，系统成熟 |

### 六、攻击者画像

#### 6.1 运营者特征推断

| 维度 | 推断 |
| --- | --- |
| **身份** | 中国籍或华人，熟悉国内互联网生态 |
| **技术能力** | 中高级（熟练使用微擎CMS、Cloudflare、防弹域名注册商） |
| **技术栈** | 微擎（WeEngine）+ PHP + MySQL + Cloudflare |
| **运营模式** | 色情内容采集/盗链 + 广告变现 + 诱导付费 |
| **隐匿意识** | 强（防弹注册商、隐私保护、CDN隐藏、多地IP切换） |
| **意图** | 纯粹的经济动机，低成本快速变现 |

#### 6.2 同注册商其他域名查询

通过注册商 `Hongkong Kouming International Limited` 关联的其他域名（需进一步查询）：

可使用以下工具进行扩展查询：

* SecurityTrails：`https://securitytrails.com`
* ViewDNS：`https://viewdns.info/reversewhois/?q=Hongkong+Kouming+International+Limited`
* WhoisXML API：`https://whoisxmlapi.com`

建议查询同一注册商/同一隐私保护服务下的其他域名，可能属于同一运营者。

### 七、完整溯源时间线

| 时间 | 事件 |
| --- | --- |
| **2016-07-30** | 域名首次解析至阿里云北京IP `60.205.11.167` |
| **2017-12-30** | 解析至阿里云北京IP `60.205.215.97` |
| **2021-07-07** | 切换至阿里云香港IP `47.91.170.222` |
| **2022-07-11** | 再次解析至阿里云香港IP `47.91.170.222` |
| **2024-02-03** | 切换至美国FASTNET DATA INC `38.60.80.218` |
| **2024-09-25** | 切换至香港Nebula Global LLC `149.104.190.212` |
| **2025-09-18** | 切换至美国Confluence Networks `204.11.56.37` |
| **2025-11-28** | **域名注册**（实际注册时间远晚于首次解析时间，表明域名可能被重新注册或更换持有人） |
| **2025-12-20** | WHOIS信息更新 |
| **2026-01-23** | 切换至 **Cloudflare CDN**（`104.21.42.199` / `172.67.165.145`），源站IP完全隐藏 |
| **2026-06-18** | 微步在线标记为“垃圾邮件”和“恶意” |

### 八、处置建议

#### 8.1 向相关方举报

| 举报对象 | 举报渠道 | 举报内容 |
| --- | --- | --- |
| **Cloudflare 滥用举报** | `abuse@cloudflare.com` | 该域名通过Cloudflare CDN托管色情内容，违反服务条款 |
| **香港居民国际（注册商）** | `abuse@kouming.com` | 该域名用于传播色情内容，涉嫌违规 |
| **微擎官方** | 微擎安全中心 | 该站点使用微擎CMS搭建色情内容平台 |
| **阿里云** | `abuse@aliyun.com` | 该域名历史曾使用阿里云服务器（如有证据） |

#### 8.2 进一步溯源

1. **查询同注册商其他域名**：

* SecurityTrails：`https://securitytrails.com`
* 搜索 `Hongkong Kouming International Limited` 关联域名

2. **查询同Cloudflare账户域名**：

* 被动DNS数据库查询同一Cloudflare NS服务器下的其他域名
* 工具：DNSlytics、SecurityTrails

3. **追踪历史源站IP**：

* 历史IP如 `47.91.170.222`（阿里云香港）、`60.205.215.97`（阿里云北京）可能关联真实运营者身份
* 阿里云有实名认证要求，可通过历史IP追溯运营者身份

#### 8.3 安全提醒

1. **不要直接访问**该网站，页面可能包含跟踪脚本和恶意弹窗
2. **不要主动联系**页面内任何联系方式
3. 溯源全程使用 **代理/VPN** 保护自身安全
4. 如需深度溯源，建议使用 **非实名注册的境外VPS** 进行访问

### 总结

`xxxxv.net` 是一个运营手法成熟的色情资源聚合站，运营者具备较强的隐匿意识和黑产运营经验，使用了“防弹域名注册商 + Cloudflare CDN + 无ICP备案”的标准隐匿组合。该域名历史曾长期托管于阿里云（北京/香港），后逐步切换至境外节点，最终完全隐藏于Cloudflare之后。

虽然没有直接定位到运营者的真实身份，但通过完整的基础设施溯源，已经确定了其 **技术栈、注册商、DNS供应商、历史源站IP、CMS框架** 等关键信息。若通过阿里云历史IP配合执法机关调取实名信息，仍有追踪到真实运营者的可能性。

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/fpGDcfCA2iccpBfjz06vN4gd8XvhIEX8cBd4FejMdyketqOiahO5FsQzMD6pUl2q53VDa0A5ePTfOdbDKHKFibduQ/0?wx_fmt=png)

金夏安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/fpGDcfCA2iccpBfjz06vN4gd8XvhIEX8cBd4FejMdyketqOiahO5FsQzMD6pUl2q53VDa0A5ePTfOdbDKHKFibduQ/0?wx_fmt=png)

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