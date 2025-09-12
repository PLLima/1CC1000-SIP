import sys
import csv

def common_friends(friendships):
    common_friends = {}

    for person1, person1_friends in friendships.items():
        for person2, person2_friends in friendships.items():
            if person1 != person2:

                key = (person1, person2) if person1 < person2\
                    else (person2, person1)

                if key in common_friends:
                    continue

                common = list(set(person1_friends) &
                              set(person2_friends))

                common_friends[key] = common

    return common_friends

# If no command-line argument is passed, raise an error.
if len(sys.argv) == 1:
    sys.exit("You must pass this program the name of the file containing the social network")

# Get the first command-line argument (the input file name)
input_filename = sys.argv[1]

# Open the input file
with open(input_filename, mode='r') as file:

    # Set up the object used to read the file as a CSV file.
    csv_reader = csv.reader(file)

    # The dictionary that will contain the social network read from file.
    social_network = {}
    for row in csv_reader:
        # Store the list of of friends of the individual at the current row.
        social_network[row[0]] = row[1:]


print(common_friends(social_network))