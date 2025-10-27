---
title: 企业级 Linux 挖矿实战揭秘，附应急专杀编写攻略
url: https://www.freebuf.com/articles/endpoint/421687.html
source: FreeBuf网络安全行业门户
date: 2025-02-15
fetch_date: 2025-10-06T20:36:21.463501
---

# 企业级 Linux 挖矿实战揭秘，附应急专杀编写攻略

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

企业级 Linux 挖矿实战揭秘，附应急专杀编写攻略

* ![]()
* 关注

* [终端安全](https://www.freebuf.com/articles/endpoint)

企业级 Linux 挖矿实战揭秘，附应急专杀编写攻略

2025-02-14 15:46:00

所属地 湖南省

## 文章源代码地址

https://github.com/mir1ce/MKT

## ****背景****

日常工作中分配到一个Linux横向的分析处置任务，经过一系列分析后，发现这个黑产组织整体的攻击路径都是比较单一，拿下一台主机后，就是疯狂套娃，在执行挖矿任务的同时，还不忘记对内网横向攻击，进一步的拓展他的战果，进行进一步的牟利。

下面可以这个图可以看到，黑产组织牟利的手段简单粗暴，无脑SSH，获取权限。本文具体日志分过程就不展开了，涉及敏感信息，主要是针对这个挖矿病毒的处理过程进行分析。整体来说还是比较简单，没有出现大量的比较难搞的问题。

日志分析这块儿，作者重点关注了以下日志：

```
/var/log/secure or /var/log/auth.log这个两个日志文件
cat /var/log/secure | grep Failed 查看登录失败的日志
cat /var/log/secure | grep Accepted 查看登录成功的日志
```

如果发现日志文件被删除了话，可以重点关注journalctl的日志，该日志只要系统不重启，就可以看到

![1739412423_67ad53c7eea7299fd0eb2.png!small?1739412427120](https://image.3001.net/images/20250213/1739412423_67ad53c7eea7299fd0eb2.png!small?1739412427120)

## ****处置分析****

上机的话，除了上述的基础日志分析外，重点是要找到落地文件，Linux没有Windows那么的方便，Windows可以使用everything使用图形化界面直接检索，在Linux操作系统中，我们重点是使用find命令去查看。作者日常在检索文件时常用以下命令

```
find / -executable -ctime -指定天数 -type f 2>/dev/null # 这串命令主要是检索指定天数内落地的可执行文件

# 如果时间线比较模糊，只知道是哪个区间落地的，可以使用以下命令进行检索
find / -executable -newermt 'xxxx-xx-xx' ! -newermt 'xxxx-xx-xx'
```

那么作者在实际场景中，很快就找到了这个可执行文件。

![1739412449_67ad53e1b664a3f7747c2.png!small?1739412452085](https://image.3001.net/images/20250213/1739412449_67ad53e1b664a3f7747c2.png!small?1739412452085)

直接查看网络连接，就能够很明显的看到一个名为crond的进程在外连，对于Linux比较熟悉的朋友，看到这个crond会觉得这是一个计划任务，这是没错的，但是计划任务这个进程存在外连就有问题了。

![1739412522_67ad542a5f6ba8f68d82e.png!small?1739412524522](https://image.3001.net/images/20250213/1739412522_67ad542a5f6ba8f68d82e.png!small?1739412524522)

那么我们就需要去定位，这个恶意进程的具体可执行文件位置。

```
ls -alth /proc/pid/exe
```

如下图所示，就能够比较明显的看到这个恶意进程的可执行文件所在的位置了，与我们使用find命令看到的文件相差无几。

![1739412556_67ad544ce0ccab03e66fc.png!small?1739412558509](https://image.3001.net/images/20250213/1739412556_67ad544ce0ccab03e66fc.png!small?1739412558509)

进入到相关目录后，看看这些落地文件的文件属性，能够进一步的知道他的作用

![1739412573_67ad545d7dbe27b16e22e.png!small?1739412575299](https://image.3001.net/images/20250213/1739412573_67ad545d7dbe27b16e22e.png!small?1739412575299)

其中cfg为一个配置文件，从配置来看是一个挖矿的配置文件

![1739412587_67ad546ba2dd5b6315b88.png!small?1739412589744](https://image.3001.net/images/20250213/1739412587_67ad546ba2dd5b6315b88.png!small?1739412589744)

cron为计划任务程序

![1739412598_67ad5476d7b5c0de63d18.png!small?1739412600428](https://image.3001.net/images/20250213/1739412598_67ad5476d7b5c0de63d18.png!small?1739412600428)

而run脚本则是用来调用h32和h64来隐藏真实挖矿程序run32/run64。根据脚本的代码来看，他这里是将挖矿进程名称隐藏成crond，也就是说攻击者可以通过h32/h64将进程隐藏为其他的名称，比如sshd等等。

![1739412643_67ad54a3cd01296d96e0a.png!small?1739412645788](https://image.3001.net/images/20250213/1739412643_67ad54a3cd01296d96e0a.png!small?1739412645788)

而autorun脚本，则是一个维权脚本，主要通过计划任务来达到权限维持的目的，从而达到利益持久化。

![1739412615_67ad5487c5430c8d01dd3.png!small?1739412618449](https://image.3001.net/images/20250213/1739412615_67ad5487c5430c8d01dd3.png!small?1739412618449)

根据以上文件信息基本上知道这个病毒的行为了。那么整体的处置也是比较简单的

1、先删除计划任务

2、终止恶意进程

3、删除恶意文件

那么手工的话，还是比较麻烦的，如果存在大批量的主机都存在呢？那么就需要编写专杀脚本，来辅助我们达到快速处置的目的。

那么这里以python为例，基本上Linux系统都支持python脚本运行（为啥不用bash，本机环境没跑起来？？？），专杀写完后，可以看到恶意外连和文件基本都被处理掉了，而且计划任务也已经删除。

![1739412670_67ad54bed8796fd4da6e8.png!small?1739412673712](https://image.3001.net/images/20250213/1739412670_67ad54bed8796fd4da6e8.png!small?1739412673712)

那么专杀编写的思维，主要还是根据人工处理的过程进行编写，首先我们要知道这个主机是否存在相关的现象或者是外连，如果存在的话，我们就需要程序进行到下一步，找到对应的可执行文件的位置以及相关的权限维持项，最后，通过程序来代替我们的人工操作的方式，来达到快速查杀的目的。

同时编写的程序的时候，我们需要和用户交互，毕竟程序可能会存在一些问题，为了保证在处置过程中，不影响我们正常程序的运行，在终止进程，删除文件以及修改系统配置的这个过程中，我们需要人工确认。

最后本次的恶意程序还是根据外连进行判断然后进行查杀，代码如下：

```
import os
import subprocess
import sys

# ANSI 转义序列
BLUE = "\033[34m"
RESET = "\033[0m"

def get_process_info(ip_address):
    try:
        netstat_output = subprocess.check_output(['netstat', '-anoplt'], stderr=subprocess.DEVNULL).decode()
        for line in netstat_output.splitlines():
            if ip_address in line:
                parts = line.split()
                net_pid = parts[6].split('/')[0]
                net_name = parts[6].split('/')[1]
                return net_pid, net_name
    except subprocess.CalledProcessError as e:
        print(f"{BLUE}[-] 获取进程信息时出错: {e}{RESET}")
    return None, None

def get_virus_file_path(pid):
    try:
        virus_file_path = os.readlink(f"/proc/{pid}/exe")
        return virus_file_path, os.path.dirname(virus_file_path)
    except Exception as e:
        print(f"{BLUE}[-]获取病毒文件路径时出错: {e}{RESET}")
    return None, None

def terminate_process(pid):
    choice = input(f"{BLUE}[?] 确认终止进程 {pid} 吗? (y/n): {RESET}")
    if choice.lower() == 'y':
        try:
            print(f"{BLUE}[!] 正在终止进程 {pid}...{RESET}")
            subprocess.call(['kill', '-9', str(pid)])
            subprocess.call(['sleep', '2'])
        except Exception as e:
            print(f"{BLUE}[-] 终止进程时出错: {e}{RESET}")
    else:
        print(f"{BLUE}[!] 已取消终止进程。{RESET}")

def check_crontab():
    try:
        print(f"{BLUE}[*] 检查全系统计划任务...{RESET}")
        cron_files = subprocess.check_output(['find', '/var/spool/cron', '-type', 'f'], stderr=subprocess.DEVNULL).decode().splitlines()

        for cron_file in cron_files:
            try:
                with open(cron_file, 'r') as f:
                    if '.cached/update' in f.read():
                        print(f"{BLUE}[!] 发现恶意计划任务: {cron_file}{RESET}")
            except Exception as e:
                print(f"{BLUE}[-] 读取计划任务文件 {cron_file} 时出错: {e}{RESET}")

        # 检查当前用户的 crontab
        try:
            user_crontab = subprocess.check_output(['crontab', '-l'], stderr=subprocess.DEVNULL).decode()
            if '.cached/update' in user_crontab:
                print(f"{BLUE}[!] 发现恶意计划任务，正在清理...{RESET}")
                new_crontab = '\n'.join(line for line in user_crontab.splitlines() if '.cached/update' not in line)
                subprocess.run(['crontab', '-'], input=new_crontab.encode())
        except subprocess.CalledProcessError:
            print(f"{BLUE}[-] 无法获取当前用户的 crontab，可能没有设置计划任务。{RESET}")
    except Exception as e:
        print(f"{BLUE}[-] 检查计划任务时出错: {e}{RESET}")

def delete_virus_file(virus_folder_path):
    if os.path.isdir(virus_folder_path):
        choice = input(f"{BLUE}[?] 确认删除病毒文件夹 {virus_folder_path}? (y/n): {RESET}")
        if choice.lower() == 'y':
            try:
                subprocess.call(['sudo', 'rm', '-rf', virus_folder_path])
                print(f"{BLUE}[*] 病毒文件夹已删除。{RESET}")
            except Exception as e:
                print(f"{BLUE}[-] 删除病毒文件夹时出错: {e}{RESET}")
    else:
        print(f"{BLUE}[-] 病毒文件不存在或已被移除{RESET}")

def main():
    ip_address = "172.86.83.142"
    net_pid, net_name = get_process_info(ip_address)

    if net_name and net_pid:
        print(f"{BLUE}[*] 发现可疑进程：{RESET}")
        print(f"{BLUE}[*] 进程名称: {net_name}{RESET}")
        print(f"{BLUE}[*] 进程ID: {net_pid}{RESET}")
    else:
        print(f"{BLUE}[-] 未发现与IP 172.86.83.142 相关的进程。{RESET}")
        sys.exit(1)

    virus_file_path, virus_folder_path = get_virus_file_path(net_pid)

    terminate_process(net_pid)
    check_crontab()
    delete_virus_file(virus_folder_path)

if __name__ == "__main__":
    main()
```

## ****总结****

以上案例主要入侵方式还是通过ssh爆破，尤其是遇到这种大批量被横向爆破的时候，可以分析病毒的特征针对性的编写专杀，根据个人习惯，适...