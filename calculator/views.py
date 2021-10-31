from django.shortcuts import render
from .calculations import operation
from .intorfloatvalue import checkIntOrFloat

flag = [1]  # flag[0] = 1 means Number1 and flag[0] = 2 means Number2
firstNumber = ""
secondNumber = ""
sign = ""
result = ""
equalSign = [0]


# equalSign[0] = 0 means '=' sign has not pressed yet.
# equalSign[0] = 1 means'=' sign has pressed.

def calculatorfunc(request):
    global firstNumber
    global secondNumber
    global sign
    global result
    if request.method == "POST":

        if '0' in request.POST:
            if equalSign[0] == 1:
                result = ""
                firstNumber = ""
                secondNumber = ""
                sign = ""
                equalSign[0] = 0
            if flag[0] == 1:
                firstNumber = firstNumber + "0"
            elif flag[0] == 2:
                secondNumber = secondNumber + "0"

        elif '1' in request.POST:
            if equalSign[0] == 1:
                result = ""
                firstNumber = ""
                secondNumber = ""
                sign = ""
                equalSign[0] = 0
            if flag[0] == 1:
                firstNumber = firstNumber + "1"
            elif flag[0] == 2:
                secondNumber = secondNumber + "1"

        elif '2' in request.POST:
            if equalSign[0] == 1:
                result = ""
                firstNumber = ""
                secondNumber = ""
                sign = ""
                equalSign[0] = 0
            if flag[0] == 1:
                firstNumber = firstNumber + "2"
            elif flag[0] == 2:
                secondNumber = secondNumber + "2"

        elif '3' in request.POST:
            if equalSign[0] == 1:
                result = ""
                firstNumber = ""
                secondNumber = ""
                sign = ""
                equalSign[0] = 0
            if flag[0] == 1:
                firstNumber = firstNumber + "3"
            elif flag[0] == 2:
                secondNumber = secondNumber + "3"

        elif '4' in request.POST:
            if equalSign[0] == 1:
                result = ""
                firstNumber = ""
                secondNumber = ""
                sign = ""
                equalSign[0] = 0
            if flag[0] == 1:
                firstNumber = firstNumber + "4"
            elif flag[0] == 2:
                secondNumber = secondNumber + "4"

        elif '5' in request.POST:
            if equalSign[0] == 1:
                result = ""
                firstNumber = ""
                secondNumber = ""
                sign = ""
                equalSign[0] = 0
            if flag[0] == 1:
                firstNumber = firstNumber + "5"
            elif flag[0] == 2:
                secondNumber = secondNumber + "5"

        elif '6' in request.POST:
            if equalSign[0] == 1:
                result = ""
                firstNumber = ""
                secondNumber = ""
                sign = ""
                equalSign[0] = 0
            if flag[0] == 1:
                firstNumber = firstNumber + "6"
            elif flag[0] == 2:
                secondNumber = secondNumber + "6"

        elif '7' in request.POST:
            if equalSign[0] == 1:
                result = ""
                firstNumber = ""
                secondNumber = ""
                sign = ""
                equalSign[0] = 0
            if flag[0] == 1:
                firstNumber = firstNumber + "7"
            elif flag[0] == 2:
                secondNumber = secondNumber + "7"

        elif '8' in request.POST:
            if equalSign[0] == 1:
                result = ""
                firstNumber = ""
                secondNumber = ""
                sign = ""
                equalSign[0] = 0
            if flag[0] == 1:
                firstNumber = firstNumber + "8"
            elif flag[0] == 2:
                secondNumber = secondNumber + "8"

        elif '9' in request.POST:
            if equalSign[0] == 1:
                result = ""
                firstNumber = ""
                secondNumber = ""
                sign = ""
                equalSign[0] = 0
            if flag[0] == 1:
                firstNumber = firstNumber + "9"
            elif flag[0] == 2:
                secondNumber = secondNumber + "9"

        elif '.' in request.POST:
            if equalSign[0] == 1:
                firstNumber = result
                result = ""
                secondNumber = ""
                sign = ""
                equalSign[0] = 0
            if flag[0] == 1:
                firstNumber = firstNumber + "."
            elif flag[0] == 2:
                secondNumber = secondNumber + "."

        elif 'INT' in request.POST:
            if result != "":
                firstNumber = str(int(float(result)))
                result = ""
                secondNumber = ""
                equalSign[0] = 0

            if flag[0] == 1:
                firstNumber = str(int(float(firstNumber)))
            elif flag[0] == 2:
                secondNumber = str(int(float(secondNumber)))

        elif '+' in request.POST:
            if result != "":
                firstNumber = result
                result = ""
                secondNumber = ""
                equalSign[0] = 0
            sign = "+"
            flag[0] = 2

        elif '-' in request.POST:
            if result != "":
                firstNumber = result
                result = ""
                secondNumber = ""
                equalSign[0] = 0
            sign = "-"
            flag[0] = 2

        elif '×' in request.POST:
            if result != "":
                firstNumber = result
                result = ""
                secondNumber = ""
                equalSign[0] = 0
            sign = "×"
            flag[0] = 2

        elif '÷' in request.POST:
            if result != "":
                firstNumber = result
                result = ""
                secondNumber = ""
                equalSign[0] = 0
            sign = "÷"
            flag[0] = 2

        elif '%' in request.POST:
            if result != "":
                firstNumber = result
                result = ""
                secondNumber = ""
                equalSign[0] = 0
            sign = "%"
            flag[0] = 2

        elif 'AC' in request.POST:
            flag[0] = 1
            firstNumber = ""
            secondNumber = ""
            sign = ""
            result = ""
            equalSign[0] = 0

        elif 'C' in request.POST:
            if flag[0] == 1:
                firstNumber = firstNumber[0:len(firstNumber)-1]
            else:
                if secondNumber == "":
                    sign = ""
                    flag[0] = 1
                else:
                    secondNumber = secondNumber[0:len(secondNumber) - 1]

        elif '=' in request.POST:
            result = str(operation(float(firstNumber), float(secondNumber), sign))
            if checkIntOrFloat(result) == 1:
                result = str(int(float(result)))
            flag[0] = 1
            equalSign[0] = 1
    context = {
        "firstNumber": firstNumber,
        "sign": sign,
        "secondNumber": secondNumber,
        "result": result
    }
    return render(request, 'calculator/calculator.html', context)
