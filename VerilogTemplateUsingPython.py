#Sherouk Ali Ali
import re
import random

###################### the required lists ###########################################
input_signals=[]
input_widths=[]

output_widths=[]
output_signals=[]

parameters_names=[]
parameters_values=[]

internal_wire_signals=[]
internal_wire_signals_widths=[]

internal_reg_signals=[]
internal_reg_signals_widths=[]
#-----------------------------------------
tb_parameters_names=[]
tb_parameters_values=[]

################################ function to check the valid name #########################################


def is_valid_signal_name(name):

    # Verilog reserved words
    reserved_words = set([
        'always', 'and', 'assign', 'automatic', 'begin', 'buf', 'bufif0', 'bufif1', 'case', 'casex',
        'casez', 'cmos', 'deassign', 'default', 'defparam', 'disable', 'else', 'end', 'endcase', 'endfunction',
        'endmodule', 'endprimitive', 'endspecify', 'endtable', 'endtask', 'event', 'for', 'force', 'forever',
        'fork', 'function', 'if', 'ifnone', 'initial', 'inout', 'input', 'integer', 'join', 'macromodule',
        'module', 'nand', 'negedge', 'nmos', 'nor', 'not', 'notif0', 'notif1', 'or', 'output', 'parameter',
        'pmos', 'posedge', 'primitive', 'pull0', 'pull1', 'pulldown', 'pullup', 'rcmos', 'real', 'realtime',
        'reg', 'release', 'repeat', 'rnmos', 'rpmos', 'rtran', 'rtranif0', 'rtranif1', 'scalared', 'signed',
        'small', 'specify', 'specparam', 'strong0', 'strong1', 'supply0', 'supply1', 'table', 'task', 'time',
        'tran', 'tranif0', 'tranif1', 'tri', 'tri0', 'tri1', 'triand', 'trior', 'trireg', 'unsigned', 'use',
        'vectored', 'wait', 'wand', 'weak0', 'weak1', 'while', 'wire', 'wor', 'xnor', 'xor'
    ])

    if name.lower() in reserved_words:
        return False
    if not re.match(r'^[a-zA-Z_][a-zA-Z0-9$_]*$', name):
        return False
    if name.find('$') > 0:
        return True
   
    return True

############################## check if the entered name is previosls entered #################################
def isexist(prev_entered_name):
    for i in range(len(input_signals)):
        if prev_entered_name==input_signals[i]:
            print("\033[1;37;41m\n This name is previously used \033[0;0;0m")
            return False
    for i in range(len(output_signals)):
        if prev_entered_name==output_signals[i]:
            print("\033[1;37;41m\n This name is previously used \033[0;0;0m") 
            return False
    for i in range(len(parameters_names)):
        if prev_entered_name==parameters_names[i]:
            print("\033[1;37;41m\n This name is previously used \033[0;0;0m") 
            return False
    for i in range(len(internal_wire_signals)):
        if prev_entered_name==internal_wire_signals[i]:
            print("\033[1;37;41m\nThis name is previously used \033[0;0;0m")
            return False
    for i in range(len(internal_reg_signals)):
        if prev_entered_name==internal_reg_signals[i]:
            print("\033[1;37;41m\n This name is previously used \033[0;0;0m")
            return False
    return True  
###################################### check if the entered param name of tb is previously entered#################################
def is_param_tb_exist(prev_entered_name):
    for i in range(len(tb_parameters_names)):
        if prev_entered_name==tb_parameters_names[i]:
            print("\033[1;37;41m\n This name is previously used \033[0;0;0m")
            return False
    return True    
###################################### Enter module name ############################
def Module_Name():
    while True:
        module_name=input("\nEnter the module name: ")
        print("*****************")
        if is_valid_signal_name(module_name):
            return module_name
            
        else:
            print("\033[1;37;41m\n Invalid module name. Please follow Verilog naming rules.\033[0;0;0m")
            
                
############################### Enter inputs #################################
def inputs ():
    while True:
        num_inputs = input("\n<<< Enter the number of input signals without clock signals:>>> ")
        print("*****************")
        if num_inputs.isdigit():
            for i in range(int(num_inputs)):
                while True:
                    input_sig=input(f"\nEnter the name of input signal {i+1}: ")
                    print("*****************")
                    if is_valid_signal_name(input_sig) and isexist(input_sig) :  
                        input_signals.append(input_sig)
                        while True:
                            sig_width=input(f"\nEnter the width of input signal {i+1}: ")
                            print("*****************")
                            if sig_width.isdigit() and (sig_width !='0'):
                                input_widths.append(sig_width)
                                break
                            else:
                                print("\033[1;37;41m\n Invalid width!, must be numerical value >0. \033[0;0;0m")        
                        break
                    else:
                        print("\033[1;37;41m\n Invalid signal name. Please follow Verilog naming rules.\033[0;0;0m")        
            break

        else:
            print("\033[1;37;41m\n Invalid input, enter a valid numerical value.\033[0;0;0m")
            
 
############################### Enter outputs ###################################################


def outputs():
    while True:
        num_outputs = (input("\n<<< Enter the number of output signals:>>> "))
        print("*****************")
        if num_outputs.isdigit():
            for i in range(int(num_outputs)):
                while True:
                    output_sig=input(f"\nEnter the name of output signal {i+1}: ")
                    print("*****************")
                    if is_valid_signal_name(output_sig) and isexist(output_sig):
                        output_signals.append(output_sig)
                        while True:
                            sig_width=input(f"\nEnter the width of output signal {i+1}: ")
                            print("*****************")
                            if sig_width.isdigit() and (sig_width !='0'):
                                output_widths.append(sig_width)
                                break
                            else:
                                print("\033[1;37;41m\n Invalid width!, must be numerical value >0.\033[0;0;0m") 
                                
                        break
                    else:
                        print("\033[1;37;41m\n Invalid signal name. Please follow Verilog naming rules.\033[0;0;0m") 
                   
            break 
        else:
            print("\033[1;37;41m\n Invalid value, enter a valid numerical value.\033[0;0;0m")
            
############################### Enter parameters ################################################

def design_parameters():
    while True:
        num_parameters = (input("\n<<< Enter the number of parameters:>>> "))
        print("*****************")
        if num_parameters.isdigit():
            for i in range(int(num_parameters)):
                while True:
                    param=input(f"\nEnter the name of parameter {i+1}: ")
                    print("*****************")
                    if is_valid_signal_name(param) and isexist(param):
                        parameters_names.append(param)
                        while True:
                            param_value=input(f"\nEnter the value of parameter {i+1}: ")
                            print("*****************")
                            if param_value.isdigit():
                                parameters_values.append(param_value)
                                break
                            else:
                                print("\033[1;37;41m\n Invalid value, enter a valid numerical value. \033[0;0;0m")
                                
                        break
                    else:
                        print("\033[1;37;41m\n Invalid parameter name. Please follow Verilog naming rules. \033[0;0;0m") 
                   
            break 
        else:
            print("\033[1;37;41m\n Invalid value, enter a valid numerical value.\033[0;0;0m")

###################################### the internal reg signals ######################################
            
def enter_internal_reg_signals ():
    while True:
        num_internal_regs = (input("\n<<< Enter the number of internal_reg signals:>>> "))
        print("*****************")
        if num_internal_regs.isdigit():
            for i in range(int(num_internal_regs)):
                while True:
                    internal_reg_sig=input(f"\nEnter the name of internal_reg signal {i+1}: ")
                    print("*****************")
                    if is_valid_signal_name(internal_reg_sig) and isexist(internal_reg_sig):
                        internal_reg_signals.append(internal_reg_sig)
                        while True:
                            sig_width=input(f"\nEnter the width of internal_reg signal {i+1}: ")
                            print("*****************")
                            if sig_width.isdigit() and (sig_width !='0'):
                                internal_reg_signals_widths.append(sig_width)
                                break
                            else:
                                print("\033[1;37;41m\n Invalid width!, must be numerical value >0. \033[0;0;0m") 
                                
                        break
                    else:
                        print("\033[1;37;41m\n Invalid signal name. Please follow Verilog naming rules. \033[0;0;0m") 
                   
            break 
        else:
            print("\033[1;37;41m\n Invalid value, enter a valid numerical value. \033[0;0;0m")
            
###################################### the internal wire signals ######################################
     
def enter_internal_wire_signals ():
    while True:
        num_internal_wires = (input("\n<<< Enter the number of internal_wires signals:>>> "))
        print("*****************")
        if num_internal_wires.isdigit():
            for i in range(int(num_internal_wires)):
                while True:
                    internal_wire_sig=input(f"\nEnter the name of internal_wire signal {i+1}: ")
                    print("*****************")
                    if is_valid_signal_name(internal_wire_sig) and isexist(internal_wire_sig):
                        internal_wire_signals.append(internal_wire_sig)
                        while True:
                            sig_width=input(f"\nEnter the width of internal_wire signal {i+1}: ")
                            print("*****************")
                            if sig_width.isdigit() and (sig_width !='0'):
                                internal_wire_signals_widths.append(sig_width)
                                break
                            else:
                                print("\033[1;37;41m\n Invalid width!, must be numerical value >0. \033[0;0;0m") 
                                
                        break
                    else:
                        print("\033[1;37;41m\n Invalid signal name. Please follow Verilog naming rules. \033[0;0;0m") 
                   
            break 
        else:
            print("\033[1;37;41m\n Invalid value, enter a valid numerical value. \033[0;0;0m")
            
######################################## Specify the type of the design #######################################
def design_type():
    print("\033[1;30;47m\n Specify whether the design is sequential or combinantional or compound: \033[0;0;0m")

    while True:
        design_type=input("\nEnter '0' for sequential, '1' for combinantional, '2' for compound design : ")
        print("*****************")
        if design_type=='0' or design_type=='1' or design_type=='2':
            return design_type
        else:
            print("\033[1;37;41m\n Invalid value, enter a numerical value '0' or '1' or '2': \033[0;0;0m")            
            
######################################## Specify the type of clk edge ########################################  
def clock_edge ():
        print("\033[1;30;47m\n Specify the type of clk edge: \033[0;0;0m")

        while True:
            clk_edge=input("\nEnter '0' for positive edge or '1' for negative edge:  ")
            print("*****************")
            if clk_edge=='0':
                clock_edge="posedge"
                return clock_edge
            elif clk_edge=='1':
                clock_edge="negedge"
                return clock_edge
            else:
                print("\033[1;37;41m\n Invalid value, enter a numerical value '0' or '1': \033[0;0;0m")
##################################################################################################
def is_synchronous():
    print("\033[1;30;47m\n Specify whether the reset signal is Synchronous or Asynchronous: \033[0;0;0m")

    while True:
        is_Synch=input("\nEnter '1' for Synchronous or '0' for Asynchronous:  ")
        print("*****************")
        if is_Synch=='1' or is_Synch=='0':
            return is_Synch
        else:
            print("\033[1;37;41m\n Invalid value, enter a numerical value '0' or '1': \033[0;0;0m")

#########################################################################################
def assign_statements():
    
    while True:
        assign_num=input("\nEnter the number of assign statements: ")
        if assign_num.isdigit():
            return assign_num
        else:
            print("\033[1;37;41m\n Invalid value, enter a valid numerical value. \033[0;0;0m")
    
#################################### call  functions ###############################################
module_name=Module_Name() 
inputs()
outputs()
design_parameters()
design_type=design_type()

    
if ( design_type=='0' or design_type=='2'):
    enter_internal_reg_signals ()
    is_sync=is_synchronous()
    clk_edge=clock_edge ()

if ( design_type=='1' or design_type=='2'):
    enter_internal_wire_signals ()
    assign_statement_num=assign_statements()
        
############################### write the design into file  #######################################

with open(f"{module_name}.v", "w") as file:
    
    file.write(f"module {module_name} (") 
        
#-----------------------------------------------------------------------------------------------
   
    if (design_type=='2' or design_type=='0'):
        file.write("\n// Input Ports")
        file.write("\ninput   clk,  //clock signal")
        if  len(output_signals)==0 and len(input_signals)==0 :           
            file.write("\ninput   rst  //reset signal")
        else:
            file.write("\ninput   rst,  //reset signal")
    if (design_type=='1' and len(input_signals)!=0 ):
        file.write("\n// Input Ports")        
                    
    for i in range(len(input_signals)):
        if len(output_signals)==0:
            if (i<len(input_signals)-1) :
                if input_widths[i]=='1':
                    file.write(f"\ninput    {input_signals[i]},")
                else:
                    file.write(f"\ninput    [{input_widths[i]}-1:0]  {input_signals[i]},")
            else:
                if input_widths[i]=='1':
                    file.write(f"\ninput    {input_signals[i]}")
                else:
                    file.write(f"\ninput    [{input_widths[i]}-1:0]  {input_signals[i]}")
        
        else:
            if input_widths[i]=='1':
                file.write(f"\ninput    {input_signals[i]},")
            else:
                file.write(f"\ninput    [{input_widths[i]}-1:0]  {input_signals[i]},")    
                      
        file.write("\n")         
       
#-----------------------------------------------------------------------------------------------        
    while len(output_signals)!=0:
        file.write("\n// output Ports")    
        for i in range(len(output_signals)):
            
            if (i<len(output_signals)-1):
                if output_widths[i]=='1':
                    file.write(f"\noutput     {output_signals[i]},")
                else:
                    file.write(f"\noutput    [{output_widths[i]}-1:0]  {output_signals[i]},")
                    
            else:
                if output_widths[i]=='1':
                    file.write(f"\noutput   {output_signals[i]}")
                else:
                    file.write(f"\noutput   [{output_widths[i]}-1:0]  {output_signals[i]}")
                    
        file.write("\n")        
        break
    if len(output_signals)!=0 or len(input_signals)!=0 or (design_type=='2' or design_type=='0'):
        file.write("\n") 
        file.write(");")
    else:
        file.write(");")
    
    
#----------------------------------------------------------------------------------------------    
    for i in range(len(parameters_names)):
            file.write(f"\nparameter {parameters_names[i]}={parameters_values[i]};")     
#---------------------------------------------------------------------------------------------------------  
           
    while len(internal_wire_signals)!=0:
        file.write("\n//Internal wire Signals")
        for i in range(len(internal_wire_signals)):
            if internal_wire_signals_widths[i]=='1':
                file.write(f"\nwire  {internal_wire_signals[i]};")
            else:
                file.write(f"\nwire  [{internal_wire_signals_widths[i]}-1:0]  {internal_wire_signals[i]};")
                
        break
#---------------------------------------------------------------------------------------------------------    
        
    while len(internal_reg_signals)!=0:
        file.write("\n// Internal reg Signals")
        for i in range(len(internal_reg_signals)):
            if internal_reg_signals_widths[i]=='1':
                file.write(f"\nreg  {internal_reg_signals[i]};")
            else:
                file.write(f"\nreg  [{internal_reg_signals_widths[i]}-1:0]  {internal_reg_signals[i]};")
                
        break
#--------------------------------------------------------------------------------------------------------- 
   
    if (design_type=='2' or design_type=='1'):
         
        while assign_statement_num !='0':
            file.write("\n// Combinational Logic")
            if int(assign_statement_num) > len(internal_wire_signals):
                for i in range(len(internal_wire_signals)):
                    file.write(f"\nassign  {internal_wire_signals[i]}=         //assign value to the internal wire")
                for i in range(int(assign_statement_num)-len(internal_wire_signals)):
                    file.write("\nassign")
            else:
                for i in range(int(assign_statement_num)):
                    file.write(f"\nassign  {internal_wire_signals[i]}=         //assign value to the internal wire")
                
            break 
            
        
#---------------------------------------------------------------------------------------------------------    

    if (design_type=='2' or design_type=='0'):
        file.write("\n// Sequential Logic")
        
        if is_sync=='1':   # synchronous reset
            file.write(f"""\n always@({clk_edge} clk) begin
                if (rst)
                begin
                    // Reset logic here
                    
                end 
                else
                begin
                    // Sequential logic here
                    
                end
            end""") 
            
        else:  # Asynchronous reset
            file.write(f"""\n always@({clk_edge} clk or negedge rst) begin
                if (!rst)
                begin
                    // Reset logic here
                    
                end 
                else
                begin
                    // Sequential logic here
                    
                end
            end""")
        
    
        
    file.write("\nendmodule")    
######################################### the script of testbench ##############################################
while True:
    num_tb_parameters = (input("\nEnter the number of testbench parameters: "))
    print("*****************")
    if num_tb_parameters.isdigit():
        for i in range(int(num_tb_parameters)):
            while True:
                param=input(f"\nEnter the name of parameter {i+1}: ")
                print("*****************")
                if is_valid_signal_name(param) and is_param_tb_exist(param):
                    tb_parameters_names.append(param)
                    while True:
                        param_value=input(f"\nEnter the value of parameter {i+1}: ")
                        print("*****************")
                        if param_value.isdigit():
                            tb_parameters_values.append(param_value)
                            break
                        else:
                            print("\033[1;37;41m\n Invalid value, enter a valid numerical value. \033[0;0;0m")
                            
                    break
                else:
                    print("\033[1;37;41m\nInvalid parameter name. Please follow Verilog naming rules. \033[0;0;0m") 
               
        break 
    else:
        print("\033[1;37;41m\n Invalid value, enter a valid numerical value. \033[0;0;0m")
    
#################################################################################################
while True:
    period=input("\nEnter the waiting period: ")
    if period.isdigit():
        break
        
    else:
        print("\033[1;37;41m\n Invalid value, enter a valid numerical value. \033[0;0;0m")
################################################################################################
while True:
    testcases_num=input("\nEnter the number of test cases: ")
    if testcases_num.isdigit():
        break
    else:
        print("\033[1;37;41m\n Invalid value, enter a valid numerical value. \033[0;0;0m") 
      

############################### write the testbench into file  ##################################################

with open(f"{module_name}_testbench.v", "w") as file:
    
    file.write("\n`timescale 1ns/1ns")
    file.write(f"\nmodule {module_name}_TB ();")
#----------------------------------------------------------------------------  
    if (design_type=='2' or design_type=='0'):
        file.write("\nreg   clk;")
        file.write("\nreg   rst;")
    for i in range(len(input_signals)):       
        if input_widths[i]=='1':
            file.write(f"\nreg   {input_signals[i]}_tb;")        
        else:
            file.write(f"\nreg  [{input_widths[i]}-1:0]  {input_signals[i]}_tb;")
        
#----------------------------------------------------------------------------------        
    for i in range(len(output_signals)):
        if output_widths[i]=='1':
            file.write(f"\nwire  {output_signals[i]}_tb;")           
        else:
            file.write(f"\nwire  [{output_widths[i]}-1:0]  {output_signals[i]}_tb;")
#-----------------------------------------------------------------------------------        
    for i in range(int(num_tb_parameters)):
            file.write(f"\nparameter {tb_parameters_names[i]}={tb_parameters_values[i]};")  
            
#----------------------------------------------------------------------------------------  
    
    file.write(f"\n{module_name} uut (")
    
    if (design_type=='2' or design_type=='0'):
       
        file.write("\n.clk(clk),")
        if  len(output_signals)==0 and len(input_signals)==0 :           
            file.write("\n.rst(rst)")
        else:
            file.write("\n.rst(rst),")
                       
    for i in range(len(input_signals)):
        if len(output_signals)==0:
            if (i<len(input_signals)-1) :
                file.write(f"\n.{input_signals[i]}({input_signals[i]}_tb),")                
            else:
                file.write(f"\n.{input_signals[i]}({input_signals[i]}_tb)")                       
        else:
            file.write(f"\n.{input_signals[i]}({input_signals[i]}_tb),")
            
    for i in range(len(output_signals)):
        
        if (i<len(output_signals)-1):
            file.write(f"\n.{output_signals[i]}({output_signals[i]}_tb),")
                
        else:
            file.write(f"\n.{output_signals[i]}({output_signals[i]}_tb)")
                      
        
    file.write(");")        

#-------------------------------------the clock generation ----------------------------------------------
    
    if (design_type=='2' or design_type=='0'):
        file.write("\n// Clock generation")
        file.write("\nalways #5 clk = ~clk;")
        
#------------------------------------------the initial block ----------------------------------------
        
    file.write(f"""\ninitial begin\n $dumpfile("{module_name}_tb.vcd");\n $dumpvars(0, {module_name}_tb);\n //Initialize inputs""")
  
    for i in range(len(input_signals)):
        file.write(f"\n{input_signals[i]}_tb={input_widths[i]}'b0\t// Adjust initial values ")
        
    
    for i in range(int(testcases_num)):
        file.write(f"\n#{period}")
        file.write(f"\n//Test case {i+1}")
        for j in range(len(input_signals)):
            max_digit=pow(2,int(input_widths[j]))-1
            
            random_num=int(random.randint(0,max_digit))
                      
            binary=bin(random_num).replace("0b", f"{input_widths[j]}'b")
            file.write(f"\n{input_signals[j]}_tb={binary}      //{random_num}")
            
    
    file.write("\n$finish")
    file.write("\nend")
    file.write("\nendmodule")
    
    
    
  
               
       
