import time 
startime = time.time()
for i in range(0.5):
    print(i)
    time.sleep(1)
endTime = time.time()
elaspedTime = endTime - startime
print("Elasped Time= %s" % elaspedTime)