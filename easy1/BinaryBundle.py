class BinaryBundle:

    # Function to convert decimal number
    # to binary using recursion
    def DecimalToBinary(self, num):
        if num >= 1:
            self.DecimalToBinary(num // 2)
        print(num % 2, end = '')