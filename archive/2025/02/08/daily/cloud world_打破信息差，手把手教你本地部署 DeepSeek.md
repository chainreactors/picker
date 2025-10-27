---
title: 打破信息差，手把手教你本地部署 DeepSeek
url: https://cloudsjhan.github.io/2025/02/07/%E6%89%93%E7%A0%B4%E4%BF%A1%E6%81%AF%E5%B7%AE%EF%BC%8C%E6%89%8B%E6%8A%8A%E6%89%8B%E6%95%99%E4%BD%A0%E6%9C%AC%E5%9C%B0%E9%83%A8%E7%BD%B2-DeepSeek/
source: cloud world
date: 2025-02-08
fetch_date: 2025-10-06T20:35:30.051953
---

# 打破信息差，手把手教你本地部署 DeepSeek

[cloud world](/)

# To be A geek

* [home](/)
* [tags](/tags/)
* [categories](/categories/)
* [archives](/archives/)
* [top](/top)
* [about](/about/)
* search

## 打破信息差，手把手教你本地部署 DeepSeek

posted

2025-02-07

|

in

[deepseek](/categories/deepseek/)

|

visitors:

|

|

wordcount:

1,409
|

min2read ≈

5

打破信息差，手把手教你本地部署 DeepSeek

![](https://)

# 打破信息差，手把手教你本地部署 DeepSeek

在AI技术迅速发展的今天，越来越多的人开始尝试将大语言模型（如DeepSeek）应用于日常学习和工作中。然而，对于普通用户来说，如何快速、便捷地在本地环境中部署并使用这些工具仍然存在一定的门槛。再加上最近官方 deepseek 访问压力大和来源未知的大量 ddos 攻击，经常出现服务器访问繁忙的情况，使用体验并不好。

![](https://files.mdnice.com/user/4760/b79ca9aa-60ff-4936-97b4-b56025dcd0f6.png)

本文将以 **Open Web UI** 和 **Ollama** 为例，手把手教你完成本地部署，让你轻松实现与AI模型的交互，本教程适合新手和不具备相关行业经验的小白新手。

---

## 为什么要本地部署？

1. **数据隐私**：相比于在线服务，本地部署可以避免将数据上传到云端，确保敏感信息的安全性。
2. **个性化配置**：可以根据自己的需求调整服务参数，获得更好的使用体验。
3. **低成本运行**：通过开源工具和本地资源，大幅降低使用成本。

---

## 部署前的准备

在开始部署之前，请确认以下几点：

1. **安装依赖**：
   * 确保你的系统已经安装了Python 3.11或更高版本。
   * 如果你选择使用Docker，则需要先安装 Docker 和 Docker Compose。
2. **网络环境**：确保本地网络可以正常访问互联网，以便下载所需的软件包和镜像。

---

## 步骤一：安装并启动 Open Web UI

![](https://files.mdnice.com/user/4760/1837ddf4-4735-4466-ac34-e074a021f190.png)

[Open Web UI](https://github.com/open-webui/open-webui "open webui") 是一个基于Web的界面工具，支持与多种AI模型（包括DeepSeek）进行交互。以下是两种常见的安装方式：

### 方式一：通过 pip 安装

如果你更倾向于直接在本地机器上运行服务，可以使用以下命令：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` pip3.11 install open-webui ``` |

安装完成后，输入以下命令启动服务：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` open-webui --host 0.0.0.0 --port 3000 ``` |

这将在本地的 `localhost:3000` 端口启动一个Web界面。

### 方式二：通过 Docker 安装（推荐）

如果你希望更简单地管理服务，可以使用 Docker。运行以下命令：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 ``` | ``` docker run -d \   -p 3000:8080 \   --add-host=host.docker.internal:host-gateway \   -v open-webui:/app/backend/data \   --name open-webui \   --restart always \   ghcr.io/open-webui/open-webui:main ``` |

这条命令会下载并运行 Open Web UI 的Docker镜像，服务会在 `localhost:3000` 端口启动。

---

## 步骤二：安装并启动 Ollama

![](https://files.mdnice.com/user/4760/0a0818a2-bcb0-4207-a433-9e74b97f3e47.png)

[Ollama](https://ollama.com/ "ollama") 是一个轻量级的AI模型运行工具，支持多种大语言模型。你需要先在本地安装并启动 Ollama 服务，然后将其与 Open Web UI 集成。

### 安装 Ollama

根据你的操作系统选择相应的安装方式：

#### 在 Linux 上：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` curl -s https://ollama.ai/install.sh | bash ``` |

#### 在 macOS 上：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` brew install ollama ``` |

#### 在 Windows 上：

你可以通过 [Ollama 官方网站](https://ollama.ai/) 下载安装包。

### 启动 Ollama

安装完成后，运行以下命令启动服务：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` ollama serve --listen 0.0.0.0:11434 ``` |

这样，Ollama 将在 `localhost:11434` 端口提供模型推理服务。

### 模型下载

deepseek 提供了不同参数数量的模型，比如 7b, 14b, 32b, 70b 和满血版本的 671b，这里根据你的机器配置选择不同的参数，我本地的机器是 128g 的内存，选择了 32b 的模型，仅供参考。

![](https://files.mdnice.com/user/4760/0888b630-00a5-413e-af37-a975031e2f8d.png)

|  |  |
| --- | --- |
| ``` 1 ``` | ``` ollama run deepseek-r1:32b ``` |

---

## 步骤三：配置 Open Web UI

启动 Open Web UI 后，访问 `http://localhost:3000`，你需要进行以下配置：

![](https://files.mdnice.com/user/4760/0d0901b9-95dc-4873-960a-934ba9cd09bb.png)

1. **添加 Ollama 服务**：

   * 在页面上找到“Add New Model”或类似选项。
   * 填写模型名称（如 DeepSeek）和地址（`http://localhost:11434/api/generate`）。
   * 确保勾选支持的模型类型（如文本生成、问答等）。
2. **验证连接**：

   * 配置完成后，尝试发送一条简单的查询（例如“你好”）。
   * 如果返回正常结果，则说明配置成功。

---

## 步骤四：测试 DeepSeek 功能

完成上述步骤后，你就可以通过 Open Web UI 使用 DeepSeek 提供的功能了。以下是几个常见的使用场景：

1. **文本生成**：
   * 输入类似“写一篇关于人工智能的科普文章”。
2. **问答交互**：
   * 提问：“DeepSeek 和其他大语言模型有什么区别？”
3. **代码辅助**：
   * 输入：“帮我写一个Python脚本，用于计算斐波那契数列。”

---

## 常见问题与故障排查

1. **服务无法启动**：

   * 检查端口是否被占用（如 `3000` 或 `11434`）。
   * 确保防火墙或安全软件没有阻止相关端口的访问。
2. **模型响应慢或无响应**：

   * 确认 Ollama 服务是否正常运行。
   * 检查网络连接，确保模型可以访问互联网（部分模型依赖于在线资源）。
3. **配置错误**：

   * 确保 Open Web UI 和 Ollama 的地址配置正确。
   * 参考官方文档或社区论坛，获取更多帮助。

---

## More

如果是想使用满血版本的 deepseek r1 ，目前稳定输出方案就是在硅基流动生成 API 密钥，结合 [CHATBOX](https://chatboxai.app/zh "chatboxai")使用。不过该方案稍微复杂，适合有些基础的同学，感兴趣的话后面开新的教程讲一下。

## 总结

通过本文的指导，你已经成功在本地部署了 DeepSeek 相关服务，并可以通过 Open Web UI 与模型进行交互。这种方式不仅降低了使用成本，还提供了更高的灵活性和安全性。如果你对AI技术感兴趣，不妨尝试将这些工具应用到更多的场景中，进一步探索其潜力！

---

-------------The End-------------

Title:[打破信息差，手把手教你本地部署 DeepSeek](/2025/02/07/%E6%89%93%E7%A0%B4%E4%BF%A1%E6%81%AF%E5%B7%AE%EF%BC%8C%E6%89%8B%E6%8A%8A%E6%89%8B%E6%95%99%E4%BD%A0%E6%9C%AC%E5%9C%B0%E9%83%A8%E7%BD%B2-DeepSeek/)

Author:[cloud sjhan](/ "visit cloud sjhan blog")

Publish Time:2025年02月07日 - 17:02

Last Update:2025年02月07日 - 17:02

Original Link:[https://cloudsjhan.github.io/2025/02/07/打破信息差，手把手教你本地部署-DeepSeek/](/2025/02/07/%E6%89%93%E7%A0%B4%E4%BF%A1%E6%81%AF%E5%B7%AE%EF%BC%8C%E6%89%8B%E6%8A%8A%E6%89%8B%E6%95%99%E4%BD%A0%E6%9C%AC%E5%9C%B0%E9%83%A8%E7%BD%B2-DeepSeek/ "打破信息差，手把手教你本地部署 DeepSeek")

License: [By-NC-ND 4.0 international](https://creativecommons.org/licenses/by-nc-nd/4.0/ "Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)")。

![cloud sjhan wechat](/images/wechat-qcode.jpg)

keep going, keep coding

donate

![cloud sjhan 微信支付](/images/wechatpay.jpg)

![cloud sjhan 支付宝](/images/alipay.jpg)

[deepseek](/tags/deepseek/)

(>给这篇博客打个分吧<)

[Testing Databend Applications Using Testcontainers - Multi-Language Implementation Guide](/2024/11/26/Testing-Databend-Applications-Using-Testcontainers-Multi-Language-Implementation-Guide/ "Testing Databend Applications Using Testcontainers - Multi-Language Implementation Guide")

[使用 Seatunnel 建立从 MySQL 到 Databend 的数据同步管道](/2025/07/07/%E4%BD%BF%E7%94%A8-Seatunnel-%E5%BB%BA%E7%AB%8B%E4%BB%8E-MySQL-%E5%88%B0-Databend-%E7%9A%84%E6%95%B0%E6%8D%AE%E5%90%8C%E6%AD%A5%E7%AE%A1%E9%81%93/ "使用 Seatunnel 建立从 MySQL 到 Databend 的数据同步管道")

* Content
* Overview

![cloud sjhan](/images/avatar.png)

[166
日志](/archives/)

[40
分类](/categories/index.html)

[73
标签](/tags/index.html)

[RSS](/atom.xml)

[GitHub](https://github.com/hantmac "GitHub")

E-Mail

Links

* [CSDN](https://blog.csdn.net/u012421976 "CSDN")
* [w3school](http://www.w3school.com.cn/ "w3school")
* [快搜](http://search.chongbuluo.com/ "快搜")

1. [1. 打破信息差，手把手教你本地部署 DeepSeek](#打破信息差，手把手教你本地部署-DeepSeek)
   1. [1.1. 为什么要本地部署？](#为什么要本地部署？)
   2. [1.2. 部署前的准备](#部署前的准备)
   3. [1.3. 步骤一：安装并启动 Open Web UI](#步骤一：安装并启动-Open-Web-UI)
      1. [1.3.1. 方式一：通过 pip 安装](#方式一：通过-pip-安装)
      2. [1.3.2. 方式二：通过 Docker 安装（推荐）](#方式二：通过-Docker-安装（推荐）)
   4. [1.4. 步骤二：安装并启动 Ollama](#步骤二：安装并启动-Ollama)
      1. [1.4.1. 安装 Ollama](#安装-Ollama)
         1. [1.4.1.1. 在 Linux 上：](#在-Linux-上：)
         2. [1.4.1.2. 在 macOS 上：](#在-macOS-上：)
         3. [1.4.1.3. 在 Windows 上：](#在-Windows-上：)
      2. [1.4.2. 启动 Ollama](#启动-Ollama)
      3. [1.4.3. 模型下载](#模型下载)
   5. [1.5. 步骤三：配置 Open Web UI](#步骤三：配置-Open-Web-UI)
   6. [1.6. 步骤四：测试 DeepSeek 功能](#步骤四：测试-DeepSeek-功能)
   7. [1.7. 常见问题与故障排查](#常见问题与故障排查)
   8. [1.8. More](#More)
   9. [1.9. 总结](#总结)

© 2018 — 2025

cloud sjhan
|

Site words total count:
308.0k

stay hungry,stay foolish

Total Words:308.0k

0%

;