from datetime import datetime
import csv
from importlib.util import spec_from_file_location

#---------------------Functions Section---------------------'''

#---------------------Database Fuctions---------------------#
def gettingData():
    f = open('DisasterRecords.csv', 'r')
    csvr = csv.reader(f)

    tempRow = []
    for row in csvr:
        tempRow.append(row)
    inp = input("want your data: ? (y/n)")
    if (inp == "y" or inp == "Y"):
        idStr = str(input("Enter id: "))
        c = 0
        for i in tempRow:
            if not i:
                continue

            if i[0] == idStr:
                for _ in i:
                    print(_, end=' ')
                print()
                c += 1
                break
        if c == 0:
            print("Cant find data, user not registered")
    f.close()


def settingData(name, city, state, priority, services, extraservice, specificReq):
    f = open('DisasterRecords.csv', 'a')
    inp = input("Want to register your data:? (y/n) ")
    csvw = csv.writer(f)
    if (inp == "y"):
        now = datetime.now()
        uniqueId = now.strftime("%d%m%Y%H%M%S")
        userArray = [uniqueId, name, city, state, priority, services, extraservice,
                     specificReq]  # priority(int),services(int),extraService(int),specificReq(str)
        csvw.writerow(userArray)
        print("registered")
        print("Please Keep Your Unique ID For Any Future Reference ",)
        print(uniqueId)
    f.close()

#---------------------------Prevention Functions-----------------------------

def tornadoPrev():
    print("------Preventive Measures During A Tornado-------")
    print('''The best way to stay safe during a tornado is to be prepared with the following items:
i)   Fresh batteries and a battery-operated TV, radio, or internet-enabled device to listen to the latest emergency weather information
ii)  A tornado emergency plan including access to a safe shelter for yourself, your family, people with special needs, and your pets
iii) An emergency kit (including water, non-perishable food, and medication)
iv)  A list of important information, including telephone numbers''')


def cyclonePrev():
    print("----Precautions to Be Taken During a Cyclone------")
    print('''
i)Be aware of the official cyclone warning by listening to the radio or other authentic sources.
ii)Install storm shutters or board up glass windows.
iii)Keep all the doors and windows closed.
iv)Take proper care of adults or children who need attention.''')


def floodPrev():
    print("----Precautions to Be Taken During A FLood----")
    print('''i)Introduce a better flood warning device so it can give \npeople more time to prepare and take action during flash floods. It can also save more lives by releasing an early warning.
ii)Construct a building that is one meter or more from the ground to \nprevent flood damage.
iii)Restore rivers and clean drainage to prevents floods. The mere fact \nthat the rivers will restore to its original state and drainages are clean, the flow of water can be control and damages may be prevented.
iv)Add flood barriers so it can control flood. It can also contain water, \nand damage to properties can be prevented.
v)Apply the technological innovation and advancement where a Flood can be \ndetermined before it actually happens and prevention may take place immediately.''')


def droughtPrev():
    print("----Precautions To Be Taken During Drought----")
    print(''' i)Avoiding Overuse -
One of the biggest strains on our water supply is simple overuse. Being mindful\n of the amount of water you use each day can be a powerful way to prevent droughts.
ii)Conserving Water -
Water doesn’t always have to be in drinkable condition for us to use it for other \nneeds. That means, in many cases, we can re-use water to help conserve our supplies of fresh, potable water.
iii)Better Monitoring -
Technology has made it possible for households and businesses to gain greater \ninsight into how they use their resources, and so-called “smart plumbing” is on the rise.''')


def earthquakePrev():
    print("----Precautions To Be Taken During Earthquake----")
    print('''i)Connections of gas lines and appliances must be made flexible.
ii)An earthquake readiness plan must be kept ready, including locating a shelter \nhouse, canned food and up to date first aid kit, gallons of water, dust masks, goggles, firefighting equipment, a torch, and a working battery-operated radio.
iii)Architects and structural engineers must be consulted before laying the \nfoundation of buildings in earthquake-prone areas. Also the building must be manufactured as per the rules and regulations laid by the disaster management committee.
iv)Awareness must be spread among friends and family members about the \nabove-mentioned measures. ''')


# --------------------------HelpLine Number FUnctions----------------------------
def floodHelp():
    print("Contact Number - 91XXXXXX21 and 89XXXXXX13")


def droughtHelp():
    print("Contact Number - 91XXXXXX21 and 89XXXXXX13")


def earthquakeHelp():
    print("Contact Number - 91XXXXXX21 and 89XXXXXX13")


def tornadoHelp():
    print("Contact Number - 91XXXXXX21 and 89XXXXXX13")


def cycloneHelp():
    print("Contact Number - 91XXXXXX21 and 89XXXXXX13")


# --------------------------After Disaster Functions----------------------------

def afterDisaster():
    global specificReq
    global services
    global priority
    global extraservice
    priority = int(input('''Enter Your Priority Level
    1)Very High
    2)Moderately High
    3)Normal Priority'''))
    services = int(input('''Select The Service You Need
    1)Transport
    2)Medical
    3)Shelter And Food '''))
    extra = input("Do You Need any Extra Service (y/n)")
    extraservice = 0
    if extra == "y" or extra == "Y":
        extraservice = int(input('''Enter Your Secondary Service
        1)Transport
        2)Medical
        3)Shelter And Food'''))
    else:
        extraservice = 0
    specificReq = input("Enter Your Specific Requirements, if any, excluding the information given above - \n ")


# -------------------------MAIN CODE------------------------------

name = input("Enter your Name - ")
city = input("Enter Your city - ")
state = input("Enter your state - ")
priority = 0
services = 0
extraservice = 0
specificReq = "NIL"

a = int(input('''Which Disaster Are You Facing
1) Flood
2) Drought
3) Earthquake
4) Cyclone
5) Tornado'''))
if a == 1:
    b = int(input(''' Select The Option
    1) Preventive Measures
    2) After Disaster Help'''))
    if b == 1:
        floodPrev()
        helpnom=input(" Do You Want a Helpline Number - y/n\t")
        if helpnom=="y" or helpnom=="Y":
            floodHelp()
    elif b == 2:
        afterDisaster()
if a == 2:
    c = int(input(''' Select The Option
    1) Preventive Measures
    2) After Disaster Help'''))
    if c == 1:
        droughtPrev()
        helpnom=input(" Do You Want a Helpline Number - y/n\t")
        if helpnom=="y" or helpnom=="Y":
            droughtHelp()
    elif c == 2:
        afterDisaster()
if a == 3:
    d = int(input(''' Select The Option
    1) Preventive Measures
    2) After Disaster Help'''))
    if d == 1:
        earthquakePrev()
        helpnom=input(" Do You Want a Helpline Number - y/n\t")
        if helpnom=="y" or helpnom=="Y":
            earthquakeHelp()
    elif d == 2:
        afterDisaster()
if a == 4:
    e = int(input(''' Select The Option
    1) Preventive Measures
    2) After Disaster Help'''))
    if e == 1:
        cyclonePrev()
        helpnom=input(" Do You Want a Helpline Number - y/n\t")
        if helpnom=="y" or helpnom=="Y":
            cycloneHelp()
    elif e == 2:
        afterDisaster()
if a == 5:
    f = int(input(''' Select The Option
    1) Preventive Measures
    2) After Disaster Help'''))
    if f == 1:
        tornadoPrev()
        helpnom=input(" Do You Want a Helpline Number - y/n\t")
        if helpnom=="y" or helpnom=="Y":
            tornadoHelp()
    elif f == 2:
        afterDisaster()
settingData(name, city, state, priority, services, extraservice, specificReq)
gettingData()
