class actionNumber():

    def __init__(self,value1):
        """
        For initialization
        """
        self.value1 = value1
        self.random_num = 20 #:random number assigned

    def addme(self,num1):
        """
        This will add
        """
        self.value1 = self.value1+num1
        return self.value1

    def multme1(self,num1):
        """
        This will multiply
        """
        self.value1 = self.value1*num1
        return self.value1

    def divme(self,num1):
        self.value1 = self.value1/num1
        return self.value1

    def subme1(self,num1):
        """
        This will subtract
        """

        test1 = """
        Will you come in?
        """
        self.value1 = self.value1-num1
        return self.value1



obj1 = actionNumber(100)
expected_IP = '35.123.23.21'#:this should be the expected
print obj1.divme(20)