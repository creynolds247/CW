id=['Swim','Bike','Running'] # List of sport disciplines
speed=[1.72,14.66,5.1]
distance=[]
timetaken=[]
total_time=[]
racetotal=[]
# List to store data for calculations and print functions


clothing=['Cycling Shoes','Running Shoes','Flippers']
eye_wear=['Swimming Goggles', 'Sunglasses']

#2 separate lists for equipment and eyewear 

combo=[] # Combo is an empty list that is to be populated on each iteration of the calcuation loop

iterations = len(clothing)*len(eye_wear) #The number of loops performed is directly related to the number of equipment combinations

Cycling_Shoes=[0.9,1.12,0.75]
Running_Shoes=[0.98,1.04,1.25]
Flippers=[1.6,0.95,0.7]
Gog=[0.35,-0.08,-0.12]
Sun=[-0.1,0.08,0.05]

# Lists storing numerical values for % change in speed. 

modifier = Cycling_Shoes + Running_Shoes + Flippers #Variable defined & used to store the variables used in future calculations





def input(): #First function defined to make altering distances of the race more user friendly
   distance.append(1500)
   distance.append(40000)
   distance.append(10000)

def Display(): #Print function used to make main function code cleaner

    print "======"*3

def Calculation(distance,speed,modifier,eyewear):
    Time=float(distance/((speed*modifier)+(speed*eyewear))) #Calcuations for total time taking
    return Time



def Main():
    input()
    racetotal=[]
    

    for i in range(len(id)):
        print
        print "For",id[i],"distance you entered",distance[i],"Metres"
    print "\n "*3

    for i in range (len(id)):
        print "Equipment Combination: %5s and %5s "%(clothing[i], eye_wear[0])
        combo.append(clothing[i]+' and '+eye_wear[0]) #Ammending combo list with single terms of combinations
        print
        print "Discipline           Time Taken (s)"
        print
        z=i*3 #Variable used to determine position in modifier list to reduce number of for loops required in program
        
        
        del timetaken[:] #Command to empty timetaken list on each iteration to use this temporary list for calculations
        
        
       

        
        for t in range(len(id)):
                 
                tmp=Calculation(float(distance[t]), float(speed[t]), float(modifier[z+t]), float(Gog[t]))
                
                timetaken.append(tmp)
                racetotal=sum(timetaken)
                
                
                print "%10s %20.2f"%(id[t],tmp)
        
        total_time.append(racetotal)
       
        print ""
        print "The total race time is: %5.2f seconds."%(racetotal)        

        print "\n" *2
          
        

        
    for i in range (len(id)):
        print "Equipment Combination: %5s and %5s "%(clothing[i], eye_wear[1])
        combo.append(clothing[i]+' and '+eye_wear[1])
        print
        print "Discipline           Time Taken (s)"
        print
        z=i*3
        
        del timetaken[:]
        
        
              

        
        for t in range(len(id)):

                
                tmp=Calculation(float(distance[t]), float(speed[t]), float(modifier[z+t]), float(Sun[t]))
                
                timetaken.append(tmp)
                racetotal=sum(timetaken)
                
                
                
                print "%10s %20.2f"%(id[t],tmp)
        
        total_time.append(racetotal)
        
       
        
        print ""
        print "The total race time is: %5.2f seconds."%(racetotal)
        print "\n"*2
 

               
                
        



    print ""
    print ""
    
    print "Johnny will take: %5.2f seconds to complete the race in the fastest combination." %(min(total_time))


    sort=total_time.index(min(total_time)) 
    print "The fastest combination is: %s" %(combo[sort]) # Designed to link the position in list of the fastest time and the associated combination
    


Main()
