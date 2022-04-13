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

def run_xfta(xfta_config_name):
    xfta_exec_dir = "C:/Users/emaras/Desktop/xfta/xfta-1-3-1-win32/"
    command_to_run_xfta = xfta_exec_dir + "xftar " + xfta_config_name
    print(command_to_run_xfta)
    os.system(command_to_run_xfta)

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
        print(os.getcwd() + "/codes/xfta/xfta_ft_" + str(num_basic) + ".xml")
        run_xfta(os.getcwd() + "/codes/xfta/xfta_ft_" + str(num_basic) + ".xml")
        # print(command_to_generate)
        num_basic += 100

if __name__ == '__main__':
    if not os.path.exists("codes/scram"):
        os.makedirs("codes/scram")
    if not os.path.exists("codes/xfta"):
        os.makedirs("codes/xfta")
    generate_multiple_ft()
    # prepare_xfta()
