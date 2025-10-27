---
title: 伪装成ToDesk安装程序加载后门盗取数字货币
url: https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247489656&idx=1&sn=b2693f2eecfd194407c52a70a20646ab&chksm=902fb750a7583e465c5ec31f000f5f3d8bf101a39b8b8704794a8cb29233ffbd4c8b3fd6b903&scene=58&subscene=0#rd
source: 安全分析与研究
date: 2024-12-10
fetch_date: 2025-10-06T19:39:55.709118
---

# 伪装成ToDesk安装程序加载后门盗取数字货币

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmVRnnmoyjHxactdjqxVNjD1rlhFOJEU0I43o4Wp5t6yPibNXdUKrGR7BxMibmLaicm9jzMxlb8xCem6g/0?wx_fmt=jpeg)

# 伪装成ToDesk安装程序加载后门盗取数字货币

原创

pandazhengzheng

安全分析与研究

**安全分析与研究**

专注于全球恶意软件的分析与研究

前言概述

原文首发出处：

https://xz.aliyun.com/t/16552

先知社区 作者：熊猫正正

近日有微信朋友发给笔者一个样本，让笔者有空可以看看，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVbiaw4cwibTHNI8VjO8LMyztTcQB3j7QK9zboxkDqPZTTBAEMRw8Y6PiaDMckibLcQ1icS3Ba5XT42lZA/640?wx_fmt=png)

分析之后，发现样本还挺新的，而且有一定的对抗性，通过捆绑ToDesk安装程序加载远控后门盗取数字货币等信息，分享出来供大家学习参考。

详细分析

1.初始样本为使用Setup Factory打包的安装程序，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVbiaw4cwibTHNI8VjO8LMyztS2e6b5m0hicGnw9sib3WNlIg4PO3BeLkc0XHrADiaddGvVctpPjtOMyKA/640?wx_fmt=png)

2.安装完成之后，在安装目录的dev目录下生成相应的恶意文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVbiaw4cwibTHNI8VjO8LMyztJXcq05a4icyx80qDSPqy3jJtMDCQjbWtGxEotgmJ6mgJiaoicQ1YHCZiaw/640?wx_fmt=png)

3.样本采用白+黑的方式加载恶意模块，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVbiaw4cwibTHNI8VjO8LMyzt9Aee6twRkorEhIaM2aKRwaj189kSl2pqT2y5icVAyPMibPlhvhhicAu7Q/640?wx_fmt=png)

4.恶意模块采用Delphi语言编写，编译时间为2024年10月30日，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVbiaw4cwibTHNI8VjO8LMyzt6j9wQZ0M9yqmLucEwN7m0rObGLD1LUsQgo8VQjibHwX5n6XknxJYffw/640?wx_fmt=png)

5.导出函数都被混淆了，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVbiaw4cwibTHNI8VjO8LMyzt4kC0s4QWQgQZZ0OoTLkMQPCSzBojzx2HwSuCZM2JfDYPvbxvxw6ZUg/640?wx_fmt=png)

6.笔者注意到有一个导出函数比较特别IsWindowServer，通过分析发现恶意代码就隐藏在该导出函数当中，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVbiaw4cwibTHNI8VjO8LMyztWrgHtbhtWRFTI8NB1DNFokB3PIHJ96G0EIibExvU1YCscbP8UILB62g/640?wx_fmt=png)

7.读取同目录下的Prgkectiodn.u6mg文件加密数据到内存，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVbiaw4cwibTHNI8VjO8LMyztvmQb4ozxBmfHUzWPGvmb6gPVJU7qdctpWQRVujF3emjUNvhba0TnoA/640?wx_fmt=png)

8.通过异或算法解密加密的数据，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVbiaw4cwibTHNI8VjO8LMyztBjMLpbZEYNkMbR1JVvAibNbSPPcT5zibMYDNqfTeJtZ0O2GmMnia2vyuw/640?wx_fmt=png)

9.解密算法，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVbiaw4cwibTHNI8VjO8LMyzt4biaHL4V9bus2lYpgicbLvmVCaxcDna3J80GSia5NGc7N4dMQSZx1rrmQ/640?wx_fmt=png)

10.解密出来的PayLoad，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVbiaw4cwibTHNI8VjO8LMyzttkuqcCSiaYm63gPl6Xz6ro7ibq6RIlbO3EGLXUF49d3Ho9DQVJbUoLXg/640?wx_fmt=png)

11.解密出来的PayLoad也是使用Delphi语言编写，编译时间为2024年10月30日，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVbiaw4cwibTHNI8VjO8LMyzt1569IBpxsMTdKWjeWehicDwMFRG8lqzAf3AVfKFxoibrcOTPoOiaiaSNzg/640?wx_fmt=png)

12.调用执行该PayLoad的M78E27BDC3EF60E302EDD6DD505E10A2F22D17DD23AF703GYT导出函数，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVbiaw4cwibTHNI8VjO8LMyztytP7eqNa3jqAGniaHoVrL3x0YjtTCSsbffkl4TajD2Yibm9WHeawtp5w/640?wx_fmt=png)

13.创建互斥变量GREHERTHE27BDE2361E06CCD30E00B3AFDGFDG5，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVbiaw4cwibTHNI8VjO8LMyztqf3ialQwV0m86Gia1SWCORHKcqx9XNfSbM7SxmIRH1icys3ibmrqicibiag7A/640?wx_fmt=png)

14.设置相应的自启动注册表项，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVbiaw4cwibTHNI8VjO8LMyztLiaZ5p2DBJnvVMKnta4Qgo2Ckiatlxk6EJAibGsQmibeT1UHYEd3Vkw3UA/640?wx_fmt=png)

15.设置完成之后，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVbiaw4cwibTHNI8VjO8LMyztH4UnLSxummwiaWzXic2hrVtA2s5HoxrkY1Yyk4z8CzSLjloWLibUkVF2Q/640?wx_fmt=png)

16.获取操作系统相关信息，操作系统版本、类型、GUID、BIOS信息等，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVbiaw4cwibTHNI8VjO8LMyzt8q21qAhc683ibCWqXiaYtjHIf9ye6HMoNibge8ZqhaHtMAVxBW6oGYDKQ/640?wx_fmt=png)

17.PayLoad是一个远控类的模块，通过不同的指令，执行不同的操作，一共有几十个不同的指令执行不同的操作，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVbiaw4cwibTHNI8VjO8LMyzthEVgOEff40KjG8TftIic25mOqlMrVEhRicC8bibItaLm26M1LpTOKXu9A/640?wx_fmt=png)

18.上面指令非常多，笔者重点关注一下数字货币钱包操作，盗取系统上的数字货币钱包，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVbiaw4cwibTHNI8VjO8LMyztP7q8UmNVNbNbKtbCZ6eJp8eBjnibQBJlKVr1V3Uk7aLtX6vXtYu78JA/640?wx_fmt=png)

19.通过Chrome扩展程序ID信息等，定位操作系统中存在的数字货币钱包信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVbiaw4cwibTHNI8VjO8LMyzth3ZkL7RfSInHiaIykEYtusZfUeo6IuIgOtYyyfgkgTqD90CezvM6Ukw/640?wx_fmt=png)

20.盗取用户浏览器相关数据，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVbiaw4cwibTHNI8VjO8LMyztY2evYmRN2XlqjC3Aj8Q6ZsXqZggrQic6Iqxlrad8VYoeic3XDhUic7Qbw/640?wx_fmt=png)

21.盗取系统用户ETH和TRON数字货币，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVbiaw4cwibTHNI8VjO8LMyztQ7fKz1Rq8AlVfGDpOXDH8bsndvD5g5EibX8pKWXW8TfSiboZP5b231eQ/640?wx_fmt=png)

22.获取系统安全软件信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVbiaw4cwibTHNI8VjO8LMyzt6ZILhsxibVyWRYtdq0hEytJ1kILmy1B11Q9QbFicnoOjq3Qzeqib5GZeA/640?wx_fmt=png)

23.黑客C2域名为golomee.com，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVbiaw4cwibTHNI8VjO8LMyztpOGUcjia1jvicia2dgEPSkNYzkAvnrqbH3REFh8lvHFXZBD03icxphETpA/640?wx_fmt=png)

通过威胁情报平台查询，该C2域名被标记为“黑猫”黑产组织，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVbiaw4cwibTHNI8VjO8LMyztUD21cn1ic7qevw1ticI1NAx4J7hNVD0OrnPibZVib82zibRRwLiaNk6oRTBw/640?wx_fmt=png)

24.笔者从程序中提取出相关数字货币钱包Chrome扩展程序ID信息，如下所示：

Wallet NameExtension ID

MetaMask

nkbihfbeogaeaoehlefnkodbefgpgknn

MetaMask

ejbalbakoplchlghecdalmeeeajnimhm

TronLink

ibnejdfjmmkpcnlpebklmnkoeoihofec

Phantom

bfnaelmomeimhlpmgjnjophhpkkoljpa

Terra Station

aiifbnbfobpmeekipheeijimdpnlpgpp

Terra Station

ajkhoeiiokighlmdnlakpjfoobnjinie

Keplr

dmkamcknogkgcdfhhbddcghachkejeap

Keplr

efknohjclbjfppcmniflbmnokbihoofp

Math Wallet

afbcbjpbpfadlkmhmclhkeeodmamcflc

Math Wallet

dfeccadlilpndjjohbjdblepmjeahlmm

Binance

fhbohimaelbohpjbbldcngcnapndodjp

Binance

mkinohlchpfiljfihdblneojpbpchmad

TokenPocket

mfgccjchihfkkindfppnaooecgfneiii

Trust Wallet

egjidjbpglichdcondbcbdnbeeppgdph

Trust Wallet

glcnemilkfekippdjmhghgakcbmkejnk

OuYiWEB3 Wallet

mcohilncbfahbmgdjkbpemcciiolgcge

Coin98 Wallet

aeachknmefphepccionboohckonoeemg

Math Wallet

afbcbjpbpfadlkmhmclhkeeodmamcflc

Math Wallet

dfeccadlilpndjjohbjdblepmjeahlmm

Wombat Gaming Wallet

amkmjjmmflddogmhpjloimipbofnfjih

Pontem Aptos Wallet

phkbamefinggmakgklpkljjmgibohnba

Pontem Aptos Wallet

phkbamefinggmakgklpkljjmgibohnba

X Wallet

bofddndhbegljegmpmnlbhcejofmjgbn

Keeper Wallet

lpilbniiabackdjcionkobglmddfbcjo

Keeper Wallet

hdpempkibblfcglmkkakkpnjmbnebaki

TON Wallet

nphplpgoakhhjchkkhmiggakijnkhfnd

TON Wallet

dgegbhgbijbhkmkacomdlogdkacokpam

Leap Terra Wallet

aijcbedoijmgnlmjeegjaglmepbmpkpi

XDEFI Wallet

hmeobnfnfcmdkdcmlblgagmfpfboieaf

Maiar DeFi Wallet

dngmlblcodfobpdpecaadgfbcggfjfnm

Ronin Wallet

fnjhmkhhmkbjkkabndcnnogagogbneec

Ronin Wallet

kjmoohlgokccodicjjfebfomlbljgfhk

Oasis Wallet

ppdadbejkmjnefldpcdjhnkpbjkikoip

XCoinbase Wallet

hnfanknocfeofbddgcijnmhnfnkdnaad

bitkeep Wallet

jiidiaalihmmhddjgbnbgdfflelocpak

Argent X

dlcobpjiigpikoobohmabehhmhfoodbb

Coinhub

jgaaimajipbpdogpdglhaphldakikgef

FINX

ejehodfgjhiadihgjdkgffciiepfdeep

Plug

cfbfdhimifdmdehjmkdobpcjfefblkjm

Rabby

acmacodkjbdgmoleebolmdjonilkdbch

Sui Wallet

opcgpfmipidbgpenhmajoajpbobppdil

Temple Tezos Wallet

ookjlbkiijinhpmnjffcofjonbfbgaoc

Zecrey

ojbpcbinjmochkhelkflddfnmcceomdi

Martian Aptos Wallet

efbglgofoippbgcjepnhiblaibcnclgk

Petra Aptos Wallet

ejjladinnckdgjemekebdpeokbikhfci

Fewcha Wallet

ebfidpplhabeedpnhjnobghokpiioolj

Polygon Wallet

bjnlkgkghpnjgkonekahiadjmgjpmdak

Typhon Wallet

kfdniefadaanbjodldohaedphafoffoh

Nitrogen Wallet

ajbieehikidekihmekmbdmdconafgkie

Meteor Wallet

pcndjhkinnkaohffealmlmhaepkpmgkb

JustLiquidity Wallet

cmbagcoinhmacpcgmbiniijboejgiahi

Nami

lpfcbjknijpeeillifnkikgncikgfhdo

Wallet Crypto BTC ETH

glbgnkopdilgbjchligmlbmhkgohggoj

Carbon Wallet

pnphepacpjpklpbacfmebicbgndobakn

Saifu Solana Wallet

ejdabmcenoflojakpkgjnilnohjoobac

ZEON Wallet

gbjepgaebckfidagpfeioimheabiohmg

MWC Wallet

ahhdnimkkpkmclgcnbchlgijhmieongp

Stash Wallet

incepomdpmhakfkbifbhhmbjeofohaka

Avana Wallet

ajnodjmfajgabkmeididajpkoobeiofn

Auvitas Wallet

klbgaboailigngkiifaglicepkfckppa

Sentinel T4L3NT Wallet

bpefpmecbepflicbncadgnhdaapjgnpk

USDC Wallet

pkjmoihlmlhhkahcplhijafhcioaciih

UMI Wa...