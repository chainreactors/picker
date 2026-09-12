---
title: Bug Bounty 干货：一条正则搞定泄漏密钥扫描——附 Burp Suite 实战
url: https://mp.weixin.qq.com/s/qzKUCmTPDShuh96MhI4IqQ
source: Doonsec's feed
date: 2026-09-11
fetch_date: 2026-09-12T06:47:28.123683
---

# Bug Bounty 干货：一条正则搞定泄漏密钥扫描——附 Burp Suite 实战

# Bug Bounty 干货：一条正则搞定泄漏密钥扫描——附 Burp Suite 实战

原创

Red Hunter
Red Hunter

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6M4X6auwic8TD3b6aGIUkPDmQbFxS78SQs28Q5RN4u6jBf0wG0nhuHVfpaeOpNX0Micic6Wiay8ibIt8au8iaCz0RaRmLyaN98m6MpV8/640?from=appmsg)
> **导语**：挖漏洞最怕的不是 0day 难找，是金矿就在眼前你却看不见。安全研究员 @wtf\_yodhha 最近在 X 上贴了一条通用密钥扫描正则，覆盖 AWS、Google Maps、阿里云、Cloudflare 等二十多个主流云平台与 SaaS 服务。把这条正则丢进 Burp Suite 的搜索框，3 秒就能从响应体里拽出 132 条命中。下面拆解这条正则的构造逻辑，并给出实战用法。
>
> （关键词简注：Bug Bounty 即漏洞悬赏计划，企业花钱请白帽挖自家漏洞；正则即正则表达式，一种字符串模式匹配语法；SaaS 是软件即服务的英文缩写，指托管在云端的现成软件；Burp Suite 是渗透测试人员最常用的 Web 抓包与扫描工具）

---

## 一、这条正则长什么样

原始正则来自 GitHub Gist，作者是 h4x0r-dz，原帖也给出了 Telegram 频道（brutsecurity）里的一份简化版本。我们直接看完整版的核心结构：

```
(?i)((access_key|access_token|admin_pass|...|aws_secret_key|...|eureka.awssecretkey)
[a-z0-9_ .\-,]{0,25})(=|>|:=|\\|:|<=|=>|:).{0,5}['\"]([0-9a-zA-Z\-_=]{8,64})['\"]
```

（完整版本覆盖 200+ 字段名，限于篇幅不展开。需要查看完整列表可以直接拉到文末的 Gist 地址。）

乍一看很长，但拆成三段就清晰了：

* **第一段 `(?i)((...)[a-z0-9_ .\-,]{0,25})`**：不区分大小写地匹配 200 多个密钥相关字段名（access\_key、api\_key、aws\_secret、阿里云 access key、Algolia、Cloudflare、Datadog 等都囊括在内），字段名后面允许 0 到 25 个字符的间隔（兼容 access\_key\_id、aws\_secret\_key 这种带后缀的写法）。
* **第二段 `(=|>|:=|...|:)`**：匹配赋值符号。常见的有 =、=>、:=、:、<= 这五种，覆盖 JSON、YAML、ENV、URL 参数、Python 字典等几乎所有配置文件格式。
* **第三段 `.{0,5}['\"]([0-9a-zA-Z\-_=]{8,64})['\"]`**：赋值符号后允许 0 到 5 个空白或转义字符，然后用单引号或双引号包住真正的密钥值。8 到 64 字符的长度限制过滤掉过短的占位符（如 example、test），同时兼容短 ID 与长哈希。

这套设计的精妙之处在于把"字段名 + 赋值符 + 引号包值"这个三段式作为骨架，把所有需要扫描的密钥类型塞进第一段的字段名清单里就行。**新增一种密钥支持时不需要改语法，只需要往清单里加字符串**，可扩展性极强。

---

## 二、实战演示：Burp Suite 三秒扫出 132 条命中

原作者给的截图最有说服力：把这条正则塞进 Burp Suite 的搜索栏，勾选 Regex、Target、Response body 三个选项，对一个普通 Web 应用的响应包跑一次搜索。结果直接吐出 132 条匹配，其中一条命中把藏在缩混淆 JavaScript 里的 Google Maps API Key 给挖了出来。

![Burp Suite 正则匹配密钥命中 132 条](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6MBYdXDUcdVvsDfBbFQzVf5FYhXFXVibLjlsbbgtZ5y91R8ItUrccKMQ3lhqXyqbL5CYB6weamqtvh1S8ic37WfE3PCuNhkr70ibE/640?from=appmsg "Burp Suite 正则匹配密钥命中 132 条")

放大看那条命中的细节：`apiKey:"AIzaSyCab6eIMNih34mQb3XI_QwXagmF2_rvQAg"` —— 这是一个典型的 Google Maps JavaScript API Key，藏在某段业务代码的深处。攻击者拿到这种 Key 就能调用 Google Maps 各种付费接口，按调用次数扣企业账户的钱，更严重的还能用来做地理定位伪装。

![放大后的 Google Maps API Key 命中细节](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6MXvq1qInJ62zGPYEdvKCXyPyIlLZOx2Ck5yX5KJ1NWsmffGX1KOns02FDlZMMPKIBXHPrHicJiaMQscWRcLs6nt8PAFrTcwpm7s/640?from=appmsg "放大后的 Google Maps API Key 命中细节")

这个 Key 在没跑正则之前，靠人工翻响应体几乎不可能找到。生产环境的 JavaScript 都是被 Webpack 压缩成一行，几十 KB 的 minified 代码（去除所有空格换行的极简化代码）里要肉眼定位 "apiKey":"AIzaSy..." 模式，等于大海捞针。

---

## 三、为什么这条正则比大多数密钥扫描器更狠

市面上不缺密钥扫描工具，GitHub 上 stars 过千的项目就有好几个：

* **gitleaks**：基于 Git 历史扫描，靠正则 + entropy（信息熵，用来衡量字符串看起来是否像随机生成的高熵值字符串）双判定，业内事实标准。
* **truffleHog**：主打 entropy 检测，能挖出非标准命名的密钥。
* **grep.app**：在线工具，跨 GitHub 全网搜索泄漏密钥。
* **HaENet**：专门做密钥规则库的开源项目，规则文件覆盖几百种服务。

这些工具的问题在于**默认只扫文件**，不直接对接 HTTP 流量。生产环境的密钥泄漏往往不在源码里，而是在：

1. **前端 JS bundle 的运行时配置**（本次案例就是这种）
2. **服务端 API 返回的 JSON 里**（如 debug=true 时泄露内部 token）
3. **WebSocket 握手响应里**
4. **错误堆栈里**（开发环境配置失误）

把这条正则丢进 Burp Suite 的搜索栏，相当于把上面四种场景一次性全覆盖。配合 Burp Suite 的被动扫描 + 主动爬虫，能在一次渗透测试里把所有 HTTP 响应过一遍，这是 gitleaks/truffleHog 这种文件级工具做不到的。

回复里那位研究员提到的 **grep.app** 是另一种思路——它直接索引全网公开的 GitHub 仓库与 Gist，用关键词搜泄漏密钥。它的好处是覆盖面广（任何人在 GitHub 上 commit 过就会被搜到），坏处是时效性差（已经被删除的 commit 可能在缓存里存活数周），而且对前端 bundle 这种未公开的密钥无能为力。

---

## 四、红队实战怎么用、怎么避坑

**用法层面**：

1. **被动扫描模式**：在 Burp Suite 的 Proxy → Options → Search 里配置这条正则，所有经过 Burp 的 HTTP 响应都会自动匹配。这是默认推荐模式，适合长时间挂机做信息收集。
2. **主动扫描模式**：用 Burp Scanner 跑全站 + 配正则搜索，能在主动探测阶段就发现密钥泄漏。但要注意速率控制，避免把目标网站打挂。
3. **配合历史回放**：爬过的流量包存成 .burp 文件，离线后再用正则重扫。很多 Bug Bounty 项目的核心收入都来自这种"复盘"，因为初期扫描时漏看的响应，过几周回头看会发现新价值。
4. **集成到 CI/CD（持续集成/持续部署流水线）**：把这条正则包装成脚本，在 CI 流水线里对每次构建产物（前端 bundle、配置文件、Docker 镜像元数据）跑一遍，能在代码上线前拦截密钥泄漏。

**避坑层面**：

* **过滤 false positive（误报）**：正则匹配到的字符串不一定是真密钥，可能是单元测试里的 mock 数据或文档示例。判断标准：拿这个 Key 去调对应服务的公开接口看是否生效。Google Maps Key 直接访问 `https://maps.googleapis.com/maps/api/js?key=XXX` 看返回 200 还是 403 即可。
* **遵守授权范围**：Bug Bounty 项目必须在授权范围内扫描，私自用拿到的 Key 调接口可能违反规则。挖到 Key 就提交报告，不要直接薅羊毛。
* **白嫖 vs 举报**：Google Maps Key 拿来调 API 是会被计费的，这种薅法一旦触发风控，企业账户会被标记。所以挖到 Key 之后正确的姿势是提交漏洞报告，让企业自己轮换密钥，而不是偷偷调用。

---

## 五、这条正则的局限性

实事求是地讲，这条正则也不是万能的，有几个明显的盲区：

* **环境变量文件**：`.env` 文件里的 KEY=value 格式匹配没问题，但如果是 export AWS\_ACCESS\_KEY\_ID=XXX 这种 shell 导出语法，正则能匹配到值但需要二次确认是不是真密钥。
* **Base64 编码的密钥**：很多服务会把密钥 base64 编码后再写入配置，这条正则匹配的是 base64 字符集但识别不出"这是被编码过的密钥"。
* **JWT（JSON Web Token）类令牌**：JWT 由三段 base64url 字符串拼接而成，长度通常 100+，超出了正则的 64 字符上限。这种情况应该单独写一条正则：`eyJ[A-Za-z0-9_=-]+\.[A-Za-z0-9_=-]+\.?[A-Za-z0-9_.+/=-]*`。
* **私钥文件**：RSA、SSH 私钥有明显的 BEGIN/END 标记，应该单独匹配 `-----BEGIN [A-Z ]+PRIVATE KEY-----` 这种锚点。

实战中通常的做法是把这套正则作为**基础规则**，再根据目标应用的特点补充几条针对性规则。比如扫金融应用就加 JWT、扫云原生应用就加 Kubernetes Secret、扫区块链就加助记词正则。

---

## 六、写在最后

挖漏洞这件事，七分靠思路三分靠工具。这条正则之所以值得单独拎出来讲，不是因为它技术上有多高明，而是因为它演示了一个红队思路：**别只盯着代码层，HTTP 流量才是密钥泄漏的真正富矿**。

很多企业以为把密钥从前端移到后端就安全了，结果后端 API 在调试模式下把内部 token 塞到响应里，反而比前端泄露得还干净。把这条正则部署到 Burp Suite 上，至少能让你在一次普通的渗透测试里多捡几条中低危漏洞报告，省下来的时间就是真金白银。

（关键词简注：Bundle 在前端工程里指打包后的资源文件；Proxy 是 Burp Suite 的代理抓包模块；mock 是测试时用来模拟真实接口返回值的假数据）

---

![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6NN4wPxvHoTCj7uxZPb01H9PlbeywRUzCsjFwic3IrxgVARohOFPmUBD6esWpdJ4fS3OibxBCBJB0ib9fia40S7z3URxWETuDZ6yicA/640?from=appmsg)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6N3YTF5MrI7QzTWia2UTUkBCic0rHl9ad1of5Fia9tHxIV1fxuNZb4ouf4ZUciaenMn0xkkpq8HziaGoH8jibiaE7ast82qYcExj5nIts/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621144&idx=1&sn=895132b6dea5c5055ac21126293661f9&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6NsVxSgREfOjy8Dcgh1XvtXficRROkQJRicAXyHO3HzCApW3Kq0DmBBR1wWiayfIFz04K6Z2Ql4sic56lCQPpNfLYY7BXHjxar49tU/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621255&idx=4&sn=75d0f413e300d99d4e5cc631714c96ae&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6N71CGZ0ogcZg7LVPOkLeWYCQrRIn0CDQ5BcJkKFcKe7SsNO6es8dp7kBsvM9sFiaGI7lfAsO0WKKAJS9XJFZb88dI6Ve20jeYA/640?from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650621242&idx=1&sn=c7504153dd6aa285da53fc1a4a907f82&scene=21#wechat_redirect)

> 👇 点击**阅读原文**，访问我的网站

---

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

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