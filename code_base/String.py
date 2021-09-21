class String:
    '''DCS 229 implementation of a version of the built-in str class.

    This class implements a simple version corresponding to the str class,
    where a String object consists of a sequence of characters.

    Attributes:
        __str__    : returns an str version of this String object
        len        : returns the (int) number of characters in this String
        is_empty   : returns True if this String is an empty string; False o/w
        __eq__     : allows comparison of this String vs. either a String or str
        __getitem__: allows fetching a character using [] notation
        __setitem__: allows overwriting a character using [] assignment
        __add__    : returns a new String object that is the concatenation of
                        this String object and a given String or str object
        substring  : returns a new String object by specifying substring indices
    '''

    ''' Notes on type hints below:
        - A parameter type hint is specified by : and type following the param
                def method(self, param: type)
        - A method return type hint is specified by an arrow between ) and :
                def method(self) -> type:
        - Python itself does not enforce type hints, but these can be checked
          by type checkers such as mypy.
        - As the String class does not yet exist, the standard approach is
          to use 'String' which is understood by type checkers as a lookahead.
        - Python 3.10 allows "or" support a la 'String' | str.  To fake this
          support in the presence of < 3.10 versions of Python, we are using
          'String | str' here (rather than the suggested Union['String', str]
          approach) for convenience and brevity. 
    '''

    __slots__ = ('_chars')

    #####################################################
    def __init__(self, string: str) -> None:
        ''' initialization method for the String class

        Args:
            string: a str type used to initialize the String

        Returns:
            None
        '''
        self._chars = [c for c in string]  # a list of characters in the str

    #####################################################
    def __str__(self) -> str:
        ''' overrides the __str__ special method for conversion to str

        Returns:
            an str version of the String object contents
        '''
        string = "".join(self._chars)
        return string

    #####################################################
    def len(self) -> int:
        ''' returns the number of characters present in the String object

        Returns:
            an int representing the number of character in the String
        '''
        # string_length = 0
        # for c in self._chars:
        #     string_length += 1
        # return string_length

        return len(self._chars)

    #####################################################
    def is_empty(self) -> bool:
        ''' Boolean method indicating whether the String is an empty string

        Returns:
            True if no characters are present in the String; False o/w
        '''
        if self.len() == 0:
            return True
        else:
            return False

    #####################################################
    def __eq__(self, other: 'String | str') -> bool:  # faking Python 3.10 support for hints
        ''' overrides the __eq__ special method for comparing two String
            objects, or for comparing a String object and an str object

        Args:
            other: a separate String or str object for comparing

        Returns:
            True if the two objects contain exactly the same characters in
            the same order; False o/w
        '''

        # make sure to allow comparison when other is either String or str
        otherString = other.__str__() if isinstance(other, String) else other

        #Compare the number of characters
        if self.len() != len(otherString): return False

        #Bail out when there is a different
        for index, c in enumerate(self._chars):
            if otherString[index] != c: return False

        return True

    #####################################################
    def __getitem__(self, index: int) -> str:
        ''' overrides the __getitem__ special method, allowing [] access
            into a String object to access a single character (str)

        Args:
            index: an integer indicating the position of the character to fetch

        Returns:
            the character (a str in Python) at the indicated position

        Raises:
            IndexError: if the index value is invalid relative to String length
        '''
        pass

    #####################################################
    def __setitem__(self, index: int, char: str) -> None:
        ''' overrides the __setitem__ special method, allowing one to overwrite
            a character at a specific index in the String

        Args:
            index: an integer indicating the position of the character to overwrite

        Returns:
            None

        Raises:
            IndexError: if the index value is invalid relative to String length
        '''
        pass

    #####################################################
    def __add__(self, other: 'String | str') -> 'String':
        ''' overrides the __add__ special method, allowing one to add
            (concatenate) two String objects, or to concatenate an str object
            to a String object; this String and other should remain unchanged

        Args:
            other: a String or str object to append to this String

        Returns:
            a String object represent the concatenation of the two strings
        '''
        #Create a new string to not modify the current one
        newCharArray = self._chars[:] #Slice to copy
        otherString  = other.__str__() if isinstance(other, String) else other #Check instance
        otherCharArr = [c for c in otherString]

        newCharArray.extend(otherCharArr) 
        
        return String(newCharArray)

    #####################################################
    def substring(self, start: int, end: int) -> 'String':
        ''' overrides the __add__ special method, allowing one to add
            (concatenate) two String objects, or to concatenate an str object
            to a String object; this String and other should remain unchanged

        Args:
            other: a String or str object to append to this String

        Returns:
            a String object represent the concatenation of the two strings
        '''
        if start >= end: raise ValueError("Start index cannot be larger or equal to end")

        newChars = self._chars[start : end]
        #ddads
        return String("".join(newChars))