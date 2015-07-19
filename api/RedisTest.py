import redis
import unittest
from api import app
from api.utils import redis_get_domains, redis_insert_domain, redis_delete_domain

class RedisTest(unittest.TestCase):
    def setUp(self):
        # Should set up a test redis database
        self.redis_server = redis.StrictRedis('localhost')
        self.redis_server.flushall()
        # self.publish = self.redis_server.pubsub()
        # self.publish.subscribe('DomainChannel')
        redis_insert_domain('test1')
        redis_insert_domain('test2')
        redis_insert_domain('test3')
        self.domains = redis_get_domains()
    def test_redis_server_connects_successfully(self):
        self.assertTrue(self.redis_server)
    def test_redis_gets_all_existing_domains(self):
        # test1, test2, test3 has been inserted when tests are set
        self.assertEqual(3, len(self.domains))
    def test_insert_and_delete_domain(self):
        result = redis_delete_domain('test1')
        self.assertTrue(result)
        self.assertEqual(2, len(redis_get_domains()))
    def test_insert_domain_does_not_allow_duplicates(self):
        # test1 is already in the database
        self.assertFalse(redis_insert_domain('test1'))
    def test_insert_domain_publishes_to_channel_domains(self):
        pass

if __name__ == '__main__':
    unittest.main()
