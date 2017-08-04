from guizero import App,Combo,TextBox,Text,PushButton,info,MenuBar
import csv


def SuccessfulMessage():
    listVar=[BugTitle.get(),Bugdescription.get(), BugType.get(),AssignedTo.get(),assignedBy.get()]
    with open('BugList', 'w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(listVar)
    info("SuccessfulMessage", "Thanks For Submitting Bug")

def file_function():
    print("File option")

def edit_function():
    print("Edit option")
    
app = App(title="Bug Tracker client Saffron", width=300, height=200, layout="grid")

menubar = MenuBar(app,
                  toplevel=["File", "Edit"],
                  options=[
                      [ ["File option 1", file_function], ["File option 2", file_function] ],
                      [ ["Edit option 1", edit_function], ["Edit option 2", edit_function] ]    
                  ])
#Bug title
BugTitle_description = Text(app, text="Bug Title", grid=[0,0], align="left") # adding Description for combo box
BugTitle=TextBox(app , grid=[0,1], align="left")
#Bug Description
Bug_description_1 = Text(app, text="Bug Description", grid=[1,0], align="left") # adding Description for combo box 
Bugdescription=TextBox(app , grid=[1,1], align="left")
#BugType
BugType = Combo(app, options=["Major", "High", "Low"], grid=[2,1], align="left") # adding combo box
Bugtype_description = Text(app, text="BugType", grid=[2,0], align="left") # adding Description for combo box
#Assigned To
AssignedTo = Combo(app, options=["Dev", "Tester", "Client"], grid=[3,1], align="left") # adding combo box
assignedto_description = Text(app, text="Assigned To", grid=[3,0], align="left") # adding Description for combo box
#Assigned By
AssignedByDesc = Text(app, text="Assigned By", grid=[4,0], align="left") # adding Description for combo box 
assignedBy=TextBox(app , grid=[4,1], align="left")
#SubmitButton
update_text = PushButton(app, command=SuccessfulMessage , text="Submit" , grid=[5,1], align="left")

app.display()
    