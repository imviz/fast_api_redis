# simple fast api redis setup
**Redis installation**
#
`sudo apt install redis-server`
#
`sudo systemctl enable redis-server`
#
`sudo service redis-server start`
#
`sudo systemctl status redis`

**Testing of Redis works correctly**
#
###### got to redis terminal
`redis-cli`
#
type `ping` in terminal  then get `PONG`
#
type `set test "It's working!"` in terminal then get `Ok` 
#
type `get test` then get `"It's working!"`
###### then the installation set up completed
#
#
***How to use this simple project in your system***
#
Git clone using `https://github.com/imviz/fast_api_redis`
#
install all packages using `pipenv install` command
#
 run the script using `python main.py`
#
you can check the cache is working correctly 
# 
 go to `redis-cli`
#
`keys *` replace `*` with which key you want
#
