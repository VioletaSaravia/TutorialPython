class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        self.SymbolValue = {
            'I'      :      1,
            'V'      :      5,
            'X'      :      10,
            'L'      :      50,
            'C'      :      100,
            'D'      :      500,
            'M'      :      1000
        }
        
        
        dec = int(num / 10) if num > 9 else 0
        un = int(num % 10)
        cent = int(num / 100) if num > 99 else 0
        mil = int(num / 1000) if num > 999 else 0
        
        resultado = []

# https://stackoverflow.com/questions/30280856/populating-a-dictionary-using-for-loops-python
