date = '05.17.2016'
print(date[3:6] + date[0:3] + date[6:])


name = 'Mark Zuckerberg'
print(name[-10:] + name[-11] + name[-15:-11])

name_2 = 'Mark Zuckerberg'
name_2_lst = name_2.split(' ')
name_2_lst = name_2_lst[::-1]
reverse = ' '.join(name_2_lst)
print(reverse)

snake_case = 'employee_first_name'
camel_case = snake_case.split('_')
print(camel_case[0].capitalize() + camel_case[1].capitalize() + camel_case[2].capitalize())


