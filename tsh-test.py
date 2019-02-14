import pytest


def file_loader():
    file = open('test_data.txt', 'r')
    data_all = file.read()
    return data_all

def line_splitter(data):
    data_lines = data.split('\n')
    return data_lines

def extract_names(data_lines):
    names = []
    for i in range(int(len(data_lines)/4)-1):
        names.append(data_lines[4*i])
    print('names')
    print(names)
    return names

def extract_age(data_lines):
    age = []
    for i in range(int(len(data_lines)/4)-1):
        age.append(data_lines[4*i+1])
    print('age')
    print(age)
    return age

def extract_sex(data_lines):
    sex = []
    for i in range(int(len(data_lines)/4)-1):
        sex.append(data_lines[4*i+2])
    print('sex')
    print(sex)
    return sex

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
            print(k)
            print(l)
            print(score_nums[k][l])
    print('scores')
    print(score_nums)
    return score_nums

if __name__ == '__main__':
    tsh_all = file_loader()
    tsh_lines = line_splitter(tsh_all)
    names = extract_names(tsh_lines)
    age = extract_age(tsh_lines)
    sex = extract_sex(tsh_lines)
    scores = extract_scores(tsh_lines)
