import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.toast import ToastNotification
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.validation import add_regex_validation

class App(ttk.Frame):
    def __init__(self,root):
        super().__init__(root,padding=(10,10))
        self.pack(expand=YES,fill=BOTH)
        self.name = ttk.StringVar(value="")
        self.id = ttk.StringVar(value="")
        self.course = ttk.StringVar(value="")
        self.score = ttk.DoubleVar(value=0)
        self.data = []
        self.colors = root.style.colors

        ttk.Label(self,text = "Please enter your contance info : ",width=50).pack(fill=X , pady = 10)

        self.create_from_entry("Name : ",self.name)
        self.create_from_entry("ID : ", self.id)
        self.create_from_entry("Course Name", self.course)
        self.score_input = self.create_from_entry("Final score", self.score)

        self.create_meter()
        self.create_buttonbox()
        self.table = self.create_table()

    def create_from_entry(self,label , variable):
        frame = ttk.Frame(self)
        frame.pack(fill = X ,expand=YES,padx = 10)

        ttk.Label(frame, text=label).pack(side=LEFT,padx = 10 , pady = 5)

        form = ttk.Entry(frame , textvariable=variable )
        form.pack(side=LEFT,padx = 10 ,pady = 5, fill = X , expand=YES )
        return form

    def create_meter(self):
        meter = ttk.Meter(self,metersize=150 , padding=5 , amountused=50,metertype="full",amounttotal=100,subtext="Final score",interactive=True,bootstyle=LIGHT)
        meter.pack()
        self.score.set(meter.amountusedvar)
        self.score_input.configure(textvariable= meter.amountusedvar)

    def create_buttonbox(self):
        frame = ttk.Frame(self)
        frame.pack(fill = X , expand=YES , pady=10)
        ttk.Button(master=frame, text="Cancel", command=self.on_cancel, bootstyle=DANGER).pack(side=RIGHT,padx=5)
        ttk.Button(master=frame, text="Submit", command=self.on_submit, bootstyle=SUCCESS).pack(side=RIGHT,padx=5)
    def on_submit(self):
        name = self.name.get()
        id = self.id.get()
        course = self.course.get()
        score = self.score_input.get()

        toast = ToastNotification(title="Submission succesful",message="your data has been succesfully submitted",duration=1500)
        toast.show_toast()

        self.data.append((name , id , course , score))

        self.table.destroy()
        self.table = self.create_table()

    def on_cancel(self):
        self.quit()

    def create_table(self):
        coldata = [{"text": "Name"}, {"text": "ID" , "stretch" : False}, {"text": "Course"}, {"text": "Score" , "stretch" : False}]

        table = Tableview(self,coldata=coldata,rowdata= self.data,paginated=True,searchable=True,bootstyle=PRIMARY , stripecolor=(self.colors.light ,  None))
        table.pack(fill = BOTH , expand=YES , pady=10 , padx=10 )
        return table


if "__main__" == __name__:
    app = ttk.Window(themename="darkly")
    App(app)
    app.mainloop()
