---
title: 【云安全系列】让Seccomp“动”起来­­–SeccompNotify
url: https://www.secpulse.com/archives/190569.html
source: 安全脉搏
date: 2022-11-08
fetch_date: 2025-10-03T21:54:54.980868
---

# 【云安全系列】让Seccomp“动”起来­­–SeccompNotify

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

# 【云安全系列】让Seccomp“动”起来­­–SeccompNotify

[漏洞](https://www.secpulse.com/archives/category/vul)

[Further\_eye](https://www.secpulse.com/newpage/author?author_id=9241)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2022-11-07

8,613

**简介**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190569-1667802278.png)

根据我们上一篇[《Seccomp -云安全syscall防护利器》](http://mp.weixin.qq.com/s?__biz=Mzg2NjgzNjA5NQ==&mid=2247515073&idx=1&sn=1c41a8b0807cc1363c683e9c15914bf1&chksm=ce4630d1f931b9c7950694337f977e4a823d17c8ce332cfa6b8a04554bf9752863dd9041093e&scene=21#wechat_redirect)的分析，我们可以知道 Seccomp-BPF 模式无论是在可扩展性上还是开发简易性上都得到了大幅的改善。尽管如此，Seccomp-BPF 却存在一个致命的缺陷，其对应的生效方式不适合动态的场景。具体来说，无论 syscall 最后是成功还是失败，一旦一个 Seccomp filter 成功加载到内核后，对应 syscall 的规则也就固定下来了。接下来不管在什么场景下，用户都无法再次根据具体的情况，去修改对应的 syscall 规则。这就意味着**用户从一开始，就需要确定好对应进程所有的系统调用权限，一旦出现偏差，就需要重新修改、编译代码，这其实无形中增加了用户的试错成本。**

**SeccompNotify**

为此，在 5.0（2019年3月4日）版本内核又加入了 seccomp-unotify 机制。相较于 Seccomp-BPF 模式下，系统调用的裁决需要由 filter 程序自己完成，seccomp-unotify 机制能够将裁决权转移给另一个用户态进程。为了方便理解，接下来我们将需要加载 Seccomp filter 程序的进程叫做 target，接收到 target 通知的进程叫做 supervisor。在这个模式下，supervisor 不仅可以对是否允许系统调用做出判断，它还可以替代 target 进程去执行这个系统调用的行为。这无疑再一次扩展了 Seccomp 的使用范围。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190569-1667802279.png)

接下来我们通过一个简单的示例来了解 SeccompNotify 的具体流程，target 进程如下：

```
int main(int argc, char **argv){    ...    #创建filter    struct sock_filter filter[] = {        BPF_STMT(BPF_LD+BPF_W+BPF_ABS, (offsetof(struct seccomp_data, nr))),

        BPF_JUMP(BPF_JMP+BPF_JEQ+BPF_K, __NR_mkdir, 0, 1),        BPF_STMT(BPF_RET+BPF_K, SECCOMP_RET_USER_NOTIF),

        BPF_STMT(BPF_RET+BPF_K, SECCOMP_RET_ALLOW),   };

    ...    #初始化notify fd    notifyfd = syscall(__NR_seccomp, SECCOMP_SET_MODE_FILTER,            SECCOMP_FILTER_FLAG_NEW_LISTENER, &prog);    if (notifyfd < 0) {        printf("fail to create seccomp: %s\n", strerror(errno));        exit(-1);   }

    printf("tid: %d, notify fd: %d\n", syscall(SYS_gettid), notifyfd);    #触发mkdir    fd = mkdir(argv[1], O_CREAT|O_RDWR);    ...

    return 0;}
```

在 target 进程内，我们首先定义了一个 socket filter, 这个 filter 允许除了 mkdir 之外的所有系统调用，mkdir 需要通过 Seccomp Notify 的方式由 supervisor 去判决是否允许执行。接着，通过 Seccomp 系统调用的方式来加载 filter，将对应的 tid 和 fd 打印出来。最后执行 mkdir 命令，触发 mkdir 系统调用，进程进入阻塞状态，等待内核返回。

对于 supervisor 程序：

```
static void supervisor_process_notifications(int notifyfd){    ...    #创建seccomp    if (syscall(SYS_seccomp, SECCOMP_GET_NOTIF_SIZES, 0, &sizes) == -1) {        ...   }

    ...    #从notify df中轮询事件    if (ioctl(notifyfd, SECCOMP_IOCTL_NOTIF_RECV, req) == -1) {       ...   }

    ...    # 判断mkdir的参数是否是 add    if (strlen(path) == strlen("add") &&        strncmp(path, "add", strlen("add")) == 0)   {        printf("change name for add dir\n");        if (access("change", 0) == -1){            mkdir(path, O_CREAT|O_RDWR);       }   }    resp->error = 0;    resp->flags = SECCOMP_USER_NOTIF_FLAG_CONTINUE;

    resp->id = req->id;    # 发送结果给内核    if (ioctl(notifyfd, SECCOMP_IOCTL_NOTIF_SEND, resp) == -1) {        ...   }}

int main(int argc, char **argv){    ...    pid = atoi(argv[1]);    targetfd = atoi(argv[2]);    printf("PID: %d, TARGET FD: %d\n", pid, targetfd);    #获取target fd对应的pid fd    pidfd = syscall(SYS_pidfd_open, pid, 0);    assert(pidfd >= 0);    printf("PIDFD: %d\n", pidfd);    #根据target fd获取监听的notify fd    notifyfd = syscall(SYS_pidfd_getpid, pidfd, targetfd, 0);    assert(notifyfd >= 0);    printf("NOTIFY FD: %d\n", notifyfd);    #监视target进程    supervisor_process_notifications(notifyfd);

    return 0;}
```

首先，supervisor 进程通过 pidfd\_getpid 获取到 target 进程的 seccomp fd，并且从 fd 中不断轮询 target 内的 seccomp notify 事件。然后，再从 /proc/{pid}/mem 文件内获取 mkdir 系统调用所引用的参数，也就是创建的文件夹名称。supervisor 规定，如果创建文件夹的名称为 add，则会自动将该文件夹名称修改成 change，并且将结果返回给内核，从而达到约束 target 进程的目的。

执行 target 进程：

```
root@localhost:~/CLionProjects/seccomp# ./target /tmp/aa
tid: 8005, notify fd: 7
```

可以看到 target 进程进入了阻塞状态，并且对应的 tid 和 notify id 分别为 8005和7

，然后我们在另一个中断终端内执行 supervisor 进程：

```
root@localhost:~/CLionProjects/seccomp# ./supervisor 8005 7
PID: 8005, TARGET FD: 7
PIDFD: 7NOTIFY FD: 5
Got notification for PID: 8005
SYSCALL: 83
open path: /tmp/aa
```

查看 /tmp 目录可以看到文件夹被成功创建了：

```
root@localhost:/tmp# ls -l /tmp/
总用量 5124
d--x------ 2 root root   4096 10月 14 15:47 aa
drwxr-xr-x 2 root root   4096 10月 14 11:32 gproc
-rw-r--r-- 1 root root     0 10月 14 11:32 heartalive.lock
```

但是如果我们将创建的文件夹名称修改为 add，情况又会是什么样呢？

```
root@localhost:~/CLionProjects/seccomp# ./target add
tid: 8773, notify fd: 7
```

target 进程依旧是在阻塞状态，然后运行 supervisor：

[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/11/image.png "image.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/11/image.png)

通过日志可以看到，supervisor 捕获到 target 的文件夹名称为 add 后，执行了修改 add 文件夹的操作，遍历当前目录，查看是否成功修改：

[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/11/image1.png "image1.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/11/image1.png)

所以这里的话，supervisor 进程就通过截获了target进程的syscall，从而达到安全管控的目的了。

**使用场景和注意事项**

就目前而言，SeccompNotify 的运用场景主要有以下三种：

1. supervisor 直接拒绝 target 的 syscall 请求。
2. 在 supervisor 内执行其他的操作，并且向内核反馈对应的结果（也就是高特权进程替换低特权进程的操作）。
3. 允许 target 执行对应 syscall。

   但需要注意的是第三种情况，如果执行的 syscall 携带了引用指针，那么就可能存在多个进程同时陷入阻塞状态，从而导致 race-condition的 情况。所以大家在使用的时候请务必小心谨慎。

**总结**

Seccomp 作为最早一批系统级安全防护机制，从最开始只支持4个 syscall 的保护，逐步发展到 300+syscall 管控，再到现在可以在用户态定义的动态管控。我们可以察觉系统安全正在逐步由小部分的内核开发维护人员，向着更加普遍且大众的开发者贴近。本文通过实际编码的方式，着重介绍了 SeccompNotify 在进程中通过将裁决移交给第三方进程，从而达到约束 target 进程的功能。除此之外，我们还概括了目前 SeccompNotify 主要使用的场景和注意事项，当然**除了在进程中，SeccompNotify 在容器环境也能够实现动态生效的功能，而且还在不断的发展之中，****深信服创新研究院云安全研究团队将对此持续探索****。**

**参考链接**

1. ht...