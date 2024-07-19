from smartphone import Smartphone

catalog = []
phone1 = Smartphone("Apple", "iPhone 5S", "+79218885533")
phone2 = Smartphone("Samsung", "Galaxy S5", "+79898955305")
phone3 = Smartphone("Siemens","A35", "+79285553535")
phone4 = Smartphone("Nokia", "1100", "+79659652147")
phone5 = Smartphone("SonyEricsson", "G900", "+79286491295")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. - {phone.phone_number}")