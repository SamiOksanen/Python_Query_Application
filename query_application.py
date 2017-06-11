customers = open('customer_data.csv')
data = customers.readlines()
customer_list = [line[:-1].split(';') for line in data]


def get(name):
    found = False
    for person in customer_list:
        if person[1] == name:
            print(person)
            found = True
    if found is False:
        print('not found')


def post(name, email, phone_number):
    if len(phone_number) <= 12 and phone_number[0] != '0' and len(name) <= 25:
        try:
            id = 0
            for i in customer_list:
                if id <= int(i[0]):
                    id = int(i[0]) + 1
            customer_list.append([str(id), name, email, phone_number])
        except ValueError:
            return 0


def delete(name):
    for person in customer_list:
        if person[1] == name:
            customer_list.remove(person)


def save():
    result = ''
    for person in customer_list:
        result += '' + person[0] + ';' + person[1] + ';' + person[2] + ';' + person[3] + '\n'
    n_write = open('customer_data.csv', 'w')
    n_write.write(result)
    n_write.close()


def make_queries():
    while True:
        query = input().split()
        if query[0] == 'get':
            get(query[1])
        elif query[0] == 'post':
            post(query[1], query[2], query[3])
        elif query[0] == 'del':
            delete(query[1])
        elif query[0] == 'save':
            save()
        elif query[0] == 'exit':
            break

make_queries()
