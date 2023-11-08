# mitmproxy docker installation
## Installation
```
./run.sh
```
## Setting read-only domain
You can add push allowed server domain in scripts/read-only-list
## Test using CA certificate
```
curl -x http://localhost:8080 --cacert ~/.mitmproxy/mitmproxy-ca-cert.pem https://github.com
```
## Apply CA cerificate on clients

## Apply Git proxy settings on client
```
git config --global http.proxy http://localhost:8080
git config --global http.sslCAInfo ~/.mitmproxy/mitmproxy-ca-cert.pem
```
