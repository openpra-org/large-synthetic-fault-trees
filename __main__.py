import os
import shutil
# from scripts import fault_tree_generator
import re

def prepare_xfta(name):
    with open('xfta.template', 'r') as file:
        filedata = file.read()
    filedata = re.sub("NAME", name, filedata)
    with open("xfta_" + name + ".xml", 'w') as file:
        file.write(filedata)

# def run_codes():
#     command_to_run = "docker run -it --rm -v C:\Users\emaras\Desktop\xfta\xfta-1-3-1-win32:/usr/app supra scram /usr/app/FT-100.xml"


def generate_multiple_ft():

    num_basic = 100
    while (num_basic <= 300):
        command_to_generate = "python scripts/fault_tree_generator.py -b " + str(num_basic) + " -o codes/scram/ft_" + str(num_basic) + ".xml"
        # generate inputs in scram directory
        os.system(command_to_generate)
        # copy ft inputs to xfta directory
        shutil.copy("codes/scram/ft_" + str(num_basic) + ".xml", "codes/xfta/ft_" + str(num_basic) + ".xml")
        # generate xfta config file and move
        prepare_xfta("ft_"+str(num_basic))
        os.replace("xfta_ft_"+str(num_basic)+".xml", "codes/xfta/xfta_ft_"+str(num_basic)+".xml")
        # rest
        print(command_to_generate)
        num_basic += 100


if __name__ == '__main__':
    generate_multiple_ft()
    # prepare_xfta()
