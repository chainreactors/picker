---
title: 温习Hadoop安装部署
url: https://mp.weixin.qq.com/s/7hBgw38R2JIwDKNVirQM9Q
source: Doonsec's feed
date: 2026-03-21
fetch_date: 2026-03-22T04:17:28.181896
---

# 温习Hadoop安装部署

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/2PhZXrB0gN51FdgNOqDCr2rXebiafDRYjpSMqvyJVIMGyXAR0NQRDrLyrRGvROLpib1KqRqiahKVbWL0l5Vay0kEW7gDTDVrYTVrLZxPVXexicY/0?wx_fmt=jpeg)

# 温习Hadoop安装部署

原创

MicroPest
MicroPest

MicroPest

![]()

在小说阅读器中沉浸阅读

最近，在开发几个齐头并进的平台，象千手观音，有点忙。

今天，有个同学来问关于hadoop的事情，我也借机学习了一下，作个笔记记录。

场景：4台机器组成一个集群，一主三从，分别为master、slave1、slave2、slave3，docker容器化部署。

一、Hadoop安装部署

（一）启动Docker容器

## 1.加载镜像

实验使用的Docker镜像保存在`/cg/images/hadoop_node.tar.gz`文件中，执行如下命令加载该镜像:

```
docker load < /cg/images/hadoop_node.tar.gz
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2PhZXrB0gN4XBkmtdAiaVrqlHsy7LBIOSKSqPvvkWSX5TJ10SXsAuS83PVPtyr7e4XCcMYJtTOI455XYNAibmXZyTticmFbia66SYQIkoxQkrhc/640?wx_fmt=png&from=appmsg)

## 2.启动实验容器

执行如下4条命令，启动4个名称分别为master、slave1、slave2、slave3的docker容器用于实验：

```
(1)docker run --name master --privileged --ulimit nofile=65535:65535--hostname master --ip 172.18.0.2--add-host=slave1:172.18.0.3--add-host=slave2:172.18.0.4--add-host=slave3:172.18.0.5-itd -v /cgsrc:/cgsrc:ro -v /headless/course/:/course hadoop_node /service_start.sh

(2)docker run --name slave1 --privileged --ulimit nofile=65535:65535--hostname slave1 --ip 172.18.0.3--add-host=master:172.18.0.2--add-host=slave2:172.18.0.4--add-host=slave3:172.18.0.5-itd -v /cgsrc:/cgsrc:ro hadoop_node /service_start.sh

(3)docker run --name slave2 --privileged --ulimit nofile=65535:65535--hostname slave2 --ip 172.18.0.4--add-host=master:172.18.0.2--add-host=slave1:172.18.0.3--add-host=slave3:172.18.0.5-itd -v /cgsrc:/cgsrc:ro hadoop_node /service_start.sh

(4)docker run --name slave3 --privileged --ulimit nofile=65535:65535--hostname slave3 --ip 172.18.0.5--add-host=master:172.18.0.2--add-host=slave1:172.18.0.3--add-host=slave2:172.18.0.4-itd -v /cgsrc:/cgsrc:ro hadoop_node /service_start.sh
```

执行结果如下:
![](https://mmbiz.qpic.cn/sz_mmbiz_png/2PhZXrB0gN6o9U1QqqrQwsPzCyEVlhNx43DWwD2oKAu6aGd0YIC0sibM0oqmhp2KNKKTGKMVq4TCxNLRe8qs4MatXib0WV8Dvic2ZwYe3sMTib8/640?wx_fmt=png&from=appmsg)![]()

在终端使用如下命令进入容器中：

```
docker exec -it --privileged $NAME/bin/bash
```

将命令中的`$NAME`替换为对应的容器名称即可，比如进入master容器可以使用命令:

```
dockerexec -it --privileged master /bin/bash
```

**特别注意：如果发现容器未启动，按顺序使用下面命令启动容器。**

```
docker start master
docker start slave1
docker start slave2
docker start slave3
```

**注意：不要使用 `docker start master slave1 slave2 slave3`并发启动多容器，使用该命令启动容器时，容器的启动先后顺序是不确定的，这可能会导致容器分配到的IP和创建容器时指定的IP不一致，导致集群无法启动。**

然后检查IP和hosts是否对应，如果不对，使用下面命令关闭容器后，再次按顺序启动容器。

```
docker stop master slave1 slave2 salve3
```

---

（二）配置Hadoop环境

## 1.配置JAVA环境

Hadoop是基于Java语言开发的，因此需要安装Java环境。

仅介绍master的配置方法，**slave1、slave2和slave3都需要按照下面的步骤配置Java环境！**

首先使用命令`docker exec -it --privileged master /bin/bash`进入master容器，在容器master中使用如下命令从资源文件夹`/cgsrc`中将JDK安装包复制到`/usr/local/java`目录下：

```
mkdir /usr/local/java
cp /cgsrc/jdk-8u171-linux-x64.tar.gz/usr/local/java/
```

我们接下来切换到`/usr/local/java`目录下，将安装包解压，并删除用过的tar文件。

```
cd /usr/local/java/
tar -zxvf jdk-8u171-linux-x64.tar.gz
rm -f jdk-8u171-linux-x64.tar.gz
```

此时`/usr/local/java`目录下仅有一个`jdk1.8.0_171`目录，这就是Java主目录。

接下来需要配置`JAVA_HOME`环境变量，为了方便起见，这里直接在`~/.bachrc`这个文件中进行设置，采用这种配置方式时，只对当前登录的单个用户生效，当该用户登录以及每次打开新的Shell时，它的环境变量文件`.bashrc`会被读取。输入下面命令打开当前登录用户的环境变量配置文件`.bashrc`：

```
vim ~/.bashrc
```

在文件最后面添加如下3行（**注意等号前后不能有空格**），然后保存退出vim：

```
exportJAVA_HOME=/usr/local/java/jdk1.8.0_171
exportCLASSPATH=.:${JAVA_HOME}/jre/lib/rt.jar:${JAVA_HOME}/lib/dt.jar:${JAVA_HOME}/lib/tools.jar
exportPATH=$PATH:${JAVA_HOME}/bin
```

接下来让环境变量生效，执行如下代码：

```
source ~/.bashrc
```

执行上述命令后，可以检验一下是否设置正确：

```
echo $JAVA_HOME    #检验变量值
java -version      #查看java版本
```

输出如下即表明配置Java环境成功：

```
java version "1.8.0_171"
Java(TM)SERuntimeEnvironment(build 1.8.0_171-b11)
JavaHotSpot(TM)64-BitServerVM(build 25.171-b11, mixed mode)
```

**请务必以同样的步骤对每个节点进行配置!**

## 2.配置分布式模式

> 当Hadoop采用分布式模式部署和运行时，存储采用分布式文件系统HDFS。而且，HDFS的名称节点和数据节点位于不同的机器上。这时，数据就可以分布到多个节点上，不同数据节点上的数据计算可以并行执行，这使得MapReduce分布式计算能力才能真正发挥作用。

使用4个节点搭建集群环境：1个Master节点和3个Slave节点。节点的IP地址可以在对应的命令行中使用`ifconfig`命令查看：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2PhZXrB0gN4NqVcia24RJve0Lduib6NW8CqsY5NYyK1ohumkp7VibcdPGoZV44icsIxBtCvasNXonDEXDTxib4gW6t9C5AcIyCnAZrI1oJrKYI6M/640?wx_fmt=png&from=appmsg)

Hadoop集群的安装配置大致包括以下步骤：

（1）选定1个节点作为Master

（2）在Master节点上安装Hadoop，并完成配置。

（3）将Master节点上的Hadoop目录复制到其他Slave节点上

（4）在Master节点上开启Hadoop

## 3.配置hosts文件

本次演示中，4个节点的ip地址如下：

（1）master 172.18.0.2

（2）slave1 172.18.0.3

（3）slave2 172.18.0.4

（4）slave3 172.18.0.5

由于我们在docker的启动命令里已经加入了host配置，所以检查发现`/etc/hosts`文件里映射关系齐全则可以略过此步骤。

执行如下命令打开并修改master节点中的`/etc/hosts`文件：

```
vim /etc/hosts
```

**确保在hosts文件中有如下IP和主机名映射关系：**

```
172.18.0.2    master
172.18.0.3    slave1
172.18.0.4    slave2
172.18.0.5    slave3
```

上面完成了master节点的配置，接下来**在3个slave节点中使用同样步骤配置hosts文件**。

在各个节点上执行如下指令，测试节点之间是否已经联通：

```
ping master -c 3
ping slave1 -c 3
ping slave2 -c 3
ping slave3 -c 3
```

如果都能连通，则配置成功。

## 4.配置SSH无密码登录

需要让master节点可以SSH无密码登录到各个slave节点上。

首先，生成master节点的公钥，**如果之前已经生成过公钥，必须删除原来的公钥**，重新生成一次。具体命令如下：

```
cd ~/.ssh            #如果没有该目录，先执行一次 ssh localhost，密码默认为83953588abc
rm -f ./id_rsa*        #删除之前生成的公钥
ssh-keygen -t rsa    #执行该命令后，遇到提示信息，均按Enter即可
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/2PhZXrB0gN6aYb8QSlCYPxasiaj6vElh0icKLyOAicic1CvuWUP6XSrjKS0hIHtg7nX4jaObC4hn827luAbwYQ1HiaYbNmsDOpo9ib5tOsw7bsrAI/640?wx_fmt=png&from=appmsg)

为了让master节点能无密码SSH登录到本机，需要在master节点上执行如下命令：

```
cat ./id_rsa.pub>>./authorized_keys
```

完成后可以执行`ssh master`来验证一下，可能会遇到提示信息，只要输入 `yes` 即可，测试成功后执行`exit`命令返回原来的终端。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/2PhZXrB0gN7BNp71yJUYmx6YCk49tk4uzW5X5p6pZvsJlTYEcj3xN0NU0ytGROIgHsZJ0XHcLbaDDawpkbEFsyHiaALtBlAErjjvPTjpKsibg/640?wx_fmt=png&from=appmsg)![]()
接下来在master节点上将公钥传输到3个slave节点：

```
scp ~/.ssh/id_rsa.pub root@slave1:/root
scp ~/.ssh/id_rsa.pub root@slave2:/root
scp ~/.ssh/id_rsa.pub root@slave3:/root
```

执行scp复制文件时会要求输入相应的slave的密码，默认为：\*\*\*\*

传输完成后在3个slave节点上将SSH公钥加入授权：

```
mkdir -p ~/.ssh       #如果slave节点上已存在该目录，则先删除该目录再执行该命令
cat ~/id_rsa.pub >> ~/.ssh/authorized_keys
rm -f ~/id_rsa.pub
```

slave1的操作过程如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/2PhZXrB0gN6d99hiaV9kRSrlpjvzYqaaj4ppCE3DAicmHJZTuYicApEwRicpicaAYCMgX8kTFLw69B4pZVdVgXTejVicpkSQpicyTzb8yH2GVZvGYM/640?wx_fmt=png&from=appmsg)

其他的，同样操作。

这样就可以在master节点上无密码SSH登录到各个slave节点了。

注意：由于启动Hadoop集群时，master节点需要通过ssh登录自身节点(`ssh localhost`)，为了去掉ssh的交互式认证提示，需要在master节点上执行以下命令：

```
ssh-keyscan localhost >>~/.ssh/known_hosts
```

上述执行过程如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/2PhZXrB0gN65SqCrNp6qlvr45nz5jLEldVqyicswibukpdPEmvkfaPSFIpribv55V93IsswYGdfnm8SRpv9dCa9nE5tdLmmcpxZqrTa4GiaMDWA/640?wx_fmt=png&from=appmsg)

**请在master节点上使用如下3条命令，确认可以从master无密码ssh登录到各个slave节点。**

```
ssh slave1
ssh slave2
ssh slave3
```

如果不能无密码登录，请重新操作排查问题。

## 5.安装Hadoop并配置环境变量

在master节点上执行如下操作安装hadoop并配置环境变量。

首先将hadoop安装包复制到 `/usr/local`目录下：

```
cp /cgsrc/hadoop-2.7.1.tar.gz/usr/local/
```

切换到`/usr/local`目录下，对安装包进行解压：

```
cd /usr/local
tar -zxvf hadoop-2.7.1.tar.gz
rm -f hadoop-2.7.1.tar.gz
```

解压得到名为`hadoop-2.7.1`的目录，将其重命名为 `hadoop`：

```
mv hadoop-2.7.1/ hadoop
```

该命令执行后，之后就可以配置`PATH`变量了，使我们可以在任何目录下使用`hadoop`指令。

首先打开 ~/.bashrc 文件：

```
vim ~/.bashrc
```

然后在该文件最末加入下面一行内容：

```
exportPATH=$PATH:/usr/local/hadoop/bin:/usr/local/hadoop/sbin
```

保存后执行 `source ~/.bashrc` 使配置生效。

之后执行如下命令查看hadoop版本：

```
hadoop version
```

若得到如下输出则安装成功：
![](https://mmbiz.qpic.cn/mmbiz_png/2PhZXrB0gN5Ihd7tjkTlpW0LD86FUk7B6m9TlTj2ficcBg0dt7bRGONDE9ukyVD460G0BV95CFr0bu36GtcibS3pnHx40Qb0SF26Iib6XjCxL0/640?wx_fmt=png&from=appmsg)![]()

---

# 二、配置集群环境

配置集群环境时，需要修改 `/usr/local/hadoop/etc/hadoop` 目录下的配置文件，这里仅设置正常启动必须的设置项，包括 `slaves`、`core-site.xml`、`hdfs-site.xml`、`mapred-site.xml`、`yarn-site.xml`共五个文件。

（一）配置**master**节点

1.修改文件slaves

需要把所有数据节点的主机名写入该文件，每行一个，默认为localhost（即把本机作为数据节点）。在进行集群配置时，可以保留localhost，让master节点同时充当名称节点和数据节点，也可以删除localhost这行，让master节点仅作为名称节点使用。

本节让master节点仅作为名称节点使用，因此将slaves文件中原来的内容删除，添加如下内容：

```
slave1
slave2
slave3
```

## 2.修改文件core-site.xml

把`core-site.xml`文件修改为如下内容：

```
<configuration>
<property>
<name>fs.de...