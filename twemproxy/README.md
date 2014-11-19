ganglia-twemproxy -- twemproxy in Ganglia
=========================================


## SYNOPSIS

1. modify `metric_alpha` in `twemproxy.py` 
2. modify parameters in `twemproxy.pyconf`
Then, place `twemproxy.py` and `twemproxy.pyconf` in the appropriate directories and restart `gmond`. Enjoy it!

## DESCRIPTION

Read twemproxy metrics.

## Metircs

sample:
{
    "service": "nutcracker", 
    "source": "host191", 
    "version": "0.2.4", 
    "uptime": 16, 
    "timestamp": 1415942266, 
    "beta": {
        "client_eof": 0, 
        "client_err": 0, 
        "client_connections": 0, 
        "server_ejects": 0, 
        "forward_error": 0, 
        "fragments": 0, 
        "192.168.28.192:6379": {
            "server_eof": 0, 
            "server_err": 0, 
            "server_timedout": 0, 
            "server_connections": 0, 
            "requests": 0, 
            "request_bytes": 0, 
            "responses": 0, 
            "response_bytes": 0, 
            "in_queue": 0, 
            "in_queue_bytes": 0, 
            "out_queue": 0, 
            "out_queue_bytes": 0
        }
    }, 
    "alpha": {
        "client_eof": 0, 
        "client_err": 0, 
        "client_connections": 0, 
        "server_ejects": 0, 
        "forward_error": 0, 
        "fragments": 0, 
        "192.168.28.191:6379": {
            "server_eof": 0, 
            "server_err": 0, 
            "server_timedout": 0, 
            "server_connections": 0, 
            "requests": 0, 
            "request_bytes": 0, 
            "responses": 0, 
            "response_bytes": 0, 
            "in_queue": 0, 
            "in_queue_bytes": 0, 
            "out_queue": 0, 
            "out_queue_bytes": 0
        }, 
        "192.168.28.192:6379": {
            "server_eof": 0, 
            "server_err": 0, 
            "server_timedout": 0, 
            "server_connections": 0, 
            "requests": 0, 
            "request_bytes": 0, 
            "responses": 0, 
            "response_bytes": 0, 
            "in_queue": 0, 
            "in_queue_bytes": 0, 
            "out_queue": 0, 
            "out_queue_bytes": 0
        }
    }
}

## AUTHOR

Chen Tao <dintau@126.com>