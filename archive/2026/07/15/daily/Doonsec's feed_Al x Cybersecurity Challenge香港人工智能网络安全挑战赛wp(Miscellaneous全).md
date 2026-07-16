---
title: Al x Cybersecurity Challenge香港人工智能网络安全挑战赛wp(Miscellaneous全)
url: https://mp.weixin.qq.com/s/W_Ee-Uvqe74g3HglMWvDqg
source: Doonsec's feed
date: 2026-07-15
fetch_date: 2026-07-16T04:55:17.866800
---

# Al x Cybersecurity Challenge香港人工智能网络安全挑战赛wp(Miscellaneous全)

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YdkQKXYKSBgjWsPvkFB7jVgu0yLnJc0dVg0HuaT2znD0xJ4Lq9vTHcpfIxbhxKmep8bzq5nqsJdJLjdZemyKibMKQicfd6TUCeITg659ldoAs/0?wx_fmt=jpeg)

# Al x Cybersecurity Challenge香港人工智能网络安全挑战赛wp(Miscellaneous全)

赛查查

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于玫家大院
，作者玫幽倩

![](https://wx.qlogo.cn/mmhead/sc8lJYpicUaWe4sDb1V43WuBUWZ0qR9taqbprebuQQgm7KqcuLHn9KvCrh8JtkISVnFMib07gRibM4/0)

**玫家大院**
.

希望我们所有人都越来越好，博客更新更快https://mei-you-qian.github.io/，合作私聊s2764174229

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBhEnQ8aGoRN7qUr2aWtTyo7xlkgcSict9T6cjibwyg5WibIZMCwOKnJNxUJHLGRTibmj0R4j6YcZ9vQYhqjhyM4XBGrVF206icUGVv8/640?wx_fmt=png&from=appmsg "null")

快一个月没更新了，小发一篇嘿嘿

这套题的misc还是蛮有意思的，感觉蛮好玩的，像RAID 5、词向量模型之类的，稍微写了一下，misc的wp已经手搓复盘过了，别的部分ai做了还没手动复盘，就先不发了

## Miscellaneous

### database

题目描述：

> 某公司的RAID 5业务服务器备份只保留下部分数据。请检查残留证据，尽可能还原有用内容，并找出隐藏的 flag。

题目说的很明确了这个服务器采用的是RAID 5，而且是只保留下部分数据，看起来是一道RAID 5恢复的题目

应该是先恢复RAID 5阵列，再进入文件系统找flag

那在找之前我们自然是先要搞明白什么是RAID 5阵列

RAID，Redundant Array of Independent Disks，即独立磁盘冗余阵列，我们一般称之为磁盘阵列

其实本质上就是用多个独立的磁盘组成在一起形成一个大的磁盘系统，从而实现比单块磁盘更好的存储性能和更高的可靠性

而RAID5正是其中一种排列方式，实际上，这是目前用的最多的一种磁盘阵列排列方式，因为其兼顾了存储性能、数据安全和存储成本

其排布大致如下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBh83zvPQ56odnAdeiapQGJd4q2npibeqiaUOJVuHmicOGn1QSxSnNpq3yPA9Vcho9rIRsR8nYUiaMDnmwFOT00M52Dt0BzTwvGxLCe0/640?wx_fmt=png&from=appmsg "null")

RAID 5至少需要3块硬盘

数据会被分成若干数据块，分别写入不同硬盘；同时，系统会计算一份用于恢复数据的**校验信息 Parity**，并将校验信息分散存储在各块硬盘中。

例如有 3 块硬盘：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBggJuOvJUufcAewKvaBpTp0vrdYHAaTvhqEx0TOnhrVVWKEmjia9zvIibPRDkRicYTdaSZKzskXemgPUSEbgPhSjO8zSqFHv7bv8c/640?wx_fmt=png&from=appmsg "null")

校验块不会固定放在某一块硬盘上，而是轮流分布，这样可以避免某一块专门负责校验的硬盘成为性能瓶颈

那如何恢复数据呢，RAID 5一般采用的是XOR技术

例如 A XOR B = P 存进去的

那么如果A的数据坏了，只要 P XOR B = A 就能把A恢复出来

所以只要同时坏的不超过1块，RAID 5通常仍然可以继续读取数据

好来看题来

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBjcsaOcMgnNDH66kCg5z1ROj8hSy8orubpEv8Xk7lY4N7rJaBVgaXUlX3ibHvo3aLWOvrLwgr902mPwT6WjpnhtNWET7lp89lC0/640?wx_fmt=png&from=appmsg "null")![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBjGTwtpuiaUzUuHrCtxWres6EnPJIibGGibfs8icCiczd1kyOtb4xaFdFYAhc1zxoia5qMyKfib9AApU75d0XMgpxj37bARLaicUSbwcv4/640?wx_fmt=png&from=appmsg "null")

可以看到题目给了两块镜像

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBiaiczLRxbyvYLF0Liat6ibnBoUT3v5Vftp1IVPtnChz2xrKczVD1eDUtSo2CYTMoElsWNBG4ic1kibQ3nwdGKt7wvzr26Q0969qzelU/640?wx_fmt=png&from=appmsg "null")

```
file disk1.img
file disk2.img
```

检查文件类型可以直接发现是三块盘搭的RAID 5，但是只给了两块，尝试降级恢复

看看具体的RAID元数据，我们一般在Linux直接用mdadm来处理RAID

先把这两个镜像变成loop设备，因为RAID的成员盘一般不能直接挂载，我们先建立loop设备，其实就是把.img文件给模拟成一块磁盘， 给它分配一个`/dev/loopX`设备

```
sudo losetup -fP disk1.img
sudo losetup -fP disk2.img
```

查看 loop 设备对应关系：

```
losetup -a
```

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBiaq7771LGnXcUGLPvNibmibjtAsWH0BpzlwrKOkbrFQozDaNQ5ewUticrJZTgaiboIZ14cUFHP7rNViaWxIcjOvI4tThkWzKsTPJ258/640?wx_fmt=png&from=appmsg "null")

建立好loop设备后就可以用mdadm来看元数据了

```
sudo mdadm --examine /dev/loop0
sudo mdadm --examine /dev/loop1
```

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBgBksVzj6NNk66v7XS2HN1lVYDPichMHsuqNV1SG1F8WBaN42CD2UHsnibk6rSuOPIfyL0OrnTRia0gtwpxREMG9ZwsibqkyIjzt20/640?wx_fmt=png&from=appmsg "null")

可以看到关键信息，这两块分别是role 0和role 1，即第一块成员盘和第二块成员盘

我们缺失了role 2，第三块成员盘

注意这一步是必须的，因为我们得知道这俩分别是哪一块成员盘，才能按条带规则来重组RAID

由于缺失了一块盘，所以我们需要降级模式来组装RAID

```
sudo mdadm --assemble --readonly --run /dev/md0 /dev/loop0 /dev/loop1
```

各参数大概是下边这些意思

```
--assemble 组装已有 RAID 阵列
--readonly 只读方式组装，避免搞坏了
--run 即使阵列不完整，也尝试启动
/dev/md0 生成的 RAID 设备名
/dev/loop0 第一个 RAID 成员
/dev/loop1 第二个 RAID 成员
```

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBhPgFOO0dlx5gMIFo9gAlzmxfvCSdibV9sRV0uPY4Lf6I1K2TfBbPUq9BTPjjJicSP3QhgGN8T0JibySNCXMLtiabyI5OwRdFibWZU8/640?wx_fmt=png&from=appmsg "null")

```
cat /proc/mdstat
```

即可看见RAID的状态，这边的[UU\_]中U表示正常存在的成员盘，\_表示缺失的成员盘

通过 RAID 规则把成员盘重新组合起来后，我们终于得到了完整的 ext4 文件系统

开始挂载就好了

```
sudo mkdir -p /mnt/raid_recover
sudo mount -o ro /dev/md0 /mnt/raid_recover
```

创建一下挂载目录然后直接只读挂载

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBiaS0f60m15x0BVCMYlQ5I1ibs1BQ2iahAkZE6spIb08u7q1uGuCVU0YFJibnPGWlPB3BAd4aPBbrLr5VbHKyZzEAtGmupGMLrrglY/640?wx_fmt=png&from=appmsg "null")

cd过去，发现成功恢复，我们已经进入了原文件系统

之后就是找东西环节了，题目说是数据，我们可以搜一下

```
sudo find /mnt/raid_recover -type f | grep -iE 'db|sqlite|database'
```

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBhXQzp3iaTvNUaABAXO6raU1qBcHO3a6iaIT3JJhNLJNbx0ocea1b5fEXribBAMGwmWUtVNoeAfWr7KssSc797Bz77ePZC2dGxzQA/640?wx_fmt=png&from=appmsg "null")

这个 /var/lib/companydb/important.db的数据库明显很可疑

打开看看

```
sqlite3 /mnt/raid_recover/var/lib/companydb/important.db
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBiaMek7XEWClW4fSicALP4SFnAjKdvoFbOdjh1HcjEiaA52icSxeVFibXx0633qXmJuw2V9iaetITVFyic77525INqib0CKFqja1lWLPXk/640?wx_fmt=png&from=appmsg "null")

.tables看看表名，就发现个此地无银三百两的表

我们直接全部拉出来看看

```
SELECT * FROM flag_not_here;
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBiahhkgU6s7uh70KTu281yO6icOuBqnjAIjDW5tjbc3O0p0nNp88vwB2uAicM55lq3jvqLAlAXZwP4d7bJ0icIbBZ2utVo0l46libSo/640?wx_fmt=png&from=appmsg "null")

给了四个flag，不过仔细看看就能发现只有最后一个是对的

所以本题答案为flag{raid5\_recovery\_1s\_1mportant}

### ntfs\_dump

题目描述：

> 某员工将数据隐藏到bin文件中，请尽可能还原数据，并找出隐藏的flag，flag格式为FLAG{xxx}。

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBgUjdwSVwOgr5MvChl68CBUmENJCTydEibztDib61MfJ70d6LfOVfr0YwqcySY13e5m4BDvc7QcaYaYreic79ibLsYBfv4C0HlchOA/640?wx_fmt=png&from=appmsg "null")和题目描述一模一样啊，只给了一个bin文件，说是把数据隐藏进去了，让我们还原![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBiaTAVRXkRmUR0AcIiaicdsLJlPlRe9yDCHictZsBQqKQnR1yNyQ686U9qZ0a2k7nJhouMIQiaqIxpicHfibbPribJHQbD4Hxju05bklFI/640?wx_fmt=png&from=appmsg "null")

先file看看文件格式，发现被识别为了NTFS的启动扇区，看起来像是个NTFS文件系统镜像

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBgCIk1ZuGwXTgVYS1vOr7IaqCh0BiaNBB5BIzvXO1dfA70ibFoyEsicIoAMkNvIrcOteyGbaicWiaLfdgYjSOkOia2W4qC3S72uvaD50/640?wx_fmt=png&from=appmsg "null")

但是扔到Xways报错了，似乎不是一个正常的NTFS镜像

不过BPB似乎没有损坏，我们还是能看到一些基础参数

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBjfI9nUBYfp5zSTLObUsyHcCEsU5APsI5RLOwaItNmjudOJjAuAvaAAXWVRYmvdkyDv68yQIMLtend5icd7BIdDgsicRlNrqYFcw/640?wx_fmt=png&from=appmsg "null")![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBhJdG9TYslRqPMeBSMeUGBibIEJq4z1ia28uAzjibJiao9oxEV29q2kwlAAc0WhyRdauiaicPOqO1gxribCicTaOnmS0PicSIyMxJb1BtGI/640?wx_fmt=png&from=appmsg "null")

可以看到这边每扇区字节数是00 02，小端序存储，所以应该是0x0200，即512字节

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBgVv4BuRDcicZPaG9pUsE1U1ObIIzqeiclSWyia3UsHRNRDcfEkgJTl5UEWCY8K0dfXo1RAYCgcrLRaprcLk9VAYKpnWDPLWiaWbmA/640?wx_fmt=png&from=appmsg "null")

每簇是8个扇区，所以是每簇8\*512=4096字节

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBiaCkBJ2cibRibN0AriaUZVAyjjTjfcax1UCZficqPtQfuZswUdJnwvT5Z7P4mVJU2FvyLp1n271k9kfvECXnHRXoqUibJIhXfeD0Cicg/640?wx_fmt=png&from=appmsg "null")

扇区总数是0x4000，即16384（小端序

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBgFXnNibNE2xsXicjWOOICzQUdEnJWI17qTk3tHyk0gJp4engrBhuOSydib6X3D2ySq9kxAxiarVHAmecmJLwC2TC0cibKlvvDApMQk/640?wx_fmt=png&from=appmsg "null")

$MFT起始簇号为4（小端序

不过其实Xways的技术报告可以直接分析出就是了

![](https://mmbiz.qpic.cn/mmbiz_png/YdkQKXYKSBhLib2gojfb4JXwwQDjhTTHQibaCRfuYsWoKz7luZAyiaqgg4EDWAnibVvgCsxvpXvRIUIaQkormdpBNHccsKWrhE3j4UtV0IyPxVE/640?wx_fmt=png&from=appmsg "null")

偏移MFT 起始簇号 × 簇大小

所以$MFT 偏移应该是16384，即0x4000

![](https://mmbiz.qpic.cn/sz_mmbiz_png/YdkQKXYKSBjr22ibia6Mbu6rEYcJkpibMyD5WGYv2K0aBEJQ8xmTrCgTTB7cpRZpwicTNBgSnHiaibdt5UCxeE4QEbMcsgEwuYicHKic1dpIOnr3ibV8/640?wx_fmt=png&from=appmsg "null")

正常情况下准备按应该能看到FILE，但是现在这里塞了一大堆的伪造文件头，这会导致binwalk一类的工具无法检测

显然，我们必须手动搜索些有用的才行，那一般这种数据恢复的题目都会放到压缩包里作为载体，所以我们可以优先对于ZIP的几个主要结构十六进制进行搜索，主要是下边这三个

```
PK\x03\x04 Local File Header，本地文件头
PK\x01\x02 Central Directory，中央目录
PK\x05\x06 End of Central Directory，中央目录结束记录
```

当然，其中中央目录当然是最主要的，里边会记录很多东西

```
from pathlib import Path

data = Path("ntfs_dump.bin").read_bytes()

for sig in [
    b"PK\x03\x04",
    b"PK\x01\x02",
    b"PK\x05\x06",
    b"text.txt",
]:
    pos = []
    start = 0

    while True:
        i = data.find(sig, start)
        if i == -1:
            break
        pos.append(i)
      ...