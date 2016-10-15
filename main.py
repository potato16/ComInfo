import sys, platform, math
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction
from PyQt5.uic import loadUi
import cpuinfo, psutil, netifaces

class MyMain(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('design.ui',self)
        self.lblosi.setText("Go Away!")
        self.actionGet_Information.triggered.connect(self.getinfo)

    #get info then show it up
    def getinfo(self):
        #get computer name
        self.lblcomnamei.setText(platform.node())
        # get os
        self.lblosi.setText(platform.platform())
        #get processors
        self.lblcpui.setText(cpuinfo.get_cpu_info()['brand'])
        #get Disk storage info
        self.lbldiski.setText(self.getstorage())
        # get Ram storage
        self.lblrami.setText(self.getRam())
        # get ipv4 address
        self.lbllanipi.setText(self.getLanIPv4())
        pass
    def getLanIPv4(self):
        #Using netifaces
        # 2 is AF_INET
        # 30 is AF_INET6 (IPv6)
           #  help(netifaces)
        l_interfaces = netifaces.interfaces()
        for item in l_interfaces:
            netifaces.ifaddresses(item)
        
        
    def getRam(self):
        total = psutil.virtual_memory().total
        return "%.0f"%(math.ceil(total*(1e-9))) + " GB"
    def getstorage(self):
        
        total =0
        ltmp = psutil.disk_partitions()
       
        for i in ltmp:
            if i.fstype is not '':
                try:
                    total += psutil.disk_usage(i.mountpoint).total
                except:
                    print("Oops, I did not see that coming! Sorry!")
        
        return str("%.0f"%(math.ceil(total*(1e-9)))) +" GB"
     


if __name__ == '__main__' :
    
    app = QApplication(sys.argv)
    w = MyMain()
    w.show()
    sys.exit(app.exec_())


