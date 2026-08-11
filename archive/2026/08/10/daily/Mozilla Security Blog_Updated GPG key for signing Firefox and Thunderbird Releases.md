---
title: Updated GPG key for signing Firefox and Thunderbird Releases
url: https://blog.mozilla.org/security/2026/08/10/updated-gpg-key-for-signing-firefox-and-thunderbird-releases/
source: Mozilla Security Blog
date: 2026-08-10
fetch_date: 2026-08-11T03:30:24.550375
---

# Updated GPG key for signing Firefox and Thunderbird Releases

[Mozilla](https://www.mozilla.org/?utm_source=blog.mozilla.org&utm_medium=referral&utm_campaign=blog-nav "Visit mozilla.org")

Menu

* [About Mozilla](https://www.mozilla.org/about/?utm_source=blog.mozilla.org&utm_medium=referral&utm_campaign=blog-nav)
* [Products](https://www.mozilla.org/firefox/products/?utm_source=blog.mozilla.org&utm_medium=referral&utm_campaign=blog-nav)
* [Give](https://donate.mozilla.org/?presets=50,30,20,10&amount=30&currency=usd&utm_source=blog.mozilla.org&utm_medium=referral&utm_campaign=blog-nav)
* [Discover Firefox](https://www.mozilla.org/firefox/?utm_source=blog.mozilla.org&utm_medium=referral&utm_campaign=blog-nav)

[#### Mozilla Security Blog](https://blog.mozilla.org/security/ "Go to the front page")

* Search this site

  Search

**Categories:**
[Security](https://blog.mozilla.org/security/category/security/)

# Updated GPG key for signing Firefox and Thunderbird Releases

Ben Hearsum
August 10, 2026

Today, we moved to a new GPG signing subkey used to sign certain Firefox and Thunderbird artifacts (namely Linux tarballs, RPM packages, checksums files) after an unencrypted copy of the previous subkey was inadvertently committed to a private GitHub repository.

Our review of available audit records found no evidence that the key was accessed by an unauthorized party while it was present in the repository. Access to the repository was limited to a small group within Mozilla, all of whom already had authorized access to the key through other means.

We have revoked the previous signing key and added safeguards to prevent similar issues in the future.

**For most users, no action is required.**

There are two cases where you may need to take action:

* If you manually verify our GPG signatures, you will need to import the new signing key and the revocation for the old key.
* If you use Firefox RPM packages, some manual intervention may be required. See the instructions below for details.

Thunderbird does not provide official RPM packages, so there is no RPM-specific action required.

### RPM Users

Different RPM package management tools deal with GPG key rotations and revocations differently. See the sections below for what action (if any) you need to take to ensure you continue to receive the latest Firefox updates.

#### Fedora 43 and later

No special action needed. During the next update, dnf will download the updated key and you just need to confirm the import. Make sure the shown fingerprint matches `827E 6586 0867 9618 CD34 9F93 678E 455D 7676 7AA3` before accepting.

#### Fedora 42 and older, RHEL/Rocky/Almalinux

Dnf on these releases cannot replace the key on its own. Updates will fail with “Import of the key didn’t help, wrong key?” or “The GPG keys listed for the mozilla repository are already installed but they are not correct for this package”. The old keys must be removed manually:

`sudo rpm -e --allmatches gpg-pubkey-14f26682d0916cdd81e37b6d61b7b526d98f0353`
`sudo rpm --import https://packages.mozilla.org/rpm/firefox/signing-key.gpg`
`sudo dnf clean all`

Important: Remove the previous signing key before importing the new one. If you run `rpm --import` while the previous key is still installed, the command may report success even though the key is not updated.

#### openSUSE/SUSE based distributions

Same as the previous section, zypper won’t replace the key on its own and it must be removed manually. Updates will fail with “Signature verification failed” or “NOKEY”. Use the following commands:

`sudo rpm -e --allmatches gpg-pubkey-14f26682d0916cdd81e37b6d61b7b526d98f0353`
`sudo rpm --import https://packages.mozilla.org/rpm/firefox/signing-key.gpg`
`sudo zypper refresh`

### New GPG Key Details

The GPG fingerprint is `14F2 6682 D091 6CDD 81E3 7B6D 61B7 B526 D98F 0353`. The new signing subkey’s fingerprint is `827E 6586 0867 9618 CD34 9F93 678E 455D 7676 7AA3`, and it expires 2028-08-05.

The new public key and revocation of the previous one can be fetched from:

* KEY files of the latest Firefox Nightly (https://archive.mozilla.org/pub/firefox/nightly/latest-mozilla-central/)
* keys.openpgp.org, or
* inline below

This can be used to validate releases signed with the new key. Due to the nature of GPG signing, releases signed with the previous key will no longer be verifiable after importing the revocation.

`-----BEGIN PGP PUBLIC KEY BLOCK-----`
`mQINBFWpQAQBEAC+9wVlwGLy8ILCybLesuB3KkHHK+Yt1F1PJaI30X448ttGzxCz`
`PQpH6BoA73uzcTReVjfCFGvM4ij6qVV2SNaTxmNBrL1uVeEUsCuGduDUQMQYRGxR`
`tWq5rCH48LnltKPamPiEBzrgFL3i5bYEUHO7M0lATEknG7Iaz697K/ssHREZfuuc`
`B4GNxXMgswZ7GTZO3VBDVEw5GwU3sUvww93TwMC29lIPCux445AxZPKr5sOVEsEn`
`dUB2oDMsSAoS/dZcl8F4otqfR1pXg618cU06omvq5yguWLDRV327BLmezYK0prD3`
`P+7qwEp8MTVmxlbkrClS5j5pR47FrJGdyupNKqLzK+7hok5kBxhsdMsdTZLd4tVR`
`jXf04isVO3iFFf/GKuwscOi1+ZYeB3l3sAqgFUWnjbpbHxfslTmo7BgvmjZvAH5Z`
`asaewF3wA06biCDJdcSkC9GmFPmN5DS5/Dkjwfj8+dZAttuSKfmQQnypUPaJ2sBu`
`blnJ6INpvYgsEZjV6CFG1EiDJDPu2Zxap8ep0iRMbBBZnpfZTn7SKAcurDJptxin`
`CRclTcdOdi1iSZ35LZW0R2FKNnGL33u1IhxU9HRLw3XuljXCOZ84RLn6M+PBc1eZ`
`suv1TA+Mn111yD3uDv/u/edZ/xeJccF6bYcMvUgRRZh0sgZ0ZT4b0Q6YcQARAQAB`
`tC9Nb3ppbGxhIFNvZnR3YXJlIFJlbGVhc2VzIDxyZWxlYXNlQG1vemlsbGEuY29t`
`PokCOAQTAQIAIgUCValABAIbAwYLCQgHAwIGFQgCCQoLBBYCAwECHgECF4AACgkQ`
`Ybe1JtmPA1NQqg//Rr6/V7uLqrIwx0UFknyNJasRJZhUkYxdGsLD18zO0Na8Ve3Q`
`sYpOC3ojpqaFUzpqm6KNv8eXfd/Ku7j3WGr9kPkbjZNghvy6V5Lva4JkxO6LMxKk`
`JYqiqF2o1Gfda8NfcK08GFy4C0L8zNwlADvmdMo4382tmHNGbTTft7BeVaRrE9xW`
`9eGmGQ2jYOsjxb5MsadAdZUuK8IC95ZHlUDR3gH9KqhfbQWp5Bo924Kiv+f2JUzN`
`rrG98eOm1Qb8F9rePzZ2DOYRJyOe4p8Gpl+kojCXNntkJgcwJ1a1yRE6wy9RzpeB`
`lCeoQuLS92MNne+deQZUskTZFoYXUadf6vbdfqL0nuPCKdl9lhef1QNwE30IRymt`
`6fhJCFffFQjGdeMfSiCHgcI8ichQbrzhBCGGR3bAHan9c2EbQ+puqG3Aa0YjX6Db`
`GJjWOI6A61bqSPepLCMVaXqV2mZEIaZWdZkOHjnRrU6CJdXG/+D4m1YBZwYM60eJ`
`kNu4eMMwMFnRsHiWf7bhqKptwuk8HyIGp2o4j8iqrFRVJEbK/ctdhA3H1AlKug9f`
`NrfwCfqhNCSBju97V03U26j04JMn9nrZ2UEGbpty+8ONTb38WX5/oC61BgwV8Ki4`
`6Lwyb7fImUzz8jE83pjh7s3+NCKvvbH+VfT12f+V/fsphN3EwGwJPTC3fX2IRgQQ`
`EQIABgUCVaz/SwAKCRB2JUA9fw0VsVNkAKDjhUW5GyFNcyj9ot48v+lSh5GBIACf`
`Ten/Rpo5tf77Uq7445cVs80EK5CIRgQQEQIABgUCVa064wAKCRDDTldH4j3WdwW5`
`AKCVDRxKjb/XYqGhjBCKYhbQ4xJuOACfVIpzE3wGLC/cm9eUnSVnv+elQnKIXgQQ`
`EQgABgUCVgZXYwAKCRACWrAQaxfqHqzWAP9dzEHoZNwH5JYxotudv3FOotVThaQr`
`jnk+5StnObpxnAD9FmYyAyYGh4o7axeDCgmW1J89+1cZtDnFPKnBpGFMB4uIXgQQ`
`EQoABgUCVa0s/gAKCRDwqefc055FLpQGAP99Z2ISKW+7FYoKJ3vDrxTtfcbZEff7`
`8ufoinmAlZb2bQD/a2fOcprjWDal9Orfq7g6htkX3VISemg+SDQ/ig+b3uyJARwE`
`EAECAAYFAlWs/X4ACgkQs8WpWFCKQ/JrjAf7B+fGzEs8xfc010a6KZXcO1W4/Va0`
`Q+zcqF+DpQwK7b3S6oD5tCVKD9oFyDXkrlT6Tnwuu+slZwRDIyH6hI6tPb3G8Gsk`
`vjXMeL0IdgZsw1DSxN0pZ0Z9mxFq/UkC/6TmFA1IJmOWtFCH/1irQWqbDxPmWp+d`
`Xs2EhH8QzX1KQOE9v/YlsCdmTstMiHy3R8r7prsonpCa36zGheC/UNDpycKdT8JL`
`zeCFcIWXmA7SCTeJ0XCSuS68FOwfe7nn9oagQZZe/6gh5ecuCoW9HLBWpyIPqUCz`
`1CXSImLc6BbZYMpAetacarVPa6hiltNicxFE/A3T1F8ZjAcugPKBngUR/4kBHAQQ`
`AQIABgUCVa0XXAAKCRBlc4Lb/yURCkCYB/95w/9/0rpi+5xtoO2NR0KlqYVG5+NF`
`1r42XB6t7gVJ9UGF3meV+ekgDSzNrfroqxpzWmV1t3MRJeSMmVS25nC1hAZVQHKd`
`gX9xVxW3SSufX/jPstvo2U/X3k8q8PhLS6Ihk8YJC3ScjMiNMRpkITMeVdXsdQsY`
`WStiT48wlWK4gSNMCG5iovdGDTEKErHTIWJl/Wx5el1kvUwg1rKo9uRS2CS/lnlV`
`6YztDY0cBBOqXP6pXXiWBuVW39LJxsSHq13vpeQ/GHeDxAJ6Y+fPuaV3qBmGZ91o`
`1/HkxTABFPkISylkPo/2PCoo4Hu31MZ0jQWdihJ7gzf+B7/w6whS79eAiQEcBBAB`
`AgAGBQJVrWVaAAoJEOQyfGw+ApnAc7AH/0TKg3VR4IEB3NP2C7dX/72PWO0EOh8J`
`w67XDccRK0lXDILg/CujsYq9EzEofv2LmQFvCuCkoBFEcGas+J2vP3jsY/G5bjZp`
`XALHkAx7MKlOgsgfeVqMtwaHIoR+y9Hg12TjM7Gt970UBwTIqC8SG6Z1bVWxUdc+`
`7Zsn43Dq8z99saOUKD6HMyl9upbjAYwL28NRQtIrNiDZ5lEmDOLh+4hWblxjxWMX`
`AKjg6sucrNzKD2uKGe9XdB6IkYpdfrNGPtgcnXWdfaRNk16eGVzWDVI/9mkY/G+L`
`E40eK6oRyMf736CvlQjcv7JBVGTsj3W28phNLLU0UidYK/QmS3AVmBeJARwEEAEC`
`AAYFAlXBWXAACgkQiRc/lXxV+V6gKQf/d/KfgiYg0Z4dqO3g1p40sgLuxVplhpDk`
`J4yP5K2isdb6I7GJykVw+po6tUCfB7KeLWiZy0I3KJDU1Ikk+Jv3uGSRMT1riSpM`
`Ja2pVhh+jaamHIFj2o0mG9HmEAuGKktJH8s6Jax3SiPGODRhFO8suc7B8FpB7f5q`
`TUDK2J18MlnSK3NN1/zl6OdXScrISQ0cNyJ0RMgW5RSXC7wKzR89tfcDK1wInD8r`
`cOMHz6Va5g8ehq2XCPKvBAlgo8El17+4UaRLhS0suVz4THPsGASYzZVKIhQQBf+8`
`xDXd6...