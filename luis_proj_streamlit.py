import streamlit as st
import pandas as pd

st.title("FlowProjections")
#st.header("Program Description")
#st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.")
st.write("Hi! Welcome to FlowProjections!")
st.write("Thank you for choosing us!")
st.write("We are here to simplify your tasks by automatically calculating your flow projections. Just create a csv file that has 3 columns containing your group numbers, days, and gilts in each group (make sure that the first line of the file says “group, day, gilts” as this indicates to our program which columns hold what information). Here’s an example of what it should look like:")
st.write("[insert image here]")
st.write("Once you’re done, upload your file and our program does all the work for you, letting you focus on what really matters!")
st.write("We are still in the development stage and are starting to test and troubleshoot. In the future we expect to add more functionalities and make our program more user-friendly. We are excited to provide this service and would appreciate any input in order to improve our application. If you have any issues with the application please email us with your questions or concerns at [insert email].")
#st.header("Instructions")
#st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.")



# Constants
roomsize = st.slider("Set room capacity", min_value = 1, max_value= 100, step=1)
startingRoomnumber = 13
emptySlots = roomsize
currentRoom = st.slider("Set starting room number", min_value = 1, max_value= 100, step=1)
currentDay = 2
daysIndex = 2

# File uploader
file = st.file_uploader("_Upload your csv or txt file here_", type=['txt','csv'], accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")

if file != None:
    df = pd.read_csv(file)
    #st.table(df2)
    data = {"group": [], "day": [], "room number": [], "gilt count": []}
    #pd.Dataframe.from_dict(data)
    #st.write(df)

    for index, row in df.iterrows():
        group = int(row['group'])
        day = int(row['day'])
        giltCount = int(row['gilts'])

        if emptySlots - giltCount < 0: #If there's more gilts than empty slots        
            #outputfile.write(str(emptySlots) + "\n")
            #st.write("Group: " + str(group) + ", Day: " + str(day) + ", Room: " + str(currentRoom) + ", Gilt Count: " + str(emptySlots) + "\n") 
            data["group"].append(group)
            data["day"].append(day)
            data["room number"].append(currentRoom)
            data["gilt count"].append(emptySlots)
            
            remainingGilts = abs(emptySlots - giltCount) 
            emptySlots = 0 #Room is full so empty slots goes down to 0
            while remainingGilts > 0:
                currentRoom += 1 #Room number increases by 1
                emptySlots = roomsize #Empty slots resets to 20 because we have a new room
                #Write out Group, Day, Room, and Gilt Count in output file
                #outputfile.write("Group: " + str(group) + ", Day: " + str(day) + ", Room: " + str(currentRoom) + ", Gilt Count: " + str(remainingGilts) + "\n")
                if emptySlots - remainingGilts < 0 and emptySlots != 0:
                    #st.write("Group: " + str(group) + ", Day: " + str(day) + ", Room: " + str(currentRoom) + ", Gilt Count: " + str(emptySlots) + "\n") 
                    data["group"].append(group)
                    data["day"].append(day)
                    data["room number"].append(currentRoom)
                    data["gilt count"].append(emptySlots)

                    remainingGilts = abs(emptySlots - remainingGilts)
                    emptySlots = roomsize
                elif emptySlots - remainingGilts == 0: #If there's an equal amount of empty slots and remaining gilts
                    #st.write("Group: " + str(group) + ", Day: " + str(day) + ", Room: " + str(currentRoom) + ", Gilt Count: " + str(20) + "\n") 
                    data["group"].append(group)
                    data["day"].append(day)
                    data["room number"].append(currentRoom)
                    data["gilt count"].append(roomsize)
                    remainingGilts = 0
                    emptySlots = roomsize
                    currentRoom += 1
                elif emptySlots - remainingGilts > 0 and remainingGilts != 0: #If there's more empty slots than remaining gilts
                    #st.write("Group: " + str(group) + ", Day: " + str(day) + ", Room: " + str(currentRoom) + ", Gilt Count: " + str(remainingGilts) + "\n")
                    data["group"].append(group)
                    data["day"].append(day)
                    data["room number"].append(currentRoom)
                    data["gilt count"].append(remainingGilts)

                    emptySlots = emptySlots - remainingGilts
                    remainingGilts = 0                
                    #day += 1
        
        elif emptySlots - giltCount > 0: #If there's less gilts than empty slots
            #st.write("Group: " + str(group) + ", Day: " + str(day) + ", Room: " + str(currentRoom) + ", Gilt Count: " + str(giltCount) + "\n") 
            data["group"].append(group)
            data["day"].append(day)
            data["room number"].append(currentRoom)
            data["gilt count"].append(giltCount)

            remainingGilts = 0
            emptySlots -= giltCount #Empty slots are reduced by the amount of gilts that were put in the room
        
        elif emptySlots - giltCount == 0: #If there's an equal amount of gilts and empty slots
            #st.write("Group: " + str(group) + ", Day: " + str(day) + ", Room: " + str(currentRoom) + ", Gilt Count: " + str(giltCount) + "\n") 
            data["group"].append(group)
            data["day"].append(day)
            data["room number"].append(currentRoom)
            data["gilt count"].append(giltCount)

            remainingGilts = 0
            emptySlots = roomsize
            currentRoom += 1

    #st.write(data)
    df2 = pd.DataFrame(data= data)
    st.write(df2)

    def convert_df(df):
        return df.to_csv(index=False).encode('utf-8')
    
    csv = convert_df(df2)

    st.download_button("Press to Download", csv, "file.csv", "text/csv", key='download-csv')
