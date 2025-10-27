---
title: Creating a NexThink installer for deployment via Jamf Pro
url: https://derflounder.wordpress.com/2022/12/03/creating-a-nexthink-installer-for-deployment-via-jamf-pro/
source: Der Flounder
date: 2022-12-04
fetch_date: 2025-10-04T00:28:35.006903
---

# Creating a NexThink installer for deployment via Jamf Pro

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Jamf Pro](https://derflounder.wordpress.com/category/jamf-pro/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/), [macOS](https://derflounder.wordpress.com/category/macos/), [Packaging](https://derflounder.wordpress.com/category/packaging/), [Scripting](https://derflounder.wordpress.com/category/scripting/) > Creating a NexThink installer for deployment via Jamf Pro

## Creating a NexThink installer for deployment via Jamf Pro

December 3, 2022
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

A while back, I had to build an installer for [NexThink Collector](https://docs.nexthink.com/platform/latest/overview-collector) which could be deployed via Jamf Pro. NexThink can be interesting to deploy because the installation process:

1. Involves an application named **csi.app**, which has a command line tool.
2. The referenced **csi** app’s command line tool configures and runs an installer package.
3. The command line tool also needs to reference a license file, which NexThink refers to as a CustomerKey file.

The CustomerKey file should look similar to what’s shown below:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | —–BEGIN CUSTOMER KEY—–MIIDhzCCAm+gAwIBAgIEIa+KoTANBgkqhkiG9w0BAQsFADBbMScwJQYDVQQDDB5SZWdlcnkgU2VsZi1TaWduZWQgQ2VydGlmaWNhdGUxIzAhBgNVBAoMGlJlZ2VyeSwgaHR0cHM6Ly9yZWdlcnkuY29tMQswCQYDVQQGEwJVQTAgFw0yMjEyMDIwMDAwMDBaGA8yMTIyMTIwMjIwMDIxMFowSTEVMBMGA1UEAwwMbG9jYWxob3N0LmlvMSMwIQYDVQQKDBpSZWdlcnksIGh0dHBzOi8vcmVnZXJ5LmNvbTELMAkGA1UEBhMCVUEwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDaKRW9KeX4wg/838FkxmzaBjqf1DeKD5GKEqhUKz0y78Wwnsv2zAXGM4UkdZJP9zHtC9/wFQT+lhclDlogxkU9lfMADV7nMdGL0GkJzwMQNS52dPNXDup7/d9yRkyjkV0Pf4t2fJF3igoNXFQuBvuArkNV6hfja2gOEczOSAaJ7L7qRnSahLjciJRaCuEPjwneh3krhOFT+djwuYJMIvBDEqs+gfp4OPDDBtVg2scUUGRmHsC+JAoK+JwqYwB9TNt+9hZtGfDqgZSHebXEfRTguhQpBj0mPTo76EahAbHbXJhV+efg3jt32pZ6qRl8ffrZAjefWEAnOMyXQ7fbL+bpAgMBAAGjYzBhMA8GA1UdEwEB/wQFMAMBAf8wDgYDVR0PAQH/BAQDAgGGMB0GA1UdDgQWBBRNHRZG3IKNH0kTRaiVfq6N8Ovp5zAfBgNVHSMEGDAWgBRNHRZG3IKNH0kTRaiVfq6N8Ovp5zANBgkqhkiG9w0BAQsFAAOCAQEAhpbntg+nwhIKgRuUidu/wXn197Ah0Pd4CYYxG5dR9rg8nWObx4QO6ApIH91nUUQVuV6mSTFtfy4yNQzxaROgZP9hDNvhd78D/ewXxp6bN/Xkn+c7SWrs/b1vHb2Dr1sDP4F9SAOrCI6TdoYa8UNhPXXSTt8M/hGSB2oWOpT2FAb2IbdmdYhDaibcJwp+/Had1FLbeDZgdgYCFoZLjws/9E/pIXjSxBYAJLbaQZffrfO5jCe2KesE73iQatW2IPynsFifRGGoMHXVLOfsLA9c2KDGqDmnJ+PvsBSe9rIpSJYC4WjR5Mt8W88kQSj05b9NqCsXmmMDEbD8uVLyKvQihA==—–END CUSTOMER KEY—– |

[view raw](https://gist.github.com/rtrouton/938fe413d797923971f75d517924940e/raw/03cbcf0b0cad50b04cb89f26903fa9292b9b808e/Company-Name-customer-key.txt)
 [Company-Name-customer-key.txt](https://gist.github.com/rtrouton/938fe413d797923971f75d517924940e#file-company-name-customer-key-txt)
hosted with ❤ by [GitHub](https://github.com)

All the needed components with the exception of the CustomerKey file, which is different for each customer, ship on a disk image.

![Screenshot 2022 12 02 at 3 31 46 PM](https://derflounder.wordpress.com/wp-content/uploads/2022/12/screenshot-2022-12-02-at-3.31.46-pm.png?w=595 "Screenshot 2022-12-02 at 3.31.46 PM.png")

[NexThink’s install documentation](https://docs.nexthink.com/platform/latest/installing-collector-on-macos) for the macOS version of the Collector software assumes that a human is doing one of the following:

**Graphical installation**: Mounting the disk image, double-clicking on the installer package and following the prompts, entering the correct configuration information were needed.

![Screenshot 2022 12 02 at 3 46 29 PM](https://derflounder.wordpress.com/wp-content/uploads/2022/12/screenshot-2022-12-02-at-3.46.29-pm.png?w=595 "Screenshot 2022-12-02 at 3.46.29 PM.png")

![Screenshot 2022 12 02 at 3 46 39 PM](https://derflounder.wordpress.com/wp-content/uploads/2022/12/screenshot-2022-12-02-at-3.46.39-pm.png?w=595 "Screenshot 2022-12-02 at 3.46.39 PM.png")

**Command line installation**: Mounting the disk image, opening the Terminal application and using the **csi** app’s command line tool to configure the installer package and run the installation process.

![Screenshot 2022 12 02 at 3 46 53 PM](https://derflounder.wordpress.com/wp-content/uploads/2022/12/screenshot-2022-12-02-at-3.46.53-pm.png?w=595 "Screenshot 2022-12-02 at 3.46.53 PM.png")

![Screenshot 2022 12 02 at 3 47 02 PM](https://derflounder.wordpress.com/wp-content/uploads/2022/12/screenshot-2022-12-02-at-3.47.02-pm.png?w=595 "Screenshot 2022-12-02 at 3.47.02 PM.png")

For the **Enterprise Deployment** section of the application, the NexThink documentation says they support it but doesn’t provide information on how to do it.

![Screenshot 2022 12 02 at 3 47 10 PM](https://derflounder.wordpress.com/wp-content/uploads/2022/12/screenshot-2022-12-02-at-3.47.10-pm.png?w=595 "Screenshot 2022-12-02 at 3.47.10 PM.png")

In my case, I decided to do the following to deploy it via Jamf Pro:

1. Wrap the disk image and CustomerKey file inside a separate installer package.
2. Use a postinstall script to perform the following actions:

A. Identify the location of the disk image stored inside the installer package.
B. Mount the disk image
C. Identify the location of the **csi.app** on the mounted disk image.
D. Identify the location of the CustomerKey file stored inside the installer package.
E. Use the **csi** app’s command line tool to configure and run the NexThink-provided installer package on the mounted disk image, to install the NexThink Collector software.
F. Unmount the disk image.

For more details, please see below the jump.

**Note:** *The details of installing and configuring NexThink are going to vary between shops, because different shops are going to configure different options for NexThink. Please consider what’s shown below as a general example, not something that will work for all environments.*

**Pre-requisites:**

* [Packages](http://s.sudre.free.fr/Software/Packages/about.html)
* Vendor-provided NexThink disk image with the NexThink Collector installer for macOS
* Vendor-provided CustomerKey text file

Before building the package, you’ll need to create a directory named **CustomerKeys** somewhere convenient.

![Screenshot 2022 12 02 at 4 09 34 PM](https://derflounder.wordpress.com/wp-content/uploads/2022/12/screenshot-2022-12-02-at-4.09.34-pm.png?w=595 "Screenshot 2022-12-02 at 4.09.34 PM.png")

Once the **CustomerKeys** directory has been created, add the CustomerKey file to it. The CustomerKey file is a plaintext file, where the filename must end in the **.txt** file extension. For this example, the CustomerKey file is named **Company-Name-customer-key.txt**.

![Screenshot 2022 12 02 at 4 09 23 PM](https://derflounder.wordpress.com/wp-content/uploads/2022/12/screenshot-2022-12-02-at-4.09.23-pm.png?w=595 "Screenshot 2022-12-02 at 4.09.23 PM.png")

**Building the NexThink Collector installer**

1. Set up a new Packages project and select **Raw Package**.

![Screenshot 2022 12 02 at 3 59 32 PM](https://derflounder.wordpress.com/wp-content/uploads/2022/12/screenshot-2022-12-02-at-3.59.32-pm.png?w=595 "Screenshot 2022-12-02 at 3.59.32 PM.png")

2. In this case, I’m naming the project **NexThink Collector Install 22.9.1.14**.

![Screenshot 2022 12 02 at 4 00 21 PM](https://derflounder.wordpress.com/wp-content/uploads/2022/12...