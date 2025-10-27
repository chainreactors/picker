---
title: 环境搭建 | 手动搭建K8S环境
url: https://www.secpulse.com/archives/190079.html
source: 安全脉搏
date: 2022-10-29
fetch_date: 2025-10-03T21:11:43.191139
---

# 环境搭建 | 手动搭建K8S环境

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

# 环境搭建 | 手动搭建K8S环境

[Web安全](https://www.secpulse.com/archives/category/articles/web)

[贝塔安全实验室](https://www.secpulse.com/newpage/author?author_id=9525)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2022-10-28

17,033

**手动搭建K8S环境**

K8S环境搭建

前期准备好三台Centos机器，配置如下：

|  |  |  |
| --- | --- | --- |
| **主机名** | **ip** | **系统版本** |
| k8s-master | 172.16.200.70 | Centos7 |
| k8s-node1 | 172.16.200.71 | Centos7 |
| k8s-node2 | 172.16.200.72 | Centos7 |

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190079-16669443401.png)

**0****1**

**前期准备**

前期准备好三台Centos7机器，均配置如下：

[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/10/image48.png "image48.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/10/image48.png)

在三台机器上均安装docker、kubeadm、kubelet，在master节点安装kubectl

 如下配置阿里云的K8s源

```
cat > /etc/yum.repos.d/kubernetes.repo << EOF
[kubernetes]
name=Kubernetes
baseurl=https://mirrors.aliyun.com/kubernetes/yum/repos/kubernetes-el7-x86_64
enabled=1
gpgcheck=0
repo_gpgcheck=0
gpgkey=https://mirrors.aliyun.com/kubernetes/yum/doc/yum-key.gpg https://mirrors.aliyun.com/kubernetes/yum/doc/rpm-package-key.gpgEOF
```

安装docker就不赘述了，执行如下命令一键安装

```
curl -s https://get.docker.com/ | sh
```

如下所示安装完成：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190079-16669443402.png)

接着执行如下命令安装kubelet、kubeadm和kubectl

```
#安装kubelet、kubeadm和kubectl
yum install -y kubelet-1.23.0 kubeadm-1.23.0 kubectl-1.23.0
#设置kubelet开机自启
systemctl enable kubelet
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190079-1666944341.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190079-1666944346.png)

**02**

**部署K8S-Master**

    在master节点执行如下命令初始化master

```
kubeadm init --apiserver-advertise-address=172.16.200.70 --image-repository=registry.aliyuncs.com/google_containers --kubernetes-version v1.23.0 --service-cidr=10.10.10.0/24 --pod-network-cidr=10.20.20.0/24 --ignore-preflight-errors=all
```

    然后拷贝k8s认证文件

```
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
```

    这里记住kubeadm join这条命令，在node节点执行这条命令加入集群。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190079-16669443461.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190079-1666944348.png)

**03**

**K8S-Node**

在两个node节点执行如下命令即可加入K8S集群

```
kubeadm join 172.16.200.70:6443 --token y05mrn.y5yz5g0zvjyanos5 --discovery-token-ca-cert-hash sha256:683c265dcc24cdf2f1a677f0bd38236326514d4270d2d62b602912bf8f70c22e
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190079-16669443481.png)

默认token的有效期为24小时，过了24小时之后，该token就不可用了。这时就需要重新创建token，可以在master节点直接如下命令生成：

```
kubeadm token create --print-join-command
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190079-1666944350.png)

**04**

**部署网络**

Calico是一个纯三层的数据中心网络方案，是目前Kubernetes主流的网络方案。

```
wget https://docs.projectcalico.org/v3.19/manifests/calico.yaml --no-check-certificate
wget https://docs.projectcalico.org/manifests/calico.yaml --no-check-certificate
```

    下载完后还需要修改里面定义Pod网络（CALICO\_IPV4POOL\_CIDR），与之前kubeadm init的 --pod-network-cidr指定的一样。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190079-1666944351.png)

    默认calico.yaml中所使用的镜像都来源于docker.io国外镜像源，这里我们可以删除docker.io前缀以使镜像从国内镜像加速站点下载。

```
cat calico.yaml |grep 'image:'
sed -i 's#docker.io/##g' calico.yaml
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190079-16669443511.png)

修改完后文件后，进行部署：

```
#部署
kubectl apply -f calico.yaml
#查看状态，执行完上一条命令需要等一会才全部running
kubectl get pods -n kube-system
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190079-1666944353.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190079-1666944358.png)

**报错解决**

    如果在部署calico.yaml文件的时候碰到如下错误，则是因为calico版本与k8s版本不匹配导致的，可以参考[https://projectcalico.docs.tigera.io/archive/v3.23/getting-started/kubernetes/requirements](https://projectcalico.docs.tigera.io/archive/v3.23/getting-started/kubernetes/requirements)找到对应版本的calico。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190079-1666944363.png)

查看pods的状态，可以看到calico的是Init:ImagePullBackOff

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190079-1666944368.png)

直接去网站进行下载：https://github.com/projectcalico/calico/releases

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190079-1666944371.png)

下载完成后解压，image文件夹下为docker镜像文件，还原

```
docker load < xx.tar
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190079-1666944372.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190079-1666944380.png)

重新部署

```
#移除
kubectl delete -f calico.yml
#部署
kubectl apply -f calico.yaml
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190079-1666944382.png)

**05**

**部署Dashboard**

Dashboard是官方提供的一个Web UI，可用于基本管理K8s资源，执行如下命令下载yaml文件。默认Dashboard只能集群内部访问，修改Service为NodePort类型，暴露到外部：

```
wget https://raw.githubusercontent.com/kubernetes/dashboard/v2.4.0/aio/deploy/recommended.yaml
```

    修改如下，nodePort的端口范围为30000-32767，这里设置为31000，并且添加type：NodePort

![](htt...