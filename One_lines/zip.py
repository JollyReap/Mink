
list1  =  [1, 2, 3]
list2  =  [4, 5, 6]

# Упаковка
zipped =  list(zip(list1, list2))

# Распаковка
new_lst1, new_lst2 = zip(*zipped)

# Теперь представим что надо упоковать мини бд
column_names = ['name', 'job', 'sallary']
db_rows = [('Petya', 300000, 'data_sciencest'),
           ('Bob', 'free', 'frontend_developer'),
           ('Tad', 40000, 'django_developer')]

# Запихнём в однострочник
db = [dict(zip(column_names, row)) for row in db_rows]

# Result
print(db)