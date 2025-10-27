---
title: SIPVicious PRO incremental update - and Gitlab CI/CD examples
url: https://www.rtcsec.com/post/2023/03/sipvicious-pro-with-various-fixes-and-gitlab-ci/
source: Real-time communications security on Communication Breakdown - Real-Time Communications Security
date: 2023-03-08
fetch_date: 2025-10-04T08:54:23.023736
---

# SIPVicious PRO incremental update - and Gitlab CI/CD examples

[Skip to main content](#content)

[![Enable Security logo](https://www.enablesecurity.com/assets/img/logo-header-white.min.ac2c259ad95c9e369b3d7e44d9986a07c2c45fec663fbceaefe184e92011793a.svg)](/)

* [Get in touch](/contact/)

* Security Testing
  + [VoIP Penetration Testing](/voip-penetration-testing/)
  + [WebRTC Penetration Testing](/penetration-testing/)
  + [VoIP Security Assessment](/voip-security-assessment/)
  + [DDoS Resilience Testing](/ddos-testing/)
  + [Code & Config Analysis](/code-and-config-analysis/)
  + [Fuzz Testing](/fuzz-testing/)
* [SIPVicious](/sipvicious/)
* [Consultancy](/consultancy/)
* [Research](/research/)
* [Blog](/blog/)
* [Newsletter](/newsletter/)
* [About](/about/)
* [Contact](/contact/)

# SIPVicious PRO incremental update - and Gitlab CI/CD examples

Published on Mar 7, 2023
in
*[sip security](https://www.enablesecurity.com/tags/sip-security/)*,
*[sipvicious pro](https://www.enablesecurity.com/tags/sipvicious-pro/)*,
*[sip security testing](https://www.enablesecurity.com/tags/sip-security-testing/)*,
*[sipvicious releases](https://www.enablesecurity.com/tags/sipvicious-releases/)*,
*[devops](https://www.enablesecurity.com/tags/devops/)*,
*[security tools](https://www.enablesecurity.com/tags/security-tools/)*

We just pushed out a new SIPVicious PRO update to our subscribing members! This version does not include any new major features. Instead, it fixes various bugs and brings missing but necessary features to various SIPVicious PRO tools. We have the following highlights in this update:

* Documentation now includes realistic Gitlab CI/CD examples
* The RTP fuzzer in the experimental version now supports SRTP
* Support for new SIP DoS flood request methods
* The RTP inject tool can now specify the RTP’s SSRC and payload ID
* The SIP password cracking tool now supports closing the connection upon each attempt
* The SIP ping utility supports INVITE

For the boring details, including a list of bug fixes, do read the [release notes](https://docs.sipvicious.pro/stable/release-notes/) for v6.0.0-experimental.6 and v6.0.0-beta.6.

[Get in touch](https://www.enablesecurity.com/contact/) for further details.

## Gitlab CI/CD examples

SIPVicious PRO has supported CI/CD pipelines and been used in an automated fashion since v6.0.0-alpha.5, for almost 3 years. We have people using it in Jenkins, Gitlab and Github environments. Therefore we’re publishing practical examples of how SIPVicious PRO integrates with devops environments to detect vulnerabilities before they go into production - starting with our favourite, the Gitlab CI/CD.

[The automation documentation](https://docs.sipvicious.pro/stable/automation/gitlab-ci/) now includes practical examples showing SIPVicious PRO usage within a `.gitlab-ci.yml` and explaining how to build custom SIPVicious PRO Docker images.

Additionally, we published a [repository](https://gitlab.com/sipviciouspro/ci-cd-demos/demo-server-monitor) on the public Gitlab servers as a full example of a monitoring solution based on SIPVicious PRO. Check out the [pipelines and jobs](https://gitlab.com/sipviciouspro/ci-cd-demos/demo-server-monitor/-/pipelines) as they get executed regularly at 4am each morning to make sure that our Demo Server stays vulnerable. If you are a SIPVicious PRO subscriber, you will probably want the opposite - to make sure that your VoIP systems stay secure!

## RTP inject tool can specify the SSRC and payload ID

The RTP inject tool is meant to test if attackers can insert RTP audio into ongoing RTP streams. This update allows testers to specify the SSRC to test for cases where only a specific SSRC is being allowed to inject. More interestingly, testers can also specify the payload ID. During our engagements we noticed that if a specific codec is in use, in some cases, RTP injection will only work if the attacker makes use of the correct payload ID associated with that codec. Therefore this update makes the tool more effective in performing manual tests for this particular vulnerability.

These configuration options can be passed through the [`--inject-config` flag](https://docs.sipvicious.pro/stable/cui-reference/rtp/inject/#flag---inject-config).

## SRTP support for the RTP fuzzer

The RTP fuzzer included with the experimental build now [supports SRTP](https://docs.sipvicious.pro/experimental/cui-reference/rtp/fuzz/#flag---srtp) like many other SIPVicious PRO tools. This is particularly useful for testing media servers that enforce the use of SRTP and therefore could not be fuzz tested before this update.

## Closing the connection upon each password cracking attempt

During one of our penetration tests, we noticed that although password cracking attempts were being blocked after a few attempts, if we closed the connection, no blocking occurred. This update to the SIP password cracker allows security testers to automate this test and bypass certain naive security protection mechanisms.

This update adds the [`--close-conn` flag](https://docs.sipvicious.pro/stable/cui-reference/sip/crack/online/#flag---close-conn) to the `sip crack online` tool.

## SIP DoS flood additional request methods

Session Border Controllers (SBCs) and SIP routers are very flexible tools that can be configured to handle SIP methods in various ways. Such customizations can sometimes introduce inefficiencies that may then be abused in a DoS attack. This update is meant to expand our coverage of such scenarios.

The SIP DoS flood tool now supports the following [SIP request methods](https://docs.sipvicious.pro/stable/cui-reference/sip/dos/flood/#flag--m---method):

* REGISTER
* SUBSCRIBE
* NOTIFY
* PUBLISH
* MESSAGE
* INVITE
* OPTIONS
* ACK
* CANCEL
* BYE
* PRACK
* INFO
* REFER
* UPDATE

## SIP ping utility with INVITE

Finally, the SIP ping utility can now send an INVITE. Originally, we avoided adding this feature simply because of the nature of SIP INVITE - it starts a call. We changed our mind because we often need this functionality ourselves to monitor servers with INVITE - we simply use it without valid credentials or a destination SIP address that starts a call.

Use this new feature by making use of the [`--method INVITE` flag](https://docs.sipvicious.pro/stable/cui-reference/sip/utils/ping/#flag--m---method).

## How to get this update

SIPVicious PRO is available to our subscribing members - [get in touch to learn more](https://www.enablesecurity.com/sipvicious/#subscribe-to-sipvicious-pro).

###### Contents

* [Gitlab CI/CD examples](#gitlab-cicd-examples)
* [RTP inject tool can specify the SSRC and payload ID](#rtp-inject-tool-can-specify-the-ssrc-and-payload-id)
* [SRTP support for the RTP fuzzer](#srtp-support-for-the-rtp-fuzzer)
* [Closing the connection upon each password cracking attempt](#closing-the-connection-upon-each-password-cracking-attempt)
* [SIP DoS flood additional request methods](#sip-dos-flood-additional-request-methods)
* [SIP ping utility with INVITE](#sip-ping-utility-with-invite)
* [How to get this update](#how-to-get-this-update)

[![Enable Security GmbH logo](https://www.enablesecurity.com/assets/img/logo-white.min.ac2c259ad95c9e369b3d7e44d9986a07c2c45fec663fbceaefe184e92011793a.svg)](https://www.enablesecurity.com/)

* [Contact](/contact/)
* [Blog](/blog/)
* [Newsletter](/newsletter/)

* [SIPVicious](/sipvicious/)
* [Consultancy](/consultancy/)
* [VoIP Pentesting](/voip-penetration-testing/)

* [WebRTC Pentesting](/penetration-testing/)
* [VoIP Sec Assess](/voip-security-assessment/)
* [Code Analysis](/code-and-config-analysis/)

* [DDoS Testing](/ddos-testing/)
* [Fuzz Testing](/fuzz-testing/)
* [About](/about/)

© Enable Security GmbH · 2025

* [Privacy policy](/privacy/)
* [Impressum](/impressum/)

`User-Agent: friendly-scanner`

**Cookie settings**

We use cookies to personalize content and analyze access to our website. For more information, please refer to our [privacy policy](/privacy/).

Got it
No thanks