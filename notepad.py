import tkinter as tk
from tkinter import ttk
from tkinter import messagebox,filedialog,font,colorchooser
import os
main_application=tk.Tk()
main_application.geometry('1000x500')
main_application.title('Note Pad')
# main_application.wm_iconbitmap()
# ***********************************++++++++++++++++       Main menu        ++++++++++++++***************************************
# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&***************           End        ******************&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
main_menu=tk.Menu()
# ==============file data==============
# ****File icons*****
new_icon=tk.PhotoImage(file=r"icons2/new.png")
open_icon=tk.PhotoImage(file=r"icons2/open.png")
save_icon=tk.PhotoImage(file=r"icons2/save.png")
save_as_icon=tk.PhotoImage(file=r"icons2/save_as.png")
exist_icon=tk.PhotoImage(file=r"icons2/exit.png")
# *************************************
file=tk.Menu(main_menu,tearoff=False)
# *************************************
# ==============Edit data==============
# ****Edit icons*****
copy_icon=tk.PhotoImage(file=r"icons2/copy.png")
paste_icon=tk.PhotoImage(file=r"icons2/paste.png")
cut_icon=tk.PhotoImage(file=r"icons2/cut.png")
clear_icon=tk.PhotoImage(file=r"icons2/clear_all.png")
find_icon=tk.PhotoImage(file=r"icons2/find.png")
# *************************************
Edit=tk.Menu(main_menu,tearoff=False)
# *************************************
# ==============View data==============
# ****View icons*****
toolbar_icon=tk.PhotoImage(file=r"icons2/tool_bar.png")
statusbar_icon=tk.PhotoImage(file=r"icons2/status_bar.png")
# *************************************
View=tk.Menu(main_menu,tearoff=False)
# *************************************
# ==============Theme data==============
# ****Theme icons*****
light_default_icon=tk.PhotoImage(file=r"icons2/light_default.png")
light_plus_icon=tk.PhotoImage(file=r"icons2/light_plus.png")
dark_icon=tk.PhotoImage(file=r"icons2/dark.png")
red_icon=tk.PhotoImage(file=r"icons2/red.png")
monokai_icon=tk.PhotoImage(file=r"icons2/monokai.png")
night_blue_icon=tk.PhotoImage(file=r"icons2/night_blue.png")
# *************************************
Theme=tk.Menu(main_menu,tearoff=False)
# *************************************
Theme_choice=tk.StringVar()
color_icons=(light_default_icon,light_plus_icon,dark_icon,red_icon,monokai_icon,night_blue_icon)
color_dict={
    'light default':('#000000','#ffffff'),
    'light plus':('#474747','#e0e0e0'),
    'dark':('#c4c4c4','#2d2d2d'),
    'red':('#2d2d2d','#ffe8e8'),
    'monokai':('#d3b774','#474747'),
    'night blue':('#ededed','#6b9dc2')    
}

#cascade
main_menu.add_cascade(label='File',menu=file)
main_menu.add_cascade(label='Edit',menu=Edit)
main_menu.add_cascade(label='View',menu=View)
main_menu.add_cascade(label='Theme',menu=Theme)

# ***********************************++++++++++++++++   Tool bar   ++++++++++++++***************************************
tool_bar=ttk.Label(main_application)
tool_bar.pack(side=tk.TOP,fill=tk.X)
# ******font langangues************
font_tuple=tk.font.families()
font_family=tk.StringVar()
font_box=ttk.Combobox(tool_bar,width=30,textvariable=font_family,state='readonly')
font_box['values']=font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row=0,column=0,padx=5)
# ******font Size************
font_size=tk.IntVar()
font_size=ttk.Combobox(tool_bar,width=14,textvariable=font_size,state='readonly')
font_size['values']=tuple(range(12,80,2))
font_size.current(0)
font_size.grid(row=0,column=1,padx=5)
#***********buttons**********
#bold
Bold_icon=tk.PhotoImage(file=r"icons2/bold.png")
bold_button=ttk.Button(tool_bar,image=Bold_icon)
bold_button.grid(row=0,column=2,padx=5)
#italic
italic_icon=tk.PhotoImage(file=r"icons2/italic.png")
italic_button=ttk.Button(tool_bar,image=italic_icon)
italic_button.grid(row=0,column=3,padx=5)
#underline
underline_icon=tk.PhotoImage(file=r"icons2/underline.png")
underline_button=ttk.Button(tool_bar,image=underline_icon)
underline_button.grid(row=0,column=4,padx=5)
#color selection
color_select_icon=tk.PhotoImage(file=r"icons2/font_color.png")
color_button=ttk.Button(tool_bar,image=color_select_icon)
color_button.grid(row=0,column=5,padx=5)
#align left
A_left_icon=tk.PhotoImage(file=r"icons2/align_left.png")
A_left_button=ttk.Button(tool_bar,image=A_left_icon)
A_left_button.grid(row=0,column=6,padx=5)
#align Center
A_center_icon=tk.PhotoImage(file=r"icons2/align_center.png")
A_center_button=ttk.Button(tool_bar,image=A_center_icon)
A_center_button.grid(row=0,column=7,padx=5)
#align right
A_right_icon=tk.PhotoImage(file=r"icons2/align_right.png")
A_right_button=ttk.Button(tool_bar,image=A_right_icon)
A_right_button.grid(row=0,column=8,padx=5)





# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&***************       End      ******************&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&


# ***********************************++++++++++++++++    Text editor    ++++++++++++++***************************************
text_editor=tk.Text(main_application)
text_editor.config(wrap='word',relief=tk.FLAT)
scroll_bar=tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.pack(fill=tk.BOTH,expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)
#@@@@@@@@@@@@@@@@@@@@@@@@@Font family and Font size functinality@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
current_font_family='Arial'
current_font_size=12
def change_font(main_application):
    global current_font_family
    current_font_family=font_family.get()
    text_editor.configure(font=(current_font_family,current_font_size))
def change_fontsize(main_application):
    global current_font_size
    current_font_size=font_size.get()
    text_editor.configure(font=(current_font_family,current_font_size))
font_box.bind('<<ComboboxSelected>>',change_font)
font_size.bind('<<ComboboxSelected>>',change_fontsize)
# @@@@@@@@@@@@@@@@@@@@@@@Button Functionality@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# Bold  button function
def change_bold():    
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight']=='normal':
        text_editor.configure(font=(current_font_family,current_font_size,'bold'))
    if text_property.actual()['weight']=='bold':
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))
# italic  button function
def change_italic():    
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant']=='roman':
        text_editor.configure(font=(current_font_family,current_font_size,'italic'))
    if text_property.actual()['slant']=='italic':
        text_editor.configure(font=(current_font_family,current_font_size,'roman'))
# underline  button function
def change_underline():    
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline']==0:
        text_editor.configure(font=(current_font_family,current_font_size,'underline'))
    if text_property.actual()['underline']==1:
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))
# colour  button function
def change_font_color():
    color_var=tk.colorchooser.askcolor()
    print(color_var)
    text_editor.configure(fg=color_var[1])
#left align button
def align_left():
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config('left',justify=tk.LEFT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT, text_content,'left')

#center align button
def align_center():
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config('center',justify=tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT, text_content,'center')

#right align button
def align_right():
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config('right',justify=tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT, text_content,'right')


#&&&&&&&&&&&&*********commands*******&&&&&&&&&&&&&
A_right_button.configure(command=align_right)
A_center_button.configure(command=align_center) 
A_left_button.configure(command=align_left)
color_button.configure(command=change_font_color)
underline_button.configure(command=change_underline)
italic_button.configure(command=change_italic)
bold_button.configure(command=change_bold)
text_editor.configure(font=('Arial',12))

# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&***************         End      ******************&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&


# ***********************************++++++++++++++++     Main status bar    ++++++++++++++***************************************
status_bar=ttk.Label(main_application,text='words')
status_bar.pack(side=tk.BOTTOM)
text_changed=False
def changed(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed=True
        words=len(text_editor.get(1.0,'end-1c').split())
        char=len(text_editor.get(1.0,'end-1c').replace(' ', ''))
        status_bar.config(text=f'Characters:{char} words:{words}')
    text_editor.edit_modified(False)
text_editor.bind('<<Modified>>',changed)
# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&***************           End        ******************&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&



# ***********************************++++++++++++++++    Main menu funtionality    ++++++++++++++***************************************
#########new file functinality#########
url=''
def new_file(event=None):
    global url
    url=''
    text_editor.delete(1.0,tk.END)

# *** new file command****
file.add_command(label='New',image=new_icon,compound=tk.LEFT,accelerator='Ctrl+N',command=new_file)
#########Open file functinality#########
url=''
def open_file(event=None):
    global url
    url=filedialog.askopenfilename(initialdir=os.getcwd(),title='Select File',filetypes=(('Text File','*.txt'),('All Files','*.*')))
    try:
        with open(url,'r') as fr:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0, fr.read())
    except FileNotFoundError:
        return
    except:
        return
    main_application.title(os.path.basename(url))
# *** open file command****
file.add_command(label='Open',image=open_icon,compound=tk.LEFT,accelerator='Ctrl+O',command=open_file)
#########Save  file functinality#########
def save_file(event=None):
    global url
    try:
        if url:
            content=str(text_editor.get(1.0,tk.END))
            with open(url,'w',encoding='utf-8') as fw:
                fw.write(content)
        else:
            url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All Files','*.*')))
            content2=text_editor.get(1.0,tk.END)
            url.write(content2)
            url.close()
    except:
        return      
# *** save file command****
file.add_command(label='Save',image=save_icon,compound=tk.LEFT,accelerator='Ctrl+S',command=save_file)  
#########Save as  file functinality#########
def save_as_file(event=None):
    global url
    try:
        url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All Files','*.*')))
        content2=text_editor.get(1.0,tk.END)
        url.write(content2)
        url.close()
    except:
        return  
# *** save as file command****
file.add_command(label='Save As',image=save_as_icon,compound=tk.LEFT,accelerator='Ctrl+Alt+S',command=save_as_file)
#########Exist file functinality#########
def exist_func(event=None):
    global url,text_changed
    try:
        if text_changed:
            mbox=messagebox.askyesnocancel('warning','Do you want to save the file')
            if mbox is True:
                if url:
                    content=text_editor.get(1.0,tk.END)
                    with open(url,'w',encoding='utf-8') as fw:
                        fw.write(content)
                        main_application.destroy()
                else:
                    content2=text_editor.get(1.0,tk.END)
                    url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All Files','*.*')))
                    url.write(content2)
                    url.close()
                    main_application.destroy()
            elif mbox is False:
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        return
# *** exist file command****
file.add_command(label='Exist',image=exist_icon,compound=tk.LEFT,accelerator='Ctrl+Q',command=exist_func)
# ***Edit command****
Edit.add_command(label='Copy',image=copy_icon,compound=tk.LEFT,accelerator='Ctrl+C',command=lambda:text_editor.event_generate('<Control c>'))
Edit.add_command(label='Paste',image=cut_icon,compound=tk.LEFT,accelerator='Ctrl+V',command=lambda:text_editor.event_generate('<Control v>'))
Edit.add_command(label='Cut',image=paste_icon,compound=tk.LEFT,accelerator='Ctrl+X',command=lambda:text_editor.event_generate('<Control x>'))
Edit.add_command(label='Clear All',image=clear_icon,compound=tk.LEFT,accelerator='Ctrl+Alt+C',command=lambda:text_editor.delete(1.0,tk.END))
# ************find functionality************
def find_func(event=None):
    def find():
        word=find_input.get()
        text_editor.tag_remove('match','1.0',tk.END)
        matches=0
        if word:
            start_pos='1.0'
            while True:
                start_pos=text_editor.search(word,start_pos,stopindex=tk.END)
                if not start_pos:
                    break
                end_pos=f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match',start_pos,end_pos)
                matches+=1
                start_pos=end_pos
                text_editor.tag_config('match',foreground='red',background='yellow')

    def replace():
            word=find_input.get()
            replace_text=replace_input.get()
            content=text_editor.get(1.0,tk.END)
            new_content=content.replace(word, replace_text)
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0, new_content)
    find_dialogy=tk.Toplevel()
    find_dialogy.geometry('350x150+500+200')
    find_dialogy.title('Find')
    find_dialogy.resizable(0,0)
    #frame
    find_frame=ttk.Labelframe(find_dialogy,text='Find/Replace')
    find_frame.pack(pady=20)
    #labels
    text_find_label=ttk.Label(find_frame,text='Find')
    text_replace_label=ttk.Label(find_frame,text='Replace')
    #entry
    find_input=ttk.Entry(find_frame,width=30)
    replace_input=ttk.Entry(find_frame,width=30)
    #button
    find_button=ttk.Button(find_frame,text='Find',command=find)
    replace_button=ttk.Button(find_frame,text='Replace',command=replace)
    #label Grid
    text_find_label.grid(row=0,column=0,padx=4,pady=4)
    text_replace_label.grid(row=1,column=0,padx=4,pady=4)
    #entry grid
    find_input.grid(row=0,column=1,padx=4,pady=4)
    replace_input.grid(row=1,column=1,padx=4,pady=4)
    #button grid
    find_button.grid(row=2,column=0,padx=8,pady=4)
    replace_button.grid(row=2,column=1,padx=8,pady=4)

    find_dialogy.mainloop()
# *** find  command****
Edit.add_command(label='Find',image=find_icon,compound=tk.LEFT,accelerator='Ctrl+F',command=find_func)
# ***View cheakbutton****
show_tool_bar=tk.BooleanVar()
show_tool_bar.set(True)
show_status_bar=tk.BooleanVar()
show_status_bar.set(True)
def hide_tool_bar():
    global show_tool_bar
    if show_tool_bar:
        tool_bar.pack_forget()
        show_tool_bar=False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP,fill=tk.X)
        text_editor.pack(fill=tk.BOTH,expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_tool_bar=True
def hide_status_bar():
    global show_status_bar
    if show_status_bar:
        status_bar.pack_forget()
        show_status_bar=False
    else:
        status_bar.pack(side=tk.BOTTOM)
        show_status_bar=True 

View.add_checkbutton(label='Toolbar',onvalue=True,offvalue=0,variable=show_tool_bar,image=toolbar_icon,compound=tk.LEFT,command=hide_tool_bar)
View.add_checkbutton(label='Status Bar',onvalue=True,offvalue=0,variable=show_status_bar,image=statusbar_icon,compound=tk.LEFT,command=hide_status_bar)
# ***Theme command****
def change_theme():
    chosen_theme=Theme_choice.get()
    color_tuple=color_dict.get(chosen_theme)
    fg_color,bg_color=color_tuple[0],color_tuple[1]
    text_editor.config(background=bg_color,fg=fg_color)
count=0
for i in color_dict:
    Theme.add_radiobutton(label=i,image=color_icons[count],variable=Theme_choice,compound=tk.LEFT,command=change_theme)
    count+=1

# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&***************           End     ******************&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
main_application.config(menu=main_menu)
# @@@@@@@@@@@@@@@@@@@@@@@Shortcut keys@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
main_application.bind('<Control-n>',new_file)
main_application.bind('<Control-o>',open_file)
main_application.bind('<Control-s>',save_file)
main_application.bind('<Control-Alt-s>',save_as_file)
main_application.bind('<Control-q>',exist_func)
main_application.bind('<Control-f>',find_func)
main_application.mainloop()