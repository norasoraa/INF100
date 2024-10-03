# For å kjøre dette programmet trenger dere å endre to punkter.
# Inne i funskjonen som heter 'create_new_format_csv_file(path_input)' på linje 35-38,
# må dere legge til navnet på den nye csv-filen som dere vil opprette.
# Dette gjør dere ved å endre der det står 'with open(....)' på linje 37.
# Da tar dere vekk 'expected_output.csv' og skriver inn navnet på filen dere vil opprette (den nye filen),
# husk å ta anførselstegn rundt navnet på filen.
# Etter dette må dere nederst i koden, hvor det står print(create_new_format_csv_file(...) på linje 40,
# endre argumentet til funksjonen 'create_new_format_csv_file(...)' ved å legge til navnet på csv-filen dere ønsker å endre.
# Dette gjør dere ved å ta vekk 'sample_input.csv' og skriver inn navnet på den filen dere vil endre (den gamle filen),
# husk også her å ta anførselstegn rundt navnet på filen.
# Til slutt trykker dere på trekanten/pilen oppe i høyre hjørne i vinduet som gjør at koden kjøres.
# Da vil det opprettes en ny fil med navnet dere valgte og det nye formatet inni.

def csv_file_to_list(path_input):
    with open(path_input, "rt", encoding='utf-8') as f:
        file_as_string = f.read()
    file_as_list = []
    for line in file_as_string.splitlines():
        line = line.split(",")
        file_as_list.append(line)
    return file_as_list
    
def each_patient(path_input):
    list_of_patients = csv_file_to_list(path_input)
    new_format_string = 'personnummer,medisin,dato,endring \n'
    for patient in list_of_patients[1:]:
        personnummer = str(patient[0])
        medisin = patient[1]
        startdato = patient[2]
        sluttdato = patient[3]
        new_format_string += f'{personnummer},{medisin},{startdato},1 \n'
        new_format_string += f'{personnummer},{medisin},{sluttdato},0 \n'
    return new_format_string

def create_new_format_csv_file(path_input):
    path_output = each_patient(path_input)
    with open('expected_output.csv', 'x') as f:
        f.write(path_output)

print(create_new_format_csv_file('sample_input.csv'))