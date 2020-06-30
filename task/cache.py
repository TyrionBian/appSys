import redis
import os

redis_host = os.environ['REDIS_HOST']
redis_port = 6379
redis_password = ""

def write_redis(key, value):
    try:
    
        # The decode_repsonses flag here directs the client to convert the responses from Redis into Python strings
        # using the default encoding utf-8.  This is client specific.
        r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
    
        # step 4: Set the hello message in Redis 
        r.set(key, value)       
    
    except Exception as e:
        print(e)

def get_redis(key):  
    try:
        # The decode_repsonses flag here directs the client to convert the responses from Redis into Python strings
        # using the default encoding utf-8.  This is client specific.
        r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
    
        msg = r.get(key)     
        return(msg)  
    
    except Exception as e:
        print(e)

