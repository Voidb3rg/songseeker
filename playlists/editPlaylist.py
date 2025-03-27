import csv
from csv import DictReader

@app.route("/home")
def home():        
    values_list=[]
    with open("hitster-de.csv", 'r') as f:  #file.csv is name of the csv file
        dict_reader = DictReader(f)
        values_list = list(dict_reader)
    return render_template('home.html', values=values_list)