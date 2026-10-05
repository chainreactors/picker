---
title: [工具推荐]EduSRC 教育行业猎洞工具 —— 基于搜索引擎 Dork 的一键式侦察 Chrome 扩展-crazyedusrc
url: https://mp.weixin.qq.com/s/LbjkKb7WI7aPkQh4wdXwXQ
source: Doonsec's feed
date: 2026-10-04
fetch_date: 2026-10-05T07:54:01.398809
---

# [工具推荐]EduSRC 教育行业猎洞工具 —— 基于搜索引擎 Dork 的一键式侦察 Chrome 扩展-crazyedusrc

# [工具推荐]EduSRC 教育行业猎洞工具 —— 基于搜索引擎 Dork 的一键式侦察 Chrome 扩展-crazyedusrc

dollmarker
dollmarker

陌笙不太懂安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

免责声明

```
由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号陌笙不太懂安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉，谢谢！
```

工具介绍

crazy\_edusrc 是一个面向 EduSRC 教育行业授权安全研究的 Chrome 扩展工具，它基于搜索引擎 Dork 语法，把多条针对教育行业敏感信息的查询语法集成到侧边栏面板中，用户在 Google、百度、Bing 等搜索结果页一键点击即可同步跳转查询，从而快速发现教育行业目标暴露的敏感信息与潜在漏洞入口，辅助安全研究人员在授权范围内高效完成前期侦察与信息收集。

## 功能

### 教育行业专用语法库（60+ 条）

按 8 类攻击面组织，全部支持 {target\_domain} 占位符：

| 分类 | 覆盖内容 |
| --- | --- |
| 敏感文档 | 学生名单 / 花名册、身份证号文档、全字段表格、**工资津贴表**、录取名单、成绩单、奖助学金、教职工信息、党员信息、论文 |
| 个人信息 | 身份证+手机号关键词、学籍异动、**心理咨询记录**、简历泄露、试题答案、**文档内口令** |
| 后台入口 | 管理后台、OA、一卡通、图书馆、宿舍后勤、缴费财务、**教务处后台**、监控门禁、实验室管理 |
| 统一认证 | CAS、办事大厅、WebVPN、**深信服 VPN 指纹**、SSO 门户、邮箱、微信入口 |
| 组件指纹 | 正方（新版 jwglxt / 旧版）、强智、青果、招生就业、Nacos、Druid、Swagger、**Spring Boot 端点**、Jenkins、phpMyAdmin、UEditor、**泛微 / 致远 / 通达 OA**、**用友 NC** |
| 配置泄露 | 数据库备份、网站备份、.env/config、.git/.svn、日志、容器/K8s 配置、**数据库连接串** |
| 目录遍历 | 开放目录、上传目录、备份目录、索引中的表格 |
| 通用侦察 | 报错泄露、测试/旧系统、弱口令、上传接口、论坛、API 文档 |

### 资产测绘四档联动

| 模式 | Fofa | Quake | Hunter | ZoomEye | 用途 |
| --- | --- | --- | --- | --- | --- |
| 主域 | domain="x" | domain:"x" | domain.suffix="x" | site:"x" | 基线资产 |
| **证书拓线** | cert="x" | cert:"x" | cert="x" | ssl:"x" | **找同证书的旁站与隐藏域名** |
| 组件指纹 | domain="x" && (title="k" || body="k") | 同左 | 同左 | 同左 | 直接定位爆洞组件 |
| 备案主体 | icp="k" | — | — | icp:"k" | 按单位名找全部备案域名 |

外加 6 个侦察入口：crt.name（证书透明枚举子域，国内直连）、Wayback（历史快照找回下线系统）、VirusTotal、Shodan、爱企查、ICP 备案。面板实时显示生成的查询语句。

### 队列式「一键跑高危」

v1.0 是 `slice(0, limit)` 直接丢掉剩余语法，且无延迟连开标签页，极易触发搜索引擎人机验证。v2.0 改为：

* 全部高危语法入队，按「每批 N 个」推进
* 标签页之间随机抖动延迟（默认 1200ms），批与批之间再额外等待
* 实时进度条 + 「停止」按钮
* 每执行一条即打上「已执行」标记

### 敏感 URL 分级高亮

10 类特征按危险程度分三级着色：

* **critical**（红）：数据库 / 备份 / 配置 / 版本控制
* **warn**（橙）：后台 / 接口调试 / 上传点
* **info**（青）：学生数据 / 证件信息 / 文档

敏感项自动排到列表最前，可一键导出 CSV（含 URL、等级、命中标签）。

### 其他

* 语法实时搜索（面板内按 `/` 聚焦）、分类筛选
* **「已执行」跨会话记录**：知道这个学校跑到哪了，悬浮球上显示进度
* 语法库导入 / 导出 JSON（便于团队共享），导入内容强校验
* 跨校猎洞：对全量 `edu.cn` 资产执行 9 类高危语法
* 面板可拖拽、位置记忆、收起为悬浮球
* 快捷键：`Alt+Shift+S` 面板、`Alt+Shift+R` 跑高危、`Alt+Shift+U` 提取 URL、`/` 搜索、`Esc` 收起
* URL 黑名单（域名 / 通配符 / 正则）
* 明暗双主题 + 跟随系统
* 数据全部本地存储，零上传、零追踪

## 界面预览

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTvJaUGicytsibdGt2ia9C6byO4JU6xm3G4fkIzymUoAAUX4Hpscriaicrf9HTZaPIHfe0jFO94ViaJGm4Kf58J5r506HNGEIrwEIbQE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSgrqzOkKtYibW6wXZrico1LYk8hS7ibbibMFeTrIIGrLib0qLYsbEwv6oDsmUKUw6qpiaIDcaicFMLrPtGrNOQ6w9Ur0OIqONrHRed00/640?wx_fmt=png&from=appmsg)

### 一键提取页面 URL

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTOMFSHONNfkicYCS2EnqY1aoPljpZnULNsReThEDsvQe7WjvlDRjDZ1oNQHhLbPAbNdG1R5TTZwNkbZPQS6wpfkgDQB77HqFKg/640?wx_fmt=png&from=appmsg)

在百度 / Google / Bing 的结果页，面板会自动停靠在右侧；切到「URL」标签页点「提取本页 URL」， 即可把当页所有结果链接抓下来，敏感目标按危险等级着色，支持复制全部与导出 CSV。 抓不到时面板会给出诊断计数（扫描多少条、被谁过滤掉多少），并提供「强制全页扫描」兜底。

## 工具安装

```
cd crazyedusrc-v2.0npm install          # 首次npm run build        # 产物在 dist/
```

1. 打开 Chrome → chrome://extensions/
2. 开启右上角**开发者模式**
3. 点**加载已解压的扩展程序**，选择 dist/ 目录

开发模式：npm run dev（watch 重新构建）；类型检查：npm run typecheck。

## 工具使用

1. 在 Google / 百度 / Bing 执行 site:目标学校.edu.cn，面板自动出现
2. 「语法」页按攻击面逐类排查，点一条就跳一次搜索
3. 「URL」页提取当前结果页链接，红色标记的高危项优先核验
4. 「测绘」页用**证书拓线**找主域之外的边缘资产，用**组件指纹**直接定位爆洞系统
5. 没搜 site: 时按 Alt+Shift+S 手动唤起，在目标栏手填域名

工具链接

```
https://github.com/dollmarker/crazy_edusrc/tree/main
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

**skill+grok辅助挖掘某企业sr****c****实战效果，能出但是重复多，agent独立挖掘也可以，见仁见智，看个人习惯，好的模型是最重要的。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQwyn779TTwY7vZkePQCL8k3K8dYxNdyzfgADL4dJcNUvpmodLeDVCZ6xDC4RJXEBmO2tcWqgUNdTVicKTW0jpdsg7X6xwP5gIQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQnIqagDL2A4BUIXrib9YVmATWuaIDqETqYd9ToHib52mDyoMyqc6Wzh733FRnbsDsGgey7B8s8jr72UtkPY6ich58niaPJqoItKcE/640?wx_fmt=png&from=appmsg)

**企业src边缘&核心资产实战效果&&有重复但是证明好模型+AI确实够用**

**（图片仅供参考，我出不等于你出，见识**到**ai神力即可，多去用AI!!!）**

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboT1YNI9U6r6NMO4UMUBROoWeC4XQC4Dge94ODZ7tXY6tbxqb3IJoghve0u1SfkygE5UJ5HTdUBvLZKrn5ps13F71piax5dlHnOE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboTGjdxKy4nllaLXIznTvRqicichITccuB8psYFRYakw6ViauCk6iccziahfPw4fnrqhyCp7Zkq7lRI0DOicyrZlNyicYibTVibfGFZVaG0c/640?wx_fmt=png&from=appmsg)

**不是P图,单洞1.2w记录**

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQQpQdR2Ttwqxibyr75Is0kBG2N2tLYQIaau7SS278oyQ4RDpNScviaMt4wtlfgDCibE05WgoMhE5kZUrP8ciaYIdnxA594wsmoAAs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSRn2EsfFkA5mG6dcn7JLQMroc2dy3EQb3ueY2Cspd0WYgicXEnSF68UD43nNd4plkxmkTpEOh2kkQMEWZZIjE0ibA8r1q4IfiaxI/640?wx_fmt=png&from=appmsg)

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

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRbZ1HYm7R7YEiaxRVQibGWyricx9l7HpGjS4ZfWRdlft8iacwkpzYyZfmYEkWdJgYRORPkNFR6dADR5MyE524tWX6cAwN8MmrCZu0/640?wx_fmt=png&from=appmsg)

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

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSB...