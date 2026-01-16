# Defaults CANNOT Be Changed
defaults = ["a", "b"]


def mathOperations(operation: str, vars: dict, flags: dict, tempResult: str, tempVar1: str, tempVar2: str) -> tuple[dict, str, str]:

    """ Carries Out The Mathematical Operations """

    var1 = tempVar1
    var2 = tempVar2

    # Check If var1 In vars
    if var1 in vars.keys():
        # Try Changing To int
        try:
            var1 = vars[var1]
        except ValueError:
            flags["not_integer"] = 1
            flags["no_errors"] = False
            return flags, None, None

    # Check If var2 In vars
    if var2 in vars.keys():
        # Try Changing To int
        try:
            var2 = vars[var2]
        except ValueError:
            flags["not_integer"] = 1
            flags["no_errors"] = False
            return flags, None, None


    result: int = 0
    try:
        match operation:
            case "add":
                result = int(var1) + int(var2)
            case "sub":
                result = int(var1) - int(var2)
            case "mul":
                result = int(var1) * int(var2)
            case "div":
                # Division By Zero
                if int(var2) == 0:
                    flags["zero_division"] = 1
                    flags["no_errors"] = False
                    return flags, None, None
                else:
                    # Enforce Integer Division
                    result = int(var1) // int(var2)
    except ValueError:
        flags["not_integer"] = 1
        flags["no_errors"] = False
        return flags, None, None

    return flags, tempResult, str(result)


def setVariable(vars: dict, tempArg1: str, tempArg2: str) -> dict:

    """ Sets A New Variable """

    # Is This Variable Already Existing
    if tempArg1 in vars.keys():
        # Is "Value" A Variable Too
        if tempArg2 in vars.keys():
            vars[tempArg1] = vars[tempArg2]
            return vars
        else:
            vars[tempArg1] = tempArg2
            return vars

    # Imagine It Is A New Variable
    # Is "Value" A Variable
    if tempArg2 in vars.keys():
        tempArg2 = vars[tempArg2]

    # Create A New Variable
    vars[tempArg1] = tempArg2
    return vars


def printr(vars: dict, tempArg1: str) -> str:

    """ Print A Value To c Value """

    # If Value Is A Variable
    if tempArg1 in vars.keys():
        return vars[tempArg1]
    else:
        return tempArg1


def updateList(vars: dict, flags: dict, theList: list, index: int, value: int) -> tuple[dict, list]:

    """ Updates A List To c Value """

    try:
        tempMax: int = int(vars["a"])
        tempMin: int = int(vars["b"])
        # Is index In List's Bounds
        if tempMax > index >= tempMin:
            # Is value 0 Or 1
            if value == 0 or value == 1:
                theList[index] = value
                return flags, theList
            else:
                flags["bad_value_printr"] = 1
                flags["no_errors"] = False
                return flags, theList
        else:
            flags["out_of_bounds"] = 1
            flags["no_errors"] = False
            return flags, theList
    except ValueError:
        flags["not_integer"] = 1
        flags["no_errors"] = False
        return flags, theList


def checkForVariable(var1: str, variables: list) -> bool:

    """ Check For Certain Variables """

    if var1 in variables:
        return True
    else:
        return False


def manageNucleotideCheck(vars: dict, dataList: list, flags: dict, var1: str, var2: str) -> tuple[dict, int]:

    """ Manages Nucleotide Check """

    # Is User Checking For Nucleotide At Index c
    if var1 == '-':
        try:
            index = int(vars["c"])
            if index < 0 or index >= len(dataList):
                flags["out_of_bounds"] = 1
                flags["no_errors"] = False
                return flags, 2
            # Is It Equal To Nucleotide At Index c
            if str(dataList[index]) == str(var2):
                return flags, 1
            else:
                return flags, 0
        except ValueError:
            flags["not_integer"] = 1
            flags["no_errors"] = False
    return flags, -1


def executeLine(lineContent: str, vars: dict, flags: dict, execCounter: int, tempIndex: int, tempValue: str, IF_FLAG: int, dataList: list, updatedList: list) -> tuple[dict, dict, int, int, int, str, list]:

    """ Executes A Line Of Code """

    # Error Checking
    if not lineContent:
        return vars, flags, execCounter, tempIndex, tempValue, IF_FLAG, updatedList
    # Remove Newline Character
    lineContent = lineContent.strip("\n")
    # Get Command
    tempCommand = lineContent.split(" ")

    # Check If Anything In tempCommand Has A Length 0 Meaning We Got No Arguments Still
    if "" in tempCommand:
        flags["argument_error"] = 1
        flags["no_errors"] = False
        return vars, flags, execCounter, tempIndex, tempValue, IF_FLAG, updatedList

    # Printr To result list
    if tempCommand[0] == "printr" and IF_FLAG == 1:
        tempArg1: str = tempCommand[1]
        if not tempArg1:
            return vars, flags, execCounter, tempIndex, tempValue, IF_FLAG, updatedList
        else:
            tempStr: str = printr(vars, tempArg1)
            index: str = vars["c"]
            try:
                temp1 = int(tempStr)
                temp2 = int(index)
                # Update The List
                flags, updatedList = updateList(vars, flags, updatedList, temp2, temp1)
            except ValueError:
                flags["not_integer"] = 1
                flags["no_errors"] = False
                return vars, flags, execCounter, tempIndex, tempValue, IF_FLAG, updatedList

    # Initializing Or Setting Variables
    elif tempCommand[0] == "set" and IF_FLAG == 1:
        tempArg1: str = tempCommand[1]
        tempArg2: str = tempCommand[2]
        # Is User Setting Defaults
        if checkForVariable(tempArg1, defaults):
            flags["variable_access"] = 1
            flags["no_errors"] = False
            return vars, flags, execCounter, tempIndex, tempValue, IF_FLAG, updatedList
        else:
            if not tempArg1 or not tempArg2:
                return vars, flags, execCounter, tempIndex, tempValue, IF_FLAG, updatedList
            else:
                vars = setVariable(vars, tempArg1, tempArg2)

    # Comments
    elif tempCommand[0][:2] == "//" and IF_FLAG == 1:
        # Check The First Two Characters Of The Comment
        return vars, flags, execCounter, tempIndex, tempValue, IF_FLAG, updatedList

    elif tempCommand[0] == "add" and IF_FLAG == 1:
        tempResultVar = tempCommand[1]
        tempArg1: str = tempCommand[2]
        tempArg2: str = tempCommand[3]
        # Is User Changing Defaults
        if checkForVariable(tempResultVar, defaults):
            flags["variable_access"] = 1
            flags["no_errors"] = False
            return vars, flags, execCounter, tempIndex, tempValue, IF_FLAG, updatedList
        else:
            if not tempArg1 or not tempArg2 or not tempResultVar:
                return vars, flags, execCounter, tempIndex, tempValue, IF_FLAG, updatedList
            else:
                flags, tempResult, value = mathOperations(tempCommand[0], vars, flags, tempResultVar, tempArg1, tempArg2)
                if tempResult is None or value is None:
                     return vars, flags, execCounter, tempIndex, tempValue, IF_FLAG, updatedList
                if tempResult in vars.keys():
                    vars[tempResult] = str(value)
                else:
                    # If Not A Variable
                    # Create One With The result
                    vars[tempResult] = str(value)

    elif tempCommand[0] == "sub" and IF_FLAG == 1:
        tempResultVar = tempCommand[1]
        tempArg1: str = tempCommand[2]
        tempArg2: str = tempCommand[3]
        # Is User Changing Defaults
        if checkForVariable(tempResultVar, defaults):
            flags["variable_access"] = 1
            flags["no_errors"] = False
            return vars, flags, execCounter, tempIndex, tempValue, IF_FLAG, updatedList
        else:
            if not tempArg1 or not tempArg2 or not tempResultVar:
                return vars, flags, execCounter, tempIndex, tempValue, IF_FLAG, updatedList
            else:
                flags, tempResult, value = mathOperations(tempCommand[0], vars, flags, tempResultVar, tempArg1, tempArg2)
                if tempResult is None or value is None:
                     return vars, flags, execCounter, tempIndex, tempValue, IF_FLAG, updatedList
                if tempResult in vars.keys():
                    vars[tempResult] = str(value)
                else:
                    # If Not A Variable
                    # Create One With The result
                    vars[tempResult] = str(value)

    elif tempCommand[0] == "mul" and IF_FLAG == 1:
        tempResultVar = tempCommand[1]
        tempArg1: str = tempCommand[2]
        tempArg2: str = tempCommand[3]
        # Is User Changing Defaults
        if checkForVariable(tempResultVar, defaults):
            flags["variable_access"] = 1
            flags["no_errors"] = False
            return vars, flags, execCounter, tempIndex, tempValue, IF_FLAG, updatedList
        else:
            if not tempArg1 or not tempArg2 or not tempResultVar:
                return vars, flags, execCounter, tempIndex, tempValue, IF_FLAG, updatedList
            else:
                flags, tempResult, value = mathOperations(tempCommand[0], vars, flags, tempResultVar, tempArg1, tempArg2)
                if tempResult is None or value is None:
                     return vars, flags, execCounter, tempIndex, tempValue, IF_FLAG, updatedList
                if tempResult in vars.keys():
                    vars[tempResult] = str(value)
                else:
                    # If Not A Variable
                    # Create One WIth The result
                    vars[tempResult] = str(value)

    elif tempCommand[0] == "div" and IF_FLAG == 1:
        tempResultVar = tempCommand[1]
        tempArg1: str = tempCommand[2]
        tempArg2: str = tempCommand[3]
        # Is User Changing Defaults
        if checkForVariable(tempResultVar, defaults):
            flags["variable_access"] = 1
            flags["no_errors"] = False
            return vars, flags, execCounter, tempIndex, tempValue, IF_FLAG, updatedList
        else:
            if not tempArg1 or not tempArg2 or not tempResultVar:
                return vars, flags, execCounter, tempIndex, tempValue, IF_FLAG, updatedList
            else:
                flags, tempResult, value = mathOperations(tempCommand[0], vars, flags, tempResultVar, tempArg1, tempArg2)
                if tempResult is None or value is None:
                    return vars, flags, execCounter, tempIndex, tempValue, IF_FLAG, updatedList
                if tempResult in vars.keys():
                    vars[tempResult] = str(value)
                else:
                    # If Not A Variable
                    # Create One With The result
                    vars[tempResult] = str(value)

    elif tempCommand[0] == "when" and IF_FLAG == 1:
        tempCondition = tempCommand[1]
        if not tempCondition:
            return vars, flags, execCounter, tempIndex, tempValue, IF_FLAG, updatedList
        else:
            tempValue = tempCondition
            tempIndex = execCounter

    elif tempCommand[0] == "end" and IF_FLAG == 1:
        # Handles Nested Loops Hence No Errors
        if not tempValue:
            return vars, flags, execCounter, tempIndex, tempValue, IF_FLAG, updatedList
        else:
            # Is tempValue A Variable
            if tempValue in vars.keys():
                if int(vars[tempValue]) != 0:
                    execCounter = tempIndex - 1
                return vars, flags, execCounter, tempIndex, tempValue, IF_FLAG, updatedList
            # Is tempValue Just A Number
            if int(tempValue) != 0:
                execCounter = tempIndex - 1
            else:
                tempIndex = 0
                tempValue = ""

    elif tempCommand[0] == "if" and IF_FLAG == 1:
        tempConditionVar1 = tempCommand[1]
        tempConditionVar2 = tempCommand[2]
        if not tempConditionVar1 or not tempConditionVar2:
            return vars, flags, execCounter, tempIndex, tempValue, IF_FLAG, updatedList
        else:
            if tempConditionVar1 in vars.keys():
                tempConditionVar1 = vars[tempConditionVar1]
            if tempConditionVar2 in vars.keys():
                tempConditionVar2 = vars[tempConditionVar2]

            flags, nuc_check_result = manageNucleotideCheck(vars, dataList, flags, tempConditionVar1, tempConditionVar2)
            # Is User Checking Nucleotide Base
            if nuc_check_result == 2:
                IF_FLAG = 0
                return vars, flags, execCounter, tempIndex, tempValue, IF_FLAG, updatedList
            elif nuc_check_result == 1:
                IF_FLAG = 1
                return vars, flags, execCounter, tempIndex, tempValue, IF_FLAG, updatedList
            elif nuc_check_result == 0:
                IF_FLAG = 0
                return vars, flags, execCounter, tempIndex, tempValue, IF_FLAG, updatedList
            elif nuc_check_result == -1:
                # Do They Match Whether Variables Or Values
                if int(tempConditionVar1) == int(tempConditionVar2):
                    IF_FLAG = 1
                else:
                    IF_FLAG = 0

    elif tempCommand[0] == "done":
        # Release Execution When Locked
        if IF_FLAG == 0:
            IF_FLAG = 1

    else:
        # If Code Could Be Run Then Failed
        if IF_FLAG == 1:
            flags["bad_command"] = 1
            flags["no_errors"] = False
            return vars, flags, execCounter, tempIndex, tempValue, IF_FLAG, updatedList

    return vars, flags, execCounter, tempIndex, tempValue, IF_FLAG, updatedList