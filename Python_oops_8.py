# Multilevel Inheritence

class Dad:
    basketball = 6

class Son(Dad):
    dance = 1
    basketball = 9
    def isdance(self):
        return f'Yes I dance {self.dance} no of times'

class Grandson(Son):
    dance = 6
    def isdance(self):
        return f"Jackson Yeah!" \
            f"Yes I dance very awsomely {self.dance} no of times"

papa = Dad()
beta = Son()
pota = Grandson()
print(pota.basketball)
print(pota.isdance())
print(beta.isdance())