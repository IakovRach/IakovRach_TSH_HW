#Module to extract TSH scores of patients and diagnose them
import pytest

#laods text from file
def file_loader():
    file = open('test_data.txt', 'r')
    data_all = file.read()
    return data_all


#splits by line
def line_splitter(data):
    data_lines = data.split('\n')
    return data_lines


#extracts patient name
def extract_names(data_lines):
    names = []
    for i in range(int(len(data_lines)/4)-1):
        names.append(data_lines[4*i])
    return names


#extracts patient age
def extract_age(data_lines):
    age = []
    for i in range(int(len(data_lines)/4)-1):
        age.append(data_lines[4*i+1])
    return age


#extracts patient's sex
def extract_sex(data_lines):
    sex = []
    for i in range(int(len(data_lines)/4)-1):
        sex.append(data_lines[4*i+2])
    return sex


#extracts patient's scores and converts to float
def extract_scores(data_lines):
    scores = []
    score_nums = []
    for i in range(int(len(data_lines)/4)-1):
        scores.append(data_lines[4*i+3])
    for j in range(len(scores)):
        score_nums.append(scores[j].split(','))
    for k in range(0, len(score_nums)):
        for l in range (1, len(score_nums[k])):
            score_nums[k][l] = float(score_nums[k][l])
    for i in range(0,  len(score_nums)):
        del score_nums[i][0]
    return score_nums


#diagnoses patient and returns diagnosis
def diagnose_tsh(scores, patient):
    if float(min(scores[patient])) < float(1.0):
        return 'hyperthyroidism'
    elif float(max(scores[patient])) > float(4.0):
        return 'hypothyroidism'
    else:
        return 'normal thyroid function'


#to run code
if __name__ == '__main__':
    tsh_all = file_loader()
    tsh_lines = line_splitter(tsh_all)
    names = extract_names(tsh_lines)
    age = extract_age(tsh_lines)
    sex = extract_sex(tsh_lines)
    scores = extract_scores(tsh_lines)
    patient = input('Enter patient number: ')
    print(diagnose_tsh(scores, int(patient)))
