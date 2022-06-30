from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField


app = Flask(__name__)
@app.route("/")
def index():
    return render_template('design.html')


class Patient(Form):
    name = StringField('Patient Name:', [validators.DataRequired()])
    age = StringField('Patient age:', [validators.Length(min=6, max=35)])
    doctor = StringField('doctor:', [validators.Length(min=4, max=25)])
    print ('hello')
    @app.route("/", methods=['GET', 'POST'])
    def hello():
        form = Patient(request.form)

        print
        form.errors
        if request.method == 'POST':
            name = request.form[' Patient name']
            age = request.form['Patient age']
            doctor = request.form['doctor']
            print
            name, " ", age, " ", doctor

        if form.validate():
            # Save the comment here.
            flash('Thanks for registration ' + name)
        else:
            flash('Error: All the form fields are required. ')

        return render_template('design.html', form=form)

if __name__ == "__main__":
    app.run()
    app.debug = True