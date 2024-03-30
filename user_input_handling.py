'''
Utility function for specifying what input user must enter and verifying that it was entered correctly.
Author: Jude Darmanin
Date: September 2023
'''

import re
from typing import List

class InputError(Exception):
    '''Raised when user enters an invalid input'''
    pass

def get_user_input(input_string:str, required_input:List[str]=[], pattern:str = '', required_len:int=None, case_sensitive:bool = True, return_case:str = None, trim:bool = True, max_retries:int = 3) -> str:

    '''
    Prompt user for an input via 'input_string' and specify input requirements:
    - required_input (list) - specify list of inputs from which user can enter, else throw error.
    OR
    - pattern (str) - specify the regex pattern of input that user must enter
    OR
    - required_len (int) - specify the length of the input that the user must enter.

    Other options:
    - case_sensitive (bool) - specify whether user input is case_sensitive (in case of a string input)
    - return_case (str) - specify 'upper' or 'lower' to automatically convert user input to upper or lower case
    - trim (bool) - strip user input of excess whitespace if True
    - max_retries (int) - maximum retries to give user in case of bad entry
    
    '''
    try:
       
        #get raw user input
        retries = 1

        while True:

            ui = input(input_string)
            if trim:
                ui = ui.strip()

            if retries < int(max_retries):

                try:
                    if len(required_input) > 0:
                        
                        if (not isinstance(required_input, list) or not all(isinstance(i, str) for i in required_input)):
                           raise TypeError

                        if case_sensitive:
                            if ui not in required_input:
                                raise InputError(f'Input should be a value in {required_input}, please try again. Case sensitive: {case_sensitive}') 
                        else:
                            if ui.lower() not in [x.lower() for x in required_input]:
                                raise InputError(f'Input should be a value in {required_input}, please try again. Case sensitive: {case_sensitive}')
                            
                    elif len(pattern) > 0:
                        if case_sensitive:
                            re_pattern = re.compile(pattern)
                        else:
                            re_pattern = re.compile(pattern, re.IGNORECASE)
                        if not re_pattern.match(ui):
                            raise InputError(f'Input does not match the required pattern \'{pattern}\', please try again. Case sensitive: {case_sensitive}')

                    elif required_len is not None:
                        if len(ui) != int(required_len):
                            raise InputError(f'Input does not match the required length of {int(required_len)}, please try again.')

                except InputError as e:

                    print(f'{e}')
                    retries += 1

                else:
                    break

            else:
                raise InputError(f'Input did not match the requirements after {int(max_retries)} attempts.')

        if return_case == 'upper':
            return ui.upper()
        elif return_case == 'lower':
            return ui.lower()
        else:
            return ui
    
    except (ValueError, TypeError) as e:
        print('Incorrect argument specification')
        print(get_user_input.__doc__)
        #or print(get_user_input.__annotations__)
        

if __name__ == "__main__":

    user_input = get_user_input('Enter prompt ', required_input=[], pattern = '', required_len=3, case_sensitive=True, return_case = 'upper', trim=True, max_retries=3.3)
    print(user_input)



    
