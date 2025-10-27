---
title: Basic Authentication authentication now disabled for the Jamf Pro Classic API as of Jamf Pro 11.5.0
url: https://derflounder.wordpress.com/2024/05/21/basic-authentication-authentication-now-disabled-for-the-jamf-pro-classic-api-as-of-jamf-pro-11-5-0/
source: Der Flounder
date: 2024-05-22
fetch_date: 2025-10-06T16:49:02.857513
---

# Basic Authentication authentication now disabled for the Jamf Pro Classic API as of Jamf Pro 11.5.0

# [Der Flounder](https://derflounder.wordpress.com/)

Seldom updated, occasionally insightful.

* [Home](https://derflounder.wordpress.com/ "Home")
* [About](https://derflounder.wordpress.com/about-2/)
* [Contact](https://derflounder.wordpress.com/contact/)

[Home](https://derflounder.wordpress.com/ "Go to homepage")
> [Jamf Pro](https://derflounder.wordpress.com/category/jamf-pro/), [Jamf Pro Classic API](https://derflounder.wordpress.com/category/jamf-pro-classic-api/), [Scripting](https://derflounder.wordpress.com/category/scripting/) > Basic Authentication authentication now disabled for the Jamf Pro Classic API as of Jamf Pro 11.5.0

## Basic Authentication authentication now disabled for the Jamf Pro Classic API as of Jamf Pro 11.5.0

May 21, 2024
[rtrouton](https://derflounder.wordpress.com/author/rtrouton/ "Posts by rtrouton") [Leave a comment](#respond)
[Go to comments](#comments)

As a follow-up to my earlier post on Basic Authentication being deprecated for the Jamf Pro Classic API ([first announced as part of the release of Jamf Pro 10.35.0](https://derflounder.wordpress.com/2022/01/04/basic-authentication-deprecated-for-the-jamf-pro-classic-api/)), [Jamf has disabled Basic Authentication support for the Jamf Pro Classic API as Jamf Pro 11.5.0](https://learn.jamf.com/en-US/bundle/jamf-pro-release-notes-current/page/Important_Notices.html#ariaid-title2).

![](https://derflounder.wordpress.com/wp-content/uploads/2024/05/screenshot-2024-05-21-at-1.10-1.png?w=599&h=335 "Screenshot 2024-05-21 at 1.10.png")

One thing to note is that this change does not impact Cisco ISE integration, which also uses Basic Authentication.

![](https://derflounder.wordpress.com/wp-content/uploads/2024/05/screenshot-2024-05-21-at-1.10.png?w=599&h=335 "Screenshot 2024-05-21 at 1.10.png")

For those looking now to transition away from Basic Authentication for connecting to the Jamf Pro Classic API, I’ve written a couple of shell script functions to assist with getting the bearer tokens now used for API authentication for the following categories:

* [Jamf Pro API clients](https://learn.jamf.com/en-US/bundle/jamf-pro-documentation-current/page/API_Roles_and_Clients.html)
* [Jamf Pro user accounts](https://learn.jamf.com/en-US/bundle/jamf-pro-documentation-current/page/Jamf_Pro_User_Accounts_and_Groups.html)

For more details, please see below the jump.

Jamf Pro API clients:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

[Show hidden characters](%7B%7B%20revealButtonHref%20%7D%7D)

|  |  |
| --- | --- |
|  | #!/bin/bash |
|  |  |
|  | # If you choose to hardcode API information into the script, set one or more of the following values: |
|  | # |
|  | # The Jamf Pro URL |
|  | # An API client ID on the Jamf Pro server with sufficient API privileges |
|  | # The API client secret for the API client ID |
|  |  |
|  | # Set the Jamf Pro URL here if you want it hardcoded. |
|  | jamfpro\_url="" |
|  |  |
|  | # Set the Jamf Pro API Client ID here if you want it hardcoded. |
|  | jamfpro\_api\_client\_id="" |
|  |  |
|  | # Set the Jamf Pro API Client Secret here if you want it hardcoded. |
|  | jamfpro\_api\_client\_secret="" |
|  |  |
|  | # If you do not want to hardcode API information into the script, you can also store |
|  | # these values in a ~/Library/Preferences/com.github.jamfpro-info.plist file. |
|  | # |
|  | # To create the file and set the values, run the following commands and substitute |
|  | # your own values where appropriate: |
|  | # |
|  | # To store the Jamf Pro URL in the plist file: |
|  | # defaults write com.github.jamfpro-info jamfpro\_url <https://jamf.pro.server.goes.here:port_number_goes_here> |
|  | # |
|  | # To store the Jamf Pro API Client ID in the plist file: |
|  | # defaults write com.github.jamfpro-info jamfpro\_api\_client\_id api\_client\_id\_information\_goes\_here |
|  | # |
|  | # To store the Jamf Pro API Client Secret in the plist file: |
|  | # defaults write com.github.jamfpro-info jamfpro\_api\_client\_secret api\_client\_secret\_information\_goes\_here |
|  | # |
|  | # If the com.github.jamfpro-info.plist file is available, the script will read in the |
|  | # relevant information from the plist file. |
|  |  |
|  | if [[ -f "$HOME/Library/Preferences/com.github.jamfpro-info.plist" ]]; then |
|  |  |
|  | if [[ -z "$jamfpro\_url" ]]; then |
|  | jamfpro\_url=$(defaults read $HOME/Library/Preferences/com.github.jamfpro-info jamfpro\_url) |
|  | fi |
|  |  |
|  | if [[ -z "$jamfpro\_api\_client\_id" ]]; then |
|  | jamfpro\_api\_client\_id=$(defaults read $HOME/Library/Preferences/com.github.jamfpro-info jamfpro\_api\_client\_id) |
|  | fi |
|  |  |
|  | if [[ -z "$jamfpro\_api\_client\_secret" ]]; then |
|  | jamfpro\_api\_client\_secret=$(defaults read $HOME/Library/Preferences/com.github.jamfpro-info jamfpro\_api\_client\_secret) |
|  | fi |
|  |  |
|  | fi |
|  |  |
|  | # If the Jamf Pro URL, the API Client ID or the API Client Secret aren't available |
|  | # otherwise, you will be prompted to enter the requested URL or API client credentials. |
|  |  |
|  | if [[ -z "$jamfpro\_url" ]]; then |
|  | read -p "Please enter your Jamf Pro server URL : " jamfpro\_url |
|  | fi |
|  |  |
|  | if [[ -z "$jamfpro\_api\_client\_id" ]]; then |
|  | read -p "Please enter your Jamf Pro API client ID : " jamfpro\_api\_client\_id |
|  | fi |
|  |  |
|  | if [[ -z "$jamfpro\_api\_client\_secret" ]]; then |
|  | read -p "Please enter the API client secret for the $jamfpro\_api\_client\_id API ID client: " -s jamfpro\_api\_client\_secret |
|  | fi |
|  |  |
|  | echo "" |
|  |  |
|  | # Remove the trailing slash from the Jamf Pro URL if needed. |
|  | jamfpro\_url=${jamfpro\_url%%/} |
|  |  |
|  | GetJamfProAPIToken() { |
|  |  |
|  | # This function uses the API client ID and client ID secret to get a new bearer token for API authentication. |
|  |  |
|  | if [[ $(/usr/bin/sw\_vers -productVersion | awk -F . '{print $1}') -lt 12 ]]; then |
|  | api\_token=$(/usr/bin/curl -s -X POST "$jamfpro\_url/api/oauth/token" –header 'Content-Type: application/x-www-form-urlencoded' –data-urlencode client\_id="$jamfpro\_api\_client\_id" –data-urlencode 'grant\_type=client\_credentials' –data-urlencode client\_secret="$jamfpro\_api\_client\_secret" | python -c 'import sys, json; print json.load(sys.stdin)["access\_token"]') |
|  | else |
|  | api\_token=$(/usr/bin/curl -s -X POST "$jamfpro\_url/api/oauth/token" –header 'Content-Type: application/x-www-form-urlencoded' –data-urlencode client\_id="$jamfpro\_api\_client\_id" –data-urlencode 'grant\_type=client\_credentials' –data-urlencode client\_secret="$jamfpro\_api\_client\_secret" | plutil -extract access\_token raw -) |
|  | fi |
|  |  |
|  | } |
|  |  |
|  | APITokenValidCheck() { |
|  |  |
|  | # Verify that API authentication is using a valid token by running an API command |
|  | # which displays the authorization details associated with the current API user. |
|  | # The API call will only return the HTTP status code. |
|  |  |
|  | api\_authentication\_check=$(/usr/bin/curl –write-out %{http\_code} –silent –output /dev/null "${jamfpro\_url}/api/v1/auth" –request GET –header "Authorization: Bearer ${api\_token}") |
|  |  |
|  | } |
|  |  |
|  | GetJamfProAPIToken |
|  |  |
|  | APITokenValidCheck |
|  |  |
|  | echo "$api\_authentication\_check" |
|  |  |
|  | echo "$api\_token" |

[view raw](https://gist.github.com/rtrouton/a32eed58f2407f77af3daab0422f64e3/raw/08ff3b8399388dda3d143af1d4935841418f71c7/jamf_pro_api_client_token_management.sh)
 [jamf\_pro\_api\_client\_token\_management.sh](https://gist.github.com/rtrouton/a32eed58f2407f77af3daab0422f64e3#file-jamf_pro_api_client_token_management-sh)
hosted with ❤ by [GitHub](https://github.com)

...