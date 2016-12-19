# function is a function which takes the first element of each entry in tests and verifies that it produces the second element of that entry
# tests is a list of pairs [(input, expected_output)]
def test(function,tests):
    if (tests == []):
        return True
    case = tests[0]
    input = case[0]
    expected = case[1]
    actual = function (input)
    success = actual == expected

    if success:
        return test(function,tests[1:])
    else:
        print("Function `" + function.__name__ + "` failed on input: " + str(input) +  ". Expected: `" + str(expected) + "`; Actual: `" + str(actual) + "`.")
        return False
