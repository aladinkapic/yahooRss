import datetime
from rest_framework.response import Response

# This class would define all data

# Class for custom pagination
class cPagination:

    # Creates page numbers +-3 pages from current page
    def get(page_number, num_of_pages):
        p_from = 1
        p_to = 0

        if num_of_pages > 6:
            if page_number <= 3: p_to = 6
            elif page_number >= (num_of_pages - 3):
                p_from = num_of_pages - 4
                p_to = num_of_pages + 1
            else:
                p_from = page_number - 2
                p_to = page_number + 3
        else:
            p_to = num_of_pages + 1

        return range(p_from, p_to)

# Class for scraping data



# Class for validation
class Validation:

    # Validate date - Codes are just a convention - 0000 good to go, everything else is some kind of error and / or warning
    def dValidate(date):
        try:
            datetime.datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            return {
                'code': '4004',
                'message': 'Date format not valid !',
            }
        return { 'code': '0000' }



# Class API response