class Hangaar:
    def __init__(self,aircraft_model, prod_year, aircraft_value):
        self.aircraft_model = aircraft_model
        self.prod_year = prod_year
        self.aircraft_value = aircraft_value

    def display(self):
        return "AIRCRAFT\nModel: {}\nProduction Year: {}\nValue: {}Million $\n".format(self.aircraft_model,self.prod_year,self.aircraft_value)

class Market:
    pass
    def __init__(self):
        pass

model_1 = Hangaar("Boeing 777", "1997", 500)
model_2 = Hangaar("Airbus A380", "2006", 800)
model_3 = Hangaar("Concord", "2002", 1200)

print(model_1.display())
print(model_2.display())
print(model_3.display())