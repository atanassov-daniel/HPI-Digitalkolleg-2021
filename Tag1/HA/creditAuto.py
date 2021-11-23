def func(passwords):
    valid = 0
    invalid=0

    for password in passwords:
        pass_str = str(password)
        sum = 0
        last_digit = len(pass_str) - 1

        i = last_digit
        while i >= 0:
            digit = int(pass_str[i])

            if i % 2 == last_digit % 2:  # letzte ziffer und jede zweite von der letzten
                sum += digit
            else:  # jede zweite ziffer von der vorletzten
                product = digit * 2
                if product // 10 == 0:
                    sum += product
                else:
                    sum += product % 10
                    sum += product // 10
            i -= 1

        if sum % 10 == 0:
            valid+=1
        else:
            invalid+=1
    
    print(f"valid amount: {valid}")
    print(f"invalid amount: {invalid}")
    
valids15 = [
    4003600000000014, 374245455400126, 378282246310005, 6250941006528599,
    60115564485789458, 6011000991300009, 3566000020000410,3530111333300000,
    5425233430109903, 5425233430109903, 2223000048410010, 4263982640269299, 
    6062826786276634, 6271701225979642, 6034883265619896,
]
invalids3 = [5, 4843905893480, 7298342937489273489]

func(valids15)
func(invalids3)