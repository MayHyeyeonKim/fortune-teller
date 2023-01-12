from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return 'About this app'


@app.route('/result222')
def user_info(username):
    return render_template('result.html',
                           users=[
                               {
                                   "name": "Sara",
                                   "color": "red",
                                   "number": "1"
                               },
                               {},
                               {},
                           ])


@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        userName = request.form['userName']
        color = request.form['color']
        number = request.form['number']
        print(userName)
        print(color)
        print(number)
        return render_template('result.html',
                           user={
                                   "name": userName,
                                   "color": color,
                                   "number": number,
                                   "colors":[{"key":"red","value":"빨간"},
                                             {"key":"green","value":"푸른"},
                                             {"key":"blue","value":"파란"},
                                             {"key":"yellow","value":"노란"}
                                            ],
                                   "numbers": [{"key":"1","value":"하루"},
                                               {"key":"2","value":"사과"},
                                               {"key":"3","value":"바나나"},
                                               {"key":"4","value":"키위"},
                                               {"key":"5","value":"자몽"}]
                            
                               }
                           )
    else:
        return "Handle GET request"
  

app.run(host='0.0.0.0', port=81)
