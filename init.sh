#! /bin/bash 
python3 -m venv .env
source .env/bin/activate
sleep 3
pip3 install -r requirements.txt
echo "All task are finished" 