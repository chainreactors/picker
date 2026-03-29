---
title: 装了几个插件，花了20多块钱Token
url: https://mp.weixin.qq.com/s/ml-7FcS2gdtMyYvx1MZBqg
source: Doonsec's feed
date: 2026-03-28
fetch_date: 2026-03-29T04:40:39.579641
---

# 装了几个插件，花了20多块钱Token

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/LjdkpgSF7PdCaUUmFoMvF0mehTRIz28cjUxDckN2y3sHOYANGgKOafe7zRSCmF3KPib2qNeLslXexrwsJICJXunVTw84qGUPONqwLgON4Yy0/0?wx_fmt=jpeg)

# 装了几个插件，花了20多块钱Token

原创

hyang0
hyang0

生有可恋

![]()

在小说阅读器中沉浸阅读

在使用 Claude Code 的过程中一定要注意 token 用量统计，大部分平台都有详细的实时用量记录。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LjdkpgSF7PcjVjmL5XFaicHRgF825EMMUf3icfMyr0sKibNico8QiaTD8hTPv2ibWdhBsMkmJrmkccNJX1pjiaZVU94mo4taNTY23nibprnTW0J9EWY/640?wx_fmt=png&from=appmsg)

Claude Code、OpenClaw 等 Agent 对 token 的消耗有可能突然暴涨，在使用过程中一定要实时查看费用情况。Coding Plan 也有用量统计，不要用超了，用超了 API 会短暂连不上，到下一个记时周期才会重新刷新。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LjdkpgSF7PfueIKQpOHmulQKgt01a17WSKU4xzib3libfOTDPQUJ4A50r03Cvh7cAX3m5kyx6kKcCa0MGTNHReL3o6XqgFvWLpz9QNBrRFfW4/640?wx_fmt=png&from=appmsg)

火山平台的 Coding Plan 用量查看地址：

```
https://console.volcengine.com/ark/region:ark+cn-beijing/openManagement?LLM=%7B%7D&advancedActiveKey=subscribe
```

硅基流动的 token 用量查看在：

![](https://mmbiz.qpic.cn/mmbiz_png/LjdkpgSF7Pd3e4skPfpRu71tb2TX2yG3Efcjj6eN3WdvQfsibrFBnc4JQyXec6C0A1iaLb54GxI5c9HFnYsvExzrvvjDIyHxKb92kCfh7HaiaU/640?wx_fmt=png&from=appmsg)

下面看下我今天都执行了什么这么快就干掉了20块的 token：

![](https://mmbiz.qpic.cn/mmbiz_png/LjdkpgSF7Pf1YbPIkL5dldL6jEvwXgKia1lhbsuoSmWcyqDBFXdAJcePoWKyuib4V5gHQsmkgHATgE5LTu1cAHxw3sRMajAwibZ9Tia018Ywy04/640?wx_fmt=png&from=appmsg)

装了三个卡神推荐的插件，提示词如下：

```
帮我安装这个Skill:                                                                                                                                                         https://github.com/obra/superpowers
```

```
安装以下技能：https://github.com/anthropics/skills
```

```
帮我安装这个 skill：https://github.com/eze-is/web-access
```

然后测试了一下 eze 的 web-access 搜索插件：

```
⏺ web-access skill 已安装成功！  主要功能：  - 联网工具自动选择（WebSearch / WebFetch / curl / Jina / CDP）  - CDP Proxy 浏览器操作（直连 Chrome，携带登录态）  - 支持动态页面交互、视频截帧  - 站点经验积累（跨 session 复用）  环境检查结果：  ┌────────────┬─────────────┐  │    依赖    │    状态     │  ├────────────┼─────────────┤  │ Node.js    │ ✅ v25.5.0  │  ├────────────┼─────────────┤  │ Chrome CDP │ ⚠️  需要配置 │  └────────────┴─────────────┘  启用 CDP 模式（浏览器自动化）：  1. Chrome 地址栏打开 chrome://inspect/#remote-debugging  2. 勾选 Allow remote debugging for this browser instance  3. 可能需要重启浏览器  安装后可直接使用，例如：  - "帮我搜索 xxx 最新进展"  - "去小红书搜索 xxx 的账号"  - "同时调研这 5 个产品官网"✻ Baked for 60s❯ 帮我搜索 数字生命卡兹克 的最新进展
```

由于我个人网络的原因，web-access 的表现不是很好，没有搜到有用的东西。又让它搜了一下 frontend-design 技能的信息，它提示我已经安装了。

```
搜一下 frontend-design skill 的信息                                                                                                                                        Read 1 file (ctrl+o to expand)⏺ frontend-design skill 信息  ┌──────────┬────────────────────────────────────────────────────┐  │   属性   │                        内容                        │  ├──────────┼────────────────────────────────────────────────────┤  │ 名称     │ frontend-design                                    │  ├──────────┼────────────────────────────────────────────────────┤  │ 用途     │ 创建高质量的、具有独特设计风格的前端界面           │  ├──────────┼────────────────────────────────────────────────────┤  │ 触发场景 │ 构建 web 组件、页面、应用、海报，或美化任何 web UI │  └──────────┴────────────────────────────────────────────────────┘  设计理念：  1. 设计思考    - 理解目的：解决什么问题？用户是谁？    - 确定风格：极简主义、极繁主义、复古未来、有机自然、奢华精致等    - 差异化：让它令人难忘  2. 美学指南    - 字体：避免 Arial、Inter 等通用字体，选择独特、有性格的字体    - 配色：使用 CSS 变量保持一致性，主色调+锐利点缀色    - 动效：CSS 动画、React Motion，页面加载动画、滚动触发、hover 状态    - 空间布局：非对称、重叠、对角线、打破网格、负空间    - 背景细节：渐变网格、噪点纹理、几何图案、透明层叠、阴影、边框  3. 禁止使用    - 通用 AI 审美（Inter、Roboto、Arial）    - 老套配色（紫色渐变+白底）    - 千篇一律的布局和组件  核心原则：大胆选择，极致执行。 无论是极繁还是极简，关键在于意图明确、细节精致。
```

差不多就干了这点事，token 账单咣咣地涨，还是推荐手工安装这类 skill，一条命令就搞定了。让 Claude Code 安装 Skill 看起来智能，实际上它也是进到 github 项目中读 Readme.md，然后按照 Readme 中的要求去安装。

不如直接自己去读 Readme.md，毕竟不花钱。不信，我给你读一个：

```
https://github.com/obra/superpowers
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LjdkpgSF7PeMEAqfrhRJqsToa9ChibQ1KB3U4pmcDPHsoicBl1rmqD9ydRxFg5LYGn2iatar1NN23bicWdicZTKZ3ZvO325VpRPxiaeflFeT4oa3c/640?wx_fmt=png&from=appmsg)

Claude Code 手工安装方法，执行以下两步：

```
/plugin marketplace add obra/superpowers-marketplace/plugin install superpowers@superpowers-marketplace
```

然后，这就完了，就这么简单。

如果你让 Claude Code 去给你安装，我截图给你看：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LjdkpgSF7Pe9xKAUpZ6dS6Psjd7T9CdB8TRU2ydOpVmXsNfYrtO7YEQqmkY6ibAfZfKRniaqZycQzCSa5uUfd13AN284QB3lb6YoARTEufCpw/640?wx_fmt=png&from=appmsg)

差不多，上面推荐执行的就是 Readme.md 中读到的步骤。Superpowers 没有花多少 token，web-access 是真花 token，如果不是包月尽量少用。

全文完。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ulAibOLeecVtlibejT79OV1CEtDxRdopU4ZpHTLW4EDibaYb0p30STPSN6c6ZLX3qIB67IrbuElJkFgNRJfW1Fg3g/0?wx_fmt=png)

生有可恋

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ulAibOLeecVtlibejT79OV1CEtDxRdopU4ZpHTLW4EDibaYb0p30STPSN6c6ZLX3qIB67IrbuElJkFgNRJfW1Fg3g/0?wx_fmt=png)

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