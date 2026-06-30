---
title: 中国专利.Skill！一键自动化，查新、绘图、成文全覆盖
url: https://mp.weixin.qq.com/s/s8WVzdyVJpufKOqGeXZpPg
source: Doonsec's feed
date: 2026-06-29
fetch_date: 2026-06-30T06:06:05.963398
---

# 中国专利.Skill！一键自动化，查新、绘图、成文全覆盖

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TVljsu2eAicI3ShKMRnVgcD2XaG1J7MEaRyVAlWsTh7MO4fNpW804lCvtyhC6rXbjEctW40SmicAjUGtwA7EQjpFBsIAVNIgIicnXpLuAVO1AA/0?wx_fmt=jpeg)

# 中国专利.Skill！一键自动化，查新、绘图、成文全覆盖

原创

hacking
hacking

Hacking黑白红

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

GitHub 看到一个skill：`patent-disclosure-skill`

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TVljsu2eAicKh1jZY3EhHx35ib5zCAC1mibibYogByeESYpmPm54w5iadcl5mE5f7K88d4DPAgibzVu7scxPTUA81ICdlaLiaO6BHD93RHXDzIK5gI/640?wx_fmt=jpeg)

这项目名字直译叫"专利披露技能"，实际上是一个给 Claude Code 和 Cursor 用的 Agent Skill。它把写中国专利交底书这件事拆成了流水线，从读代码到出 Word，全流程自动化。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicLFQ1S97NueJugqolHcMHQkOzOkBN7qO8ztypfBrbvmr2iaWhMfVbjP71NlUiaOE4OKeglJUjRAPLTN3iaxSGypBaia1nHzB6TI008/640?wx_fmt=jpeg)

研发写专利痛点，一套工具全打通

开发申请软件专利流程繁琐：

梳理代码提取创新点、绘制架构流程图、国知局手动查新、多轮修改定稿，人工操作耗时耗钱。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicKws4XlnZGNjYpnUy9dKZcktxZtE0saT3TlicUUh2z4ow5ooTIgnKDxLN3Png9aT7vkJvrTEOxYuOBaX6mEee2XGR3kRjVVNR2o/640?wx_fmt=jpeg)

GitHub上新开源 patent-disclosure-skill ，适配Claude Code、Cursor，把国内专利交底书做成标准化流水线，直接输出可交付Word底稿，大幅降低研发写专利成本。

六大核心功能，覆盖专利全流程

1. 智能解析项目文件

自动读取代码、Word、PPT，统一转Markdown解析；大型仓库定向检索，无需全量遍历。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicIuWseVMsoBLrQBRiasqjia4cPNkKnPQUQpSwDL5BWDpdW5LmgTUTic38IrO9WR3ABYtfHMk909dc9lb4mETud0zZkDZlmDmDhlyA/640?wx_fmt=jpeg)

2. 精准挖掘专利创新点

不会直接生成文稿，先筛选、沟通候选专利点，确认后再进入撰写环节，避免无效内容。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicI0FD3WrquppMaWyjYdXWSG9gor84tJdpgvjA8tWNibGib0hQ7lvYGpic0MiaL7WC46PvJGem4grRh7DUD9rnQpbAOls1wLCEeZmqY/640?wx_fmt=jpeg)

3. 官方渠道专利查新

优先爬取国知局公告站检索新颖性，接口异常自动切换全网搜索，检索结果直接写入交底书。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TVljsu2eAicLC2CejVHkmqp0pIQBakVg6FYUS9QVgO6UB12mbNkiav18wzQ07yW90SSYdI24gb0d6pwpUcJXuQPPaZWHuKBsTBm2ZEiceZaOiaM/640?wx_fmt=jpeg)

4. 自动生成规范交底书

内置专利模板，自动生成Mermaid框图并渲染图片，同步输出Markdown与Word，代理人可直接修改。

5. 版本迭代全程可追溯

补充材料、纠错自动生成带时间戳新文件，留存完整修订对话记录，多版本互不覆盖。

6. 内置自检校验机制

定稿后台自动核查逻辑、参数一致性，减少人工反复校对。

极简部署，自然语言直接调用

Claude Code通过Git克隆至.skills目录；Cursor放入指定技能文件夹重启即可。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/TVljsu2eAicIEicmy9EG9ejUbWUexTSvMKx1dlCtOCKM0ByPIwdNTKQ6lVf7P7oB9eibjugrerPEOibHfZ5bKFTEChnffEAxC0BibHylTWqYuGYY/640?wx_fmt=jpeg)

需安装Python、Node.js依赖，用于文档转换与图表渲染。使用时输入自然语言需求，或斜杠指令 /交底书 附带项目路径即可启动。

上手步骤

**Claude Code：**

mkdir -p .claude/skills

git clone https://github.com/handsomestWei/patent-disclosure-skill.git .claude/skills/patent-disclosure-skill

**Cursor**：把仓库完整内容放到Cursor约定的skills路径，重启后在Settings里确认技能已被发现。

**依赖**：pip install -r requirements.txt。国知局查新需额外装Playwright。渲染mermaid图需要Node.js。

实际跑起来，在Agent里用自然语言说就行——

**“帮我挖一下这个项目的专利点，写份交底书。”**

就这么简单。

工具优缺点客观点评

项目开源两月收获近3k Star，细分工具热度亮眼。核心优势是适配国内专利规范，原生对接国知局检索，区别于仅支持海外专利的同类工具。

局限在于仅兼容Claude Code与Cursor，VS Code Copilot暂不支持；国知局网站偶有访问故障，降级搜索数据时效性偏弱。

该工具无法替代专利代理人，但能包揽检索、格式、初稿撰写等重复工作，是研发、知识产权从业者高效提效利器。

![](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicIBichnvfaHp0wjvQCibToQRfndHLOPc3Trco5WImIo4iaibUh46ydJJuhff3Xq0URonTEjn3SINtXDBMWAicUCLCbKX6BCqnJAb8fI/640?wx_fmt=jpeg)

GitHub仓库地址：https://github.com/handsomestWei/patent-disclosure-skill

作者：hacking。前北漂程序员，现在做安全。文章数据来自网络，大模型优化，侵权删。

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONTk9JHJcRia5QdqxUfpBz4cb5VGKUIUyrVaviawse20DccoB4C6WKwxm6xVzq4oU7dSdfxryTMc9Vvg/0?wx_fmt=png)

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