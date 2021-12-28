from subprocess import Popen, PIPE

######################################################################################################################
# TODO:                                                                                                              #
# 1) PUT THIS FILE IN THE SAME FOLDER AS THE PYTHON FILE CONTAINING YOUR SOLUTION                                    #
# 2) CHANGE THE NAME 'MY_FILE_NAME.py' BELOW THIS BOX TO THE NAME OF YOUR PYTHON FILE                                #
# 3) RUN THIS FILE                                                                                                   #
######################################################################################################################

YOUR_SOLUTION_FILE_NAME = "Practicum1.1.py"

######################################################################################################################
# DO NOT CHANGE ANYTHING BELOW THIS LINE                                                                             #
######################################################################################################################


# Parse the given output string into a list of floats
def parse_output(full_output_string):
    try:
        output = [float(value) for value in
                  str(full_output_string).replace('\\n', '').replace(',', '').replace('\\r', '')
                  .replace('(', '').replace(')', '').replace('"', '').replace('\'', '')[1:].split(' ')
                  if len(value) > 0]
    except:
        output = None
    return output


# Run one test case with given input and output, return True when test succeeds, False when test fails
def run_one_test_case(inp, expected_output):
    process = Popen(["python", YOUR_SOLUTION_FILE_NAME], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    (output, err) = process.communicate(inp)
    if len(str(err)) > 3:
        print("Je programma gooide een error. "
              "(Kijk eventueel ook na of de naam en locatie van je programma correct zijn.)")
        return False
    process.wait()
    parsed_output = parse_output(output)
    if parsed_output is None:
        print("Controleer het formaat van je output! Geef enkel de gevraagde numerieke waarden, en géén tekst!"
              " Kijk ook na dat je bij input() geen prompt meegeeft.")
        return False
    return parsed_output == expected_output


# Retrieve a list containing all test_cases
def get_test_cases():
    test_cases = []
    # In: 100 -20 0 Uit: 80.0 0 0 0
    test_cases.append((b'100\n-20\n0\n', [80, 0, 0, 0]))
    # In: 80 50 -200 0 Uit: -84.0 -14.0 0 -14.0
    test_cases.append((b'80\n50\n-200\n0\n', [-84, -14, 0, -14]))
    # In: 100 150 -200 -100 -200 0 Uit: -245.0 5.0 5.0 0
    test_cases.append((b'100\n150\n-200\n-100\n-200\n0\n', [-245, 5, 5, 0]))
    # In: 100 -150 20 100 200 -150 20 0 Uit: 145.4 5.4 11.4 -6.0
    test_cases.append((b'100\n-150\n20\n100\n200\n-150\n20\n0\n', [145.4, 5.4, 11.4, -6]))
    # In: 20 -150 100 100 100 -250 20 20 100 -200 0 Uit: -159.52 -19.52 3.68 -23.2
    test_cases.append((b'20\n-150\n100\n100\n100\n-250\n20\n20\n100\n-200\n0\n', [-159.52, -19.52, 3.68, -23.2]))
    # In: 100 50 -150 200 250 -450 -1000 400 600 20 0 Uit: 20.0 0 0 0
    test_cases.append((b'100\n50\n-150\n200\n250\n-450\n-1000\n400\n600\n20\n0\n', [20, 0, 0, 0]))
    # In: 1 2 3 4 5 -6 -7 -8 -9 0 Uit: -16.13 -1.13 -1.56 -2.69
    test_cases.append((b'1\n2\n3\n4\n5\n-6\n-7\n-8\n-9\n0\n', [-16.13, -1.13, 1.56, -2.69]))
    return test_cases


# Run all given test_cases
def run_test_cases(all_tests):
    for test_nb in range(len(all_tests)):
        (inp, exp_out) = all_tests[test_nb]
        test_result = run_one_test_case(inp, exp_out)
        if test_result:
            print('Test ' + str(test_nb + 1) + ': Succeeded')
        else:
            print('Test ' + str(test_nb + 1) + ': Failed')


# Load all test cases and test them
run_test_cases(get_test_cases())
