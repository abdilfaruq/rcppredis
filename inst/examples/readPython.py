#!/usr/bin/env python

import redis

redishost  = "localhost"
redisserver = redis.StrictRedis(redishost)

key1 = "ex:simpleString"
val1 = redisserver.get(key1)
print "Got", val1, "from", key1

key2 = "ex:scalarVal"
val2 = redisserver.lpop(key2)
print "LPop'ed", val2, "from", key2

key3 = "ex:vectorVal"
val3 = redisserver.lpop(key3)
print "LPop'ed", val3, "from", key3
