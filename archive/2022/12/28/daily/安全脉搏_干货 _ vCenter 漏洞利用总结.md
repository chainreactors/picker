---
title: 干货 | vCenter 漏洞利用总结
url: https://www.secpulse.com/archives/194053.html
source: 安全脉搏
date: 2022-12-28
fetch_date: 2025-10-04T02:35:39.294159
---

# 干货 | vCenter 漏洞利用总结

[![](https://www.secpulse.com/wp-content/themes/secpulse2017/img/logo-header.png)](https://www.secpulse.com "安全脉搏")

* [首页](https://www.secpulse.com/)
* [分类阅读](https://www.secpulse.com/archives/category/category)

  #### 脉搏文库

  - [内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)
  - |
  - [代码审计](https://www.secpulse.com/archives/category/articles/code-audit)
  - |
  - [安全文献](https://www.secpulse.com/archives/category/articles/sec-doc)
  - |
  - [Web安全](https://www.secpulse.com/archives/category/articles/web)
  - |
  - [移动安全](https://www.secpulse.com/archives/category/articles/mobile-security)
  - |
  - [系统安全](https://www.secpulse.com/archives/category/articles/system)
  - |
  - [工控安全](https://www.secpulse.com/archives/category/articles/industrial-safety)
  - |
  - [CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)
  - |
  - [IOT安全](https://www.secpulse.com/archives/category/iot-security)
  - |

#### 安全建设

+ [业务安全](https://www.secpulse.com/archives/category/construction/businesssecurity)
+ |
+ [安全管理](https://www.secpulse.com/archives/category/construction/securityissue)
+ |
+ [数据分析](https://www.secpulse.com/archives/category/construction/bigdata)
+ |

#### 其他

+ [资讯](https://www.secpulse.com/archives/category/news)
+ |
+ [漏洞](https://www.secpulse.com/archives/category/vul)
+ |
+ [工具](https://www.secpulse.com/archives/category/tools)
+ |
+ [人物志](https://www.secpulse.com/archives/category/people)
+ |
+ [区块链安全](https://www.secpulse.com/archives/category/exclusive/block_chain_security)
+ |
+ [安全招聘](https://www.secpulse.com/archives/category/hiring)
+ |

- [安全问答](https://www.secpulse.com/newpage/question_list)
- [金币商城](https://www.secpulse.com/shop?donotcachepage=c010349fd98847cb9d6e07d3cbc19288)
- [安全招聘](https://www.secpulse.com/archives/category/hiring)
- [活动日程](https://www.secpulse.com/newpage/activity)
- [live课程](https://www.secpulse.com/live)
- [企业服务](https://duoyinsu.com/service.html)
- [插件社区](https://x.secpulse.com/)

小程序

![脉搏小程序](https://www.secpulse.com/wp-content/themes/secpulse2017/img/wxchat.jpg)
[登录](https://www.secpulse.com/user_login)
|
[注册](https://www.secpulse.com/user-register)

# 干货 | vCenter 漏洞利用总结

[漏洞复现](https://www.secpulse.com/archives/category/articles/%E6%BC%8F%E6%B4%9E%E5%A4%8D%E7%8E%B0)

[HACK\_Learn](https://www.secpulse.com/newpage/author?author_id=8971)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2022-12-27

11,599

# **1 vSphere 背景介绍**

vSphere，ESXi 和 vCenter 辨析：

* VMware Inc

\*\*VMware Inc \*\* 是一家软件公司。它开发了许多产品，尤其是各种云解决方案 。它的云解决方案包括云产品，数据中心产品和桌面产品等。

* vSphere

**vSphere** 是在数据中心产品下的一套软件。vSphere 类似微软的 Office 办公套件，Office 办公套件包含了许多软件如 Word，Excel，Access 等。和 Office 一样，vSphere 也是一个软件的集合。它包括了 vCenter Server， ESXi 和 vSphere client，是整套虚拟化部署方案的总和。

* ESXi

**ESXi** 是 vSphere 中最重要的一个组件。ESXi 是虚拟化服务。所有的虚拟机都是运行在 ESXi 服务上面。

* vSphere Client

**vSphere (web) client** 是一个管理平台，它能够直接管理多个不同的 ESXi 主机，包含许多进阶功能：集群故障转移等。而 ESXi 自带的管理平台只能管理自身所处的 ESXi 主机。而 vSphere client 有更加详细的性能监控，批量更新接管所有 ESXi 系统版本。通过资源池也可以规划虚拟机资源占用。

* vCenter Server

在 ESXi 6.0 之前是通过 C/S 架构来管理 ESXi 集群的，没有 web 端，且安装环境较为苛刻，必须为 Server 版本的服务器才可以安装。在 6.0 版本之后，官方已经取消了 C/S 架构的客户端，转而采用了 web 管理平台，又被称之为 vSphere web client。而部署了 vSphere web client 的服务器被称之为 **vCenter Server**。

官方推荐将打包好的 Client 与 Server 应用部署在 VMware 自家的 Photon 系统下，其安装包命名为：VMware vCenter Server Appliance，简称为：**VCSA**。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194053-1672109847.jpeg "https://geekby.oss-cn-beijing.aliyuncs.com/MarkDown/202205101547624.png-water_print")

## **2 常见漏洞**

### **2.1 版本信息探测**

通过调用 VMWare Sphere 组件的 SOAP API，可以获取其版本信息，XML 数据如下：

```
<?xml version="1.0" encoding="UTF-8"?><soap:Envelopexmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"xmlns:xsd="http://www.w3.org/2001/XMLSchema"xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><soap:Header><operationID>00000001-00000001</operationID></soap:Header><soap:Body><RetrieveServiceContentxmlns="urn:internalvim25"><_this xsi:type="ManagedObjectReference" type="ServiceInstance">ServiceInstance</_this></RetrieveServiceContent></soap:Body></soap:Envelope>
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194053-1672109848.png)

Nuclei 相关模板：

`/nuclei-templates/technologies/vmware/vmware-detect.yaml`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194053-1672109850.png)

### **2.2 任意文件读取**

影响版本：`Vmware vCenter Server <= 6.5.0`

Fofa Dork：`title="ID_VC_Welcome"`

VMware vCenter 存在任意文件读取漏洞，可读取 vCenter 配置文件获得管理帐号密码进而控制 vCenter 平台及其管理的虚拟机集群。

由于 EAM 用户运行该存在漏洞的服务（非域用户），因此不存在 NTLM Relay 等中继攻击风险。

由于不同的系统版本，数据库配置文件（`vcdb.properties`）存放位置不同，根据官方文档，大体可以分为：

对于 vCenter Server 5.5 及更低版本：

Windows 2008 - `C:ProgramDataVMwareVMware VirtualCenter`

其他 Windows 版本 -

`C:Documents and SettingsAll UsersApplication DataVMwareVMware VirtualCenter`

对于 vCenter Server 6.0、6.5、6.7：

`C:ProgramDataVMwarevCenterServercfgvmware-vpx`

POC：

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` GET /eam/vib?id={{path}}vcdb.properties HTTP/1.1 Host: {{Hostname}} ``` |

nuclei 中对应的 poc：

`/nuclei-templates/vulnerabilities/vmware/vmware-vcenter-lfi.yaml`

`/nuclei-templates/vulnerabilities/vmware/vmware-vcenter-lfi-linux.yaml`

### **2.3 CVE-2021-21972**

#### **2.3.1 漏洞利用**

默认启用的 vROps 插件（com.vmware.vropspluginui.mvc）ServicesController 类的 uploadova 接口存在未授权访问，可利用路径穿越将文件解压至特定目录实现 getshell。

影响版本：

`7.0 <= vCenter Server < 7.0 U1c`

`6.7 <= vCenter Server < 6.7 U3l`

`6.5 1e <= vCenter Server < 6.5 U3n`

`4.x <= Cloud Foundation (vCenter Server) < 4.2`

`3.x <= Cloud Foundation (vCenter Server) < 3.10.1.2`

POC：

`/nuclei-templates/cves/2021/CVE-2021-21972.yaml`

EXP：

https://www.exploit-db.com/exploits/49602

#### **2.3.2 漏洞分析**

定位到存在漏洞的 Jar 包：

`/etc/vmware/vsphere-ui/vc-packages/vsphere-client-serenity/com.vmware.vrops.install-6.x.x.xx000/plugins/vropsplugin-service.jar`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194053-1672109859.png)

注意到第 463 行，直接将 TAR 的文件名与 `/tmp/unicorn_ova_dir` 拼接并写入文件。如果文件名内存在 `../`，可将文件解压至 `vsphere-ui` 用户有权限的目录。切入该用户并查找可写目录：

```
su vsphere-ui
find / -writable -type d |& grep -v "Permission denied"
```

其中 `.ssh` 目录可写，因此，最为常见的思路就是写入公钥，并利用该用户登录。但是该方式存在一定的局限，首先看一下 shadow 文件：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194053-1672109862.jpeg "https://geekby.oss-cn-beijing.aliyuncs.com/MarkDown/202205061953700.png-water_print")

看到密码过期时间为 90 天，因此在安装 90 天后即使写入了公钥登录也会提示密码过期，需要提供原密码并修改密码。此外，`vsphere-ui` 用户的第二项为 `!`，这表示该用户未设置密码（与空密码不同），所以也就没法修改密码，因此，当密钥过期后，就无法再次登录。

另一种思路就是写入 Webshell。首先需要遍历找出存在有 jsp 的 web.xml 并且目录可写：

```
grep "<servlet-name>jsp</servlet-name>" $(find / -name "*web.xml")
```

最终确定了如下几个 linux 下的存放位置：

```
# vCenter 6.5/6.7 < 13010631/usr/lib/vmware-vsphere-ui/server/work/deployer/s/global/%d/0/h5ngc.war/resources/<thefile>
# vCenter 6.7 >= 13010631/usr/lib/vmware-vsphere-ui/server/static/resources/libs/<thefile>
# vCenter 7.0，其中 resources15863815 动态生成，可以通过访问 /ui 可以获取该目录信息/usr/lib/vmware-vsphere-ui/server/static/resources15863815/libs/<thefile>
```

由 `/usr/lib/vmware-vsphere-ui/server/configuration/tomcat-server.xml` 查到监听端口为 5090，再由 rhttpproxy 反向代理找到 web 访问路径：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194053-16721098621.jpeg "https://geekby.oss-cn-beijing.aliyuncs.com/MarkDown/202205062006466.png-water_print")

最后将 webshell 释放至

 `/usr/lib/vmware-vsphere-ui/server/work/deployer/s/global/xx/0/h5ngc.war/resources/` 目录或其子目录，即可解析并由 `https://IP/ui/resources/webshell.jsp` 访问

该路径中的 xx 并非是固定数值，会随着重装重启等行为发生改变，所以构造上传包时可以暴力批量添加，并探测是否上传成功。

此外，6.7U2 及之后的版本，会在服务启动时判断如果存在 work 目录就删除，也就是说 Web 是跑在内存里面的。这时对于 6.7U2 及更新的 6.7 版本可以将 webshell 释放至 `/usr/lib/vmware-vsphere-ui/server/static/resources/libs/` 目录作为后门，待其重启后会被加载运行。对于 7.0 版本 static 后面的 resources 会跟一串动态数字路径，能够在请求的返回包中获取到。

针对...