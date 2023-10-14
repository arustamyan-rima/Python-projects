"""
Parse list

1. write a function list_parse(), which takes a list of strings, tries to parse them as
floats and returns a list of floats. There are also strings in the list that use the 
comma as a decimal separator, these must also be taken into account.
2. all input strings that cannot be parsed to float are collected in an error list.
 This must contain the original strings.

The return value of the funcition is a tuple of resultlist and errorlist.


Example:
a = ["2", "a3", "0.2", "0,4", "a01", "3", ",", "a.a", "a,"]

Result:
b = [2.0, 0.2, 0.4, 3.0]
errorlist = ['a3', 'a01', ',', 'a.a', 'a,']

"""


a = ["2", "0,4", "0.2", "a3", "a01", "3", ",", "a.a", "a,a"]

def list_parse(x:list) -> tuple:
    resultlist = []
    errorlist = []
    for i in x:
        try:
            i = float(i)
            resultlist.append(i)
        except ValueError:
            try:
                new_i = i.replace(',', '.')
                resultlist.append(float(new_i))
            except:
                errorlist.append(i)
        except:
            errorlist.append(i)
    return resultlist, errorlist 


B = list_parse(a)
print(B)

