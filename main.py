#names for the missions
mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
#starts at 0
mission_total = 0
#temp assigns the missions to a variable
for mission in mission_names:
    mission_total += 1 #assigns the number of missions plus one 

print(f"Total number of missions: {mission_total}") #prints out the total of missions


mission_success = [True, False, True, True, True, True, False] # success data

successful_missions = 0 #starts at 0

for mission in mission_success:# temp assigns a variable to the amount
    if mission == True: # checks if the index is true or false
        successful_missions += 1 #assigns the number of successes plus one

print(f"Total of number of successfull missions: {successful_missions}") # prints out the total number of successes

success_rate = 71.43 # assigns the success rate to a variable
print(f"Success rate: {success_rate:.2f}%") # converts the success rate into a percentage


mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970] #years of the missions

print("Missions launched before the year 2000:") # prints out out the prompt

mission = 0 # list starts at 0 
 # cite for using zip due to not knowing how to combine strings, used google search
for names, years in zip(mission_names, mission_years): 
    if years < 2000: # checks if the year is over 2000
        mission += 1 # if the year is under 2000 it adds one
        print(f"- {names}") # prints out the names of the missions that qualify









