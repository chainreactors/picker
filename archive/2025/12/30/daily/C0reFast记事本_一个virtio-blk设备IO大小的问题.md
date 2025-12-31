---
title: 一个virtio-blk设备IO大小的问题
url: https://www.ichenfu.com/2025/12/30/virtio-blk-io-size/
source: C0reFast记事本
date: 2025-12-30
fetch_date: 2025-12-31T03:24:11.121415
---

# 一个virtio-blk设备IO大小的问题

[C0reFast猫庐掳盲潞聥忙聹卢](/)

to inspire confidence in somebody.

* [茅娄聳茅隆碌](/)
* [氓聢聠莽卤禄](/categories/)
* [氓陆聮忙隆拢](/archives/)
* [忙聽聡莽颅戮](/tags/)
* [氓聟鲁盲潞聨](/about/)
* 忙聬聹莽麓垄

* 忙聳聡莽芦聽莽聸庐氓陆聲
* 莽芦聶莽聜鹿忙娄聜猫搂聢

1. [1. 忙聸麓氓陇職莽職聞忙碌聥猫炉聲](#%E6%9B%B4%E5%A4%9A%E7%9A%84%E6%B5%8B%E8%AF%95)
2. [2. 猫庐戮氓陇聡莽職聞茅聶聬氓聢露](#%E8%AE%BE%E5%A4%87%E7%9A%84%E9%99%90%E5%88%B6)
3. [3. 氓聫聜忙聲掳盲录聵氓聦聳](#%E5%8F%82%E6%95%B0%E4%BC%98%E5%8C%96)
4. [4. OneMoreThing](#OneMoreThing)

茅聶聢氓颅職

[112
忙聴楼氓驴聴](/archives/)

[15
氓聢聠莽卤禄](/categories/)

[255
忙聽聡莽颅戮](/tags/)

[GitHub](https://github.com/C0reFast "GitHub 芒聠聮 https://github.com/C0reFast")

E-Mail

[Weibo](https://weibo.com/c0refast "Weibo 芒聠聮 https://weibo.com/c0refast")

猫碌聻氓聤漏氓聲聠

茅聯戮忙聨楼

* [莽聢卤氓录聙忙潞聬](https://www.aikaiyuan.com/ "https://www.aikaiyuan.com/")
* [盲赂聙氓聠聣氓聠聧](https://blog.yiranzai.top/ "https://blog.yiranzai.top/")
* [PikachuWorld](https://www.cnblogs.com/pikachuworld/ "https://www.cnblogs.com/pikachuworld/")

# 盲赂聙盲赂陋virtio-blk猫庐戮氓陇聡IO氓陇搂氓掳聫莽職聞茅聴庐茅垄聵

氓聫聭猫隆篓盲潞聨
2025氓鹿麓12忙聹聢30忙聴楼 21:26

氓聢聠莽卤禄盲潞聨

[Linux](/categories/Linux/)

茅聵聟猫炉禄忙卢隆忙聲掳茂录職

忙聹聙猫驴聭氓聹篓忙碌聥猫炉聲忙聢聭盲禄卢莽職聞VM忙聴露茂录聦氓聫聭莽聨掳盲潞聠盲赂聙盲赂陋忙炉聰猫戮聝氓楼聡忙聙陋莽職聞莽聨掳猫卤隆茂录職氓炉鹿盲潞聨氓聬聦忙聽路莽職聞盲赂聙盲赂陋IO氓聨聥氓聤聸茂录聦氓陆聯IO猫庐戮氓陇聡忙聵炉`NVMe`忙聢聳猫聙聟`virtio-blk`忙聴露茂录聦猫隆聦盲赂潞忙聹聣盲赂聙盲潞聸盲赂聧氓陇陋盲赂聙忙聽路茂录聦氓聟路盲陆聯猫隆篓莽聨掳氓聹篓IOPS盲赂聤茂录聦猫聙聦盲赂聰氓路庐猫路聺茅聺聻氓赂赂氓陇搂茂录聦氓聬聦忙聽路忙聵炉1GB/s氓路娄氓聫鲁莽職聞IO茂录聦盲赂陇盲赂陋盲赂聧氓聬聦猫庐戮氓陇聡莽職聞IOPS氓路庐盲潞聠忙聨楼猫驴聭4氓聙聧茂录職

![](/images/virtio-blk-io-size/iops.png)

### 忙聸麓氓陇職莽職聞忙碌聥猫炉聲

盲赂聙猫聢卢忙聺楼猫炉麓茂录聦NVMe猫庐戮氓陇聡茂录聦氓聧聲盲赂陋IO莽職聞忙聹聙氓陇搂氓陇搂氓掳聫忙聵炉`128KB`茂录聦茅聜拢氓炉鹿盲潞聨1GB/s莽職聞氓聬聻氓聬聬忙聺楼猫炉麓茂录聦氓陆聯氓聣聧莽職聞IOPS忙聵炉盲赂聙盲赂陋氓聬聢莽聬聠莽職聞氓聙录茂录聦茅聜拢茅聴庐茅垄聵氓戮聢忙聵戮莽聞露氓聡潞氓聹篓盲潞聠`virtio-blk`猫庐戮氓陇聡盲赂聤茂录聦氓聫炉盲禄楼莽隆庐氓庐職氓聹掳忙聵炉茂录聦氓聹篓`virtio-blk`猫庐戮氓陇聡盲赂聤莽職聞IO猫垄芦氓聢聡氓聢聠盲潞聠茫聙聜莽庐聙氓聧聲茅聶陇盲赂聙盲赂聥茂录聦氓聫炉盲禄楼氓陇搂猫聡麓氓戮聴氓聢掳猫庐戮氓陇聡氓卤聜莽職聞IO氓陇搂氓掳聫氓陇搂猫聡麓氓聹篓`30KB`茅聶聞猫驴聭茂录聦忙聦聣莽聟搂氓赂赂莽聬聠茂录聦`virtio-blk`猫庐戮氓陇聡莽職聞忙聹聙氓陇搂IO氓陇搂氓掳聫氓聫炉盲赂聧忙颅垄猫驴聶莽聜鹿茫聙聜

盲赂潞盲潞聠忙聰露茅聸聠忙聸麓氓陇職莽職聞盲驴隆忙聛炉茂录聦猫驴聵忙聵炉氓陇職氓聛職盲赂聙盲潞聸忙碌聥猫炉聲茂录聦莽聹聥莽聹聥猫庐戮氓陇聡氓聹篓盲赂聧氓聬聦莽職聞IO忙篓隆氓聻聥盲赂聥莽職聞氓聟路盲陆聯莽職聞猫隆篓莽聨掳茫聙聜盲陆驴莽聰篓`fio`莽禄聶猫庐戮氓陇聡氓聤聽盲赂聤盲赂聙盲赂陋氓聸潞氓庐職莽職聞IO茂录職

```
# fio -filename=/dev/vdb -direct=1 -iodepth 1 -thread -rw=read -ioengine=libaio -rate_iops=200 -bs=4K -size=200G -numjobs=1 -runtime=5 -group_reporting -name=test
```

莽聞露氓聬聨氓聠聧盲陆驴莽聰篓`iostat -x 1`氓聭陆盲禄陇猫搂聜氓炉聼猫庐戮氓陇聡氓卤聜莽職聞IO忙聝聟氓聠碌茂录聦莽聞露氓聬聨氓掳卤忙聵炉忙聤聤`-bs=4K`氓聫聜忙聲掳忙聧垄忙聢聬盲赂聧氓聬聦莽職聞IO氓陇搂氓掳聫氓掳卤猫隆聦盲潞聠茂录職

```
# iostat -x 1
Device            r/s     rkB/s   rrqm/s  %rrqm r_await rareq-sz
vdb            200.00    800.00     0.00   0.00    0.07     4.00
```

氓聫炉盲禄楼莽聹聥氓聢掳氓陆聯`bs=4K`忙聴露茂录聦忙聲掳忙聧庐忙聵炉莽卢娄氓聬聢茅垄聞忙聹聼莽職聞茂录聦盲禄聨猫庐戮氓陇聡氓卤聜盲鹿聼猫搂聜氓炉聼氓聢掳盲潞聠`200 r/s`莽職聞IOPS茂录聦氓鹿鲁氓聺聡莽職聞IO氓陇搂氓掳聫`rareq-sz`盲鹿聼忙聵炉`4.0K`茫聙聜

盲赂聥茅聺垄忙聵炉盲赂聧氓聬聦IO氓陇搂氓掳聫盲赂聥莽職聞莽聸聭忙聨搂忙聲掳忙聧庐忙聲麓莽聬聠猫隆篓茂录職

| IO氓陇搂氓掳聫 (K) | r/s | rkB/s | rareq-sz | 忙聰戮氓陇搂氓聙聧忙聲掳 |
| --- | --- | --- | --- | --- |
| 4 | 200.00 | 800.00 | 4.00 | 1.00 |
| 8 | 200.00 | 1600.00 | 8.00 | 1.00 |
| 16 | 200.00 | 3200.00 | 16.00 | 1.00 |
| 32 | 400.00 | 6400.00 | 16.00 | 2.00 |
| 64 | 600.00 | 12800.00 | 21.33 | 3.00 |
| 128 | 1000.00 | 25600.00 | 25.60 | 5.00 |
| 256 | 2000.00 | 51200.00 | 25.60 | 10.00 |
| 512 | 3800.00 | 102400.00 | 26.95 | 19.00 |

氓聫炉盲禄楼氓聫聭莽聨掳茂录聦氓陆聯氓聣聧氓聫陋猫娄聛猫露聟猫驴聡`32K`莽職聞IO猫炉路忙卤聜茂录聦茅聝陆盲录職猫垄芦忙聥聠忙聢聬忙聸麓氓掳聫莽職聞IO茂录聦盲禄聨忙聲掳忙聧庐莽聹聥盲赂聧茅職戮莽聹聥氓聡潞猫庐戮氓陇聡猫聝陆忙聨楼氓聫聴莽職聞忙聹聙氓陇搂IO氓潞聰猫炉楼氓聹篓[26.95K 32K)莽職聞猫聦聝氓聸麓氓聠聟茫聙聜

氓聹篓[BCC](https://github.com/iovisor/bcc/tree/master)茅隆鹿莽聸庐茅聡聦茂录聦忙聫聬盲戮聸盲潞聠盲赂聙盲赂陋氓路楼氓聟路`biosnoop`茂录聦盲陆驴莽聰篓猫驴聶盲赂陋氓路楼氓聟路氓聫炉盲禄楼忙聤聯氓聡潞忙聺楼忙炉聫盲赂陋忙聫聬盲潞陇氓聢掳猫庐戮氓陇聡莽職聞猫炉路忙卤聜茂录聦氓掳聺猫炉聲盲陆驴莽聰篓盲赂聙盲赂聥茂录聦莽聹聥莽聹聥猫聝陆盲赂聧猫聝陆忙聣戮氓聢掳盲赂聙盲潞聸忙聹聣莽聰篓莽職聞盲驴隆忙聛炉茂录聦盲陆驴莽聰篓莽卢卢盲赂聙盲赂陋氓录聙氓搂聥忙聥聠氓聢聠莽職聞`bs=32K`猫驴聸猫隆聦忙碌聥猫炉聲莽職聞氓聬聦忙聴露忙聤聯氓聫聳盲赂聙盲赂聥IO莽職聞忙聫聬盲潞陇忙聝聟氓聠碌茂录職

```
# /usr/share/bcc/tools/biosnoop -d /dev/vdb
TIME(s)     COMM           PID     DISK      T SECTOR     BYTES  LAT(ms)
0.000000    fio            46743   vdb       R 56         4096      0.18
0.000103    fio            46743   vdb       R 0          28672     0.29

0.004934    fio            46743   vdb       R 120        4096      0.14
0.005040    fio            46743   vdb       R 64         28672     0.25

0.009920    fio            46743   vdb       R 128        28672     0.13
0.010024    fio            46743   vdb       R 184        4096      0.23
#...
# 盲赂聥茅聺垄忙聵炉64K莽職聞忙聝聟氓聠碌
197.473052  fio            48670   vdb       R 0          28672     0.25
197.473153  fio            48670   vdb       R 56         28672     0.35
197.473157  fio            48670   vdb       R 112        8192      0.35

197.477947  fio            48670   vdb       R 128        28672     0.17
197.478051  fio            48670   vdb       R 240        8192      0.28
197.478053  fio            48670   vdb       R 184        28672     0.28

197.482997  fio            48670   vdb       R 256        28672     0.22
197.483098  fio            48670   vdb       R 312        28672     0.33
197.483100  fio            48670   vdb       R 368        8192      0.33
```

氓聫炉盲禄楼莽聹聥氓聢掳盲赂聙盲赂陋32K莽職聞猫炉路忙卤聜茂录聦猫垄芦忙聥聠氓聢聠忙聢聬盲潞聠`28K`+`4K`茫聙聜猫聶陆莽聞露氓聹篓`iostat`茅聡聦莽聹聥氓聢掳莽職聞氓鹿鲁氓聺聡IO氓陇搂氓掳聫忙聵炉16K茂录聦盲陆聠氓庐聻茅聶聟盲赂聤氓聫炉盲禄楼氓聫聭莽聨掳茂录聦莽聹聼忙颅拢氓聢掳猫庐戮氓陇聡莽職聞IO氓鹿露盲赂聧忙聵炉2盲赂陋16K茂录聦忙聧垄盲潞聠氓聟露盲禄聳莽職聞IO氓陇搂氓掳聫莽禄搂莽禄颅氓聨聥忙碌聥茂录聦氓聫聭莽聨掳忙聫聬盲潞陇氓聢掳猫庐戮氓陇聡莽職聞IO氓搂聥莽禄聢忙聴聽忙鲁聲莽陋聛莽聽麓28K猫驴聶盲赂陋芒聙聹氓聺聨芒聙聺茫聙聜

### 猫庐戮氓陇聡莽職聞茅聶聬氓聢露

氓聹篓Linux莽職聞氓聺聴猫庐戮氓陇聡盲赂颅茂录聦忙聹聣氓聡聽盲赂陋茅聡聧猫娄聛莽職聞氓聫聜忙聲掳氓聠鲁氓庐職盲潞聠猫庐戮氓陇聡猫聝陆氓陇聼忙聨楼氓聫聴莽職聞忙聹聙氓陇搂IO氓陇搂氓掳聫茂录聦盲禄聳盲禄卢氓聢聠氓聢芦忙聵炉`max_segments`茂录聦`max_segment_size`氓聮聦`max_sectors_kb`茂录聦盲禄楼NVMe盲赂潞盲戮聥茂录職

```
# cat /sys/class/block/nvme0n1/queue/max_segments
33
# cat /sys/class/block/nvme0n1/queue/max_segment_size
4294967295
# cat /sys/class/block/nvme0n1/queue/max_sectors_kb
128
```

忙聙聨盲鹿聢莽聬聠猫搂拢猫驴聶氓聡聽盲赂陋忙聲掳氓聙录氓聭垄茂录聦氓聮卤盲禄卢氓聫炉盲禄楼莽禄聯氓聬聢`struct bio`莽職聞氓庐職盲鹿聣莽聹聥茂录職

```
struct bio_vec {
       struct page     *bv_page;
       unsigned short  bv_len;
       unsigned short  bv_offset;
};

/*
 * main unit of I/O for the block layer and lower layers (ie drivers)
 */
struct bio {
       struct bio          *bi_next;    /* request queue link */
       struct block_device *bi_bdev;	/* target device */
       unsigned long       bi_flags;    /* status, command, etc */
       unsigned long       bi_opf;       /* low bits: r/w, high: priority */

       unsigned int	bi_vcnt;     /* how may bio_vec's */
       struct bvec_iter	bi_iter;	/* current index into bio_vec array */

       unsigned int	bi_size;     /* total size in bytes */
       unsigned short 	bi_phys_segments; /* segments after physaddr coalesce*/
       unsigned short	bi_hw_segments; /* segments after DMA remapping */
       unsigned int	bi_max;	     /* max bio_vecs we can hold
                                        used as index into pool */
       struct bio_vec   *bi_io_vec;  /* the actual vec list */
       bio_end_io_t	*bi_end_io;  /* bi_end_io (bio) */
       atomic_t		bi_cnt;	     /* pin count: free when it hits zero */
       void             *bi_private;
};
```

忙炉聫盲赂陋氓聺聴氓卤聜IO氓聫炉盲禄楼茅聙職猫驴聡盲赂聙盲赂陋`struct bio`猫隆篓莽陇潞茂录聦猫聙聦IO忙聲掳忙聧庐氓颅聵忙聰戮氓聹篓`struct bio_vec`盲赂颅茂录聦盲潞聨忙聵炉氓掳卤忙聹聣盲潞聠盲赂聙盲赂陋`bio`忙聹聙氓陇職氓聦聟氓聬芦`max_segments`盲赂陋`bio_vec`茂录聦忙炉聫盲赂陋`bio_vec`忙聹聙氓陇職氓聦聟氓聬芦`max_segment_size`莽職聞忙聲掳忙聧庐茂录聦氓聬聦忙聴露茂录聦忙炉聫盲赂陋`bio`忙聹聙氓陇搂盲赂聧猫露聟猫驴聡`max_sectors_kb`茫聙聜

氓聼潞盲潞聨盲赂聤茅聺垄NVMe猫庐戮氓陇聡莽職聞猫驴聶氓聡聽盲赂陋氓聫聜忙聲掳茂录聦盲赂聧茅職戮氓聫聭莽聨掳茂录聦氓聸聽盲赂潞NVMe猫庐戮氓陇聡莽職聞`max_segments*max_segment_size`猫驴聹氓陇搂盲潞聨`max_sectors_kb`茂录聦盲陆聠莽聰卤盲潞聨IO盲赂聧猫聝陆猫露聟猫驴聡`max_sectors_kb`莽職聞氓聙录茂录聦氓聸聽忙颅陇茂录聦氓炉鹿盲潞聨NVMe猫聙聦猫篓聙茂录聦忙聹聙氓陇搂IO氓陇搂氓掳聫盲鹿聼氓掳卤猫垄芦茅聶聬氓聢露氓聹篓盲潞聠`128KB`盲潞聠茫聙聜

茅聜拢`virtio-blk`猫庐戮氓陇聡氓聭垄茂录聼

```
# cat /sys/class/block/vdb/queue/max_segments
7
# cat /sys/class/block/vdb/queue/max_segment_size
65536
# cat /sys/class/block/vdb/queue/max_sectors_kb
1280
```

氓聫炉盲禄楼莽聹聥氓聢掳氓陆聯氓聣聧莽職聞猫驴聶盲赂陋猫庐戮氓陇聡茂录聦忙聹聙氓陇搂IO氓聫聴茅聶聬盲潞聨`max_segments*max_segment_size`茂录聦莽聬聠猫庐潞盲赂聤忙聹聙氓陇搂IO忙聵炉`512K`茂录聦盲陆聠猫驴聶茅聡聦忙聹聣盲赂陋茅聴庐茅垄聵茂录聦`512K`盲鹿聼猫驴聹氓陇搂盲潞聨氓聢職氓聢職`biosnoop`茅聡聦莽聹聥氓聢掳莽職聞`28K`氓聲聤茂录聦猫驴聶氓聫聢忙聵炉盲赂潞盲禄聙盲鹿聢茂录聼

氓聟露氓庐聻莽聹聥氓聢掳`struct bio_vec`氓庐職盲鹿聣莽職聞莽聻卢茅聴麓茂录聦氓掳卤氓潞聰猫炉楼猫聝陆莽聦聹氓聢掳氓聨聼氓聸聽盲潞聠茂录聦氓聸聽盲赂潞盲赂聙猫聢卢忙聝聟氓聠碌盲赂聥茂录聦`bio_vec`茅聝陆盲录職忙聦聡氓聬聭盲赂聙盲赂陋`page茅隆碌`茂录聦茅聜拢忙颅拢氓赂赂忙聝聟氓聠碌盲赂聥茂录聦page氓陇搂氓掳聫氓掳卤忙聵炉`4K`茂录聦氓聸聽忙颅陇氓掳卤盲赂聧猫聝陆盲禄聟盲禄聟莽聹聥max\_segment\_size忙聣聙盲禄拢猫隆篓莽職聞忙聹聙氓陇搂氓聙录茂录聦猫驴聵猫娄聛猫聙聝猫聶聭氓聟路盲陆聯莽職聞茅隆碌氓陇搂氓掳聫...