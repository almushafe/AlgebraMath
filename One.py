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
        self.NeturalNumber = self.NeturalNumbers()

    def NeturalNumbers(self,n=100,type=0):
        """ ## Natural Numbers - ℕ 
            > **The numbers used to count objects or things. **
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
            for NTN in range(1,n):
                arr.append(NTN)
                obj[NTN] = NTN
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
            
    def WholeNumbers():
        """
         ## Whole Numbers - ℤ₀

        """

    def IntegerNumbers():
        """
        ## Integer - ℤ
        """

            
    

M = fine()
M.NeturalNumbers()

print()
