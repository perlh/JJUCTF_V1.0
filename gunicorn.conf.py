workers = 5   #定义同时开启的处理请求的进程数量，根据网站流量适当调整
worker_class = "gevent"
bind = "0.0.0.0:80"
