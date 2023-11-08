#!/bin/bash

docker run --name mitmproxy -it -d -v ~/.mitmproxy:/home/mitmproxy/.mitmproxy -v ./scripts:/home/mitmproxy/scripts -p 8080:8080 -p 127.0.0.1:8081:8081 mitmproxy/mitmproxy mitmweb --web-host 0.0.0.0 -s /home/mitmproxy/scripts/block.py
