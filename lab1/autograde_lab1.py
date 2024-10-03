#!/usr/bin env python3
# -*- coding: utf-8 -*-

### Universitetet i Bergen INF100 høst 2022
### AUTOGRADER for lab 1

# Du kan kjøre dette programmet for å sjekke om du har gjort lab 1 riktig.

# For å bruke autograderen:
# 1. Legg denne filen i samme mappe som uke_01_oppg_1.py, uke_01_oppg_2.py osv.
# 2. Kjør denne filen med python3 (f. eks. åpne den i VSCode og klikk Run)
# 3. Du vil få en liste over feilmeldinger hvis du har gjort noen feil.

# Du kan konfigurerer hvilke test du vil kjøre her.

def run():
    """ Run the autograder for these tasks. 
        You may comment out any tests you do not wish to run. """
    task1()
    task2()
    task3()
    task4()
    task5a()
    task5b()
    task5c()
    task6()


### Å ENDRE PÅ KODEN UNDER DENNE LINJEN SKJER PÅ EGET ANSVAR ###
### CHANGING THE CODE BELOW THIS LINE IS AT YOUR OWN RISK ###

###############################################################################
### Test definitions ##########################################################
###############################################################################

def task1():
    run_input_output_tests("uke_01_oppg_1.py", [
        # Tester skrevet i formatet [ input_string, expected_output ]
        # Test 1
        ["",
        "Hei, det er meg, datamaskinen.\n" +
            "Hyggelig å se deg her.\n" +
            "Lykke til med INF100!\n"
        ],
        # Test 2
        ["bare\ntull",
        "Hei, det er meg, datamaskinen.\n" +
            "Hyggelig å se deg her.\n" +
            "Lykke til med INF100!\n"
        ],
    ])
    
def task2():
    run_input_output_tests("uke_01_oppg_2.py", [
        # Tester skrevet i formatet [ input_string, expected_output ]
        # Test 1
        # Input
        ["Kari Nordmann\n" +
            "Gateveien 1\n" +
            "1234 Stedet\n",
        # Forventet output
        "Hva er ditt navn?\n" +
            "Hva er din adresse?\n" +
            "Hva er ditt postnummer og poststed?\n" +
            "Kari Nordmanns adresse er:\n" +
            "\n" +
            "Kari Nordmann\n" +
            "Gateveien 1\n" +
            "1234 Stedet\n"
        ],
        # Test 2
        # Input
        ["Ola Nordmann\n" +
            "Veigaten 2\n" +
            "4321 Tedets\n",
        # Forventet output
        "Hva er ditt navn?\n" +
            "Hva er din adresse?\n" +
            "Hva er ditt postnummer og poststed?\n" +
            "Ola Nordmanns adresse er:\n" +
            "\n" +
            "Ola Nordmann\n" +
            "Veigaten 2\n" +
            "4321 Tedets\n"
        ],
    ])
    
def task3():
    run_input_output_tests("uke_01_oppg_3.py", [
        # Tester skrevet i formatet [ input_string, expected_output ]
        # Test 1
        ["Kari Nordmann\n" +
            "Gateveien 1\n" +
            "1234 Stedet\n",
        "Hva er ditt navn?\n" +
            "Hva er din adresse?\n" +
            "Hva er ditt postnummer og poststed?\n" +
            "13\n"
        ],
        # Test 2
        ["Ola Nordmann\n" +
            "Veigaten 2\n" +
            "1234567890123456\n",
        "Hva er ditt navn?\n" +
            "Hva er din adresse?\n" +
            "Hva er ditt postnummer og poststed?\n" +
            "16\n"
        ],
        # Test 3
        ["Ola Nordmann\n" +
            "12345678901234567890\n" +
            "1234 Goddag\n",
        "Hva er ditt navn?\n" +
            "Hva er din adresse?\n" +
            "Hva er ditt postnummer og poststed?\n" +
            "20\n"
        ],
    ])

def task4():
    run_input_output_tests("uke_01_oppg_4.py", [
        # Tester skrevet i formatet [ input_string, expected_output ]
        # Test 1
        ["What a pleasure to\n" +
            "right justify a haiku\n" +
            "as an exercise\n",
        "Første raden:\n" +
            "Andre raden:\n" +
            "Tredje raden:\n" +
            "\n" +
            "@@@@@@@@@@@@@@@@@@@@@@@@@\n" +
            "@    What a pleasure to @\n" +
            "@ right justify a haiku @\n" +
            "@        as an exercise @\n" +
            "@@@@@@@@@@@@@@@@@@@@@@@@@\n"
        ],
    ])

def task5a():
    run_import_based_function_tests(
        "uke_01_oppg_5.py", 
        "volume_of_box",
        [
            # expected_return, expected_stdout, w, h, d
            [30, "", 2, 3, 5],              # Test 1
            [1, "", 1, 1, 1],               # Test 2
            [0.001, "", 0.1, 0.1, 0.1],     # Test 3
        ]
    )

def task5b():
    run_import_based_function_tests(
        "uke_01_oppg_5.py", 
        "distance",
        [
            # expected_return, expected_stdout, x1, y1, x2, y2
            [1.41421356237, "", 0, 0, 1, 1],     # Test 1
            [5, "", -1, -1, 2, 3],               # Test 2
            [5, "", 2, 3, -1, -1],               # Test 3
            [0, "", 9, 8, 9, 8],                 # Test 4
            [3, "", 0, 3, 0, 0],                 # Test 5
            [3, "", -3, 0, 0, 0]                 # Test 6
        ]
    )

def task5c():
    run_import_based_function_tests(
        "uke_01_oppg_5.py", 
        "circles_overlap",
        [
            # expected_return, expected_stdout, x1, y1, r1, x2, y2, r2
            [True, "", 0, 0, 1, 1, 1, 1],     # Test 1
            [False, "", 0, 0, 2, 4, 1, 2],    # Test 2
            [True, "", 0, 0, 3, 5, 0, 2],    # Test 3
        ]
    )

def task6():
    run_import_based_function_tests(
        "uke_01_oppg_6.py", 
        "joker",
        [
            # expected_return, expected_stdout, x1, x2, x3, x4, x5
            [None, "opp\nopp\nned\nned\nopp\n", 3, 4, 5, 6, 2],     # Test 1
            [None, "opp\nned\nned\nopp\nopp\n", 4, 5, 6, 2, 3],     # Test 2
            [None, "opp\nned\nned\nopp\nopp\n", 0, 9, 8, 1, 3],     # Test 3
        ]
    )


###############################################################################
### Helper functions for autograding ##########################################
###############################################################################

### Du er ikke forventet å forstå koden under. Vi vil ikke på noe tidspunkt i
### kurset eller på eksamen holde deg ansvarlig for å forstå koden under.

import io
import numbers
import os
import subprocess
import sys


def can_be_float(x):
    try:
        float(x)
    except:
        return False
    return True

def almost_equals(a, b):
    # Compare numbers
    if isinstance(a, numbers.Number) and isinstance(b, numbers.Number):
        return abs(a - b) < 0.000001
    # Compare strings
    elif isinstance(a, str) and isinstance(b, str):
        a = a.strip().split()
        b = b.strip().split()
        if len(a) != len(b):
            return False
        for i in range(len(a)):
            if can_be_float(a[i]) and can_be_float(b[i]):
                return almost_equals(float(a[i]), float[b[i]])
            if a[i] != b[i]:
                return False
        return True
    # Compare something else
    return a == b


def file_exists(filename):
    """ Return True if a file with the given filname exists in the
    working directory, and False otherwise."""
    try:
        with open(filename) as f:
            return True
    except FileNotFoundError:
        return False


def run_input_output_test(filename, provided_input, 
                            expected_output, timeout=4):
    """ Run an input/output -based test. The python script `filename`
    will be run with the provided_input given as input to the script on 
    standard input (i.e. as if a person was typing it in the terminal). 
    Actual output must match expected output EXACTLY, otherwise an error
    will be returned.

    Returns None if test passes without error, or error message otherwise."""

    # Check that the file exists
    if not file_exists(filename):
        return f"FEIL! Fant ikke filen {filename}"

    # Run the file as a python script and give the to_stdin string to stdin,
    # and check that output is correct
    python_executable = sys.executable # e.g. 'C:\path\to\python3.exe'
    try:
        process = subprocess.run([python_executable, filename],
            input=provided_input,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            encoding="utf-8",
            timeout=timeout)
    except subprocess.TimeoutExpired:
        return f'FEIL! Kjøring med input: \n' + \
                f'"""{provided_input or " ~ingen input~ "}"""\n' + \
                f'brukte for lang tid. Har koden en evig løkke?\n'
    actual_output = process.stdout
    if process.returncode != 0:
        return f'FEIL! Kjøring med input: \n' + \
                f'""{provided_input or " ~ingen input~ "}"""\n' + \
                f'førte til at programmet krasjet.\n\n' + \
                f'Feilmelding:\n"""{process.stderr}"""\n'
    elif actual_output.strip() != expected_output.strip():
        return f'FEIL! Kjøring med input: \n' + \
                f'"""{provided_input or " ~ingen input~ "}"""\n\n' + \
                f'forventet output: \n"""{expected_output}"""\n\n' + \
                f'men fikk output:\n"""{actual_output}"""\n'


def run_input_output_tests(filename, tests):
    """ Run a series of input/output -based tests with the filname script.
    The parameter `tests` should be a list of tuples, where each tuple is
    of the form (provided_input, expected_output)."""
    print(f"Tester {filename}:", end=" ", flush=True)
    for test in tests:
        to_stdin, expected_output = test
        error = run_input_output_test(filename, to_stdin, expected_output)
        if error:
            print("X ", end="")
            print(error)
            return False
        else:
            print(".", end="", flush=True)

    print(" Alle tester OK")

def run_and_capture(f, *args):
    """Run the function silently on *args. Returns return value of
    function call, standard output produced, standard error produced,
    and exception (if applicable). """
    save_stdout = sys.stdout
    save_stderr = sys.stderr
    sys.stdout = the_stdout = io.StringIO()
    sys.stderr = the_stderr = io.StringIO()
    try:
        return f(*args), the_stdout.getvalue().strip(), \
                the_stderr.getvalue().strip(), None
    except BaseException as ex:
        return None, the_stdout.getvalue().strip(), \
                the_stderr.getvalue().strip(), ex
    finally:
        sys.stdout = save_stdout
        sys.stderr = save_stderr


def test_runner(f, expected_return, expected_stdout, *args):
    """ Runs the function f with the provided args, and compares the
    result to the expected value. Returns an error message if test fails,
    and None if test passes."""
    # Check that the function f exists
    if not f:
        return f"FEIL! Fant ikke funksjonen f={f}"
    if type(f) != type(lambda: None):
        return f"FEIL! f={f} er ikke en funksjon"

    # Check that f accepts the correct number of arguments
    # Note that this version does not work with *args
    if f.__code__.co_argcount != len(args):
        return f"FEIL! {f} har ikke {len(args)} parametere"

    f_call = f'{f.__name__}({", ".join(map(str, args))})'

    # Perform the test
    actual_return, actual_stdout, err_msg, exception = run_and_capture(f, *args)

    # Check possible failures
    if exception:
        return f"FEIL! {f_call} krasjer med Exception:\n{exception}"
    if err_msg:
        return f'FEIL! {f_call} gav følgende feilmelding:\n"""{err_msg}"""'
    elif not almost_equals(actual_return, expected_return):
        return f"FEIL! {f_call} forventet returverdi '{expected_return}' " + \
                f"men fikk '{actual_return}'"
    elif not almost_equals(actual_stdout, expected_stdout):
        return f'FEIL! {f_call} forventet utskrift\n"""{expected_stdout}' + \
                f'"""\nmen fikk\n"""{actual_stdout}"""'

    return None
        

class DummyFile(object):
    """ Dummy channel for dumping output. """
    def write(self, x): pass


def import_function_from_file_silently(module_name, function_name):
    """ Importer en funksjon fra en modul. Returnerer en referanse til denne
    funksjonen, eller None hvis det skulle oppstå en feil."""

    save_stdout = sys.stdout
    sys.stdout = DummyFile()
    try:
        module = __import__(module_name)
        return getattr(module, function_name, None)
    except ImportError:
        return None
    finally:
        sys.stdout = save_stdout


def run_import_based_function_tests(filename, function_name, tests):
    print(f"Tester {filename} ({function_name}):", end=" ", flush=True)

    # Sjekk at filen finnes
    if not file_exists(filename):
        print("X ", end="")
        print(f"FEIL! Fant ikke filen '{filename}'")
        return False

    # Importer modulen og funksjonen
    module_name = filename.replace(".py", "")
    f = import_function_from_file_silently(module_name, function_name)
    if not f:
        print(f"FEIL! Klarte ikke importere '{function_name}'" + \
            f" fra {module_name}. Er metoden definert i denne filen?")
        return False

    for test in tests:
        error = test_runner(f, *test)
        if error:
            print("X ", end="")
            print(error)
            return False
        else:
            print(".", end="", flush=True)

    print(" Alle tester OK")


if __name__ == "__main__":
    currWorkDir = os.getcwd()
    import pathlib
    os.chdir(pathlib.Path(__file__).parent.resolve())
    # Run autograder
    run()
    os.chdir(currWorkDir)
