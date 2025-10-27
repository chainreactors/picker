---
title: DarkAngel – 全自动白帽漏洞扫描器
url: https://www.secpulse.com/archives/193672.html
source: 安全脉搏
date: 2022-12-17
fetch_date: 2025-10-04T01:44:12.042377
---

# DarkAngel – 全自动白帽漏洞扫描器

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

# DarkAngel – 全自动白帽漏洞扫描器

[工具](https://www.secpulse.com/archives/category/tools)

[bywalks](https://www.secpulse.com/newpage/author?author_id=42997)

2022-12-16

13,319

![darkangel.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/darkangel-1024x341.png "darkangel-1024x341.png")

---

DarkAngel 是一款全自动白帽漏洞扫描器，从hackerone、bugcrowd资产监听到漏洞报告生成、企业微信通知。

DarkAngel 下载地址：[[github.com/Bywalks/DarkAngel](https://github.com/Bywalks/DarkAngel)]

当前已支持的功能：

- hackerone资产监听；

- bugcrowd资产监听；

- 自定义资产添加；

- 子域名扫描；

- 网站指纹识别；

- 漏洞扫描；

- 漏洞报告自动生成；

- 企业微信通知扫描结果；

- 前端显示扫描结果；

## 自动生成漏洞报告

自动生成漏洞报告 - MarkDown格式 - 存放地址/root/darkangel/vulscan/results/report

![report.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/report-1024x865.png "report-1024x865.png")

支持自添加漏洞报告模板，目前已添加漏洞报告模板如下，漏洞名配置为nuclei模板文件名即可

![report_template1.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/report_template1-1024x183.png "report_template1-1024x183.png")

自定义漏洞报告模板格式

![report_template2.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/report_template2-1024x501.png "report_template2-1024x501.png")

## 企业微信通知

可先查看如何获取配置：[[企业微信开发接口文档](https://developer.work.weixin.qq.com/document/path/90487)]

获取参数后，在/root/darkangel/vconfig/config.ini中配置参数，即可启用企业微信通知

微信通知 - 漏洞结果

![result_vx2.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/result_vx21.png "result_vx21.png")

微信通知 - 扫描进程

![result_vx1.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/result_vx12.png "result_vx12.png")

## 安装

整体项目架构ES+Kibana+扫描器，所以安装需要三个部分

ES镜像：

```
拉取ES镜像
docker pull bywalkss/darkangel:es7.9.3
部署ES镜像
docker run -e ES_JAVA_OPTS="-Xms1024m -Xms1024m" -d -p 9200:9200 -p 9300:9300 --name elasticsearch elasticsearch:7.9.3
查看日志
docker logs -f elasticsearch
出现问题，执行命令
sysctl -w vm.max_map_count=262144
重启docker
docker start elasticsearch
```

Kibana镜像：

```
拉取Kibana镜像
docker pull bywalkss/darkangel:kibana7.9.3
部署Kibana镜像（修改一下es-ip）
docker run --name kibana -e ELASTICSEARCH_URL=http://es-ip:9200 -p 5601:5601 -d docker.io/bywalkss/darkangel:kibana7.9.3
查看日志
docker logs -f elasticsearch
出现问题，执行命令
sysctl -w vm.max_map_count=262144
重启docker
docker start elasticsearch
```

扫描器镜像：

```
拉取扫描器镜像
docker pull bywalkss/darkangel:v1
部署扫描器
docker run -it -d -v /root/darkangel:/root/darkangel --name darkangel bywalkss/darkangel:v1
```

docker容器内挂载目录无权限

运行容器时：--privileged=true

## 用法

```
usage:  [-h] [--scan-new-domain]
        [--add-domain-and-scan ADD_DOMAIN_AND_SCAN [ADD_DOMAIN_AND_SCAN ...]]
        [--offer-bounty {yes,no}] [--nuclei-file-scan]
        [--nuclei-file-scan-by-new-temp NUCLEI_FILE_SCAN_BY_NEW_TEMP]
        [--nuclei-file-scan-by-new-add-temp NUCLEI_FILE_SCAN_BY_NEW_ADD_TEMP]
        [--nuclei-file-scan-by-temp-name NUCLEI_FILE_SCAN_BY_TEMP_NAME]
        [--nuclei-file-polling-scan] [--delete]
DarkAngel is a white hat scanner. Every user makes the Internet more secure.
--------------------------------------------------------------------------------
optional arguments:
  -h, --help            show this help message and exit
  --scan-new-domain     scan new domain from h1 and bc
  --add-domain-and-scan ADD_DOMAIN_AND_SCAN [ADD_DOMAIN_AND_SCAN ...]
                        scan new domain from h1 and bc
  --offer-bounty {yes,no}
                        set add domain is bounty or no bounty
  --nuclei-file-scan    scan new domain from h1 and bc
  --nuclei-file-scan-by-new-temp NUCLEI_FILE_SCAN_BY_NEW_TEMP
                        use new template scan five file by nuclei
  --nuclei-file-scan-by-new-add-temp NUCLEI_FILE_SCAN_BY_NEW_ADD_TEMP
                        add new template scan five file by nuclei
  --nuclei-file-scan-by-temp-name NUCLEI_FILE_SCAN_BY_TEMP_NAME
                        use template scan five file by nuclei
  --nuclei-file-polling-scan
                        five file polling scan by nuclei
```

### --scan-new-domain

```
$ python3 darkangel.py --scan-new-domain
```

- 监听hackerone和bugcrowd域名并进行扫描（第一次使用时会把hackerone和bugcrowd域名全部添加进去，资产过多的情况下做好准备，扫描时间很长）

![scan-new-domain.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/scan-new-domain.png "scan-new-domain.png")

### --add-domain-and-scan

```
$ python3 darkangel.py --add-domain-and-scan program-file-name1 program-file-name2 --offer-bounty yes/no
```

- 自定义添加扫描域名，并对这些域名进行漏洞扫描

- 文件名为厂商名称，文件内存放需扫描域名

- 需提供--offer-bounty参数，设置域名是否提供赏金

![add_domain_and_scan1.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/add_domain_and_scan1.png "add_domain_and_scan1.png")

![add_domain_and_scan2.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/add_domain_and_scan2-1024x434.png "add_domain_and_scan2-1024x434.png")

扫描结束后，会把子域名结果存在在/root/darkangel/vulscan/results/urls目录，按照是否提供赏金分别存放在，bounty\_temp\_urls\_output.txt、nobounty\_temp\_urls\_output.txt文件内

### --nuclei-file-scan

```
$ python3 darkangel.py --nuclei-file-scan
```

- 用nuclei扫描20个url文件

![nuclei-file-scan1.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/nuclei-file-scan12-1024x165.png "nuclei-file-scan12-1024x165.png")

url列表存放位置

![nuclei-file-scan1.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/nuclei-file-scan12-1024x165.png "nuclei-file-scan12-1024x165.png")

### --nuclei-file-polling-scan

```
$ python3 darkangel.py --nuclei-file-polling-scan
```

- 轮询用nuclei扫描20个url文件，可把该进程放在后台，轮询扫描，监听是否url列表是否存在新漏洞出现

### --nuclei-file-scan-by-new-temp

```
$ python3 darkangel.py --nuclei-file-scan-by-new-temp nuclei-template-version
```

- 监听nuclei-template更新，当更新时，对url列表进行扫描

当前nuclei-template版本为9.3.1

![nuclei_file_scan_by_new_temp1.png](http...