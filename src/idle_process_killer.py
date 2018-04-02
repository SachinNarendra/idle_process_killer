import datetime as _datetime
import os as _os
import psutil as _psutil
import subprocess as _subprocess
import threading as _threading

B = 0
KB = 10
MB = 20
GB = 30
TB = 40

# Wait period between two subsequent checks in seconds
_IDLE_CHECK_WAIT_TIME = 60 * 0.25

_IDLE_CHECK_START_TIME = 9


def get_memory_usage(pid, unit=MB):
    # 10 / 1,024 / 1KB
    # 20 / 1,048,576 / 1 MB ...

    process = _psutil.Process(pid)
    mem = process.memory_info()[0] / float(2 ** unit)
    return mem


def get_pid_list(name):
    pids = _subprocess.check_output(["pidof", name]).split(" ")
    return [int(_pid) for _pid in pids if _pid.isdigit()]


class ProcessIdleChecker(_threading.Thread):
    def __init__(self, pid):
        self._pid = pid

        current_time = _datetime.datetime.now()
        dir(current_time.hour)

    def run(self):
        pass


if __name__ == "__main__":
    process_ids = get_pid_list('Python')
    print process_ids
    for process_id in process_ids:
        print "%s : %s" % (process_id, get_memory_usage(process_id, MB))
