class Number:
    debug = False
    def __init__(self, number=""):
        self.number = number
        self.index = 0
    def __add__(self, other):
        newnum = Number()
        remainder = 0
        current_sum = 0

        self_number = self.number
        other_number = other.number

        # zero pad the smaller number
        if len(self.number)>=len(other.number):
            
            while len(other_number)<len(self_number):
                other_number = "0" + other_number
        else:
            
            while len(self_number)<len(other_number):
                self_number = "0" + self_number
        
        # reassign the zero padded numbers back to their objects
        self.number = self_number
        other.number = other_number

        if self.debug: print("self_number is: '"+self_number+"' and other_number is: '"+other_number+"'")
        for self_digit, self_index in self.reverse():

            other_digit = int(other_number[self_index])

            if self.debug: print(str(self_index)+": self_digit is: '"+str(self_digit)+"' and other_digit is: '"+str(other_digit)+"'")
            
            if self.debug: print("Remainder is "+str(remainder))    
            if remainder > 0:
                if self.debug: print("Adding remainder of "+str(remainder))
                current_sum = remainder + self_digit + other_digit
            else:
                current_sum = self_digit + other_digit

            if self.debug: print("Current_sum is "+str(current_sum))
            # check for remainder
            if current_sum >= 10:
                remainder = current_sum//10
                current_sum = current_sum%10
                if self.debug: print("There was a remainder of "+str(remainder)+" and the digit will now be: "+str(current_sum))
            else:
                remainder = 0
            newnum.number = str(current_sum) + newnum.number
            if self.debug: print("newnum.number is currently: "+str(newnum.number))
        if remainder > 0:
            newnum.number = str(remainder) + newnum.number

        # strip leading zeroes
        while self.number[0]=="0":
            if self.number!="0":
                self.number=self.number[1:]
            else:
                break
        while other.number[0]=="0":
            if other.number!="0":
                other.number=other.number[1:]
            else:
                break
        
        return newnum
    def output(self):
        print(self.number)
    def value(self):
        return self.number
    def reverse(self):
        for index in range(len(self.number)-1, -1, -1):
            yield int(self.number[index]), int(index)


