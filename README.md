# lhflask

# v1.1
flask + redis

    docker run --name redis --rm -p 6379:6379 -d redis:latest redis-server
    docker run -ti --name lhflask --rm -p 3389:80 ywllyht/lhflask:1.1 bash


Then open browser, visit http://xxxx.com:3389/redis

    if something wrong, check the redis server IP in appsite/index.py

## reference link
https://www.cnblogs.com/zhzhlong/p/9465670.html

# v1.0
flask only

## test in local
flask run --host=0.0.0.0 --port=8080


## how to run this app
docker run -ti --name lhflask --rm -p 3389:80 ywllyht/lhflask:1.0 bash
docker run -d --name lhflask --rm -p 3389:80 ywllyht/lhflask:1.0 bash


## reference link
https://zhuanlan.zhihu.com/p/78432719

