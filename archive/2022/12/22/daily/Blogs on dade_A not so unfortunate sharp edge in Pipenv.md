---
title: A not so unfortunate sharp edge in Pipenv
url: https://0xda.de/blog/2022/12/a-not-so-unfortunate-sharp-edge-in-pipenv/
source: Blogs on dade
date: 2022-12-22
fetch_date: 2025-10-04T02:12:41.837495
---

# A not so unfortunate sharp edge in Pipenv

[>
cd /0xda.de/](https://0xda.de/)

[ ]

* [About](https://0xda.de/about/)
* [Blog](https://0xda.de/blog/)
* [Garden](https://0xda.de/garden/)
* [Speaking](https://0xda.de/speaking/)
* [Music](https://0xda.de/music/)
* [Consulting](https://room641a.com)
[Tor](http://dadehacks5p4qrui2wy2bcfp37wgtycysqhxuwa2o7k2t34rryrzhdqd.onion/blog/2022/12/a-not-so-unfortunate-sharp-edge-in-pipenv/ "Tor")

[0xdade](https://0xda.de/)
![Photo of the site's author](https://0xda.de/img/dade-transparent-logo.png)

Seasonal Influencer. Python dev, security engineer, former red team, former SSD engineer. Hacker, rapper, writer. he/him

8 minutes

# [A not so unfortunate sharp edge in Pipenv](https://0xda.de/blog/2022/12/a-not-so-unfortunate-sharp-edge-in-pipenv/)

I’ve been a proponent of [pipenv](https://pipenv.pypa.io/en/latest/) for several years now, particularly for application development (rather than library development). While the features around virtual environment management and the integration with pyenv to automatically install the version of python necessary for an application are nice, the features that I’ve really advocated for are the separation of direct dependencies and transient dependencies, via Pipfile and Pipfile.lock, and the hash validation provided by Pipfile.lock. I find it helpful in improving the deterministic nature of builds (not solving, mind you, but improving), making sure everyone in the engineering organization is using the same versions of packages as everyone else. It’s also a minor reassurance against supply chain attacks, which is sort of what I want to write about today.

When you install a package with `pipenv install Django`, for instance, pipenv will automatically add `Django` to your `Pipfile` as a direct dependency, and then add Django’s dependencies as transient dependencies in `Pipfile.lock`. Say I install Django today and the latest version is `4.1.4`, and then tomorrow Django releases `4.1.5`. `Pipfile.lock` ensures that when my coworkers run `pipenv sync` (or when our Dockerfile does), they get `4.1.4` – the version that I originally installed. Of course we can update this automatically with `pipenv update`, but for the most part it is easy to install the same versions of the same packages I have installed. But because `Pipfile.lock` also contains the hashes of the distribution files for `Django==4.1.4`, if someone were to try to publish new distribution files for `Django==4.1.4` then `pipenv sync` would fail, because the hashes on pypi are not the same as the hashes your `Pipfile.lock` is expecting.

Therein lies a small problem, though. While Django was just an example using a popular package, I’m going to switch gears to a real life scenario.

## Real world example - python-crontab

We’ve got an application, and that application relies on a package called `python-crontab`. From it’s own description on PyPI:

> Crontab module for reading and writing crontab files and accessing the system cron automatically and simply using a direct API.

We installed `python-crontab` back in late October of 2021, and we installed the latest version at the time – `2.6.0`. `pipenv install python-crontab` gives us an entry in our `Pipfile.lock` that looks like this (along with some dependencies, not shown):

```
         "python-crontab": {
            "hashes": [
                "sha256:1e35ed7a3cdc3100545b43e196d34754e6551e7f95e4caebbe0e1c0ca41c2f1b"
            ],
            "version": "==2.6.0"
        }
```

Fast forward to today, our build is breaking and we aren’t really sure why. We automatically update dependencies every Monday morning, but after that happened the build was still working just fine. We also happened to update to the latest version of pipenv yesterday, but that still passed through the build fine. Something else had to have happened. Someone on our team attempted to rebuild our container environment with no cache and managed to get this output error from our `pipenv sync` step.

```
Installing dependencies from Pipfile.lock (2cdb99)...
ERROR: THESE PACKAGES DO NOT MATCH THE HASHES FROM THE REQUIREMENTS FILE. If you have updated the package versions, please update the hashes. Otherwise, examine the package contents carefully; someone may have tampered with them.
    python-crontab==2.6.0 from https://files.pythonhosted.org/packages/8a/65/ee4f4db956d14b42aa6cf0dbd0b77217a206484b99f1d4aa11326cd3952a/python_crontab-2.6.0-py3-none-any.whl (from -r /tmp/pipenv-uqho_tzz-requirements/pipenv-2hctl0kl-hashed-reqs.txt (line 183)):
        Expected sha256 1e35ed7a3cdc3100545b43e196d34754e6551e7f95e4caebbe0e1c0ca41c2f1b
             Got        f308a64b8b1d072da4a235e9320398a242e92d080c1d8143bd0c600b24e160f8
Installing initially failed dependencies...
ERROR: Disabling PEP 517 processing is invalid: project specifies a build backend of setuptools.build_meta in pyproject.toml
```

If we install the same version of `python-crontab` today into a new virtual environment with `pipenv install python-crontab==2.6.0` then we get this entry:

```
"python-crontab": {
            "hashes": [
                "sha256:1e35ed7a3cdc3100545b43e196d34754e6551e7f95e4caebbe0e1c0ca41c2f1b",
                "sha256:f308a64b8b1d072da4a235e9320398a242e92d080c1d8143bd0c600b24e160f8"
            ],
            "index": "pypi",
            "version": "==2.6.0"
        }
```

## Investigating

Interesting. It looks like the `python-crontab` wheel changed. Did my annoying insistence on using `pipenv` to help us combat supply chain attacks finally yield some fruit? Is this what vindication feels like? Well… sorta.

The hash that `pipenv` was expecting actually corresponds to [the hash for the sdist](https://pypi.org/project/python-crontab/2.6.0/#copy-hash-modal-811f8508-00b8-4437-9256-13cdb7f532df) from the initial release (October 19th, 2021) – the .tar.gz file. But a wheel is available now, as of December 19th 2022, which apparently wasn’t available before. This caused the hash validation to fail, which caused our build to fail, which caused us to get a hundred messages deep in a slack thread trying to understand what had happened.

I pulled down the source for [python-crontab-2.6.0.tar.gz](https://files.pythonhosted.org/packages/06/b0/c270a1b5c83d9e0f83ab654d3153c39d80f61ba49fefde50fd23ab351381/python-crontab-2.6.0.tar.gz) and the source for the new wheel [python\_crontab-2.6.0-py3-none-any.whl](https://files.pythonhosted.org/packages/8a/65/ee4f4db956d14b42aa6cf0dbd0b77217a206484b99f1d4aa11326cd3952a/python_crontab-2.6.0-py3-none-any.whl). I unzipped the wheel and then I went through each of the files in the wheel and diff’d them against the files available from the sdist.

![output of the diff command on each of the three suspicious files – there is no diff](https://0xda.de/blog/2022/12/a-not-so-unfortunate-sharp-edge-in-pipenv/img/pipenv-no-diff.6c382a903566c7525def1b6919640fc9.png)

No differences in any of the files in the wheel compared to the versions that we were running from the sdist for the past year. We can dig deeper and look at the issue tracker for python-crontab, where we see an issue created yesterday [asking for python wheels to be published to PyPI](https://gitlab.com/doctormo/python-crontab/-/issues/102). This corresponds to when the new wheel showed up. We can also see a ticket opened earlier today complaining about the same thing we noticed in our build system – [the hash changed for version 2.6.0](https://gitlab.com/doctormo/python-crontab/-/issues/103).

Overall this is `pipenv` working exactly as it should. This could have very easily been a wheel containing different code than what we’d previously been installing, and `pipenv` tried its hardest to make sure we investigated that before running the new code. If this had been an actual supply chain attack, we would have avoided deploying the malicious code into production. Hooray! And thankfully, it was just a developer trying to be helpful by providing a prebuilt wheel for an old pac...