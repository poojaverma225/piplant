import csv

#creating an instance of the flask app; is also a direction to flask itself, telling it where my app is 
app = Flask(__name__)

#decorator function; instructions for what happens if someone visits teh website
@app.route('/')
#called when u open the site homepage
def index():
        timestamps = [] #later will be updated by csv file
        values = []
        with open('piplant_data.csv', 'r') as file: #in a read only format, the csv reads lines of data 
                reader = csv.reader(file) 
                for row in reader: #establishes loop that goes through the entire csv 
                        timestamps.append(row[0]) #adds the timestamps of each reading to the x axis of the csv 
                        values.append(float(row[1])) #adds in the actual soil readings; first conversts to a float or number values 
                return render_template('index.html', labels=timestamps[-50:], data=values[-50:]) #renders html template, passing in the last 50 timestamps AND the >
if __name__ == '__main__':  #just a syntaxy thing? Only runs if u run this file manually, not imported 
        app.run(host='0.0.0.0', port=5000) #creates the flask website server @ port 5000!
