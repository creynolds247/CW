
Acivity=['Swim','Bike','Running']
speed=[1.77,14.66,5.1]
distance=[]
clothing=['Cycling Shoes','Running Shoes','Flippers','Swimming Goggles','Sunglasses']

Cycling_Shoes=[-0.1,0.12,-0.25]
Running_Shoes=[-0.02,0.04,0.25]
Flippers=[0.6,-0.05,-0.3]
Swimming_Goggles=[0.35,-0.08,-0.12]
Sunglasses=[-0.1,0.08,0.05]

Swimming=[-0.1,-0.02,0.6,0.35,-0.1]
Cycling=[0.12,0.04,-0.05,-0.08,0.08]
Running=[-0.25,0.25,-0.3,-0.12,0.05]



def input():
    for i in range(len(Acivity)):
        distance.append(float(raw_input("Disance for "+Acivity[i])))
        if distance[i]<0:

            print "Error disance cannot be less than 0"
            exit(0)


def Display():

    print "======"*8

def Calculation(disance,speed,modifier):
    modifier=1.0-modifier
    Time=float((disance/speed)*modifier)
    #print disance,speed,modifier,Time
    return Time


def Clothing_modifyer_finder(Clothing,Acivity):
    Clothing=0

    return Clothing


def Main():
    input()

    print "         Clothing              Time Taken (s)"
    Display()

    time=[]
    Name_clothing_max=''
    Name_clothing_min=''

    for i in range(len(clothing)):
        tmp_time=0
        for x in range(len(Acivity)):
            if x==0:
                tmp_time = tmp_time+Calculation(float(distance[x]), float(speed[x]),Swimming[i])

            if x==1:
                tmp_time = tmp_time+Calculation(float(distance[x]), float(speed[x]),Cycling[i])

            if x==2:
                tmp_time = tmp_time+Calculation(float(distance[x]), float(speed[x]),Running[i])

        time.append(tmp_time)
        print "%17s %20.2f"%(clothing[i],tmp_time)
    #Names for Clothing with largest and smallest
    for i in range(len(clothing)):
        if time[i]==max(time):
            Name_clothing_max=clothing[i]
        elif time[i]==min(time):
            Name_clothing_min=clothing[i]


    print "Smallest =",Name_clothing_min,round(min(time),2),"(s)",Name_clothing_max," Largest =",round(max(time),2),"(s)"





Main()