# def
def print_greeting():
    """
    print 'hello!' text
    :return: None
    """
    print('hello!')


# call the func
print_greeting()

# receive the description of the func
help(print_greeting)


def print_greeting_with_name(name='Name'):
    print('hello ' + name + ' !')


print_greeting_with_name('jack')
print_greeting_with_name()
print_greeting_with_name('jane')


def sum_of_two_number(a=0, b=0):
    return a+b


x = sum_of_two_number(1, 1)
print(x)


def is_hello_in_text(text):
    if 'hello' in text.lower():
        return True
    else:
        return False


print(is_hello_in_text('hello everyone!'))


def is_str_in_text(string, text):
    return string in text


print(is_str_in_text('abc', 'avcfd'))


def greeting_depends_on_gender(name, gender):
    if gender == 'male':
        print('Hello ' + name + 'You are looking great!')
        return gender
    elif gender == 'female':
        print('Hello ' + name + 'You are so nice!')
        return gender
    else:
        print('Hello ' + name + 'I\'ve never seen the creature like you!')
        return gender


returned_velue_1 = greeting_depends_on_gender('jake ', 'male')
returned_velue_2 = greeting_depends_on_gender('jame ', 'fgd')
returned_velue_3 = greeting_depends_on_gender('jane ', 'female')
print(returned_velue_1)
print(returned_velue_2)
print(returned_velue_3)


def cat_voice():
    print('Meow!')


def dog_voice():
    print('woof!')


dog_voice()
cat_voice()


def cat_voice(cat_choice):
    return cat_choice * 2


def dog_voice(dog_choice):
    return dog_choice * 2


print(cat_voice(' Meow!'))
print(dog_voice(' Woof!'))


def name(name='Jane'):
    return name


print(name())


def odd_number(a, b):
    a = [odd for odd in range(0, 11) if odd % 2 == 0]
    b = [odd for odd in range(0, 11) if odd % 2 == 0]
    return a, b


print(list(odd_number(range(1, 11), range(0, 6))))


def get_odd_number_list(a, b):
    number_list = list(range(a, b + 1))
    odd_number_list = [number for number in number_list if number % 2 == 1]
    return odd_number_list


get_odd_number_list(a, b)
