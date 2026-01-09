---
title: Apt_t00ls：Java 开发的OA设备高危漏洞集成利用工具
url: https://mp.weixin.qq.com/s/It_8VnOhiNNAYzesd46gdw
source: Doonsec's feed
date: 2026-01-08
fetch_date: 2026-01-09T03:27:14.668618
---

# Apt_t00ls：Java 开发的OA设备高危漏洞集成利用工具

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3ibCZqSDX9ujwEpJ8e5eiapzo5oEkMWTQmxpKVCHQdicZFedIGwomczFwDJic6OMgth0b8BIQ1BX7oMZwcppU5tYag/0?wx_fmt=jpeg)

# Apt\_t00ls：Java 开发的OA设备高危漏洞集成利用工具

原创

网安武器库

网安武器库

![]()

在小说阅读器中沉浸阅读

**更多干货  点击蓝字 关注我们**

**注：本文仅供学习，坚决反对一切危害网络安全的行为。造成法律后果自行负责！**

**往期回顾**

·[Hashcat密码工具：快速识别百种哈希密码类型+GPU加速密码爆破](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247485727&idx=1&sn=da20b5443572fb7e1550eb1e42b28dbc&scene=21#wechat_redirect)

·[Nikto：一款Web安全漏洞扫描器](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247485724&idx=1&sn=8daf51f5fb3946907463096de6309731&scene=21#wechat_redirect)

·[HTTrack爬虫：网站递归式资源抓取工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247485715&idx=1&sn=819198a15960118702253dffd868f127&scene=21#wechat_redirect)

·["手机版的kali"黑客工具：Tool-X使用和安装指南](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247485663&idx=1&sn=95cbaadb12dcf74077ec6e0bf8448c11&scene=21#wechat_redirect)

·[pentmenu:黑客必备实战流量攻击工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247485644&idx=1&sn=ef9b011a20e30cea78592357736ca177&scene=21#wechat_redirect)

·[CTF-FlaskSession的cookie密码快速爆破工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247485611&idx=1&sn=ad4273b85b9685bb4c94beb2fb350701&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

介绍

Apt\_t00ls 是一个基于 Java 开发的高危漏洞利用工具，专注于企业安全测试和漏洞检测。该项目由 Gec、I0veD 和 luckyh 等安全研究人员共同开发，旨在为合法授权的企业安全建设提供技术支持。

项目地址：

```
https://github.com/White-hua/Apt_t00ls?tab=readme-ov-file
```

核心功能

漏洞利用模块

项目包含多个分类的漏洞利用模块，覆盖了常见的企业系统和设备：

1. 办公系统（OA）漏洞 ：

```
 - 泛微 e-cology/e-office 系列漏洞（如文件上传 RCE、BshServlet RCE 等） - 蓝凌 OA 漏洞（如 datajson RCE、sysSearchMain RCE 等） - 用友系列漏洞（如畅捷通 T+ RCE、NC 反序列化 RCE 等） - 万户 OA 漏洞（如 OfficeServer RCE、DocumentEdit SQLi 等） - 致远 OA 漏洞（如 log4j2 RCE、wpsAssistServlet RCE 等） - 通达 OA 漏洞（如 getdata RCE、apiali RCE 等） - 帆软漏洞（如 save_svg RCE 等）
```

2. 设备漏洞 ：

```
   - 深信服（Sangfor）设备漏洞   - H3C 设备漏洞   - 海康威视（hikvision）设备漏洞   - 启明星辰（qianxin）设备漏洞   - 网御星云（wangyu）设备漏洞
```

3. 中间件漏洞 ：

```
   - IIS PUT 漏洞
```

4. CMS 漏洞 ：

```
 - Nacos 创建用户漏洞
```

工具模块

项目还集成了多个实用工具模块：

```
1. 文件上传指令生成 ：用于生成各种文件上传漏洞的利用 payload2. Tasklist 敏感进程检测 ：用于检测目标系统中的敏感进程3. 反弹 shell 命令生成 ：用于生成各种环境下的反弹 shell 命令
```

技术架构

```
 - 开发语言 ：Java 8 - GUI 框架 ：JavaFX - 构建工具 ：Maven
```

核心依赖 ：

```
  - hutool-all：Java 工具库  - jfoenix：JavaFX 界面组件库  - junit-jupiter-api：单元测试框架
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

使用

运行环境要求

```
 - Java JDK 8 或更高版本 - Maven 3.6.0 或更高版本（用于构建项目） - 支持 JavaFX 的操作系统（Windows、Linux、macOS）
```

如何使用：

检查环境：

```
java -versionmvn -version
```

在确保java和maven部署好后

```
cd ..\path\to\Apt_t00ls-master
```

(网络问题别忘了配镜像)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ujwEpJ8e5eiapzo5oEkMWTQmUIAKjgibogeQibwUBjzy4vibo5aK0rMUPb4qPmRfR1LzmrIj2mGPuR9PQ/640?wx_fmt=png&from=appmsg)

```
mvn compile
```

Maven编译成功，现在使用

```
mvn package
```

构建可执行的JAR文件。

之后就可以打开了

```
java -jar ..\path\to\target\apt_tools-jar-with-dependencies.jar
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ujwEpJ8e5eiapzo5oEkMWTQmq7Nw6apAL8Wsic16RpuB3F9cWg0hzAmUHAKUsKNtGffvicUSHbN8HYbQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

功能

泛微:

```
e-cology workrelate_uploadOperation.jsp-RCE (默认写入冰蝎4.0.3aes)e-cology page_uploadOperation.jsp-RCE (暂未找到案例 仅供检测poc)e-cology BshServlet-RCE (可直接执行系统命令)e-cology KtreeUploadAction-RCE (默认写入冰蝎4.0.3aes)e-cology WorkflowServiceXml-RCE (默认写入内存马 冰蝎 3.0 beta11)e-office logo_UploadFile.php-RCE (默认写入冰蝎4.0.3aes)e-office10 OfficeServer.php-RCE (默认写入冰蝎4.0.3aes)e-office8 fileupload-RCE (默认写入冰蝎4.0.3aes)e-office doexecl.php-RCE (写入phpinfo,需要getshell请自行利用)e-mobile_6.0 sqlli-RCE (可直接执行系统命令)e-mobile_6.6 messageType.do-SQlli (sqlmap利用，暂无直接shell的exp)
```

蓝凌：

```
landray_datajson-RCE (可直接执行系统命令)landray_treexmlTmpl-RCE (可直接执行系统命令)landray_sysSearchMain-RCE (多个payload，写入哥斯拉 3.03 密码 yes)landrayoa_fileupload_sysSearch-RCE (默认写入冰蝎4.0.3aes)
```

用友:

```
yongyou_chajet_RCE (用友畅捷通T+ rce 默认写入哥斯拉 Cshap/Cshap_aes_base64)yongyou_chajet_反序列化RCE(可直接执行系统命令)yongyou_NC_FileReceiveServlet-RCE 反序列化rce (默认写入冰蝎4.0.3aes)yongyou_NC_bsh.servlet.BshServlet_RCE (可直接执行系统命令)yongyou_NC_jsInovke任意文件上传 (默认写入冰蝎4.0.3aes)yongyou_NC_NCFindWeb 目录遍历漏洞 (可查看是否存在历史遗留webshell)yongyou_GRP_UploadFileData-RCE(默认写入冰蝎4.0.3aes)yongyou_GRP_AppProxy-RCE(默认写入冰蝎4.0.3aes)yongyou_KSOA_imageUpload-RCE (默认写入冰蝎4.0.3aes)yongyou_KSOA_Attachmentupload-RCE (默认写入冰蝎4.0.3aes)
```

万户：

```
wanhuoa_OfficeServer-RCE(默认写入冰蝎4.0.3aes)wanhuoa_OfficeServer-RCE(默认写入哥斯拉4.0.1 jsp aes 默认密码密钥)wanhuoa_DocumentEdit-SQlli(mssql数据库 可 os-shell)wanhuoa_OfficeServerservlet-RCE(默认写入冰蝎4.0.3aes)wanhuoa_fileUploadController-RCE(默认写入冰蝎4.0.3aes)
```

致远：

```
seeyonoa_main_log4j2-RCE (仅支持检测，自行开启ladp服务利用)seeyonoa_wpsAssistServlet-RCE(默认写入冰蝎4.0.3aes)seeyonoa_htmlofficeservlet-RCE(默认写入冰蝎4.0.3aes)seeyonreport_svg_upload-RCE(默认写入冰蝎4.0.3aes)seeyonoa_ajaxBypass-RCE(写入天蝎 密码sky)seeyon_testsqli-RCE(仅检测是否存在漏洞页面)
```

通达:

```
tongdaoa_getdata-RCE (直接执行系统命令)tongdaoa_apiali-RCE (默认写入冰蝎4.0.3aes)
```

帆软：

```
fanruan_save_svg-RCE (默认写入冰蝎4.0.3aes)
```

中间件:

```
IIS_PUT_RCE (emm暂时没办法getshell  仅支持检测 java没有MOVE方法)
```

安全设备:

```
综合安防_applyCT_fastjson-RCE(仅支持检测,自行使用ladp服务利用)综合安防_api_file任意文件上传 (默认写入冰蝎4.0.3aes)综合安防_external_report任意文件上传 (默认写入冰蝎4.0.3aes)网康下一代防火墙_ngfw_waf_route-RCE(写入菜刀shell 密码:nishizhu)H3C cas_cvm_upload-RCE  (默认写入冰蝎4.0.3aes)大华智慧园区任意文件上传  (默认写入冰蝎4.0.3aes)深信服应用交付管理系统命令执行网御星云账号密码泄露 阿里nacos未授权任意用户添加
```

使用截图：
![QQ截图20221014202028](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ujwEpJ8e5eiapzo5oEkMWTQmsQfUlLTnZaE8qLk1n2jicIGwgl81qicE9MDPLiclvYSuiaFZgckv5ciaAsQ/640?wx_fmt=png&from=appmsg)

![QQ截图20221014202151](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ujwEpJ8e5eiapzo5oEkMWTQmJMpto29mMc3qKVUeGbtDa3m2yJGJdv90DhUXHicStAibxKsS0ot0LkKw/640?wx_fmt=png&from=appmsg)
![3](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ujwEpJ8e5eiapzo5oEkMWTQmp1ZgGia6QsdhBA7N03iahRLNoBHboRpUsfOm5vLpySxmicqBMYclU3gIA/640?wx_fmt=png&from=appmsg)

---

##

## 工具模块:

文件上传指令生成
![upload](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ujwEpJ8e5eiapzo5oEkMWTQmxkwAmc5IIE583woicOGxqNaiaQ5qsQvlpib0yG2TYQV3Bjjs6gvPzXiaZw/640?wx_fmt=png&from=appmsg)

Tasklist敏感进程检测
![tasklist](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ujwEpJ8e5eiapzo5oEkMWTQmuqt1suhnic4lnVicUyfEneL5vrLTx8oISrX4HPhB6d1dhxUic0tMSgJyw/640?wx_fmt=png&from=appmsg)

反弹shell命令生成
![shell](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ujwEpJ8e5eiapzo5oEkMWTQmAicaticmVWec0XV6n81BkxP9AYa4U5ibXnY41m5nVGgS22Tta6bZxIyvw/640?wx_fmt=png&from=appmsg)

---

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eRUtCzBCFbaMYy1c7utlweibCFXWsicmm9ebyvInBtdsD0QRlUDTdLib1g/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ujZsao69o9To7R2EPMICOxibwVeWgBhbMqg4icbbohwQibUQoRcx6ymIwZylKcXjdYCZWgQcibhibzqTyA/0?wx_fmt=png)

网安武器库

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ujZsao69o9To7R2EPMICOxibwVeWgBhbMqg4icbbohwQibUQoRcx6ymIwZylKcXjdYCZWgQcibhibzqTyA/0?wx_fmt=png)

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