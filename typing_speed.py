import time
import random as r

def mistake(partest,usertest):
    error=0
    for i in range(len(partest)):
        try:
            if partest[i]!=usertest[i]:
                error=error+1
        except :
            error=error+1
    return error


def speed_time(time_s,time_e,userinput):
    time_delay=time_e-time_s
    time_R=round(time_delay,2)
    speed=len(userinput)/time_R
    return round(speed)



SENTENCES = [
    "The quick brown fox jumps over the lazy dog.",
    "Typing fast requires practice and patience.",
    "Code every day to become a better programmer.",
    "Artificial intelligence is shaping the future.",
    "Debugging is twice as hard as writing the code in the first place."
]

test1=r.choice(SENTENCES)
print("****** typing speed*******")
print(test1)
time_1=time.time()
testinput=input("Enter: ")
time_2=time.time()

print("Speed : ",speed_time(time_1,time_2,testinput)," w/sec")
print("Error : ",mistake(test1,testinput))
