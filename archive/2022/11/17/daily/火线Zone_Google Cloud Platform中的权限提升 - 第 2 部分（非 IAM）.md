---
title: Google Cloud Platform中的权限提升 - 第 2 部分（非 IAM）
url: https://mp.weixin.qq.com/s?__biz=MzI2NDQ5NTQzOQ==&mid=2247497322&idx=1&sn=2c5c319b68fcdd06aa3fd49bdc61f0f3&chksm=eaa97e4adddef75c0d5a913d552ff4db0c588eb0b83680576c952aebffa48814b72a4b4adf0f&scene=58&subscene=0#rd
source: 火线Zone
date: 2022-11-17
fetch_date: 2025-10-03T23:01:24.699256
---

# Google Cloud Platform中的权限提升 - 第 2 部分（非 IAM）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/0Z0LqMyVGaReHnticDnv8bO8Rsc1qox2fyrAF2JS5zEMXQxh60Je03ic2bL4iaBppqyymmUZMCIgXHfAU49tFu3mg/0?wx_fmt=jpeg)

# Google Cloud Platform中的权限提升 - 第 2 部分（非 IAM）

养了个羊

火线Zone

***第一部分已在火线Zone发布，请参考https://zone.huoxian.cn/d/1289-google-cloud-platform-1-iam***

***这一部分重点介绍非 IAM 服务提权方法。例如，这些权限都不属于“IAM”系列，就像第 1 部分中的大多数方法一样，例如iam.serviceAccounts.update。***

**非IAM方法**

orgpolicy.policy.set

此方法不一定会授予您更多 IAM 权限，但它可能会禁用一些阻止某些操作的障碍。例如，有一个名为*appengine.disableCodeDownload*的组织策略约束，它可以防止项目用户下载 App Engine 源代码。如果启用此功能，您将无法下载该源代码，但您可以使用*orgpolicy.policy.set*禁用约束，然后继续下载源代码。

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaReHnticDnv8bO8Rsc1qox2f1ehhwibDT5IUetQw7wgNNQ5YJaicgt92wicZtiaek1nibJ2Ets4icAFPpicqw/640?wx_fmt=png)

上面的截图显示*appengine.disableCodeDownload*约束被强制执行，这意味着它阻止我们下载源代码。使用*orgpolicy.policy.set*，我们可以禁用该强制执行，然后继续下载源代码。

可以在此处（https://github.com/RhinoSecurityLabs/GCP-IAM-Privilege-Escalation/blob/master/ExploitScripts/orgpolicy.policy.set.py）找到此方法的漏洞利用脚本。

**storage.hmacKeys.create**

Cloud Storage 有一个特性，即“互操作性”，它为 Cloud Storage 提供了一种与来自其他云提供商（如 AWS S3）的存储产品进行交互的方式。作为其中的一部分，可以为服务帐户和普通用户创建 HMAC 密钥。我们可以通过为更高权限的服务帐户创建 HMAC 密钥来升级 Cloud Storage 权限。

属于您的用户的 HMAC 密钥不能通过 API 访问，必须通过 Web 控制台访问，但好的是访问密钥和密钥在任何时候都可用。这意味着我们可以获取现有的一对并将它们存储起来，以便备份访问帐户。属于服务帐户的 HMAC 密钥**可以**通过 API 访问，但创建后，您将无法再次看到访问密钥。

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaReHnticDnv8bO8Rsc1qox2ficG9g8jnKRNV0RZsCLg0b7BPZZumFqzHq9WWsobllQyd5e4F6uMhLTA/640?wx_fmt=png)

上面的屏幕截图显示了来自 gsutil CLI 的简单命令，用于为服务帐户创建 HMAC 密钥。现在您只需使用这些密钥作为服务帐户访问 Cloud Storage API。

可以在此处（https://github.com/RhinoSecurityLabs/GCP-IAM-Privilege-Escalation/blob/master/ExploitScripts/storage.hmacKeys.create.py）找到此方法的漏洞利用脚本。

**serviceusage.apiKeys.create**

还有另一种使用 GCP API 进行身份验证的方法，称为 API 密钥。默认情况下，它们的创建没有任何限制，这意味着它们可以访问创建它们的整个 GCP 项目。我们可以通过创建一个可能比我们自己的用户拥有更多权限的新 API 密钥来利用这一事实。对此没有官方 API，因此需要将自定义 HTTP 请求发送到*https://apikeys.clients6.google.com/*  （或*https://apikeys.googleapis.com/*）。这是通过在浏览 GCP Web 控制台时监控 HTTP 请求和响应而发现的。有关与 API 密钥相关的限制的文档，请访问此链接。

以下屏幕截图显示了如何在 Web 控制台中创建 API 密钥。

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaReHnticDnv8bO8Rsc1qox2fjLWgYmibbfph5ibI3cveibuiagy74lFDBdtkkkfxXia41q3fvCvmDmOosng/640?wx_fmt=png)

通过发现未记录的 API，我们还可以通过 API 本身创建 API 密钥。

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaReHnticDnv8bO8Rsc1qox2fSBMrAZAL6ia3PqiaMzjUkMicmbKgL41kUduKeLsTu8r3eWfpILmY5R9oA/640?wx_fmt=png)

上面的屏幕截图显示了发送 POST 请求以检索项目的新 API 密钥。

可以在此处（https://github.com/RhinoSecurityLabs/GCP-IAM-Privilege-Escalation/blob/master/ExploitScripts/serviceusage.apiKeys.create.py）找到此方法的漏洞利用脚本。

**serviceusage.apiKeys.list**

发现另一个未记录的 API 用于列出已经创建的 API 密钥（这也可以在 Web 控制台中完成）。因为创建后仍然可以看到 API 密钥的值，所以我们可以拉取项目中的所有 API 密钥。

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaReHnticDnv8bO8Rsc1qox2fV661icxicaIQ3TaCuLibUj9e4zmWsBFHQEeicAicMZmWegZfEHWA2RYzZ6Q/640?wx_fmt=png)

上面的截图显示请求和之前完全一样，只是一个 GET 请求而不是一个 POST 请求。这仅显示一个键，但如果项目中有其他键，也会列出这些键。

可以在此处（https://github.com/RhinoSecurityLabs/GCP-IAM-Privilege-Escalation/blob/master/ExploitScripts/serviceusage.apiKeys.list.py）找到此方法的漏洞利用脚本。

**其它setlamPolicy API调用**

除了上述所有方法之外，还可以通过更新与目标资源关联的 IAM 策略来执行简单的权限提升。下面的权限升级扫描器也会检查这些。

有关使用 setIamPolicy 时特定资源上的权限提升的示例，请阅读我们过去关于 Google 存储桶枚举和提升的博客文章：https://rhinosecuritylabs.com/gcp/google-cloud-platform-gcp-bucket-enumeration/

这里列出了一些值得研究的权限升级：

* resourcemanager.organizations.setIamPolicy

+ 在组织级别将 IAM 角色附加到您的用户。

* resourcemanager.folders.setIamPolicy

+ 在文件夹级别将 IAM 角色附加到您的用户。

* resourcemanager.projects.setIamPolicy

+ 在项目级别将 IAM 角色附加到您的用户。

* iam.serviceAccounts.setIamPolicy

+ 在服务帐户级别将 IAM 角色附加到您的用户。

* cloudfunctions.functions.setIamPolicy

+ 修改 Cloud Functions 的策略以允许您自己调用它。

以下权限是您可以更新的所有不同 IAM 策略：

```
accesscontextmanager.accessPolicies.setIamPolicyaccesscontextmanager.policies.setIamPolicyapigee.environments.setIamPolicyartifactregistry.repositories.setIamPolicyautoml.datasets.setIamPolicyautoml.locations.setIamPolicyautoml.models.setIamPolicybigquery.connections.setIamPolicybigquery.datasets.setIamPolicybigtable.instances.setIamPolicybigtable.tables.setIamPolicybilling.accounts.setIamPolicybinaryauthorization.attestors.setIamPolicybinaryauthorization.policy.setIamPolicycloudfunctions.functions.setIamPolicycloudiot.registries.setIamPolicycloudkms.cryptoKeys.setIamPolicycloudkms.importJobs.setIamPolicycloudkms.keyRings.setIamPolicycloudprivatecatalogproducer.catalogs.setIamPolicycloudsupport.accounts.setIamPolicycloudtasks.queues.setIamPolicycompute.disks.setIamPolicycompute.globalOperations.setIamPolicycompute.images.setIamPolicycompute.instanceTemplates.setIamPolicycompute.instances.setIamPolicycompute.licenseCodes.setIamPolicycompute.licenses.setIamPolicycompute.maintenancePolicies.setIamPolicycompute.networkEndpointGroups.setIamPolicycompute.nodeGroups.setIamPolicycompute.nodeTemplates.setIamPolicycompute.regionOperations.setIamPolicycompute.securityPolicies.setIamPolicycompute.snapshots.setIamPolicycompute.subnetworks.setIamPolicycompute.zoneOperations.setIamPolicydatacatalog.categories.setIamPolicydatacatalog.entries.setIamPolicydatacatalog.entryGroups.setIamPolicydatacatalog.tagTemplates.setIamPolicydatacatalog.taxonomies.setIamPolicydatafusion.instances.setIamPolicydataproc.autoscalingPolicies.setIamPolicydataproc.clusters.setIamPolicydataproc.jobs.setIamPolicydataproc.operations.setIamPolicydataproc.workflowTemplates.setIamPolicydatastore.databases.setIamPolicydatastore.namespaces.setIamPolicydns.policies.setIamPolicygenomics.datasets.setIamPolicygkehub.memberships.setIamPolicyhealthcare.datasets.setIamPolicyhealthcare.dicomStores.setIamPolicyhealthcare.fhirStores.setIamPolicyhealthcare.hl7V2Stores.setIamPolicyiam.serviceAccounts.setIamPolicyiap.tunnel.setIamPolicyiap.tunnelInstances.setIamPolicyiap.tunnelZones.setIamPolicyiap.web.setIamPolicyiap.webServiceVersions.setIamPolicyiap.webServices.setIamPolicyiap.webTypes.setIamPolicymanagedidentities.domains.setIamPolicyml.jobs.setIamPolicyml.models.setIamPolicyml.studies.setIamPolicynetworkmanagement.connectivitytests.setIamPolicynotebooks.environments.setIamPolicynotebooks.instances.setIamPolicyproximitybeacon.beacons.setIamPolicyproximitybeacon.namespaces.setIamPolicypubsub.snapshots.setIamPolicypubsub.subscriptions.setIamPolicypubsub.topics.setIamPolicyresourcemanager.folders.setIamPolicyresourcemanager.organizations.setIamPolicyresourcemanager.projects.setIamPolicyrun.services.setIamPolicyruntimeconfig.configs.setIamPolicyruntimeconfig.variables.setIamPolicyruntimeconfig.waiters.setIamPolicysecretmanager.secrets.setIamPolicysecuritycenter.sources.setIamPolicyservicebroker.bindings.setIamPolicyservicebroker.catalogs.setIamPolicyservicebroker.instances.setIamPolicyservicedirectory.endpoints.setIamPolicyservicedirectory.namespaces.setIamPolicyservicedirectory.services.setIamPolicyservicemanagement.consumerSettings.setIamPolicyservicemanagement.services.setIamPolicysource.repos.setIamPolicyspanner.backups.setIamPolicyspanner.databases.setIamPolicyspanner.instances.setIamPolicystorage.buckets.setIamPolicystorage.objects.setIamPolicydeploymentmanager.deployments.setIamPolicy
```

如果您拥有上述任何权限，则可以修改指定资源的 IAM 策略以授予自己在该资源上的角色，从而在资源级别授予您额外的权限。

**GCP提权扫描程序**

单独的漏洞利用脚本很好，但更有用的是检查您自己的 GCP 环境以获取现有权限提升路径的方法。我们为此编写了一个脚本。它枚举成员及其对组织、文件夹、项目和服务帐户的权限，并报告任何权限提升方法和/或 setIamPolicy 权限。请注意，该脚本甚至会枚举继承的权限！例如，这意味着您在组织级别授予的所有权限也将显示在您的项目级别权限下，因为权限是向下继承的。

可以在Rhino Github（https://github.com/RhinoSecurityLabs/GCP-IAM-Privilege-Escalation/tree/master/PrivEscScanner）上找到扫描器。

本质上，您只需运行*enumerate\_member\_permissions.py*脚本来枚举成员及其权限，然后运行*check\_for\_privesc.py*脚本来检查这些权限以进行特权升级。请注意，项目所有者和编辑者可能会由于权限过大而返回大量结果。

这是脚本运行并显示其输出的屏幕截图。枚举脚本接受访问令牌并将枚举目标项目中的所有内容，而权限升级脚本离线解析枚举的权限以查找权限升级。屏幕截图显示了一些用户/组容易受到我们测试项目中某些权限提升方法的攻击。

![](https://mmbiz.qpic.cn/mmbiz_png/0Z0LqMyVGaReHnticDnv8bO8Rsc1qox2fmrOINz5zJn3tgCjVP3eVdiaDCRKiaMt1PqTBMiaML65A6LU6TaEv6AibEQ/640?wx_fmt=png)

之后，将有三个文件包含您的结果：

1. *all\_org\_folder\_proj\_sa\_permissions.json* – 所有成员及其相关权限
2. *privesc\_methods.txt* – 所有检测到的提权方法
3. *setIamPolicy\_methods.txt* –...