#README

用于WINDOWS获取CPU进程信息，主要针对内存

用法：
getProcessMem.exe *间隔时间*  *次数*  输出目录

返回的文件信息依次为
- 时间
- PID
- PNAME
- rss
- vms
- num_page_faults
- peak_wset,wset
- peak_paged_pool
- paged_pool
- peak_nonpaged_pool
- nonpaged_pool,pagefile
- pagefile
- private
- memory_percent
- cpu_percent
- cpu_times
- cpu_times
- status
- cmd line

[参考](http://pythonhosted.org/psutil/#psutil.Process.memory_info)

|Linux  | OSX   | BSD   | Solaris | Windows                 |
|:-----:|:-----:|:-----:|:-------:|:-----------------------:|
|rss    | rss   |rss    | rss     | rss(alias for wset)     |
|vms    | vms   |vms    | vms     | vms (alias for pagefile)|
|shared |pfaults| text  |         | num_page_faults         |
|text   |pageins| data  |         | peak_wset               |
|lib    |       | stack |         | wset                    |
|data   |       |       |         |peak_paged_pool          |
|dirty  |       |       |         |paged_pool               |
|       |       |       |         |peak_nonpaged_pool       |
|       |       |       |         |nonpaged_pool            |
|       |       |       |         |pagefile                 |
|       |       |       |         |peak_pagefile            |
|       |       |       |         |private                  |

- rss: aka “Resident Set Size”, this is the non-swapped physical memory a process has used. On UNIX it matches “top“‘s RES column (see doc). On Windows this is an alias for wset field and it matches “Mem Usage” column of taskmgr.exe.
- vms: aka “Virtual Memory Size”, this is the total amount of virtual memory used by the process. On UNIX it matches “top“‘s VIRT column (see doc). On Windows this is an alias for pagefile field and it matches “Mem Usage” “VM Size” column of taskmgr.exe.
- shared: (Linux) memory that could be potentially shared with other processes. This matches “top“‘s SHR column (see doc).
- text (Linux, BSD): aka TRS (text resident set) the amount of memory devoted to executable code. This matches “top“‘s CODE column (see doc).
- data (Linux, BSD): aka DRS (data resident set) the amount of physical memory devoted to other than executable code. It matches “top“‘s DATA column (see doc).
- lib (Linux): the memory used by shared libraries.
- dirty (Linux): the number of dirty pages.
- pfaults (OSX): number of page faults.
- pageins (OSX): number of actual pageins.