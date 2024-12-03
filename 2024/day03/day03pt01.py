# in_put = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
with open('input03.txt') as f:
    in_put = f.read()

def check_sequence(text):
    numbers = []
    index = 0
    while index < len(text):
        if text[index:index + 4] == 'mul(':
            index += 4
            check = check_number(text[index:])
            if check[0] is not None:
                num1 = int(check[0])
                index += len(check[0])
                if text[index] == ',':
                    index += 1
                    check2 = check_number(text[index:])
                    if check2[0] is not None:
                        num2 = int(check2[0])
                        index += len(check2[0])
                        if index < len(text) and text[index] == ')':
                            index += 1
                            numbers.append(num1 * num2)
                        else:
                            continue
                    else:
                        continue
                else:
                    continue
            else:
                continue
        else:
            index += 1  # Move to the next character
    
    return numbers

def check_number(num):
    # Find the first non-digit character in the string
    for i in range(len(num)):
        if num[i].isdigit():
            continue
        else:
            if i == 0:  # No digits at all
                return (None, 0)
            return (num[:i], i)
    # If we reach here, we have completely scanned the string
    return (num, len(num))  # Return the whole string if it's all digits

# Execute the code and print the result
result = check_sequence(in_put)
print(sum(result))
