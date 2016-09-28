################################################
#		  Default Configuration				   #
################################################

TIME_ZONE = 'US/Pacific'
ALLOWED_HOSTS = [ '*' ]
MEMCACHE_HOSTS = ['127.0.0.1:11211']
MEMCACHE_KEY_PREFIX = 'graphite'
LOG_METRIC_ACCESS = False
DEFAULT_CACHE_DURATION = 60 # Cache images and data for 1 minute
DEFAULT_CACHE_POLICY = [(0, 60), # default is 60 seconds
                        (7200, 120), # >= 2 hour queries are cached 2 minutes
                        (21600, 180)] # >= 6 hour queries are cached 3 m

CLUSTER_SERVERS = []
CARBONLINK_HOSTS = [
        "127.0.0.1:7102:a",
        "127.0.0.1:7202:b",
        "127.0.0.1:7302:c",
        "127.0.0.1:7402:d",
        "127.0.0.1:7502:e",
        "127.0.0.1:7602:f",
        "127.0.0.1:7702:g",
        "127.0.0.1:7802:h"
        ]
CARBONLINK_TIMEOUT = 7.0
#CARBONLINK_RETRY_DELAY = 15 # Seconds to blacklist a failed remote server
#CARBONLINK_RETRY_DELAY = 1 # Seconds to blacklist a failed remote server
REPLICATION_FACTOR = 1

REMOTE_RENDERING = False
CARBONLINK_QUERY_BULK = True

# specification as the old database specification style is removed in 1.4
DATABASES = {
    'default': {
        'NAME': 'graphite',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'graphite',
        'PASSWORD': 'graphite',
        'HOST': '127.0.0.1',
        'PORT': '3306'
    }
}

SECRET_KEY = 'YOUR_SECRET_KEY'
MAX_FETCH_RETRIES = 2


# Set URL_PREFIX when deploying graphite-web to a non-root location
URL_PREFIX = '/graphite'



