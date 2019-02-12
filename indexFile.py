#kiankai
from flask import Flask, render_template, request, url_for, flash, redirect
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        sqrFeet= request.form.get('SquareFeet')
        size=  request.form.get('size')
        bed =   request.form.get('bed')
        bath =   request.form.get('bath')
        rooms = request.form.get('rooms')
        price = 400*int(sqrFeet)+100*int(size)+40000*int(bed)+100000*int(rooms)+50000*int(bath)
        return render_template("home.html",price=price,sqrFeet=sqrFeet,size=size,bed=bed,bath=bath,rooms=rooms)
    sqrFeet= 0
    size=  0
    bed =  0
    bath =  0
    rooms = 0
    return render_template("home.html",sqrFeet=sqrFeet,size=size,bed=bed,bath=bath,rooms=rooms)





if __name__ == '__main__':
    app.run(debug=True)
