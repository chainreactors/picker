---
title: Tsunami：一款功能强大的通用网络安全扫描工具
url: https://buaq.net/go-137335.html
source: unSafe.sh - 不安全
date: 2022-11-27
fetch_date: 2025-10-03T23:52:27.785942
---

# Tsunami：一款功能强大的通用网络安全扫描工具

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/9ba0cb4d901a5746ef7bb9307e47e561.jpg)

Tsunami：一款功能强大的通用网络安全扫描工具

TsunamiTsunami是一款功能强大的通用网络安全扫描工具，除此之外，它还是一个可扩展的插件系统，可以帮助广大安全研究人员以高可信度的方式检测和扫描高危严重漏洞。Tsunami依赖于其功能强大的
*2022-11-26 08:48:50
Author: [mp.weixin.qq.com(查看原文)](/jump-137335.htm)
阅读量:56
收藏*

---

![](https://mmbiz.qpic.cn/mmbiz_gif/3xxicXNlTXLicwgPqvK8QgwnCr09iaSllrsXJLMkThiaHibEntZKkJiaicEd4ibWQxyn3gtAWbyGqtHVb0qqsHFC9jW3oQ/640?wx_fmt=gif)

## Tsunami

Tsunami是一款功能强大的通用网络安全扫描工具，除此之外，它还是一个可扩展的插件系统，可以帮助广大安全研究人员以高可信度的方式检测和扫描高危严重漏洞。

Tsunami依赖于其功能强大的插件系统来给安全社区提供基本的漏洞扫描功能，所有公开可用的Tsunami插件都托管在一个独立的google/tsunami-security-scanner-plugins安全扫描插件库中。

## Tsunami的必要性

当安全漏洞或错误配置被攻击者主动利用时，组织需要迅速作出反应，以保护潜在的易受攻击的资产。随着攻击者越来越多地投资于自动化，对新发布的高危严重漏洞作出反应的时间窗口通常以小时为单位。这对拥有数千甚至数百万互联网连接系统的大型组织来说是一个重大挑战。在这种超大规模的环境中，必须检测到安全漏洞，并以完全自动化的方式进行理想的补救。要做到这一点，信息安全团队需要有能力在极短的时间内实现并推出针对新的安全问题的检测器。为了解决这些挑战，我们创建了一个可扩展的网络扫描引擎Tsunami，它可以在未经验证的情况下以高可信度的形式检测到高危严重漏洞。

## 工具特性

> Tsunami支持手动管理小规模漏洞集；
>
> Tsunami能够检测到高危安全漏洞（RCE等），这些漏洞通常利用率非常高；
>
> Tsunami生成的扫描结果可信度非常高，假阳性非常低；
>
> Tsunami探测器部署和实施都非常简单；
>
> Tsunami支持自定义功能扩展，运行速度快，抗干扰能力强；

### 当前状态

> Tsunami的当前版本仍处于开发测试阶段（pre-alpha），仅供开发者预览。
>
> Tsunami项目当前提供的API接口将随时发生变化。

## 快速开始

如需立即使用Tsunami的扫描功能，请按照下列步骤操作。

1、安装Tsunami所需的依赖组件：

```
nmap >= 7.80ncrack >= 0.7
```

2、安装配置一个存在漏洞的并且是Tsunami可识别的应用程序，比如说一个存在身份验证漏洞的Jupyter Notebook服务器。最简单的方法就是直接使用一个Docker镜像：

```
docker run --name unauthenticated-jupyter-notebook -p 8888:8888 -d jupyter/base-notebook start-notebook.sh --NotebookApp.token=''
```

3、执行下列命令：

```
bash -c "$(curl -sfL https://raw.githubusercontent.com/google/tsunami-security-scanner/master/quick_start.sh)"
```

### 项目中的quick\_start.sh脚本将会执行下列任务：

1、将下列两个项目克隆至本地主机的$HOME/tsunami/repos目录中：

```
google/tsunami-security-scannergoogle/tsunami-security-scanner-plugins
```

2、编译所有的Google Tsunami插件，并将所有的插件jar文件移动到$HOME/tsunami/plugins目录内。

3、编译Tsunami扫描器Fat Jar文件，然后将其移动到$HOME/tsunami目录内。

4、将tsunami.yaml样本配置文件移动到$HOME/tsunami目录内。

5、输出样本Tsunami命令并使用之前生成的工具对127.0.0.1地址进行漏洞扫描。

## 扫描器构建和执行

切换到项目的根目录，并执行下列命令：

./gradlew shadowJar

命令执行完成之后，生成的扫描器jar文件将存储在main/build/libs目录内，命名为tsunami-main-[version]-cli.jar。这是一个Fat Jar文件，可以当作一个单独的代码库来使用。

如需执行扫描器，首先我们需要将插件安装在一个给定目录内，并且至少要安装一个PortScanner插件。假设插件安装在~/tsunami-plugins/目录内，那么你就需要使用下列命令来执行一次Tsunami扫描任务：

```
java \    # Tsunami classpath, as of now plugins must be installed into classpath.    -cp "tsunami-main-[version]-cli.jar:~/tsunami-plugins/*" \    # Specify the config file of Tsunami, by default Tsunami loads a tsunami.yaml    # file from there the command is executed.    -Dtsunami.config.location=/path/to/config/tsunami.yaml \    # Main class for TsunamiCli.    com.google.tsunami.main.cli.TsunamiCli \    # Scan target.    --ip-v4-target=127.0.0.1 \    # Scan output file and data format.    --scan-results-local-output-format=JSON \--scan-results-local-output-filename=/tmp/tsunami-result.json
```

## 安装Tsunami插件

正如前文所述，Tsunami插件必须安装在一个可以在运行时被Tsunami识别的目录内。这个目录可以是任意目录，只要该目录路径存在于Tsunami运行时类路径下即可。

一般来说，每一个Tsunami插件都是一个单独的jar文件，你可以将任何一个支持的jar插件文件放在这个目录内。比如说，如果插件安装目录为~/tsunami-plugins/，那么该目录结构应该为:

```
$ ls ~/tsunami-pluginsawesome-port-scanner.jar         my-web-fingerprinter.jar      weak-ssh-cred-detector.jarwordpress-installation.jar       exposed-jupyter-notebook.jar
```

## 许可证协议

Tsunami项目的开发与发布遵循Apache 2.0开源许可证协议。

## 项目地址

Tsunami：

```
https://github.com/google/tsunami-security-scanner
```

作者：Alpha\_h4ck

转载自FreeBuf.COM

黑白之道发布、转载的文章中所涉及的技术、思路和工具仅供以安全为目的的学习交流使用，任何人不得将其用于非法用途及盈利等目的，否则后果自行承担！

如侵权请私聊我们删文

**END**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3xxicXNlTXL8fHInwic65QarBzLTDecgAlRicyRRNJu5ItVq0eGBmhibeaUEib2sMnAsOTOHicWtz7P2iaAeftdlNQGCg/640?wx_fmt=jpeg)

多一个点在看![](https://mmbiz.qpic.cn/mmbiz_gif/zYdFdnRZ0h95ZAL5c8h6iaMiaqbgljvZ80YraNgwWAtyyZRGT8INEgx8qWKgf9wXribCDNibDvDa2R1EQB4grqAKDg/640?wx_fmt=gif)多一条小鱼干

文章来源: https://mp.weixin.qq.com/s?\_\_biz=MzAxMjE3ODU3MQ==&mid=2650557032&idx=4&sn=54ec7e2dd2aa7bc166962fa56ba53953&chksm=83bd2f8cb4caa69a6d39386ebdb8ec0e49fd1b1c171c1e94b5fde53a5cad42ec6b5ada72d5ef#rd
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)