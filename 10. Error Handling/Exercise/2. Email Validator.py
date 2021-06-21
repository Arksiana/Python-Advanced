domain_list = [".com", ".org", ".bg", ".net"]
is_valid = True


class MustContainAtSymbolError(Exception):
    pass


class NameTooShortError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


while True:
    command = input()
    if command == 'End':
        break

    if '@' not in command:
        is_valid = False
        raise MustContainAtSymbolError("Email must contain @")
    else:
        name, rest = command.split('@')
        server, domain = rest.split('.')
        domain = '.' + domain

    if domain not in domain_list:
        is_valid = False
        raise InvalidDomainError('Domain must be one of the following: .com, .bg, .org, .net')

    if len(name) <= 4:
        is_valid = False
        raise NameTooShortError('Name must be more than 4 characters')

    if is_valid:
        print('Email is valid')
