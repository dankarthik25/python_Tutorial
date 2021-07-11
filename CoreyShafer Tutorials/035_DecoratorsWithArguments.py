
def prefix_deocorator(prefix):
    def decorator_function(original_func):
        def wrapper_function(*args, **kwargs):
            print(prefix, 'Executed before', original_func.__name__)
            result = original_func(*args, **kwargs)
            print(prefix, 'Executed after', original_func.__name__)
            return result
        return wrapper_function
    return decorator_function


@prefix_deocorator('LOG: ')
def display_info(name, age):
    print('dispaly function ran with argument ({}, {})'.format(name, age))


display_info('John', 35)
display_info('Travis', 30)
