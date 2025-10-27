---
title: Extreme Privacy Update: Self-Hosted SearXNG Guide
url: https://inteltechniques.com/blog/2025/07/11/extreme-privacy-update-self-hosted-searxng-guide/
source: IntelTechniques Blog
date: 2025-07-12
fetch_date: 2025-10-06T23:49:23.363288
---

# Extreme Privacy Update: Self-Hosted SearXNG Guide

[Skip to content](#main)

[# IntelTechniques](https://inteltechniques.com)

[IntelTechniques Blog](https://inteltechniques.com/blog/)

* [Training](https://inteltechniques.com/training.html)
* [Services](https://inteltechniques.com/services.html)
* [Resources](https://inteltechniques.com/links.html)
* [Tools](https://inteltechniques.com/tools/)
* [Blog](https://inteltechniques.com/blog/)
* [Podcast](https://inteltechniques.com/podcast.html)
* [Magazine](https://unredactedmagazine.com)
* [Books](https://inteltechniques.com/books.html)
* [Contact](https://inteltechniques.com/contact.html)

# Extreme Privacy Update: Self-Hosted SearXNG Guide

* [Posted on
  July 11, 2025](https://inteltechniques.com/blog/2025/07/11/extreme-privacy-update-self-hosted-searxng-guide/)
* Posted in
  [OSINT](https://inteltechniques.com/blog/category/osint/), [Privacy](https://inteltechniques.com/blog/category/privacy/), [Security](https://inteltechniques.com/blog/category/security/)

In my books [Extreme Privacy](https://inteltechniques.com/book7.html) and [OSINT Techniques](https://inteltechniques.com/book1.html), I discuss the SearXNG as an option to access search engine results. SearXNG is not a search engine itself. It is a metasearch engine which aggregates the results of multiple search engines, such as Google, Bing, and others, but does not share information about users to the engines queried. It is also open source and can be self-hosted. The easiest way to get started is to visit https://searx.space/ and test a few public instances.

After you have played with any of the public instances of SearXNG, you may now see the benefits of an aggregated search service. You may also be considering the risks associated with this behavior. Let's start with the benefits of a public instance which is not self-hosted.

* All queries are submitted to search engines from a third-party server.
* The IP addresses collected from engines are those of the server, not yours.
* Your queries cannot easily be associated to one user by the engines.

That may sound great, but there are risks with public instances. Consider the following.

* The host of the instance could monitor your queries.
* If the host is popular, some engines may block access.
* If the host has an outage, you are without service.

Overall, I believe it would be very unusual for a SearXNG host to monitor queries. This cannot be done with the stock SearXNG software, and hosts would have to go out of their way to collect data about users. I just do not see the motive of that. However, anything is possible. Personally, I prefer to self-host my own instance of SearXNG. Consider the following benefits.

* All queries are submitted from your machine directly to the engines.
* The tracking code on engine websites is removed from the SearXNG pages.
* Minimal usage ensures that all options function reliably.
* Does not rely on the uptime of an online instance for my queries.

As always, there are also risks. My IP address is submitted with every query I make, but I am always behind a VPN so I am not bothered by that. The ability to host my own code and know that no one else is intercepting that data is more important to me. You can never hide the queries from the search engines themselves, but you can limit the information loaded into your browser by not visiting their sites directly. Receiving results from multiple search engines simultaneously is very advantageous. Take some time to determine whether you are better served with a public instance or your own. I took the following steps on my Linux machine to configure my own host locally. If you decide to replicate these steps, you should copy and paste the in its entirety directly into Terminal. Note that these steps deviate from the official installation guides which are mostly outdated.
 `sudo -H apt-get install -y python3-pip python3-dev python3-babel \
python3-venv uwsgi uwsgi-plugin-python3 \
git build-essential libxslt-dev zlib1g-dev \
libffi-dev libssl-dev
mkdir ~/Documents/searxng && cd ~/Documents/searxng
git clone "https://github.com/searxng/searxng"
python3 -m venv searxngEnvironment
source searxngEnvironment/bin/activate
pip install -U pip
pip install -U setuptools
pip install -U wheel
pip install -U pyyaml
cd searxng && pip install --use-pep517 --no-build-isolation -e .
sudo -H mkdir -p "/etc/searxng"
sed -i "s|ultrasecretkey|$(openssl rand -hex 32)|g" searx/settings.yml
sudo -H cp searx/settings.yml /etc/searxng/settings.yml
export SEARXNG_SETTINGS_PATH="/etc/searxng/settings.yml"
deactivate`
My machine is now configured to run the SearXNG software. The following commands execute the program.
 `cd ~/Documents/searxng
source searxngEnvironment/bin/activate
cd searxng
python searx/webapp.py`
The software is now running in the background. You can minimize this Terminal window. As long as it is not closed completely, the service is running. You can launch Firefox and navigate to http://127.0.0.1:8888 to load your own instance. Similar to public instances, any modifications you make to SearXNG will be erased when you close Firefox, unless you add http://127.0.0.1 to your stored cookies (or modify the settings.yml file directly). You can execute the following commands to fetch any updates.
 `cd ~/Documents/venv/searxng/searxng
git pull "https://github.com/searxng/searxng"`
If desired, you can add these two commands to the Linux update script presented in Extreme Privacy. You could also add the launch commands to the maintenance scripts within the book. The image below displays an example query. Notice that I receive results from Google, Bing, Brave, and DuckDuckGo simultaneously.

![](https://inteltechniques.com/blog/wp-content/uploads/Picture1-1-620x339.png)

From any search result, I prefer to click the "Preferences" option on the far right and make a few modifications. I disable any auto-complete options; disable SafeSearch; switch to a light theme; enable results in new tabs; and enable preferred search engines throughout all topics. You can even modify the way URLs will be presented. This allows you to remove embedded URL tracking codes, force older or mobile versions of websites, or even remove affiliate tracking links. Your options are unlimited when you control the code. If you want to store these changes so they will be preserved after you restart Firefox, you must conduct the following.

* Navigate to Firefox's Settings menu and click the "Privacy & Security" option.
* Click "Manage Exceptions" next to "Delete cookies...".
* Enter the URL of your SearXNG instance, such as "https://127.0.0.1".
* Click "Allow" and "Save Changes".

I currently have a self-hosted SearXNG instance running on my laptop, which allows me to query dozens of search engines simultaneously from my browser without trusting any third-party middle man. Since I rarely search or browse websites from my mobile device, I simply rely on a public SearXNG instance on it.

Let's repeat the process for those on macOS who want to self-host SearXNG. Make sure you have Homebrew configured as explained in the book.
 `brew install python3.13 git
mkdir ~/Documents/venv
cd ~/Documents/venv
python3.13 -m venv searxng
source searxng/bin/activate
cd searxng
git clone "https://github.com/searxng/searxng"
pip3.13 install -U pip
pip3.13 install -U setuptools
pip3.13 install -U wheel
pip3.13 install -U pyyaml
pip3.13 install -U lxml
cd searxng
pip3.13 install --use-pep517 --no-build-isolation -e .
cd searx
sudo mkdir "/etc/searxng"
sudo cp settings.yml /etc/searxng/settings.yml
sed -i '' "s/ultrasecretkey/00ef3039748274b4f2b93d16fb9695de00a4bb35e4c02b7704a167c7aeb274bd/g" /etc/searxng/settings.yml`

deactivate

My machine is now configured to run the SearXNG software. The following commands execute the program.
 `cd ~/Documents/venv
source searxng/bin/activate
cd searxng/searxng
python3.13 searx/webapp.py`
The software is now running in the background. You can minimize this Terminal window. As long as it is not clo...