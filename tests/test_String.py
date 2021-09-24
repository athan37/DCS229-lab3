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
            if isinstance(expected, String): expected = expected.__str__()
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

###############################################################################
# Added description of what the fixture actually does, consistent with previous
# fixtures
# Thomas added on 9/21/2021
###############################################################################

@pytest.fixture
def sample_String1(sample_string1):
    ''' pytest fixture that creates a String object using sample_string1

    Args:
        sample_string1: pytest fixture (above) that generates a specific string

    Returns:
        a String object containing the characters in sample_string1
    '''
    return String(sample_string1)

@pytest.fixture
def sample_String2(sample_string2):
    ''' pytest fixture that creates a String object using sample_string2

    Args:
        sample_string2: pytest fixture (above) that generates a specific string

    Returns:
        a String object containing the characters in sample_string2
    '''
    return String(sample_string2)

@pytest.fixture
def string_from_0_to_9():
    ''' pytest fixture that creates an str containing the numbers 0 through 9

    Args:

    Returns:
        an str consisting of the numbers 0 through 9
    '''
    return "0123456789"

###############################################################################

#####################################
# Testing __init__(self, string: str)
#####################################

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

###################################
#Testing __str__(self, string: str)
###################################

def test_conversion_on_simple_string(simple_random_string):
    ''' pytest test for str conversion of a random simple String object
        (1) stores the actual and expected results of the conversion
        (2) calls print_test with string version of test, result of the actual
            test, and expected result
        (3) assert required by pytest
    '''
    result = str(String(simple_random_string))
    expected = simple_random_string
    print_test(f"str(String({simple_random_string}))", \
               result = result, expected = expected)
    assert(result == expected)

def test_conversion_on_random_string(random_string):
    ''' pytest test for str conversion of a random String object
        (1) stores the actual and expected results of the conversion
        (2) calls print_test with string version of test, result of the actual
            test, and expected result
        (3) assert required by pytest
    '''
    result = str(String(random_string))
    expected = random_string
    print_test(f"str(String({random_string}))", \
               result = result, expected = expected)
    assert(result == expected)

def test_conversion_on_empty_string(empty_string):
    ''' pytest test for str conversion of an empty String object
        (1) stores the actual and expected results of the conversion
        (2) calls print_test with string version of test, result of the actual
            test, and expected result
        (3) assert required by pytest
    '''
    result = str(String(empty_string))
    expected = empty_string
    print_test(f"str(String({empty_string}))", \
               result = result, expected = expected)
    assert(result == expected)

##############################################################################

###################
# Testing len(self)
###################

def test_length_on_random_string(random_string):
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

def test_length_on_empty_string(empty_string):
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

#######################
#Testing is_empty(self)
#######################

def test_is_empty_on_empty_string(empty_string):
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

def test_is_empty_on_random_string(random_string):
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

##############################################################################

############################################
#Testing __eq__(self, other: 'String | str')
############################################

def test_is_equal_on_predetermined_String(sample_String1, sample_String2):
    ''' pytest test to determine whether two str objects are equal
        (1) stores the actual and expected results of the equality
        (2) calls print_test with string version of test, result of the actual
            test, and expected result
        (3) assert required by pytest
    '''

    ##########################################
    # Fixed code that intially was not working
    # Thomas on 9/21/2021
    ##########################################

    result = sample_String1 == sample_String2
    expected = False
    print_test(f"String({sample_String1}) == String({sample_String2})", \
               result = result, expected = expected)
    assert(result == expected)

###########################
# Thomas added on 9/21/2021
###########################

def test_is_equal_on_predetermined_string(sample_string1, sample_String2):
    ''' pytest test to determine whether two str objects are equal
        (1) stores the actual and expected results of the equality
        (2) calls print_test with string version of test, result of the actual
            test, and expected result
        (3) assert required by pytest
    '''
    result = sample_string1 == sample_string2
    expected = False
    print_test(f"String({sample_string1}) == String({sample_string2})", \
               result = result, expected = expected)
    assert(result == expected)

##############################
#Duc Anh added on 9/20/2021
#Thomas formatted on 9/21/2021
##############################

def test_is_equal_on_empty_str_and_empty_String(empty_string):
    ''' pytest test to see if an empty string from class String equals
        an empty string from class 'str'
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

##############################################################################

#############################################
#Testing __add__(self, other: 'String | str')
#############################################

def test_add_on_empty_String_and_empty_str(empty_string):
    ''' pytest test that adds an empty String object to an
        empty str object
        (1) stores the actual and expected results of the sum
        (2) calls print_test with string version of test, result of the actual
            test, and expected result
        (3) assert required by pytest
    '''
    result = String(empty_string) + ''
    expected = String(empty_string)

    print("Result type", type(result), "Expected type:", type(expected))
    print_test(f"String('{empty_string}') + '' ",\
            result = result, expected = expected)

    assert(result == expected)

def test_add_on_String_and_other_String(sample_String1, sample_String2, sample_string1, sample_string2):
    ''' pytest test that adds 2 String objects
        (1) stores the actual and expected results of the sum
        (2) calls print_test with string version of test, result of the actual
            test, and expected result
        (3) assert required by pytest
    '''
    result   = sample_String1 + sample_String2
    expected = String(sample_string1 + sample_string2)
    print_test(f"String('{sample_string1}') + String('{sample_string2}')", \
               result = result, expected = expected)
    assert(result == expected)

def test_add_on_String_and_other_str(sample_String1, sample_string1, sample_string2):
    ''' pytest test that adds a String object to an str object
        (1) stores the actual and expected results of the sum
        (2) calls print_test with string version of test, result of the actual
            test, and expected result
        (3) assert required by pytest
    '''
    result   = sample_String1 + sample_string2
    expected = String(sample_string1 + sample_string2)
    print_test(f"String('{sample_String1}') + '{sample_string2}'", \
               result = result, expected = expected)
    assert(result == expected)

def test_add_on_String_and_empty_str(sample_String1, empty_string):
    ''' pytest test that adds a String object to an empty str object
        (1) stores the actual and expected results of the sum
        (2) calls print_test with string version of test, result of the actual
            test, and expected result
        (3) assert required by pytest
    '''
    result   = sample_String1 + empty_string
    expected = sample_String1
    print_test(f"String('{sample_string1}') + '{empty_string}'", \
               result = result, expected = expected)
    assert(result == expected)

##############################################################################


def test_substring_from_0_to_0_of_an_empty_string(empty_string):
    ''' pytest test that uses substring on an empty str object
        (1) stores the actual and expected results of the substring
        (2) calls print_test with string version of test, result of the actual
            test, and expected result
        (3) assert required by pytest
    '''
    result   = String(empty_string).substring(0, 1)
    expected = String(empty_string)
    print_test(f"String('{empty_string}').substring(0, 1)", \
               result = result, expected = expected)
    assert(result == expected)

def test_substring_from_3_to_7_of_a_String(sample_string1):
    ''' pytest test that uses substring on a String object
        (1) stores the actual and expected results of the substring
        (2) calls print_test with string version of test, result of the actual
            test, and expected result
        (3) assert required by pytest
    '''
    result   = String(sample_string1).substring(3, 7)
    expected = String(sample_string1[3:7])
    print_test(f"String('{sample_String1}').substring(3, 7)", \
               result = result, expected = expected)
    assert(result == expected)

def test_substring_from_minus_7_to_minus_3_of_a_String(string_from_0_to_9):
    ''' pytest test that uses substring on a String object
        (1) stores the actual and expected results of the substring
        (2) calls print_test with string version of test, result of the actual
            test, and expected result
        (3) assert required by pytest
    '''
    result   = String(string_from_0_to_9).substring(-7, -3)
    expected = String("3456")
    print_test(f"String('{string_from_0_to_9}').substring(-7, -3)", result = result, expected = expected)
    assert(result == expected)


def test_substring_from_minus_3_to_minus_3_of_a_String(random_string):
    ''' pytest test that uses 
    '''
    result = String(random_string).substring(-3,-4)
    expected = ""
    print_test(f"String('{random_string}').substring(-3,-4)", \
               result = result, expected = expected)
    assert(result == expected)

##############################################################################
##############################################################################

######################################
#Testing __getitem__(self, index: int)
######################################
def test_get_item_when_index_equals_length(random_string):
    ''' test when user tries to get an index that is larger than the length - 1
        (1) stores the actual and expected results of the substring
        (2) calls print_test with string version of test, result of the actual
            test, and expected result
        (3) assert required by pytest
    '''
    with pytest.raises(IndexError) as exception_info:
        random_string[len(random_string)]

    result   = type(exception_info.value)   # if correct, result should be IndexError
    expected = IndexError
    print_test(f"__getitem__(len(String('{random_string}''))", \
            result = result, expected = expected)
    assert(result == expected)

def test_getitem_first_on_empty_String(empty_string):
    ''' pytest test for accessing [0] entry in an empty string
        (1) uses 'with pytest.raises' to look for appropriate raised exception,
            which is raised by the indented code
        (2) stores the type of the value of the raised exception
        (3) calls print_test with string version of test, result of the actual
            test, and expected result
        (3) assert required by pytest
    '''
    with pytest.raises(IndexError) as exception_info:
        String(empty_string)[0]             # this should raise an IndexError
    result   = type(exception_info.value)   # if correct, result should be IndexError
    expected = IndexError
    print_test(f'String("{empty_string}")[0]', \
               result = result, expected = expected)
    assert(result == expected)

def test_getitem_out_of_range_on_random_String(random_string):
    ''' pytest test for accessing [21] entry in a random string
        (1) uses 'with pytest.raises' to look for appropriate raised exception,
            which is raised by the indented code
        (2) stores the type of the value of the raised exception
        (3) calls print_test with string version of test, result of the actual
            test, and expected result
        (4) assert required by pytest
    '''
    with pytest.raises(IndexError) as exception_info:
        String(random_string)[21]
    result   = type(exception_info.value)
    expected = IndexError
    print_test(f'String("{random_string}")[21]', \
               result = result, expected = expected)
    assert(result == expected)

def test_getitem_first_on_simple_String(sample_String1):
    ''' pytest test for accessing [0] entry in a random string
        (1) stores the actual and expected results for the first item
        (2) calls print_test with string version of test, result of the actual
            test, and expected result
        (3) assert required by pytest
    '''
    result = sample_String1[0]
    expected = '1'
    print_test(f"String('{sample_string1}')[0]", \
               result = result, expected = expected)
    assert(result == expected)

##############################################################################
##############################################################################

#################################################
#Testing __setitem__(self, index: int, char: str)
#################################################

def test_setitem_first_on_empty_String(empty_string):
    ''' pytest test for setting [0] entry in an empty string
        (1) uses 'with pytest.raises' to look for appropriate raised exception,
            which is raised by the indented code
        (2) stores the type of the value of the raised exception
        (3) calls print_test with string version of the test, result of the
            actual test, and expected result
        (3) assert required by pytest
    '''
    string = String(empty_string)  # first need a construction...
    with pytest.raises(IndexError) as exception_info:
        string[0] = '❤'            # this should raise an IndexError
    result   = type(exception_info.value)
    expected = IndexError
    print_test(f'String("{empty_string}")[0] = \'❤\'', \
               result = result, expected = expected)
    assert(result == expected)

def test_setitem_second_on_String(sample_String1):
    ''' pytest test for setting [0] entry in an empty string
        (1) uses 'with pytest.raises' to look for appropriate raised exception,
            which is raised by the indented code
        (2) stores the type of the value of the raised exception
        (3) calls print_test with string version of the test, result of the
            actual test, and expected result
        (3) assert required by pytest
    '''
    string = sample_String1  # first need a construction...
    string[2] = '$'
    result = string
    expected = "1h$2beropijsdf"
    print_test(f'String("{empty_string}")[2] = \'$\'', \
            result = result, expected = expected)
    assert(result == expected)

def test_setitem_firt_on_index_value_greater_than_String(sample_String2):
    ''' pytest test for setting [0] entry in an empty string
        (1) uses 'with pytest.raises' to look for appropriate raised exception,
            which is raised by the indented code
        (2) stores the type of the value of the raised exception
        (3) calls print_test with string version of the test, result of the
            actual test, and expected result
        (4) assert required by pytest
    '''
    string = sample_String2  # first need a construction...
    with pytest.raises(IndexError) as exception_info:
        string[27] = '&'            # this should raise an IndexError
    result   = type(exception_info.value)
    expected = IndexError
    print_test(f'String("{empty_string}")[27] = \'&\'', \
            result = result, expected = expected)
    assert(result == expected)
