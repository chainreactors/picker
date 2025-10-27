---
title: 【Python+Java】Burpsuite插件开发
url: https://www.secpulse.com/archives/200103.html
source: 安全脉搏
date: 2023-05-10
fetch_date: 2025-10-04T11:37:42.679175
---

# 【Python+Java】Burpsuite插件开发

[![](https://www.secpulse.com/wp-content/themes/secpulse2017/img/logo-header.png)](https://www.secpulse.com "安全脉搏")

* [首页](https://www.secpulse.com/)
* [分类阅读](https://www.secpulse.com/archives/category/category)

  #### 脉搏文库

  - [内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)
  - |
  - [代码审计](https://www.secpulse.com/archives/category/articles/code-audit)
  - |
  - [安全文献](https://www.secpulse.com/archives/category/articles/sec-doc)
  - |
  - [Web安全](https://www.secpulse.com/archives/category/articles/web)
  - |
  - [移动安全](https://www.secpulse.com/archives/category/articles/mobile-security)
  - |
  - [系统安全](https://www.secpulse.com/archives/category/articles/system)
  - |
  - [工控安全](https://www.secpulse.com/archives/category/articles/industrial-safety)
  - |
  - [CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)
  - |
  - [IOT安全](https://www.secpulse.com/archives/category/iot-security)
  - |

#### 安全建设

+ [业务安全](https://www.secpulse.com/archives/category/construction/businesssecurity)
+ |
+ [安全管理](https://www.secpulse.com/archives/category/construction/securityissue)
+ |
+ [数据分析](https://www.secpulse.com/archives/category/construction/bigdata)
+ |

#### 其他

+ [资讯](https://www.secpulse.com/archives/category/news)
+ |
+ [漏洞](https://www.secpulse.com/archives/category/vul)
+ |
+ [工具](https://www.secpulse.com/archives/category/tools)
+ |
+ [人物志](https://www.secpulse.com/archives/category/people)
+ |
+ [区块链安全](https://www.secpulse.com/archives/category/exclusive/block_chain_security)
+ |
+ [安全招聘](https://www.secpulse.com/archives/category/hiring)
+ |

- [安全问答](https://www.secpulse.com/newpage/question_list)
- [金币商城](https://www.secpulse.com/shop?donotcachepage=c010349fd98847cb9d6e07d3cbc19288)
- [安全招聘](https://www.secpulse.com/archives/category/hiring)
- [活动日程](https://www.secpulse.com/newpage/activity)
- [live课程](https://www.secpulse.com/live)
- [企业服务](https://duoyinsu.com/service.html)
- [插件社区](https://x.secpulse.com/)

小程序

![脉搏小程序](https://www.secpulse.com/wp-content/themes/secpulse2017/img/wxchat.jpg)
[登录](https://www.secpulse.com/user_login)
|
[注册](https://www.secpulse.com/user-register)

# 【Python+Java】Burpsuite插件开发

[工具](https://www.secpulse.com/archives/category/tools)

[公众号:安全女巫](https://www.secpulse.com/newpage/author?author_id=49672)

2023-05-09

19,391

#

********如果你喜欢我的文章，欢迎关注公众号：安全女巫
转载请注明出处：********https://mp.weixin.qq.com/s/xEKSXm2-fCHhyvZxrQUQvQ

burpsuite 最新版下载地址：

关注公众号回复burpsuite

#

# 0x1 前言

官方只支持三种语言：Java, Python & Ruby

因Burpsuite使用Java编写，推荐使用java语言编写插件。若想用Python或Ruby，需使用借助JPython或JRuby，以达到使用Java调用Python或Ruby库的目的。

可根据实际情况进行插件编写。

## 0x2 Burp Api接口

保存所有接口到本地

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200103-1683611694.png)

## 0x3 Java插件编写

### java环境准备

安装jdk

安装idea

idea创建web项目，可做了解  https://blog.csdn.net/justdoit\_potato/article/details/82994046

### 代码编写

创建项目时，File-New-Project-选择jdk版本，点击下一步.

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200103-1683611699.png)

如此，便成功创建项目

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200103-1683611700.png)

将burp导出的API文件Burp文件夹，复制至新建项目src目录，便于后续调用与编写。

新建BurpExtender.java文件，内容如下：

```
package burp;

import java.io.PrintWriter;

public class BurpExtender implements IBurpExtender
{
    public void registerExtenderCallbacks (IBurpExtenderCallbacks callbacks)
    {
        // set our extension name
        callbacks.setExtensionName("Hello world extension");

        // obtain our output and error streams
        PrintWriter stdout = new PrintWriter(callbacks.getStdout(), true);
        PrintWriter stderr = new PrintWriter(callbacks.getStderr(), true);

        // write a message to our output stream
        stdout.println("Hello output");

        // write a message to our error stream
        stderr.println("Hello errors");

        // write a message to the Burp alerts tab
        callbacks.issueAlert("Hello alerts");

        // throw an exception that will appear in our error stream
        throw new RuntimeException("Hello exceptions");
    }
}
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200103-1683611701.png)

###

### 项目打包

File-Project Structure-Artifacts

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200103-1683611703.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200103-1683611704.png)

plugin\_jar为jar包目录

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200103-1683611705.png)

Build-Build Artifacts

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200103-1683611708.png)

成功打包为jar

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200103-16836117081.png)

### Burp插件导入

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200103-1683611709.png)

插件编写信息，成功展示

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200103-1683611710.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200103-1683611711.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200103-1683611712.png)

### Burp调试

以上为简单插件编写，仅为输出展示可不进行调试。若是进行复杂插件编写，必不可少，需idea调试burp插件。具体配置如下：

idea配置，监听8888端口

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200103-1683611714.png)

开启插件调试命令：

java -agentlib:jdwp=transport=dt\_socket,server=y,suspend=n,address=8888 --illegal-access=permit -Dfile.encoding=utf-8 -javaagent:BurpSuiteLoader\_v2021.8.jar -noverify -jar burpsuite\_pro\_v2021.8.jar

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200103-1683611717.png)

进行部署

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200103-1683611718.png)

可见，运行时，jdk版本与burp运行时jdk版本不一致。需将idea中jdk修改

File->Project Settings

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200103-1683611720.png)

此处点击，设置断点

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200103-1683611721.png)

设置成功后点击进行debug模式

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200103-1683611722.png)

此时，将burp插件进行加载，可见调试输出信息

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200103-1683611723.png)

### Tips

Burp sdk与Idea jdk版本需保持一致，否则Burp调试异常

Burp版本最好使用社区版本，否则Burp调试无法开启

文章中，原本使用的中文破解版Burp，jdk 1.8，因遇到以上2问题，更换Burp为burpsuite\_pro\_2021.8、jdk 11

## 0x4 Python插件编写

### python环境准备

安装python2

设置jpython路径

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200103-1683611724.png)

### 代码编写

将burp导出的API文件Burp文件夹，复制至python脚本同级目录，便于后续调用与编写。

python脚本 hello.py

```
from burp import IBurpExtender
from java.io import PrintWriter
from java.lang import RuntimeException

class BurpExtender(IBurpExtender):
    def registerExtenderCallbacks(self, callbacks):
        callbacks.setExtensionName("Hello world extension")
        stdout = PrintWriter(callbacks.getStdout(), True)
        stderr = PrintWriter(callbacks.getStderr(), True)
        stdout.println("Hello output")
        stderr.println("Hello errors")
        callbacks.issueAlert("Hello alerts")
        raise RuntimeException("Hello exception")
```

### Burp插件导入

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200103-1683611726.png)

导入成功显示如下：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200103-1683611727.png)

![](h...