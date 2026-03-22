---
title: 阿里云SLS对接方案技术实现
url: https://mp.weixin.qq.com/s/9q7Opvqs_qOryf9pAAIhPw
source: Doonsec's feed
date: 2026-03-21
fetch_date: 2026-03-22T04:14:20.323768
---

# 阿里云SLS对接方案技术实现

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/bCZqF8oBiaybnH1mGSJkscom6ODPF03U0ajRIxsVLDTpNl0dSjicAw4fDh3St16vqd8pyN0aNQoO609LjVOnzgI0n1JILVg9w7iatFH3aicyEe4/0?wx_fmt=jpeg)

# 阿里云SLS对接方案技术实现

原创

静观云起
静观云起

码云精炼

![]()

在小说阅读器中沉浸阅读

**阿里云SLS是Simple Log Service的缩写**‌ ，即“简单日志服务”。它是阿里云提供的一站式日志管理平台，支持Log(日志),Metric(指标),Trace(调用链)数据的采集、存储、分析与可视化，广泛应用于运维监控、安全审计和业务分析等场景。

![](https://mmbiz.qpic.cn/mmbiz_png/bCZqF8oBiaybVgTTDfesvH61Z45NPIynM8yiayNzJ9a6QIEia0u0OiabGCKiciaXLVWKJksb6ib7X520HKjO09jxcqPEuWuUBREHLIfr8n77Qr9vgA/640?wx_fmt=png&from=appmsg)

一 ‌**开通服务**‌

登录阿里云控制台

进入 ‌**日志服务SLS**‌ 并开通服务

####

#### 二 ‌**创建Project与Logstore**‌

‌**Project**‌：资源管理单元，命名体现业务用途(如 `prod-logs)`

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/bCZqF8oBiayZnNCTIEwVstgibtjFRlngic7YKjSGXiaGMs78WqiaxxSDHplZE8o934wRKNVX68rcbEFjpbibvtQkAebdicx7CoFcfCXVNmKQKg7ZRo/640?wx_fmt=png&from=appmsg)

‌**Logstore**‌：日志存储容器，建议按服务或组件划分(如 `nginx-access`、`app-error)`

![image](https://mmbiz.qpic.cn/mmbiz_png/bCZqF8oBiaya8HtBLibB6ibUF8jKG4MPicJWSZJibW3JIgF2HiaCy7fQ2YsuohUFIvjia4XtHw92jMSe2bySjGPIhRlibP9CBeOP3trKdzApgibtMhAg/640?wx_fmt=png&from=appmsg)

设置日志保存周期（推荐 ≥30天）

开启索引功能以支持查询分析

三 ECS实例上安装并配置Logtail

✅ 安装Logtail

LoongCollector（原Logtail）‌，安装客户端采集服务器/容器日志

登录ECS实例，根据实例的操作系统选择对应的安装方式：

‌**Linux系统**‌：可通过包管理工具安装

如CentOS系统执行`yum install -y logtail`

Ubuntu系统执行`apt-get install -y logtail`

也可以从SLS控制台的“Logtail管理”页面下载安装包手动安装。

‌**Windows系统**‌：从SLS控制台下载Logtail安装包，运行安装程序完成安装

支持文件路径配置（如 /var/log/nginx/\*.log）

**✅ 配置Logtail采集规则**‌

‌**Linux系统**‌：

编辑Logtail的配置文件，一般路径为`/etc/logtail/conf/`，创建新的配置文件，比如`ecs-log.conf`。

在配置文件中填写SLS项目和日志库信息，以及要采集的日志文件路径、日志格式等，示例配置如下：

```
{  "inputs" : [    {      "type" : "file",      "detail" : {        "file_paths" : ["/var/log/nginx/access.log"],        "log_format" : "json",        "encoding" : "utf-8"      }    }  ],  "processors" : [],  "outputs" : [    {      "type" : "sls",      "detail" : {        "project" : "projectName",        "logstore" : "logStoreName",        "endpoint" : "SLS endpoint",        "ak_id" : "AccessKey ID",        "ak_secret" : "AccessKey Secret"      }    }  ]}
```

保存配置文件后，重启Logtail服务，执行systemctl restart logtail

Windows系统：

1. 打开Logtail的配置界面,点击“添加采集配置”

2. 选择“文件采集”,填写日志文件路径,日志格式等信息

3. 在输出配置中,选择“SLS”,填写SLS项目名称,日志库名称,地域endpoint,AccessKey ID和AccessKey Secret

4. 保存配置后，启动Logtail服务

### 四 验证对接是否成功

等待一段时间，让Logtail采集并上传日志到SLS。回到SLS控制台，进入对应的日志库，查看是否有日志数据上传。也可以在SLS控制台使用日志查询语句，查询采集到的日志内容，验证日志是否正常采集和上传。

![](https://mmbiz.qpic.cn/mmbiz_png/bCZqF8oBiayZsw7NvONUgYPCoEuVkZRk6uH3Oib21dHTBh7Eictbl3cr1M2RNcpGrWEmic5a7c2buTy9PxBCFticFvfywXk7SW8ib3zjQrwj8G8b0/640?wx_fmt=png&from=appmsg)

## 五 配置通知对象

1.创建用户

在左侧导航栏中，单击**告警**。在**告警中心**页面，参照下图，例如配置用户`Bob`相关信息，单击**确认**。

![image](https://mmbiz.qpic.cn/mmbiz_png/bCZqF8oBiayZfYiaupHPAA4BHWcCQnw6xoCWibCdvjjd2p6N7RSbibPkicPuJDIujqRjQM9Nib7QBbXDqBiax1ICo99sFlcx10ictyVCpFb06RNfFdg/640?wx_fmt=png&from=appmsg)

### **2.创建用户组**

参照下图步骤，在**添加用户组**对话框中，将`Bob`加入到`test`组，单击**确认**。

![image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/bCZqF8oBiaybympkMJgPpR3Cl1opUr4BG3LZAkKqEiasOiczriciaUUQPNTYbZNeeJOmjLCzLDtdbxN2DjpMtDfQSam1jOytSwbGkGp3E6bJAWPE/640?wx_fmt=jpeg&from=appmsg)

六 配置预警规则

将日志采集到LogStore后，设置告警规则，有数据则触发告警，钉钉机器人发送告警信息并提醒用户处理。

![image](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7dFiacmgGnmbXX9aScvoDiaibbmwBkadYIoRJwNGm522bDEzLJ8nUuPYxSElYsYTItLVJWIecxDvr83ia7G8oK6icEeMzfJLKogUXfeaPlPkEl4tw/640?wx_fmt=svg&from=appmsg)

## 1.在**告警中心** > **告警规则**页签，单击**新建告警**。

## ![](https://mmbiz.qpic.cn/mmbiz_png/bCZqF8oBiayasZeHLnhbk4GrIO1LEzO7zqxSyMITjP76SyK5iaQZs3BbRExVXC3R2GuDaGd7rqutP6ibY48VZGbpLcE8MKZhxv0mE9t4g8WKGw/640?wx_fmt=png&from=appmsg)

## 2.在**新建告警**面板中，配置**查询统计**，单击**添加**

## ![image](https://mmbiz.qpic.cn/sz_mmbiz_png/bCZqF8oBiayaA9KX1mcPrUqJezyPf0FcnjoiaKBfvAz3M9ITic8ykE5ThF80INQfsuovbHn7oKsXN6vuxN8FFEwo56eHdBZrO8ef8EH6WQc4wQ/640?wx_fmt=png&from=appmsg)

## 3.在**查询统计**对话框中，选择目标**日志库**，单击**预览**查看数据，然后单击**确认**

## ![](https://mmbiz.qpic.cn/mmbiz_png/bCZqF8oBiayZhYlZOVApPxtABNxia3oIsllmiaW279uXwQsLu6cbQ8YT6iaFXkxdkvsxR6uXWFwiaIB1YFnexTria2P87Wq3BBaZXMThqnNRAVt94/640?wx_fmt=png&from=appmsg)

##

4.在**新建告警**面板中，**触发条件**选择当**有数据**时告警，**严重度**选择**中**，点击**确定**。

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/bCZqF8oBiayZLAia4WYAZNM6h3yThD1Lp36BQMy9tnfibAhHwyuNmiclmgf2ZWFmj3t4M6KxyOFicnSoNmlfOP0Qeq8ZqRPhXZksHQxPBcjibVkGA/640?wx_fmt=png&from=appmsg)

七  配置通知策略

### **配置内容模板:**

1. 在**告警中心**-->**通知策略--**>**内容模板**页签，选择**SLS内置内容模板**，在操作列单击**修改**。

   ![image](https://mmbiz.qpic.cn/mmbiz_png/bCZqF8oBiaybyC2qsVYpsrdyyiaVSia0QS8t7h8kQiaQFUqPgcZEaXkFhg2URDCduibHgPZ9XWDusMRMV4FbIs8lK7tpvzpFfYSeezG9Q1kAvic9I/640?wx_fmt=png&from=appmsg)
2. 参考下图，配置**钉钉**告警的**发送内容**。

   ![image](https://mmbiz.qpic.cn/mmbiz_png/bCZqF8oBiayaXDUNciboaNxdvpWZc5iaQ00L1zJ1FrHnbtbZexorlY1DiazsdJ8VWbOXUVlJKNXmricM5DY4r3REiazjPlByuicFObW9iaicj4P3etYQ/640?wx_fmt=png&from=appmsg)

### **配置SLS通知:**

1. 前提条件

   例如使用钉钉发送告警通知前，需要完成如下配置。

   ✅根据钉钉企业内部应用机器人的创建和安装创建一个消息接收模式为HTTP模式的机器人应用。

   ✅打开钉钉客户端，进入钉钉群，单击右上角的图标。

   ✅选择 **机器人--**>**添加机器人**。

   ✅选择**通过Webhook接入自定义服务**，点击**添加**，配置**机器人名字**，**安全设置**选择**自定义关键字**，输入**告警**，点击**完成**。

   ✅在群聊中的机器人管理页面查看创建好的机器人，复制Webhook链接。
2. 配置通知对象

   在**新建Webhook**对话框，**请求地址**填写复制的Webhook链接，参考下图配置，然后单击**确定**。

   ![image](https://mmbiz.qpic.cn/sz_mmbiz_png/bCZqF8oBiayay0lWXIrfibf0Tia8VzvoFRdCRTtyKD0yjjJSwBXwZI9SQSGtcHat33u6iaaYpGYicJMKWUj5YZ1DKlia0uYqSNEqdE7Y6XcRp65rM/640?wx_fmt=png&from=appmsg)
3. 配置通知渠道

   在**告警规则**页签中，选择目标规则，单击**编辑**。

   ![image](https://mmbiz.qpic.cn/sz_mmbiz_png/bCZqF8oBiayaoic4bmdiaGGo49StpkzcxJ3C9xVyoXgPvPTWkwdVZiacFgXcQSxdIp5GcrzAVnDRwerWGuTFrMll7CcK5zPYpMaNiaV3LicqaWRhY/640?wx_fmt=png&from=appmsg)

   在**编辑告警**面板中，参考下图配置，然后单击**确定**。

   ![image](https://mmbiz.qpic.cn/sz_mmbiz_png/bCZqF8oBiayZgNliciayxHBhIwTfureicjs2ecuqI5DmRsL2JFDarYbUGxjuMsmKOSbhO0S0k3EzMBSKh5fibLvt2YyicGcctE1kUibXJLD7ELCiaj4/640?wx_fmt=png&from=appmsg)

##

## 八 查看告警触发记录

1. 在**告警中心--**>**告警大盘--**>**告警规则中心**页面，查看告警触发次数。

![image](https://mmbiz.qpic.cn/mmbiz_png/bCZqF8oBiayYicCF3ZND6jD7f7hjfcWZBYMWuZhsriaDibyicMJA0VeKhibiaibLvAiaLQewG5ian2ptenhD1QElwRP8Bq8ju1F7SLic4ghvLY3ew3eMWY/640?wx_fmt=png&from=appmsg)

2.在****告警中心--**>**告警规则****页面，单击目标规则。

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/bCZqF8oBiaybYPhTPTmuRmShDJhhMdMSAiajAfFrzkeStEia6ZJrTeG87YCC6fWQrdPeMWlxbjhKjWBQxPs88J6icKBc3WbuzbbpJICtCHZcEDA/640?wx_fmt=png&from=appmsg)

3.您可以查看详细的告警信息。**是否触发告警**为true，表示已成功触发。

![image](https://mmbiz.qpic.cn/sz_mmbiz_png/bCZqF8oBiayasw5Yic1f7tCxgCE2FU3zwNQ4924UvQITSicxtunRy9GCxHxuwrvJIvll1tJQ3VGDQTjnWhHPn3ODPynrdzf2Q406XuMGHrbcic0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/YFxLNg1Bibfnia4huCODlTdyh6PTbL1pic45RaY9PANbJVIia0XOz1gV28f9BHd4341P1lpqQwn0cRGBjHPbHYmYIQ/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/YFxLNg1BibfnlOXAcdPXnWKdTyfxKRwkUYCzGrICTx2DxXjHOOr3JOX74dPjlW71DIy7udMwgvWdUuh3FgJs6Pw/0?wx_fmt=png)

码云精炼

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/YFxLNg1BibfnlOXAcdPXnWKdTyfxKRwkUYCzGrICTx2DxXjHOOr3JOX74dPjlW71DIy7udMwgvWdUuh3FgJs6Pw/0?wx_fmt=png)

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