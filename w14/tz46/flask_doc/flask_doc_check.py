import redis


r = redis.StrictRedis(host='localhost', port=6379)

llen = r.llen('flask_doc:items')

assert llen >= 70
