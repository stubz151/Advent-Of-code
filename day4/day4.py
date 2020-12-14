from common_logic import CommonLogic
import re


def get_value(batches):
    count = 0
    for x in batches:
        print(x)
        line = x.split(' ')
        tags_in_line_count = 0
        for val in line:
            tags = val.split(':')[0]
            if tags != 'cid':
                tags_in_line_count += 1
        if tags_in_line_count >= 7:
            count += 1
    return count


def get_value_second_test(batches):
    count = 0
    for x in batches:
        line = x.split(' ')
        tags_in_line_count = 0
        hclR = re.compile('[a-zA-Z0-9]*')
        for val in line:
            tags = val.split(':')[0]
            value_for_tag = val.split(':')[1]
            if tags == 'byr' and 1920 <= int(value_for_tag) <= 2002:
                tags_in_line_count += 1
            elif tags == 'iyr' and 2010 <= int(value_for_tag) <= 2020:
                tags_in_line_count += 1
            elif tags == 'eyr' and 2020 <= int(value_for_tag) <= 2030:
                tags_in_line_count += 1
            elif tags == 'hgt':
                m = re.split('(\d+)', value_for_tag)
                if m[2] == 'cm' and 150 <= int(m[1]) <= 193:
                    tags_in_line_count += 1
                elif m[2] == 'in' and 59 <= int(m[1]) <= 76:
                    tags_in_line_count += 1
            elif tags == 'hcl' and value_for_tag[0] == '#' and len(value_for_tag) == 7 and hclR.match(
                    value_for_tag[:1]):
                tags_in_line_count += 1
            elif tags == 'ecl' and (value_for_tag == 'amb' or value_for_tag == 'blu' or value_for_tag == 'brn' or
                                    value_for_tag == 'gry' or value_for_tag == 'hzl' or value_for_tag == 'oth'
                                    or value_for_tag == 'grn'):
                tags_in_line_count += 1
            elif tags == 'pid' and len(value_for_tag) == 9:
                tags_in_line_count += 1

        if tags_in_line_count >= 7:
            count += 1
    return count


if __name__ == '__main__':
    print(get_value_second_test(CommonLogic.get_input_as_batches()))
