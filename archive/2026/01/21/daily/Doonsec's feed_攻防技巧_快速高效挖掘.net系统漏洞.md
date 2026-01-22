---
title: 攻防技巧|快速高效挖掘.net系统漏洞
url: https://mp.weixin.qq.com/s/cRPHl0FEL3kDkyQZ7GYo7g
source: Doonsec's feed
date: 2026-01-21
fetch_date: 2026-01-22T03:34:21.683552
---

# 攻防技巧|快速高效挖掘.net系统漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/h8P1KUHOKuazhHYOsWHGzvMq4ZoTCRysb7Q1hicXrYALibzKUiadKoMv3Jeict9AlTJtXsdbkWdzqx8yXnv2SAicdYA/0?wx_fmt=jpeg)

# 攻防技巧|快速高效挖掘.net系统漏洞

Z2O安全攻防

![]()

在小说阅读器中沉浸阅读

以下文章来源于亿人安全
，作者hyyrent

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM7P6QhEtne4ElK29ATrgstibwthblEw9OciaJSBtquvAEKA/0)

**亿人安全**
.

知其黑，守其白。手握利剑，心系安全。主要研究方向包括：Web、内网、红蓝对抗、代码审计、安卓逆向、CTF。

### 在红队攻防对抗中，.NET系统是出现频次比较高，.NET系统由于其架构特性，通常会将业务逻辑封装在DLL程序集中，通过ASPX/ASHX等页面文件进行调用。这种架构使得我们能够通过反编译技术快速还原源代码，结合静态代码审计和动态测试，快速定位SQL注入、命令执行、文件上传、反序列化等常见高危漏洞。本文将围绕获取源码、反编译、漏洞快速定位、绕过技巧和实战案例来帮助师傅们快速在红队场景中挖掘0day

---

### 源码获取

凌风云网盘

https://www.lingfengyun.com/

![](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTTooEibtJNAdotkGsicKFvAly6OHmLKWibfKlNSsrPESkJ8EZib7iav2QqyajMbdicoBvY4lrJDkTq5jYcKw/640?wx_fmt=png&from=appmsg)

闲鱼购买

![](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTTooEibtJNAdotkGsicKFvAly6REApSV7ISwJmtrdWIvbLVCZiax0VNcXBBLicrTZm9PvucQ0H6g6xnMmQ/640?wx_fmt=png&from=appmsg)

指纹提取旁站扫描备份文件

指纹提取 body=”xxxx” + 压缩文件目录扫描 （指定文件名www.zip）

![](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTTooEibtJNAdotkGsicKFvAly6mrhvUXf9MQqBhsFHTqmNFdfEiazm3XeZYQ2dGpZ3ZAmUTSDPqDK3QZg/640?wx_fmt=png&from=appmsg)

### 反编译dll+去混淆

反编译 / 静态查看：ILSpy、dnSpy、dotPeek

dnSpy单个打开并导出到工程

![](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTTooEibtJNAdotkGsicKFvAly6jfnjmxHMltFiauJmM7iazoaCYddX25hzicQMjL5WsqibW3G9wn4rhiauIbg/640?wx_fmt=png&from=appmsg)

使用dnSpy批量打开:

|  |
| --- |
| ``` File -> Open -> 选择整个 bin 目录 dnSpy会自动加载所有程序集 ``` |

使用ILSpy命令行:

|  |
| --- |
| ``` # 安装 ilspycmd dotnet tool install ilspycmd -g  # 反编译整个目录 ilspycmd -p -o output_dir .\bin\*.dll  # 反编译到单个文件 ilspycmd -p -o output.cs .\bin\YourApp.dll ``` |

使用脚本批量反编译:

把下面的代码保存为bat文件，放到bin目录下，该bat脚本会在每个DLL所在目录下创建一个与 DLL 同名的文件夹

（例如`C:\xxx\lib\test.dll`→`C:\xxx\lib\test\`），并将`ilspycmd`的输出写入该文件夹

|  |
| --- |
| ``` @echo off chcp 65001 setlocal enabledelayedexpansion  REM 从当前目录递归查找所有 dll for /R %%F in (*.dll) do (     REM %%F = 完整路径（含文件名和扩展名）     set "dll_path=%%F"     set "dll_name=%%~nF"     set "dll_dir=%%~dpF"     set "out_dir=%%~dpF%%~nF"      echo 正在导出 "%%F" 到 "!out_dir!\ ..."     if not exist "!out_dir!\" mkdir "!out_dir!"      ilspycmd -p -o "!out_dir!" "%%F" )  echo 全部完成！ pause ``` |

去混淆: 混淆后的代码可能会出现类似的片段：

|  |
| --- |
| ``` private string \u0001; private void \u0002(string \u0003) {     if (this.\u0001 == \u0003) } ``` |

![](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTTooEibtJNAdotkGsicKFvAly6ZKJIQvgZbRYojQYMHZF5F8zOaMAB9kDvtTDqBrPYGYVuEPueBZVhqQ/640?wx_fmt=png&from=appmsg)

处理混淆代码: 使用 de4dot 去混淆，下载程序添加至环境变量

https://github.com/0xd4d/de4dot

https://github.com/ViRb3/de4dot-cex

|  |
| --- |
| ``` de4dot.exe source.dll -o Remove_obfuscated.dll de4dot.exe -r D:\input -ru -ro D:\output ``` |

单个反编译太慢，我们可以使用命令或脚本进行快速批量去混淆

|  |
| --- |
| ``` #!/usr/bin/env python3 import os import subprocess import shutil from pathlib import Path import time  def main():     print("🔧 快速de4dot批量反混淆工具")     print("=" * 40)     try:         result = subprocess.run(["de4dot", "--help"], capture_output=True, text=True, timeout=5)         if result.returncode != 0:             raise Exception("de4dot命令执行失败")         print("✅ de4dot全局命令检查通过")     except Exception as e:         print(f"❌ de4dot全局命令不可用: {e}")         return      current_dir = Path(".")     dll_files = []     for pattern in ["*.dll", "*.exe"]:         dll_files.extend(current_dir.glob(pattern))      exclude_patterns = [         "System.", "Microsoft.", "Newtonsoft.", "EntityFramework",         "Oracle.", "MySql.", "NLog.", "Quartz.", "RestSharp",         "StackExchange.", "Thinktecture.", "BouncyCastle"     ]     filtered_files = [f for f in dll_files if not any(p in f.name for p in exclude_patterns)]      if not filtered_files:         print("❌ 当前目录没有找到需要处理的DLL文件")         return      print(f"📁 找到 {len(filtered_files)} 个文件需要处理:")     for f in filtered_files:         print(f"   - {f.name}")      output_dir = Path("deobfuscated")     output_dir.mkdir(exist_ok=True)     print(f"\n🚀 开始处理...")     print(f"输出目录: {output_dir.absolute()}")      success_count = 0     start_time = time.time()     for i, dll_file in enumerate(filtered_files, 1):         print(f"\n[{i}/{len(filtered_files)}] 🔄 处理: {dll_file.name}")         try:             output_subdir = output_dir / dll_file.stem             output_subdir.mkdir(exist_ok=True)             cmd = ["de4dot", str(dll_file), "-o", str(output_subdir / dll_file.name)]             print(f"   执行: {' '.join(cmd)}")             result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)             if result.returncode == 0:                 print(f"   ✅ 成功: {dll_file.name}")                 success_count += 1             else:                 print(f"   ❌ 失败: {dll_file.name}")         except subprocess.TimeoutExpired:             print(f"   ⏰ 超时: {dll_file.name}")         except Exception as e:             print(f"   ❌ 异常: {dll_file.name} - {e}")      end_time = time.time()     print(f"\n📊 处理完成! 成功 {success_count}/{len(filtered_files)} 个, 耗时 {end_time - start_time:.1f} 秒")     print(f"输出目录: {output_dir.absolute()}")     print("\n🎉 批量反混淆完成!")  if __name__ == "__main__":     main() ``` |

![](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTTooEibtJNAdotkGsicKFvAly6ybTsfBibznnRZKe14UlaVynicPBY3O6S3pP2ZX9zQq17MYQVLdmWl8ng/640?wx_fmt=png&from=appmsg)

去混淆前后对比

![](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTTooEibtJNAdotkGsicKFvAly6yDdK4bFwOibDeqVAkQPDmTS2b7WfLnKGIabbn2MZiaT6Yia9IZVmrFe9Q/640?wx_fmt=png&from=appmsg)

### ashx和dll映射关系

如`AjaxUpload.aspx`，逻辑代码在`AjaxUpload.aspx.cs`，页面会继承`M_Main.AjaxUpload`类，并自动绑定事件

![](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTTooEibtJNAdotkGsicKFvAly6Sp5ibpyknQGfn5hbwDv4jffENXIvTjM91Fxcic3zuGxPPAe1B7OGMpUw/640?wx_fmt=png&from=appmsg)

这时候我们反编译`M_Main.dll`，并找到对应的`AjaxUpload`类，便可以开始愉快的代码审计了

![](https://mmbiz.qpic.cn/mmbiz_png/iar31WKQlTTooEibtJNAdotkGsicKFvAly6nx15WUkEFiaYEvL9NgWibXXiaINV8URYp2Qxdj1V2cjWwoZdXoicxFdEGw/640?wx_fmt=png&from=appmsg)

### 常见漏洞sink点

|  |  |  |
| --- | --- | --- |
| 漏洞类型 | 漏洞Sink点 | 审计描述 |
| SQL 注入 | `ExecuteNonQuery()`  ,`ExecuteReader()`  ,`ExecuteScalar()`  ,`SqlDataAdapter.Fill()`  ,`ExecuteSqlCommand()`  ,`ExecuteSqlRaw()`  ,`CreateSQLQuery()`  ,`connection.Query()` | 检查点：查找 SQL 语句是否通过字符串拼接或格式化（`+`  ,`String.Format`  ,`$""`  ）将`Request/Query/Form/Cookie`  等直接插入。 |
| 命令执行（RCE） | `Process.Start()`  ,`ProcessStartInfo.FileName`  ,`ProcessStartInfo.Arguments` | 检查点：是否把用户输入拼接到命令或传给 shell/PowerShell，`FileName`  与`Arguments`  是否来自外部 |
| 文件上传 / 任意文件写入 | `SaveAs()`  ,`WriteAllBytes()`  ,`WriteAllText()`  ,`FileStream.Write()` | 检查点：是否校验扩展名、MIME、内容类型、文件名（路径分隔符）、以及保存目录权限；是否防止覆盖已有文件，上传可执行脚本（`.aspx`  /`.ashx`  ）getshell |
| 反序列化 | `BinaryFormatter.Deserialize()`  ,`SoapFormatter.Deserialize()`  ,`JsonConvert.DeserializeObject()`  ,`LosFormatter.Deserialize()` | 检查点：反序列化是否对不可信输入（Request、Cookie、ViewState、文件等）执行；是否使用不安全的序列化库（BinaryFormatter、SoapFormatter） |
| 任意文件读取 | `File.ReadAllBytes()`  ,`File.ReadAllText()`  ,`Response.WriteFile()`  ,`Response.TransmitFile()`  ,`File()` | 检查点：是否将用户参数直接作为文件路径输出或读取；是否存在未做路径合法化的文件下载接口。 |
| 路径遍历 | `Server.MapPath()`  ,`Path.Combine()`  ,`File.Delete()`  ,`Directory.GetFiles()` | 检查点：路径拼接是否包含未过滤的用户输入；`Path.Combine`  后是否做规范化校验。 |
| XXE（XML External Entity） | `XmlDocument.LoadXml()`  ,`XmlDocument.Load()`  ,`XmlReader.Create()`  ,`DataSet.ReadXml()` | 检查点：XML 解析是否启用了外部实体解析（DTD）；是否解析来自不受信任来源的 XML。 |
| SSRF | `WebClient.DownloadString()`  ,`HttpClient.GetAsync()`  ,`WebRequest.Create()`  ,`HttpClient.PostAsync()` | 检查点：是否允许用户指定 URL 并由服务器发起请求；是否对目标地址做白名单或内部地址检测。 |
| 远程文件下载 | `WebClient.DownloadFile()、HttpClient.GetStreamAsync()、HttpClient.GetByteArrayAsync()` | 检查点：是否允许用户提供远程文件 URL（例如通过参数、表单、配置等输入），是否存在任意文件写入风险（保存路径是否可控、是否拼接了用户输入 |

### 未授权访问

#### 检查默认路由暴露

* 默认路由`{controller}/{action}/{id}`会将所有 public action 暴露出来
* 查找未授权用户访问敏感控制器/方法，列出所有 Controller 和 public Action，与路由匹配，判断是否有不应暴露的接口

|  |
| --- |
| ``` var controllerTypes = typeof(MvcApplication).Assembly.GetTypes()     .Where(t => t.IsSubclassOf(...