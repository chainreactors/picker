---
title: 警惕！校园学习接口暗藏 SQL 注入风险
url: https://mp.weixin.qq.com/s/Y1vF0qcGLbvL4xpGikqc8g
source: Doonsec's feed
date: 2026-10-01
fetch_date: 2026-10-02T07:44:18.740609
---

# 警惕！校园学习接口暗藏 SQL 注入风险

# 警惕！校园学习接口暗藏 SQL 注入风险

三垣网安

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/SxoDJcKqQGI3OyCTvCV745ibTKPZQZibq65nNHPEpE2IibUtDhEQIdvqQhGd1Aq6AdchZ8mzHoBYNdX5W28jRb4YzUHsCXSPJmfZa7EF3Y2K44/640?wx_fmt=png&from=appmsg)

**目录**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SxoDJcKqQGK2wO4s78iaCv39M5xueW48TjdDicMthUXp7tX4EpAquKXjpz85AnA5oEUyKCkvkf1icexJqFjBp1cRfdu7mt9pwq8iao9Z6bibWF1A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/SxoDJcKqQGLicK3nfE6R3QdeVeH0hnxrN2ibeHA1ZbJxHp4ocPItoicLKBNA05VG1Pt8YD7PZicHxkYbexySstdNibYHQTOKahvSqhsnrt8Xf66o/640?wx_fmt=png&from=appmsg)

1.漏洞背景

2.漏洞复现

3.漏洞危害

4.修复建议

**一、漏洞背景**

本次测试目标为某职业院校智慧学习平台，资产暴露在互联网公网，平台具备课程中心、课程创建、教师选择、学员管理等教学业务功能。在对平台业务数据包抓包分析过程中，发现一处参数存在 SQL 注入安全风险。

**二、漏洞复现**

1.登录后台

![](https://mmbiz.qpic.cn/mmbiz_jpg/SxoDJcKqQGLFPIFK1qFcNo0lKsQOTv4iaNjRraMiaEBsyLRlAWwYNtzNQGGLfS354UlEqJoic7ARRkqguIEK0aWWzrUVMS1Q2ibNo9uDdhKavU8/640?wx_fmt=jpeg&from=appmsg)

2.在微课负责人选择处抓包

![](https://mmbiz.qpic.cn/mmbiz_jpg/SxoDJcKqQGLKkZmc7DtLekv0OicCkdaoZcFG8KsPicydCvcwJwzqY8XHz9C2xQqlJAnH182leicnWtTYrmMiajXLmD6G63ej4Mnr4oqdXWIE0wo/640?wx_fmt=jpeg&from=appmsg)

3.在教师列表数据包中发现参数

![](https://mmbiz.qpic.cn/mmbiz_png/SxoDJcKqQGIwiaJmMEusA1w2SdOhb2tpicwwpRwSIib3a3xn4dLsLsyBWLvw5NIGAsbCYn29G1rJ2VZRMaehflj3CQIO3xtzp9b1w6T6EeuE6Y/640?wx_fmt=png&from=appmsg)

4.尝试注入，单个引号报错，两个引号正常，判断存在sql注入

![](https://mmbiz.qpic.cn/mmbiz_png/SxoDJcKqQGJRe5tccRI9Nd2ZIicoqZeTdaicRXlhXgRhXWz5G7cDCJt5eav1V1ibs1FNVOUVJv4tPX2eWq1lN866XH5cG9H1nELn6opfPQMYZ4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SxoDJcKqQGLV9SaHYRrwXibbia0tNjQHWyyQaM9IgPEoluNH6N9adicEy9XeGC1FaQeNfoRssUd0Y4eXgDo56k3bo1YTic71W5bBHub6CItl7ibI/640?wx_fmt=png&from=appmsg)

5放到sqlmap中跑，得到数据库名，sql注入漏洞存在.

![](https://mmbiz.qpic.cn/mmbiz_jpg/SxoDJcKqQGIicxNI8VUq7ooN9kIAHlhLReLUicmcyGn8T9KicA3Mib6gGhNQlgwsIOYquYMy6gv3vsmdibFJHds6pBRqTtxoTlDuxxiacEHwHuhrA/640?wx_fmt=jpeg&from=appmsg)

**三、漏洞危害**

1.数据泄露：攻击者利用该漏洞可读取全部业务数据库，获取教师账号、学生信息、课程数据、账号密码等敏感校内数据；

2.数据库篡改：条件允许情况下可实现修改、删除数据库数据，篡改教学业务信息；

3.权限接管：读取管理员账号密码，登录智慧学习平台后台，接管平台管理权限。

**四、修复建议**

1.优先使用预编译语句（PreparedStatement），杜绝直接拼接用户输入到 SQL 语句，从根源防御 SQL 注入；

2.输入过滤校验：对前端传入参数做白名单校验，严格过滤单引号、特殊 SQL 关键字；

3.最小权限原则：业务账号数据库权限做收缩，业务账号禁止 drop、alter 等高风险权限；

4.统一异常处理：不要直接抛出数据库原始报错信息给前端，自定义错误页面，避免泄露数据库结构信息；

5.WAF 防护：部署 Web 应用防火墙，拦截 SQL 注入特征攻击 payload；

6.安全测试：上线前对所有接口开展安全测试，重点检查查询类接口可控参数。

**点击关注三垣网安**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SxoDJcKqQGLNUR5XXC6Y4kIWtSrDibDOFodgy2ykNeMMs7tnxGpItLPBNylWIKISDZm7742X9aGBs3knA91CyXxdxbQwhOO2hrdhOG6Iib8icw/640?wx_fmt=png&from=appmsg)

**了解更多网安知识**

#SQL注入 #渗透测试 #实战案例

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/SxoDJcKqQGJaWOwicn7raXm5k4xXDlBia0Okyg0R9d4niakArWeAcFZe0mbIWPKXdgcJHv0mIY6picqR7UB0GmPPeMC70E9VFWMXDEdYOj8GS3o/0?wx_fmt=png)

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