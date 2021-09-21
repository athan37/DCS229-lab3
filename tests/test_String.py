from code_base.String import *
import pytest
import random
import string

###############################################################################

class print_test:
    ''' Class to be used in streamlining prints of each test in "test_..."
        pytest testing functions below.  Because this class only provides
        an __init__ method, it can be used as though it was simply a
        function call, e.g.,
            print_test('String("")._chars', ...)
        Because this is a class, each call to print_test can therefore track
        the total number of calls/tests to be displayed in the printing.

        Usage syntax:

            print_test([string representing the call being tested], \
                       result =   [result of the call being tested], \
                       expected = [expected result of the call teing tested])

        Usage example:
            print_test('String("")._chars', \
                       result   = String("")._chars,
                       expected = [])

    '''
#I wish github worked 

    test_number = 0  # class-level (static) variable to track number of tests

    def __init__(self, what_test: str, *args: list, **kwargs: dict):
        ''' Defining print_test as a class with __init__ will allow the user
            call print_test like a funtion, when they're actually constructing
            a print_test object (but allows us to track the total number of
            tests).

        Args:
            what_test: str representation of what is being tested, e.g., of the
                form 'String("")._chars' when testing the contents of an
                instance variable _chars inside a newly created String object
            kwargs['result']: type varies (typically String or str or list or None).
                The actual result of the test being conducted.  For example, this
                would be [] for a correct implementation of String("")._chars.
            kwargs['expected']: type varies (typically String or str or list or None)
                The expected result of the test being conducted. For example, this
                should be [] when testing String("")._chars.

        Returns:
            None -- this is an __init__ method.
        '''

        # grab the required keyword arguments
        result   = kwargs['result']
        expected = kwargs['expected']

        # some setup for printing the test info below
        prefix = f'Test {print_test.test_number}: '
        # fish out the class name, which whould be String in this context,
        # and the argument to the String construction
        open1_idx  = what_test.index('(')
        close1_idx = what_test.index(')', open1_idx)
        class_name = what_test[0:open1_idx]
        argument1  = what_test[open1_idx + 2 : close1_idx - 1]  # account for quotes
        # create a string with string-indices for displaying
        indices = "".join(str(i % 10) for i in range(len(argument1)))

        argument2 = None; padding = ""
        # check whether String("...") appears twice for adding second arg's indices
        if class_name in what_test[close1_idx:]:
            open2_idx    = what_test.index('(', close1_idx)
            close2_idx   = what_test.index(')', open2_idx)
            argument2    = what_test[open2_idx + 2 : close2_idx - 1]  # account for quotes
            arg2_indices = "".join(str(i % 10) for i in range(len(argument2)))
            padding      = ' ' * (open2_idx - close1_idx + 1 + 2)     # account for quotes

        # indentation (accounting for # of tests) used in printing below
        indent = '    ' + (' ' * len(str(print_test.test_number)))

        # print the test info, a la 'Test 0: String("")._chars';
        # print indices below whenever the argument is not the empty string
        print(f'\n\n{prefix}{what_test}')
        if argument2 is None:
            if len(argument1) > 0:
                print(f'{indent}# indices: {indices} (length:{len(argument1)})')
        else:
            if len(argument1) > 0 or len(argument2) > 0:
                print(f'{indent}# indices: {indices}{padding}{arg2_indices}')

        try:
            if isinstance(result, String): result = result.__str__()
            assert(type(result) == type(expected))
        except:
            # if the provided result and expected mismatch in type,
            # let the user know...
            print(f"ERROR: mismatched list type in print_test's " + \
                  f"test #{print_test.test_number}:")
            print(f"\t result type: {type(result)}  expected type: {type(expected)}")
        else:
            if isinstance(expected, list):
                # remove spaces from between list items for compact printing
                print(f'{indent}Result:   {str(result).replace(", ", ",")}')
                print(f'{indent}Expected: {str(expected).replace(", ", ",")}')
            elif isinstance(expected, str):
                # include quotes when output is type str
                print(f'{indent}Result:   "{result}"')
                print(f'{indent}Expected: "{expected}"')
            else:
                print(f'{indent}Result:   {result}')
                print(f'{indent}Expected: {expected}')

        print_test.test_number += 1  # increment the static test count

###############################################################################

@pytest.fixture
def empty_string():
    ''' pytest fixture to return an empty string

     Returns:
         empty string
    '''
    return ""

@pytest.fixture
def empty_list():
    ''' pytest fixture to return an empty list

     Returns:
         empty list
    '''
    return []

@pytest.fixture
def characters():
    ''' pytest fixture to provide a list of characters for generating random strings

     Returns:
         a string of characters consisting of letters, digits, and punctuation,
             but with parentheses and quotes removed (to make output comparison
             easier in printed output)
    '''
    return string.digits + string.ascii_letters + \
           "!#$%&*+,-./:;<=>?@[\\]^_`{|}~"

@pytest.fixture
def simple_characters():
    ''' pytest fixture to provide a list of leters for generating simple random strings

    Returns:
        a string of characters consisting of letters
    '''
    return string.ascii_letters

@pytest.fixture
def random_string(characters):
    ''' pytest fixture to generate a random string between length 2 and 20

    Args:
        characters:  pytest fixture (above) for generating a random character string

    Returns:
        an str consisting of randomly-selected characters
    '''
    length = random.randint(2,20)
    return "".join(random.choice(characters) for i in range(length))

@pytest.fixture
def different_random_string(characters):
    ''' pytest fixture to generate a different random string between length 2 and 20
        (e.g., for using random_string and different_random_string as argument to
        the same subsequent fixture)

        see RonnyPfannschmidt 1 Oct 2019 comment here:
        https://github.com/pytest-dev/pytest/issues/5896

    Args:
        characters:  pytest fixture (above) for generating a random character string

    Returns:
        an str consisting of randomly-selected characters
    '''
    length = random.randint(2,20)
    return "".join(random.choice(characters) for i in range(length))

@pytest.fixture
def simple_random_string(simple_characters):
    ''' pytest fixture to generate a simple random string between length 2 and 20
        consisting only of letters

    Args:
        simple_characters: pytest fixture (above) for generating a simple random strings

    Returns:
        an str consisting of randomly-selected letters
    '''
    length = random.randint(2,20)
    return "".join(random.choice(simple_characters) for i in range(length))

@pytest.fixture
def sample_string1():
    ''' pytest fixture that always returns the same string, useful for initial
        equality testing

    Args:
        None

    Returns:
        an str consisting of pre-selected charaters
    '''
    return "1hv2beropijsdf"

@pytest.fixture
def sample_string2():
    ''' pytest fixture that always returns the same string but one that is
        different from the one above

    Agrs:
        None

    Returns:
        an str consisting of pre-selected characters
    '''
    return "lkfh1p209uwefblkjnrsdflkh1"

@pytest.fixture
def sample_String1(sample_string1):
    return String(sample_string1)

@pytest.fixture
def sample_String2(sample_string2):
    return String(sample_string2)

# NOTE: you may want/need to define more fixtures (e.g., for length-one
#   strings?).

###############################################################################

# individual pytest unit tests below

def test_empty_constructor(empty_string):
    ''' pytest test for String construction of an empty string
        (1) stores the actual result of the construction, grabbing internal list
        (2) calls print_test with string version of test, result of the actual
            test, and expected result
        (3) assert required by pytest
    '''
    result = String(empty_string)._chars
    expected = []
    print_test(f'String("{empty_string}")._chars', \
               result = result, expected = expected)
    assert(result == expected)

def test_basic_constructor(random_string):
    ''' pytest test for String construction of a random string
        (1) stores the actual result of the construction, grabbing internal list
        (2) calls print_test with string version of test, result of the actual
            test, and expected result
        (3) assert required by pytest
    '''
    result   = String(random_string)._chars
    expected = [c for c in random_string]
    print_test(f'String("{random_string}")._chars', \
               result = result, expected = expected)
    assert(result == expected)

##############################################################################
##############################################################################
def test_simple_string_conversion(simple_random_string):
    ''' pytest test for str conversion of a random simple String object
        (1) stores the actual and expected results of the conversion
        (2) calls print_test with string version of test, result of the actual
            test, and expected result
        (3) assert required by pytest
    '''
    result = simple_random_string
    expected = simple_random_string
    print_test(f"str({simple_random_string})", \
               result = result, expected = expected)
    assert(result == expected)

def test_complex_string_conversion(random_string):
    ''' pytest test for str conversion of a random String object
        (1) stores the actual and expected results of the conversion
        (2) calls print_test with string version of test, result of the actual
            test, and expected result
        (3) assert required by pytest
    '''
    result = str(random_string)
    expected = random_string
    print_test(f"str({random_string})", \
               result = result, expected = expected)
    assert(result == expected)

def test_empty_string_conversion(empty_string):
    ''' pytest test for str conversion of an empty String object
        (1) stores the actual and expected results of the conversion
        (2) calls print_test with string version of test, result of the actual
            test, and expected result
        (3) assert required by pytest
    '''
    result = str(empty_string)
    expected = empty_string
    print_test(f"str({empty_string})", \
               result = result, expected = expected)
    assert(result == expected)

##############################################################################

def test_random_string_length(random_string):
    ''' pytest test for returning the length of a random String object
        (1) stores the actual and expected results of the length
        (2) calls print_test with string version of test, result of the actual
            test, and expected result
        (3) assert required by pytest
    '''
    result = String(random_string).len()
    expected = len(random_string)
    print_test(f"String({random_string}).len()", \
               result = result, expected = expected)
    assert(result == expected)

def test_empty_string_length(empty_string):
    ''' pytest test for returning the length of an empty String object
        (1) stores the actual and expected results of the length
        (2) calls print_test with string version of test, result of the actually
            test, and expected result
        (3) assert required by pytest
    '''
    result = String(empty_string).len()
    expected = len(empty_string)
    print_test(f"String({empty_string}).len()", \
               result = result, expected = expected)
    assert(result == expected)

##############################################################################

def test_empty_string(empty_string):
    ''' pytest test to determine whether or not a String is empty and return
        a boolean indicating the case
        (1) stores the actual and expected results of the equality
        (2) calls print_test with string version of test, result of the actual
            test, and expected result
        (3) assert required by pytest
    '''
    result = String(empty_string).is_empty()
    expected = True
    print_test(f"String({empty_string}).is_empty()", \
               result = result, expected = expected)
    assert(result == expected)

def test_empty_random_string(random_string):
    ''' pytest test to determine whether or not a String is empty and return
        boolean indicating the case
        (1) stores the actual and expected results of the equality
        (2) calls print_test with string version of test, result of the actual
            test, and expected result
        (3) assert required by pytest
    '''
    result   = String(random_string).is_empty()
    expected = False
    print_test(f"String({random_string}).is_empty()", \
               result = result, expected = expected)
    assert(result == expected)

def test_simple_random_string_equal(sample_string1, sample_string2):
    ''' pytest test to determine whether two str objects are equal
        (1) stores the actual and expected results of the equality
        (2) calls print_test with string version of test, result of the actual
            test, and expected result
        (3) assert required by pytest
    '''

    result   = sample_string1 == sample_string2
    expected = False

    try:
        #There is some problem here
        print_test(f"{sample_string1} == {sample_string2}",\
                result = result, expected = expected)
    except Exception as e: 
        print(e)

    assert(result == expected)

##############################################################################  Duc Anh's change 9/20/2021 ###############

#Test equal
def test_empty_str_equals_empty_String(empty_string):
    ''' Test if an empty string from class String equals to that from class 'str'. 
    
        (1) stores the actual and expected results of the equality
        (2) calls print_test with string version of test, result of the actual
            test, and expected result
        (3) assert required by pytest
    '''
    result   = String(empty_string) == empty_string 
    expected = True
    print_test(f"String({empty_string}) == {empty_string}", \
               result = result, expected = expected)
    assert(result == expected)


#Test add string

def test_add_empty_String_to_empty_str(empty_string):
    ''' Test adding 2 empty normal python string

        (1) stores the actual and expected results of the equality
        (2) calls print_test with string version of test, result of the actual
            test, and expected result
        (3) assert required by pytest
    '''
    result   = String(empty_string) + ''
    expected = String(empty_string) 
    print_test(f"String('{empty_string}') + '' ",\
            result = result, expected = expected)

    assert(result == expected)

def test_add_normal_String_to_other_String(sample_string1, sample_string2):
    ''' Test adding 2 normal string 
    
        (1) stores the actual and expected results of the equality
        (2) calls print_test with string version of test, result of the actual
            test, and expected result
        (3) assert required by pytest
    '''
    result   = String(sample_string1) + String(sample_string2)
    expected = String(sample_string1 + sample_string2)
    print_test(f"String('{sample_string1}') + String('{sample_string2}')", \
               result = result, expected = expected)
    assert(result == expected)

def test_add_normal_String_to_other_str(sample_string1, sample_string2):
    ''' Test adding 2 normal string 
    
        (1) stores the actual and expected results of the equality
        (2) calls print_test with string version of test, result of the actual
            test, and expected result
        (3) assert required by pytest
    '''
    result   = String(sample_string1) + sample_string2
    expected = String(sample_string1 + sample_string2)
    print_test(f"String('{sample_string1}') + '{sample_string2}'", \
               result = result, expected = expected)
    assert(result == expected)

def test_add_normal_String_to_an_empty_str(sample_string1, empty_string):
    ''' Test adding a String with an empty str
    
        (1) stores the actual and expected results of the equality
        (2) calls print_test with string version of test, result of the actual
            test, and expected result
        (3) assert required by pytest
    '''
    result   = String(sample_string1) + empty_string
    expected = String(sample_string1)
    print_test(f"String('{sample_string1}') + '{sample_string2}'", \
               result = result, expected = expected)
    assert(result == expected)

#Test substring

def test_substring_from_0_to_0_of_an_empty_string(empty_string):
    ''' Test substring on empty string
    
        (1) stores the actual and expected results of the equality
        (2) calls print_test with string version of test, result of the actual
            test, and expected result
        (3) assert required by pytest
    '''
    result   = String(empty_string).substring(0, 0 + 1)
    expected = String(empty_string)
    print_test(f"String('{empty_string}').substring(0, 1) + '{empty_string}'", \
               result = result, expected = expected)
    assert(result == expected)

def test_substring_normally(sample_String1, sample_string1):
    ''' Test substring on empty string
    
        (1) stores the actual and expected results of the equality
        (2) calls print_test with string version of test, result of the actual
            test, and expected result
        (3) assert required by pytest
    '''

    result   = sample_String1.substring(3, 7)
    expected = String(sample_string1[3: 7])

    print_test(f"String('{sample_String1}').substring(3, 7) + '{sample_string1}'", \
               result = result, expected = expected)
    assert(result == expected)

def test_substring_start_larger_than_end(random_string):
    ''' Test substring if start is larger than end
    
        (1) stores the actual and expected results of the equality
        (2) calls print_test with string version of test, result of the actual
            test, and expected result
        (3) assert required by pytest
    '''

    with pytest.raises(ValueError) as exception_info:
        String(random_string).substring(7, 3) #This should produce value error
    result   = type(exception_info.value)   # if correct, result should be IndexError
    expected = ValueError

    print_test(f"String('{sample_String1}').substring(3, 7) + '{sample_string1}'", \
            result = result, expected = expected)
    assert(result == expected)


##############################################################################
##############################################################################

##############################################################################
# this test gives an example of how to look for accessing-element exceptions
#
# def test_getitem_first_on_empty_String(empty_string):
#     ''' pytest test for accessing [0] entry in an empty string
#         (1) uses 'with pytest.raises' to look for appropriate raised exception,
#             which is raised by the indented code
#         (2) stores the type of the value of the raised exception
#         (3) calls print_test with string version of test, result of the actual
#             test, and expected result
#         (3) assert required by pytest
#     '''
#     with pytest.raises(IndexError) as exception_info:
#         String(empty_string)[0]             # this should raise an IndexError
#     result   = type(exception_info.value)   # if correct, result should be IndexError
#     expected = IndexError
#     print_test(f'String("{empty_string}")[0]', \
#                result = result, expected = expected)
#     assert(result == expected)

##############################################################################
##############################################################################

# plenty more tests go here...

##############################################################################
##############################################################################

##############################################################################
# this test gives an example of how to look for modifiying-element exceptions
#
# def test_setitem_first_on_empty_String(empty_string):
#     ''' pytest test for setting [0] entry in an empty string
#         (1) uses 'with pytest.raises' to look for appropriate raised exception,
#             which is raised by the indented code
#         (2) stores the type of the value of the raised exception
#         (3) calls print_test with string version of the test, result of the
#             actual test, and expected result
#         (3) assert required by pytest
#     '''
#     string = String(empty_string)  # first need a construction...
#     with pytest.raises(IndexError) as exception_info:
#         string[0] = '❤'            # this should raise an IndexError
#     result   = type(exception_info.value)
#     expected = IndexError
#     print_test(f'String("{empty_string}")[0] = \'❤\'', \
#                result = result, expected = expected)
#     assert(result == expected)

##############################################################################
##############################################################################

# plenty more tests go here...

##############################################################################
##############################################################################
