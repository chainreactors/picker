---
title: Create your own telemetry system
url: https://armoredcode.com/blog/create-your-own-telemetry-system/
source: Over Security
date: 2026-05-28
fetch_date: 2026-05-29T06:06:07.142851
---

# Create your own telemetry system

[Armored Code](/)

[Blog](/blog/)
[Newsletter](https://mailchi.mp/a61f93445c94/armored-code-newsletter)

# Create your own telemetry system

April 2019

In order to monitor [dawnscanner](https://dawnscanner.org) security scaner
usage, I introduced in upcoming version
[2.0.0](https://github.com/thesp0nge/dawnscanner/tree/kb_revamp_in_yaml), a
telemetry system.

On boot, dawnscanner will check if it has a unique identifier and if not it
will ask for one to the telemetry system.

```
get '/new' do
  i = Id.new
  i.uuid = Id.get_new_id
  i.save

  content_type :json
  {:uuid => i.uuid }.to_json
end
```

Id is an
[ActiveRecord](https://api.rubyonrails.org/classes/ActiveRecord/Base.html)
class for the identifier model.

```
require 'securerandom'

class Id < ActiveRecord::Base
  def self.get_new_id
    return SecureRandom.uuid
  end
end
```

The initialization part happens in the
[Dawn::Cli](https://github.com/thesp0nge/dawnscanner/blob/kb_revamp_in_yaml/lib/dawn/cli/dawn_cli.rb)
class.

```
$telemetry_url = $config[:telemetry][:endpoint] if $config[:telemetry][:enabled]
debug_me("telemetry url is " + $telemetry_url) unless @telemetry_url.nil?
$telemetry_id = $config[:telemetry][:id] if $config[:telemetry][:enabled]

debug_me("telemetry id is " + $telemetry_id) unless @telemetry_id.nil?
$logger.info("telemetry is disabled in config file") unless $config[:telemetry][:enabled]
```

The real magic is in the
[Dawn::Engine](https://github.com/thesp0nge/dawnscanner/blob/kb_revamp_in_yaml/lib/dawn/engine.rb)
class. Here we’ve got a telemetry method that do all the stuff.

The basic idea is to do a post on a URL posting the unique dawnscanner
identifier (that is also the URL where the post is made), the IP address and
the knowledge base version.

```
def have_a_telemetry_id?
  debug_me ($telemetry_id != ""  and ! $telemetry_id.nil?)
  return ($telemetry_id != ""  and ! $telemetry_id.nil?)

end

def get_a_telemetry_id
  return "" if ($telemetry_url == "" or $telemetry_url.nil?)
  debug_me("T: " + $telemetry_url)

  url = URI.parse($telemetry_url+"/new")
  res = Net::HTTP.get_response(url)

  return "" unless res.code.to_i == 200
  return JSON.parse(res.body)["uuid"]
end

def telemetry
  unless have_a_telemetry_id?
    $telemetry_id = get_a_telemetry_id
    $config[:telemetry][:id] = $telemetry_id
    debug_me($config)
    debug_me("saving config to " + $config_name)
    File.open($config_name, 'w') { |f| f.write $config.to_yaml }
  end

  debug_me("Telemetry ID is: " + $telemetry_id)

  uri=URI.parse($telemetry_url+"/"+$telemetry_id)
  header = {'Content-Type': 'text/json'}
  tele = { "kb_version" => Dawn::KnowledgeBase::VERSION ,
           "ip" => Socket.ip_address_list.detect{|intf| intf.ipv4_private?}.ip_address,
           "message"=> Dawn::KnowledgeBase
        }
  http = Net::HTTP.new(uri.host, uri.port)
  request = Net::HTTP::Post.new(uri.request_uri, header)
  request.body = tele.to_json

  response=http.request(request)
  debug_me(response.inspect)

  return true

end
```

That’s it. No personal data apart from your IP is sent to dawnscanner servers.
On backend side, I implemented a simple Sinatra post catcher block of code,
saving the data on a SQLite3 database.

```
post '/:uuid' do
  request.body.rewind
  @request_payload = JSON.parse request.body.read

  i = Id.find_by("uuid", params['uuid'].to_s)
  unless i.nil?
    l=Log.new
    l.uuid = params['uuid'].to_s
    l.ip=@request_payload['ip']
    l.kb_version=@request_payload['kb_version']
    l.message=@request_payload['message']
    l.save
  end
end
```

This very basic telemetry system needs tons of improvements and, of course,
it’s opensource code hosted on
[Github.com](https://github.com/thesp0nge/telemetry).

Enjoy it!

© 2012 - 2026 Armored Code. All rights
reserved.