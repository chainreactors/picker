---
title: Uncovering Hidden Cloudflare Pages and Workers
url: https://infosecwriteups.com/uncovering-hidden-cloudflare-pages-and-workers-af602df05f1a?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-02-25
fetch_date: 2025-10-06T20:34:38.861910
---

# Uncovering Hidden Cloudflare Pages and Workers

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Faf602df05f1a&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Funcovering-hidden-cloudflare-pages-and-workers-af602df05f1a&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Funcovering-hidden-cloudflare-pages-and-workers-af602df05f1a&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-af602df05f1a---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-af602df05f1a---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# **Uncovering Hidden Cloudflare Pages and Workers for Fun and Profit !**

[![Scott Lindh](https://miro.medium.com/v2/resize:fill:64:64/1*t920uWILCzfvaRTNExHlyg.png)](https://medium.com/%40scottlindh?source=post_page---byline--af602df05f1a---------------------------------------)

[Scott Lindh](https://medium.com/%40scottlindh?source=post_page---byline--af602df05f1a---------------------------------------)

4 min read

·

Feb 24, 2025

--

Listen

Share

Cloudflare Pages/Workers offers a seamless platform for deploying static sites and applications, integrating directly with repositories on GitHub and GitLab. While this service enhances performance and security for legitimate users, it can inadvertently expose hidden pages or workers if not properly configured.

As penetration testers, identifying these overlooked assets is crucial for comprehensive security assessments.

**Reconnaissance Tools and Techniques**

Effective reconnaissance is the cornerstone of penetration testing. To uncover hidden Cloudflare Pages, consider the following tools and methodologies:

1. **Censys / Shodan**: A powerful search engine that indexes internet-connected devices. While Shodan and Censys can reveal exposed services, its effectiveness may be limited without a paid subscription.
   We can search Certificates for pages.dev

Press enter or click to view image in full size

![]()

Search Certificates for pages.dev

1. **Cert.sh**: A valuable resource for discovering SSL/TLS certificates. By querying cert.sh, you can identify domains associated with Cloudflare Pages deployments.

Here is a little bash script you may use to scrape from cert.sh:

```
#!/bin/bash

# URL to fetch
url="https://crt.sh/?Identity=pages.dev&exclude=expired"

# File to save the raw HTML
html_file="output.html"

# File to save the filtered results
output_file="filtered_results.txt"

# Fetch the HTML content and save it to a file
echo "Fetching HTML from $url..."
curl -s "$url" -o "$html_file"

# Check if the HTML file was successfully created
if [[ ! -f "$html_file" ]]; then
  echo "Error: Failed to fetch HTML content."
  exit 1
fi

# Extract all unique domain names containing "pages.dev" from the HTML table
echo "Extracting unique 'pages.dev' domains..."
grep -oP '<TD>[^<]*pages\.dev[^<]*</TD>' "$html_file" | sed 's/<TD>\(.*\)<\/TD>/\1/' | sort | uniq > "$output_file"

# Check if the output file was successfully created
if [[ ! -f "$output_file" ]]; then
  echo "Error: Failed to extract results."
  exit 1
fi

# Print the results to the terminal
echo "Unique 'pages.dev' domains found:"
cat "$output_file"

echo "HTML content saved to: $html_file"
echo "Filtered results saved to: $output_file"
```

Using the above script you will get results similar to the below list:
*(If you are doing reseach on a specific target you might want to edit the above script to also include a search for your keywords/company)*

```
00111.pages.dev
00133.pages.dev
00138.pages.dev
006-02vsexblay.pages.dev
02-24tregd.pages.dev
02-hiperlinks-interno.pages.dev
0333f5d1-b331-43a7-b910-3150d68f8f41.pages.dev
04bd.pages.dev
04s7a19ul9.pages.dev
04vhvfuncs.pages.dev
05285902.pages.dev
06323842.pages.dev
0c82660e-8ab7-4390-9428-d7b7fc6ea967.pages.dev
0d2a4de9-33a6-46a4-8510-ef31d90ff649.pages.dev
0it5h5p30i.pages.dev
0s9g6rk609.pages.dev
0wdoz1o71g.pages.dev
111-017-4ir.pages.dev
112-arf.pages.dev
11-dvk.pages.dev
```

Press enter or click to view image in full size

![]()

**Automated Reconnaissance with GoWitness**

To streamline the reconnaissance process, consider using GoWitness, an open-source tool designed to capture screenshots of web pages and generate a user-friendly dashboard for analysis.

*Installation:*

Ensure Go is installed on your system:

```
sudo apt install golang-go
```

Then, install GoWitness:

```
go install github.com/sensepost/gowitness@latest
```

*Usage:*

```
gowitness scan file -f merged_file.txt --write-db
```

This command processes a list of URLs from `merged_file.txt`, capturing screenshots and generating a report.

Press enter or click to view image in full size

![]()

Gowitness Dashboard

We can use the Gowitness dashboard to search for some interesting pages, ie: admin…

```
gowitness report list

OR

gowitness report server
```

Press enter or click to view image in full size

![]()

We can see many Login pages !

**Enhancing Analysis with Eyeballer**

For advanced categorization of discovered pages, integrate Eyeballer, an AI-driven tool that classifies web pages into categories such as login pages, landing pages, or dashboards.

*Installation:*

```
git clone https://github.com/BishopFox/eyeballer.git
cd eyeballer
pip install -r requirements.txt
```

*Usage:*

```
python eyeballer.py --input screenshots/ --output categorized/
```

This command processes the screenshots in the `screenshots/` directory and outputs categorized results in the `categorized/` directory.

We can see Eyeballer uses AI to categorize the pages we found :

Press enter or click to view image in full size

![]()

**Identifying Sensitive Resources**

Examine the titles and status codes of the captured pages to identify sensitive resources, such as admin panels or internal dashboards.

For a more detailed analysis, you can generate a report with GoWitness:

```
gowitness scan file -f merged_file.txt -t 10 --write-db
gowitness report server
gowitness report list --db-uri sqlite://gowitness.sqlite3
gowitness server -A
```

These commands provide a comprehensive overview of the captured pages, facilitating the identification of critical assets.

**Conclusion**

Uncovering hidden Cloudflare Pages requires a methodical approach using tools like Shodan, cert.sh, GoWitness, and Eyeballer. By systematically applying these techniques, penetration testers can identify overlooked assets, ensuring a more comprehensive security assessment.

During my research, I discovered numerous assets that users likely assumed were hidden but were, in fac...