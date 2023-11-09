# awards.py
# ENDG 233 F23
# DANIEL JAMES EDGAR
# A terminal-based program for analyzing movie awards data.
# You must include the code listed below. You may add your own additional functions, variables, etc. 
# You may not import any modules.
# You may only use built-in functions that directly support strings, lists, dictionaries, sets, and tuples.
# Remember to include docstrings for your functions and comments throughout your code.
# ******************************************************************************************************
# Data is imported from the included awards_data.py file. Both files must remain in the same directory.
# Do not modify the code in this section.
# You may not hardcode (manually enter in the code) any other data.
from awards_data import SAG, oscars, NBR, ISA, GLAAD, NAACP
award_list_names = ['sag', 'oscars', 'nbr', 'isa', 'glaad', 'naacp']
award_list_options = [SAG, oscars, NBR, ISA, GLAAD, NAACP]
# ******************************************************************************************************
def count_awards(title):
    """Iterate through each organization in the organization list, count how many times the movie appears in the winners and add to the total awards won by the movie.
    
    Parameters:
        title: the string representing the movie title.
    
    Returns:
        total: the total number of times that the movie won an award
    """
    total = 0 # look through each award organization lists, see if the title is equal to an element when it is lowercase, if it is add the amount of appearances to total
    for i in award_list_options: 
        for j in i:  
            if title == j.lower():
                total += j.lower().count(title)
    return total

def print_award_winners(organization):
    """Find if the organization selected is in the list, if it is then return its position to print it's winners, otherwise dont print.

    Parameters:
        organization: the string representing the organization
        
    Returns:
        None
    """
    if organization in award_list_names: # find the index of the organization in the award_list_options then print each element in that embedded list.
        org_index = award_list_names.index(organization) 
        print('--Requested Award Winners--')
        for i in award_list_options[org_index]:
            print(i)
    else:
        print('Awards list not found.')
# ******************************************************************************************************
print("ENDG 233 Awards Data Program")

menu_input = input('\nSelect 1 to search a specific movie, 2 to print specific rewards results, 0 to end: ')

while menu_input != '0': # iterate until 0 is given as the menu input

    if menu_input == '1': # if 1 is selected, print the template then call the count_awards function to count how many awards the movie won. Print the
        movie_title = input('Please enter the movie title you would like to search: ')
        movie_title = movie_title.strip()
        movie_title = movie_title.lower()
        print(f'--Number of Awards Won--\n{count_awards(movie_title)}')

    elif menu_input == '2': # if 2 is selected, print the template, then input orginization name and then call the print_awards_winners function to print the winning movies.
        print('\nPlease choose one of the following awards lists:\nOscars\nSAG\nNBR\nISA\nGLAAD\nNAACP\n')
        org_name = input('')
        org_name = org_name.strip()
        org_name = org_name.lower()
        print_award_winners(org_name)

    else: # if the menu input is not 1, 2, or 0 then ask for an appropiate input
        print('You must select either 1, 2, or 0.')     
    menu_input = input('\nSelect 1 to search a specific movie, 2 to print specific rewards results, 0 to end: ') # ask for the menu input until 0 is chosen

print('Thank you for using the awards data program.')