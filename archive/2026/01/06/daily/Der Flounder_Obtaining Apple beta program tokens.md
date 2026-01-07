---
title: Obtaining Apple beta program tokens
url: https://derflounder.wordpress.com/2026/01/06/obtaining-apple-beta-program-tokens/
source: Der Flounder
date: 2026-01-06
fetch_date: 2026-01-07T03:26:34.305107
---

# Obtaining Apple beta program tokens

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Apple Beta Programs](https://derflounder.wordpress.com/category/apple-beta-programs/), [Apple Business Manager](https://derflounder.wordpress.com/category/apple-business-manager/), [Mac administration](https://derflounder.wordpress.com/category/mac-administration/) > Obtaining Apple beta program tokens

## Obtaining Apple beta program tokens

January 6, 2026
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

As [discussed in an earlier post](https://derflounder.wordpress.com/2026/01/04/signing-up-for-appleseed-for-it-using-apple-business-manager/), you can sign up for Apple’s [AppleSeed for IT program](https://beta.apple.com/for-it) using a user with the [Administrator role](https://support.apple.com/guide/apple-business-manager/intro-to-roles-and-privileges-axm97dd59159/web) in [Apple Business Manager](https://support.apple.com/guide/apple-business-manager/welcome/web) or [Apple School Manager](https://support.apple.com/guide/apple-school-manager/welcome/web) and subsequently obtain tokens which allow devices to be enrolled in Apple’s beta programs without the need for the user to sign in with an Apple Account on the device.

Apple has [documentation available on how to obtain these tokens](https://support.apple.com/guide/deployment/test-software-updates-appleseed-beta-program-depe8583cf10/web) using an API call to the following endpoint:

<https://mdmenrollment.apple.com/os-beta-enrollment/tokens>

However, the documentation does not include the specifics on how to set up the API call or the necessary OAuth authentication for it. Fortunately, the folks at [HCS Technology Group](https://hcsonline.com) have published a [technical article](https://hcsonline.com/support/resources/white-papers/deploy-apple-software-beta-updates-with-jamf-pro-blueprints-without-an-apple-account) showing how to obtain the necessary tokens using the following:

* An ADE token from your organization’s [Apple Business Manager](https://support.apple.com/guide/apple-business-manager/welcome/web) or [Apple School Manager](https://support.apple.com/guide/apple-school-manager/welcome/web) instance.
* The [getBetaTokens script](https://github.com/microsoft/shell-intune-samples/tree/master/macOS/Tools/getBetaTokens) written by the folks from [Microsoft](https://www.microsoft.com).

For more details, please see below the jump.

I’m going to be using the process described in the HCS technical article to do the following:

1. Set up a new Device Management Services server in Apple Business Manager.
2. Use the **getBetaTokens** script to do the following:

* Generate a public key for the new Device Management Services server.
* Use the ADE token from the new Device Management Services server as a source for the necessary OAuth credentials for the API call to the <https://mdmenrollment.apple.com/os-beta-enrollment/tokens> endpoint
* Authenticate to the API endpoint and fetch all available Apple beta tokens associated with an organization’s AppleSeed for IT program.
* Display all available beta tokens

**Pre-requisites**:

* An [Apple Business Manager](https://support.apple.com/guide/apple-business-manager/welcome/web) instance.
* Enrollment in the [AppleSeed for IT program](https://beta.apple.com/for-it) by a user with the [Administrator role](https://support.apple.com/guide/apple-business-manager/intro-to-roles-and-privileges-axm97dd59159/web) for that Apple Business Manager instance.
* A managed Apple Account with [the Administrator or Device Manager role](https://support.apple.com/guide/apple-business-manager/intro-to-roles-and-privileges-axm97dd59159/web) for that Apple Business Manager instance.
* The [getBetaTokens script](https://github.com/microsoft/shell-intune-samples/tree/master/macOS/Tools/getBetaTokens).

1. Log into Apple Business Manager using a managed Apple Account with [the Administrator or Device Manager role](https://support.apple.com/guide/apple-business-manager/intro-to-roles-and-privileges-axm97dd59159/web). In the case of my example, I am using an account with the **Administrator** role.
2. At the bottom left corner of the browser, click on the menu and select **Preferences**.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/01/screenshot-2026-01-04-at-12.33-2.png?w=600&h=398 "Screenshot 2026-01-04 at 12.33.png")

3. Click the **Add** button for the **Device Management Services** section.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/01/screenshot-2026-01-06-at-9.07.png?w=599&h=434 "Screenshot 2026-01-06 at 9.07.png")

4. Name the new Device Management Services server. For this example, I’m choosing to name it as **Apple Beta Tokens**.

**Note:** You will not be able to save changes to the new Device Management Services server until a public key is uploaded.

![](https://derflounder.wordpress.com/wp-content/uploads/2026/01/screenshot-2026-01-06-at-9.09.png?w=599&h=434 "Screenshot 2026-01-06 at 9.09.png")

5. Launch the **getBetaTokens** script. You should see output similar to this:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | [INFO] No .p7m found in ./abm\_auth. |
|  | [ACTION] A certificate will be generated – upload the PEM to ABM, then |
|  | download the issued \*.p7m token (it usually lands in ~/Downloads). |
|  | [INFO] No .p7m found: generating key + self-signed cert… |
|  | Generating RSA private key, 2048 bit long modulus |
|  | .+++++ |
|  | …………………………………………+++++ |
|  | e is 65537 (0x10001) |
|  | Signature ok |
|  | subject=/CN=Your MDM Server |
|  | Getting Private key |
|  |  |
|  | [ACTION] Upload this PEM to Apple Business Manager (Settings → MDM Servers) |
|  |  |
|  | ──────────────────────────────────────────────────────────────── |
|  | —–BEGIN CERTIFICATE—– |
|  | MIICsDCCAZgCCQD5GClF1eAa6DANBgkqhkiG9w0BAQsFADAaMRgwFgYDVQQDDA9Z |
|  | b3VyIE1ETSBTZXJ2ZXIwHhcNMjYwMTA2MTQxMzI5WhcNMjcwMTA2MTQxMzI5WjAa |
|  | MRgwFgYDVQQDDA9Zb3VyIE1ETSBTZXJ2ZXIwggEiMA0GCSqGSIb3DQEBAQUAA4IB |
|  | DwAwggEKAoIBAQDPVjJynmJ3QJNTwrMACJ467WB1zvASfJWKIXFzKKIhdXZBgAXi |
|  | FqlLgXUi3J0sai9mrfbVI0yfnlOpaGws/t3lZ/4riKyfTj8IxSHSebwdDzHQR/8Q |
|  | 5+B884wXdxs9FuWodvQ0EdGHMKkm5HaEc//m261JvadoT0LhScq1DT3Izv8Gd8k1 |
|  | v5HjshNxZLSkqj4La7phb++bGem+nDXtItyykY7D5310xYl7XT6bGgM/s7QbvObj |
|  | BuIKTkKLwtmlfU+Di4acqJ89VjuX6gnUxmn4YmNTCCWiT5v6GxvSbtzHQsLSD6Qk |
|  | mac43pbeG/NFwSjR+YoyYLkdFuB0BUDcC0glAgMBAAEwDQYJKoZIhvcNAQELBQAD |
|  | ggEBAIMUxul28kUTmFN8NT6bbjXPweORwtqiqEi3Y36ti2ING6Q2g+F29O7w5hrj |
|  | bweGIHvON8V+oEzKWCQIDboCCD5iPa/EEaFhsy9/v/4jvPlrtW6c9eU8QOzCupSY |
|  | Gyxfhg70M4cQCOl2G1eXsbzroLtJKmFMkpy8rCdMrFgaHW2/Xvw/cLDgQryDBSu3 |
|  | Z7RAGRB+0QtG/qpMG/8oFhc32ZqdqPa+8L1HvxILYqf7zDRXrfyA1peI5dsmiPB2 |
|  | X+2BWL5iAO/vl86XD8NO+ZKO82AzZXRVbTNRb0lSrweWMlbrC3u/plL2hiPDp6bj |
|  | wBLo/hybOuVUGFmbPvTbjHMZdis= |
|  | —–END CERTIFICATE—– |
|  | ──────────────────────────────────────────────────────────────── |
|  |  |
|  | After ABM issues you a \*.p7m server token, drop it into this directory. |
|  |  |
|  | [INFO] Watching /Users/username/Downloads for NEW \*.p7m files (every 5s)… |

[view raw](https://gist.github.com/rtrouton/c441487df977ac8901db973540be5d28/raw/c6575a509008b1d9b6f8f8acf859bef46ec576ba/gistfile1.txt)
 [gistfile1.txt](https://gist.github.com/rtrouton/c441487df977ac8901db973540be5d28#file-g...