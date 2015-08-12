import sys

def read_students_csv(filename):
    try:
        f = file(filename)
        lines = [line.strip() for line in f.readlines()]

        return {
            'header': lines[0],
            'records': lines[1:],
        }

    except IOError:
        print filename, 'does not exist'
        sys.exit()

    except IndexError:
        print 'Oops, you tried to read an empty file.'
        sys.exit()


def make_student(s, header):
    headers = header.split(',')
    parts = s.split(',')

    try:
        studentname = parts[0] or None
    except IndexError:
        studentname = None

    try:
        studentage = parts[1] or None
    except IndexError:
        studentage = None

    try:
        studentheight = parts[2] or None
    except IndexError:
        studentheight = None

    return {
        headers[0]: studentname,
        headers[1]: studentage,
        headers[2]: studentheight,
    }

def mean(numbers):
    return sum(numbers) * 1.0 / len(numbers)

def apply(li, funcname, rmnone=False):
    return funcname(filter(lambda x: x is not None, li))

def normalize(li, funcname):
    temp = []

    for el in li:
        try:
            temp.append(funcname(el))
        except:
            temp.append(el)

    return temp

def extract(data, field):
    return [element[field] for element in data]

def main():
    """
    1. fix make_student function so that it works with any file
    2. fix read_students_csv function so that it can also work with any file
    """

    students_csv = read_students_csv('students.csv')

    # transform raw student records (which are strings) into student dictionaries
    students = [make_student(record, students_csv['header']) for record in students_csv['records']]

    print apply(normalize(extract(students, 'studentage'), float), mean, rmnone=True)

    print apply(normalize(extract(students, 'studentheight'), float), sum, rmnone=True)


if __name__ == '__main__':
    main()
