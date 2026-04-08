---
title: Openclaw开发之ARL资产灯塔对接skill
url: https://mp.weixin.qq.com/s/GdygVFxIHm2GlvgZo159MQ
source: Doonsec's feed
date: 2026-04-07
fetch_date: 2026-04-08T04:31:24.768948
---

# Openclaw开发之ARL资产灯塔对接skill

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/niasx7fyic9CMJA6iatiax4lyz0giaAbA7ZcaTBKPY7cicLgNGmRYH8ia4ACJia1esAo73E9lUlIGeU6yIxAf5US6HdhicWFMM6YxUwlCUKR1kTiaibDXA/0?wx_fmt=jpeg)

# Openclaw开发之ARL资产灯塔对接skill

原创

油漆工
油漆工

C4安全

![]()

在小说阅读器中沉浸阅读

很多人用 ARL，可能都喜欢手动在“打开页面—填目标—勾选选项—等结果”这一步。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9CMQDy5aPIbsdVz34gOicPLHFX4UZs6fKxXTgvbQ1ib2MX9KxlXApJNIjh4MeiaPe76MIUajga2j1PupNAwlo9ubEyqdJN10JWRXBM/640?from=appmsg)

这套方式当然能用，但一旦场景变成：

* 批量下发目标
* 固定策略重复执行
* 扫描结束后自动提取结果
* 把结果继续交给 AI 汇总或写报告

Web 页面就不够顺手了。

这次开发的是直接把 ARL 后端 API 封装成一个可复用 Skill：arl-scan-api。

![](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9COxOEOiboia28QWmUey6WH8ztjV5EZ42tSwibXq7DvHetVyuQbPssfDOHT7YVVJ5bn5PF5HBO4icsSnpIOH1EufO9FfVGBGsU9XUFM/640?from=appmsg)![]()

它解决的核心问题只有一句话：

```
让 ARL 从“手工操作工具”，变成“可自动化、可编排、可被 AI 调用的能力节点”。
```

---

一、这个 Skill 到底做了什么？

这个 Skill 的核心文件很简单：

* SKILL.md：定义能力边界与使用方式
* USAGE.md：使用说明
* scripts/arl\_api.py：真正执行 API 调用的脚本
* references/api-map.md：接口映射
* references/payload-examples.md：请求示例

从能力上看，它主要做了 4 件事：

1）自动登录 ARL

支持两种认证方式：

* 直接使用 ARL\_TOKEN
* 使用 ARL\_USERNAME + ARL\_PASSWORD 自动调用 /api/user/login 换 token

也就是说，调用者不必手工先去页面里取 token。

2）下发扫描任务

支持直接调用：

* /api/task/：一次性任务提交
* /api/task/policy/：基于策略的任务提交

适合两类典型场景：

* 临时扫一次
* 复用固定策略反复扫

3）轮询任务状态

Skill 支持等待任务执行完成，直到任务进入：

* done
* stop
* error

这一步非常关键，因为它把“提交任务”和“拿结果”之间的人工等待去掉了。

4）按集合精确取结果

ARL 的结果分散在多个集合里，不同需求要查不同接口：

* task
* domain
* ip
* site
* url
* vuln
* nuclei\_result
* wih

---

二、为什么不用网页，而要走 API？

原因很现实。

在人工使用时，网页最直观；但在自动化场景下，网页恰恰是效率瓶颈。

举个常见流程：

传统方式

![](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9CPhPLicrLoJs62f2TS5rjCRsKw5VOcmROSQgUvghuib5CAiclblmKgsFCgSziaOId9DWibUVDmS59uGjncsBkWDve6eqvbfhvmauSWQ/640?from=appmsg)![]()

1. 打开 ARL
2. 填目标
3. 勾选扫描项
4. 提交任务
5. 过一会回来刷新页面
6. 手工点开任务看结果
7. 再导出、整理、写汇报

![](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CPTQrXyZSbUsI7caXynTLMkURDQPKeH5qiaHic941dx8M4PmHVYNzJEbX3V6BcspRu22CduibVQPBOTQzFZjvBn7TpphAZia0w7MGc/640?from=appmsg)![]()

Skill 方式

1. API 提交任务
2. 自动等待完成
3. 自动拉取 site / vuln / nuclei\_result
4. 交给 AI 汇总成报告

差别就在这里：

```
Web 适合“人操作”，API 适合“系统协作”。
```

而安全工作流真正要规模化，靠的一定是后者。

---

三、Skill 如何对接 ARL

本机 ARL 服务地址是：

```
http://127.0.0.1:5003
```

然后 Skill 的推荐环境变量写法是：

```
export ARL_BASE_URL="http://127.0.0.1:5003"
export ARL_USERNAME="admin"
export ARL_PASSWORD="你的密码"
```

然后就可以通过脚本直接调用。

例如查询任务列表：

```
python3 /root/.openclaw/skills/local__arl-scan-api/scripts/arl_api.py \
  --base-url http://127.0.0.1:5003 \
  --username admin \
  --password 你的密码 \
  query task --size 10
```

这个命令做的事情其实很清楚：

1. 自动登录
2. 拿到 token
3. 请求 /api/task/
4. 返回结构化结果

---

四、skill适用场景

场景 1：定期资产巡检

每周或每天把一批域名、IP 自动送入 ARL，任务完成后自动汇总站点与漏洞结果。

场景 2：攻防演练快速落地

需要快速把多批目标下发给 ARL，统一拿回 site / vuln / nuclei\_result 做分析。

场景 3：AI 安全助手联动

把 Skill 接给 AI 助手后，可以直接通过自然语言让 AI 完成：

* 提交扫描
* 等待结果
* 拉取数据
* 输出总结

场景 4：平台集成

如果你已经有自己的安全平台、Bot、自动化任务系统，就可以直接把 ARL 接成后端能力。

---

五、结语

ARL 本身功能已经很完善了，但当需求走向自动化、平台化、AI 化时，光靠页面就不够了。

arl-scan-api 这个 Skill 做的事，是让资产发现、扫描编排、结果提取，开始真正进入自动化工作流。

![](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CNMntn4Aob0wyjibRHoTBuiamzgKSOnr6eAHAaJXqOKwBUHJGmjt4KnqiassESiaw8S8buaML6fTccpribPKLkj1jItDAbDvfA0kXYM/640?from=appmsg)![]()

这个skill我放进内部知识圈里面分享了，师傅们可以下载使用。

```
https://wiki.freebuf.com/societyDetail/articleDetail?society_id=184&article_id=216412
```

---

感兴趣的师傅可以公众号私聊我进团队交流群，咨询问题，hvv简历投递，nisp和cisp考证都可以联系我

内部src培训视频，内部知识圈，可私聊领取优惠券，加入链接：

https://wiki.freebuf.com/societyDetail?society\_id=184
安全渗透感知大家族

![](https://mmbiz.qpic.cn/mmbiz_png/niasx7fyic9CO7ibAkqvwp75NGAamSCtUib7dAxDOcg41coZhjLYSvknDVdyyHrgC1cB6V3e0h6yfBwAAFKhOfe1DXleeT743iacxeIvd5uDgVqA/640?from=appmsg)![]()

（新人优惠券折扣20.0￥，扫码即可领取更多优惠）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/niasx7fyic9CPgKictJKqT0ZaQy9lWgqLfR62ZQbRzjsaKkqnPGhWBWUTW4RQWxv7s3WBvqSwJbYqNBp2AtlepEgjxuwcMhQ5olsJTwRzG2Tu0/640?from=appmsg)![]()

![](https://mmbiz.qpic.cn/mmbiz_jpg/niasx7fyic9CPDYQ9VugNMre3WTDGeChiaiceKBTEN4jX41cZ3qCkPcKU4tYCibRLwkkJ55ZzibIfDCbvdhOyiaib0aBp5CMrv5v2icG1emva0TyISm0/640?from=appmsg)![]()

加入团队、加入公开群等都可联系微信：yukikhq，搜索添加即可

END

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJQiaZKk16p8ASnxuOUZiaJWeVzm5jndulrhBy63D46ic8H6lq8tpJfXTCNEhUeq9LckNiaObB9Auiaicp2Q/0?wx_fmt=png)

C4安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/EXTCGqBpVJQiaZKk16p8ASnxuOUZiaJWeVzm5jndulrhBy63D46ic8H6lq8tpJfXTCNEhUeq9LckNiaObB9Auiaicp2Q/0?wx_fmt=png)

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