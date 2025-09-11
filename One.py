

class fine:
    def __init__(self):
        """
        ## Classifying Real Numbers - Lesson : 1

        - [ℕ](https://www.tutorialgateway.org/python-program-to-print-natural-numbers/)
        - [ℤ₀]()
        - [ℤ]()
        - [ℚ]()
        - [Q']()
        - [ℝ]()
        """

        self.NTN = self.NeturalNumbers()
        """**Netural Number ℕ**"""
        
        self.WN = self.WholeNumbers()
        """**Whole Number ℤ₀**"""

    def NeturalNumbers(self,n=10,type=0):
        """ ## Natural Numbers - ℕ 
            > **The numbers used to count objects or things.**
            > **Numbers - ℕ**

            - stop last number : n = 1...1000000
            
            - All Types : type = 0

            _________________________________________________________________________________
            ### All Types
            - 0 : list
            - 1 : obj
            - 2 : str
        """
        arr = []
        obj = {}
        stri = ""
        try:
            for NTN in range(1,n+1):
                if type == 0:
                    arr.append(NTN)
                elif type == 1:
                    obj[NTN] = NTN
                elif type == 2:
                    stri += str(NTN) + ","

        except Exception as e:
            print(f"Error : {e}")
        else:
            if type == 0:
                return arr
            elif type == 1:
                return obj
            elif type == 2:
                return stri.rstrip(", ")
            
    def WholeNumbers(self,n=10,type=0):
        """
         ## Whole Numbers - ℤ₀

        """
        try:
            a = self.NeturalNumbers(n,type)
        except Exception  as e:
            print(f"Whole Numbers Error : {e}")
        else:
            if type == 0:
                a.insert(0,0)
                return a
            elif type == 1:
                # main logics in object dictory
                a[0] = 0
                main_obj = {}
                for i in sorted(a.keys()):
                    main_obj[i] = i
                return main_obj

            elif type == 2:
                b = a.split(',')
                b.insert(0,"0")
                a = ','.join(b)
                return a

    def IntegerNumbers():
        """
        ## Integer - ℤ
        """
        pass

            
    

M = fine()
print(f"Nutural Number : {M.NTN}")
print(f"Whole Number : {M.WN}")
print(M.WholeNumbers(10,0)) # list
print(M.WholeNumbers(10,1)) # dict
print(M.WholeNumbers(10,2)) # str
