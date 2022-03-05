#!/usr/bin/env python3
# python3.7で動作確認済み

import serial
import time
import json
import datetime
import os
import time
import subprocess

DEBUG = True

def logging(path, name, data):
    timestamp = datetime.datetime.now()
    filename = name + "_" + timestamp.strftime("%Y-%m-%d") + ".csv"
    write_str = timestamp.strftime("%Y/%m/%d %H:%M:%S") + "," + data
    path = path + "/"

    os.makedirs(path, exist_ok=True)
    f = open(path + filename, mode="a")
    f.write(write_str)
    f.close()

# 設定値読み込み
f = open("/home/pi/work/logger_rpi_throttole/config.json", "r")
conf = json.loads(f.read())
f.close()

data_old = ""
cmd = 'vcgencmd get_throttled'

path = conf["basedir"] + "/" + conf["logdir_name"]

while conf["interval"]:
    data = subprocess.Popen(cmd, stdout=subprocess.PIPE,shell=True).communicate()[0].decode('utf-8')
    if data_old != data:
        logging(path,conf["logdir_name"],str(data))
    data_old = data
    time.sleep(conf["interval"])