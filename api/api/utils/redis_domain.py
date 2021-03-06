import redis

redis_server = redis.StrictRedis('localhost')
publish = redis_server.pubsub()
redis_domains = "Domains"
template_directory = "/home/sangm/templates"
nginx_directory = "/home/sangm/subdomains"

def redis_get_domains():
    return redis_server.lrange(redis_domains, 0, -1)
def redis_insert_domain(domain):
    if redis_server.hgetall(domain):
        return False
    else:
        redis_server.lpush(redis_domains, domain)
        redis_server.publish('DomainChannel', domain)
        return redis_server.hmset(domain, {'ServerName': domain,
                                           'Template' : template_directory,
                                           'Nginx': nginx_directory})
def redis_delete_domain(domain):
    result = redis_server.hdel(domain, 'ServerName')
    result |= redis_server.hdel(domain, 'Directory')
    result |= redis_server.lrem(redis_domains, 1, domain)
    return result
