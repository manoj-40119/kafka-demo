from faker import Faker
fake = Faker()
x=10
while(x!=0):
    message = {
        'name': fake.name(),
        'address': fake.address(),
        'phone': fake.phone_number()
    }
    print(message)
    x=x-1