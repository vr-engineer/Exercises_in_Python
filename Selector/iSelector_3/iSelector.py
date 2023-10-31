#!/usr/bin/python

########################################################################
#
#       File:           iSelector.py
#       Purpose:        Selecting automatic tests and setting
#                       their number of iterations.
#
#       Authors:        Victor Rivero Diez
#
#       Updates:
#
########################################################################

# --- Libraries
import re
import os
from sys import exit
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


# --- Variables
path_file_steps_source = 'extracted_steps.csv'
path_file_steps_selection = 'seleccion_test.csv'
path_file_iters_template = 'Q_ITERATIONS-body.1.0.tcl'


re.purge()                                                                          #To clean regular expressions cache.
regex_TCL = re.compile(r"^.*[^0-9]_([0-9]+)_([0-9]+).*STEP_([0-9]+)\-.*$", re.I)    #Regular expression to match with TCL tests.    
regex_RF = re.compile(r"^.*[^0-9]_([0-9]+)_([0-9]+).*STEP_([0-9]+)_.*$", re.I)      #Regular expression to match with RobotFramework tests.                                                                          
regex_No_Number = re.compile(r"^.*\sSTEP_([A-Za-z_]*)-[A-Za-z_]*;\d\D\d$", re.I)    #Regular expression to match with tests without number. For example: RANGE_AND_BEARING
regex_iter = re.compile(r'(?<=\s")\d{1,}(?=")')                                     #To get number of iterations from iterations file.



# --- Classes
class StopSave(Exception):
    #We create an ad hoc class for an exception.
    pass

class Test:                                                                 #Each test is an object made out of this class 
    def __init__(self,suite,case,skip,group,category,number):
        self.suite = suite
        self.case = case
        self.skip = skip
        self.group = group
        self.category = category
        self.number = number
        self._ID_ = self.group + '.' + self.category + '.' + self.number    #To create an id to seak each test in iterations file.
        self.samples = self.read_iterations()
        self.tk_skip = ''
        self.tk_iter = ''
        self.tk_widget_field = ''
        self.tk_widget_check = ''
        
    def read_iterations(self):                                                          
        file_iters_template = open(path_file_iters_template, 'r', encoding='utf-8')
        for l in file_iters_template:
            if self._ID_ in l:
                num_iter = re.search(regex_iter,l).group()
                file_iters_template.close()
                return num_iter     #Loop finishes when it gets a match.              

        return '0'  #If there is not any match, it means that the test does not exist in iterations file. So, it shows 0 by default.


class Window(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
       
        self.parent = parent
        self.picture=PhotoImage(file='AUTOMATION.png')

        # ++++ + Creation of containers +
        self.frame_common_setter = ttk.Frame(self, padding = (2,10,2,10))   #Frame for setting a common number of iterations.
        self.frame_browser = ttk.Frame(self, padding = (2,10,2,10))         #Frame for browser section.    
        self.canvas = Canvas(self)                                          #Canvas is chosen as scrollable object.
        self.table = Frame(self.canvas)                                     #A Frame is held in a Canvas. That Frame holds widgets.
        self.scroll_H = Scrollbar(self)                                     #A horizontal scroll
        self.scroll_V = Scrollbar(self)                                     #A vertical scroll
        self.frame_buttons = Frame(self)                                    #A Frame to locate buttons.
        # ++++ - Creation of containers -

        # ++++ + Configuration of containers +
        self.canvas.config(xscrollcommand = self.scroll_H.set, yscrollcommand = self.scroll_V.set, highlightthickness = 0)
            #xscrollcommand -> To connect a canvas to a horizontal scrollbar.
            #yscrollcommand -> To connect a canvas to a vertical scrollbar.
            #highlightthickness -> width of the highlight border = 0 pixels.
        self.scroll_H.config(orient = HORIZONTAL, command = self.canvas.xview)
        self.scroll_V.config(orient = VERTICAL, command = self.canvas.yview)
            #command -> A callback to update the associated widget.
            #xview and yview -> Adjust the canvas view.
        # ++++ - Configuration of containers -

        # ++++ + Managment of containers +
        self.frame_common_setter.pack()
        ttk.Separator(self, orient = "horizontal").pack(fill = "x")           #To add a horizontal line
        self.frame_browser.pack()
        self.frame_buttons.pack(side = BOTTOM)
        self.scroll_H.pack(fill = X, side = BOTTOM, expand = FALSE)
        self.scroll_V.pack(fill = Y, side = RIGHT, expand = FALSE)
        self.canvas.pack(fill = BOTH, side=LEFT, expand = TRUE)
        self.canvas.create_window(0, 0, window = self.table, anchor = NW)
            #canvas.create_window -> It creates a canvas-window object that allows to place more than one tkinter widget on the canvas.
            # 0, 0  -> To set canvas-window position (two coordinates (x,y)).
            #window -> To set widget you want to place onto the canvas. (the Frame called table).
            #anchor -> Where to place the widget relative to the given position. (North West)
        # ++++ - Managment of containers -

        # ++++ + Common iterations-setter section +
        self.n_iter = StringVar()
        ttk.Label(self.frame_common_setter, text = "Number of iterations: ").grid(row = 0,column = 0)
        ttk.Spinbox(self.frame_common_setter, textvariable = self.n_iter, from_ = 0, to = 300, width = 10).grid(row = 0,column = 1)
        ttk.Label(self.frame_common_setter, image = self.picture).grid(row = 0,column = 2)
        ttk.Button(self.frame_common_setter, text = "Set", command = self.On_Set_Button).grid(row = 0,column = 3)
        # ++++ - Common iterations-setter section -

        # ++++ + Browser section +
        self.test_to_search = StringVar()
        ttk.Label(self.frame_browser, text = "Test: ").grid(row = 0, column = 0)
        ttk.Entry(self.frame_browser, textvariable = self.test_to_search, width = 50).grid(row = 0, column = 1)
        ttk.Button(self.frame_browser, text = "Search", command = self.buscar).grid(row = 0, column = 2)
        # ++++ - Browser section -

        # ++++ + Buttons section +
        self.feedback = StringVar()
        ttk.Label(self.frame_buttons, textvariable = f"{self.feedback}").grid(row = 0,column = 0, ipadx = 20)
        ttk.Button(self.frame_buttons, text = "Select all", command = self.On_Select_All_Button).grid(row = 0,column = 1)       
        ttk.Button(self.frame_buttons, text = "Unselect all", command = self.On_Unselect_All_Button).grid(row = 0,column = 2)   
        ttk.Button(self.frame_buttons, text = "Save & Close", command = self.On_Save_And_Close).grid(row = 0,column = 3)                         
        ttk.Button(self.frame_buttons, text = "Exit", command = self.destroy).grid(row = 0,column = 4)
        # ++++ - Buttons section -


        # ++++ + To init +
        f = 0       #Row 0
        cat = 'x'   #To have a different category for sure.

        for ob in M:

            self.control_skip = StringVar(value = ob.skip)      #Control variable for checkbutton.
            ob.tk_skip = self.control_skip
            self.control_iter = StringVar()                     #Control variable for number of iterations.
            ob.tk_iter = self.control_iter

            if cat != ob.category:                              #Si objct.category es diferente a la categoría anterior, se imprime la Label con grupo y categoría
                ttk.Label(self.table, text = f' GROUP: {ob.group} - CATEGORY: {ob.category} ', relief=SUNKEN, font=("Helvetica", 11, "bold")).grid(row=f, column=1, sticky='W')
                f += 1
                cat = ob.category
        
            self.field_iter = ttk.Spinbox(self.table, textvariable = self.control_iter, from_ = 0, to = 300, width = 7)
            ob.tk_widget_field = self.field_iter                                                                    #Asigno el widget al atributo de la clase Test
            ob.tk_widget_field.grid(row = f, column = 0, padx = (10,10))
            ob.tk_widget_field.insert(END, ob.samples)                                                              #para ver texto por defecto
                
                
            self.check_widget = ttk.Checkbutton(self.table, text = ob.case, variable = self.control_skip, onvalue = '0', offvalue = '1')
            ob.tk_widget_check = self.check_widget
            ob.tk_widget_check.grid(row = f, column = 1, sticky = 'W')

            f+=1

            self.canvas.update_idletasks()                              # nos permite actualizar el scroll al ir rellenando los widgets
            self.canvas.config(scrollregion = self.table.bbox())    
                
        # ++++ - To init -

    def buscar(self):
        if self.test_to_search.get() != '':
            print("Searching...")
            self.feedback.set("Searching...")
            for ob in M:
                #If there is match, widget is retrieved/shown
                if (self.test_to_search.get() in ob.case) or (self.test_to_search.get() in ob._ID_): #It
                    
                    ob.tk_widget_check.grid()
                    ob.tk_widget_field.grid()

                else:
                    #If there is not match, widget is hidden
                    ob.tk_widget_check.grid_remove()
                    ob.tk_widget_field.grid_remove()

            print("Search done")
            self.feedback.set("Search done")

        else:
            print("Restoring list...")
            self.feedback.set("Restoring list...")
            for ob in M:
                
                ob.tk_widget_check.grid()
                ob.tk_widget_field.grid()
            
            print("List restored")    
            self.feedback.set("List restored")


    def On_Unselect_All_Button(self):
        for ob in M:
            ob.tk_skip.set('1')

        print("All were unselected")
        self.feedback.set("ALL UNSELECTED")


    def On_Select_All_Button(self):
        for ob in M:
            ob.tk_skip.set('0')

        print("All were selected")
        self.feedback.set('ALL SELECTED')


    def check_data_input(self, data):
        for i in data:
           if i not in '0123456789':
               return False

        if int(data) > 600:
            return False
    
        return True


    def On_Set_Button(self):

        if self.check_data_input(self.n_iter.get()):
            for ob in M:
                ob.tk_iter.set(self.n_iter.get())

            print(f'[{self.n_iter.get()}] iter(s) set for all')
            self.feedback.set("SET")
        
        else:
            print(f'[{self.n_iter.get()}] wrong value')
            self.feedback.set("ERROR")


    def On_Save_And_Close(self):

        ########## + Saving selection +
        c = 0 #Contador
        
        try:
            
            for ob in M:
                if ob.tk_skip.get() == '0':
                    c+=1

            if messagebox.askokcancel(message=f"{c} selected"):
                pass
            
            else:
                
                raise StopSave()

        except:
            
            pass

        else:           
            
            print("Saving selection ...")
            self.feedback.set("Saving selection ...")
            file_steps_selection = open(path_file_steps_selection, 'w', encoding = 'utf-8')
            file_steps_selection.write('#CASE_FILE;STEP_NAME;SKIP_FLAG;NONCRITICAL_FLAG;\n')        #First line to write in file

            for ob in M:

                ob.skip = ob.tk_skip.get()  #To get the value from iteration field.
                file_steps_selection.write(ob.suite + ';' + ob.case + ';' + ob.skip + ';1\n')

            file_steps_selection.close()
        ########## - Saving selection -

        
            ########## + Saving iterations +

            try:
                #Let's check if any iteration was set wrongly. For that, I've a ad hoc exception.
                for ob in M:
                    if self.check_data_input(ob.tk_iter.get()):
                        #If it is ok, nothing is done.
                        pass
                    else:
                        #If some data is not an int (a wrong data), an exception is raised.
                        print(f"[{ob.tk_iter.get()}] wrong value for {ob._ID_}")
                        self.feedback.set("ERROR")
                        raise StopSave()
                        break
                    
            except:
                #There was an exception so new data is not save and GUI remains opened.
                pass
            
            else:
                #There was not an exception so new data is taken from GUI insterface and it is saved.
                print("Saving iterations ...")
                self.feedback.set("Saving iterations ...")
                file_iters_selection=open(path_file_iters_template,'w', encoding='utf-8')
                file_iters_selection.write('{0}\n{1}{2}\n\n'.format("module_body Q_ITERATIONS 1.0 implementation {\n",
                                                                    "# TEST.CASE.STEP		NUMBER OF ITERATIONS\n",
                                                                    "#----------------------------------------------------------------------------\n"))

                before_test = 'x' #To avoid duplicates IDs in iterations file.
                for ob in M:
                    if before_test != ob._ID_:
                        #We have already checked that all data are correct so it is not necessary a second validation.
                        ob.samples = ob.tk_iter.get()
                        file_iters_selection.write(f"    dict set v_iterations  \"{ob._ID_}\" \"{ob.samples}\"\n")
                        before_test = ob._ID_
                        

                file_iters_selection.write("{0}{1}\n{2}{3}{4}{5}\n{6}{7}{8}{9}{10}\n{11}{12}".format("#----------------------------------------------------------------------------\n",
                                                                                                     "#----------------------------------------------------------------------------\n",
                                                                                                     "\tproc_body Get_Num_Iterations {key} {\n",
                                                                                                     "\t\tvariable v_iterations\n",
                                                                                                     "\t\treturn [dict get $v_iterations $key]\n",
                                                                                                     "\t}\n",
                                                                                                     "\t#proc_body Get_Possible_Iterations {key} {\n",
                                                                                                     "\t\t# variable v_possible_iterations\n",
                                                                                                     "\t\t# return [dict get $v_possible_iterations $key]\n",
                                                                                                     "\t\t# Changed for iCAS\n",
                                                                                                     "\t#return \"0\"\n",
                                                                                                     "\t#}\n",
                                                                                                     "}\n"))


                self.destroy()  #To close GUI_Selector.

        ########## - Saving iterations -


# --- Functions    
def generate_data_matrix ():

    file_steps_source = open(path_file_steps_source, 'r', encoding='utf-8')
    data_matrix = []
    
    for line in file_steps_source:
        line = line.rstrip('\n')
        if not line.startswith('#'):

            step_suite = line.split(';')[0]   
            step_case = line.split(';')[1]
            step_skip = line.split(';')[2]

            if test := re.match(regex_RF,line):

                step_group = test.group(1)
                step_category = test.group(2)
                step_number = test.group(3)
                data_matrix.append(Test(step_suite,step_case,step_skip,step_group,step_category,step_number))

            elif test := re.match(regex_TCL,line):

                step_group = test.group(1)
                step_category = test.group(2)
                step_number = test.group(3)
                data_matrix.append(Test(step_suite,step_case,step_skip,step_group,step_category,step_number))

            elif test := re.match(regex_No_Number,line):
            
                step_group = 'NO_GROUP'
                step_category = 'NO_CATEGORY'
                step_number = test.group(1)
                data_matrix.append(Test(step_suite,step_case,step_skip,step_group,step_category,step_number))

            else:
                #If there is not any match, nothing is done.
                pass
                         
    file_steps_source.close()
    return data_matrix


# --- Body
if __name__ == "__main__":

    if os.path.exists(path_file_steps_source) and os.path.exists(path_file_iters_template):
    
        M = generate_data_matrix()          #To create the data matrix (list of Test-class objects). Global variable.
        GUI_Selector = Window(None)         #To create a Window-class object.
        GUI_Selector.title('SELECTOR')
        GUI_Selector.geometry('800x600')
        GUI_Selector.resizable(True, True)
        GUI_Selector.mainloop()
        exit()  #To finish python script

    else:
        print(f"\nERROR, {path_file_steps_source} or {path_file_iters_template} does not exist\n")
        exit()  #To finish python script


