class Solution:
    def intToRoman(self, num: int) -> str:
        num=list(str(num)[::-1])
        ans=list()
        for i in range(len(num)):
            if(i==0):
                if(int(num[i])<=3):
                    roman_digit=int(num[i])*'I'
                elif(int(num[i])==4):
                    roman_digit='IV'
                elif(int(num[i])==5):
                    roman_digit='V'
                elif(int(num[i])>5 and int(num[i])<9):
                    roman_digit='V'+(int(num[i])-5)*'I'
                elif(int(num[i])==9):
                    roman_digit='IX'
                else:
                    roman_digit='X'
            elif(i==1):
                if(int(num[i])<=3):
                    roman_digit=int(num[i])*'X'
                elif(int(num[i])==4):
                    roman_digit='XL'
                elif(int(num[i])==5):
                    roman_digit='L'
                elif(int(num[i])>5 and int(num[i])<9):
                    roman_digit='L'+(int(num[i])-5)*'X'
                elif(int(num[i])==9):
                    roman_digit='XC'
                else:
                    roman_digit='C'
            elif(i==2):
                if(int(num[i])<=3):
                    roman_digit=int(num[i])*'C'
                elif(int(num[i])==4):
                    roman_digit='CD'
                elif(int(num[i])==5):
                    roman_digit='D'
                elif(int(num[i])>5 and int(num[i])<9):
                    roman_digit='D'+(int(num[i])-5)*'C'
                elif(int(num[i])==9):
                    roman_digit='CM'
                else:
                    roman_digit='M'
            elif(i==3):
                if(int(num[i])<=3):
                    roman_digit=int(num[i])*'M'
            else:
                pass
            ans.insert(0,roman_digit)
        ans=''.join(ans)
        return(ans)
