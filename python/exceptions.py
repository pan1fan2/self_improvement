x = -5
if x > 0:
    raise Exception('x should be positive')

# assert(x >= 0), 'x is not positive'

# try:
#     a = 5 / 0
# # except:
# #     print('error')
# except Exception as e:
#     print(e) #division by zero


# try:
#     a = 5 / 1
#     b = a + '10'
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e) #unsupported operand type(s) for +: 'float' and 'str'
# else:
#     print('everything is fine')
# finally:
#     print("cleaning up...")


class ValueTooHighError(Exception):
    def __init__(self,message,value):
        self.message = message
        self.value = value

def test_value(x):
    if x > 100:
        raise ValueTooHighError('Value is too high',x)

try:
    test_value(200)
except ValueTooHighError as e:
    print(f"The error message is : {e.message}, the input is : {e.value}.")


