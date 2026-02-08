---
title: 不能不知道的OA综合利用工具
url: https://mp.weixin.qq.com/s/r4cSoO2BXFDzqktuIOGJKw
source: Doonsec's feed
date: 2026-02-07
fetch_date: 2026-02-08T04:28:01.265605
---

# 不能不知道的OA综合利用工具

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zDP7QPgHQjR3USRj31sLFlTwx00m6rvdibkoF1EVuouicmAMGXM6G728iaiaUEfgYkic0jDIpnIVibeRET9kJiceqFLZTMeoeAH2cujQY4RgTp6q2c/0?wx_fmt=jpeg)

# 不能不知道的OA综合利用工具

Enginge
Enginge

Enginge

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/SEdvtYR5JaYI00RAa1ZTy35yKKkZEN7ElLsNgz8ts6yTA4cMcHfnGFJotpTGKt04nQBy5H1nAkTOUzZ0AqpdKg/640?wx_fmt=jpeg)

幸福不是拥有一切，而是想要的恰好都在身边。——

Exp-Tools-1.3.1-encrypted该工具使用了ExpDemo-JavaFX项目，保留了核心的数据包请求接口，使用jdk1.8环境开发。目前编写了oa、设备、框架、产品等多个系列，对相关漏洞进行复现和分析，极力避免exp的误报和有效性。

截止到目前为止，已实现了用友、泛微、蓝凌、万户、帆软报表、致远、通达、红帆、金和、金蝶、广联达、华天动力总共12个OA。 全部是命令执行、文件上传类的漏洞，包括前台和后台。

![](https://mmbiz.qpic.cn/mmbiz_png/zDP7QPgHQjTW6edlGmfbWHg6XolkIgtuBrnsFNTwxADDS7qoibzfO0XZVOpibfgfvPsxou6Us332VYdjmYuhE5pjCe0lmuC3iaJmd0ANsTIwfk/640?wx_fmt=png&from=appmsg)

用友部分：

```
用友NC-BshServlet 远程命令执行用友NC-BshServlet-bypass 远程命令执行用友NC accept 文件上传用友NC uapim 文件上传用友NC mp 文件上传用友NC saveXmlToFileServlet 文件上传用友NC FileManager 文件上传用友NC saveImageServlet 文件上传用友NC反序列化-1用友NC反序列化-2用友NC反序列化-3用友NC Cloud 文件写入用友NC Cloud uploadChunk文件上传用友NC Cloud importhttpscer文件上传用友U8CRM swfupload 文件上传用友U8CRM getemaildata 文件上传用友U8CRM crmtools 文件上传用友GRP-U8 UploadFileData 文件上传用友GRP-U8 U8AppProxy 文件上传用友GRP-U8 services 文件写入用友GRP-U8 servlet 文件上传用友U8C 文件上传用友U8C 反序列化-1用友U8C 反序列化-2用友U8C esnserver文件写入用友U9 PatchFile 文件写入用友畅捷通T+密码重置用友畅捷通T+文件上传-1用友畅捷通T+文件上传-2用友畅捷通T+GetStoreWarehouseByStore反序列化用友KSOA ImageUpload 文件上传用友KSOA Attachment 文件写入用友移动管理平台Apk文件上传用友移动管理平台Icon文件上传用友U8-OA文件上传用友UFIDA NC 文件写入
```

泛微部分:

```
泛微eoffice OfficeServer 文件上传泛微eoffice UploadFile 文件上传泛微eoffice uploadify 文件上传泛微eoffice ajax 文件上传泛微BshServlet 远程命令执行泛微ecology前台sql注入-1泛微ecology前台sql注入-2泛微ecology前台sql注入-3泛微ecology任意用户爆破泛微ecology任意用户登录-1泛微ecology任意用户登录-2泛微ecology FileClient 文件上传泛微ecology WorkflowServiceXml命令执行泛微ecology KtreeUploadAction 文件上传泛微ecology uploaderOperate 文件上传泛微ecology weaver.common.Ctrl 文件上传泛微ecology后台风格文件上传泛微ecology后台流程命令执行泛微ecology后台库存文件上传泛微emobile client命令执行泛微emobile messageType命令执行泛微emobile lang2sql文件覆盖
```

蓝凌部分:

```
蓝凌OA 任意用户登录蓝凌OA SSRF蓝凌OA SSRF BeanShell 文件上传蓝凌OA SSRF XmlDecoder 文件上传蓝凌OA treexml 命令执行蓝凌OA界面文件上传蓝凌OA主题文件上传蓝凌OA jg_service文件上传蓝凌OA sysUiComponent文件复制蓝凌OA后台模板文件上传蓝凌EIS api文件上传
```

万户部分:

```
万户OA用户密码泄露万户OA fileUpload 文件上传万户OA officeserverservlet 文件上传万户OA smartUpload 文件上传万户OA OfficeServer 文件上传万户OA senddocument 文件导入万户OA wpsservlet 文件上传万户OA SOAP 文件写入万户OA SOAP创建文件写入
```

帆软报表部分:

```
帆软报表任意文件读取帆软报表任意文件读取-bypass帆软报表任意文件覆盖帆软报表未授权命令执行-1帆软报表未授权命令执行-2帆软报表未授权命令执行-3帆软报表channel命令执行-1帆软报表channel命令执行-2帆软报表ReportServer sql注入帆软报表后台插件文件上传帆软报表后台主题文件上传
```

致远部分:

```
致远session泄露processUpload文件上传致远uploadMenuIcon文件上传致远ajax文件上传致远ajax文件上传-bypass致远wpsAssistServlet文件上传致远htmlofficeservlet文件上传致远任意用户密码重置致远audit-admin用户默认密码致远audit-admin用户重置密码致远后台模板文件上传致远后台模板管理器文件上传致远后台表格文件写入致远后台ofd文件解压致远后台jdbc文件写入致远后台constDef代码执行致远帆软报表文件读取致远帆软报表文件读取-bypass致远帆软报表日志命令执行致远帆软报表后台插件文件上传致远帆软报表后台主题文件上传致远M1命令执行
```

通达部分:

```
通达任意用户登录-1通达任意用户登录-2通达任意用户登录-3通达任意用户登录-4通达Ispirit文件上传通达ueditor文件上传通达gateway反序列化通达后台附件文件上传
```

红帆部分:

```
红帆OA任意文件上传红帆OA任意文件写入
```

金和部分:

```
金和OA命令执行金和OA editeprint文件写入金和OA EditMain文件写入金和OA saveAsOtherFormatServlet文件上传金和OA OfficeServer文件上传金和OA UploadFileBlock文件上传金和OA servlet 文件上传金和OA jcsUploadServlet文件上传金和OA UploadFileEditorSave文件上传金和OA viewConTemplate 模板注入
```

金蝶已完成:

```
金蝶云星空反序列化-1金蝶云星空反序列化-2金蝶云星空反序列化-3金蝶云星空文件上传金蝶EAS file文件上传金蝶EAS logo文件上传金蝶Apusic 文件上传
```

广联达部分:

```
广联达OA GetIMDictionary sql注入广联达OA 任意用户登录广联达OA 用户文件上传广联达OA 后台文件上传
```

华天动力部分:

```
华天动力OA 登录绕过华天动力OA ntkoupload 文件上传华天动力OA Servlet文件上传
```

## `可回复"260207"获取工具链接`

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/SEdvtYR5JabmH4p5zqINv9hK3mIfaDs0YRicvRQAMFtXk6ZwibGBEzyhm0DWkOvbXSa044LTVoFI7jfqOibSSmWMg/0?wx_fmt=png)

Enginge

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/SEdvtYR5JabmH4p5zqINv9hK3mIfaDs0YRicvRQAMFtXk6ZwibGBEzyhm0DWkOvbXSa044LTVoFI7jfqOibSSmWMg/0?wx_fmt=png)

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