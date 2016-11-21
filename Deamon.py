# *.* coding: utf-8 *.*
import os
import sys
import atexit
import logging,time
from signal import SIGTERM


class Daemon(object):
    def __init__(self, pidfile='/tmp/Goldedging.pid', logfile='/tmp/Goldedging/log',
                 logname='Goldedging', loglevel='logging.INFO', eventlevel='logging.INFO'):
        self.pidfile = pidfile
        self.logfile = logfile
        self.logname = logname
        self.loglevel = loglevel   #loglevel = 'logging.INFO/logging.DEBUG'
        self.evtlevel = eventlevel  #eventlevel = 'logging.INFO/logging.DEBUG'


    def _set_Logging_attr(self):
        logger = logging.getLogger(self.logname)
        logger.setLevel(self.loglevel)
        event_fh = logging.FileHandler(self.logfile)
        event_fh.setLevel(self.evtlevel)
        formatter = logging.Formatter('%(name)s - %(levelname)s  %(message)s')
        event_fh.setFormatter(formatter)
        logger.addHandler(event_fh)
        return logger


    def _daemonize(self):
        try:
            pid = os.fork()
            if pid > 0:
                sys.exit(0)
        except OSError as e:
            with open(self.logfile,'w+') as fp:
                fp.write('fork #1 failed: %d (%s)\n' % (e.errno, e.strerror))
            sys.exit(1)
        os.chdir("/")
        os.setsid()
        os.umask(0)
        try:
            pid = os.fork()
            if pid > 0:
                sys.exit(0)
        except OSError as e:
            with open(self.logfile,'w+') as fp:
                fp.write('fork #2 failed: %d (%s)\n' % (e.errno, e.strerror))
            sys.exit(1)
        atexit.register(self.del_pid)
        pid = str(os.getpid())
        with open(self.pidfile, 'w+') as f:
            f.write('%s\n' % pid)


    def del_pid(self):
        os.remove(self.pidfile)


    def start_deamon(self):
        try:
            with open(self.pidfile,'r') as start_fp:
                pid = int(start_fp.read().strip())
        except IOError:
            pid = None
        if pid:
            message = 'pidfile %s already exist. Daemon already running!\n'
            with open(self.logfile, 'w+') as start_fp:
                start_fp.write(message % self.pidfile)
            sys.exit(1)
        self._daemonize()
        self._run()


    def stop_deamon(self):
        try:
            with open(self.pidfile,'r') as stop_fp:
                pid = int(stop_fp.read().strip())
        except IOError:
            pid = None
        if not pid:
            message = 'pidfile %s does not exist. Daemon not running!\n'
            with open(self.logfile, 'w+') as stop_fp:
                stop_fp.write(message % self.pidfile)
            return
        try:
            while 1:
                os.kill(pid, SIGTERM)
                time.sleep(0.1)
        except OSError as err:
            err = str(err)
            if err.find('No such process') > 0:
                if os.path.exists(self.pidfile):
                    os.remove(self.pidfile)
            else:
                print(str(err))
                sys.exit(1)


    def restart_deamon(self):
        self.stop_deamon()
        self.start_deamon()

    def _run(self):
        """
            > function which you want run under a deamon process
        """
        print("Time : %s" % time.ctime())
        time.sleep(1)


if __name__ == "__main__":
    deamon = Daemon()
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print('unknown command')
            sys.exit(2)
        sys.exit(0)
    else:
        print('usage: %s start|stop|restart' % sys.argv[0])