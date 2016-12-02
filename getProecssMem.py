# -*- coding: utf-8 -*-

"""
返回进程的内存使用情况
时间,PID,PNAME,
--内存信息--
rss,vms,num_page_faults, peak_wset,wset, peak_paged_pool, paged_pool, peak_nonpaged_pool, nonpaged_pool,pagefile, pagefile, private,
--然后是
memory_percent, cpu_percent，
--然后是
cpu_times, cpu_times,进程状态，命令行

"""

import psutil
import sys
# import json
# import os
import time

proclist = []
waitsec = 60


def getProcessMem(pid):
    proc = psutil.Process(pid)
    # total = psutil.virtual_memory().total

    # print "total: %.2f(M)" % (float(total) / 1024 / 1024)
    a = proc.memory_info()
    s = '%0.2f,%0.2f,%0.2f,%0.2f,%0.2f,%0.2f,%0.2f,%0.2f,%0.2f,%0.2f,%0.2f,%0.2f,%0.2f' % (
        proc.memory_percent(), a.rss / 1024 / 1024, a.vms / 1024 /
        1024, a.num_page_faults, a.peak_wset, a.wset, a.peak_paged_pool,
        a.paged_pool, a.peak_nonpaged_pool, a.nonpaged_pool,
        a.pagefile, a.pagefile, a.private)
    return s


def getAll():
    s = []
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'cmdline',
                                        'memory_info', 'memory_percent',
                                        'cpu_percent', 'cpu_times', 'status'])
        except psutil.NoSuchProcess:
            pass
        else:
            if not proclist or pinfo['name'] in proclist:
                t = '%s,%d,%s,'
                t = t + '%0.2f,%0.2f,%0.2f,%0.2f,%0.2f,%0.2f,%0.2f,%0.2f,%0.2f,%0.2f,%0.2f,%0.2f,'
                t = t + '%0.2f,%0.2f,'
                t = t + '%0.2f,%0.2f,'
                t = t + '%s,%s'
                a = pinfo['memory_info']
                if pinfo['cmdline'] and isinstance(pinfo['cmdline'], list):
                    cl = ' '.join(pinfo['cmdline'])
                else:
                    cl = str(pinfo['cmdline'])

                t = t % (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),
                         pinfo['pid'], pinfo['name'],

                         a.rss, a.vms, a.num_page_faults, a.peak_wset,
                         a.wset, a.peak_paged_pool, a.paged_pool,
                         a.peak_nonpaged_pool, a.nonpaged_pool,
                         a.pagefile, a.pagefile, a.private,

                         pinfo['memory_percent'], pinfo['cpu_percent'],

                         pinfo['cpu_times'].user, pinfo['cpu_times'].system,

                         pinfo['status'], cl
                         )
                # print t
                # minfo = getProcessMem(pinfo['pid'])
                s.append(t)
    return s


if __name__ == '__main__':
    try:
        waitsec = int(sys.argv[1])
        count = int(sys.argv[2])
        filepath = str(sys.argv[3])
    except Exception as e:
        waitsec = 1
        count = 1
    lgnm = filepath + '\processUseMem_' + \
        time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())) + '.txt'
    # print lgnm
    log = open(lgnm, 'w+')
    for i in range(count):
        info = getAll()
        for a in info:
            log.write(a + '\n')
        log.flush()
        time.sleep(waitsec)
    log.close()

    '''
    if len(sys.argv) == 1
        waitsec = 60

    # 如果有两个参数，并且参数在命令列表中，则执行mainwork
    if len(sys.argv) == 3 and in CMD_LIST:
        cmd_type = sys.argv[2]
        cmd_cfg = sys.argv[1]
        mainwork(cmd_type, cmd_cfg, showStatus=False)
    if
    if os.path.exists('pm.cfg'):
        f = open('pm.cfg')
        js = f.read()
        try:
            cfg = json.loads(js)
            if 'proclist' in cfg.keys():
                proclist = cfg['proclist']
            if 'waitsec' in cfg.keys():
                waitsec = cfg['waitsec']
        except Exception, e:
            print(str(e))
        finally:
            f.close()

    else:
        print 'config file:%s not found' % ('pm.cfg')
    '''
