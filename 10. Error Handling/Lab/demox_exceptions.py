def raise_exception(ExceptionType):
    raise ExceptionType()


try:
    raise_exception(ValueError)
except TypeError:
    print('Handled with TypeError')
except ValueError:
    print('Handled with ValueError')
except:
    print('Handle in except')
