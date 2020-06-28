"""
To Do
- Random returns for Names
- Split into species/type
"""
import os, random, names

generator_running = True
num_to_gen = 1

############ Functions ############

### Generate Fantasy Names ###
def generateFantasy(gender, species, num_to_gen):
    # Human Male
    if gender == "male" and species == 'Human':
        for i in range(num_to_gen):
            first_name = random.choice(names.male_fantasy_names[0])
            surname = random.choice(names.fantasy_surnames[0])
            name = f'{first_name} {surname}'
            formatted_print(gender,species,name)
    #Elf Male
    elif gender == "male" and species == 'Elf':
        for i in range(num_to_gen):
            first_name = random.choice(names.male_fantasy_names[1])
            surname = random.choice(names.fantasy_surnames[1])
            name = f'{first_name} {surname}'
            formatted_print(gender,species,name)
    #Dwarf Male
    elif gender == "male" and species == 'Dwarf':
        for i in range(num_to_gen):
            first_name = random.choice(names.male_fantasy_names[2])
            surname = random.choice(names.fantasy_surnames[2])
            name = f'{first_name} {surname}'
            formatted_print(gender,species,name)
    #Human Female
    elif gender == "female" and species == 'Human':
        for i in range(num_to_gen):
            first_name = random.choice(names.female_fantasy_names[0])
            surname = random.choice(names.fantasy_surnames[0])
            name = f'{first_name} {surname}'
            formatted_print(gender,species,name)
    #Elf Female
    elif gender == "female" and species == 'Elf':
        for i in range(num_to_gen):
            first_name = random.choice(names.female_fantasy_names[1])
            surname = random.choice(names.fantasy_surnames[1])
            name = f'{first_name} {surname}'
            formatted_print(gender,species,name)
    #Dwarf Female
    elif gender == "female" and species == 'Dwarf':
        for i in range(num_to_gen):
            first_name = random.choice(names.female_fantasy_names[2])
            surname = random.choice(names.fantasy_surnames[2])
            name = f'{first_name} {surname}'
            formatted_print(gender,species,name)
    #Human, Both Male and Female
    elif gender == 'both' and species == "Human":
        print('Test passed')
        for i in range(num_to_gen):
            first_name = random.choice(names.all_human_names)
            surname = random.choice(names.fantasy_surnames[0])
            name = f'{first_name} {surname}'
            formatted_print(gender,species,name)
    #Elf, Both Male and Female
    elif gender == 'both' and species == 'Elf':
        for i in range(num_to_gen):
            first_name = random.choice(names.all_elf_names)
            surname = random.choice(names.fantasy_surnames[1])
            name = f'{first_name} {surname}'
            formatted_print(gender,species,name)
    #Dwarf, Both Male and Female
    elif gender == 'both' and species == 'Dwarf':
        for i in range(num_to_gen):
            first_name = random.choice(names.all_dwarf_names)
            surname = random.choice(names.fantasy_surnames[2])
            name = f'{first_name} {surname}'
            formatted_print(gender,species,name)


### Generate Sci-Fi Names ###
# TO DO
# - Sci-fi isn't separated between gender except for Human.
# Instead of asking for gender (can be skipped) just ask for this specific
# one here.
def generateScifi(species,num_to_gen):
    # Human Male
    if species == 'Human Male':
        gender = 'male'
        species = 'Human'
        for i in range(num_to_gen):
            name = random.choice(names.scifi_names[0])
            #surname = random.choice(names.fantasy_surnames[0])
            #name = f'{first_name} {surname}'
            formatted_print(gender,species,name)
    # Human Female
    elif species == 'Human Female':
        gender = 'female'
        species = 'Human'
        for i in range(num_to_gen):
            name = random.choice(names.scifi_names[1])
            #surname = random.choice(names.fantasy_surnames[0])
            #name = f'{first_name} {surname}'
            formatted_print(gender,species,name)
    # Alien
    elif species == 'Alien':
        gender = 'both'
        for i in range(num_to_gen):
            name = random.choice(names.scifi_names[2])
            #surname = random.choice(names.fantasy_surnames[0])
            #name = f'{first_name} {surname}'
            formatted_print(gender,species,name)
    # Robot
    elif species == 'Robot':
        gender = 'both'
        for i in range(num_to_gen):
            name = random.choice(names.scifi_names[3])
            #surname = random.choice(names.fantasy_surnames[0])
            #name = f'{first_name} {surname}'
            formatted_print(gender,species,name)

    print("Sci-Fi Name Generated")


#Format the output
def formatted_print(gender,species,name):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n'*3)
    if gender == 'both':
        print(f'Your {species} name is {name}!')
    else:
        print(f'Your {gender} {species} name is {name}!')
    print('\n'*3)



#####################################
############# Main Loop #############
#####################################

while generator_running == True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome to The SPD StoryStudio Name Generator!")
    print("Let's get generating.\n\n")

    # Main menu
    print("Main Menu".center(40,'='),end='')
    print(
    """
    1. Generate Fantasy Names
    2. Generate Science Fiction Names
    3. Exit"""
    )
    print("".center(40,'='))
    print('\n'*3)
    genre_choice = str(input('What Do You Want To do? '))

    # Exit command
    if genre_choice == '1':
        genre_choice = 'Fantasy'
    elif genre_choice == '2':
        genre_choice = "Sci-Fi"
    elif genre_choice == '3':
        generator_running = False
        break

    # Clears screen between menu choices
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Welcome to The SPD StoryStudio Name Generator!")
    print("Let's get generating.\n\n")
    #Species/Type Menu

    print("Species/Type Menu".center(40,'='),end='')
    if genre_choice == 'Fantasy':
        print(
        """
        1. Generate Human Names
        2. Generate Elf Names
        3. Generate Dwarf Names"""
        )
        print("".center(40,'='))
        print('\n'*3)
        species_choice = str(input('What Species/Type? '))
        if species_choice == '1':
            species_choice = 'Human'
        elif species_choice == '2':
            species_choice = 'Elf'
        elif species_choice == '3':
            species_choice = "Dwarf"

        os.system('cls' if os.name == 'nt' else 'clear')

        print("Welcome to The SPD StoryStudio Name Generator!")
        print("Let's get generating.\n\n")
        # Gender menu
        print("Gender Menu".center(40,'='),end='')
        print(
        """
        1. Generate Male Names
        2. Generate Female Names
        3. Generate Male & Female Names"""
        )
        print("".center(40,'='))
        print('\n'*3)
        gender_choice = str(input('What Gender? '))
        if gender_choice == '1':
            gender_choice = 'male'
        elif gender_choice == '2':
            gender_choice = 'female'
        elif gender_choice == '3':
            gender_choice = 'both'


    elif genre_choice == 'Sci-Fi':
        print(
        """
        1. Generate Human Male Names
        2. Generate Human Female Names
        3. Generate Alien Names
        4. Generate Robot Names"""
        )
        print("".center(40,'='))
        print('\n'*3)
        species_choice = str(input('What Species/Type? '))
        if species_choice == '1':
            species_choice = 'Human Male'
        elif species_choice == '2':
            species_choice = 'Human Female'
        elif species_choice == '3':
            species_choice = 'Alien'
        elif species_choice == '4':
            species_choice = "Robot"



    # Clears screen between menu choices



    if genre_choice == "Fantasy":
        generateFantasy(gender_choice, species_choice, num_to_gen)
    elif genre_choice == "Sci-Fi":
        generateScifi(species_choice, num_to_gen)
    else:
        print("Invalid choices, please try again.")

    generate_again = input("Do you want to generate more names? (y/n): ")
    if generate_again.lower() == 'n':
        generator_running = False


# use os.system('cls' if os.name == 'nt' else 'clear') to clear screen before returning to menu
