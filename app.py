from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        if name == "":
            return "Error: Name required"
        return "Hello " + name
    else:
        return '''
            <form method="post">
                Name: <input type="text" name="name">
                <input type="submit" value="Submit">
            </form>
        '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

