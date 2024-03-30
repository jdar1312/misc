#Code to check function argument types.
#ORIGINAL from: https://stackoverflow.com/questions/2489669how-do-python-functions-handle-the-types-of-parameters-that-you-pass-in
#August 2023

import functools
    
def type_check(func):
    '''  
    Wrapper function for verifying function argument types.
    Does not work if any of the arguments' (or return's) type is not declared.

    USE EXAMPLE:

    @type_check
    def test(name : str) -> float:
        return 3.0

    >> test('asd')
    >> 3.0
    '''
    @functools.wraps(func)
    def check(*args, **kwargs):
        for i in range(len(args)):
            v = args[i]
            v_name = list(func.__annotations__.keys())[i]
            v_type = list(func.__annotations__.values())[i]
            error_msg = 'Variable `' + str(v_name) + '` should be type ('
            error_msg += str(v_type) + ') but instead is type (' + str(type(v)) + ')'
            if not isinstance(v, v_type):
                raise TypeError(error_msg)

        result = func(*args, **kwargs)
        v = result
        v_name = 'return'
        v_type = func.__annotations__['return']
        error_msg = 'Variable `' + str(v_name) + '` should be type ('
        error_msg += str(v_type) + ') but instead is type (' + str(type(v)) + ')'
        if not isinstance(v, v_type):
                raise TypeError(error_msg)
        return result

    return check


# The code above does not work if any of the arguments' (or return's) type is not declared. The following edit can help, on the other hand, it only works for kwargs and does not check args.
# def type_check(func):

#     @functools.wraps(func)
#     def check(*args, **kwargs):
#         for name, value in kwargs.items():
#             v = value
#             v_name = name
#             if name not in func.__annotations__:
#                 continue
                
#             v_type = func.__annotations__[name]

#             error_msg = 'Variable `' + str(v_name) + '` should be type ('
#             error_msg += str(v_type) + ') but instead is type (' + str(type(v)) + ') '
#             if not isinstance(v, v_type):
#                 raise TypeError(error_msg)

#         result = func(*args, **kwargs)
#         if 'return' in func.__annotations__:
#             v = result
#             v_name = 'return'
#             v_type = func.__annotations__['return']
#             error_msg = 'Variable `' + str(v_name) + '` should be type ('
#             error_msg += str(v_type) + ') but instead is type (' + str(type(v)) + ')'
#             if not isinstance(v, v_type):
#                     raise TypeError(error_msg)
#         return result

#     return check