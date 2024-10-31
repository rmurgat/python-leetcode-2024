from typing import List


class BinaryBundle:

    def InvertBinaryDecimal(self, num) -> List:
        bin = []

        def DecimalToBinary(decimal):
            if decimal >= 1:
                DecimalToBinary(decimal // 2)
            bin.append(decimal % 2)

        def Binary2Decimal(bin: List[int]) -> int:
            decimal = 0
            for i in range(0,len(bin)):
                decimal = decimal + bin[i] * pow(2,i)
            return decimal
        
        DecimalToBinary(num)
        
        print("decimal to binary:", bin[::-1])
        print("binary to decimal:", Binary2Decimal(bin[::-1]))
        print("binary to decimal:", Binary2Decimal(bin))
        return bin