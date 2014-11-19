import socket
import time
import json
import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s\t Thread-%(thread)d -%(message)s", filename='/tmp/gmond-twemproxy.log', filemode='w')
logging.debug('starting up')

# IPAndPort = "192.168.28.192:6379"
# return 192
def getIPName(IPAndPort):
    return IPAndPort.split('.')[3].split(':')[0]
    
def metric_handler(name):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        s.connect((metric_handler.host,metric_handler.port))
        s.send('GET %s HTTP/1.0\r\n\r\n' % metric_handler.url)
        info = s.recv(4096)
        metric_handler.info = {}
        twemproxy_info = json.loads(info)
        for (k,v) in twemproxy_info.items():
            if k in metric_handler.poollist: #pool name 1
                for (k_,v_) in v.items():
                    if k_ in metric_handler.nodelist: #redis server name
                        for (k2_,v2_) in v_.items():
                            k2_ = k + '_' + getIPName(k_) + '_' + k2_
                            if k2_ in metric_handler.descriptors:
                                metric_handler.info[k2_] = int(v2_)
                    else:
                        k_ = k + '_' + k_
                        if k_ in metric_handler.descriptors:
                            metric_handler.info[k_] = int(v_)
                        
    except Exception,e:
        logging.error(e)
        pass

    s.close()
    return metric_handler.info.get(name,0)

def metric_init(params):
    metric_handler.host = params['host']
    metric_handler.port = int(params['port'])
    metric_handler.url = params['url']
    metric_handler.timestamp = 0
    metric_handler.poollist = params['pool-list'].split(',')
    metric_handler.nodelist = params['node-list'].split(',')

    metric_alpha = {
        "alpha_client_connections":{"units":"counts","value_type":"int","format":"%d"},
        "alpha_server_ejects":{"units":"counts","value_type":"int","format":"%d"},
        "alpha_forward_error":{"units":"counts","value_type":"int","format":"%d"},
        "alpha_client_err":{"units":"counts","value_type":"int","format":"%d"},
        "alpha_client_eof":{"units":"counts","value_type":"int","format":"%d"},
        "alpha_191_requests":{"units":"counts","value_type":"int","format":"%d"},
        "alpha_191_request_bytes":{"units":"counts","value_type":"int","format":"%d"},
        "alpha_191_responses":{"units":"counts","value_type":"int","format":"%d"},
        "alpha_191_response_bytes":{"units":"counts","value_type":"int","format":"%d"},
        "alpha_192_requests":{"units":"counts","value_type":"int","format":"%d"},
        "alpha_192_request_bytes":{"units":"counts","value_type":"int","format":"%d"},
        "alpha_192_responses":{"units":"counts","value_type":"int","format":"%d"},
        "alpha_192_response_bytes":{"units":"counts","value_type":"int","format":"%d"},
        "beta_client_connections":{"units":"counts","value_type":"int","format":"%d"},
        "beta_server_ejects":{"units":"counts","value_type":"int","format":"%d"},
        "beta_forward_error":{"units":"counts","value_type":"int","format":"%d"},
        "beta_client_err":{"units":"counts","value_type":"int","format":"%d"},
        "beta_client_eof":{"units":"counts","value_type":"int","format":"%d"},
        "beta_192_requests":{"units":"counts","value_type":"int","format":"%d"},
        "beta_192_request_bytes":{"units":"counts","value_type":"int","format":"%d"},
        "beta_192_responses":{"units":"counts","value_type":"int","format":"%d"},
        "beta_192_response_bytes":{"units":"counts","value_type":"int","format":"%d"}
    }

    metric_handler.descriptors = {}

    for name,updates in metric_alpha.iteritems():
        descriptor = {
            "name":name,
            "call_back":metric_handler,
            "time_max":90,
            "units":"",
            "slope":"both",
            "description":"twemproxy cluster's stats info",
            "groups":"twemproxy"
        }

        descriptor.update(updates)
        metric_handler.descriptors[name] = descriptor


    return metric_handler.descriptors.values()

def metric_cleanup():
    pass

if __name__ == '__main__':
    descriptors = metric_init({})
    for d in descriptors:
        v = d['call_back'](d['name'])
        print 'value for %s is %u' % (d['name'],  v)