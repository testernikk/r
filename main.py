from guizero import App,Combo,TextBox,Text,PushButton
app = App(title="Bug Tracker client Saffron", width=300, height=200, layout="grid")
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
update_text = PushButton(app, command=0 , text="Submit" , grid=[5,0], align="left")

app.display()
