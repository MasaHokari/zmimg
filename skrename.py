#
# Generate rename script
#
# Written by Masa Hokari
# Started on 2021-01-05
#
# This script generates a script to rename a set of files.
#
# Example:
# python3 skrename.py
#
# original file name:
# SJH2-1.2020-12-19 at 10.27.59 AM-2.png
#
# new file name:
# classphoto.sj_11_1.2020-12-19 at 10.27.59 AM-2.png
#

import glob
import regex
import sys


PATTERN = '(?<campus>SJ|SF)(((?<level>K|E|M|H)(?<grade>\\d*)-(?<class>(\\d|\\w+))))\\.*(?<uid>.*)\\.(png)'
MASK = '*.png'
NEW_FORMAT1 = 'classphoto.{campus2}_{grade2}_{class_number2}.png'
NEW_FORMAT2 = 'classphoto.{campus2}_{grade2}_{class_number2}.{uid}.png'
MV_CMD_LINE = 'mv \'{file_name}\' \'{new_file_name}\''
ERROR_LINE = '# ERROR: {file_name}'


def get_substring(regex_match, group_name):
    group_index = regex_match.re.groupindex[group_name]
    start = regex_match.regs[group_index][0]
    end = regex_match.regs[group_index][1]
    string = regex_match.string
    return string[start:end]


def get_campus(value):
    if value == 'SF':
        return 'sf'
    elif value == 'SJ':
        return'sj'
    else:
        raise ValueError(f'Unknown campus value: {value}')


def get_grade_base(value):
    if value == 'K':
        return 0
    elif value == 'E':
        return 1
    elif value == 'M':
        return 7
    elif value == 'H':
        return 10
    else:
        raise ValueError(f'Unknown level value: {value}')


def get_grade_offset(value):
    if value == '':
        return 0
    elif value == '1':
        return 0
    elif value == '2':
        return 1
    elif value == '3':
        return 2
    elif value == '4':
        return 3
    elif value == '5':
        return 4
    elif value == '6':
        return 5
    else:
        raise ValueError(f'Unknown grade value: {value}')


def get_class_number(value):
    if value == '1':
        return 1
    elif value == '2':
        return 2
    elif value == '3':
        return 3
    elif value == '4':
        return 4
    elif value == '5':
        return 5
    elif value == '6':
        return 6
    elif value == '7':
        return 7
    elif value == '8':
        return 8
    elif value == '9':
        return 9
    elif value == 'Hitsuji':
        return 'hitsuji'
    elif value == 'Kirin':
        return 'kirin'
    elif value == 'Risu':
        return 'risu'
    elif value == 'Usagi':
        return 'usagi'
    else:
        raise ValueError(f'Unknown class_number value: {value}')


def get_file_name(campus, level, grade, class_number, uid):
    campus2 = get_campus(campus)
    grade2 = get_grade_base(level)
    grade2 += get_grade_offset(grade)
    class_number2 = get_class_number(class_number)
    if (uid is None) or uid == '':
        return NEW_FORMAT1.format(campus2=campus2, grade2=grade2, class_number2=class_number2, uid=uid)
    return NEW_FORMAT2.format(campus2=campus2, grade2=grade2, class_number2=class_number2, uid=uid)


def make_batch():
    commands = []
    for file_name in glob.glob(MASK):
        regex_match = regex.search(PATTERN, file_name)
        if regex_match is not None:
            campus = get_substring(regex_match, 'campus')
            level = get_substring(regex_match, 'level')
            grade = get_substring(regex_match, 'grade')
            class_number = get_substring(regex_match, 'class')
            uid = get_substring(regex_match, 'uid')
            new_file_name = get_file_name(campus, level, grade, class_number, uid)
            commands.append(MV_CMD_LINE.format(file_name=file_name, new_file_name=new_file_name))
        else:
            commands.append(ERROR_LINE.format(file_name=file_name))
    commands.sort()
    return commands


def print_each_line(items):
    for item in items:
        print(item)


def main():
    commands = make_batch()
    print_each_line(commands)


if __name__ == '__main__':
    if sys.version_info[0] < 3:
        raise Exception("This program requires Python 3 or later.")
    main()
