---
title: 2026美亚杯个人资格赛Writeup（全解）
url: https://mp.weixin.qq.com/s/95CcYzZd-7IMyIiYrOmPzA
source: Doonsec's feed
date: 2026-11-18
fetch_date: 2026-11-19T09:38:52.193777
---

# 2026美亚杯个人资格赛Writeup（全解）

# 2026美亚杯个人资格赛Writeup（全解）

Serendipity
Serendipity

鱼影安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

检材密码：`=zxky_rvQyv*4VnD2sqW?J!F&TmAcT8$9JgtPZsW?uV*_Smyp*PB+7S?sV-9%FTkTaAC`

`Hcd9A*aTHKh*rE78m=@?*4aaJdD!6QM$Xa7c56uERjM7C=7L?Zb2YQCernMA`

如果觉得阅读不便可移步：https://www.cnblogs.com/lyydbk/p/23685196

# 碎碎念

今年的美亚也是结束了，想起来第一篇文章就是从去年美亚个人赛开始，账号建立至今也已经快一年了，时间过得还是非常的快啊！很荣幸能被学生组团体赛冠军在ppt上分享，以后肯定还是会持续输出优质内容供大家观看，保持古法取证人的浪漫~

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9OIicEdrInSGeEam6ujWvJCDaNVxNVqZ5wt1M020xVY6rJOQPHbUnHTpHPhxR16IicnV8cx1NyrhqEsJSgjX9nx6wOxDTrrM2jPA/640?wx_fmt=png&from=appmsg)

# 使用的工具

1.VeraCrypt

2.**qiko3.0取证智能体**

3.一个迅速的解压工具，7-zip、bandzip等

4.数据库工具，navicat、DB Browser等

5.时间戳转换工具，Dcode

6.流量分析工具，lovelyspark、wireshark等

# 题目解析

这次的个人赛全是压缩包，所以我们不能一股脑全丢给分析软件，而是先看看压缩包里的内容，果不其然，压缩包里放的镜像，得先去解压一下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9NJjxLVdBNe7heM8XkjXXAxHADkqe8biazdJzlOPCCZpT4fkicQmEaO0QM7OOFLBEo5VzbqnAEqiceUiaraCIlESQAfupqlrku8ry8/640?wx_fmt=png&from=appmsg)

用qiko挂载的话记得手动选一下手机

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9NicB1VVbibWWJyvaYeFK7Y8JwLQTNWicibOoKhuubvK3BqmncQaEk0hYmd30yRIjWPXt79rXcl1mJZfhTjNC1pArGlpjqsEB6pkhg/640?wx_fmt=png&from=appmsg)

# 受害人1的手机（VTM-1）

> 手机的话其实你看压缩包，他就只有两个文件夹，所以解析不解析都一样，也可以翻文件

### 1.POON Chi-ming 通过哪个社交媒体 APP 与诈骗分子进行视频通话

**TELEGRAM**

直接看那几个照片就可以了，顺便就把第三题做了

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9MaCUsV0bnNrJcpjouR39IQHwsOLTn8Siam3vauicNWPSnKQL3o6KRuFokFKP9gO8TD0PWibeL5jAFgGPeniaPruElon4JJ7ENjfLQ/640?wx_fmt=png&from=appmsg)

### 2.POON Chi-ming 收到信用卡消费消息的时间

**AUG-07\_0947**

也是在图片里看到

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9NxaVlMDx30lic0t4YfTNg1GTvgDzGbdib8Iqf3HnFouN1VJFCicVIlMKhGAem8yfibCSjY9ibFOujhOXqHhZCSuLEJQLPDy7hZHzbo/640?wx_fmt=png&from=appmsg)

### 3.POON Chi-ming 通话记录中，诈骗分子来电时显示的名称

**KaHo**

见第一题

# 受害人2的手机（VTM-2）

### 4.诈骗分子安排 SIU Wai-shing 参加投资讲座的时间

**14:00**

这个检材就一个mp4，直接看就好了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9Nu31F3lGrrtF0taoYQFKk3icXvcbsM9xh82SpsDic7DkqU1HAKRfBVUcHd3YhGL6ibSnTGsUFpWlcr3H7YeKiamV3IaPCwibOBTcMI/640?wx_fmt=png&from=appmsg)

直接拖动视频一点点看就好了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9OoOJKXauoODxUSqX0LibURY9qqiaHZFVc8Q4JwN0wd15wJ899w60ic4s2r55yBX3fYibSHROEC8qhckG9Dr4Q846ia01TFQocrIENA/640?wx_fmt=png&from=appmsg)

# 冯程手机（FC-01）

> 这里也是挂载的时候记得手动选一下手机

### 5.冯程向张美透露，他此前曾在哪里工作

A:银行

B:学校

C:科网公司

D:酒店

**B**

这里没有分析出什么东西，但是有个whatsapp（赛前超大更新了qiko没更新…现已更新）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9Ou65x2R4rSibUVLlw2uGFFesZibnI8nzdRSqAiae9AE42d4RcOW2Hco8pdbqUaia054MiaKL6ps4S1tcIibkLvVpw5K7POlDib229MYs/640?wx_fmt=png&from=appmsg)

这里有个方式就是把他当做计算机再挂载一下，也可以看到whatsapp的解析

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9OZuHPvibSdBGmickau2aqQXPxShrX0qWS0xaVBI6Wic6OqC4lMhVNaiaEY3LoNsicLPXXIpM3693Im4KB1W9iaDvu8aBiaHVEJbcqgkw/640?wx_fmt=png&from=appmsg)

### 6.涉案群组「IT Working Group」建立者在数据库底层记录的账户标识符（JID / Creator JID）

**192252030808131@lid**

一个02剩下的都是03，02肯定是建立者了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9OleTCL2QvJLQlxMLjPn96kzAj9ns8378P3GO8ltPickfXlVOJKc0BA73WpJWYohe8Ip9xnJtvs4xYPQWQYqEYs4aUibOLicoh3wM/640?wx_fmt=png&from=appmsg)

### 7.「IT Working Group」对话记录中，冯程手机记录的发送与接收消息总数（合计）

**111**

这里qiko和火眼看到是109条，但是正确答案和AI跑的话都是111，超大解析也是111

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9OD913kFRzSicXVcWicThqRbBCAKJKt9ib4EPqer3NH5DoDGcNXv8QW0olKW7NCyTicTVuZ3ibPazlibQKsNO2YFuK9GBa2NDU7odQAw/640?wx_fmt=png&from=appmsg)

挺神奇的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/T5C6icTcSx9P0oibcCqDPJNnbOEjSTKysBPAfuqu1Im3MpcPmkIHhlUL9co96oalaNTvkrTnEIOibc4OweMAn7OTvW6O2MmKKibcpqLtXvcY8jM/640?wx_fmt=png&from=appmsg)

以下为qiko中全局问答告诉我的原因

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9OibyydY28wLBEGQXOgpnbDpmu1GF93xFbbUG64tibQUmw2JcclNMQicNibTOQqqZUtZErhXWfJW6CZ10HTtZ7E7HIy2DUw5U9xteA/640?wx_fmt=png&from=appmsg)

### 8.冯程 WhatsApp 个人头像原始图片在备份 Manifest 中对应的备份文件标识符 fileID

**df40ecf80230f659346084bc556ce96b0646eb2f**

在账户信息这里可以看到头像

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9PJEGoCrvwMwB94cBIxuf1CDNP6q1wdCjTRJ1XDlQcHHjBAGsJR6tCKLDpBsvvMCMpBOwibwicRWILEGNleZ9iaZynEqL1gqCbn1Y/640?wx_fmt=png&from=appmsg)

知道图片名称，直接去manifest.db中去搜索即可

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9O1koLASAnP5lE7THJRFiaM5ibPiaEj33w5Y4ssjJuF0aEkhibRibibduzJmBKulwuV059mYHxiaAQ1VibtYSlNwa6qoTvZoLRsbwD9dXE/640?wx_fmt=png&from=appmsg)

### 9.在拍摄或生成后不足 20 秒内即被迅速移至垃圾桶的照片

**IMG\_0001.PNG（标准答案IMG\_0015.JPG）**

在photo的数据库中没有看到任何有用的东西，所以就看看他的历史版本

![](https://mmbiz.qpic.cn/mmbiz_png/T5C6icTcSx9MMbvywvUkbQFl9PzUiaOprZ0dImyNbmwjHdvA4apeHQpWic0lkGvljAoCfCpSQn0ZoXMVVNzDRia5U3iarbFAmStKlCggsdMqVzUo/640?wx_fmt=png&from=appmsg)

让ai写一个恢复脚本

```
python

import argparse, os, shutil, sqlite3, struct, sys

try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

defparse_wal(wal_path):
    data = open(wal_path, 'rb').read()
    iflen(data) < 32:
        raise ValueError('WAL 文件太小，不是有效 WAL')
    magic, ver, psize, ckpt, salt1, salt2, c1, c2 = struct.unpack('>8I', data[:32])
    if magic notin (0x377f0682, 0x377f0683):
        raise ValueError('不是有效的 WAL 文件: magic=0x%x' % magic)
    frame_size = 24 + psize
    nframe = (len(data) - 32) // frame_size
    frames = []    # (idx, page_no, dbsize, frame_offset)
    commits = []   # 提交点的帧号（dbsize != 0）
    for i inrange(nframe):
        off = 32 + i * frame_size
        pno, dbsize = struct.unpack('>2I', data[off:off+8])
        if pno == 0:
            break
        frames.append((i + 1, pno, dbsize, off))
        if dbsize:
            commits.append(i + 1)
    return data, psize, frames, commits

defframes_containing(data, needle_bytes, psize):
    frame_size = 24 + psize
    res = set()
    start = 0
    whileTrue:
        i = data.find(needle_bytes, start)
        if i < 0:
            break
        if i >= 32:
            res.add((i - 32) // frame_size + 1)
        start = i + 1
    returnsorted(res)

defmain():
    ap = argparse.ArgumentParser(description='SQLite WAL 历史快照恢复')
    ap.add_argument('--src', default='wal_recover_input', help='源目录（含主库和 -wal）')
    ap.add_argument('--dst', default='wal_recover_out', help='输出目录')
    ap.add_argument('--db', default='Photos.sqlite', help='主库文件名')
    ap.add_argument('--needle', default='IMG_0001', help='被删记录中的关键字')
    ap.add_argument('--cut', type=int, default=None, help='手动指定截断帧号（默认自动）')
    args = ap.parse_args()

    db_src = os.path.join(args.src, args.db)
    wal_src = db_src + '-wal'
    ifnot os.path.exists(db_src):
        print('找不到主库:', db_src); return1
    ifnot os.path.exists(wal_src):
        print('找不到 WAL:', wal_src); return1

    data, psize, frames, commits = parse_wal(wal_src)
    print('WAL 页大小: %d 字节, 总帧数: %d, 提交点数: %d' % (psize, len(frames), len(commits)))

    needle_b = args.needle.encode('utf-8')
    nframes = frames_containing(data, needle_b, psize)
    print('包含 %r 的帧号: %s' % (args.needle, nframes))
    ifnot nframes:
        print('!! WAL 中没搜到该关键字，无法定位。可换 --needle 试试其他字符串。')
        return1

    f_last = nframes[-1]
    if args.cut:
        cut = args.cut
        print('手动指定截断帧: %d' % cut)
    else:
        cand = [c for c in commits if c > f_last]
        ifnot cand:
            print('该关键字出现在最后一个提交点之后，无法通过截断恢复。')
            return1
        cut = cand[0]
        print('最后一个含关键字的帧: %d ; 自动截断点(其后第一个提交帧): %d' % (f_last, cut))

    os.makedirs(args.dst, exist_ok=True)
    db_dst = os.path.join(args.dst, args.db)
    if os.path.exists(db_dst):
        os.remove(db_dst)
    shutil.copy2(db_src, db_dst)
    nbytes = 32 + cut * (24 + psize)
    wal_dst = db_dst + '-wal'
    withopen(wal_dst, 'wb') as f:
        f.write(data[:nbytes])
    print('已生成恢复副本: %s （截断 WAL 保留前 %d 帧）' % (db_dst, cut))

    con = sqlite3.connect(db_dst)
    cur = con.cursor()
    ok = True
    try:
        try:
            total = cur.execute('SELECT COUNT(*) FROM ZASSET').fetchone()[0]
            print('恢复库 ZASSET 资产总数:', total)
        except Exception as e:
            ok = False
            print('(查询 ZASSET 失败: %s)' % e)
        try:
         ...