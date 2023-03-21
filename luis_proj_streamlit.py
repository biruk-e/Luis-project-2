import streamlit as st
import pandas as pd

st.title("Luis Project Temp. Website")
st.header("Program Description")
st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.")
st.header("Instructions")
st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.")
st.subheader("Upload your input file in csv or txt form")
file = st.file_uploader("File uploader", type=['txt','csv'], accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")
string = st.text_input("Text Inp Widget", value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, placeholder=None, disabled=False, label_visibility="visible")

if file == None:    
    pass
elif file != None:
    #inputfile = open(file, "r")
    #Removing the "\n" at the end of each line in the input file and storing it in the list data
    inputfile = open(file.name, "r")
    temp_data = inputfile.readlines()
    #st.write(temp_data)
    data = []
    for line in temp_data:
        data.append(line.rstrip("\n"))

    #Creating a dictionary with the days/gilts that are added when we run out of gilts
    days = {}
    for line in data:
        bites = line.split(",")
        days[bites[0] + " - " + bites[1]] = bites[2]

    roomsize = 20
    startingRoomnumber = 13
    emptySlots = 20
    currentRoom = 13
    currentDay = 2
    daysIndex = 2

    outputfile = open("\\Users\\Biruk\\Desktop\\Luis Project\\luis_proj_output.txt", "a")

    #outputfile.write("Group: " + "50" + ", Day: " + "2" + ", Room: " + str(currentRoom) + ", Gilt Count: " + str(20) + "\n")
    for line in data:
        chunks = line.split(",")
        group = int(chunks[0])
        day = int(chunks[1])
        giltCount = int(chunks[2])

        if emptySlots - giltCount < 0: #If there's more gilts than empty slots        
            #outputfile.write(str(emptySlots) + "\n")
            st.write("Group: " + str(group) + ", Day: " + str(day) + ", Room: " + str(currentRoom) + ", Gilt Count: " + str(emptySlots) + "\n") 
            remainingGilts = abs(emptySlots - giltCount) 
            emptySlots = 0 #Room is full so empty slots goes down to 0
            while remainingGilts > 0:
                currentRoom += 1 #Room number increases by 1
                emptySlots = 20 #Empty slots resets to 20 because we have a new room
                #Write out Group, Day, Room, and Gilt Count in output file
                #outputfile.write("Group: " + str(group) + ", Day: " + str(day) + ", Room: " + str(currentRoom) + ", Gilt Count: " + str(remainingGilts) + "\n")
                if emptySlots - remainingGilts < 0 and emptySlots != 0:
                    st.write("Group: " + str(group) + ", Day: " + str(day) + ", Room: " + str(currentRoom) + ", Gilt Count: " + str(emptySlots) + "\n") 
                    remainingGilts = abs(emptySlots - remainingGilts)
                    emptySlots = 0
                elif emptySlots - remainingGilts == 0: #If there's an equal amount of empty slots and remaining gilts
                    st.write("Group: " + str(group) + ", Day: " + str(day) + ", Room: " + str(currentRoom) + ", Gilt Count: " + str(20) + "\n") 
                    remainingGilts = 0
                    emptySlots = 0
                elif emptySlots - remainingGilts > 0 and remainingGilts != 0: #If there's more empty slots than remaining gilts
                    st.write("Group: " + str(group) + ", Day: " + str(day) + ", Room: " + str(currentRoom) + ", Gilt Count: " + str(remainingGilts) + "\n")
                    emptySlots = emptySlots - remainingGilts
                    remainingGilts = 0                
                    #day += 1
        
        elif emptySlots - giltCount > 0: #If there's less gilts than empty slots
            st.write("Group: " + str(group) + ", Day: " + str(day) + ", Room: " + str(currentRoom) + ", Gilt Count: " + str(giltCount) + "\n") 
            remainingGilts = 0
            emptySlots -= giltCount #Empty slots are reduced by the amount of gilts that were put in the room
        
        elif emptySlots - giltCount == 0: #If there's an equal amount of gilts and empty slots
            st.write("Group: " + str(group) + ", Day: " + str(day) + ", Room: " + str(currentRoom) + ", Gilt Count: " + str(giltCount) + "\n") 
            remainingGilts = 0
            emptySlots = 0
