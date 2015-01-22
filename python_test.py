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
        print "before clean %s" %arg
        arg = arg.rstrip('\n')
        print "after clean %s" %arg


        #and append it to the list
        cleaned_list.append(int(arg) if arg.isdigit() else arg)
    print cleaned_list

    #print cleaned_list


    #call sort on the list
    sort_data(*cleaned_list)


def sort_data(*args):
    #sort the data


    #format the data


    #call write to file with the filename and the list
    write_to_file('bananana file', *args)


def write_to_file(filename, *args):
    pass
    #create a new file

    #write the data to the file

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
