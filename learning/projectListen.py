# 抓包
import pcap
import dpkt
a=pcap.pcap()
a.setfilter('tcp port 80')  #过滤功能，可以设置需要显示的
for i,j in a:
       tem=dpkt.ethernet.Ethernet(j)
       print('%s %x',i,tem)
