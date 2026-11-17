---
title: 11 个运维工具，涉及新服务器从到手到对外服务
url: https://mp.weixin.qq.com/s/o9uxXRIB6PFUCiHzCUhRgw
source: Doonsec's feed
date: 2026-11-16
fetch_date: 2026-11-17T09:54:44.322858
---

# 11 个运维工具，涉及新服务器从到手到对外服务

# 11 个运维工具，涉及新服务器从到手到对外服务

原创

wljslmz瑞哥
wljslmz瑞哥

网络技术联盟站

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

新服务器从到手到对外服务，要过的关卡很固定：分区怎么规划、配额留多少、内核参数调什么值、服务怎么注册成自启、数据盘怎么稳定挂载、SSH 怎么收紧、防火墙敢不敢设成默认 DROP。资料都查得到，但分散、版本不一，写错一个字母就得回机房救机器。

V2.15.0 把这条链路上的 11 个高频动作做成了在线工具：浏览器本地计算与生成，无需登录，不上传任何服务器输出。

```
https://tool.geek.cab/?category=ops
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dibzmm9niba05wnPjlKZdBnO2eibhIRQWibvOeQV01c2jKLncsd8P43tpCgIs7FH1sGFylk5rfDCEg8vGU8ibvibMLDxIrprNkxwJ1pXwwVwnRD2o/640?wx_fmt=png&from=appmsg)

完整清单如下。

## 存储与容量

### LVM 规划计算器

![](https://mmbiz.qpic.cn/mmbiz_png/Dibzmm9niba05QeBM8TYv4GO0XX4n2dN3NT1ic9ibXZra0cAD60CQJMb4MSCjUjenIQjvrGYFxj6uxicCzbwPru4icosFf9eRhqcA3HRiaVXKhYIW4/640?wx_fmt=png&from=appmsg)

* 输入磁盘数、单盘容量与 PE 大小，给出卷组真实可用容量：PE 向下取整、元数据开销、PE 总数与剩余零头全部列明
* 按 root、var、home、swap、数据盘逐项分配，实时显示已分配、剩余与使用率，超额时明确提示还需缩减多少
* 自动校验逻辑卷重名、容量小于一个 PE、PE 过小导致单 LV 超过 65534 个 extent 上限
* 一键生成 `pvcreate`、`vgcreate`、`lvcreate`、`mkfs`、`mkswap` 命令序列，内置三套预设与 PE 对照表（4MB PE 下单 LV 上限约 256GB）

![](https://mmbiz.qpic.cn/mmbiz_png/Dibzmm9niba059TyFIyibZ9oew2tfr23SqCskRYEUUOIk1VaAq3tIgLceyh7ic3qiajycksWcztkGzo0WoUwu4ic674rk25Niax0w6tgoQsfKkBxdQ/640?wx_fmt=png&from=appmsg)

### 文件系统配额估算

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dibzmm9niba07oewO8cH1atOPu7ic3w2xO8HicibpzZyjDIY4j6n6hxqUsriavt9u7bEuR4jrYhRYMdzjLibJkMSGWXaO51r7rlx9SJWRmqdXehRR0/640?wx_fmt=png&from=appmsg)

* 按用户数、单用户配额、预留比例、文件数与平均文件大小，算出物理容量、配额总量与预计 inode 数
* 容量与 inode 双线并行测算，直接指出哪条先到顶——`df -h` 还有空间、`df -i` 已满这类故障，一眼定位
* 支持手动填入 `df -i` 的实际上限；对小于 16KB 的小文件、inode 使用率超 80%、预留为 0 单独告警
* 按文件系统生成命令：ext4 出 `mkfs.ext4 -i`、`quotacheck`、`setquota`、`repquota`；xfs 出 `mkfs.xfs -i maxpct`、`xfs_quota`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dibzmm9niba04gPv0H4Mjsd7s6Y49XFWSuVchKThOn58ibibx5XWSvySB5FYYqVtOiasxaGrZumaPSUIniaHZjPA92Erbichia9F2trCW5kBxIr1bpE/640?wx_fmt=png&from=appmsg)

### 磁盘水位预估

![](https://mmbiz.qpic.cn/mmbiz_png/Dibzmm9niba04AheMuOKa2mWFgaSCXzOeIbO0iacGnkNqGGcVHJrhUDI8mVYtR14o9S2CjyZSb7Ty2bIlGPtbWibWUYdJN0WWtWxfPdZt8oLAec/640?wx_fmt=png&from=appmsg)

* 输入总容量、已用量与增长率（GB/天、GB/月、%/天、%/月），算出距 70/80/85/90 各档水位的剩余天数与写满时间，进度条同时标出当前水位与阈值
* 填写基准日期即给出触线日期，并把增速换算成月增、年增用量
* 反向预算：按"撑住 180 天不越阈值"反推每日增长上限、届时所需容量与扩容差额
* 附 `df -hT`、`du -sh`、`du -h -d 1`、`lsof +L1` 的采集排查命令与可写入定时任务的水位告警脚本

![](https://mmbiz.qpic.cn/mmbiz_png/Dibzmm9niba06dNvbgty7gzSCvnXDv8Okuys8UNEkwMdtqk6xGgqFX8LgfutBhmuiarD2CHibzxkBicGFu6cR149ZtJQvaswF9nvvLrWWrLBeuicU/640?wx_fmt=png&from=appmsg)

## 系统配置

### Umask 与文件权限计算器

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dibzmm9niba07zRDOd5Niayg6wJml1UuW0MziaQQSR8wZXVvjplGwjbzdbMEulA4pjDjI8rdkETaMsBa5eqOqrocicmfbKNvENVhbEfr5xYAibfGg/640?wx_fmt=png&from=appmsg)

* 输入 umask 即得新建文件（666 − umask）与新建目录（777 − umask）的默认权限，列出被屏蔽的权限位，内置 022、027、077、002 说明
* 八进制与 rwx 双向换算：勾选属主/属组/其他的读写执行位实时得到 644、755，输入八进制也能反查符号

![](https://mmbiz.qpic.cn/mmbiz_png/Dibzmm9niba04SsgSQXjDzeHflS5LMGbRSDPibpIHZfqwh4KUtNibZmImDNZx1cR7wcReAl0Ntz4J90jRrrhLLEfkeDP6nJQG4ftNEd5G15WLfo/640?wx_fmt=png&from=appmsg)

* setuid、setgid、sticky 独立开关，提示 setuid 脚本被内核忽略与提权风险；结果给出数字与符号两种 `chmod`，一键复制
* 附权限对照表：600 私钥、640 配置、644 普通文件、700 用户目录、755 程序、775 协作目录、2775 继承组、1777 公共目录、4755 setuid

![](https://mmbiz.qpic.cn/mmbiz_png/Dibzmm9niba07iaAQ3fWASZibiaIAlNwSuiasxQ2prtJKMJ5lUPQr9icO8BMS8UEHZKf1Y4K9ypg5YbBBiazMSDeH2XibT7UQulLB7kK04w2nNbQUUeI/640?wx_fmt=png&from=appmsg)

### Sysctl 参数生成器

```
https://tool.geek.cab/tools/sysctl-generator
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dibzmm9niba051PRic2a0CfO4Kfd6fL11FpehAJAsiaWQHcDEO2mCCmjeeSGel771ibnnVASMk5F1UkOPgajGlMJ5SXKzcKBicXD3xpzcgyVVGeIU/640?wx_fmt=png&from=appmsg)

* 内置 30 余项参数，按网络、内存、文件系统、内核、安全分组，含 `somaxconn`、`tcp_max_syn_backlog`、`ip_local_port_range`、`tcp_tw_reuse`、rmem/wmem 缓冲、`ip_forward`、`swappiness`、`overcommit_memory`、`max_map_count`、`file-max`、`nr_open`、`rp_filter` 等

![](https://mmbiz.qpic.cn/mmbiz_png/Dibzmm9niba07MaWg42Axicv3bic6YHGfhiboUmVmYs2slaSAYVuj2YRpGOCYJeAIue4o2JfB00xOaTJmZAxJfKQt4OrsibbnNkEkH6VPQibuRibAIA/640?wx_fmt=png&from=appmsg)

* 基础通用、高并发 Web、数据库、K8s 节点、安全加固五套预设可叠加；每项附中文说明与区间校验，自定义参数检查命名与重复
* 输出可直接落盘的 `/etc/sysctl.d/99-tuning.conf`，或逐条生效的 `sysctl -w`
* 附 `sysctl.d` 与 `sysctl.conf` 加载顺序、`br_netfilter` 依赖、容器内参数共享限制、调参前备份原值等要点

![](https://mmbiz.qpic.cn/mmbiz_png/Dibzmm9niba066gVGZMuB5pUeveCAGDXYsIVp9RibKRtlRS1eEBKCnDreCFXsjibrZDNCIiaaJbqXibfSEvKLRyib30St8JJ8P7SqQjHiagMWyb0Sn4/640?wx_fmt=png&from=appmsg)

### Systemd Unit 生成器

![](https://mmbiz.qpic.cn/mmbiz_png/Dibzmm9niba079UJIg7QTwHgZM4esD25OFMgpacg5SIknYOogsk55EnVIPRMwjkicEkicVvSicCdH7I2Nwwsdd7PRPXjzbNmibFbAroUCRpPEoMpk/640?wx_fmt=png&from=appmsg)

* 生成 [Unit]、[Service]、[Install] 三段完整的 `.service`，支持 simple、forking、oneshot、notify、idle 五种 Type，可配 User/Group、WorkingDirectory、ExecStop、ExecReload、EnvironmentFile、After/Wants、Restart 策略、LimitNOFILE、自启目标

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dibzmm9niba06LeIibb39ZLOesmGKADyoObbNShGKFOKiakArZ5z5do5lprYglA3TKvJhBZyjeQXtQhMGguRhmfHtseQ5ic4ayV7LI1uhaT47jnM/640?wx_fmt=png&from=appmsg)

* Node/Java 应用、Python 脚本、一次性任务三套模板，套用后改关键字段即可
* 生成前静态检查：ExecStart 非绝对路径、误写管道或 `&&`（systemd 不经过 shell）、EnvironmentFile 相对路径、oneshot 配 `Restart=always`、forking 缺 PIDFile、root 常驻
* 安装命令一键复制：`tee` 写入 `/etc/systemd/system/` → `daemon-reload` → `enable --now` → `status` → `journalctl`

![](https://mmbiz.qpic.cn/mmbiz_png/Dibzmm9niba06hkEwy8UdpBW6iam9OHz20iaoic8jkkDZypF6ZKBtlgFsICuUnMwDCV2StddDFNosB2lnNMRzLEK6MW7qPdWoNDWFSHzbbfIm8ns/640?wx_fmt=png&from=appmsg)

### Fstab 生成与校验

![](https://mmbiz.qpic.cn/mmbiz_png/Dibzmm9niba069HgiaRWem7tpx0RUo7q05eZsxNI4eW0jmKLoB2oAjFnl3Dv00t9xiaOiclksSXn6w9icsWgUsJAakAGnHhkTwbpgGtlG2IibILAick/640?wx_fmt=png&from=appmsg)

* 按设备、挂载点、类型、选项、dump、pass 六列生成标准条目并自动对齐，系统盘、数据盘、NFS、tmpfs、bind 五套模板，支持增删行
* 校验规则覆盖：`UUID=`/`LABEL=` 防盘符漂移、挂载点绝对路径、swap 的 pass、ext4 根分区 pass=1、xfs 误设 pass、网络文件系统缺 `_netdev` 与凭证、tmpfs 未限 size、选项含空格、挂载点或设备重复
* 提供校验模式：粘贴线上 `/etc/fstab` 逐行检查并定位行号，进 emergency mode 时省下反复重启
* 结果附挂载点创建、单条 `mount` 测试、备份、`mount -a` 与 `findmnt --verify` 的完整生效步骤

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dibzmm9niba06pb3YibHY6wXlnH3BOAXYmMdHVzyos7vb6TnrpgQJ91Mc3s3x414vbBVribFUSgSxib1LsKJoK0rFlIicCSH1DlKEDHPmelxVeialo/640?wx_fmt=png&from=appmsg)

## 安全加固

### sshd\_config 生成器

![](https://mmbiz.qpic.cn/mmbiz_png/Dibzmm9niba07D8awe6ic1cOZ59jCVRxraa8730Zf64cfKbFU4RlqZSdvFqqQpujjMuO5PfTSH6w9wiclf6uNuclebW05mDaJnzERstAWsZow1I/640?wx_fmt=png&from=appmsg)

* 勾选式生成配置片段，覆盖 Port 与 ListenAddress、PermitRootLogin 四种取值、密码与公钥认证、UsePAM、MaxAuthTries、MaxSessions、LoginGraceTime、保活间隔、AuthorizedKeysFile、sftp 子系统、Allow/Deny 名单、各类转发、Banner、日志级别、Ciphers/MACs/Kex 白名单
* 安全加固、跳板机、内网宽松三套预设，一键套用后微调
* 风险检查：root 密码登录与密码认证并存、密码与公钥认证同时关闭导致锁死、MaxAuthTries 过大、算法含 3DES、改端口未同步防火墙与 SELinux
* 输出写入 `sshd_config.d/99-custom.conf`，附备份、`sshd -t` 校验、reload 与"另开窗口验证"提示

![](https://mmbiz.qpic.cn/mmbiz_png/Dibzmm9niba057iaf62apGbf1h7YYmnQQrj2sD8z8xjMzyQFPXQ5TQsiabBfeXYxwxOXUbfmicmneGbEm5rgjzs5WZiaia4vJAtVXDeD0ibBZgs3f8c/640?wx_fmt=png&from=appmsg)

### iptables/nftables 规则生成器

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dibzmm9niba06YCl1Emm0wxw40c3DtotoNoMIX7cKwOSSv1TPrAZHrByhoRdEtdVBoNOeduAAVN06WXz8vVSJ54zoNWm9q5KgNnC4npbln7PM/640?wx_fmt=png&from=appmsg)

* 一次配置，同时产出可执行的 iptables 脚本与 nftables 配置
* 白名单模式：默认策略可选 DROP，SSH 端口单独填写，放行规则按端口或端口段、tcp/udp/双协议、来源 CIDR 加备注逐条添加
* 生成内容含规则备份、清空旧规则、默认策略、回环与 `ESTABLISHED,RELATED`、SSH 防爆破限速（iptables 用 recent 模块，60 秒内新连接超 4 次丢弃；nft 侧 `limit rate 4/minute burst 4`）、ICMP echo、丢弃日志前缀，forward 与 output 链一并处理
* 内置 Web、数据库（仅内网放行 3306/6379）、K8s 节点（6443/10250/NodePort）、仅 SSH 四套预设
* 默认 DROP 但白名单缺 SSH 端口时给出锁死警告；DROP 加禁 ICMP 时提示 ping 与监控探测失效
* 附持久化与回滚：`netfilter-persistent`、`/etc/sysconfig/iptables`、`/etc/nftables.conf`、`nft -c` 语法检查

![](https://mmbiz.qpic.cn/mmbiz_png/Dibzmm9niba06IpG2uDj8xH7ialb2PU5414j9lYwKXMaFibAeI3r3s9B2jxy13UQzmrbood922qPFqJeMNTAebE2PHR7LBGs3jR78lo0LatF3iao/640?wx_fmt=png&from=appmsg)

## 现场排障

### lsblk 解析器

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dibzmm9niba05StEBHRRwoV3PfoaO6b7mYicbC8tuM4orR9zhllgVKUArFRqNZoSEzxnGXQibgzULJ7nSM0713gyqWX6jE1bev634Qdia1Azmj6o/640?wx_fmt=png&from=appmsg)

* 粘贴 `lsb...