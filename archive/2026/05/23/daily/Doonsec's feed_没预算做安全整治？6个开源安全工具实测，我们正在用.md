---
title: 没预算做安全整治？6个开源安全工具实测，我们正在用
url: https://mp.weixin.qq.com/s/WLLEjfj_I78E3YZQLfMZUQ
source: Doonsec's feed
date: 2026-05-23
fetch_date: 2026-05-24T05:56:36.221006
---

# 没预算做安全整治？6个开源安全工具实测，我们正在用

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/yJLbez93fl8t1MunkIVHwW6clbP9s16JicNR8XsEibyLDzaotia3SvJ3sjvf5wb10qYpLiamvqD2po9CxegyCNsbjCia5uk8nMJ25JSg9eQ1GjxM/0?wx_fmt=jpeg)

# 没预算做安全整治？6个开源安全工具实测，我们正在用

宝十八
宝十八

网络安全老宋

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**导语：** 你好，我是老宋。关注我，安全攻防干货准时送达！

客户没预算不是借口，开源安全工具一样能干，但你得知道用哪几个、怎么组合

![](https://mmbiz.qpic.cn/mmbiz_png/yJLbez93flibKCyad4b4H3iaUFHTSDCum0Awa95j2A3zDgKjNcloyOWXR8IdMOBc4GfTvMYxG0C4y82JG5h2TtrGpR1F8zMibFd3jzJZhUK2q4/640?wx_fmt=png&from=appmsg)

网络安全老宋实操技巧 · 2026

// 护网季 · 开源工具 · 零预算

# 没预算做安全整治？6个开源安全工具实测，我们正在用

客户没预算不是借口，开源安全工具一样能干——但你得知道用哪几个、怎么组合。

护网季实战6个开源工具OWASP ZAP · Autoswagger · ApiHunter

护网季到了，各种安全整治任务一个接一个往下压。我驻场的同事小张发来消息：

「宋老哥，领导让我们这个月完成 API 安全专项整治，发来一份方案，密密麻麻十几页，我头都大了。」

我当时第一反应：这活儿不难，难在客户。果然，第二条来了：

「客户说没有采购预算，啥商业工具都不给买。」

好嘛，又要马儿跑，又要马儿不吃草。这种情况在驻场项目里太常见了，不是客户不重视安全，是预算批不下来。那作为乙方，到底能不能把这件事做出来？

**答案是：能。开源工具组合起来够用，但你得知道用哪些。**

下面把我们目前找到的 6 个开源工具和思路分享出来，也特别欢迎你把用过的好工具和方法发我，一起把活干好。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/yJLbez93flibjTIkwvLWeA6eKfibkeKWzGsRTy9LiapibzE4vNiaicelPMX90GpGCyT91CeIDjO8Qw5gCXBJstXBvnXibgRLCAsI9Jm5ell77JfnTU/640?wx_fmt=png&from=appmsg)

01

## 我们要解决什么问题

不管是 API 安全整治，还是护网期间的排查任务，核心都是四件事：

![](https://mmbiz.qpic.cn/mmbiz_png/yJLbez93fl9CgcGvlmvuhXdcJjIjnskUmLnzTgeG8Z8CgibQ0AfyA35YL9YOgytAAsVoBuuicdicn2s5tiaabaAE2jtzw41Vn3uYgGz28aQNteM/640?wx_fmt=png&from=appmsg)

商业工具能一键搞定这四件事，价格也是一键清空预算。开源工具不能一键，但组合起来，覆盖面其实差不多。

02

## 6个工具速览

![](https://mmbiz.qpic.cn/sz_mmbiz_png/yJLbez93fl89Ba3eRzRqUPbRoE86ojeaZX1Ua3icmxTZZkqBqfIaRH1LROUrD7Wz60AmUjicJiayyd5zwIdU5oDwLho7BfDzOHtSJS02yKNy98/640?wx_fmt=png&from=appmsg)

03

## 每个工具怎么用

工具 01OWASP ZAP — API 发现 + 漏洞扫描，两步合一

主动爬取目标域名，发现存活的 API 端点，同时对发现的接口做漏洞扫描。这是我们用得多的主力工具，相当于「发现 + 扫描」两步合一。

Python · ZAP 自动化调用

![](https://mmbiz.qpic.cn/mmbiz_png/yJLbez93fl9dib6MDDlPzTQibtqrJK5licDOT6pOSfZq3DCMAEyWvyKMSQJFFSHnh7MWz77icdaa0fEHJmytT2rGZibNnzbweg7oYy7evm2Jk5UM/640?wx_fmt=png&from=appmsg)

有一个经验要说：**不要对全站做深度扫描，会扫出一堆低价值告警把自己淹死。** 优先锁定登录、数据查询、管理后台这几类高价值接口，集中火力。

工具 02Autoswagger — 专门查未授权访问

从目标域名自动找 Swagger/OpenAPI 文档，解析出所有接口，然后在不带认证的情况下逐个请求，标记出返回 200（而不是 401/403）的接口。

Shell · 克隆并运行

```
git clone https://github.com/intruder/autoswaggercd autoswagger./autoswagger https://your-api-domain.com/api-docs
```

输出结果一目了然：哪个接口不带 token 也能访问、返回了什么数据。不带任何认证直接能查到用户手机号和订单信息的历史遗留接口，客户自己往往不知道，查出来他们一般会当天就关掉。

工具 03YscFinder — 扫代码里藏的密钥

扫源码目录里硬编码的 API Key、数据库连接串、JWT 密钥等敏感信息。很多人以为这步不重要，但实际上问题很多。

Shell · 安装并扫描

```
git clone https://github.com/dikesi131/YscFindercd YscFinderpip install -r requirements.txt# 扫整个项目目录，输出 HTML 报告python3 ysc_finder.py -i /path/to/project -ks True -ss True -o report.html
```

我们在某个历史项目里扫出来一个写死在配置文件里的阿里云 AccessKey，这个 Key 还有 S3 写入权限，放在那儿不知道多久了。

工具 04ApiHunter — 一站式检测，新手友好，但有坑

从 Swagger/OpenAPI 文档自动导入接口，智能填充参数批量测试，支持未授权检测、敏感信息扫描、SQL 注入探测和文件上传漏洞检测，最后导出 Excel 报告。对「快速出活」的场景特别对口——导入文档就能跑，跑完还能直接导报告给客户交差。

使用说明 · Windows 客户端

```
# 从 GitHub Releases 下载最新版（当前 v1.5）# https://github.com/11firefly11/ApiHunter/releases# Windows 客户端，开箱即用，无需安装# 核心流程：# 1. 导入 Swagger 文档 → 2. 自动解析接口# 3. 一键批量测试 → 4. 导出 Excel 报告
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/yJLbez93fl9dgiaKkns0D58Wib27BPzQVebCv1QGylCQXMZ1xR2qCeYtwBnSos70TicXaIticPSIwc8CPTLLeicgTnNhdnbsTxy4Q4IUbbnL1icS4/640?wx_fmt=png&from=appmsg)

工具 05munshig — 开发环境实时捕漏

作为代理跑在本地，应用流量经过它，实时检测越权访问、缺失认证、PII 泄露这类问题，并且直接给出修复代码示例。这个工具更适合给开发团队用，在测试阶段就发现问题，比等上线了再查省事多了。

Shell · 一行启动✓ 零配置

```
# 一行启动，无需配置npx munshig# 把应用/测试流量指向 localhost:3001（原来的 3000）# munshig 自动透明代理，实时分析，直接给出修复建议
```

工具 06ApiPosture — CI/CD 里的自动化扫描

Node.js 项目的静态安全扫描，接入 CI/CD 流水线，每次代码提交自动扫一遍，拦截高风险问题进入生产。这个更偏"预防"，不是整治用，但如果你们帮客户顺手搭了 DevSecOps，可以加上去。

Shell · 安装并扫描

```
npm install -g @apiposture/pro# 扫描当前目录，输出 JSON 报告apiposture-pro scan . --output json --output-file report.json
```

04

## 我们打算怎么组合用

不同阶段用不同工具，这是我们目前规划的节奏（还在推进中，欢迎有经验的同学指正）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/yJLbez93fl9KbIIvXrLMyrle8rgqSfss4p9gcWMz2dBwd1icaceGAsEn4S1sWpeicGRCGibhP4bwxeFA6tto5uOjtftoKaCklw2icZDib6q7CPbU/640?wx_fmt=png&from=appmsg)

目前小张那边还在推进第一轮摸底，等跑出结果我再写一篇续集，把实际踩的坑和最终数据补上来。

![](https://mmbiz.qpic.cn/mmbiz_png/yJLbez93flibjpUOtkZ0cMO0RywNxricqK713iasakcORw0EvG4h0zf5hmdjHdMovTgn9ed0ic2JDhP5zSq6GU1ePaPE1Wg5ELtjs1siaGNzauA8/640?wx_fmt=png&from=appmsg)

05

## 开源工具做不到的事

说实话，开源工具不是万能的。

![](https://mmbiz.qpic.cn/mmbiz_png/yJLbez93flibHRC4GtvOBWH4cez5cNJ6WoXwOHAs8xMoJWSdib1HgPic6GLIXarJWsbhgQZmYPEa5suDD0A9TgQenSdqUzZDJeFgAuaiaLCqtw4/640?wx_fmt=png&from=appmsg)

开源工具能做到的是「把该发现的发现」，把风险明确化。供应链安全、数据安全这些更深的水，开源工具能帮你发现苗头，但根治还是得靠体系和流程。

客户穷，不是咱做不好的理由，是做这件事的边界条件。在这个条件里，尽量做到位就是我们能做的。

06

## 老宋说

API 安全整治这件事，虽说方案可以写十几页，但核心其实就三句话。

![](https://mmbiz.qpic.cn/mmbiz_png/yJLbez93fl8xPYSSCX6OMUW0fqhFkZhp4m00jgiaU7leXKHIibknEVsicef63eibjazl6PBsD3pfqshxrkJfEOEibmZIoUTEdX3hiaFzsyNv6jWhE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/yJLbez93flicPrkQwHcMOSXX0WGzIpicf9UxicjckiaodnjPgQ8iaFnbHCricQy7INjJmZ73quN75SgeM06bQDP2Fj26zAOKqJE49tfnr0NRrVNSw/640?wx_fmt=png&from=appmsg)

---

### 往期精彩

[杀毒软件可能有漏洞：360和金山毒霸内核驱动高危风险](https://mp.weixin.qq.com/s?__biz=MzAxMzIxMjM3Ng==&mid=2247485953&idx=1&sn=104f68a19d9e7c7599c60d01b2582386&scene=21#wechat_redirect)

[2026年国内镜像源指南：35个常用源+全场景使用方法](https://mp.weixin.qq.com/s?__biz=MzAxMzIxMjM3Ng==&mid=2247485926&idx=1&sn=132653d09e72a4edfd8ebcb58e120661&scene=21#wechat_redirect)

[影子资产、ICMP打点、无文件驻留——内网渗透的三个新趋势](https://mp.weixin.qq.com/s?__biz=MzAxMzIxMjM3Ng==&mid=2247486031&idx=1&sn=b13efe162c7db4fcd555046c85b17d6f&scene=21#wechat_redirect)

🔐 我是网络安全老宋

专注把安全威胁翻译成听得懂的实操建议。

每周推送漏洞预警、工具测评、攻防笔记。

觉得有用，点个在看，转发给你身边的运维同事，就是对我最大的支持。

我们下期见 👋

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/sowcUpcXRY07WiafrWPnt0icqSjEOPqweHgqfN5sMGTgMPP5yciaeNiaPx8oJtcS4I6dCcBUL6q4JOY9jNalwkxmZQ/0?wx_fmt=png)

网络安全老宋

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/sowcUpcXRY07WiafrWPnt0icqSjEOPqweHgqfN5sMGTgMPP5yciaeNiaPx8oJtcS4I6dCcBUL6q4JOY9jNalwkxmZQ/0?wx_fmt=png)

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