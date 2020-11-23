import random
import datetime
import time

#Random Stream generator
#Scema of Expected File - Source, Username,Amount

sources = ['imps', 'neft', 'googlepay', 'phonepay', 'amazon']
usernames = ['vasu','nagbhushan', 'rohit', 'kishor', 'bhagya', 'aanya']
count = 0
records = []
while True:
            
    medium = random.choice(sources)
    user = random.choice(usernames)
    amt = random.randint(1000, 10000)

    valueString = medium+ ',' + user + ','+ str(amt)
    
    #print(timestamp)
    #print(valueString)
    if( count == 20):
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        with open("trans_log_"+str(timestamp)+".csv","a") as f:
            for record in records:
                print(record)
                f.write(str(timestamp)+","+record+"\n")
            f.close()   
        time.sleep(15)
        count = 0
        records=[]
    else:
        count+=1
        records.append(valueString)


