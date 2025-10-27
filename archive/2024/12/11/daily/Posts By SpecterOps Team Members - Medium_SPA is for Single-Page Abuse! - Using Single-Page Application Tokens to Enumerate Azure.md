---
title: SPA is for Single-Page Abuse! - Using Single-Page Application Tokens to Enumerate Azure
url: https://posts.specterops.io/spa-is-for-single-page-abuse-using-single-page-application-tokens-to-enumerate-azure-8c38dc77e409?source=rss----f05f8696e3cc---4
source: Posts By SpecterOps Team Members - Medium
date: 2024-12-11
fetch_date: 2025-10-06T19:42:28.835165
---

# SPA is for Single-Page Abuse! - Using Single-Page Application Tokens to Enumerate Azure

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F8c38dc77e409&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fspa-is-for-single-page-abuse-using-single-page-application-tokens-to-enumerate-azure-8c38dc77e409&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fspa-is-for-single-page-abuse-using-single-page-application-tokens-to-enumerate-azure-8c38dc77e409&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## Posts By SpecterOps Team Members](https://posts.specterops.io/?source=post_page---publication_nav-f05f8696e3cc-8c38dc77e409---------------------------------------)

·

Follow publication

[![Posts By SpecterOps Team Members](https://miro.medium.com/v2/resize:fill:76:76/1*D-FDlfkqivRBQZoESrwtqw.png)](https://posts.specterops.io/?source=post_page---post_publication_sidebar-f05f8696e3cc-8c38dc77e409---------------------------------------)

Posts from SpecterOps team members on various topics relating information security

Follow publication

# SPA is for Single-Page Abuse! - Using Single-Page Application Tokens to Enumerate Azure

[![Lance B. Cain](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*v0d00TR4cFqVeADo)](https://medium.com/%40lbcain18?source=post_page---byline--8c38dc77e409---------------------------------------)

[Lance B. Cain](https://medium.com/%40lbcain18?source=post_page---byline--8c38dc77e409---------------------------------------)

8 min read

·

Dec 10, 2024

--

1

Listen

Share

*Author:*

[*Lance B. Cain*](https://medium.com/u/040c3e09d079?source=post_page---user_mention--8c38dc77e409---------------------------------------)

## Overview

Microsoft Azure is a leading cloud provider offering technology solutions to companies, governments, and other organizations around the globe. As such, many entities have begun adopting Azure for their technology needs to include identity, authentication, storage, application management, and web services. One of the most common methods for organizations to begin experimenting with and adopting Azure is by deploying web applications and an increasingly popular method for creating web applications is by designing Single-Page Applications (SPAs). Katie Lawson of [bloomreach.com](https://www.bloomreach.com/en/blog/what-is-a-single-page-application) defines SPAs as, “a website or web application that dynamically rewrites a current web page with new data from the web server, instead of the default method of a web browser loading entire new pages”. SPAs typically utilize JavaScript integrations with API calls to dynamically update for a seamless user experience. Microsoft has multiple walkthroughs, guides, and documentation to aid organizations in deploying SPAs on Azure:

* Single-page application (SPA) documentation — <https://learn.microsoft.com/en-us/entra/identity-platform/index-spa>
* Single-page application: App registration — <https://learn.microsoft.com/en-us/entra/identity-platform/scenario-spa-app-registration>
* Configure authentication in a sample single-page application by using Azure AD B2C — <https://learn.microsoft.com/en-us/azure/active-directory-b2c/configure-authentication-sample-spa-app>

As a result, there are many new publicly hosted SPAs that communicate with Azure backend resources.

This blog post is intended to share insights learned from a prior security assessment about the attack surface of Single-Page Applications integrated with Azure, aid technology professionals in securing their Azure environments, and serve as a guide for enumerating Azure tenants using the additions of the pull request I submitted to Dirk-Jan’s [ROADTools](https://github.com/dirkjanm/ROADtools) repository. This blog is not a comprehensive analysis of every SPA hosted on Azure, so your mileage may vary. Due to the widespread adoption of Microsoft’s Office products and web integrations for Azure, I will focus on two popular SPAs that Microsoft offers (i.e., *WWW.OFFICE.COM* and *PORTAL.AZURE.COM*); however, the workflow translates to many other SPAs as well.

## A Brief Origin Story

My team and I were working on a collaborative cloud assessment for one of our clients targeting their Azure tenant. We were tasked with identifying methods of escalating privileges, assisting defenders in improving detections, and documenting attack paths in the client Azure environment using a compromised non-privileged user account on a Windows Virtual Desktop Image (VDI). We began by enumerating the available applications, Azure resources, Microsoft technologies, and client subscriptions. During the assessment, we learned that the client Azure environment was hardened with enforced multi-factor authentication (MFA), allow-listed MFA conditional access policies (CAPs), administrator restrictions on internal and external application enrollments, administrator approval for external invitations, [continuous access evaluation](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-continuous-access-evaluation), blocked access to Entra ID in the Azure portal, browser extension host security checks, blocked command-line interface (CLI) and PowerShell access, and time limitations on issued tokens forcing expiration after one hour.

The defensive configurations in the client environment impeded our work obtaining access and refresh tokens to enumerate the target tenant. The team began looking at the resources our user account had access to. We had successfully authenticated as the non-privileged user to the Azure portal and administrator pre-approved Microsoft Office web applications like Excel or Word on *HTTPS://WWW.MICROSOFT365.COM*. Within the Azure portal, we discovered that the user account had access to the Azure cloud shell which the team used to obtain an access token using the built-in PowerShell cmdlet [Get-AzAccessToken](https://learn.microsoft.com/en-us/powershell/module/az.accounts/get-azaccesstoken?view=azps-13.0.0) and initiate some cursory enumeration.

**Pro-Tip:** If the cloud shell is available, it is possible to install pip Python modules, including ROADTools, in the Bash shell.

Press enter or click to view image in full size

![]()

Figure 1 — Installing ROADTools in the Azure Cloud Shell

The team started collections to enumerate the client tenant using ROADTools and AzureHound with our initial access token; however, an hour later, we discovered that the tools had failed when the acquired token expired prior to completing their tasks. With the knowledge that the client tenant was so large that automated enumeration would exceed the one-hour lifetime for access tokens, we began looking into methods to update the access token for collections. After some research, we learned one of the likely intentional limitations of Get-AzAccessTokens for the Azure cloud shell that it would obtain access tokens, but it would not return a refresh token. My teammates started working on methods to script out obtaining a new access token in the cloud console, meanwhile I began looking at the access we had to authorized Microsoft w...