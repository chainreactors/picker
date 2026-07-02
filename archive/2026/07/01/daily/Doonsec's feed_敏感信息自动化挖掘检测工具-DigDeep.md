---
title: 敏感信息自动化挖掘检测工具-DigDeep
url: https://mp.weixin.qq.com/s/tsQUxgD8FTsPaXlJRybHAQ
source: Doonsec's feed
date: 2026-07-01
fetch_date: 2026-07-02T05:55:11.363962
---

# 敏感信息自动化挖掘检测工具-DigDeep

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/MSDUaqtwboRooB69kqIwF0QqZZIXRAumQBEnmrkpZYic5v9Zv2Mr1ZVq2wBw2cfCWJNHqFJx85BKktW9XWjPCbJ5Km6LdrdS9ia8KQOSRGrPo/0?wx_fmt=jpeg)

# 敏感信息自动化挖掘检测工具-DigDeep

shine798
shine798

陌笙不太懂安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

免责声明

```
由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号陌笙不太懂安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉，谢谢！
```

## 工具简介

在日常渗透测试、代码审计或源码泄漏排查中，最令人头疼的问题莫过于：**硬编码密码、云服务器AK/SK、手机号、身份证号、数据库连接串等敏感信息散落在文件的各个角落**，靠人工逐一翻找不仅效率低下，还极易遗漏关键线索。

**掘地三尺（DigDeep）** 正是一款为解决这一痛点而生的信息收集工具。

它支持渗透测试中的多种常见场景：

* 获取了网站源码后，需要从海量文件中查找敏感凭证
* 拿到Web前端JS、HTML等文件，寻找隐藏的接口密钥
* 反编译APP或小程序得到源码后，快速定位身份证号、密码、AK/SK等敏感数据
* 需要检测Swagger、Druid等管理路径是否暴露

## 核心功能

### 近百条内置规则，覆盖全面

工具内置了**近百条敏感信息提取规则**，这些规则融合了网上公开的正则表达式与多年渗透测试实战经验提炼而成，覆盖云安全、小程序、APP、Web等常见敏感信息泄露类型。

**部分检测类型如下：**

| 风险等级 | 检测类型 |
| --- | --- |
| 🔑 高危 | 各类密码、阿里/腾讯/京东/百度/字节/金山/谷歌云平台AccessKey、微信sessionkey、Webhook、JWT令牌、AWS Key、Google OAuth Token等 |
| 📱 中危 | 手机号、身份证号、邮箱、内网/公网IP、MAC地址、URL、微信公众号/小程序APPID、企业微信/钉钉corpid、各类加密密钥等 |
| ☁️ 低危 | 阿里/腾讯/华为/亚马逊/百度/谷歌/微软/京东云存储桶地址、地图调用密钥等 |
| 🧩 额外检测 | Swagger接口路径、Druid监控路径、SQL错误信息、目录遍历特征、SSRF参数、JSONP回调参数、Source Map文件等 |

### 深层递归扫描，精准定位泄露位置

支持**递归多层文件夹扫描**，即使敏感信息藏在最深层的文件目录中，也能精准捕获。工具不仅能发现敏感信息，还会明确记录**泄露的具体文件路径和行号**，并支持通过双击记录查看**命中行及上下各5行的上下文预览**（HTML渲染展示，敏感信息标红高亮），帮助快速判断是否为有效泄露及影响范围。

### 灵活的结果管理与筛选

* **按风险等级筛选**：高危/中危/低危一键切换，优先处理高风险问题
* **按数据类型筛选**：快速聚焦特定类型的敏感信息
* **结果导出**：支持TXT / JSON / CSV三种格式一键导出，便于存档或进一步分析
* **右键快捷操作**：单条复制、单条导出、单条删除（仅从当前结果列表移除）
* **智能去重**：URL、微信公众号APPID等重复项自动合并，结果清晰不冗余

### 高效扫描，大项目无压力

* **自动跳过二进制文件**（.dex/.apk/.png/.jar等），避免无效扫描
* **实时进度条 + 当前文件提示**，大文件扫描进度一目了然，无需焦虑等待

## 适用场景

| 场景 | 说明 |
| --- | --- |
| 渗透测试 | 获取目标源码后，快速提取可利用的敏感凭证信息 |
| 代码审计 | 在代码上线前系统化排查硬编码密钥等安全隐患 |
| 源码泄漏排查 | 发现源码泄露后，第一时间评估泄露范围和风险等级 |
| 安全合规检查 | 企业内部自查，确保代码仓库不包含违规暴露的个人信息或企业密钥 |

### 使用教程：

1、对一个小程序进行反编译，得到了源码文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQsHUo2T4Toialsc4ujKQReG1nNXqUx9xhW7yfTJyYOyibKjG6FSPzSsTtMwIf5aXNWRO72sSOZeRiaM5cJAn9T2lEqdP1mjg3Zm0/640?wx_fmt=png&from=appmsg)

2、打开掘地三尺（DigDeep）

```
java -jar DigDeep.jar
```

3、选中小程序反编译后的源码文件夹，点击开始扫描，可看到扫描出大量敏感信息，包括身份证、手机号、IP地址、邮箱📮、密码等。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSu6VzPmmD6g2e5LiaOha6sWEEbWVoTe1MHE7c2RnmrAu14Qc5nd3FtfzKHHZuvwHApKGZot9FcX1R6WpC3InBk85rF3WdJfEB8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSib6icIll205GibKkpj63QJH5NgF6jzWE53NFZ3piagYfyvvNHJMHQ5d9VBKrPaUjCwDjrmzIHYmCbL1XoCSVE2qm9uwBT4P9rNPM/640?wx_fmt=png&from=appmsg)

4、双击其中的任意一条敏感信息，可以预览泄露位置的上下文（敏感信息，会以红色高亮显示），且会显示泄露信息具体的文件位置。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSXfwdz8leqh1ibnMhLCuYZu0S0IOWl9Zh1B3iaJLiaKXaN4uzoQBxO6uicxq1RLYGkVK7UOq4yXWdFPPkSIwNEaiajHPzTYt5glFck/640?wx_fmt=png&from=appmsg)

工具链接

```
https://github.com/shine798/DigDeep
```

**后台回复加群加入交流群**

**广告：****cisp pte/pts &nisp1级2级低价报考**

**陌笙安全纷传圈子+陌笙src挖掘知识库+陌笙安全漏洞库+陌笙安全面试题库****简单介绍****（****加入纷传圈子****送****知识库+漏洞库+面试题库****）**

如果觉得合适可以加入,圈子目前价格39.9元，价格只会根据圈子内容和圈子人数进行上调，不会下跌。。。

**圈子福利**

**edu漏洞挖掘1v1指导出洞**

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRKQWHxLsRrPqpqdiceX76d7yExQIyOqFmmJAfHQh7qzKvPc2V5z6iaa0RY6Ib8AsGvgS5MKkAk5aaHnJBaSnI10LDKQYMLcQMmg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboR8pnPeapLBK4Jsa4ufCvFoGL66t7PKeZyA3AjNxsObjtnCibN2gzGX7NMS7Wo5sj3YYL2iboeRuQDcWqiapc8xuo5fticoBG4DsyY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRKIBNIQIVicRWJLbyGRmg92vPzc8375PJpcYVvfywzwqnaeBicZuEbfvuic9KRdjwkahSDic5VqrH2Mb4NkqtkADl5HLIh8gPex60/640?wx_fmt=png&from=appmsg)

**陌笙src挖掘知识库介绍（内容持续更新中!!!)**

```
信息收集(主域名信息收集,子域名信息收集等&会永久提供fofa-key助力)弱口令漏洞&未授权访问漏洞挖掘任意文件读取&删除&下载&上传漏洞sql注入漏洞url重定向漏洞csrf&ssrf漏洞挖掘XSS&XXE漏洞挖掘等等常见漏洞cors&目录遍历&越权漏洞挖掘EDUSRC(证书站挖掘案例分享&edusrc挖掘技巧分享)CNVD挖掘技巧分享&实战案例报告编写公益漏洞挖掘（公益src挖掘漏洞分享&提供补天1权重资产）SRC挖掘实战(针对各种常见功能总结的常见测试思路等快速提升)经典常见Nday漏洞(常见中间件&以及各种常见框架)复现云安全相关漏洞挖掘（云key扫盲&云存储桶&快速识别云环境&云攻防）AI相关学习（AI基础&AI代码审计实战测试&webLLM攻击等）APP&小程序漏洞挖掘等各模块不在一一介绍
```

信息收集

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTu9DGyTubluhYicFynwVBKa4V06sDfEVKOyk5Q4ghZzLMDAuLb1M1oR4RJumGWrADPapFjTrOjpksKQ8q0YYCnl3ZWLof8Knzg/640?wx_fmt=png&from=appmsg)

src挖掘基础

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboR45bibbJEb28a1gS5yth3r5HyOsgPiaOUHHYriahZyIyrk0LMOsHW4VoDibyBRibTNzptGiaLWX62UwykicwvbxCJPopvklqiaxML8lS8/640?wx_fmt=png&from=appmsg)

src挖掘实战

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTKWnTsN6CXf3djhXIlMKNRjVmJn3g5b23ur9E6Cx3O68f0hXVjCiaj8J4RYeTGBecqf1k99phG0ice2wtd5lKgR46OeqeLQfMpk/640?wx_fmt=png&from=appmsg)

edusrc

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQVVlTXhibjR8UiakZBQicXRZrQ7hdoOz5G8MQrcuDBGbqJdO0kIz6R9IU4ObAeOiabT8pr6lc7jibdIkKoTjiaXNHPLAwAB3BV2UvLM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSCrvarBbzP4L9kS6P0LVH9JMdmcbFDKiaicHqMFgTxq3x4iatjDJQicmc7NPC14C9Fk3icFjrouSgNVaN8Byuf0C0Iq9O6D1XPvFvY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRALwXmgZ4mh2LW0RdicrKjBCP7P1iaF14G0Eq2v3KRnTJORpwXZlF58WEz6QicxLJpyJaA5iah5CF2rHjBz4JzOELFRaZTAKOQ2tQ/640?wx_fmt=png&from=appmsg)

经典nday复现

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRu8Gf849iaCkSBxLL8IlzJTRs185QicEe9l5UGI1dEVKISt2IGGveZynXBW9tIUsxNsz4adSTib7rib50uSJdjNfTvVRFrbPJhzL4/640?wx_fmt=png&from=appmsg)

云安全&AI安全

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQ9qiavETNjaaX162czpNCqpw3uJqVpicbI15AXzhf5x8icmHxBdTGOgRgzNPGF3Aw2gglT4Fx09JGXYibQC6U7CQKVmoH08l3meia4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQgcsjiaZ4S26TWowHfpBkhSeHf2pjrcDyicJuia3uqvRBauLEOicibibEMqibnBMtjopFL8No7UXNibbURvzeJ3dQHTibvGxRQGnorb4co/640?wx_fmt=png&from=appmsg)

**陌笙安全漏洞库介绍**

```
最新漏洞查看1day&0day分享EDU学校相关漏洞Web应用漏洞CMS漏洞OA产品漏洞中间件漏洞云安全漏洞人工智能漏洞其他漏洞
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTFBRMa8XwYxfcZMyXicx94xSKxawPcqFia2rJKOL7fSLYXiccwHc868XxNGIQ5z7ibiaI1MNAGRrK7U6wXJTsZOCAu2I5XV1boTAL4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSBzdakI9XI33ReAm2dxO8vgzw3JicQmUuWCb5ayBlKR1PoQHEHFETteBnicyupwU0mXvXibfrDoyg8nSWBGoK1p2YXY3ElhcvOQ0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSajCclDhuRpaLic9Ld915CHU7RqSC1LCrPGfNZiavdPEVeDedDWOPBhtMLCicTp3RNd1lT0Pmfo3mx5B0hUxbQg3ic6Via90NMtZVk/640?wx_fmt=png&from=appmsg)

**陌笙安全面试库**

```
渗透测试基本问题一汇总渗透测试基本问题二汇总渗透测试基本问题三汇总微步护网面试题目长亭科技面试深信服护网面试启明星辰渗透测试面试题目安恒面试题目绿盟笔试题目360面试奇安信护网面试运维面试题目运维面试题库网安面试相关文档大全相关面试文章推荐等等
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSoLqEzH0a3A4LQrvTIkGx81Sh5pf6fCoEQJhYg715vrJicSkfBuCoAmV2Kp4uOMe5jcUZutPwicibFibtJ1ZmyiaAibCg0XicWnsNcicE/640?wx_fmt=png&from=appmsg)

**POC库****&&更新适配afrog&&nuclei&&dddd的POC&1day/Nday等&&******dddd二开******工具[助力渗透测试&&红蓝攻防]**

**工具截图**

**![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRLmmY4kF0AaQjAJUQzH1sAExGoE7AmDJZXcEgdnKuRkpgZ9xYflY0UxtVkrP4HicDfvCWibXY86fAjH1E0TDJ5YqatD9fjZrUYk/640?wx_fmt=png&from=appmsg)**

**实战效果**

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSKqLXNcOPE07xOwOUCjRGuFphopPumW9RaticmNCuEUXu52GtdTTfpTUicrBj80kMcZzJsnps3abyvXIvLHEIhvMoXUApOqZCe4/640?wx_fmt=png&from=appmsg)

**poc库【后续持续更新】**

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTG9Lyp44aFffUOxQKtHjToGfqFWTjswYft0VtAPINtV5MqmrTTj8GWrVb6yowvHURubPgOqdribmibWEb0Fcj3YdN4iahUwItcxE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRAMJIIvexOOJa5KhrsKmlsx8bkwib9SPoK72Q0OSPWR5qx67yvl8scMQ5bg8caBXZH01kM39RDnKpnWSaTicgobRmLygERGFWls/640?wx_fmt=png&from=appmsg)

**AI赋能-****skill辅助****漏洞挖掘（免责&&慎用）**

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboR3Dib0RVxVhUOzS6ibC6BvkfulXQAclic0XCXMS35C4EPoqX1b2eMVj2CFiaLCelVs1szGibaHiaAq7WibRdwHUg0IwO8fjDdWxNv6eY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSXZZVels2NibmHgyxntlCRNIkgoqMPfUPwSM9O43OqniaZLDEJic9QRkW01gNTydFkibdI6yBRkJJ1sDUmfl7iaicoibz1QLp0J2pWE4/640?wx_fmt=png&from=appmsg)

**圈友ai辅助渗透****实战效果****，支持打假！**

证书站

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQibuxKAyHBZicB1t5yGVKyV82Teo8C2MbjKPytKziaXUcjPiao8ylHbD4vicAld8equC9alic3NksvWJ09wArXaPXZD...