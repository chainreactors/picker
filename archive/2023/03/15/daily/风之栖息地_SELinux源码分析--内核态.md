---
title: SELinux源码分析--内核态
url: https://hurricane618.me/2023/03/14/selinux-source-code-kernel-part/
source: 风之栖息地
date: 2023-03-15
fetch_date: 2025-10-04T09:36:02.195134
---

# SELinux源码分析--内核态



[风之栖息地](/)

SELinux源码分析--内核态

[风之栖息地](/)

# SELinux源码分析--内核态

SELinux
源码分析

字数统计: 2.6k阅读时长: 10 min


2023/03/14




Share

* 
* 
* 
* 
* 

![](/assets/loading.svg)

为了更加熟悉SELinux，针对这个安全机制的源码部分做了一些梳理，结合了官方的指南丰富了其中的源码实现细节。SELinux博大精深，这篇讲述该机制的内核部分实现，包括贯穿整个机制的两个核心——对系统行为的检查以及标签的转换，以及比较核心的数据和接口。

备注：我的源码分析中忽略了mls机制，在一些检查点中针对mls有额外的处理。

## 核心流程一：对系统调用行为的鉴权

我这里拿`fork`系统调用为例子🌰，整个调用过程核心流程如下图所示：

![](/2023/03/14/selinux-source-code-kernel-part/selinux行为鉴权.png)

首先是系统调用的入口函数里会存在一些hook点，比如这里的fork系统调用在`copy_process`中存在`security_task_alloc`，而这个是LSM的hook点位。SELinux的`hooks.c`中`selinux_hooks`结构体数组将SELinux相关的检查函数用`LSM_HOOK_INIT`设置到对应的hook点上。

在某个进程触发fork系统调用，到达安全检测点会跳转到`selinux_task_alloc`函数。该函数则是SELinux检测这个系统调用是否有权限执行。不同的系统调用有不同的检查逻辑，最终会调用的权限检查函数也有所不同，`fork`系统调用的检查函数是`avc_has_perm`。

`avc_has_perm`函数在`avc.c`中，用于检查系统调用是否被授权。其中有两个主要函数分别为`avc_has_perm_noaudit`和`avc_audit`，`avc_has_perm_noaudit`主要做具体的权限检查，而`avc_audit`则是记录avc日志信息。

`avc_has_perm_noaudit`首先给自己加上rcu的读锁，然后从已有的avc数据中查找是否缓存过，找得到就直接复制一份出来，没有找到则进入`avc_compute_av`计算av数据。根据av数据中的规则权限和请求的权限求得这次请求是否被允许，如果行为不允许，会进入`avc_denied`将这次的av结果更新。

`avc_compute_av`主要包含两个函数，其一是 `security_compute_av`，负责计算av数据；其二是`avc_insert`将计算到的avc数据插入缓存中。`security_compute_av`通过`ssid`和`tsid`在sidtab中搜索到`scontext`和`tcontext`进入到整个流程的核心函数`context_struct_compute_av`。

`context_struct_compute_av`函数含有多个检查访问是否合法的步骤。

1. avd内容的初始化；
2. 遍历检查对象类和权限，并根据节点的类型（AVTAB\_ALLOWED、AVTAB\_AUDITALLOW、AVTAB\_AUDITDENY、AVTAB\_XPERMS）将数据整合进avd中；
3. `cond_compute_av`检查是否有条件语句规则包含在这次的访问判断中，如果存在则会对权限做修改；
4. 通过`constraint_expr_eval`查看是否存在额外约束，根据额外约束移除权限；
5. 如果进程标签转换正在执行，需要检测是否有`transition`或`dyntransition`权限，是否有角色的改变。
6. 检查是否有`typebounds`规则约束应用在这次访问中，根据额外约束修正权限
7. 这些结果都保存在avd数据中

`avc_audit`会先利用`avc_audit_required`检查是否要记录audit日志，再调用`slow_avc_audit`函数构造具体的日志信息。`avc_audit_required`内部会先把请求的权限和取反后的允许权限做与操作，这样就能得到是否拒绝该行为。但这里会有另外一个位`avd->auditdeny`，如果该位被置为0，则这个拒绝行为不会被记录在audit日志中。

当整个鉴权过程结束之后会从`selinux_task_alloc`返回，一路返回到fork自身的`copy_process`中继续系统调用执行。

## 核心流程二：进程的标签转换

SELinux中存在一种规则type\_transition，让一个带着标签的进程，执行另外一个带着标签的文件时，发生标签转换，从原有的标签转换成其他设置的标签。

`type_transition unconfined_t secure_services_exec_t : process ext_gateway_t;`

`unconfined_t`的进程执行了带着`secure_services_exec_t`的文件，触发标签转换，该文件执行成功变成进程后为`ext_gateway_t`。但要真正的执行转换还需要有三个权限：

（1）`allow unconfined_t ext_gateway_t : process transition;`标签间的转换权限

（2）`allow unconfined_t secure_services_exec_t : file { execute read getattr };`进程执行文件的权限

（3）`allow ext_gateway_t secure_services_exec_t : file entrypoint;`转换标签必须有进入点权限

因为是要拉起另外一个进程所以入口都是在do\_execveat\_common中。

![](/2023/03/14/selinux-source-code-kernel-part/selinux标签转换.png)

**整个过程分为三个阶段**

第一个阶段是检查进程标签转换的标签内容

首先从程序执行入口处进入`alloc_bprm`，这里会分配`linux_binprm`结构体，这个结构体记录了二进制执行程序的相关信息，包括核心的凭证和权限，参数，环境变量，文件名等内容。经过一系列的字符串拷贝和参数检查，进入到`bprm_execve`执行新的二进制程序。`bprm_execve`函数中有LSM的hook点位`security_bprm_creds_for_exec`，最终调用`selinux_bprm_creds_for_exec`。

`selinux_bprm_creds_for_exec`会调用`security_transition_sid`检查程序的标签转换内容，而这个函数只是`security_compute_sid`的一层封装，`security_compute_sid`中会确认是否需要计算新的sid。大概分成下面的流程：

1. 搜索sidtab中的ssid和tsid，获得`scontext`和`tcontext`；
2. 设置用户id、角色id和标签类型；
3. 检查是否有`type_transition`规则在av数据中或者条件av数据中
4. 如果存在标签转换，检查是否有`role_transition`角色转换，并设置好角色
5. 检查新的标签内容是否合法，不合法内容将会被日志记录；
6. 调用`sidtab_context_to_sid`获得新标签的sid，并在sidtab中更新

第二个阶段检查进程是否有转换等权限

从`selinux_bprm_creds_for_exec`中执行完`security_transition_sid`后，会有许多的`avc_has_perm`函数用来确认是否有相关的转换权限。首先会检查，是否有`execute_no_trans`权限，拥有该权限会直接返回，没有则继续检查`transition`、`entrypoint`等其他权限。

第三个阶段检查执行二进制的相关权限

在前面两个阶段的检查结束后，会返回到`bprm_execve`中继续执行到`exec_binprm`，这个函数会调用`search_binary_handler`寻找二进制文件相应的处理器，并在处理其中执行它的`.load_binary`函数指针执行到`load_xxx_binary`中，这些函数最后的入口点在`begin_new_exec`。

`begin_new_exec`会在最后执行`security_bprm_committing_creds`和`security_bprm_committed_creds`这两个hook点对应，`selinux_bprm_committing_creds`和`selinux_bprm_committed_creds`。第一个函数用于进程初始化凭证，这里会检查是否有权限限制，第二个函数针对不会继承信号状态的进程做信号清除。

## 核心数据和接口

### SELinux状态信息的全局变量

`struct selinux_state selinux_state;`

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 ``` | ``` struct selinux_state { #ifdef CONFIG_SECURITY_SELINUX_DISABLE 	bool disabled; #endif #ifdef CONFIG_SECURITY_SELINUX_DEVELOP 	bool enforcing; #endif 	bool checkreqprot; 	bool initialized; 	bool policycap[__POLICYDB_CAP_MAX];  	struct page *status_page; 	struct mutex status_lock;  	struct selinux_avc *avc; 	struct selinux_policy __rcu *policy; 	struct mutex policy_mutex; } __randomize_layout; ``` |

一个记录SELinux的全局状态的结构体，里面包括了SELinux的开启状态，是否为enforcing模式，是否初始化，规则指针，avc记录缓存指针等信息。

### hooks挂载函数表

hooks挂载都在hooks.c文件中，把SELinux的检查函数挂载在不同系统调用的安全函数hook点中。

`static struct security_hook_list selinux_hooks[] __lsm_ro_after_init`

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` ... LSM_HOOK_INIT(inode_create, selinux_inode_create), LSM_HOOK_INIT(inode_link, selinux_inode_link), LSM_HOOK_INIT(inode_unlink, selinux_inode_unlink), LSM_HOOK_INIT(inode_symlink, selinux_inode_symlink), ... ``` |

### av数据管理

管理av数据的相关结构体

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 ``` | ``` struct selinux_avc { 	unsigned int avc_cache_threshold; 	struct avc_cache avc_cache; };  struct avc_cache { 	struct hlist_head	slots[AVC_CACHE_SLOTS]; /* head for avc_node->list */ 	spinlock_t		slots_lock[AVC_CACHE_SLOTS]; /* lock for writes */ 	atomic_t		lru_hint;	/* LRU hint for reclaim scan */ 	atomic_t		active_nodes; 	u32			latest_notif;	/* latest revocation notification */ };  struct avc_node { 	struct avc_entry	ae; 	struct hlist_node	list; /* anchored in avc_cache->slots[i] */ 	struct rcu_head		rhead; };  struct avc_entry { 	u32			ssid; 	u32			tsid; 	u16			tclass; 	struct av_decision	avd; 	struct avc_xperms_node	*xp_node; };  struct av_decision { 	u32 allowed; 	u32 auditallow; 	u32 auditdeny; 	u32 seqno; 	u32 flags; }; ``` |

selinux\_avc->avc\_cache.slots是挂着avc\_node的list。而avc\_code的ae管理着基本的请求源和目标对象的id值，通过这两个id能找到对应的标签，avd则是记录请求的权限。

### 策略数据管理

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 ``` | ``` /* The policy database */ struct policydb { 	int mls_enabled;  	/* symbol tables */ 	struct symtab symtab[SYM_NUM]; #define p_commons symtab[SYM_COMMONS] #define p_classes symtab[SYM_CLASSES] #define p_roles symtab[SYM_ROLES] #define p_types symtab[SYM_TYPES] #define p_users symtab[SYM_USERS] #define p_bools symtab[SYM_BOOLS] #define p_levels symtab[SYM_LEVELS] #define p_cats symtab[SYM_CATS]  	/* symbol names indexed by (value - 1) */ 	char		**sym_val_to_name[SYM_NUM];  	/* class, role, and user attributes indexed by (value - 1) */ 	struct class_datum **class_val_to_struct; 	struct role_datum **role_val_to_struct; 	struct user_datum **user_val_to_struct; 	struct type_datum **type_val_to_struct;  	/* type enforcement access vectors and transitions */ 	struct avtab te_avtab;  	/* role transitions */ 	struct hashtab role_tr;  	/* file transitions with the last path component */ 	/* quickly exclude lookups when parent ttype has no rules */ 	struct ebitmap filename_trans_ttypes; 	/* actual set of filename_trans rules */ 	struct hashtab filename_trans; 	/* only used if policyvers < POLICYDB_VERSION_COMP_FTRANS */ 	u32 compat_filename_trans_count;  	/* bools indexed by (value - 1) */ 	struct cond_bool_datum **bool_val_to_struct; 	/* type enforcement conditional access vectors and transitions */ 	struct avtab te_cond_avtab; 	/* array indexing te_cond_avtab by conditional */ 	struct cond_node *cond_list; 	u32 cond_list_len;  	/* role allows */ 	struct role_allow *role_allow;  	/* security contexts of initial SIDs, unlabeled file systems, 	   TCP or UDP port numbers, network interfaces and nodes */ 	struct ocontext *ocontexts[OCON_NUM];  	/* security contexts for files in filesystems that cannot support 	   a persistent label mapping or use another 	   fixed labeling behav...