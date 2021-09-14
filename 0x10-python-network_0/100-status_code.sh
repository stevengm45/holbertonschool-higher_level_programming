#!/bin/bash
# sends request to URL
curl -s -o /dev/null -I -w "%{http_code}" "$1"
