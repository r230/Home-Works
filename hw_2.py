date = '05.17.2016'
print(date[3:6] + date[0:3] + date[6:])


name = 'Mark Zuckerberg'
print(name[-10:] + name[-11] + name[-15:-11])


snake_case = 'employee_first_name'
camel_case = snake_case.split('_')
print(camel_case[0].capitalize() + camel_case[1].capitalize() + camel_case[2].capitalize())


user_data = 'Marcus Aurelius*121-04-26*180-03-17'
list = user_data.split('*')
first_date = list[1]
second_date = list[2]
born_year = first_date.split('-')[0]
death_year = second_date.split('-')[0]
age = int(death_year) - int(born_year)
print(list[0] + ',', age)

user_data = 'Leo Tolstoy*1828-08-28*1910-11-20'
list = user_data.split('*')
first_date = list[1]
second_date = list[2]
born_year = first_date.split('-')[0]
death_year = second_date.split('-')[0]
age = int(death_year) - int(born_year)
print(list[0] + ',', age)
