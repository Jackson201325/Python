filename = 'responses.txt'

with open(filename, 'w') as fo:
    responses = []
    while True:
        answer = input("Why do you like programming? ")
        if answer == 'q':
            for response in responses:
                fo.write(response)
                fo.write("\n")
            break
        else:
            responses.append(answer)
