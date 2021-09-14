#!/bin/bash
# delete request to the URL passed as the fisrt argv
curl -s -X DELETE "$1"
