---
title: 8G显存跑AI：Llama3.1完胜Qwen3.5？Ubuntu下四大模型横评，速度竟差一倍！
url: https://mp.weixin.qq.com/s/2Ei3yfikM3eTvMYZmNAPSA
source: Doonsec's feed
date: 2026-03-28
fetch_date: 2026-03-29T04:40:26.688850
---

# 8G显存跑AI：Llama3.1完胜Qwen3.5？Ubuntu下四大模型横评，速度竟差一倍！

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/9j14GSZeRZaZicCogK5mj0IHM96u2RZYHxhXA2mq1JDRvIlLEW7D0CnnqEIn1cJMiaqicWjLa20YntAClear5Zic3ibFXccz1ib4zZZBOQft0ejxs/0?wx_fmt=jpeg)

# 8G显存跑AI：Llama3.1完胜Qwen3.5？Ubuntu下四大模型横评，速度竟差一倍！

原创

衡水铁头哥
衡水铁头哥

铁军哥

![]()

在小说阅读器中沉浸阅读

我们之前使用ollama做了一系列的性能测试，最简单的是在Windows系统中，安装好GPU驱动，然后执行测试（[帮你省20块！仅需2条命令即可通过Ollama本地部署DeepSeek-R1模型](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458859055&idx=1&sn=3970b8bb301e9e3205a42ece81eb3a86&scene=21#wechat_redirect)）；或者是在macOS进行测试（[29瓦功耗运行140亿参数模型！Mac mini M4的AI能效革命](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458862085&idx=1&sn=e6183cb729704aeb133e03d9d391e21e&scene=21#wechat_redirect)）。

经过测试，我们还对模型的量化方式有了相对深入的了解（[目前来看，ollama量化过的DeepSeek模型应该就是最具性价比的选择](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458859385&idx=1&sn=19114c1432f3195512121e3ae6822c97&scene=21#wechat_redirect)），为后面的使用打下了良好基础。

但是，在我们上次使用手机测试的时候（[手机也能跑DeepSeek-R1/Qwen3了：零成本搭建AI推理平台](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458865100&idx=1&sn=ff8219a72e9800481c1e23911037e804&scene=21#wechat_redirect)），发现ollama其实只是对核心组件lamma.cpp做了封装，用起来方便一些，其实性能并不是最高的。以手机测试为例，ollama运行1.5B参数模型的输出速度约为20.9 TPS，运行2B参数模型的输出速度约为11.79 TPS，运行4B参数模型的输出速度约为5.14 TPS。如果使用lamma.cpp，运行3B参数模型的输出速度为25.6 TPS，差距明显。

现在，我们还差Linux系统没有测试，虽然我们之前使用vLLM运行过（[桌面显卡RTX4070部署AnythingLLM调用vLLM搭建本地大模型知识库](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458859613&idx=1&sn=b2b742656c9f1171edfabccf0398060a&scene=21#wechat_redirect)），但缺少引擎工具之间的对比，今天我们来补测一下。

我把我的RTX4070笔记本重装了一遍Ubuntu 24.04系统（[一劳永逸：实战Ubuntu服务器PXE自动化部署，从此装机so easy](https://mp.weixin.qq.com/s?__biz=MzI4NjAzMTk3MA==&mid=2458861992&idx=1&sn=0696137910a313a3eb49eb7d488b75dc&scene=21#wechat_redirect)）。第一步，就是安装显卡驱动，最简单也是最稳妥的方法，就是通过系统工具自动安装推荐的NVIDIA驱动。安装完成之后，重启笔记本。

```
apt update && apt upgrade -yubuntu-drivers autoinstallreboot
```

![](https://mmbiz.qpic.cn/mmbiz_png/9j14GSZeRZYj78ywC3eXlOOtvXZp3tW9UPqupnJ5DbKHbDdsqgibY2vEacVIq1ybX747CamvvWASmANrDhoQVyjS6PvichKPnGdOjsGPAx5dM/640?wx_fmt=png)

为了方便演示，我这次用的Desktop版本，这样就会遇到一个问题，那就是桌面进程会占用一部分显存，影响我们后续的测试。

![](https://mmbiz.qpic.cn/mmbiz_png/9j14GSZeRZYgsDXdoM6UxTLb2Mq8PLKvSTLdxC0icibUohTh1UgHU3ZacI9DFncmWngt9hfqicSfeEicWK1snrsm1RoiaiccQPtKGoia1vStic6xQs8/640?wx_fmt=png)

因为电脑还有一个集成显卡UHD 770，接下来，我们要通过Systemd的覆盖机制，强行把Intel的硬件加速驱动指定给gnome-remote-desktop，把本地显示都迁移到集显中。

```
mkdir -p ~/.config/systemd/user/gnome-remote-desktop.service.d/cat <~/.config/systemd/user/gnome-remote-desktop.service.d/override.conf[Service]Environment="LIBVA_DRIVER_NAME=iHD"Environment="VDPAU_DRIVER=va_gl"EOF
```

重新加载配置并重启桌面服务：

```
systemctl --user daemon-reloadsystemctl --user restart gnome-remote-desktop.service
```

![](https://mmbiz.qpic.cn/mmbiz_png/9j14GSZeRZYy4EyurJdGNdCyyXpEiaguwFAh31T5jOx3MoKZK6QHtRMLgXeoiacibloeYwwtx0MwAcdDXSgYABQKWQQfmIBCCIMSmpvLsjh9ia8/640?wx_fmt=png)

在混合显卡笔记本上，X11会强行在NVIDIA显卡里划走一块显存备用。我们要把它切换到更现代、原生由核显渲染的Wayland会话，斩断X11的显存占用。

在GDM配置文件中，配置WaylandEnable=true，解除Wayland封印：

```
nano /etc/gdm3/custom.confWaylandEnable=true
```

创建一个指向/dev/null的软链接，彻底屏蔽61-gdm.rules。

```
sudo ln -s /dev/null /etc/udev/rules.d/61-gdm.rules
```

然后，重启显示管理器，让Wayland真正生效：

```
systemctl restart gdm3
```

在内核模块层，禁用NVIDIA的图形输出，告诉Linux内核：这张RTX4070是一张纯算力卡，不要让它负责任何屏幕显示或画面渲染。

```
echo "options nvidia-drm modeset=0" | tee /etc/modprobe.d/99-nvidia-compute-only.conf
```

Xorg有个坏习惯，喜欢把主板上插着的所有显卡都摸一遍，我们直接在Xorg服务层，禁止自动添加副显卡，砍掉它的手：

```
mkdir -p /etc/X11/xorg.conf.d/cat <Section "ServerFlags"    Option "AutoAddGPU" "off"EndSectionEOF
```

因为显卡驱动在系统刚通电时就会加载，所以必须把上面的修改写进initramfs（底层引导镜像启动内存盘）里。

```
update-initramfs -u
```

![](https://mmbiz.qpic.cn/mmbiz_png/9j14GSZeRZauHibWkkUzf0IeA70J0QhgKsIib2cJNflwl0nQx9sZwlWU3b9lwxFXXxJchVJ3aDqJZmpB8BFtS9tbLEkGibpPGKN0vIzraIe0aA/640?wx_fmt=png)

跑完之后，直接重启笔记本：

最后，验证成果：

```
nvidia-smi
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9j14GSZeRZZATzN7k3lJZuJ8Yb9LjwK6EAHTjqnE7vpricZdQvJicDfHt6uTFqBIPqVd1ANicj8MUPRmicr1qTpxLj5gsbZMSpY3bXwVPWc9ib1Y/640?wx_fmt=png)

现在就剩下一个占用2 MB显存的SHELL了。

接下来，我们一键部署ollama服务。

```
curl -fsSL https://ollama.com/install.sh | sh
```

![](https://mmbiz.qpic.cn/mmbiz_png/9j14GSZeRZZCicEEIQHtOribpBHrJqPx9cEykZmpRzJPIrjZ2MQ1SSN5HJaP8S9mktmSXvibexeq9JI8KZJnbQjzyat4U5eiaaIZ5Nmeib3OZaz8/640?wx_fmt=png)

模型方面，基于我们之前的经验，8 GB显存一般也就能运行到INT4量化的9B参数就差不多了，要是再高一点，留给上下文的空间就不多了。所以，我们主要选择参数量在8B、9B附近的模型，毕竟底大一级压死人。

我爬取了ollama官网，一共抓取到7000+个模型，参数量为10B的只有一个，falcon3:falcon3:10b，但是这个模型的最大参数量就是10B，名不见经传，能力有限。

此外，最新的模型就是qwen3.5:9b，也是一款高参数密度的常规指令模型，得益于9B的参数量和3.5代的架构，它对Python的语法掌握极其精准，智商下限最高。支持通过OpenClaw调用API，对于输出绝对严格的JSON格式，它几乎不会出错。当然，以为模型比较到，导致它的上下文极短，如果一次性发送内容过多，它会瞬间爆显存导致系统卡死。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9j14GSZeRZauica0NBgI5yvdj6IeBxcW2IMxPgL9lUrRkBiaRoZYmcHKic7I6LBMNGQiatkffD4nkMgW2II0bWH1FMsWNogZHENDI3bhlmHJ7FE/640?wx_fmt=png)

还有最为经典的deepseek-r1:8b，RL强化学习驱动的CoT思维链模型。8B的参数量能留下比较多的显存，吞吐量和上下文空间非常充裕，适合处理复杂问题。缺点就是思考过程会产生大量内部Token，导致我们拿到最终答案的首字延迟（TTFT）较长。

![](https://mmbiz.qpic.cn/mmbiz_png/9j14GSZeRZYgLxMuibWibXzpLFngZ0qN7Fk81rQVIQz7lI0CZhKDvicibSaZv9zEedgEiav9iakWb9xUoAzOuS4iar2qC3CsUZGp1EhlDVNXB7NxzE/640?wx_fmt=png)

如果需要视觉处理，可以选择qwen3-vl:8b，能看图说话，但是图片比较吃显存，千万不要给它传4K图，一定要压缩到1080P以下，否则必爆显存。而且它处理纯文本任务的逻辑能力不如同级别的纯文本Qwen模型，不过我们还有qwen3.5:9b来处理文本。

![](https://mmbiz.qpic.cn/mmbiz_png/9j14GSZeRZaQiaRm5L8lc7tWTpSN2colmxq4CJqtmiasEM9biaDFHEg9QEia1Ms0ubVibvWQ1ibkSm9txNvLUAZMoFXAjrvB3r2XcDFCEIvicryLgo/640?wx_fmt=png)

在8B参数下，还有一个llama3.1:8b，是Meta出品的全球开源生态标准基座，有绝对的生态兼容性，主打高并发，且体积最小巧，显存压力最小，理论上速度最快。无论我们在Github上拉取任何最新的AI运维工具、Agent框架等，默认的测试模型100 %都是它。它的英文技术文档（如IETF RFC等）理解能力世界一流，但中文语言习惯稍显生硬。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9j14GSZeRZb4icPia3YCBHicqWx8cu87sJXfJS8yXmlgOHsp8emnibyEm0hfLazM7ekiantEm5jiaguslGuLpt7tCyCjIOhOwhpHhZLQWRrjfexh0/640?wx_fmt=png)

现在看来，这4个模型堪称四大金刚：遇到图片上传请求，召唤qwen3-vl:8b；遇到复杂问题，召唤deepseek-r1:8b进行深度思考；对于结构化API返回，召唤qwen3.5:9b；如果追求响应速度，召唤llama3.1:8b。因为模型都比较小，加载到显卡的时间基本上都在2秒钟以内。

```
ollama pull qwen3.5:9bollama pull qwen3-vl:8bollama pull deepseek-r1:8bollama pull llama3.1:8b
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9j14GSZeRZbcniaxmybCbe0OV3CpNhwdpz17PRYIhXUKIPxhOSXda2ibo9VFrIRbLUQqE4EFD1RNc8uhR0fT8ul80xicicM8FlLoxoYYibYGlZnw/640?wx_fmt=png)

简单测试一下输出速度。测试提示词如下：

你是一个资深网络工程师。我现在的网络拓扑如下：R1和R2运行OSPF，都在Area 0。R2和R3运行BGP（eBGP）。R2将OSPF路由重分发进了BGP。

现在出现了一个故障：R3能够学习到R1的Loopback接口路由，但是R3无法ping通R1的Loopback接口。请列出排查此故障的3个最可能原因，并给出具体的排查命令（假设设备为华为VRP操作系统）。要求逻辑严密，不要有废话。

先测试qwen3.5:9b。

```
ollama run qwen3.5:9b --verbose
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9j14GSZeRZaSpV4FTEO79QyOU8uLR093ia3956WxwicocItGksqqeT4ZibVP5ezvQpsLR7Nic90RPzicT8Fy5icic84XicU2P1p1ZJibBVqQEAr8ncos/640?wx_fmt=png)

中间卡了大概十秒。好像触发了极其经典的复读机幻觉，最终回答失败了，用了将近8分钟，一共输出12225 token，平均速度26.26 TPS。

![](https://mmbiz.qpic.cn/mmbiz_png/9j14GSZeRZaibkXibhHxFibrKDLn7pesGs2fCAQPFpEKJ0suNnoPW9B6SiaMSmKD7SRP5kn2orZ63LXpOJyhlgfzfIelvQuybTvF33OjiaOsZtfI/640?wx_fmt=png)

运行过程中，显存占用6154 MB，功率67瓦，还有空间，就是不太实用。

接下来测试上一代的qwen3-vl:8b，我们把问题换成图片，提示词为【看一下/root/ScreenShot\_2026-03-27\_220856\_249.png的问题】。

```
ollama run qwen3-vl:8b --verbose
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9j14GSZeRZYiaZJOeTMdz1z45PVFSdcrIx9QFia060ia236dCYgW4YpmCXKbOvAw40onqoyrr5ibNc81g4ibB8C2L9laTPCls8eUD6GQPZibLd56Y/640?wx_fmt=png)

几乎没有延迟，马上就识别到了问题，但是思考过程中，前半段是中文，后半段是英文。但好歹比3.5好使，用时两分半，一共输出6914 token，平均速度44.93 TPS，比3.5快了71 %。

![](https://mmbiz.qpic.cn/mmbiz_png/9j14GSZeRZZFlkChrqJYofJsOs9AjYiaZ2tNP0z6grPEuiaibQBvMNnNxicVptgVw54dlRY0gU8ROAmtMDrrcxRgWxfYej678B3hZic5aCQoHrpQ/640?wx_fmt=png)

运行过程中，显存占用6858 MB，功率105瓦，比9B模型资源消耗还多。

然后试试经典的deepseek-r1:8b。

```
ollama run deepseek-r1:8b --verbose
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9j14GSZeRZa4IRZTiaQ12Q0yE9ggl2wFXJF905aBHDjtXHXtNn68e9vZYOibk45ibD7hmypHWCc2gcM7jazAlwxeLAHa9ia2w2QrXSmIhKhNgIM/640?wx_fmt=png)

不愧是一代经典，仅用时34秒，一共输出1575 token，平均速度46.05 TPS，比qwen3-vl:8b稍微快一点点，大概2 %。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9j14GSZeRZbNo9lFCJwEFSiczIADIvtndlZDP7icQlq6pCLGtk9pKNbT8HDUYESuzKTlrptaadvmpTSiaYrx8tLyAx2KDN9n4T3tuiajRs6bAhM/640?wx_fmt=png)

运行过程中，显存占用5504 MB，功率100瓦。

最后试试经典的llama3.1:8b。

```
ollama run l...