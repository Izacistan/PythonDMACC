class Invoice:
    def __init__(self, invoice_id, customer_id, last_name, first_name, phone_number, address, items_with_price = {}):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        phone_number_characters = set("1234567890-()")
        customer_id_characters = set("1234567890")
        if not (name_characters.issuperset(last_name) and name_characters.issuperset(first_name)):
            raise ValueError
        if not phone_number_characters.issuperset(phone_number):
            raise ValueError
        if not customer_id_characters.issuperset(customer_id):
            raise ValueError
        self.invoice_id = invoice_id
        self.customer_id = customer_id
        self.last_name = last_name
        self.first_name = first_name
        self.phone_number = phone_number
        self.address = address
        self.items_with_price = items_with_price

    def __str__(self):
        return f"Invoice ID: {self.invoice_id}\nCustomer ID: {self.customer_id}\nLast Name: {self.last_name}\nFirst Name: {self.first_name}\nPhone Number: {self.phone_number}\nAddress: {self.address}\nItems with Price: {self.items_with_price}"

    def __repr__(self):
        return f"{type(self.invoice_id)} - {self.invoice_id}, {type(self.customer_id)} - {self.customer_id}, {type(self.last_name)} - {self.last_name}, {type(self.first_name)} - {self.first_name}, {type(self.phone_number)} - {self.phone_number}, {type(self.address)} - {self.address}, {type(self.items_with_price)} - {self.items_with_price}"

    def add_item(self, item):
        self.items_with_price.update(item)

    def create_invoice(self):
        subtotal = 0
        TAX_RATE = 0.06

        #Calculate subtotal
        for i in self.items_with_price:
            subtotal += self.items_with_price[i]

        #Get total after tax
        tax = subtotal * TAX_RATE
        total = tax + subtotal

        #Iterate through dictionary and display message
        for i in self.items_with_price:
            print(f"{i}.....${self.items_with_price[i]}")
        print(f"Tax.....${round(tax)}\nTotal.....${round(total, 2)}")

# Driver code

#Runs CORRECTLY
invoice = Invoice("1", "123", 'Mouse', 'Minnie', '555-867-5309', '1313 Disneyland Dr, Anaheim, CA 92802')
# repr(invoice)

#THROWS A VALUE ERROR
#invoice = Invoice("1", "123", '1313 Disneyland Dr, Anaheim, CA 92802' ,'Mouse', 'Minnie', '555-867-5309')
invoice.add_item({'iPad': 799.99})
invoice.add_item({'Surface': 999.99})
invoice.create_invoice()