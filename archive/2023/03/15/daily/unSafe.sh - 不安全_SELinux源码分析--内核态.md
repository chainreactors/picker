---
title: SELinux源码分析--内核态
url: https://buaq.net/go-153433.html
source: unSafe.sh - 不安全
date: 2023-03-15
fetch_date: 2025-10-04T09:33:56.094018
---

# SELinux源码分析--内核态

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

![]()

SELinux源码分析--内核态

为了更加熟悉SELinux，针对这个安全机制的源码部分做了一些梳理，结合了官方的指南丰富了其中的源码实现细节。SELinux博大精深，这篇讲述该机制的内核部分实现，包括贯穿整个机制的两个核心——对系统
*2023-3-14 23:56:59
Author: [hurricane618.me(查看原文)](/jump-153433.htm)
阅读量:54
收藏*

---

为了更加熟悉SELinux，针对这个安全机制的源码部分做了一些梳理，结合了官方的指南丰富了其中的源码实现细节。SELinux博大精深，这篇讲述该机制的内核部分实现，包括贯穿整个机制的两个核心——对系统行为的检查以及标签的转换，以及比较核心的数据和接口。

首先是系统调用的入口函数里会存在一些hook点，比如这里的fork系统调用在`copy_process`中存在`security_task_alloc`，而这个是LSM的hook点位。SELinux的`hooks.c`中`selinux_hooks`结构体数组将SELinux相关的检查函数用`LSM_HOOK_INIT`设置到对应的hook点上。

在某个进程触发fork系统调用，到达安全检测点会跳转到`selinux_task_alloc`函数。该函数则是SELinux检测这个系统调用是否有权限执行。不同的系统调用有不同的检查逻辑，最终会调用的权限检查函数也有所不同，`fork`系统调用的检查函数是`avc_has_perm`。

`avc_has_perm`函数在`avc.c`中，用于检查系统调用是否被授权。其中有两个主要函数分别为`avc_has_perm_noaudit`和`avc_audit`，`avc_has_perm_noaudit`主要做具体的权限检查，而`avc_audit`则是记录avc日志信息。

`avc_has_perm_noaudit`首先给自己加上rcu的读锁，然后从已有的avc数据中查找是否缓存过，找得到就直接复制一份出来，没有找到则进入`avc_compute_av`计算av数据。根据av数据中的规则权限和请求的权限求得这次请求是否被允许，如果行为不允许，会进入`avc_denied`将这次的av结果更新。

`avc_compute_av`主要包含两个函数，其一是 `security_compute_av`，负责计算av数据；其二是`avc_insert`将计算到的avc数据插入缓存中。`security_compute_av`通过`ssid`和`tsid`在sidtab中搜索到`scontext`和`tcontext`进入到整个流程的核心函数`context_struct_compute_av`。

`avc_audit`会先利用`avc_audit_required`检查是否要记录audit日志，再调用`slow_avc_audit`函数构造具体的日志信息。`avc_audit_required`内部会先把请求的权限和取反后的允许权限做与操作，这样就能得到是否拒绝该行为。但这里会有另外一个位`avd->auditdeny`，如果该位被置为0，则这个拒绝行为不会被记录在audit日志中。

`unconfined_t`的进程执行了带着`secure_services_exec_t`的文件，触发标签转换，该文件执行成功变成进程后为`ext_gateway_t`。但要真正的执行转换还需要有三个权限：

（2）`allow unconfined_t secure_services_exec_t : file { execute read getattr };`进程执行文件的权限

首先从程序执行入口处进入`alloc_bprm`，这里会分配`linux_binprm`结构体，这个结构体记录了二进制执行程序的相关信息，包括核心的凭证和权限，参数，环境变量，文件名等内容。经过一系列的字符串拷贝和参数检查，进入到`bprm_execve`执行新的二进制程序。`bprm_execve`函数中有LSM的hook点位`security_bprm_creds_for_exec`，最终调用`selinux_bprm_creds_for_exec`。

`selinux_bprm_creds_for_exec`会调用`security_transition_sid`检查程序的标签转换内容，而这个函数只是`security_compute_sid`的一层封装，`security_compute_sid`中会确认是否需要计算新的sid。大概分成下面的流程：

从`selinux_bprm_creds_for_exec`中执行完`security_transition_sid`后，会有许多的`avc_has_perm`函数用来确认是否有相关的转换权限。首先会检查，是否有`execute_no_trans`权限，拥有该权限会直接返回，没有则继续检查`transition`、`entrypoint`等其他权限。

在前面两个阶段的检查结束后，会返回到`bprm_execve`中继续执行到`exec_binprm`，这个函数会调用`search_binary_handler`寻找二进制文件相应的处理器，并在处理其中执行它的`.load_binary`函数指针执行到`load_xxx_binary`中，这些函数最后的入口点在`begin_new_exec`。

`begin_new_exec`会在最后执行`security_bprm_committing_creds`和`security_bprm_committed_creds`这两个hook点对应，`selinux_bprm_committing_creds`和`selinux_bprm_committed_creds`。第一个函数用于进程初始化凭证，这里会检查是否有权限限制，第二个函数针对不会继承信号状态的进程做信号清除。

selinux\_avc->avc\_cache.slots是挂着avc\_node的list。而avc\_code的ae管理着基本的请求源和目标对象的id值，通过这两个id能找到对应的标签，avd则是记录请求的权限。

|  |  |
| --- | --- |
| ``` 1 ``` | ``` static const struct tree_descr selinux_files[] = { 		[SEL_LOAD] = {"load", &sel_load_ops, S_IRUSR|S_IWUSR}, 		[SEL_ENFORCE] = {"enforce", &sel_enforce_ops, S_IRUGO|S_IWUSR}, 		[SEL_CONTEXT] = {"context", &transaction_ops, S_IRUGO|S_IWUGO}, 		[SEL_ACCESS] = {"access", &transaction_ops, S_IRUGO|S_IWUGO}, 		[SEL_CREATE] = {"create", &transaction_ops, S_IRUGO|S_IWUGO}, 		[SEL_RELABEL] = {"relabel", &transaction_ops, S_IRUGO|S_IWUGO}, 		[SEL_USER] = {"user", &transaction_ops, S_IRUGO|S_IWUGO}, 		[SEL_POLICYVERS] = {"policyvers", &sel_policyvers_ops, S_IRUGO}, 		[SEL_COMMIT_BOOLS] = {"commit_pending_bools", &sel_commit_bools_ops, S_IWUSR}, 		[SEL_MLS] = {"mls", &sel_mls_ops, S_IRUGO}, 		[SEL_DISABLE] = {"disable", &sel_disable_ops, S_IWUSR}, 		[SEL_MEMBER] = {"member", &transaction_ops, S_IRUGO|S_IWUGO}, 		[SEL_CHECKREQPROT] = {"checkreqprot", &sel_checkreqprot_ops, S_IRUGO|S_IWUSR}, 		[SEL_REJECT_UNKNOWN] = {"reject_unknown", &sel_handle_unknown_ops, S_IRUGO}, 		[SEL_DENY_UNKNOWN] = {"deny_unknown", &sel_handle_unknown_ops, S_IRUGO}, 		[SEL_STATUS] = {"status", &sel_handle_status_ops, S_IRUGO}, 		[SEL_POLICY] = {"policy", &sel_policy_ops, S_IRUGO}, 		[SEL_VALIDATE_TRANS] = {"validatetrans", &sel_transition_ops, 					S_IWUGO}, 		 {""} 	}; ``` |

文章来源: https://hurricane618.me/2023/03/14/selinux-source-code-kernel-part/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)