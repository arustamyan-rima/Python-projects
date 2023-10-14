"""
Write a function add that adds keyword arguments to a Telephone
book dictionary.
At the bottom of the code is a telephone book with two entries so far for viewing.

The call to the function:

add(first_name="Fritz", last_name="Cat", phone="1234567890")


If the keyword argument normalize=True is passed AND also
the keyword argument phone is given, the phone number will be normalized.
Important: the normalize argument must not be passed into the dict.

    add(first_name="BoB", last_name="Dog", phone="0049338900", normalize=True)

normalize_phone_number
--------------------------------------------------------------
Two null characters at the beginning: replace the null characters with +.
one null character at the beginning: remove null, keep number
otherwise keep number

To do this, write the normalize_phone_number() function.
Examples:
1234567890 => 1234567890
00249234230 => +249234230
0249234230 => 249234230

the return value of the function is the normalized phone number.
--------------------------------------------------------------

"""


def normalize_phone_number(number):
    """Normalize Telephone number.

    Args:
        number (str): unnormalized telephone number

    Returns:
       str: normalized telephone number
    """
    if number[0] != '0':
        return number
    else: 
        if number[1] != '0':
            return number[1:len(number)]
        return '+' + number[2:len(number)]


telephone_book = {}


def add(**kwargs):
    """Add number to telephonebook dict."""
    if "normalize" in kwargs.keys():
        if kwargs['normalize'] == True and 'phone' in kwargs.keys():
            kwargs["phone"] = normalize_phone_number(kwargs['phone'])
        kwargs.pop('normalize')
    telephone_book[kwargs['first_name']] = kwargs


add(first_name="Fritz", last_name="Cat", phone="1234567890")
add(first_name="BoB", last_name="Dog", phone="0049338900", normalize=True)
add(first_name="Goofy", last_name="Horse", phone="0049338900", normalize=False)
add(first_name="Bobby", last_name="Blue", normalize=True)
print(telephone_book)
