import os,csv,uuid

def fetch_details(command) : 

    os.system(command)

    with open("file.csv") as csvfile :
        dic={}
        reader = csv.DictReader(csvfile)
        for row in reader :
            if row["analyzerid"].isdigit() :
                dic[row["analyzerid"]] = {"analyzername" : row["analyzername"]}#,"analyzertype" : row["analyzertype"] }
 #       for key in sorted(dic.keys(),key=int) :
 #           print key,dic[key]["analyzername"]#,dic[key]["analyzertype"]
#    a = raw_input("do you want to fetch details\npress enter to yes\ntype any char to no")
#    if a == '' :
        ch = raw_input("Enter the analyzerid")
        if ch not in dic.keys() :
            print "analyzerid doesnt exist"
        else :
            return ch


def choose_qos_sm(product,cube_type) :
    command = 'sql2 --csv --output=file.csv -q internal.dev.query.akadns.net "select analyzerid,analyzername from analytics_info where analyzertype=\'clientside_qos1_%s\' group by 1,2 order by 1 ";'
    choices_ci  = { "sm" : {"c_c" : "288", "t_c" : "298"}, "vod" : {"c_c":"137","t_c":"138"} ,"live" : { "c_c" :"136", "t_c" : "139" }}
    command=command % product
    #print command
    #fetch_details(command)

    cube_id=choices_ci[product][cube_type]

    return cube_id

def generate_unique_id() :
    return uuid.uuid4()
    
