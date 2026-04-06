---
title: 【工具推荐】高危漏洞EXP实用性工具
url: https://mp.weixin.qq.com/s/OugrJ7T7ue53MMdsU4angQ
source: Doonsec's feed
date: 2026-04-05
fetch_date: 2026-04-06T04:43:11.160583
---

# 【工具推荐】高危漏洞EXP实用性工具

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/DJX1rNqJe4k2ibJVJ8RejxynWIVGe3l4AF6aN5B4KMXY2EnS5Z2zicjKc26ibtHq6JmdwX0viaJ0sDC9ptTAZ6zI5U1hwdulQe16TmoDBdCBoUQ/0?wx_fmt=jpeg)

# 【工具推荐】高危漏洞EXP实用性工具

隐雾安全

![]()

在小说阅读器中沉浸阅读

***隐雾安全***

**致力于为大家提供最实用的安全技能**

**项目介绍**

该工具使用了ExpDemo-JavaFX项目，保留了核心的数据包请求接口，使用jdk1.8环境开发。目前编写了oa、设备、框架、产品等多个系列，对相关漏洞进行复现和分析，极力避免exp的误报和有效性。

截止到目前为止，已实现了用友、泛微、蓝凌、万户、帆软报表、致远、通达、红帆、金和、金蝶、广联达、华天动力总共12个OA。 全部是命令执行、文件上传类的漏洞，包括前台和后台。

**检测支持**

用友检测列表：

* 用友NC-BshServlet 远程命令执行
* 用友NC-BshServlet-bypass 远程命令执行
* 用友NC accept 文件上传
* 用友NC uapim 文件上传
* 用友NC mp 文件上传
* 用友NC saveXmlToFileServlet 文件上传
* 用友NC FileManager 文件上传
* 用友NC saveImageServlet 文件上传
* 用友NC反序列化-1
* 用友NC反序列化-2
* 用友NC反序列化-3
* 用友NC Cloud 文件写入
* 用友NC Cloud uploadChunk文件上传
* 用友NC Cloud importhttpscer文件上传
* 用友U8CRM swfupload 文件上传
* 用友U8CRM getemaildata 文件上传
* 用友U8CRM crmtools 文件上传
* 用友GRP-U8 UploadFileData 文件上传
* 用友GRP-U8 U8AppProxy 文件上传
* 用友GRP-U8 services 文件写入
* 用友GRP-U8 servlet 文件上传
* 用友U8C 文件上传
* 用友U8C 反序列化-1
* 用友U8C 反序列化-2
* 用友U8C esnserver文件写入
* 用友U9 PatchFile 文件写入
* 用友畅捷通T+密码重置
* 用友畅捷通T+文件上传-1
* 用友畅捷通T+文件上传-2
* 用友畅捷通T+GetStoreWarehouseByStore反序列化
* 用友KSOA ImageUpload 文件上传
* 用友KSOA Attachment 文件写入
* 用友移动管理平台Apk文件上传
* 用友移动管理平台Icon文件上传
* 用友U8-OA文件上传
* 用友UFIDA NC 文件写入

泛微检测列表:

* 泛微eoffice OfficeServer 文件上传
* 泛微eoffice UploadFile 文件上传
* 泛微eoffice uploadify 文件上传
* 泛微eoffice ajax 文件上传
* 泛微BshServlet 远程命令执行
* 泛微ecology前台sql注入-1
* 泛微ecology前台sql注入-2
* 泛微ecology前台sql注入-3
* 泛微ecology任意用户爆破
* 泛微ecology任意用户登录-1
* 泛微ecology任意用户登录-2
* 泛微ecology FileClient 文件上传
* 泛微ecology WorkflowServiceXml命令执行
* 泛微ecology KtreeUploadAction 文件上传
* 泛微ecology uploaderOperate 文件上传
* 泛微ecology weaver.common.Ctrl 文件上传
* 泛微ecology后台风格文件上传
* 泛微ecology后台流程命令执行
* 泛微ecology后台库存文件上传
* 泛微emobile client命令执行
* 泛微emobile messageType命令执行
* 泛微emobile lang2sql文件覆盖

蓝凌检测列表:

* 蓝凌OA 任意用户登录
* 蓝凌OA SSRF
* 蓝凌OA SSRF BeanShell 文件上传
* 蓝凌OA SSRF XmlDecoder 文件上传
* 蓝凌OA treexml 命令执行
* 蓝凌OA界面文件上传
* 蓝凌OA主题文件上传
* 蓝凌OA jg\_service文件上传
* 蓝凌OA sysUiComponent文件复制
* 蓝凌OA后台模板文件上传
* 蓝凌EIS api文件上传

万户检测列表：

* 万户OA用户密码泄露
* 万户OA fileUpload 文件上传
* 万户OA officeserverservlet 文件上传
* 万户OA smartUpload 文件上传
* 万户OA OfficeServer 文件上传
* 万户OA senddocument 文件导入
* 万户OA wpsservlet 文件上传
* 万户OA SOAP 文件写入
* 万户OA SOAP创建文件写入

帆软报表检测列表:

* 帆软报表任意文件读取
* 帆软报表任意文件读取-bypass
* 帆软报表任意文件覆盖
* 帆软报表未授权命令执行-1
* 帆软报表未授权命令执行-2
* 帆软报表未授权命令执行-3
* 帆软报表channel命令执行-1
* 帆软报表channel命令执行-2
* 帆软报表ReportServer sql注入
* 帆软报表后台插件文件上传
* 帆软报表后台主题文件上传

致远检测列表:

* 致远session泄露processUpload文件上传
* 致远uploadMenuIcon文件上传
* 致远ajax文件上传
* 致远ajax文件上传-bypass
* 致远wpsAssistServlet文件上传
* 致远htmlofficeservlet文件上传
* 致远任意用户密码重置
* 致远audit-admin用户默认密码
* 致远audit-admin用户重置密码
* 致远后台模板文件上传
* 致远后台模板管理器文件上传
* 致远后台表格文件写入
* 致远后台ofd文件解压
* 致远后台jdbc文件写入
* 致远后台constDef代码执行
* 致远帆软报表文件读取
* 致远帆软报表文件读取-bypass
* 致远帆软报表日志命令执行
* 致远帆软报表后台插件文件上传
* 致远帆软报表后台主题文件上传
* 致远M1命令执行

通达检测列表：

* 通达任意用户登录-1
* 通达任意用户登录-2
* 通达任意用户登录-3
* 通达任意用户登录-4
* 通达Ispirit文件上传
* 通达ueditor文件上传
* 通达gateway反序列化
* 通达后台附件文件上传

红帆检测列表：

* 红帆OA任意文件上传
* 红帆OA任意文件写入

金和检测列表：

* 金和OA命令执行
* 金和OA editeprint文件写入
* 金和OA EditMain文件写入
* 金和OA saveAsOtherFormatServlet文件上传
* 金和OA OfficeServer文件上传
* 金和OA UploadFileBlock文件上传
* 金和OA servlet 文件上传
* 金和OA jcsUploadServlet文件上传
* 金和OA UploadFileEditorSave文件上传
* 金和OA viewConTemplate 模板注入

金蝶检测列表：

* 金蝶云星空反序列化-1
* 金蝶云星空反序列化-2
* 金蝶云星空反序列化-3
* 金蝶云星空文件上传
* 金蝶EAS file文件上传
* 金蝶EAS logo文件上传
* 金蝶Apusic 文件上传

广联达检测列表：

* 广联达OA GetIMDictionary sql注入
* 广联达OA 任意用户登录
* 广联达OA 用户文件上传
* 广联达OA 后台文件上传

华天动力检测列表：

* 华天动力OA 登录绕过
* 华天动力OA ntkoupload 文件上传
* 华天动力OA Servlet文件上传

**工具使用**

***直接下载releases版本即可***

使用JDK8启动，命令如下：

```
java -javaagent:Exp-Tools-1.3.1-encrypted.jar -jar Exp-Tools-1.3.1-encrypted.jar
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DJX1rNqJe4lJRLoBQULRxUIq9zgF053QeI1fmFVJ8WheCplOBHmr2NophWWGJL2bOiaqwiaibAXvwKibfSo0SqNKgiavklsklJz7X1q3rtvNHoKg/640?wx_fmt=png&from=appmsg)

**下载链接**

https://github.com/cseroad/Exp-Tools/

**网安交流群**

![](https://mmbiz.qpic.cn/mmbiz_jpg/DJX1rNqJe4lsLy3BopL2cXtF42S1xQhw3d6ialaw2KMBnnOZmX9ibHAyC4GvWIvGRggrQea113WmO3ntQuYNn6qnmsG4licsaREUFVWUFrkyow/640?wx_fmt=jpeg&from=appmsg)

**微信号**丨Hiddenfog001

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ELQKhUzr34xNiazXVTT6qEbEU7UjrgFplQqq3mt9dTpB7qCTQSsP9FMqic1ub553HR5NPeVcHnI7QSwde7madgCQ/0?wx_fmt=png)

隐雾安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ELQKhUzr34xNiazXVTT6qEbEU7UjrgFplQqq3mt9dTpB7qCTQSsP9FMqic1ub553HR5NPeVcHnI7QSwde7madgCQ/0?wx_fmt=png)

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