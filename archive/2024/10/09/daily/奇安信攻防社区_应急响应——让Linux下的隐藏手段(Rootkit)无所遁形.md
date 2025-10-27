---
title: 应急响应——让Linux下的隐藏手段(Rootkit)无所遁形
url: https://forum.butian.net/share/3796
source: 奇安信攻防社区
date: 2024-10-09
fetch_date: 2025-10-06T18:45:30.811507
---

# 应急响应——让Linux下的隐藏手段(Rootkit)无所遁形

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

### 应急响应——让Linux下的隐藏手段(Rootkit)无所遁形

* [安全工具](https://forum.butian.net/topic/53)

本文主要针对黑灰产相关的蠕木僵毒等恶意软件在Linux上常用的rootkit手段做一些总结，以及详细分析常见应急响应中遇到的进程、文件隐藏手段的原理以及排查和恢复方法；

0x01 前言
=======
本文主要针对黑灰产、以及蠕木僵毒等恶意软件在linux上常用的rootkit手段做一些总结，以及详细分析常见应急响应中遇到的进程、文件隐藏手段的原理以及排查和恢复方法；
从技术实现原理上看，笔者把其常见的rootkit隐藏手段大致分为五大类：
> 1、通过文件挂载实现隐藏
>
> 2、通过用户层劫持链接器或链接库实现隐藏
>
> 3、通过劫持系统环境变量，劫持相关命令，从而实现对影藏
>
> 4、通过内核层劫持实现隐藏
>
> 5、通过ebpf完成的动态劫持内核逻辑实现隐藏
0x02 实现
=======
一、通过挂载/proc/pid实现pid隐藏
----------------------
### 原理
ps 、netstat 是遍历/proc 来显示pid的原理，通过隐藏相关 /proc/pid 文件夹来实现pid隐藏
### 实现
运行如下命令，将pid对应文件夹挂载到隐藏目录上面
`mount -o bind /home/.hidden /proc/9212`
### 现象：
如下图，使用root权限调用 netstat 发现 PID和Programname 都是空：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-db6eee70bcbb64a72739f5a4044b04ae7eb89407.png)
### 排查方法
1、`cat /proc/$$/mountinfo`
`cat /proc/$$/mountinfo`，发现/proc/9212被挂载到了一个.开头的隐藏文件里面
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-ba8094d394ff3bd1dabdd0b8c593695757af622d.png)
2、 `ls -lai /proc`
在/proc下使用ls -lai:可以发现一个异常的pid目录，异常大小
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-c80cac57bb0640030f175240692182529b3131b9.png)
### 解除方法
使用umount 解除挂载
`umount /proc/9212`
二、通过用户层劫持加载器/连接器隐藏进程pld（用户层rootkit）
-----------------------------------
### 原理
linux在进程启动后，和windows加载dll一样会按照一定的顺序加载动态链接库，相关顺序如下：
- 加载环境变量`LD\_PRELOAD`指定的动态库
- 加载文件`/etc/ld.so.preload`指定的动态库
- 搜索环境变量`LD\_LIBRARY\_PATH`指定的动态库搜索路径
- 搜索路径`/lib64`下的动态库文件
攻击者常见使用的劫持方式大致存在以下三种：
1、可以通过`LD\_PRELOAD` 最先被加载的特征，攻击者写一些so文件，在这个so文件里面实现一些本来对应命令要使用的函数，运行相应命令会先从该环境变量中加载我们自定义的so文件，从而劫持相应命令对应的函数，实现恶意的逻辑；
2、利用`/etc/ld.so.preload`是系统的默认ld预加载路径，攻击者可以写一些so文件，在这个so文件里面实现一些本来对应命令要使用的函数，然后把恶意so文件的路径写入该文件内容中，从而劫持相应命令对应的函数，实现恶意的逻辑；
3、利用linux基本都是基于glibc的特征，大部分的动态连接的基础文件都是基于几个常见的so文件，比如libc.so.6，Linux下命令的动态链接中基本上都会使用这个so文件，因为这个so文件实现了各种标准C的各种函数。对于GCC而言，默认情况下，所编译的程序中对标准C函数的链接，都是通过动态链接方式来链接libc.so.6这个函数库的；所以这里攻击者可以替换劫持该so文件，从而实现对linux的几乎所有依靠动态连接的命令的劫持；
拿第二种方式举例：
回到这个进程pid的隐藏，`ps\top\netstat`等命令是通过读取遍历/proc/pid内容来返回对应的pid等相关值的，读取文件目录底层是通过 readdir/readdir64 实现，这里我们可以利用ld预加载特性，编写恶意的so文件，在相关文件里面重写上面两个函数，在相关函数中当特殊名称的进程出现的时候，相关函数不做返回，或者返回为空跳过即可，并将路径添加到`/etc/ld.so.preload`中；
该操作对ps的隐藏效果最好，因为ps的所有结果都是完全依赖于 /proc/pid 来获取内容；netstat的话是部分依赖，仅仅获取不到pid和pname（这也是一般netstat能看到网络连接，但是看不到对应的pid和进程名的原因），其他的能拿到的；
参考项目 <https://github.com/gianlucaborello/libprocesshider>
### 实现：
拿第二种方式举例：
使用上面项目编译生成的.so文件放入受害机器；
修改processhider.c文件里面的process\\_to\\_filter 参数，后面修改成要隐藏的进程：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-20c91cc5a9653fe56854d8eba30839c470e18239.png)
这个想要通过preload加载，也有好几种方式（1、修改$LD\\_PRELOAD 环境变量，添加so文件路径；2、创建/etc/ld.so.preload文件并写如对应so文件路径；3、修改动态链接器，一般来说动态链接器里面默认使用的路径是/etc/ld.so.preload，这里可以通过篡改动态连接器，修改文件路径，从而系统就会去新文件路径里面去找so文件加载），这里我们选择在受害机器的`/etx/ld.so.preload`文件中添加对应路径，如下：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-a3eeba5d1707f97adfddd78ab3d9eb34908c9cfd.png)
然后这里我们模拟一个叫1234567.py的进程（这个在编译上面.so文件的时候要把这个名称写入），该进程源码如下：就是发起socket连接101.1.1.1:43端口：
```php
import socket
​
​
def send\\_tcp\\_request(ip, port, message):
   try:
       \# 创建一个TCP/IP socket
       sock = socket.socket(socket.AF\\_INET, socket.SOCK\\_STREAM)
​
       \# 连接到指定的IP和端口
       sock.connect((ip, port))
       sock.settimeout(100)
​
       sock.sendall(message.encode())
​
       \# 接收服务器返回的数据
       received\\_data = sock.recv(1024)
       print("Received:", received\\_data.decode())
​
   except socket.error as e:
       print("Socket error:", e)
   finally:
       \# 关闭socket连接
       sock.close()
​
​
\# 测试代码
if \\_\\_name\\_\\_ == "\\_\\_main\\_\\_":
   ip = '101.1.1.1'  \# 要连接的IP地址
   port = 43  \# 要连接的端口号
   message = "Hello, server!"  \# 要发送的消息
   send\\_tcp\\_request(ip, port, message)
​
```
运行进程：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-7e7ef1aacf3e294b76ad598f40e562bcb79bba01.png)
### 现象
使用`netstat -pantu`,如下可以看到这里是发现了网络连接，但是没有pid和pname：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-9fe2db8d9158c0381c55dd74d07d518ad8d476c4.png)
使用ps命令，即使是在知道了被隐藏了进程的名称情况下，也查不到对应的进程：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-7478e5d6ad1c915367a3ae8a6feb838326680d25.png)
### 针对原理的排查方法
1、`echo $LD\_PRELOAD`（排查上述原理中第一种实现方式）
查看环境变量是否被劫持，如果存在劫持情况，`unset LD\_PRELOAD`，并且删除查出来的对应so文件
2、`cat /etc/ld.so.preload`文件，一般情况下是没有这个文件，或者是有这个文件但是文件内容为空，如果出现内容要重点排查；（排查上述原理中第二种实现方式）
如下图是被劫持的情况：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-06ef84366f117f67901a6cfc23fef98030de88b1.png)
3、排查系统的动态连接器是否被劫持，也就是最后不会去/etc/ld.so.preload加载，而是去指定的地方加载（排查上述原理中类似第三种实现方式，替换libc.so.6，但是仅仅是修改了里面默认的内置ld连接文件的位置（这点笔者没有去核实，该路径可能不是在libc.so.6里面的，是其他通用so里面，但是排查方式都是校验完整性和hash））
下图先找到命令的二进制文件，然后通过readelf读取其文件头中设置的链接器，然后判断链接器是否被改动
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-a5658c8c83d89df6bafea697cb4d7e638a6823a3.png)
通过时间判断是否动态连接器是否有问题：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-daa1aa08bb9644820b3133c56d642b6577740946.png)
通过rpm来校验是否有问题，这个就是通过hash去判断的，如果前面几个字符中没有出现5 就说明md5没有变动，如下图是未发现 ld-2.17.so文件发生了变动
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-eb343651454d805d46b6ecd5e2b768f60a9d5b6c.png)
### 快速排查的思路：
当发现有问题，进程被隐藏了，建议可以直接使用如下方法快速排查：
1、排查指定命令的动态链接库依赖，从上到下逐一排查so文件是否有问题
`ldd /usr/bin/ps` 如下：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-b84f235b360b7a9cfdd3be4b53e267f408ca1e4b.png)
2、直接使用 strace 命令 追踪 相关命令对文件的操作，ps进程执行的所有操作都会被记录，然后再去看是否存在可疑操作，打开了可疑的so文件等，从而判断问题出在哪个so文件
`strace -o result.txt -e trace=file -f ps`
效果如下：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-93d0315c39743ff2177dd7bb4c99f168f6c4d71d.png)
### 解除方法
1、如果是环境变量劫持LD\\_PRELOAD 那就清空LD\\_PRELOAD，删除劫持的恶意so文件；
unset LD\\_PRELOAD
2、如果是ld.so.preload劫持，删除 /etc/ld.so.preload里面的劫持内容，删除劫持的恶意so文件；
直接删除ld.so.preload文件也可以
3、如果链接器被篡改了，那就重下载，替换回来；
### 快速排查获取隐藏的pid方法：
1、以其人之道还治其人之身，劫持攻击者的劫持，那么程序就会调用我们的劫持，通过强行指定一个LD\\_PRELOAD环境变量 去执行对应的命令，如果我们怀疑readdir这个函数被劫持了，那么只要我们指定的LD\\_PRELOAD实现了readdir这个函数那么就能解除劫持，需要注意的是先要校验我们指定的so有没有被劫持，
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-bf10fc87ee4f499e20107607b011cc9ac4baaa17.png)
上面使用的是/lib64/libc.so.6，如下在其导出表里面可以看到其实现了readdir64，所以可以解除劫持
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-265537ac24a30bcc1d22524663f4d6003f4fd185.png)
2、上传一个busybox，busybox是使用静态连接编译而成的，不会被动态链接相关机制劫持；所以直接使用busybox，可以绕过动态链接机制，拿到pid和pname；
三、通过劫持shell环境，实现文件、进程名隐藏等操作
---------------------------
### 原理
修改或构造`/etc/profile.d/` 下sh文件，劫持环境变量，从而实现覆盖常见的命令，如：ps、ls、lsof等；
### 实现：
1、配置环境变量 shell脚本：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-7640579b5ab0eec6a816e3a9a98338e1971ecd3c.png)
重新登录用户之后；或者使用命令`source /etc/profile` 更新配置，使生效；
2、根目录下存在的myshell.sh文件被隐藏：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-d75d78b779fa8d55e396bd11e137ceb19dce5308.png)
执行ls命令效果：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-d6b243cb45486dad34c180cee726c2026f30fefd.png)
### 排查方法：
使用strace 调用执行ls，strace 里面调用ls属于非交互式shell命令执行，不会使用这个被劫持的shell环境
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-8bec19ea3a43c37117c55d60...