#Scrapy using Tor and Privoxy

[Ethics in Web Scraping](https://towardsdatascience.com/ethics-in-web-scraping-b96b18136f01)

Barebone Scrapy project
### Installing Tor and Privoxy
```
sudo apt-get update
sudo apt-get install tor privoxy
```
### Configuring Tor
Add tor password to scraper/scraper/middlewares.py in _set_new_ip function:
```
with Controller.from_port(port=9051) as controller:
    controller.authenticate(password=YOURPASSWORD)  # tor password
    controller.signal(Signal.NEWNYM)
```

Generate a hash for password:
```
tor --hash-password YOURPASSWORD
```

Add at the end of /etc/tor/torrc:
```
ControlPort 9051
HashedControlPassword GENERATEDHASH
```

### Configuring Privoxy
Add at the end of /etc/privoxy/config:
```
forward-socks5t / 127.0.0.1:9050 .
# Optional
keep-alive-timeout 600
default-server-timeout 600
socket-timeout 600
```

Start the services:
```
sudo service privoxy start
sudo service tor start
```

### Running spider
Create and activate virtual environment:
```
python3 -m venv venv
source venv/bin/activate
```
Install packages:
```
pip install --upgrade pip
pip install scrapy stem requests[socks] scrapy-fake-useragent
```
Run spider:
```
cd scraper
scrapy crawl check_ip
```