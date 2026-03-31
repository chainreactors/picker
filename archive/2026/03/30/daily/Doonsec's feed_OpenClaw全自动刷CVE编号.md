---
title: OpenClaw全自动刷CVE编号
url: https://mp.weixin.qq.com/s/JdsNZoUpRmrwbvuvzx0GIw
source: Doonsec's feed
date: 2026-03-30
fetch_date: 2026-03-31T04:34:55.763712
---

# OpenClaw全自动刷CVE编号

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/yOiat0BJcib5iblwp16QIdXicbDnrNccRjgnLhsYDxUGBOqrwoiaayp0DB3mVX9r3iavK0pbUu5RgwLP93TQzANGxP7BPeb6DzAGep00APPuPribwM/0?wx_fmt=jpeg)

# OpenClaw全自动刷CVE编号

原创

M9
M9

白昼信安

![]()

在小说阅读器中沉浸阅读

> 微信公众号：白昼信安

最近终于稍闲一点，利用周末的时间将OpenClaw的多agent协作研究了一下，搭建了一个多agent代码审计及自动提交cve的集群。

我的团队简单拓扑图如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/yOiat0BJcib58KjE5kh1MiaQjG3VX3DibEmB954LChJ3c5VtQXeImEPLt5JXaDVerhMVd573wAEhybqPtWOzlcnJkGP5DtiaVOT5BGStUhG67MbQ/640?wx_fmt=png&from=appmsg)

CTO安装的skills：

```
Self-Improving 学习纠错、经验积累、教训记录 Proactivity    主动行动、上下文恢复、任务跟进 Reason         结构化推理、决策分析
```

代码审计工程师安装的skills：

```
PHP-Code-Audit-Skilljava-audit-skills-0.2.0
项目地址：https://github.com/0xShe/PHP-Code-Audit-Skillhttps://github.com/RuoJi6/java-audit-skills
```

漏洞复现工程师无额外skills

```
安全策略：要求他在复现漏洞时将项目全部放到docker中进行本地场景搭建，写入soul.md文件中。
```

效果图：

当前团队成员：

![](https://mmbiz.qpic.cn/mmbiz_png/yOiat0BJcib5iccELU2kfYCUUPGM0GX174ThzcmeuJVQic9lBl4ibHa1QOVpUs3PtSBxF6xvLicmibtUmTcrLicLPkx1AOvo9THuymxVdKI3tibY568c/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/yOiat0BJcib59z5gObHLbEKddvdXGXZ4ZeC7jiceWv5tYXKvnrvhia1oNnmVLZPVEX1TuCovyQGXep82mULIxtbzavvhXTuIibg7xEIRo5CvicsR4/640?wx_fmt=png&from=appmsg)

审计出的漏洞列表：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/yOiat0BJcib5ibFLaJZM07SBTPKVqoU53DSnxxqJcRib8FP9LspmFFFm097mHVNxL36dnGLAAMJCyrjczIibBoZ2yNdCjoupS5n0GeD1RT4OC6yc/640?wx_fmt=png&from=appmsg)

漏洞复现反馈：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/yOiat0BJcib5icCicyQT0ibLA5f6vo1ZnaibltcOf71nVHMbGS5BZlT7wbFZib2o9hJPewtFiaWaFsTDPtlWlMErTiaf4qb5TDK0V0oleNqhwdCDB0h4/640?wx_fmt=png&from=appmsg)

自动化CVE提交：

![](https://mmbiz.qpic.cn/mmbiz_png/yOiat0BJcib5ibd1W0I0CHSuDRPsZ6ibicCW975OEic3rw2CMAL1VHawcxh6ibuSyDeuia3va6oQwYt0PkLVjbmTibxh1rMicic5MzkpiasaCUq1eibiagiaBQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/yOiat0BJcib58Nacu498yYcDKQ99D7vf4pMUUnT9KiaeJ0cdiaSn2mpyLS2uF16IWSf44GNZS5zoU0Ch03PXuBq8RHbqzw7fCRXUUiapZZnuTrFs/640?wx_fmt=png&from=appmsg)

这样就完成了从审计到复现，再到漏洞提交的全流程。

整体流程：

CTO 是怎么「指挥」的？

CTO 不写代码、不审计代码、不发 HTTP 包。他的唯一工作是：**拆任务、派活、盯进度、收结果。**整个流水线从「搜索 GitHub 项目」开始：

**① 搜索目标**

> CTO 指挥代码审计工程师：「去 GitHub 搜索 PHP 项目，取50-100的星的项目，拉取前30个源码到工作区。」

**② 拆解任务**

> CTO内部思考：30 个项目拆成 6 批，每批5个并行审计。生成任务文档：目标、步骤、风险等级标准。

**③ 并行派发**

> CTO 通过消息系统批量派给代码审计工程师：「审计以下 5 个项目，只关注严重/高危/中危，完成后返回报告。」

**④ 自动跟踪**

> CTO：每 30 秒检查一次进度。没完成？继续等。完成了？接收结果，立即派下一批。

**⑤ 搭环境 + 复现**

> 代码审计工程师发现的高危漏洞，CTO 转给漏洞复现工程师：「用 Docker 搭建项目环境，并根据审计报告逐个发包验证，复现报告附curl命令和响应截图。

**⑥ 汇总交付漏洞提交**

> 所有结果整合成结构化报告：漏洞表格、TOP 5 高危项目、需要提交 CVE 的清单，然后根据你的指令进行指定漏洞的cve提交。

我使用的模型是MiMo-V2-Pro，目前还可以免费使用到4月2日，训龙虾的整个过程确实是相当于在一个白纸上作画的感觉，不断调试和完善过程，欢迎各位师傅一起讨论！！

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/XvSe1EahHxV1aarZt3GySkHa2Jkl3D3ic6RGia1yI5ePCVZbOQGBlwbibS0K20rfFSsxTeD6b1GLz3ibhLkibE05ibbw/0?wx_fmt=png)

白昼信安

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/XvSe1EahHxV1aarZt3GySkHa2Jkl3D3ic6RGia1yI5ePCVZbOQGBlwbibS0K20rfFSsxTeD6b1GLz3ibhLkibE05ibbw/0?wx_fmt=png)

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