#Scan the java log4j app logs and print logs per java class file
#This is to determine check java files have logs in abundance, we can then revisit the java files to improvise logs


import os, re

 

logpath="/opt/middleware/tomcat/instances/cloudapp/logs"

clazcount = {}

for file in os.listdir(logpath):

        if re.match(r'CreditpackageApp.log*',file):

                logfile = open(os.path.join(logpath,file),'r')

                for line in logfile:

                        if re.match(r'^[0-9]+-[0-9]+-[0-9]+',line):

                                try:

                                        #claz = line.split("]")[1].split()[0]

                                        claz = re.split("User=",line)[0].split()[-2:-1][0]

                                        #if claz.find("http") >= 0: print file,line

                                        if claz in clazcount:

                                                clazcount[claz] += 1

                                        else:

                                                clazcount[claz] = 1

                                except:

                                        print file, ":error while processing", line

for classkey in clazcount:

        print classkey

 

for count in clazcount.values():

        print count
