# Rosetta Not That Stonks

**Rosetta Not That Stonks** is a tool that allows you to quickly validate Rosetta Stone lessons, saving time during course progression.

## Installation and usage

1. Install mitmproxy

```bash
# NixOS
nix-shell -p mitmproxy

# Archlinux
sudo pacman -S mitmproxy 
```

2. Install the **mitmproxy** Certificate Authority

```
# First, run mitmproxy once to generate the local CA certificate
mitmproxy
```

Then import the certificate located at `~/.mitmproxy/mitmproxy-ca-cert.pem` into your browser and trust it for identifying websites.

3. Setup an HTTP proxy

Configure your browser to use a local proxy on `127.0.0.1:8080`.

You can use **FoxyProxy** for an easy setup.

4. Start the proxy with the script 

```
git clone https://github.com/TRIKKSS/rosetta-not-that-stonks.git
cd rosetta-not-that-stonks
mitmproxy -s rosetta-not-that-stonks.py
```

5. Enjoy

You can now spam Ignore on Rosetta Stone challenges and still validate all your lessons !
