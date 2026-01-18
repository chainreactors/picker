---
title: rm -rf 误删文件？XFS 格式救星来了！xfs_undelete 5 分钟极速恢复实战
url: https://mp.weixin.qq.com/s/z-yB8m2TP_BTZyJvwNR3rA
source: Doonsec's feed
date: 2026-01-17
fetch_date: 2026-01-18T03:33:13.301791
---

# rm -rf 误删文件？XFS 格式救星来了！xfs_undelete 5 分钟极速恢复实战

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GYcoKKbcBjMC2JQ645Bia1hvMgiaSUSQsRhh82vZw4b3kcN456Pg4ZoMuaBY6eBID39UNbGH8E4oib7koTm1m7qlA/0?wx_fmt=jpeg)

# rm -rf 误删文件？XFS 格式救星来了！xfs\_undelete 5 分钟极速恢复实战

原创

小柳实验室
小柳实验室

小柳实验室

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/GYcoKKbcBjNrl929DxDeBczZLSiayqicia9ZzVPHicPdOljIvIf5VKuFsOBsT0CgH8jDXHn5NaI8lmyGgXa428twzg/640?wx_fmt=gif&from=appmsg)

作为Linux运维工程师，谁没经历过 `rm -rf` 按下回车后的瞬间窒息？

上一篇我们聊了`ext4 文件`系统的误删恢复神器`[extundelete](https://mp.weixin.qq.com/s?__biz=MzAxMDM2OTg4NA==&mid=2247484969&idx=1&sn=502c7c745ad63226fccb475c09ece82f&scene=21#wechat_redirect)`，后台一堆粉丝催更：**XFS文件系统误删了咋办？**

![](https://mmbiz.qpic.cn/mmbiz_png/GYcoKKbcBjMC2JQ645Bia1hvMgiaSUSQsRdgOIKgnyX92n3icZkUEDvY5hjqeBGia4swJvSUXPU1rlEItqzt3LkVKQ/640?wx_fmt=png&from=appmsg)

毕竟XFS凭借高性能、高扩展性，早已成为RHEL/CentOS 7+的默认文件系统，更是企业级存储、大数据集群的标配。但XFS的“难恢复”属性，也曾让无数运维人对着空空如也的目录欲哭无泪。

今天就给大家带来**XFS文件误删的救命方案**——基于`xfs_undelete`工具的5分钟极速部署+实战案例全解析，看完直接抄作业！

## 一、为什么xfs\_undelete是XFS恢复的首选？

XFS文件系统的inode管理机制和ext4差异很大，普通恢复工具根本无从下手。而`xfs_undelete`是专门针对XFS开发的开源恢复工具，核心优势直接戳中运维痛点：

1. 1. **只读操作，零二次伤害**
   工具全程只读取文件系统数据，不会向目标分区写入任何内容，彻底避免“越恢复越糟”的惨剧。
2. 2. **智能筛选，拒绝垃圾文件**
   内置文件类型识别引擎，能自动过滤无效碎片，不会让你在成百上千个乱码文件里大海捞针。
3. 3. **多维度过滤，精准定位目标**
   支持按**删除时间、文件类型、大小**筛选，想找啥就找啥，效率直接拉满。
4. 4. **零门槛上手，新手友好**
   无需编译安装，下载就是可执行脚本，几条命令就能搞定恢复，对运维新人极度友好。

## 二、5分钟极速部署：环境准备+工具安装

### 前置条件：检查依赖包

xfs\_undelete基于Tcl语言开发，先确保系统装了这些依赖（以CentOS 7为例）：

```
# 安装Tcl解释器及依赖库
yum install -y tcl tcllib coreutils file
```

* • **tcl**：Tcl语言的运行环境，必须装
* • **tcllib**：Tcl的扩展库，提供额外功能
* • **coreutils**：Linux基础工具集，确保命令正常运行
* • **file**：文件类型识别工具，提升恢复精准度

### 关键一步：下载工具（划重点！）

**强烈建议**：将工具下载到**非目标恢复分区**，避免覆盖待恢复数据！

```
# 创建临时目录，存放工具
mkdir -p /tmp/tools && cd /tmp/tools
# 克隆工具源码
# https://github.com/ianka/xfs_undelete
git clone https://gitcode.com/gh_mirrors/xf/xfs_undelete
# 进入工具目录，赋予执行权限
cd xfs_undelete
chmod +x xfs_undelete
```

工具是纯Tcl脚本，无需编译，赋予执行权限就能直接用！

## 三、核心命令实战：从简单到复杂，一步到位

先明确一个前提：**恢复前务必停止对目标分区的写入操作！** 最好直接卸载分区：

```
# 卸载目标分区（以/dev/sda4为例）
umount /dev/sda4
```

写入操作会覆盖inode和数据块，越晚操作，恢复成功率越低！

### 基础操作：恢复分区所有可恢复文件

这是最常用的命令，直接扫描目标分区，恢复所有被删除的文件：

```
# 恢复/dev/sda4所有误删文件，保存到当前目录的xfs_undeleted文件夹
./xfs_undelete /dev/sda4
```

**输出示例**：

```
Scanning XFS filesystem /dev/sda4...
Found 128 deleted inodes.
Recovering files to ./xfs_undeleted...
Recovery completed. 96 files recovered successfully.
```

### 进阶操作1：按时间筛选，精准定位

如果你记得大概的删除时间，用时间筛选能大幅减少恢复文件数量：

```
# 恢复最近48小时内删除的文件
./xfs_undelete -t 48h /dev/sda4

# 恢复2026-01-16之后删除的文件
./xfs_undelete -t "2026-01-16.." /dev/sda4

# 恢复2026-01-16到2026-01-17之间删除的文件
./xfs_undelete -t "2026-01-16..2026-01-17" /dev/sda4
```

### 进阶操作2：按文件类型筛选，直击目标

只恢复需要的文件类型，避免无用文件占用空间：

```
# 只恢复所有图片文件（jpg/png/gif等）
./xfs_undelete -r "image/*" /dev/sda4

# 只恢复文档类文件（txt/pdf/docx）
./xfs_undelete -r "text/plain,application/pdf,application/vnd.openxmlformats-officedocument.wordprocessingml.document" /dev/sda3
```

### 进阶操作3：指定输出目录，规范管理

默认恢复文件会存在当前目录的`xfs_undeleted`文件夹，也可以自定义输出路径：

```
# 创建专用恢复目录（必须在其他分区！）
mkdir -p /mnt/recovery
# 将恢复的文件保存到/mnt/recovery
./xfs_undelete -o /mnt/recovery /dev/sda4
```

## 四、3个真实运维场景：手把手教你救数据

### 场景1：误删项目配置文件，2小时内紧急恢复

**故障现象**：在生产服务器上误删了`/etc/nginx/conf.d`下的配置文件，删除时间不到2小时。
**操作步骤**：

1. 1. 立即停止nginx服务，防止写入新数据：

   ```
   systemctl stop nginx
   ```
2. 2. 卸载nginx配置所在分区（假设在/dev/sda3）：

   ```
   umount /dev/sda4
   ```
3. 3. 恢复最近2小时内的配置文件（文本类型）：

   ```
   ./xfs_undelete -t -2h -r "text/plain" -o /mnt/recovery /dev/sda4
   ```
4. 4. 去`/mnt/recovery`目录找到配置文件，复制回原路径，重启nginx。

### 场景2：前端误删，批量恢复图片文件

**故障现象**：开发服务器上的前端误删了`/data/design`下的所有PNG文件，删除时间1天内。
**操作步骤**：

1. 1. 卸载`/data`所在分区`/dev/sdb1`：

   ```
   umount /dev/sdb1
   ```
2. 2. 恢复最近24小时内的所有图片文件：

   ```
   ./xfs_undelete -t -24h -r "image/*" -o /mnt/design_recovery /dev/sdb1
   ```

### 场景3：误删系统文件，单用户模式下恢复

**故障现象**：误删`/usr/bin/ls`等系统命令，导致系统部分功能异常，无法正常使用。
**操作步骤**：

1. 1. 重启服务器，开机时按`e`进入GRUB编辑模式，在启动项后添加`init=/bin/bash`，进入单用户模式。
2. 2. 挂载根分区为只读模式（防止二次损坏）：

   ```
   mount -o remount,ro /
   ```
3. 3. 挂载外部U盘（假设为`/dev/sdc1`）到`/mnt/usb`：

   ```
   mount /dev/sdc1 /mnt/usb
   ```
4. 4. 执行恢复命令，恢复系统二进制文件：

   ```
   ./xfs_undelete -r "application/x-executable" -o /mnt/usb/recovery /dev/sda1
   ```
5. 5. 将恢复的文件复制回`/usr/bin`，重启系统。

## 五、运维必看：进阶技巧+避坑指南

### 提高恢复成功率的3个关键技巧

1. 1. **快！快！快！**
   文件删除后，数据块不会立即清零，一旦有新数据写入就会被覆盖。**停止写入+立即恢复**是成功的关键。
2. 2. **权限要够**
   必须用`root`用户执行恢复操作，普通用户没有访问磁盘分区的权限。
3. 3. **输出目录别选错**
   输出目录**绝对不能和目标分区在同一个磁盘**！否则新写入的恢复文件会覆盖待恢复数据。

### 常见问题故障排除

1. 1. **问题**：执行命令后提示“permission denied”
   **解决**：切换到root用户，或者用`sudo`执行命令。
2. 2. **问题**：恢复的文件都是乱码，无法打开
   **解决**：大概率是数据块已被覆盖，恢复时机太晚；或者文件类型筛选错误，调整`-r`参数重试。
3. 3. **问题**：工具提示“no deleted inodes found”
   **解决**：目标分区没有可恢复的删除文件，或者文件系统不是XFS。

### 重要注意事项

1. 1. 恢复的文件**无法保留原始文件名**，工具会根据inode号、删除时间生成新名称，需要手动识别。
2. 2. 恢复的文件大小可能比原文件大，因为会填充到XFS块大小的边界，文本文件可以用`truncate`命令去除尾部空字符。
3. 3. **备份才是王道**：任何恢复工具都是“亡羊补牢”，定期备份（rsync、tar、快照）才是防止数据丢失的根本方案。

## 六、写在最后

`xfs_undelete`就像XFS文件系统的“后悔药”，关键时刻能帮我们挽回重大损失。但作为运维人，更要养成“操作前备份、高危命令先测试”的好习惯。

![](https://mmbiz.qpic.cn/mmbiz_gif/GYcoKKbcBjPM88logbaFhsxVIxHGfN8sCHicaficYa68jS5OPPbibIUFk0oecCnia6xwiae0OX8gr1hGBSd3ca8RbXQ/640?wx_fmt=gif&from=appmsg)

#### 📬 关注我

#### 推荐阅读

#### [Redis主从复制深度解析：数据高可用与负载均衡的核心方案](https://mp.weixin.qq.com/s?__biz=MzAxMDM2OTg4NA==&mid=2247484720&idx=1&sn=d8f5606ddae7446b218ba78b20192e91&scene=21#wechat_redirect)

#### [运维必备｜Zabbix 从 0 到 1 搭建企业级监控，告警自动喊你处理！](https://mp.weixin.qq.com/s?__biz=MzAxMDM2OTg4NA==&mid=2247484738&idx=1&sn=dfca8b99647de349ea542f006a0447e6&scene=21#wechat_redirect)

#### [15分钟搞定业务宕机！运维必备排查指南（附实操命令）](https://mp.weixin.qq.com/s?__biz=MzAxMDM2OTg4NA==&mid=2247484707&idx=1&sn=a2aeb0d301f8a1ea7fabc6df7b9fcc37&scene=21#wechat_redirect)

#### [SCP 与 rsync 到底怎么选？运维老鸟的文件传输避坑指南](https://mp.weixin.qq.com/s?__biz=MzAxMDM2OTg4NA==&mid=2247484660&idx=1&sn=31cfde90b5d344f43aee94da3e741938&scene=21#wechat_redirect)

#### [效率拉满！Docker+Nginx 一站式部署 Java（JAR/WAR 通用），运维再也不加班](https://mp.weixin.qq.com/s?__biz=MzAxMDM2OTg4NA==&mid=2247484652&idx=1&sn=c2f21df196ddf1449e0228d1644af976&scene=21#wechat_redirect)

#### [别再搞混Nginx和OpenResty！90%运维都踩过的坑，一文讲透核心差异](https://mp.weixin.qq.com/s?__biz=MzAxMDM2OTg4NA==&mid=2247484642&idx=1&sn=9d801f6e32d1d48ca178f50b6f7a2f65&scene=21#wechat_redirect)

#### [开发运维必备神器！HexHub 一站式搞定数据库、SSH、Docker 所有需求](https://mp.weixin.qq.com/s?__biz=MzAxMDM2OTg4NA==&mid=2247484642&idx=2&sn=e294ce7ce735d6358ddfe44dd56de1cb&scene=21#wechat_redirect)

#### [网络排查神器！掌握 tcpdump，让网络故障无处遁形](https://mp.weixin.qq.com/s?__biz=MzAxMDM2OTg4NA==&mid=2247484599&idx=1&sn=ec867d8dcaba4dfce556d3e6b7105b1a&scene=21#wechat_redirect)

#### [MySQL 与 PostgreSQL：两个老对手的技术对决与选型指南](https://mp.weixin.qq.com/s?__biz=MzAxMDM2OTg4NA==&mid=2247484564&idx=1&sn=813b062f9a0b64ea53e4d55a5bef164f&scene=21#wechat_redirect)

#### [高性能存储刚需党必看！Docker 部署 RustFS，效率直接拉满](https://mp.weixin.qq.com/s?__biz=MzAxMDM2OTg4NA==&mid=2247484488&idx=1&sn=a558fdf75c460836f091c7fc294fac15&scene=21#wechat_redirect)

#### [别再用第三方短链了！这个开源神器3分钟搭建专属短网址平台](https://mp.weixin.qq.com/s?__biz=MzAxMDM2OTg4NA==&mid=2247484520&idx=1&sn=d9f808127d673d6cb5ebb6a075ad254c&scene=21#wechat_redirect)

#### [Linux服务器重启后服务不自启？systemd实战指南 + 混沌演练验证](https://mp.weixin.qq.com/s?__biz=MzAxMDM2OTg4NA==&mid=2247484524&idx=1&sn=bb6f6bcff27fa7290592f9eae4ef72bc&scene=21#wechat_redirect)

#### [502 Bad Gateway 不是终点：一次生产事故背后的全链路复盘](https://mp.weixin.qq.com/s?__biz=MzAxMDM2OTg4NA==&mid=2247484459&idx=1&sn=04fbd75534f6474ebe2643baa3f081a7&scene=21#wechat_redirect)

#### [备份做了，但能恢复吗？MySQL 数据恢复终极指南来了！](https://mp.weixin.qq.com/s?__biz=MzAxMDM2OTg4NA==&mid=2247484442&idx=1&sn=d6256ad2948324bc0361b8651da81dd7&scene=21#wechat_redirect)

#### [Firewalld 实战全攻略：从入门到精通，搭配 ipset 打造高效防护体系！](https://mp.weixin.qq.com/s?__biz=MzAxMDM2OTg4NA==&mid=2247484423&idx=1&sn=df5ed942097c767c8c93bc5f1750e734&scene=21#wechat_redirect)

#### [命令行也能玩转 WebSocket？别再用浏览器调了](https://mp.weixin.qq.com/s?__biz=MzAxMDM2OTg4NA==&mid=2247484404&idx=1&sn=d21ea0668e001ec88ab8a6a874e350d6&scene=21#...