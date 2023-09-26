import math

class verificationcode:
    def __init__(self, first_name: str, last_name: str, id: str):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
    
    def __check_first_name(self) -> bool:
        if self.first_name[:2].upper() == self.id[2:4].upper():
            return True
        return False
    
    def __check_last_name(self) -> bool:
        if self.last_name[2:4].upper() == self.id[:2].upper():
            return True
        return False
    
    def __check_id(self) -> bool:
        year = self.id[4:8]
        month = self.id[8:10]
        employee_number = self.id[10:12]
        last_digit = self.id[12:13]
        numeric_part = self.id[4:12]
        
        sum_odd = 0
        sum_even = 0
        for i in range(len(numeric_part)):
            if i % 2 == 0:
                sum_odd += int(numeric_part[i])
            else:
                sum_even += int(numeric_part[i])

        diff = abs(sum_odd - sum_even)
        diff = (diff % 9) if diff > 9 else diff
        return True if diff == int(last_digit) else False


    
    def check_valid(self) -> str:
        if self.__check_first_name() and self.__check_first_name() and self.__check_id():
            return "PASS"
        return "INVESTIGATE"



test = verificationcode("Jigarius", "Caesar", "CAJI202002196")
rtrn = test.check_valid()
print(rtrn)