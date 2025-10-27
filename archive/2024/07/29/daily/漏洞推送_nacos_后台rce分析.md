---
title: nacos_后台rce分析
url: https://mp.weixin.qq.com/s?__biz=MzU5MTExMjYwMA==&mid=2247485685&idx=1&sn=41fef7adb41d79dee22e702880262df9&chksm=fe32b802c9453114e50aca694082d9ad00ddf538fa9b77ab62a283f0bd841a67c545698c749a&scene=58&subscene=0#rd
source: 漏洞推送
date: 2024-07-29
fetch_date: 2025-10-06T17:41:19.412768
---

# nacos_后台rce分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/noZJ3Kqbu1cicoZicmxMRT2JxpMVuJ88bOZKVE3bu2aSZXd0cmzzIQJ9BnReNoNic5fTfoLz2HQx4cwmDKDV7a9kQ/0?wx_fmt=jpeg)

# nacos\_后台rce分析

原创

kkk mr

漏洞推送

## 环境搭建

适用 vulhub这个项目来启动漏洞环境

vulhub的nacos版本是 1.4.0，通过github下载源代码

> https://github.com/alibaba/nacos/tree/1.4.0

因为vulhub已经默认开放了debug端口，所以直接自己idea jvm远程调试即可

## 漏洞分析

从 poc来看 问题出在 `/nacos/v1/cs/ops/data/removal` 和 `/nacos/v1/cs/ops/derby` 这两个接口

removal 代码位于 `config/src/main/java/com/alibaba/nacos/config/server/controller/ConfigOpsController.java:133`

importDerby方法使用了`Secured`注解进行保护

Secured注解的实现在 `com/alibaba/nacos/core/auth/AuthFilter.java:88`

首先判断了有没有开启认证，如果没有开启就直接pass

如果开启了认证 还会判断 ua是否是 Nacos-Server开头，如果是的话就pass。这就是前几年的未授权漏洞的根源

在vuln 中的nacos是没有开启auth的，所以无需关注认证

![](https://mmbiz.qpic.cn/sz_mmbiz_png/noZJ3Kqbu1cicoZicmxMRT2JxpMVuJ88bOWUAIcY4tmrTACHZnTmwYXicaUF27c5l55txfekeYtsWu8nytOsEBAnQ/640?wx_fmt=png&from=appmsg "null")

漏洞接口代码

```
    @PostMapping(value = "/data/removal")    @Secured(action = ActionTypes.WRITE, resource = "nacos/admin")    public DeferredResult<RestResult<String>> importDerby(@RequestParam(value = "file") MultipartFile multipartFile) {        DeferredResult<RestResult<String>> response = new DeferredResult<>();        if (!PropertyUtil.isEmbeddedStorage()) {            response.setResult(RestResultUtils.failed("Limited to embedded storage mode"));            return response;        }        DatabaseOperate databaseOperate = ApplicationUtils.getBean(DatabaseOperate.class);        WebUtils.onFileUpload(multipartFile, file -> {            NotifyCenter.publishEvent(new DerbyImportEvent(false));            databaseOperate.dataImport(file).whenComplete((result, ex) -> {                NotifyCenter.publishEvent(new DerbyImportEvent(true));                if (Objects.nonNull(ex)) {                    response.setResult(RestResultUtils.failed(ex.getMessage()));                    return;                }                response.setResult(result);            });        }, response);        return response;    }
```

接受一个文件，临时储存在/tmp目录下，

然后调用`databaseOperate.dataImport`方法进行导入，然后继续调用父类的doDataImport方法进行导入

![](https://mmbiz.qpic.cn/sz_mmbiz_png/noZJ3Kqbu1cicoZicmxMRT2JxpMVuJ88bOlUpMwkf6C9ZottddaSBicWw3cu5HA0HNL8b3hsc6icSUibgSq20gskZWQ/640?wx_fmt=png&from=appmsg "null")

继续调用，在batchUpdate执行了sql语句

![](https://mmbiz.qpic.cn/sz_mmbiz_png/noZJ3Kqbu1cicoZicmxMRT2JxpMVuJ88bOGugLjtXDBsxSYr4NEtfdT8D555ziaLc9R8vwB4LIPU8SMIChIUb5W8g/640?wx_fmt=png&from=appmsg "null")

这里调用的是spring中的template库来执行sql语句，template中的jdbcurl是

`jdbc:derby:/opt/nacos/data/derby-data;create=true`

derby 是一个开源的关系型数据库，是嵌入式数据库。于java中H2类似

相关参考文档:

> https://db.apache.org/derby/docs/10.17/devguide/rdevdeploy856845.html
>
> https://db.apache.org/derby/docs/10.17/devguide/cdevdeploy21645.html

可以通过远程安装一个java包，将一个或多个 jar 文件添加到数据库后，必须通过在 derby.database.classpath 属性中包含一个或多个 jar 文件来设置数据库 jar 类路径，以使 Derby 能够从 jar 文件加载类。

然后创建一个自定义函数，这个select 这个自定义函数来触发命令执行

`select * from (select count(*) as b, S_EXAMPLE_{id}('{command}') as a from config_info) tmp /*ROWS FETCH NEXT*/`

这个时候就产生了一个问题，为什么通过`/nacos/v1/cs/ops/data/removal` 已经能执行sql语句了，为什么还要用`/nacos/v1/cs/ops/derby`这个接口来执行select语句。

因为这里执行语句的是`template.batchUpdate`函数，只能执行update相关语句无法执行select语句。

derby接口执行语句是用的`template.queryForList`所以可以执行select语句

## 修复措施

看官方的最新的代码，应该是默认禁用derby数据库了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/noZJ3Kqbu1cicoZicmxMRT2JxpMVuJ88bOAeFYDCvseBHd83FVHzMiaEXmrmp7Vwrp7vZjzq4aW0icIwuKoianBEgUQ/640?wx_fmt=png&from=appmsg "null")

通过docker搭建一个最新版运行一下

`docker run --name nacos-quick -e MODE=standalone -p 8849:8848 -d nacos/nacos-server:2.0.2`

执行poc 确实已经关闭了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/noZJ3Kqbu1cicoZicmxMRT2JxpMVuJ88bOOSpuyrfSibkU3f10ZdU0VKo3KlicHS8FIxddS0dpJmG6COgXMfyFhc6Q/640?wx_fmt=png&from=appmsg "null")

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/noZJ3Kqbu1d3FiagSGAy7dXnA4tuzIftuv0OnAu0icShibzomSCkoIf1QsZ4Hjmv3kx9ibyzdUClwChTicHoiakNOKHw/0?wx_fmt=png)

漏洞推送

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/noZJ3Kqbu1d3FiagSGAy7dXnA4tuzIftuv0OnAu0icShibzomSCkoIf1QsZ4Hjmv3kx9ibyzdUClwChTicHoiakNOKHw/0?wx_fmt=png)

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