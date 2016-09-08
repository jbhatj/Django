from script import choose_qos_sm,fetch_details
import telnetlib
import time
from .models import Machine,Machine_sjc1,Machine_dfw1,Machine_iad1
def formating(l,name) :
    machines = { 'iad1' : Machine_iad1, 'sjc1' : Machine_sjc1, 'dfw1' : Machine_dfw1 }
    l =[ [int(j) for j in i.split('\x01')[1:]] for i in l.split('\n')[2:-2] ]
    for i in l :
        machine = machines[name](bucket_time=i[0],total_rules=i[1])
        machine.save()

def do_connection(from_time,to_time,time_per_unit,product,cube_type) :# arguments :(host,port),from_time,to_time,time_in=60(i.e set to per minute by default),
    port = "8159"
    hosts   = ["adbq1.other.dfw1.dna.akamai.com","adbq1.other.iad1.dna.akamai.com","adbq1.other.sjc1.dna.akamai.com" ]
    cube_id =  choose_qos_sm(product,cube_type)
    for host in hosts :
        try :
            connection = telnetlib.Telnet(host,port,timeout=10)
            time_now = int(time.time())
            string = "Select time - ((time - %s) %% %d) as time_1_min_bucket,sum(num_denied)+sum(num_warned)+0 as total_rules From qos.100154.288 Duration time >= %s and time <= %s Group By 1 Order By 1 ASC offset 0 with '{\"redirection\":\"off\"}' ;\n"%(from_time,time_per_unit,from_time,to_time)

            connection.write(string)
            l = connection.read_all()
            m_name = host.split('.')[2]
            formating(l,m_name)
         #   with open(file_name,"w") as f :
         #       f.write(l)
            print "connection successfull"
        
            connection.close()
        except   :
            print "something went wrong while querying %s  and the error message is "%(host)

