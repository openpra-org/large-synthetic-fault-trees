import os
import shutil
import re

"""
--This scrip is able to create fault trees by allowing user to set number of basic events.
--The created fault trees are stored in as .xml in open PRA format.
--The quantification of fault trees are done using XFTA version 1.0 and SCRAM.
"""
###############################################################################################
#Creating a config .xml file tp run XFTA from a template
def prepare_xfta(name):

    with open('xfta.template', 'r') as file:
        filedata = file.read()
    filedata = re.sub("NAME", name, filedata)
    with open("xfta_" + name + ".xml", 'w') as file:
        file.write(filedata)
###############################################################################################

###############################################################################################
#Running XFTA with the command line
def run_xfta(xfta_config_name):
    xfta_exec_dir = "C:/Users/emaras/Desktop/xfta/xfta-1-3-1-win32/"
    command_to_run_xfta = xfta_exec_dir + "xftar " + xfta_config_name
    print(command_to_run_xfta)
    os.system(command_to_run_xfta)
###############################################################################################

###############################################################################################
#Running SCRAM with the command line
def run_scram(scram_input):
    scram_exec_command = "docker run -it --rm -v " + os.getcwd() + "/codes/scram:/scram supra scram /scram/" + scram_input + ".xml --mocus --probability --importance > codes/scram/" + scram_input + ".txt"
    print(scram_exec_command)
    os.system(scram_exec_command)
    #print(scram_input + '.xml kostu')
###############################################################################################

###############################################################################################
#Creating fault tree
def generate_multiple_ft():

    num_basic = 100
    while (num_basic <= 1000):
        command_to_generate = "python scripts/fault_tree_generator.py -b " + str(num_basic) + " -o codes/scram/ft_" + str(num_basic) + ".xml"
        # generate inputs in scram directory
        os.system(command_to_generate)
        run_scram("ft_" + str(num_basic))
        # copy ft inputs to xfta directory
        shutil.copy("codes/scram/ft_" + str(num_basic) + ".xml", "codes/xfta/ft_" + str(num_basic) + ".xml")
        # generate xfta config file and move
        prepare_xfta("ft_"+str(num_basic))
        os.replace("xfta_ft_"+str(num_basic)+".xml", "codes/xfta/xfta_ft_"+str(num_basic)+".xml")
        # rest
        run_xfta(os.getcwd() + "/codes/xfta/xfta_ft_" + str(num_basic) + ".xml")
        num_basic += 100
###############################################################################################

###############################################################################################
if __name__ == '__main__':
    if not os.path.exists("codes/scram"):
        os.makedirs("codes/scram")
    if not os.path.exists("codes/xfta"):
        os.makedirs("codes/xfta")
    generate_multiple_ft()
    # prepare_xfta()
###############################################################################################