from sys import argv
import re

def read_from_file(file):
    #get the list from the file
    with open((file),'rb') as file:
        my_list = file.read().split(' ')

    clean_list_items(*my_list)


def clean_list_items(*args):
    cleaned_list = []
    for arg in args:

        #strip the element of weird characters and clean it
        #print "before clean %s" %arg
        cleaned_arg = arg.rstrip('\n')
        #print "after clean %s" %arg

        #and append it to the list
        cleaned_list.append(int(cleaned_arg) if arg.isdigit() else cleaned_arg)

    #call sort on the list
    sort_data(*cleaned_list)


def sort_data(*args):

    #sort the data
    ints_sorted = sorted([arg for arg in args if type(arg) == int])
    strings_sorted = sorted([arg for arg in args if type(arg) == str])
    sorted_data = []

    for arg in args:
        print "evaluating arg %s" %arg

        if isinstance(arg, int):
            item = ints_sorted.pop(0)
            print "popping item %s" %item

            sorted_data.append(item)
            print "item %s appended to sorted_list" %item

        if isinstance(arg, str):
            item = strings_sorted.pop(0)
            print "popping item %s" %item
            sorted_data.append(item)
            print "item %s appended to sorted_list" %item

    #call write to file with the filename and the list
    write_to_file('sorted_file.txt', *sorted_data)


def write_to_file(filename, *args):
    #create a new file
    with open(filename, 'w') as newfile:
        for arg in args:
            #write the data to the file
            newfile.write("%s " % arg)
        newfile.close()


def main(filename):
    try:
        read_from_file(filename)
        #read_from_file(filename)
    except EOFError:
        print "bye"
        exit()

if __name__ == "__main__":
    script, filename = argv
    main(filename)
