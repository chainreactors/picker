---
title: 2026年盘古石杯被吊打|Hermes比赛环境搭建以SMB为例解决存储空间不足
url: https://mp.weixin.qq.com/s/rb4y3Pqnsi6XNztDGUwNiA
source: Doonsec's feed
date: 2026-05-10
fetch_date: 2026-05-11T05:53:32.459335
---

# 2026年盘古石杯被吊打|Hermes比赛环境搭建以SMB为例解决存储空间不足

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/RPq1g3ib528jS07gDBAyicCVABmzQu6ObiaW07LuuDBt9ibBX5IL33ytF21Xe7CtniamLU3uV01SjHMR7SWk5ZoQ0lZ1B6iafIjvJd8VXwPg80WKw/0?wx_fmt=jpeg)

# 2026年盘古石杯被吊打|Hermes比赛环境搭建以SMB为例解决存储空间不足

原创

0xSec笔记本
0xSec笔记本

0xSec笔记本

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

第三次参加盘古还是依旧还是看“天书”一般，

AI 能解很多题，但仍然会出错不少，尤其是面对盘古这种难题。

手机取证一塌糊涂！！！

![](https://mmbiz.qpic.cn/mmbiz_png/RPq1g3ib528h0oLl1stOWIDrSgFoMwtIHkiaXH2Mk4uYvoicTqmcAPibN6bUh1vA7uV1Re66Kw7dKhuocdJVh5iceQBsn3bkzVay7m0Uaf0Pp2ec/640?wx_fmt=png&from=appmsg)

     将 AI 自动化分析放在 Kali 的虚拟机中，但在取证分析过程中需要应对大容量容器分析——小则几十 GB，大则几百 GB，特别是盘古的检材年年都是 4、5 百 GB——我们该如何应对呢？在这里，我们通过SMB 共享来解决这个问题。

```
## SMB 解决镜像文件共享问题
 ### 结构图
```

Windows 宿主机
└── VeraCrypt 解密挂载为 K: 盘
└── SMB 只读共享：\WIN-HOST\PanguEvidence
↓
Kali 虚拟机
└── 挂载为 /mnt/evidence，只读访问
└── 分析结果、索引、数据库、临时文件写到 /casework

```
1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

32

33

34

35

36

37

38

39

40

41

42

43

44

45

46

47

48

**说明**：

- **证据源**：Windows VeraCrypt 盘符，只读
- **分析端**：Kali Agent
- **输出区**：Kali 本地虚拟磁盘 / SSD 工作目录

VeraCrypt 官方也将“一个系统挂载 VeraCrypt 卷，然后把卷内文件系统内容通过网络共享出去”列为一种共享方式；另一种“共享未挂载容器再由多个系统各自挂载”的方式要求只读，否则可能有一致性/损坏风险。你的场景更适合 **第一种方式**：Windows 只负责解密并共享内容，Kali 不再二次挂载 VeraCrypt 卷本身。

---

## 假设实际环境布局

### 设备环境

**Windows 宿主机**
- 1T SSD：系统盘，剩余约 100G
- 4T 机械硬盘：USB 硬盘盒连接，剩余约 3.5T

**Kali 虚拟机**
- Agent 安装在 Kali 中

**竞赛搭配**
- 4T 机械硬盘
  - 存放比赛加密包 / VeraCrypt 容器 / 解密后的镜像源文件

**Windows VeraCrypt**
- 挂载为 K: 盘

**Kali**
- `/mnt/evidence`：只读挂载 K: 盘共享
- `/casework`：写入分析结果、数据库、日志、Agent 输出
  - `/casework/tmp`：临时目录
  - `/casework/db`：DuckDB / SQLite 索引库
  - `/casework/report`：答案、证据链、writeup

**核心原则**：

- 大镜像留在宿主机
- Kali 只读访问
- 所有分析产物写到 Kali 本地

---

## Windows 宿主机设置

假设 VeraCrypt 解密后挂载成 `K:\`，里面有：
```

K:\disk01.E01
K:\mobile.ab
K:\memory.raw
K:\traffic.pcapng
K:\server.qcow2

```
1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

### 创建专用只读用户

在 Windows 上创建一个本地用户，例如：

- 用户名：`kali_ro`
- 密码：自定义

仅用于 Kali 读取比赛镜像。

**管理员 PowerShell 执行**：

```powershell
$UserName = "kali_ro"
$Password = Read-Host "Input password for kali_ro" -AsSecureString

New-LocalUser `
  -Name $UserName `
  -Password $Password `
  -FullName "Kali Read Only SMB User" `
  -Description "Read-only SMB user for Kali evidence access"

Set-LocalUser -Name $UserName -PasswordNeverExpires $true
Get-LocalUser kali_ro
```

---

### 共享 K:\ 为 SMB 只读共享

**管理员 PowerShell 执行**：

```
1

2

3

4

5

6

7

8

9

$ShareName = "PanguEvidence"
$DrivePath = "K:\"
$UserName = "kali_ro"
$Account = "${env:COMPUTERNAME}\$UserName"

New-SmbShare `
  -Name $ShareName `
  -Path $DrivePath `
  -ReadAccess $Account
```

**附加命令**：

```
1

2

3

4

5

# 查看共享
Get-SmbShare -Name PanguEvidence

# 查看共享权限
Get-SmbShareAccess -Name PanguEvidence
```

---

### 设置 NTFS 只读权限

**管理员 PowerShell 执行**：

```
1

2

3

4

5

$DrivePath = "K:\"
$UserName = "kali_ro"
$Account = "${env:COMPUTERNAME}\$UserName"

icacls $DrivePath /grant "${Account}:(OI)(CI)(RX)"
```

**解释**：

* • `RX` = Read & Execute
* • `OI` = Object inherit，文件继承
* • `CI` = Container inherit，文件夹继承

**查看权限**：

```
1

icacls K:\
```

---

### 开启 SMB 防火墙

**管理员 PowerShell**：

```
1

2

3

4

Set-NetFirewallRule `
  -DisplayGroup "File and Printer Sharing" `
  -Enabled True
  -Profile Private
```

> 如果 Windows 是中文系统，可能需要：
>
> ```
> 1
>
>
>
>
> netsh advfirewall firewall set rule group="文件和打印机共享" new enable=Yes
> ```

**宿主机 IP**：

```
1

2

ipconfig
192.168.134.1
```

---

## Kali 端配置设置

### 安装 CIFS 工具

```
1

2

sudo apt update
sudo apt install -y cifs-utils
```

### 创建目录结构

```
1

2

3

4

mkdir -p /casework/case001/{tmp,db,out,report,extracted,timeline,logs}

sudo chown -R "$USER:$USER" /casework
chmod -R 755 /casework
```

### 创建 SMB 凭证文件

```
1

2

3

4

5

sudo nano /root/.smb-pangu
# 内容
username=kali_ro
password=你的密码
domain=你的Windows电脑名
```

```
1

2

sudo chmod 600 /root/.smb-pangu
sudo ls -l /root/.smb-pangu
```

### 创建挂载目录

```
1

sudo mkdir -p /mnt/evidence
```

### 手动挂载 SMB 共享

```
1

2

3

4

5

# 尝试 SMB 3.1.1
sudo mount -t cifs //192.168.134.1/PanguEvidence /mnt/evidence \
  -o credentials=/root/.smb-pangu,ro,vers=3.1.1,uid=$(id -u),gid=$(id -g),iocharset=utf8,nounix,noserverino

# 如果失败尝试 SMB 3.0 或 SMB 2.1
```

### 检查挂载

```
1

2

3

findmnt /mnt/evidence
df -h /mnt/evidence
ls -lah /mnt/evidence
```

> 验证只读：尝试写入应提示 `Read-only file system` 或 `Permission denied`

### 卸载共享

```
1

2

3

4

5

6

7

8

sudo umount /mnt/evidence

# 若 busy
lsof +f -- /mnt/evidence
fuser -vm /mnt/evidence

# 强制懒卸载（不推荐常用）
sudo umount -l /mnt/evidence
```

---

### 设置开机自动挂载（可选）

```
1

2

3

4

5

6

7

8

9

10

11

12

13

id -u   # 获取 UID
id -g   # 获取 GID

sudo cp /etc/fstab /etc/fstab.bak.$(date +%F_%H%M%S)

echo '//192.168.134.1/PanguEvidence /mnt/evidence cifs credentials=/root/.smb-pangu,ro,vers=3.1.1,uid=1000,gid=1000,iocharset=utf8,nounix,noserverino,nofail,x-systemd.automount 0 0' | sudo tee -a /etc/fstab

sudo systemctl daemon-reload
sudo umount /mnt/evidence
sudo mount -a

findmnt /mnt/evidence
ls -lah /mnt/evidence
```

当然最好是直接将检材放入kali中并且使用固态硬盘，速度更快。

参考挂载脚本，需要在kali下载VeraCrypt软件。

```
#!/usr/bin/env bash
set -e

VOLUME='/casework/Gamgs/第四届盘古石杯初赛'
MOUNT_POINT='/mnt/evidence'
PASSWORD=''

if [ -z "$PASSWORD" ]; then
  echo '[!] 请先编辑 /home/kali/run_pangu_vc.sh ，把 PASSWORD=\x27\x27 改成你的比赛密码后再运行。' >&2
  exit 1
fi

sudo mkdir -p "$MOUNT_POINT"
sudo /home/kali/.local/bin/veracrypt --text --non-interactive --password="$PASSWORD" --mount "$VOLUME" "$MOUNT_POINT"
find "$MOUNT_POINT" -maxdepth 2 | head -100
```

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/1ADJCFZ0CSJbicoSblA0gAvoYITOib8ZQQ2h18ibU2NmibdWJMyU1Vmqxh0KTnw0tWymLTVSoibpTlUheiaaXcOzXNibg/0?wx_fmt=png)

0xSec笔记本

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/1ADJCFZ0CSJbicoSblA0gAvoYITOib8ZQQ2h18ibU2NmibdWJMyU1Vmqxh0KTnw0tWymLTVSoibpTlUheiaaXcOzXNibg/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过