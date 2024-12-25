from datetime import date, timedelta
from itertools import permutations

def generate_and_save_birthdays_with_permutations(start_year, end_year, filename):
    
    with open(filename, "w") as file:
        start_date = date(start_year, 1, 1)
        end_date = date(end_year, 12, 31)
        
        current_date = start_date
        while current_date <= end_date:
            day = current_date.strftime('%d')
            month = current_date.strftime('%m')
            year = current_date.strftime('%Y')
            components = [day, month, year]
    
            for perm in permutations(components):
                file.write("".join(perm) + "\n")
            
            current_date += timedelta(days=1)

generate_and_save_birthdays_with_permutations(1950, 2025, "birthday.txt")
