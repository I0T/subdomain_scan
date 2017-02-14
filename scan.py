#!/usr/bin/env python
# -*-coding: utf-8-*-
# @Time    : 17/2/14
# @Author  : IOT
# @File    : scan.py

import socket

import gevent
from gevent.pool import Pool
from gevent import monkey
monkey.patch_all()

def get_ip(url):
    try:
        ips_socket = socket.getaddrinfo(url,0,2,0,6,0)
        if len(ips_socket) != 1:
            ip = 'not_real %s'% ips_socket[-1][-1][0]
        else:
            ip = ips_socket[-1][-1][0]
        url_and_ip = '%s %s' % (url, ip)
        print(url_and_ip)
    except:
        1
def run(urls):
    pool = Pool(30)
    jobs = [pool.spawn(get_ip,url) for url in urls]
    gevent.wait(jobs)
if __name__ == "__main__":
    domain = 'google.com'
    url_0 = '%s'%(domain.split('.')[0])
    urls_0 = ['%sadmin'%url_0,'%smanage'%url_0,'%shoutai'%url_0,'%sguanli'%url_0]+\
             ['%s%s'%(url_0,num) for num in range(1000)]
    urls = urls_0 + ['%s.%s'%(url_0.strip('\n'),domain) for url_0 in open('dic.txt').readlines()]
    run(urls)
