---
title: 三星RKP内核完整性保护程序分析
url: https://mp.weixin.qq.com/s?__biz=Mzg4NjU1NDU4MA==&mid=2247483819&idx=1&sn=d74ac929c46c49e89ec0fb69842abb1b&chksm=cf96ab10f8e12206e4f718022e45aae3035726c93434966340fe58734895cf8562adb29d2c7b&scene=58&subscene=0#rd
source: kernsec
date: 2024-03-07
fetch_date: 2025-10-06T17:09:27.699198
---

# 三星RKP内核完整性保护程序分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4iaJia7Cvd3PDCM6QMDyJkP6ibiaT8KvkJ9khpF2dHd75BlBiaTZJUepSevD96ibmdCY84R3OLEPTy1ibj0c9ObaeYiboQ/0?wx_fmt=jpeg)

# 三星RKP内核完整性保护程序分析

wzt

kernsec

# **1 功能分析**

  本文主要以三星s6与s20二进制为样本进行分析。S6在2016年发布，这个版本由于有符号存在，可以大大降低逆向工程分析的难度，对于s20二进制只做部分参考分析。

## 1.1 **Cred保护**

  内核Struct cred数据结构保存了进程的权限凭证如uid/gid、capability等，是内核漏洞攻击程序进行权限提升必须要更改的数据结构，因此对cred数据结构的保护至关重要。三星rkp在el2限制了cred在el1为只读，当内核对cred进行正常写操作时，通过rkp接口调用el2层函数对其进行写操作。但rkp除了对cred做只读保护外， 还在cred数据结构引入了两个字段bp\_task和bp\_pgd对cred做完整性校验以及struct task\_security\_struct结构加入bp\_cred字段，防止被其他进程篡改。

```
struct cred {        atomic_t        usage;        kuid_t          uid;            /* real UID of the task */        kgid_t          gid;            /* real GID of the task */        kuid_t          suid;           /* saved UID of the task */...        union {                int non_rcu;                    /* Can we skip RCU deletion? */                struct rcu_head rcu;            /* RCU deletion hook */        };} __randomize_layout;
```

### 1.1.1 **反向task\_struct指针保护**

  当内核需要对cred进行创建和更新时，bp\_task和bp\_pgd就需要同步更新。

  对于bp\_task，内核在prepare\_ro\_creds函数里通过调用如下rkp接口：

```
drivers/uh/kdp.cstruct cred *prepare_ro_creds(struct cred *old, int kdp_cmd, u64 p){        memset((void *)&param_data, 0, sizeof(struct cred_param));        param_data.cred = &temp_old;        param_data.cred_ro = new_ro;        param_data.use_cnt_ptr = use_cnt_ptr;        param_data.sec_ptr = tsec;        param_data.type = kdp_cmd;        param_data.use_cnt = (u64)p;
        uh_call(UH_APP_KDP, PREPARE_RO_CRED, (u64)&param_data, (u64)current, (u64)&init_cred, (u64)&init_cred_kdp);}
```

  对应的el2层函数操作为：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4iaJia7Cvd3PDCM6QMDyJkP6ibiaT8KvkJ9kUibA0MfKrhXCe5Whxgz01KezAia7XRuQ0TESPF7x9jibaKl6iaLf3wN1ibg/640?wx_fmt=png&from=appmsg)

### 通过rkp\_assign\_creds对cred结构体的CRED\_BP\_TASK\_OFFSET偏移进行赋值。

### 1.1.2 **反向pgd指针保护**

  对于bp\_pgd，内核提供kdp\_assign\_pgd进行操作。

```
void kdp_assign_pgd(struct task_struct *p){        u64 pgd = (u64)(p->mm ? p->mm->pgd : swapper_pg_dir);
        uh_call(UH_APP_KDP, SET_CRED_PGD, (u64)p->cred, (u64)pgd, 0, 0);}
```

  对应的el2层函数操作为：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4iaJia7Cvd3PDCM6QMDyJkP6ibiaT8KvkJ9kZBcEQw4gW2cxsMGtgYcHpcUN3b5h9FgM2Q8su9eo7jShCR9ic34Ygzw/640?wx_fmt=png&from=appmsg)

### 通过rkp\_pgd\_assign对cred结构体的CRED\_BP\_PGD\_OFFSET偏移进行赋值。

### 1.1.3 **task\_security\_struct指针保护**

```
security/selinux/hooks.cstatic void cred_init_security(void){        struct cred *cred = (struct cred *) current->real_cred;        struct task_security_struct *tsec;
#ifdef CONFIG_KDP_CRED        tsec = &init_sec;        tsec->bp_cred = cred;        // is not support 5.4 upper version, so we added        cred->security = tsec;#else        tsec = selinux_cred(cred);#endif        tsec->osid = tsec->sid = SECINITSID_KERNEL;}
```

  内核调用cred\_init\_security对init进程进行初始化，后续子进程将会继承struct task\_security\_struct指针。当cred需要更改时同样使用prepare\_ro\_creds进行处理。

```
drivers/uh/kdp.cstruct cred *prepare_ro_creds(struct cred *old, int kdp_cmd, u64 p){        memset((void *)&param_data, 0, sizeof(struct cred_param));        param_data.cred = &temp_old;        param_data.cred_ro = new_ro;        param_data.use_cnt_ptr = use_cnt_ptr;        param_data.sec_ptr = tsec;        param_data.type = kdp_cmd;        param_data.use_cnt = (u64)p;
        uh_call(UH_APP_KDP, PREPARE_RO_CRED, (u64)&param_data, (u64)current, (u64)&init_cred, (u64)&init_cred_kdp);}
```

 对应的el2函数接口为：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4iaJia7Cvd3PDCM6QMDyJkP6ibiaT8KvkJ9kNicgibG64XicU1k6vhvVzAo4ZUQpABnV571kTkHKsjMnluKfeua3EKHUw/640?wx_fmt=png&from=appmsg)

### 通过rkp\_assign\_secptr对cred结构体的CRED\_SECURITY\_OFFSET偏移进行赋值。

Rkp加入这三个指针保护的目的是做完整性检查，在LSM框架里调用hook钩子之前加入判断语句：

```
security/security.c#define call_void_hook(FUNC, ...)                               \        do {                                                    \                struct security_hook_list *P;                   \                                                                \                if(security_integrity_current()) break;         \                hlist_for_each_entry(P, &security_hook_heads.FUNC, list) \                        P->hook.FUNC(__VA_ARGS__);              \        } while (0)
#define call_int_hook(FUNC, IRC, ...) ({                        \        int RC = IRC;                                           \        do {                                                    \                struct security_hook_list *P;                   \                                                                \                RC = security_integrity_current();              \                if (RC != 0)                                    \                        break;                                  \                hlist_for_each_entry(P, &security_hook_heads.FUNC, list) { \                        RC = P->hook.FUNC(__VA_ARGS__);         \                        if (RC != 0)                            \                                break;                          \                }                                               \        } while (0);                                            \        RC;                                                     \})
drivers/uh/kdp.cint security_integrity_current(void){        const struct cred *cur_cred = current_cred();
        rcu_read_lock();        if (kdp_enable &&                        (is_kdp_invalid_cred_sp((u64)cur_cred, (u64)cur_cred->security)                        || cmp_sec_integrity(cur_cred, current->mm)#ifdef CONFIG_KDP_NS                        || cmp_ns_integrity())) {#else                        )) {#endif                rcu_read_unlock();                panic("KDP CRED PROTECTION VIOLATION\n");        }        rcu_read_unlock();        return 0;}
static inline bool is_kdp_invalid_cred_sp(u64 cred, u64 sec_ptr){        if ((u64)tsec->bp_cred != cred) {                printk(KERN_ERR, "[KDP] %s: tesc->bp_cred: %lx, cred: %lx\n",                                __func__, (u64)tsec->bp_cred, cred);                return true;        }
        return false;}
```

 cmp\_sec\_integrity用来验证cred数据结构的bp\_task和bp\_pgd指针是否被篡改。

## 1.2 **Namespace保护**

   Rkp对Namespace的保护目前仅局限于mount namespace，对其保护的方式为验证nsproxy->mnt\_ns->root字段是否被篡改，同时还对mount挂载点进行了只读保护，不能挂载新的分区以及二进制程序必须从可信的mount点启动。

 首先在vfsmount和mount数据结构中都加入了互相指向的backup指针：

```
include/linux/mount.hstruct vfsmount {        struct dentry *mnt_root;        /* root of the mounted tree */        struct super_block *mnt_sb;     /* pointer to superblock */        int mnt_flags;        ANDROID_KABI_RESERVE(1);        ANDROID_KABI_RESERVE(2);        ANDROID_KABI_RESERVE(3);        ANDROID_KABI_RESERVE(4);        void *data;} __randomize_layout;
#ifdef CONFIG_KDP_NSstruct kdp_vfsmount {        struct vfsmount mnt;        struct mount *bp_mount; /* pointer to mount*/};#endif
fs/mount.hstruct mount {        struct hlist_node mnt_hash;        struct hlist_head mnt_stuck_children;} __randomize_layout;
#ifdef CONFIG_KDP_NSstruct kdp_mount {        struct mount mount;        struct vfsmount *mnt;};#endif
```

  内核通过调用kdp\_mnt\_alloc\_vfsmount请求el2进行指针设置。

```
int kdp_mnt_alloc_vfsmount(struct mount *mnt){        uh_call(UH_APP_KDP, ALLOC_VFSMOUNT, (u64)vfsmnt, (u64)mnt, 0, 0);
        return 0;}
```

  对应的el2函数操作为：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/4iaJia7Cvd3PDCM6QMDyJkP6ibiaT8KvkJ9k9YB2UZficAL30Bn56vlgNicDkBa0aAo7Npm8yGic4KCefHejod1Aak4jg/640?wx_fmt=png&from=appmsg)

## El2通过rkp\_init\_ns对mount结构的BPMNT\_VFSMNT\_OFFSET偏移进行赋值。

当LSM框架的hook钩子执行时，会调用cmp\_ns\_integrity进行指针完整性检查：

```
static unsigned int cmp_ns_integrity(void){        root = (struct kdp_mount *)current->nsproxy->mnt_ns->root;        if (root != (struct kdp_mount *)((struct kdp_vfsmount *)root->mnt)->bp_mount) {                printk(KERN_ERR "[KDP] NameSpace Mismatch %lx != %lx\n nsp: 0x%lx, mnt_ns: 0x%lx\n",                                root, ((struct kdp_vf...