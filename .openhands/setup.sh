#!/bin/bash
export MY_ENV_VAR="my value"
sudo apt-get update
sudo apt-get install -y lsof
cd frontend && npm install ; cd ..
