class Solution:
    def romanToInt(self, s: str) -> int:
        
        result = 0
        i = len(s) - 1
        j = i - 1
        #print("How is this possible?", s[0])
        
        while i >= 0:
            current_number = 0
            
            match s[i]:
                case 'I':
                    #print("its here")
                    current_number = 1
                case 'V':
                    current_number = 5
                case 'X':
                    current_number = 10
                case 'L':
                    current_number = 50
                case 'C':
                    current_number = 100
                case 'D':
                    current_number = 500
                case 'M':
                    current_number = 1000
                case _:
                    current_number = 0
            
            if j >= 0:
                match s[j]:
                    case 'I':
                        if current_number == 5 or current_number == 10:
                            current_number = current_number - 1
                        else:
                            current_number = current_number + 1
                    case 'V':
                        current_number = current_number + 5
                    case 'X':
                        if current_number == 50 or current_number == 100:
                            current_number = current_number - 10
                        else:
                            current_number = current_number + 10
                    case 'L':
                        current_number = current_number + 50
                    case 'C':
                        if current_number == 500 or current_number == 1000:
                            current_number = current_number - 100
                        else:
                            current_number = current_number + 100
                    case 'D':
                        current_number = current_number + 500
                    case 'M':
                        current_number = current_number + 1000
                    case _:
                        current_number = 0
            
            result = result + current_number
            print(current_number)
            i -= 2
            j = i - 1
        return result
