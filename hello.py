import collections
import csv
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


def make_data1(s, header):
    """ the limitation here is that if there are less values in parts than in headers, we'll skip that header and we'll get an incomplete record.
    our records should always always have the same number of fields even if the fields are empty
    """
    headers = header.split(',')
    parts = [part.strip() or None for part in s.split(',')]

    return dict(zip(headers, parts))

def make_data2(s, header):
    headers = header.split(',')
    parts = s.split(',')

    d = {}

    for i, header in enumerate(headers):

        try:
            d[header] = parts[i] or None
        except IndexError:
            d[header] = None

    return d

def make_data3(s, header):
    """ limitation is that parts and headers should be of the same length
    otherwise we can get an exception at parts[i]
    """
    headers = header.split(',')
    parts = [part.strip() or None for part in s.split(',')]

    return { header: parts[i] for i, header in enumerate(headers) }


def mean(numbers):
    return sum(numbers) * 1.0 / len(numbers)

def apply(li, funcname, rmnone=False):
    return funcname(filter(lambda x: x != '', li))


def myfilter1(li, can_keep):
    newlist = []
    for el in li:
        if can_keep(el):
            newlist.append(el)
    return newlist

# 1. we copy the start of for loop as it is
# [for el in li]
# 2. we copy the condition inside the loop if any
# [for el in li if can_keep(el)]
# 3. we do the append part
# [el for el in li if can_keep(el)]

def myfilter2(li, can_keep):
    return [el for el in li if can_keep(el)]

def myfilter3(li, can_keep):
    li_copy = li[::]

    for el in li:
        if not can_keep(el):
            li_copy.remove(el)

    return li_copy

#myfilter2([1, 2, 1, 2, 3, 1, 4, 5], lambda x: x == 1)

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

def normalize_name(name):
    name = name.strip()
    name = name.capitalize()
    return name


def read_csv(filename):
    with file(filename) as f:
        reader = csv.DictReader(f)
        return list(reader)

def write_csv(filename, data, fieldnames):
    with file(filename, 'w') as f:
        writer = csv.DictWriter(f, fieldnames)
        writer.writeheader()
        writer.writerows(data)


def main():
    #students_csv = read_students_csv('students.csv')
    # transform raw student records (which are strings) into student dictionaries
    #students = [make_data2(record, students_csv['header']) for record in students_csv['records']]

    students = read_csv('students.csv')

    print apply(normalize(extract(students, 'studentage'), float), mean, rmnone=True)
    print apply(normalize(extract(students, 'studentheight'), float), sum, rmnone=True)
    print apply(normalize(extract(students, 'studentname'), normalize_name), collections.Counter, rmnone=True)


if __name__ == '__main__':
    main()



# atharh@gmail.com
def get_weather_data(location):
    response = r.get("http://api.openweathermap.org/data/2.5/weather?q=" + location)
    # once you get the json and json.loads it, then
    # extract any fields you want and return them
    # in a dict

    return {
        'lat': '',
        'long': '',
        'humidity': '',
    }

