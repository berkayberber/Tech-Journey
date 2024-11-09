import random

from experta import *

class CoffeeMaker(Fact):
    brand_name = Field(str)
    model =  Field(str)
    pass


class Cause(Fact):
    pass


class Action(Fact):
    pass


class Error(Fact):
    error_code = Field(str)
    support_code = Field(int)
    pass


class CoffeeMaker(KnowledgeEngine):

    @Rule(Error(error_code = "E00",support_code = 200))
    def out_of_milk(self):
        self.declare(Cause("Coffee maker is out of milk."))

    @Rule(OR(Error(error_code = "E00",support_code = 2001),
             Error(error_code = "E00",support_code = 2002),
             Error(error_code = "E00",support_code = 2003)))
    def milk_supply_issue(self):
        self.declare(Cause("Coffee maker is out of milk or experiencing milk-related issues."))

    @Rule(OR(Error(error_code="E02", support_code=1001),
             Error(error_code="E10", support_code=1002),
             Error(error_code="E15", support_code=1003),
             Error(error_code="E22", support_code=1004)))
    def handle_multiple_errors(self):
        self.declare(Cause("Multiple errors detected. Your coffee maker needs repair. Please contact customer support."))

    @Rule(Error(error_code="E01", support_code=301))
    def coffee_grinder_error(self):
        self.declare(Cause("Coffee funnel blockage."))

    @Rule(OR(Error(error_code="E03", support_code=401), Error(error_code="E04", support_code=402)))
    def brew_group_error(self):
        self.declare(Cause("brew group error."))

    @Rule(Error(error_code="E05", support_code=501))
    def Air_trapped_error(self):
        self.declare(Cause("Air is trapped in the water circuit."))

    @Rule(Error(error_code="E14", support_code=601))
    def overheated_error(self):
        self.declare(Cause("The machine is overheated."))

    @Rule(AND(Error(error_code="E11", support_code=701), Error(error_code="E19", support_code=702)))
    def temperature_error(self):
        self.declare(Cause("Machine is too cold."))

    #------------------ACTIONS----------------------

    @Rule(Cause("Coffee maker is out of milk."))
    def act_load_milk(self):
        print("Load milk to coffee machine.")

    @Rule(Cause("Coffee maker is out of milk or experiencing milk-related issues."))
    def act_milk_supply_issue(self):
        print("Action: Refill the milk container or check for milk-related issues.")

    @Rule(Cause("Multiple errors detected. Your coffee maker needs repair. Please contact customer support."))
    def act_multiple_errors(self):
        print("Action: Contact customer support to repair your coffee maker.")

    @Rule(Cause("Coffee funnel blockage."))
    def act_coffee_grinder_error(self):
        print("Perform actions to unblock the coffee funnel.")

    @Rule(Cause("brew group error."), Error(error_code="E03"))
    def act_brew_group_error401(self):
        print("There is too much dirt on the brew group.")

    @Rule(Cause("brew group error."), Error(error_code="E04"))
    def act_brew_group_error402(self):
        print("Brew group not correctly placed.")

    @Rule(Cause("Air is trapped in the water circuit."))
    def act_air_trapped_error(self):
        print("Switch OFF the machine.")

    @Rule(Cause("The machine is overheated."))
    def act_overheated_error(self):
        print("Switch OFF the machine and wait for 2 minutes.")

    @Rule(Cause("Machine is too cold."), Error(error_code="E11"), Error(error_code="E19"))
    def act_temperature_error(self):
        print("Switch OFF the machine and wait 30 minutes")

error_codes = [
    ("E00",200),
    ("E00",2001),
    ("E00",2002),
    ("E00",2003),
    ("E02",1001),
    ("E10",1002),
    ("E15",1003),
    ("E15",1004),
    ("E01",301),
    ("E03",401),
    ("E05",501),
    ("E14",601),
    ("E11",701),
    ("E19",702),
]

engine = CoffeeMaker()
engine.reset()
#engine.declare(Error(error_code = "E01",support_code = 301))
engine.declare(Error(error_code = "E11",support_code = 701))  #and condition (if both occurrred than print the error message example.)
engine.declare(Error(error_code = "E19",support_code = 702))
facts = engine.facts
engine.run()
print(facts)
