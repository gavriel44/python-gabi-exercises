import csv
import datetime


def write_dict_to_csv(file_name, dictionary: dict):

    try:
        current_time = datetime.datetime.now().strftime("%H-%M-%S")
        with open(file_name, 'w') as f:
            for key in dictionary.keys():
                f.write("%s,%s\n" % (key, dictionary[key]))
    except IOError:
        print("I/O error")
