---
title: Passwordless Persistence and Privilege Escalation in Azure
url: https://posts.specterops.io/passwordless-persistence-and-privilege-escalation-in-azure-98a01310be3f?source=rss----f05f8696e3cc---4
source: Posts By SpecterOps Team Members - Medium
date: 2022-12-22
fetch_date: 2025-10-04T02:14:52.088421
---

# Passwordless Persistence and Privilege Escalation in Azure

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F98a01310be3f&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fpasswordless-persistence-and-privilege-escalation-in-azure-98a01310be3f&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fpasswordless-persistence-and-privilege-escalation-in-azure-98a01310be3f&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## Posts By SpecterOps Team Members](https://posts.specterops.io/?source=post_page---publication_nav-f05f8696e3cc-98a01310be3f---------------------------------------)

·

Follow publication

[![Posts By SpecterOps Team Members](https://miro.medium.com/v2/resize:fill:76:76/1*D-FDlfkqivRBQZoESrwtqw.png)](https://posts.specterops.io/?source=post_page---post_publication_sidebar-f05f8696e3cc-98a01310be3f---------------------------------------)

Posts from SpecterOps team members on various topics relating information security

Follow publication

# Passwordless Persistence and Privilege Escalation in Azure

[![Andy Robbins](https://miro.medium.com/v2/resize:fill:64:64/2*G-LlqSNRGI8wIrjrYRzWdA.png)](https://medium.com/%40_wald0?source=post_page---byline--98a01310be3f---------------------------------------)

[Andy Robbins](https://medium.com/%40_wald0?source=post_page---byline--98a01310be3f---------------------------------------)

13 min read

·

Dec 21, 2022

--

Listen

Share

Adversaries are always looking for stealthy means of maintaining long-term and stealthy persistence and privilege in a target environment. Certificate-Based Authentication (CBA) is an extremely attractive persistence option in Azure for three big reasons:

1. With control of a root CA trusted by AzureAD, the adversary can impersonate any user without knowing their password — including Global Admins.
2. Configuring CBA and impersonating a Global Admin doesn’t require Global Admin rights. This built-in privilege escalation makes for a very stealthy way to hide privileges.
3. While many logs can alert to the fact CBA has been configured, there does not seem to be any way whatsoever to differentiate between logins performed with a password versus those performed with a certificate.

I reported the privilege escalation primitive to MSRC, this is the disclosure timeline:

* November 3, 2022: Reported issue to MSRC
* November 4, 2022: Report acknowledged and case opened by MSRC
* November 28, 2022: Case assigned “Low” severity and closed by MSRC

## Prior Work

[Marius Solbakken](https://twitter.com/mariussmellum) covered CBA in his excellent blog post [here](https://goodworkaround.com/2022/02/15/digging-into-azure-ad-certificate-based-authentication/). Marius outlines the instructions for configuring your own Certificate Authority, configuring Azure to trust that authority, and abusing the Subject Alternative Name extension in the X.509 specification to authenticate as other users. I’ll be repeating many of the points Marius made in his blog post in the following sections.

## How Certificate Based Authentication Works

The promise of CBA is that your users can log into Azure and other services without using a password. But how does that actually work?

Upon creation, an Azure Active Directory tenant establishes what is known as a “trust boundary” around itself and every object that resides within the tenant. For example, if we create a tenant and one user, the trust boundary surrounds both objects:

Press enter or click to view image in full size

![]()

With no further changes, this boundary will remain in-tact, meaning the user can only ever be authenticated by the tenant it resides in. This also means that only other objects within the tenant can perform operations against the tenant itself or the user.

In order to use CBA, we must create a Certificate Authority (CA), enable CBA in Azure, then upload the CA’s cert to the AzureAD tenant. When we do this, we effectively pierce the trust boundary, having now created a federated identity trust with an external entity (the CA):

Press enter or click to view image in full size

![]()

The AzureAD tenant itself will always be the primary and ultimate identity authority for the user. But as CBA can be configured to allow some or all users to authenticate with certificates, this external CA has become an alternative identity authority for the user:

Press enter or click to view image in full size

![]()

This is the foundation of passwordless authentication with CBA. The AzureAD tenant trusts the CA to authenticate the user. When we present an X509 certificate signed by this CA to the Azure Security Token Service (STS), the STS will validate the certificate against the tenant’s list of trusted certificates, then emit a signed JSON Web Token which includes the properties of the user entity and can be used to authenticate to other services as the user:

Press enter or click to view image in full size

![]()

The user’s password is never required, submitted, or verified — hence “passwordless” authentication.

## Passwordless Persistence with CBA

Here are the tactical actions an adversary must take in order to install and abuse CBA for persistence.

Enabling CBA is the first step an adversary must take. We can do this in the Azure portal GUI by navigating to Azure Active Directory -> Security -> Authentication Methods -> Certificate-based authentication, clicking “Enable”, selecting users to include for CBA, then clicking “Save”:

Press enter or click to view image in full size

![]()

We can also do this step with a PATCH request directly to the MS Graph API at this endpoint:

<https://graph.microsoft.com/beta/policies/authenticationmethodspolicy/authenticationMethodConfigurations/X509Certificate>

Next we need to create a Certificate Authority. [Download OpenSSL version 3.0.5](https://www.openssl.org/source/old/3.0/). Create a new directory where you will store the CA configuration files, certs, and folders. Create the necessary files and folders in this directory:

```
cd c:\
mkdir CA
cd CA
mkdir ca
mkdir ca/ca.db.certs
New-Item -Name ca.db.index -ItemType File
Set-Content -Path "ca.db.serial" -Value "1234"
```

Now create two configuration files: ca.conf and san.conf. Fill their contents, replacing “arobbins@specterdev.onmicrosoft.com” with the UPN of the Azure user you want to log in as:

```
cd ..
Set-Content -Path ca.conf -Value '[ ca ]
default_ca = ca_default
[ ca_default ]
dir = ./ca
certs = $dir
new_certs_dir = $dir/ca.db.certs
database = $dir/ca.db.index
serial = $dir/ca.db.serial
RANDFILE = $dir/ca.db.rand
certificate = $dir/ca.crt
private_key = $dir/ca.key
default_days = 365
default_crl_days = 30
default_md = md5
preserve = no
policy = generic_policy
[ generic_policy ]
countryName = optional
stateOrProvinceName = optional
localityName = optional
organizationName = optional
organizationalUnitName = optional
commonName = optional
emailAddress = optional
[req]
x509_extensions = usr_cert
req_extensions = v3_req
[ usr_cert ]
subjectAltName = @alt_names
[ v3_req ]
subjectAltName = @alt_names
[alt_names]
otherName=1.3.6.1.4...