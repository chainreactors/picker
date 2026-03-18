---
title: 【AI安全】零基础AI攻防，技精自可不求人
url: https://mp.weixin.qq.com/s/dehPX-NdG3PxLSyw3rXSeg
source: Doonsec's feed
date: 2026-03-17
fetch_date: 2026-03-18T04:17:33.468301
---

# 【AI安全】零基础AI攻防，技精自可不求人

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GAiboNDibyQqibHO1GDvHHKzicKRvf4xvh54wP4Mf2iaFyMDUr5qCiaS9ZvO6Z6v2Xibuel87AtCMV9jTsVp0YcZ08ZLZPibN4ffbibwccnmGvEoXAdE/0?wx_fmt=jpeg)

# 【AI安全】零基础AI攻防，技精自可不求人

十月的进阶之路

![]()

在小说阅读器中沉浸阅读

以下文章来源于Sec靈魂問號
，作者耐心球\_403

![](http://wx.qlogo.cn/mmhead/icFTnRoibgibp9DoyF7CoM845DCk2UZNqdjlO2eGicGWKXXxNc1M2wPCR8iaGA28DDtgibPX93gRJKUnk/0)

**Sec靈魂問號**
.

Exploit it，外设损耗+1。延时任务：去码头整点薯条！365 up～

零基础 + 搭建靶场 + 阅读教程 + 实战案例

一、AI红队学院

![](https://mmbiz.qpic.cn/mmbiz_png/GAiboNDibyQq8iaGJFicalWgEpuKdfmzxicLnzTMpnAoOwdfrOgibzrM52ichTuVpgWtZu9shkb8ticQtjVrqEvBSftS1Mkpd9J0yKcopCLs2VZnjCQ/640?wx_fmt=png&from=appmsg)

前提条件

### **·**docker环境

### **· docker-compose**

注意：最新版Docker已经内置Compose功能，不需要单独安装docker-compose这个独立工具

步骤一、下载Kali Linux安装Docker

# 1.查看当前源，并建议替换为国内源

```
cat /etc/apt/sources.list
```

![](https://mmbiz.qpic.cn/mmbiz_png/GAiboNDibyQqic6unllyVonAt5eLn7vwqyGg737SWIshOXGT6MahJgEmusLzOTHyJGsXcwg2zTjLHpT9uib3pb4x7TzBrMOJVNdic7bzZ62ial9HA/640?wx_fmt=png&from=appmsg)

铁子，看清楚哈，vim后面有一个空格，代码如下：

```
vim /etc/apt/sources.list
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GAiboNDibyQq9icFSzds9fBnXjuibs0sIzcnpF0iaicH4qQTo45HiaeXMj1qMt78tvh4pSPtgd1K3VImI0YP6Xpibiax8gcCsKpAEPz8Z8UPGsAEwFHc/640?wx_fmt=png&from=appmsg)

当前页面按i进入编辑模式。移动箭头，在这一行前面加一个#注释掉：

#debhttp://http.kali.org/kali【你可能和我不一样自己注释】

然后在文档添加两句（Shift+Insert粘贴进入）：

```
deb http://mirrors.aliyun.com/kali kali-rolling main non-free contribdeb-src http://mirrors.aliyun.com/kali kali-rolling main non-free contrib
```

按Esc键退出编辑模式，然后输入:wq保存退出【再次查看就是图片一的样子】

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GAiboNDibyQq91lcVESgSiaBNQ6nETiaaEazKwMiapWFOSuagHYdonLf48icw9y0wngNywDWxP8Vpanz5xq7m7wPVZiafsrQrBMv2u6Qic8klF0icTdI/640?wx_fmt=png&from=appmsg)

# 2. 更新系统

```
sudo apt update
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GAiboNDibyQq8Il576zlicicIyVNqrJeL4D8SriafPmhicKc1JIYG9sX2LlXUXXZHiaXgCmgBgXP82SLUyQEP0m69bl4Yq1y2NJUXO6tEpVaIJ1Zfc/640?wx_fmt=png&from=appmsg)

遇到这个问题不要慌铁子，请输入如下代码：

```
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys ED65462EC8D5E4C5sudo apt update
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GAiboNDibyQqicGSDz7VMsvPvpY5ZTdibyiaGbSm3B0wkicOMicYGB6ibZg2VbkS6eUdUF2E2S1ksibQuhSbuAUia1SUFK0s6iaF3jNxVrq4Uu88xNjCbc/640?wx_fmt=png&from=appmsg)

# 3. 安装 Docker

```
（1）安装依赖sudo apt install -y apt-transport-https ca-certificates curl gnupg lsb-release
（2）添加阿里云 Docker GPG 密钥curl -fsSL https://mirrors.aliyun.com/docker-ce/linux/debian/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
（3）添加阿里云 Docker 源（Kali 基于 Debian）echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://mirrors.aliyun.com/docker-ce/linux/debian bookworm stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
（4）安装 Dockersudo apt updatesudo apt install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GAiboNDibyQq9tT7iahiakOyt11fTPdtRxHD5ILo2z0pUOxjKVQdicGY80iawj4ZxsRXIyXPoEGI3w6PbWgDib5tHuUGx2I1P82ib1UbnmHx4b8S5jc/640?wx_fmt=png&from=appmsg)

铁子注意：只使用该该命令sudo apt install -y docker.io安装老版本，需要额外下载docker-compose【耐心球\_403使用的是新版】

# 4. 启动 Docker

```
sudo systemctl start dockersudo systemctl enable docker
```

# 5. 验证

```
docker -vdocker compose version
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GAiboNDibyQq9wic7btBWxGibhp1PZN4XVcpK2Wlu1VgXlNNTplHANxnhwNepxzAfSYUKsI9h0OR0AW3xfgz1y08n1Met6toncBvj3QIUfHZ8hY/640?wx_fmt=png&from=appmsg)

步骤二、克隆GitHub仓库（下载项目代码）

```
git clone https://github.com/0x4d31/airt.git
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GAiboNDibyQq84qDDJILtcsWt4qLpFPuQHQUo7Woyf8upmsiclkaCxdTDNJGHkGFr8tNh4ulXxSuWD5eSiaKuIkefWQdUCqcNQ9BZNlIXPah3Fg/640?wx_fmt=png&from=appmsg)

步骤三、进入labs目录

```
cd airt/labs
```

步骤四、进入具体实验目录（以Lab 01为例）

```
cd lab01-foundations
```

步骤五、启动Docker容器（新版命令，等价于 docker-compose up）

```
docker compose up
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GAiboNDibyQqib9Y98Gwic387zmzsZH0AqSgk96QNQkc3DjWf3d633rULeQoygQCAriaicZjcrfd05QicmB2Jeo2bHUzDQhUScJZWLuV4mYCYxZm4s/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/GAiboNDibyQqibicx5ARpkCFQj2hWCBfbjgYbDztG4ibIZzKyKia4CthFYmib9YEyETQFJjc4JEGvHibmk9mibF5W7rMtWZYGrfgksKs9VKK5BVq9ictE/640?wx_fmt=png&from=appmsg)

步骤六、自动打开浏览器访问（系统命令）

```
open http://localhost:8888
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GAiboNDibyQq9mDmFYFPbuq64txQUibk0eEyHI3jkEhLhtHlLGtk32WZZ6ibVODkDUPAWE8PwZ5GHHoc7lLb7mjwMiaSrGG5oXISORTAzCDlNho8/640?wx_fmt=png&from=appmsg)

你可能在好奇密码或令牌是什么？那么看到下面来吧！

```
# 1.查看运行中的容器docker ps# 2.进入容器（替换<container_id>为实际ID）docker exec -it <container_id> /bin/bash# 3.在容器内部执行，获取Tokenjupyter server list# 4.复制输出的token，粘贴到浏览器http://<container_id>:8888/?token=redteam :: /home/jovyanhttp://<container_id>:8888/容器内部地址（对外映射到localhost:8888）?token=redteamToken密码是：redteam/home/jovyanJupyter工作目录（容器内）
```

![](https://mmbiz.qpic.cn/mmbiz_png/GAiboNDibyQq9poB1aDhziccWqsCcJK1xZAOoc6ibS3r4Vo8Qszlkdy6AbMOmiafR4JUZ6e2C6LDrKxh6anJE8txto875upPL7q08VAgzmy8LGxc/640?wx_fmt=png&from=appmsg)

当然来到这里你已经快拥有属于自己的小型AI红队学院，再坚持一下吧！铁子

# 进入 Ollama 容器【铁子，你真的让我很失望。注意，该<container\_id>不是之前的id值了】

```
docker exec -it lab01-ollama /bin/bash 或者 docker exec -it <container_id> /bin/bash
```

# 运行对话模式 需要先下载模型`llama2`

```
ollama run llama2
```

# 现在可以直接输入内容对话

```
>>> 你好>>> 什么是提示词注入攻击？>>> /bye # 退出
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GAiboNDibyQqicCc73U3xsoibyPNg9u6eJDSqXwYgqZZdibDd8XBaQC0qY6icibvfkz3uCTF62tFwVSnAmlxbh5ElyCeKrBUwF11ibmE8QQbQmdiahpU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GAiboNDibyQqic1PkQf0GOnLiamXc29Xa9Z1HJUsbdtDib7QLagy5Qcl0qWEe0UAfhoxz3gcHDCcFR4T96o0kcdvK86iciczO46PKVnibmicE8VkELIE/640?wx_fmt=png&from=appmsg)

如果模型太大，如何解决？

方案一：修改docker-compose.yml 增加内存

方案二：换用更小的模型（硬件不够时的选择）

```
# 1.在容器内执行（如果已退出，先docker exec进入）# 2.删除跑不动的大模型（释放空间）ollama rm llama2# 3.下载轻量模型（选其一）ollama pull llama3.2:1b # Meta出品，1B参数，通用ollama pull qwen2.5:1.5b # 阿里出品，中文好ollama pull phi3:mini # 微软出品，代码强# 4.运行小模型ollama run qwen2.5:1.5b
```

步骤七、在Jupyter中创建对话界面

```
import requestsimport json
OLLAMA_URL = "http://192.168.11.128:11434"def chat(model="qwen2.5:1.5b"):  # 修改默认模型为你实际下载的    """简单的交互式对话"""    print(f"开始与 {model} 对话，输入 'quit' 退出\n")
    while True:        user_input = input("耐心球_403: ")        if user_input.lower() in ['quit', 'exit', 'bye']:            print("对话结束")            break
        try:            response = requests.post(                f"{OLLAMA_URL}/api/generate",                json={                    "model": model,                    "prompt": user_input,                    "stream": False                },                timeout=60            )
            if response.status_code == 200:                reply = response.json().get('response', '无响应')                print(f"AI: {reply}\n")            else:                print(f"错误: HTTP {response.status_code}")                print(f"详情: {response.text}")
        except requests.exceptions.ConnectionError:            print("错误: 无法连接到Ollama服务")            print("请检查：1) Ollama是否运行  2) 防火墙是否放行11434端口  3) IP地址是否正确")            break        except Exception as e:            print(f"错误: {e}")if __name__ == "__main__":    chat()
```

![](https://mmbiz.qpic.cn/mmbiz_png/GAiboNDibyQq9hTHeuWpQKhiasWZVQbJSCFbGAB2JmYMgsia0CgQyUlibWiakF5DVINjL6t5NEztHsPMwm0FNroyibHlgWn26YO670slxsgs4HTdPY/640?wx_fmt=png&from=appmsg)

二、重点知识点

![](https://mmbiz.qpic.cn/sz_mmbiz_png/GAiboNDibyQq8WicibXKgHw0FeRNphD1HeZmLdaITV9VZ6CgibXgInEHsH2ovg25HZ0CHzdr5qyQhYGo0Op7YvHutjOP1e8ndcia3ZDibjfiaMxvtb0/640?wx_fmt=png&from=appmsg)

（1）提示词注入：提示词注入不叫覆盖了安全规则，叫没有成功区分数据和指令

关键：安全规则没有被覆盖，模型只是"误以为"用户输入是更高优先级的指令

（2）越狱：越狱才是覆盖了安全规则，对安全边界的突破

关键：安全规则在特定上下文下被"压制"或"绕过"，模型释放了被限制的能力

（3）数据投毒：在训练数据中植入恶意关联，通过训练过程写入权重

关键：攻击发生在训练前，影响模型权重

提示：视频并非我本人制作来源于网络，也请细心品味

三、实战案例

提示词注入一个小模块【自己去找找灵感吧】：

```
https://xz.aliyun.com/news/91428
```

简单举一个案例吧，首先AI聊天界面尝试XSS，发现HTML实体化了【无从下手】？

**想必****完成了以上****AI红队学院****课程的铁子**，知道怎么入手聊天界面、API 调用或表单字段场景吧！

提示词注入尝试让对方来说出什么大象牙？

直接提示注入：

```
[...