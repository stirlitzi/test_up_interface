import subprocess
import os
#from crontab import CronTab

class Addroute():
    def __init__(self):
        pass
    def ex_route(self):
        self.interface = 'ens33:'
        self.cmd = 'ip a'
        self.result = subprocess.check_output(self.cmd, stderr=subprocess.STDOUT, shell=True)
        if self.interface in str(self.result):
            try:
                os.system('sudo ip r add 192.168.0.0/24 via 192.168.0.1')
                print('Route added')
                #my_cron = CronTab(user='sdds')
                #job = my_cron.new(command='python /home/sdds/test.py')
                #job.minute.every(1)
                #my_cron.write()
            except OSError as err:
                print(err)
        else:
            print('Interface with the name %s is not present in the ip route. Route was not added!' % self.interface)
if __name__ == 'main':
    Addroute().ex_route()


