print("Hello World")

counties_dict={'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438}

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties")
else:
    print("El Paso is not in the list of counties")
    
#for county, voters in counties_dict.items():
 #   print(f"{county} county has {voters:,} registered voters")

voting_data=[]
voting_data.append({'county':'Arapahoe', 'registered_voters': 422829})
voting_data.append({'county':'Denver', 'registered_voters': 463353})
voting_data.append({'county':'Jefferson', 'registered_voters':432438})
print(voting_data)
# How many votes did you get?
my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
total_votes = int(input("What is the total votes in the election? "))
# Calculate the percentage of votes you received.
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")