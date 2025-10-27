---
title: Elastic SIEM
url: https://misakikata.github.io/2023/01/Elastic-SIEM/
source: Misaki's Blog
date: 2023-01-14
fetch_date: 2025-10-04T03:49:34.851705
---

# Elastic SIEM

[Misaki's Blog](/)

Toggle navigation

* [archives](/archives/)
* [about](/about/)

# Elastic SIEM

**Friday, January 13th 2023, 10:34 am**

## 安装SIEM

安全性资讯与事件 (SIEM) 是一种解决方案，可协助组织在威胁伤害企业运行之前，先进行侦测、分析和回应安全性威胁。以下使用centos7安装Elastic SIEM。

使用Ubuntu安装：<https://blog.csdn.net/UbuntuTouch/article/details/114023944>

<https://elasticstack.blog.csdn.net/article/details/112647180>

### 安装Elasticsearch

创建RPM配置/etc/yum.repos.d/elasticsearch.repo

```
[elasticsearch]
name=Elasticsearch repository for 7.x packages
baseurl=https://artifacts.elastic.co/packages/7.x/yum
gpgcheck=1
gpgkey=https://artifacts.elastic.co/GPG-KEY-elasticsearch
enabled=0
autorefresh=1
type=rpm-md
```

安装

```
yum install --enablerepo=elasticsearch elasticsearch
```

或者下载rpm文件

```
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.16.3-x86_64.rpm
sudo rpm --install elasticsearch-7.16.3-x86_64.rpm
```

修改/etc/elasticsearch/elasticsearch.yml

```
cluster.name: demo-elk
node.name: elk-1
network.host: 0.0.0.0
discovery.type: single-node
```

启动es

```
service elasticsearch start
```

### 安装kibana

同样创建配置/etc/yum.repos.d/kibana.repo

```
[kibana-7.x]
name=Kibana repository for 7.x packages
baseurl=https://artifacts.elastic.co/packages/7.x/yum
gpgcheck=1
gpgkey=https://artifacts.elastic.co/GPG-KEY-elasticsearch
enabled=1
autorefresh=1
type=rpm-md
```

安装

```
yum install kibana
```

或者下载rpm文件

```
wget https://artifacts.elastic.co/downloads/kibana/kibana-7.16.3-x86_64.rpm
sudo rpm --install kibana-7.16.3-x86_64.rpm
```

编辑配置文件/etc/kibana/kibana.yml

```
server_port: 5601
server_host: 0.0.0.0
server_name: demo-kibana
```

启动

```
service kibana start
```

### 安装Filebeat

```
yum install filebeat
```

### 安装 Zeek

一些需要的组件

```
yum install cmake gcc-c++ gcc make flex bison swig python3 python3-devel
```

下载

```
git clone --recursive https://github.com/zeek/zeek
```

配置环境

```
./configure --prefix=/opt/zeek
```

如果显示cmake版本不对，则去下载cmake

```
wget https://cmake.org/files/v3.18/cmake-3.18.6-Linux-x86_64.tar.gz -O /opt/
yum remove cmake
# 编辑环境变量写入
export CMAKE_HOME=/opt/cmake
export PATH=$PATH:$CMAKE_HOME/bin
source /etc/profile
cmake -version
```

再此执行上面的命令如果报错`No CMAKE_CXX_COMPILER could be found`，安装gcc-c++

```
yum install gcc-c++
```

如果报错 `Could NOT find ZLIB`，安装zlib

```
wget http://www.zlib.net/zlib-1.2.11.tar.gz
tar -xvzf zlib-1.2.11
./configure
make && make install
```

如果报错 `Could not find prerequisite package 'PCAP'`，安装libpcap

```
wget https://www.tcpdump.org/release/libpcap-1.10.1.tar.gz
tar -zxvf libpcap-1.10.1.tar.gz
cd libpcap-1.10.1
./configure
make -j8
make install
```

如果报错`Could not find prerequisite package 'OpenSSL'`，安装libssl

```
yum install openssl-devel
```

如果提示GCC版本过低，scl源安装多版本gcc

```
yum install centos-release-scl
yum install devtoolset-7-gcc*
scl enable devtoolset-7 bash
```

安装基本就可以成功，但是时间有点长，添加环境变量

```
export PATH=/opt/zeek/bin:$PATH
```

在 /opt/zeek/etc 找到一个叫做 node.cfg 的配置文件。修改网卡名

```
interface=ens33
```

安装sendmail

```
yum install sendmail
```

部署zeek

```
zeekctl deploy
```

在 /opt/zeek/logs 目录里发现日志。“current” 目录保存当天的日志，而前几天的日志则存档到其自己的目录中。

### 配置安全访问

需要创建一个 YAML 文件 /usr/share/elasticsearch/instances.yml

```
instances:
 - name: "elasticsearch"
   ip:"192.168.0.4"
 - name: "kibana"
   ip:"192.168.0.4"
 - name: "zeek"
   ip:"192.168.0.4"
```

运行生成证书

```
/usr/share/elasticsearch/bin/elasticsearch-certutil cert ca --pem --in instances.yml --out certs.zip
```

如果报错，说明如下是格式对其上有问题

```
expected <block end>, but found '<block mapping start>'
 in 'reader', line 3, column 3:
      ip: "192.168.36.133"
      ^
```

正常生成后，在运行解压缩

```
unzip /usr/share/elasticsearch/certs.zip -d /usr/share/elasticsearch/
```

### 配置 Elasticsearch SSL

创建一个文件夹将你的证书存储在我们的 Elasticsearch 主机上。

```
mkdir /etc/elasticsearch/certs/ca -p
```

需要将解压缩的证书复制到其相关文件夹中并设置正确的权限。

```
cp ca/ca.crt /etc/elasticsearch/certs/ca
cp elasticsearch/elasticsearch.crt /etc/elasticsearch/certs
cp elasticsearch/elasticsearch.key /etc/elasticsearch/certs
chown -R elasticsearch: /etc/elasticsearch/certs
chmod -R 770 /etc/elasticsearch/certs
```

将 SSL 配置添加到我们的 /etc/elasticsearch/elasticsearch.yml 文件

```
# Transport layer
xpack.security.transport.ssl.enabled: true
xpack.security.transport.ssl.verification_mode: certificate
xpack.security.transport.ssl.key: /etc/elasticsearch/certs/elasticsearch.key
xpack.security.transport.ssl.certificate: /etc/elasticsearch/certs/elasticsearch.crt
xpack.security.transport.ssl.certificate_authorities: [ "/etc/elasticsearch/certs/ca/ca.crt" ]

# HTTP layer
xpack.security.http.ssl.enabled: true
xpack.security.http.ssl.verification_mode: certificate
xpack.security.http.ssl.key: /etc/elasticsearch/certs/elasticsearch.key
xpack.security.http.ssl.certificate: /etc/elasticsearch/certs/elasticsearch.crt
xpack.security.http.ssl.certificate_authorities: [ "/etc/elasticsearch/certs/ca/ca.crt" ]
```

重新启动 Elasticsearch。

```
service elasticsearch restart
```

### 配置 Kibana SSL

配置证书

```
mkdir /etc/kibana/certs/ca -p
cp ca/ca.crt /etc/kibana/certs/ca
cp kibana/kibana.crt /etc/kibana/certs
cp kibana/kibana.key /etc/kibana/certs
chown -R kibana: /etc/kibana/certs
chmod -R 770 /etc/kibana/certs
```

文件 /etc/kibana/kibana.yml

```
elasticsearch.hosts: ["https://192.168.36.133:9200"]
elasticsearch.ssl.certificateAuthorities: ["/etc/kibana/certs/ca/ca.crt"]
elasticsearch.ssl.certificate: "/etc/kibana/certs/kibana.crt"
elasticsearch.ssl.key: "/etc/kibana/certs/kibana.key"
​
#在 Kibana 和浏览器之间添加配置
server.ssl.enabled: true
server.ssl.certificate: "/etc/kibana/certs/kibana.crt"
server.ssl.key: "/etc/kibana/certs/kibana.key"
```

重新启动

```
service kibana restart
```

### 配置 Beats (Zeek) SSL

首先将证书复制到运行 Zeek 的主机上，然后使用正确的权限创建证书目录。 您需要同时复制 Zeek 证书和 CA 证书。

```
mkdir /etc/filebeat/certs/ca -p
cp ca/ca.crt /etc/filebeat/certs/ca
cp zeek/zeek.crt /etc/filebeat/certs
cp zeek/zeek.key /etc/filebeat/certs
chmod 770 -R /etc/filebeat/certs
```

修改配置/etc/filebeat/filebeat.yml

```
output.elasticsearch.hosts: ['192.168.36.133:9200']
output.elasticsearch.protocol: https
output.elasticsearch.ssl.certificate: "/etc/filebeat/certs/zeek.crt"
output.elasticsearch.ssl.key: "/etc/filebeat/certs/zeek.key"
output.elasticsearch.ssl.certificate_authorities: ["/etc/filebeat/certs/ca/ca.crt"]
​
setup.kibana:
  host: "https://192.168.36.133:5601"
  ssl.enabled: true
  ssl.certificate_authorities: ["/etc/filebeat/certs/ca/ca.crt"]
  ssl.certificate: "/etc/filebeat/certs/zeek.crt"
  ssl.key: "/etc/filebeat/certs/zeek.key"
```

重启filebeat

```
service filebeat restart
```

运行以下命令来检查 FileBeats 是否可以连接到 Elasticsearch。 一切都应该返回“OK”。

```
filebeat test output
```

至此，如果想在Integrations添加集成模块，会提示不能添加，需要管理员设置，说明没有认证。

### 添加身份验证

编辑 /etc/elasticsearch/elasticsearch.yml 启用安全

```
xpack.security.enabled: true
```

重新启动 Elasticsearch:

```
service elasticsearch restart
```

Elasticsearch 附带了一个工具来执行此操作。 运行以下命令以生成这些密码并将其保存在安全的地方

```
/usr/share/elasticsearch/bin/elasticsearch-setup-passwords interactive
```

会设置多个账号密码，可以按照需要来修改，此处使用admin123，相同的设置。

这时候再去访问9200端口发现需要身份认证。同样kibana也不能访问，修改配置/etc/kibana/kibana.yml

```
elasticsearch.username: "kibana_system"
elasticsearch.password: "admin123"
```

重新启动 Kibana:

```
service kibana restart
```

修改Filebeat 配置/etc/filebeat/filebeat.yml

```
output.elasticsearch.username: "elastic"
output.elasticsearch.password: "admin123"
```

重新启动 Filebeat:

```
service filebeat restart
```

### 安装证书

链接显示不好安全链接，且本地不能验证证书，这里添加证书到本地验证，也就是生成的ca.cer添加到受信任的根证书机构中。

**Management > Fleet**。第一次访问此页面时，可能需要一分钟才能加载。

### 添加 Zeek

添加 Zeek 数据到 Elasticsearch，在集成模块中选择Zeek Logs。

使用如下的命令来启动 zeek 模块：

```
filebeat modules enable zeek
```

将 `@load policy/tuning/json-logs.zeek` 行编辑到文件 `/opt/zeek/share/zeek/site/local.zeek`中。

保存好文件，并重新启动 zeek:

```
zeekctl deploy
```

现在检查日志是否为 JSON 格式。 即使你不熟悉 JSON，日志的格式也应该与以前明显不同。

```
tail -f /opt/zeek/logs/current/status.log
```

编辑配置文件 /etc/filebeat/modules.d/zeek.yml。对于 /opt/zeek/logs/ 文件夹中的每个日志文件，必须定义 “current” 日志的路径以及以前的任何日志，如下所示，需要把配置中的全部都修改一下。

```
dns:
  enabled: true
  var.paths:...