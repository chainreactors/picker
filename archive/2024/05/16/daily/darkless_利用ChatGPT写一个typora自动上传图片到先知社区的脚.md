---
title: 利用ChatGPT写一个typora自动上传图片到先知社区的脚
url: https://darkless.cn/2024/05/15/chatgpt-typora-uploadimage/
source: darkless
date: 2024-05-16
fetch_date: 2025-10-06T17:16:06.891046
---

# 利用ChatGPT写一个typora自动上传图片到先知社区的脚

[![](/images/logo1.svg)](/)
[darkless](/)

* [首页](/)
* [归档](/archives/)
* [标签](/tags/)
* [分类](/categories/)
* [文档](https://doc.darkless.cn/)
* [安全工具](https://darkless.notion.site/12832eebad358008894af8e247044d02)
* [留言](/contact/)

* [首页](/)
* [归档](/archives/)
* [标签](/tags/)
* [分类](/categories/)
* [文档](https://doc.darkless.cn/)
* [安全工具](https://darkless.notion.site/12832eebad358008894af8e247044d02)
* [留言](/contact/)

利用ChatGPT写一个typora自动上传图片到先知社区的脚

![](https://cdn.jsdelivr.net/gh/handbye/images@master/uPic/2024/05/BUHNHt.png)

![](/images/avatar.webp)

darkless

2024-05-15

2024-05-15

* [日常](/categories/%E6%97%A5%E5%B8%B8/)
* [工具使用](/categories/%E6%97%A5%E5%B8%B8/%E5%B7%A5%E5%85%B7%E4%BD%BF%E7%94%A8/)

* [ChatGPT](/tags/chatgpt/)
* [typora](/tags/typora/)

起因是先知社区升级后，图片全部加了防盗链，并且投稿的文章必须使用先知社区本身的图床，那就导致本地markdown写完后需要将图片一个一个复制到先知社区的文章编辑器内获取图片地址。

文章图片太多了，就很不方便，于是决定使用typora自带的图片上传功能来解决这个问题。

首先看下先知社区的图片上传包：

|  |
| --- |
| ``` POST /forum/upload HTTP/1.1 Origin: https://xz.aliyun.com X-Requested-With: XMLHttpRequest Referer: https://xz.aliyun.com/t/new?time__1311=CqjEY5iIeIox%2FD0lD2QAG8KD8ADCl0b4PD&alichlgref=https%3A%2F%2Fxz.aliyun.com%2Fnotifications Cookie: xxx Content-Type: application/x-www-form-urlencoded; charset=UTF-8 X-Csrftoken: xxx Host: xz.aliyun.com  base=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAB5AAAACGCAYAAAAb8ha9AAAKqWlDQ1BJQ0MgUHJvZmlsZQAASImVlwdQU%2BkWx797bzoJLRCKlNCb9BZASugBBKSDjZAECCXGQ ``` |

将图片转成base64然后post上传

在看下返回包：

|  |
| --- |
| ``` {"success": 1, "message": "", "url": "https://xzfile.aliyuncs.com/media/upload/picture/20240515135923-4797a520-1280-1.png"} ``` |

一个json格式的文件，url就算要拿到的图片地址

拿到这些信息后，我决定使用go语言来编写这个脚本，那么还得去了解下typora自定义命令上传图片的规则，我决定把这个事交给ChatGPT来做，并让他给我写出完整的脚本。

**这里给出我和GPT的完整对话：**

你知道typora的自定义命令上传图片吗

ChatGPT

在 Typora 中，您可以通过自定义命令来实现图片上传功能。这通常涉及设置外部脚本或程序，将本地图片文件上传到图床（如图像托管服务）并返回图片的 URL。以下是如何配置 Typora 使用自定义命令上传图片的步骤：

1. **准备上传脚本**：
   编写一个脚本来处理图片上传，并返回图片的 URL。以下是一个使用 Python 的示例脚本，利用 **`requests`** 库将图片上传到图床（例如，图床服务 sm.ms）。

   |  |
   | --- |
   | ``` import sys import requests  def upload_image(file_path):     url = "https://sm.ms/api/v2/upload"     headers = {         "Authorization": "YOUR_SMMS_API_KEY"     }     with open(file_path, "rb") as f:         files = {"smfile": f}         response = requests.post(url, headers=headers, files=files)     if response.status_code == 200 and response.json()["code"] == "success":         return response.json()["data"]["url"]     else:         return None  if __name__ == "__main__":     file_path = sys.argv[1]     image_url = upload_image(file_path)     if image_url:         print(image_url)     else:         print("Upload failed", file=sys.stderr) ``` |

   请替换 **`"YOUR_SMMS_API_KEY"`** 为您从 sm.ms 获取的 API 密钥。
2. **保存脚本**：
   将上述脚本保存为一个文件，例如 \*\*`upload_image.py`\*\*，并确保它具有可执行权限。
3. **配置 Typora**：
   打开 Typora，进入设置界面（File -> Preferences -> Image），在 “Image Upload Setting” 中选择 “Custom Command”。

   在 “Command” 栏中，输入如下内容（根据实际脚本路径修改）：

   |  |
   | --- |
   | ``` python /path/to/upload_image.py ``` |
4. **使用自定义命令上传图片**：
   在 Typora 中插入图片时，可以通过点击右键选择 “Upload Image” 或直接粘贴图片来触发自定义命令。Typora 将调用您的脚本上传图片，并自动插入返回的图片 URL。

这样配置完成后，每次在 Typora 中上传图片时，您的脚本会被调用，并将图片上传到指定的图床服务，返回的 URL 将自动插入到文档中。

我想用go语言实现

ChatGPT

使用 Go 语言实现一个上传图片到图床（例如 sm.ms）的脚本，并配置 Typora 来调用这个脚本。下面是具体步骤：

1. **编写 Go 脚本**：
   首先，编写一个 Go 程序，将图片上传到图床并返回图片的 URL。这里假设使用 sm.ms 作为图床服务。

   |  |
   | --- |
   | ``` package main  import (     "bytes"     "encoding/json"     "flag"     "fmt"     "io/ioutil"     "mime/multipart"     "net/http"     "os" )  const (     smmsAPI = "https://sm.ms/api/v2/upload"     apiKey  = "YOUR_SMMS_API_KEY" // 替换为你的 sm.ms API 密钥 )  type SmmsResponse struct {     Success bool `json:"success"`     Data    struct {         URL string `json:"url"`     } `json:"data"`     Message string `json:"message"` }  func uploadImage(filePath string) (string, error) {     file, err := os.Open(filePath)     if err != nil {         return "", err     }     defer file.Close()      var buf bytes.Buffer     writer := multipart.NewWriter(&buf)     part, err := writer.CreateFormFile("smfile", file.Name())     if err != nil {         return "", err     }      _, err = io.Copy(part, file)     if err != nil {         return "", err     }      writer.Close()      req, err := http.NewRequest("POST", smmsAPI, &buf)     if err != nil {         return "", err     }      req.Header.Set("Authorization", apiKey)     req.Header.Set("Content-Type", writer.FormDataContentType())      client := &http.Client{}     resp, err := client.Do(req)     if err != nil {         return "", err     }     defer resp.Body.Close()      body, err := ioutil.ReadAll(resp.Body)     if err != nil {         return "", err     }      var res SmmsResponse     err = json.Unmarshal(body, &res)     if err != nil {         return "", err     }      if res.Success {         return res.Data.URL, nil     } else {         return "", fmt.Errorf("upload failed: %s", res.Message)     } }  func main() {     filePath := flag.String("file", "", "Path to the image file to upload")     flag.Parse()      if *filePath == "" {         fmt.Println("Usage: upload_image --file <path_to_image>")         os.Exit(1)     }      url, err := uploadImage(*filePath)     if err != nil {         fmt.Fprintf(os.Stderr, "Error: %v\n", err)         os.Exit(1)     }      fmt.Println(url) } ``` |

   将上述代码保存为 \*\*`upload_image.go`\*\*。
2. **编译 Go 程序**：
   使用 Go 编译程序，生成可执行文件。

   |  |
   | --- |
   | ``` go build -o upload_image upload_image.go ``` |
3. **配置 Typora**：
   打开 Typora，进入设置界面（File -> Preferences -> Image），在 “Image Upload Setting” 中选择 “Custom Command”。

   在 “Command” 栏中，输入如下内容（根据实际脚本路径修改）：

   |  |
   | --- |
   | ``` /path/to/upload_image --file $IMAGE ``` |
4. **使用自定义命令上传图片**：
   在 Typora 中插入图片时，可以通过点击右键选择 “Upload Image” 或直接粘贴图片来触发自定义命令。Typora 将调用您的 Go 程序上传图片，并自动插入返回的图片 URL。

这样配置完成后，每次在 Typora 中上传图片时，您的 Go 程序会被调用，并将图片上传到指定的图床服务，返回的 URL 将自动插入到文档中。

现在有个http请求包和返回包，请根据这两个包的来帮我写这个go程序

ChatGPT

当然可以，您可以提供 HTTP 请求包和返回包的示例吗？这样我可以更准确地根据这些信息编写相应的 Go 程序。如果您还没有示例，我可以假设一个典型的 HTTP 请求和响应，帮助您编写这个程序。

|  |
| --- |
| ``` 这个是http请求包： POST /forum/upload HTTP/1.1 Origin: https://xz.aliyun.com X-Requested-With: XMLHttpRequest Referer: https://xz.aliyun.com/t/new?time__1311=CqjEY5iIeIox%2FD0lD2QAG8KD8ADCl0b4PD&alichlgref=https%3A%2F%2Fxz.aliyun.com%2Fnotifications Cookie: cna=qhbCHtO32zMBASQJimIZ6nLk; munb=2206485386045; login_current_pk=1004124416781918; aliyun_lang=zh; currentRegionId=cn-hangzhou;  Content-Type: application/x-www-form-urlencoded; charset=UTF-8 X-Csrftoken: 9zeynVEPM308AyZKFbbaw4BPUbm1sTU5G3uAEGcHecIqggFx9wfIUUhqV3qbXms0 Host: xz.aliyun.com  base=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAB5AAAACGCAYAAAAb8ha9AAAKqWlDQ1BJQ0MgUHJvZmlsZQAASImVlwdQU%2BkWx797bzoJLRCKlNCb9BZASugBBKSDjZAECCXGQBCxI4srsBZURLCiK03BRSmyFgQUC4uAolgXZFFQ1sWCDcu7wBDcffPem3dmzny%2F%2FHxxx  http返回包如下： {"success": 1, "message": "", "url": "https://xzfile.aliyuncs.com/media/upload/picture/20240515135923-4797a520-1280-1.png"} ``` |

ChatGPT

好的，根据您提供的 HTTP 请求和返回包，我们可以编写一个 Go 语言程序来实现图片上传。以下是完整的 Go 代码实现：

1. **编写 Go 脚本**：
   这个脚本将读取图片文件的路径，将其编码为 base64，构建 HTTP POST 请求，并将图片上传到指定的服务器。然后，解析返回的 JSON 数据以获取图片的 URL。

   |  |
   | --- |
   | ``` package main  import (     "encoding/base64"     "encoding/json"     "flag"     "fmt"     "io/ioutil"     "net/http"     "net/url"     "os"     "strings" )  const (     uploadURL = "https://xz.aliyun.com/forum/upload"     referer   = "https://xz.aliyun.com/t/new?time__1311=CqjEY5iIeIox%2FD0lD2QAG8KD8ADCl0b4PD&alichlgref=https%3A%2F%2Fxz.aliyun.com%2Fnotifications"     origin    = "https://xz.aliyun.com"     csrfToken = "9zeynVEPM308AyZKFbbaw4BPUbm1sTU5G3uAEGcHecIqggFx9wfIUUhqV3qbXms0" // 替换为您的 CSRF token     cookie    = "xxx" // 替换为您的 cookie )  type UploadResponse struct {     Success int    `json:"success"`     Message string `json:"message"`     URL     string `json:"url"` }  func encodeImageToBase64(filePath string) (string, error) {     file, err := os...