import clear

clr.AddReference('System.Windows.Forms')

from System.Windows.Forms import Application, Form

class HelloWorldForm(Form):
    def __init__(self):
        self.Text = 'Hello'
        self.Name = 'HOLI'
        
if __name__ == "__main__":
    
    form = HelloWorldForm()
    Application.Run(form)