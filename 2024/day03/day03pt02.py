# Load input from a file
with open('input03.txt') as f:
    in_put = f.read()

def check_sequence(text):
    numbers = []
    do_execute = True  # Start with mul enabled
    index = 0
    while index < len(text):
        if do_execute:
            # Check if we have a 'don't()' instruction
            find_dont = check_dont(text[index:])
            if find_dont[0]:
                index += find_dont[1]  # Skip past 'don't()'
                do_execute = False
                continue

            # Check if we have a valid mul(...) instruction
            if text[index:index + 4] == 'mul(':
                index += 4
                check = check_number(text[index:])
                if check[0] is not None:
                    num1 = int(check[0])
                    index += len(check[0])
                    if index < len(text) and text[index] == ',':
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
        else:
            # Check for do() instructions to re-enable execution
            find_do = check_do(text[index:])
            if find_do[0]:
                index += find_do[1]  # Skip past 'do()'
                do_execute = True
                continue
            index += 1  # Move to the next character
    return numbers

def check_number(num):
    for i in range(len(num)):
        if num[i].isdigit():
            continue
        else:
            if i == 0:  # No digits at all
                return (None, 0)
            return (num[:i], i)
    return (num, len(num))

def check_dont(text):
    if text[:6] == "don't(":
        return (True, 6)
    return (False, 0)

def check_do(text):
    if text[:3] == "do(":
        return (True, 3)
    return (False, 0)

# Execute the code and print the result
result = check_sequence(in_put)
print(sum(result))

