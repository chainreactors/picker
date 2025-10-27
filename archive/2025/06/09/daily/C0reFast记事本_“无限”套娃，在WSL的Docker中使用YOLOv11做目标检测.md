---
title: “无限”套娃，在WSL的Docker中使用YOLOv11做目标检测
url: https://www.ichenfu.com/2025/06/08/yolo11-on-wslg-docker/
source: C0reFast记事本
date: 2025-06-09
fetch_date: 2025-10-06T22:50:25.073931
---

# “无限”套娃，在WSL的Docker中使用YOLOv11做目标检测

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

1. [1. 莽隆庐猫庐陇WSLg莽職聞忙颅拢莽隆庐氓庐聣猫拢聟](#%E7%A1%AE%E8%AE%A4WSLg%E7%9A%84%E6%AD%A3%E7%A1%AE%E5%AE%89%E8%A3%85)
2. [2. 氓庐聣猫拢聟NVIDIA莽職聞氓庐鹿氓聶篓猫驴聬猫隆聦莽聨炉氓垄聝](#%E5%AE%89%E8%A3%85NVIDIA%E7%9A%84%E5%AE%B9%E5%99%A8%E8%BF%90%E8%A1%8C%E7%8E%AF%E5%A2%83)
3. [3. 氓聹篓Docker茅聡聦盲陆驴莽聰篓YOLOv11](#%E5%9C%A8Docker%E9%87%8C%E4%BD%BF%E7%94%A8YOLOv11)
4. [4. 氓庐聻忙聴露猫搂聠茅垄聭忙拢聙忙碌聥](#%E5%AE%9E%E6%97%B6%E8%A7%86%E9%A2%91%E6%A3%80%E6%B5%8B)
5. [5. 忙聙禄莽禄聯](#%E6%80%BB%E7%BB%93)

茅聶聢氓颅職

[111
忙聴楼氓驴聴](/archives/)

[15
氓聢聠莽卤禄](/categories/)

[249
忙聽聡莽颅戮](/tags/)

[GitHub](https://github.com/C0reFast "GitHub 芒聠聮 https://github.com/C0reFast")

E-Mail

[Weibo](https://weibo.com/c0refast "Weibo 芒聠聮 https://weibo.com/c0refast")

猫碌聻氓聤漏氓聲聠

茅聯戮忙聨楼

* [莽聢卤氓录聙忙潞聬](https://www.aikaiyuan.com/ "https://www.aikaiyuan.com/")
* [盲赂聙氓聠聣氓聠聧](https://blog.yiranzai.top/ "https://blog.yiranzai.top/")
* [PikachuWorld](https://www.cnblogs.com/pikachuworld/ "https://www.cnblogs.com/pikachuworld/")

# 芒聙聹忙聴聽茅聶聬芒聙聺氓楼聴氓篓聝茂录聦氓聹篓WSL莽職聞Docker盲赂颅盲陆驴莽聰篓YOLOv11氓聛職莽聸庐忙聽聡忙拢聙忙碌聥

氓聫聭猫隆篓盲潞聨
2025氓鹿麓6忙聹聢8忙聴楼 19:34

氓聢聠莽卤禄盲潞聨

[忙聴楼氓赂赂忙聤聵猫聟戮](/categories/%E6%97%A5%E5%B8%B8%E6%8A%98%E8%85%BE/)

茅聵聟猫炉禄忙卢隆忙聲掳茂录職

氓聣聧氓聡聽氓陇漏氓聛露莽聞露氓聫聭莽聨掳茂录聦Windows 11莽職聞WSL2氓聫炉盲禄楼茅聙職猫驴聡WSLg忙聺楼忙聴聽莽录聺盲陆驴莽聰篓GUI氓潞聰莽聰篓茫聙聜莽卤禄盲录录忙聨篓莽聬聠/猫庐颅莽禄聝莽颅聣盲禄禄氓聤隆茂录聦茅聝陆盲赂聧氓聹篓猫炉聺盲赂聥茂录聦猫驴聶莽聻卢茅聴麓氓聥戮猫碌路盲潞聠忙聢聭莽職聞氓楼陆氓楼聡氓驴聝茂录聦氓聠鲁氓庐職猫炉聲猫炉聲氓戮庐猫陆炉忙聫聬盲戮聸莽職聞猫驴聶盲赂陋莽楼聻氓楼聡氓聤聼猫聝陆茫聙聜氓聟露氓庐聻氓戮庐猫陆炉氓聹篓2021氓鹿麓氓掳卤氓聫聭氓赂聝盲潞聠WSLg茂录聦莽聨掳氓聹篓氓路虏莽禄聫忙聵炉2025氓鹿麓盲潞聠茂录聦氓聢職氓聢職氓录聙氓搂聥忙聤聵猫聟戮盲鹿聼莽庐聴忙聵炉氓聬聨莽聼楼氓聬聨猫搂聣盲潞聠茫聙聜

WSL忙聰炉忙聦聛GUI氓潞聰莽聰篓氓聫陋猫聝陆莽庐聴忙聵炉WSLg莽職聞盲赂聙盲赂陋忙聹聙莽庐聙氓聧聲莽職聞氓聤聼猫聝陆盲潞聠茂录聦氓陆聯忙露聣氓聫聤忙篓隆氓聻聥猫庐颅莽禄聝忙聢聳猫聙聟GPU氓聤聽茅聙聼忙聴露茂录聦GPU茅漏卤氓聤篓猫驴聵忙聹聣CUDA莽颅聣莽颅聣莽聸赂氓聟鲁莽職聞茅聟聧莽陆庐氓掳卤盲录職氓聫聵氓戮聴氓陇聧忙聺聜猫碌路忙聺楼茫聙聜忙聢聭氓鹿露盲赂聧氓赂聦忙聹聸氓聸聽盲赂潞芒聙聹忙聤聵猫聟戮芒聙聺猫驴聶盲鹿聢盲赂聙盲赂聥茂录聦氓掳卤忙聤聤忙聢聭莽職聞WSL莽聨炉氓垄聝忙聬聻氓戮聴盲赂聙氓聸垄莽鲁聼茂录聦猫驴聶忙聴露氓聙聶茂录聦Docker莽職聞盲禄路氓聙录氓掳卤盲陆聯莽聨掳氓聡潞忙聺楼盲潞聠茫聙聜氓聢漏莽聰篓Docker茂录聦氓聫炉盲禄楼氓聹篓盲赂聧盲驴庐忙聰鹿莽聨掳忙聹聣WSL莽聨炉氓垄聝莽職聞忙聝聟氓聠碌盲赂聥茂录聦氓驴芦茅聙聼忙聬颅氓禄潞盲赂聙盲赂陋茅職聰莽娄禄莽職聞莽聨炉氓垄聝忙聺楼氓聛職盲潞聸莽庐聙氓聧聲莽職聞忙碌聥猫炉聲茫聙聜忙聢聭氓聠鲁氓庐職盲陆驴莽聰篓YOLO盲陆聹盲赂潞忙碌聥猫炉聲氓炉鹿猫卤隆茂录聦莽聹聥莽聹聥氓聹篓WSL+WSLg+Docker莽職聞氓聹潞忙聶炉盲赂聥茂录聦YOLO猫驴聵猫聝陆盲赂聧猫聝陆氓戮聢氓楼陆莽職聞氓路楼盲陆聹茂录聦忙颅拢莽隆庐盲陆驴莽聰篓忙聢聭莽職聞GPU猫驴聸猫隆聦氓聤聽茅聙聼茫聙聜

## 莽隆庐猫庐陇WSLg莽職聞忙颅拢莽隆庐氓庐聣猫拢聟

莽聬聠猫庐潞盲赂聤茂录聦WSLg忙聵炉WSL茅禄聵猫庐陇氓聬炉莽聰篓莽職聞氓聤聼猫聝陆茂录聦氓陆聯盲陆聽氓庐聣猫拢聟氓庐聦忙聢聬WSL2茂录聦氓鹿露盲赂聰氓庐聣猫拢聟盲潞聠Ubuntu莽颅聣Linux氓聫聭猫隆聦莽聣聢氓聬聨茂录聦氓掳卤氓聫炉盲禄楼莽聸麓忙聨楼盲陆驴莽聰篓GUI氓潞聰莽聰篓盲潞聠茫聙聜氓聟路盲陆聯莽職聞氓庐聣猫拢聟忙聳鹿忙鲁聲茂录聦猫驴聶茅聡聦氓掳卤盲赂聧氓陇職猫炉麓盲潞聠茂录聦忙炉聲莽芦聼氓戮庐猫陆炉莽職聞忙聳聡忙隆拢[氓聹篓茅聙聜莽聰篓盲潞聨 Linux 莽職聞 Windows 氓颅聬莽鲁禄莽禄聼盲赂聤猫驴聬猫隆聦 Linux GUI 氓潞聰莽聰篓](https://learn.microsoft.com/zh-cn/windows/wsl/tutorials/gui-apps)氓聠聶莽職聞茅聺聻氓赂赂莽職聞猫炉娄莽禄聠茂录職

氓庐聣猫拢聟氓庐聦忙聢聬氓聬聨茂录聦氓娄聜忙聻聹WSLg猫垄芦忙颅拢莽隆庐氓聬炉莽聰篓莽職聞猫炉聺茂录聦氓潞聰猫炉楼氓掳卤氓聫炉盲禄楼莽聹聥氓聢掳茂录職

```
# mount|grep wslg
none on /mnt/wslg type tmpfs (rw,relatime)
/dev/sdc on /mnt/wslg/distro type ext4 (ro,relatime,discard,errors=remount-ro,data=ordered)
none on /mnt/wslg/versions.txt type overlay (rw,relatime,lowerdir=/systemvhd,upperdir=/system/rw/upper,workdir=/system/rw/work)
none on /mnt/wslg/doc type overlay (rw,relatime,lowerdir=/systemvhd,upperdir=/system/rw/upper,workdir=/system/rw/work)
tmpfs on /mnt/wslg/run/user/1000 type tmpfs (rw,nosuid,nodev,relatime,size=809692k,nr_inodes=202423,mode=700,uid=1000,gid=1000)
```

盲赂聨忙颅陇氓聬聦忙聴露茂录聦氓聹篓盲赂聧莽聰篓氓庐聣猫拢聟盲禄禄盲陆聲Linux莽聣聢忙聹卢GPU茅漏卤氓聤篓莽職聞忙聝聟氓聠碌盲赂聥茂录聦氓潞聰猫炉楼盲鹿聼氓聫炉盲禄楼忙颅拢莽隆庐猫炉聠氓聢芦氓聢掳GPU猫庐戮氓陇聡茂录職

```
# which nvidia-smi
/usr/lib/wsl/lib/nvidia-smi
# nvidia-smi
Sun Jun  8 19:59:36 2025
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 560.35.02              Driver Version: 560.94         CUDA Version: 12.6     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA GeForce RTX 4070 ...    On  |   00000000:2B:00.0  On |                  N/A |
|  0%   45C    P8              7W /  285W |     895MiB /  16376MiB |      4%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI        PID   Type   Process name                              GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|    0   N/A  N/A        25      G   /Xwayland                                   N/A      |
+-----------------------------------------------------------------------------------------+
```

盲禄楼忙聢聭莽職聞猫驴聶氓聫掳盲赂禄忙聹潞盲赂潞盲戮聥茂录聦氓聫炉盲禄楼莽聹聥氓聢掳`nvidia-smi`氓聫炉盲禄楼忙颅拢氓赂赂猫炉聠氓聢芦氓聢掳GPU茂录聢莽聰職猫聡鲁nvidia-smi盲鹿聼盲赂聧忙聵炉忙聢聭氓庐聣猫拢聟莽職聞茂录聦氓戮庐猫陆炉莽聸麓忙聨楼氓赂庐忙聢聭忙聦聜猫陆陆盲潞聠茂录聣

氓聠聧猫炉聲猫炉聲猫驴聬猫隆聦盲赂聙盲赂陋GUI氓潞聰莽聰篓茂录職

```
# sudo apt install -y x11-apps
# /usr/bin/xcalc
```

![xcalc](/images/yolo11-on-wslg-docker/xcalc.png)

## 氓庐聣猫拢聟NVIDIA莽職聞氓庐鹿氓聶篓猫驴聬猫隆聦莽聨炉氓垄聝

莽聰卤盲潞聨猫娄聛盲陆驴莽聰篓Docker氓鹿露盲赂聰猫驴聵茅聹聙猫娄聛氓聹篓Docker茅聡聦盲陆驴莽聰篓GPU茂录聦Docker莽職聞氓庐聣猫拢聟忙炉聰猫戮聝莽庐聙氓聧聲茂录聦氓聹篓Ubuntu茅聡聦茂录聦莽聸麓忙聨楼`sudo apt install -y docker.io`氓聧鲁氓聫炉茂录聦猫聙聦氓炉鹿盲潞聨忙聢聭莽職聞NVIDIA忙聵戮氓聧隆忙聺楼猫炉麓茂录聦猫驴聵茅聹聙猫娄聛氓庐聣猫拢聟NVIDIA莽職聞氓庐鹿氓聶篓猫驴聬猫隆聦莽聨炉氓垄聝茂录聦猫驴聶茅聡聦氓聫炉盲禄楼氓聫聜猫聙聝NVIDIA莽職聞忙聳聡忙隆拢[Installing the NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)猫驴聸猫隆聦氓庐聣猫拢聟茂录聦氓庐聣猫拢聟氓庐聦忙聢聬盲鹿聥氓聬聨茂录聦氓聫炉盲禄楼猫路聭盲赂聙盲赂陋莽庐聙氓聧聲莽職聞忙碌聥猫炉聲茂录聦莽隆庐猫庐陇盲赂聙盲赂聥氓庐聣猫拢聟忙聵炉氓聬娄忙聢聬氓聤聼茂录聦盲禄楼氓聫聤氓庐鹿氓聶篓茅聡聦忙聵炉氓聬娄氓聫炉盲禄楼忙颅拢莽隆庐猫炉聠氓聢芦氓鹿露猫掳聝莽聰篓氓聢掳GPU茂录職

```
# sudo docker run --gpus all --runtime=nvidia nvcr.io/nvidia/k8s/cuda-sample:nbody nbody -gpu -benchmark
Run "nbody -benchmark [-numbodies=<numBodies>]" to measure performance.
        -fullscreen       (run n-body simulation in fullscreen mode)
        -fp64             (use double precision floating point values for simulation)
        -hostmem          (stores simulation data in host memory)
        -benchmark        (run benchmark to measure performance)
        -numbodies=<N>    (number of bodies (>= 1) to run in simulation)
        -device=<d>       (where d=0,1,2.... for the CUDA device to use)
        -numdevices=<i>   (where i=(number of CUDA devices > 0) to use for simulation)
        -compare          (compares simulation results running once on the default GPU and once on the CPU)
        -cpu              (run n-body simulation on the CPU)
        -tipsy=<file.bin> (load a tipsy model file for simulation)

NOTE: The CUDA Samples are not meant for performance measurements. Results may vary when GPU Boost is enabled.

> Windowed mode
> Simulation data stored in video memory
> Single precision floating point simulation
> 1 Devices used for simulation
MapSMtoCores for SM 8.9 is undefined.  Default to use 128 Cores/SM
MapSMtoArchName for SM 8.9 is undefined.  Default to use Ampere
GPU Device 0: "Ampere" with compute capability 8.9

> Compute 8.9 CUDA device: [NVIDIA GeForce RTX 4070 Ti SUPER]
67584 bodies, total time for 10 iterations: 41.515 ms
= 1100.228 billion interactions per second
= 22004.559 single-precision GFLOP/s at 20 flops per interaction
```

氓聫炉盲禄楼莽聹聥氓聢掳氓聹篓氓庐鹿氓聶篓茅聡聦莽聹聥氓聢掳氓鹿露盲赂聰盲陆驴莽聰篓盲潞聠忙聢聭莽職聞GPU茫聙聜

## 氓聹篓Docker茅聡聦盲陆驴莽聰篓YOLOv11

忙聨楼盲赂聥忙聺楼氓掳卤氓聫炉盲禄楼氓聹篓Docker茅聡聦盲陆驴莽聰篓YOLOv11盲潞聠茫聙聜莽聰卤盲潞聨氓庐聵忙聳鹿氓路虏莽禄聫莽禄聶忙聢聭盲禄卢忙聣聯氓楼陆盲潞聠[Docker茅聲聹氓聝聫](https://hub.docker.com/r/ultralytics/ultralytics)茂录聦忙聣聙盲禄楼氓聫陋茅聹聙猫娄聛忙聥聣氓聫聳茅聲聹氓聝聫氓鹿露猫驴聬猫隆聦氓聧鲁氓聫炉茂录聦氓聸聽盲赂潞忙聢聭猫驴聵忙聝鲁猫聝陆氓掳聠忙聨篓莽聬聠莽禄聯忙聻聹氓庐聻忙聴露莽職聞忙聵戮莽陇潞氓聡潞忙聺楼茂录聦忙聣聙盲禄楼猫驴聵茅...