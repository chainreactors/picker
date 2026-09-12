---
title: PHP代码审计-动态调试配置（附环境）
url: https://mp.weixin.qq.com/s/eLXJhbrOscodksn-K4OirA
source: Doonsec's feed
date: 2026-09-11
fetch_date: 2026-09-12T06:43:19.178323
---

# PHP代码审计-动态调试配置（附环境）

# PHP代码审计-动态调试配置（附环境）

原创

wolfsec
wolfsec

风铃Sec

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

##### 环境：

* ‎`Windows 11`
* ‎`PHPstudy 8.1`
* ‎`PHPStorm 2025`
* ‎`Xdebug 2.7.2(phpstudy自带)`
* ‎`php 7.3.4-nts`

#### PHPStudy配置

创建一个网站，专门用户与动态调试，网站域名设置为`debug.io`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhUibV7MPZluvG8juAickVw7ZrK6oQJkmiavTxOVJiaiaEyicic306FTiacRicmOe43WzXibSMN4ZHJDXj5aibxEgib0qFkKF4rDUaOLFl1mxs62ws3wNGk/640?wx_fmt=png&from=appmsg)

选择PHP版本为`php7.3.4`，并开启php扩展`xdebug`：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhUibV7MPZlsUSia7eibXazaicgzic19QkycRK8hMuYGPYpqXEtbjYSBn14mgO5ibiammwFRfVGxBTFWSvEZqNHLYSckheZLn6UlPMAvKYVRH2CA5w/640?wx_fmt=png&from=appmsg)

通过小皮面板打开php所在文件夹，验证xdebug在CLI中是否成功开启。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhUibV7MPZlsjoTNGrA4Aniav55iawr1l9e7z3ibu4guMg5wUXAIRfLLa8sggjR0ndEPyAsH0W6n1l7XMJ1rLkVRDQL52hRkGp8FZm0u7pibnZn4/640?wx_fmt=png&from=appmsg)

找到php.exe文件所在路径，打开`cmd`，输入如下命令：

```
php.exe --ri xdebug
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhUibV7MPZltY8lfIOJxKibibCtAZGG2mNzdokIQaKfYS0iapSibQnDb9ibXvYicdbibXMK9ibcTM6ChtoZxPGt2B3PbL5zN2jkE2CHnhgdmVWQ53VOM/640?wx_fmt=png&from=appmsg)

输出如上内容，标识`Xdebug`成功开启，且小皮自带的`Xdebug`版本为`2.7.2`。这个时候表示`Xdebug`在CLI生效，但是不代表此时`Xdebug`在`Web`端生效，想让`Xdegub`在`Web`端也生效则需要打开`php.exe`同目录的一个叫做`php.ini`文件，在文件末尾贴入如下内容（**事实上只要phpstudy中的扩展中开启xdebug插件后以下内容会被自动填充，我们只需要添加xdebug.idekey="PHPSTORM" 以及修改相对应的host、port和xdebug.remote\_enable=On就好了**）：

```
[Xdebug]
xdebug.idekey="PHPSTORM"
zend_extension=D:/phpstudy_pro/Extensions/php/php7.3.4nts/ext/php_xdebug.dll
xdebug.collect_params=1
xdebug.collect_return=1
xdebug.auto_trace=Off
xdebug.trace_output_dir=D:/phpstudy_pro/Extensions/php_log/php7.3.4nts.xdebug.trace
xdebug.profiler_enable=Off
xdebug.profiler_output_dir=D:/phpstudy_pro/Extensions/php_log/php7.3.4nts.xdebug.profiler
xdebug.remote_enable=On
xdebug.remote_host="debug.io"
xdebug.remote_port=9003
xdebug.remote_handler=dbgp
```

| 配置项 | 作用 |
| --- | --- |
| ‎`xdebug.idekey` | 指定‎`IDE` 调试会话的 ‎`Key`，用于标识调试客户端 |
| ‎`zend_extension` | 加载 ‎`Xdebug` 扩展‎`DLL` |
| ‎`xdebug.remote_enable` | 开启远程调试（要设置成On） |
| ‎`xdebug.remote_host` | 指定 IDE 所在主机（由于是在本地调试，所以此处可以直接与 ‎`PHPstudy` 中设置的网站域名一致） |
| ‎`xdebug.remote_port` | 指定 ‎`Xdebug` 连接 IDE 的端口 |
| ‎`xdebug.remote_handler` | 指定远程调试协议：‎`DBGP（Debugging Protocol）` |

在网站根目录中新建一个`phpinfo`，通过网站访问，出现`Xdebug`相关内容则表示`Xdebug`在`Web`端成功生效（不生效可能需要重启网站包括停止网站和重启Web服务器）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhUibV7MPZlsTMJH2YbFcaauclpknrHA3OtpJtFkX3XveCY4kNDoHtLkx9icYgaYJicRoD4CLiadIVCiaMPW1O87njDbNzTprVbfCc72iaTRWwUSM/640?wx_fmt=png&from=appmsg)

#### PHPStorm 配置

在`PHPStorm`中输入`Ctrl + Alt + S`打开设置窗口，设置PHP语言版本和PHP解释器路径。

![](https://mmbiz.qpic.cn/mmbiz_png/bhUibV7MPZlv0RCxddAa9pPGZMjseChu0Iw7MTVLjHGD4ic3dWCEic1AXibl8whZVpvE86PzP66Lkrdw51KtsyrMwRPcAhtl3pAxrPSjvibRwAnE/640?wx_fmt=png&from=appmsg)

设置`Debug`端口为`9003`，这边的端口号要与`php.ini`文件中的`remote_port`值一致。

![](https://mmbiz.qpic.cn/mmbiz_png/bhUibV7MPZltvCp4PIQM1edGfjUicibGzCePib7Ngknjhyf0UicWMeo12scOTLclJ65MI6iaYRkvVA2iazJqxnKcniaPCUoibZib2ibribABXVrW3xE6uT4/640?wx_fmt=png&from=appmsg)

设置`DBGp Proxy`的`IDE key`为`PHPSTORM`，`Host`为`debug.io`，端口设置为`9003`。（分别与`php.ini`中的 `xdebug.idekey` 、`xdebug.remote_host`、`xdebug.remote_port`值一一对应）

![](https://mmbiz.qpic.cn/mmbiz_png/bhUibV7MPZlvKyfMqaO6YanpN4MqWFXU9ibrAdkORPproQaC8NUpRZFOicIYk17Mn86Lemxoibk1LEsMlKG2gPzfWicDHwjDia7JUb7yjPLXNDiaqU/640?wx_fmt=png&from=appmsg)

设置服务器：`Name`可以随意设置，`Host`设置为`PHPStudy`中网站的域名`debug.io`，`Port`设置为网站的端口`90`（这边的端口是网站的访问端口，而不是`php.ini`中设置的调试端口。）

![](https://mmbiz.qpic.cn/mmbiz_png/bhUibV7MPZltOW4jnT2BHhu6AppDyTkV7PxmmaQgZ31WNJQShOWTwOicoByRtgqZ3WbVia6fNH2OnuV2SWnR0u69WGfPllQDEykoDHsDVLFrP4/640?wx_fmt=png&from=appmsg)

设置完`Host`和`Port`后，勾选底下的`Use Path mappings`，使用路径映射将`PhpStorm`看到的项目文件路径，和 `PHP/Xdebug`实际运行的文件路径对应起来（填写要调试的系统所在的路径），点击`Apply`，最后再点`OK`。

![](https://mmbiz.qpic.cn/mmbiz_png/bhUibV7MPZls5JpB7ibP1m7lnkTt1Sz2sgc7H3WJ322QK7ia9GsJcC6lvB9mG8052liaqr2JccuePMDIrEfWCHJHhnotRkZCP4R6YVo4cxbYIyk/640?wx_fmt=png&from=appmsg)

紧接着开始编辑调试配置，选择`Edit Configurations`。

![](https://mmbiz.qpic.cn/mmbiz_png/bhUibV7MPZlsJPcj8myteMmics7oVfmvf7pz7ANBUkc9LYGXibc5uQq5PeG2jFaaOrrrz0Z9PkpiaB4icsoNHSdJz5phhLgUPIvGkLyXjEavYgCQ/640?wx_fmt=png&from=appmsg)

编辑调试配置如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhUibV7MPZlsOl7zuxJJFleqhcB1O69a1XqibKFbf4nOPC7kBbPazUS0XbnYqhpeOaibHNWcticguqC3GHwpR5WDKEiakzcU06znRYMIHRr8BTmo/640?wx_fmt=png&from=appmsg)

验证需要注意，系统存放的本地目录和网站的访问目录要对应上，填写完毕后点击Validate，如果没问题则会出现绿色打勾的内容。（注：黄色感叹号不用管）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhUibV7MPZltauISKcrO7owhDFPPJCRk8FFwzkoriacSEIucSTmv5yU10uRdibibIhRJ9VbeYBpFtyu7wvIiahE4Mj1D7Z4BzH8Ml2mWSZ81rBMQ/640?wx_fmt=png&from=appmsg)

验证成功后，返回上一层窗口，点击`debug`按钮开始调试。

![](https://mmbiz.qpic.cn/mmbiz_png/bhUibV7MPZluibAXWG1BhZ0QNTibldsfZskw6icUlibq24sFdH7ZuibCpibmQfibePRicHVkK1Otw0Kp8LO0O5v1Ne05OgxRnSrOKWQh6kUzGZbrbaN0/640?wx_fmt=png&from=appmsg)

最后结果如下（记得先打断点）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhUibV7MPZlvaxXiabBibBdKGvOUA5DUM5Jz2xF5vsDoubzecBDadjuoNwKZ4stbJXypCwfap9aCABN6GeFB9JMaltNEREiaibkqLDoianf9GexCo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/bhUibV7MPZls3ebBttKicugraRhR0V4BCNIUviagv6wXQ7PT1O3xdLYIVvjrwkia7NVibJrzxBXmDjC9sabIVia7B5qPnlSSDutHdjaYMSTfArT6U/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhUibV7MPZlupo5hPTlNiafbhTE4BTjXNU18vsic7bKOvpGIDK4HFicdtbibkYIqibcIS6QTxIpf62SLaBk2VvhGLnsRjSvkkjKA20jdursOiacIHA/640?wx_fmt=png&from=appmsg)

**问题记录**：如果选择Debug的端口为9003，就要把原本的9000删除，不然会一直报9000端口繁忙，导致调试失败。（可能是我之前的错误配置导致的）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhUibV7MPZluicQicjlwnhEEtan408yBEGfe8vASRhRSQeNxYpz25tMCRBLiakd6IicJss7asexZIfqNGibBTiaTF75yCDgQjhh6GLtCqsQKibicG9OI/640?wx_fmt=png&from=appmsg)

#### 浏览器配置

安装`JetBrains`提供的 `Xdebug Helper`

![](https://mmbiz.qpic.cn/mmbiz_png/bhUibV7MPZltVtobqfRgibVTqkUa7JV5tyqXl3RlibpRCgm6Ejc2LRpT38ufDPdOK2N536x00vTuGGtFKrAa5fxCm5E8TC4jRHcXYcI4iaIBicX0/640?wx_fmt=png&from=appmsg)

安装完毕后，URL中的`XDEBUG_SESSION_START`会消失。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhUibV7MPZltJHFbKzugfmx9az7G0bickvESHHAticCGemYP7uiaZx3CfVbxxRhQkpia6xBK8gC9Dibn67GjRHG7U7TxRjk2yAgRIGvS7l0icOhOj8/640?wx_fmt=png&from=appmsg)

#### PHPStorm 配置

「PHPStorm」

链接：https://pan.quark.cn/s/37f111bd9f11

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhUibV7MPZluu2xqRlGrw0O9MZzClib76celMVPBnFt4rcHDfK11qYF61sa98Zh4AgrajUkTL2c0r4DYTib15X01ElDkuHkm2FIKokj1jFUqnc/640?wx_fmt=png&from=appmsg)

「激活教程」

链接：https://pan.quark.cn/s/4b0d7809517c

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bhUibV7MPZlvpIKgEdIXBZEuY9BjTK5IAcWuv4n73icRbePP5fTTHV00dD2OP0GgjXxy7iaBQKlpKrKckmyzG0VEnWlZeH2rvClzNvHx1Jp64Q/640?wx_fmt=png&from=appmsg)

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qGTEdaLg0HmibOdP6ibKTOYNXKuEdbPFJKnX0Z54TIaWXmS6apnB5FYRgZVtWlzvTJK3lQzuxEHTa5kCSibf2eXZw/0?wx_fmt=png)

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