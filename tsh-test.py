# Module to extract TSH scores of patients and diagnose them
import pytest
import json


# loads text from file
def file_loader():
    """Loads file with patient data and saves to variable data_all.

    param: none
    returns: string of all text in file_loader
    """
    file = open('test_data.txt', 'r')
    data_all = file.read()
    return data_all


# splits by line
def line_splitter(data):
    """Splits the text from file by line and stores sepeparate lines
    in the data_lines variable.

    param data: string of whole text from file

    returns data_lines: list of strings that are lines of the file
    """
    data_lines = data.split('\n')
    return data_lines


# extracts patient name
def extract_names(data_lines):
    """Collects all names of patients into the list names.

    param data_lines: list of strings of the lines of file

    returns names: list of names strings of all patients from file
    """
    names = []
    for i in range(int(len(data_lines)/4)):
        names.append(data_lines[4*i])
    return names


# extracts patient age
def extract_age(data_lines):
    """Collects all ages of patients into the list age.

    param data_lines: list of strings of the lines of file

    returns age: list of ages strings of all patients from file
    """
    age = []
    for i in range(int(len(data_lines)/4)):
        age.append(data_lines[4*i+1])
    return age


# extracts patient's sex
def extract_sex(data_lines):
    """Collects all sexes of patients into the list sex.

    param data_lines: list of strings of the lines of file

    returns sex: list of sex strings of all patients from file
    """
    sex = []
    for i in range(int(len(data_lines)/4)):
        sex.append(data_lines[4*i+2])
    return sex


# extracts patient's scores and converts to float
def extract_scores(data_lines):
    """Extracts scors of patients from file and stores in list scores.
    Then converts the scores to floats for further analysis.

    param data_lines: list of strings of the lines of file

    returns score_nums: list of floats of scores for each patients
    """
    scores = []
    score_nums = []
    for i in range(int(len(data_lines)/4)):
        scores.append(data_lines[4*i+3])
    for j in range(len(scores)):
        score_nums.append(scores[j].split(','))
    for k in range(0, len(score_nums)):
        for l in range(1, len(score_nums[k])):
            score_nums[k][l] = float(score_nums[k][l])
    for i in range(0,  len(score_nums)):
        del score_nums[i][0]
    return score_nums


# diagnoses patient and returns diagnosis
def diagnose_tsh(scores, patient):
    """Runs diagnosis for each patient based on min and max score of the TSH
    test and returns diagnosis.

    param scores: list of floats of scores for the particular patient

    param patient: int patient number for identification

    returns: diagnosis as a string output
    """
    if float(min(scores[patient])) < float(1.0):
        return 'hyperthyroidism'
    elif float(max(scores[patient])) > float(4.0):
        return 'hypothyroidism'
    else:
        return 'normal thyroid function'


# create dictionary
def create_patient_dict(names, age, sex, scores):
    """Creates a patient dictionary for all patients storing name, age, sex,
    scores and diagnosis.

    param names: name of all patients as strings
    param age: ages of all patients as strings
    param sex: sexes of all patients as strings
    param scores: scores of all patients as float lists

    returns patient_dict: dictionary of dictionaries for each patient
    """
    patient_dict = {}
    for i in range(0, len(names)):
        patient_dict[i] = {'name': names[i],
                        'age': age[i],
                        'sex': sex[i],
                        'scores': scores[i],
                        'diagnosis': diagnose_tsh(scores, i)
                        }
    return patient_dict


def create_json_file(patient_dict):
    """Creates a json file for each patient in which it stores the
    dictionary of each patient containing name, age, sex, scores and diagnosis.

    param patient_dict: dictionary for particular patient

    returns: creates .json file of patient data
    """
    name = patient_dict['name']
    name = name.split(' ')
    firstname = name[0]
    lastname = name[1]
    file = open(firstname+'-'+lastname, 'w')
    json.dump(patient_dict, file)
    file.close()

def full_diagnosis(patient_number):
    """Runs the whole diagnosis and returns a json file with results.

    param patient_number: int number of patient of interest

    returns: diagnosis as well as the .json file
    """
    tsh_all = file_loader()
    tsh_lines = line_splitter(tsh_all)
    names = extract_names(tsh_lines)
    age = extract_age(tsh_lines)
    sex = extract_sex(tsh_lines)
    scores = extract_scores(tsh_lines)
    patient = patient_number
    patient_dict = create_patient_dict(names, age, sex, scores)
    print(patient_dict[int(patient)]['name'])
    print(patient_dict[int(patient)]['age'])
    print(patient_dict[int(patient)]['sex'])
    print(patient_dict[int(patient)]['diagnosis'])
    for i in range(len(names)):
        create_json_file(patient_dict[i])
    return patient_dict[int(patient)]['diagnosis']

# to run code
if __name__ == '__main__':
    patient_number = input('patient number: ')
    full_diagnosis(patient_number)
