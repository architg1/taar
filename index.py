from textblob import TextBlob
from flask import Flask, render_template
from flask import request

app=Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about-us')
def us():
    return render_template('about-us.html')

@app.route('/about-taar')
def taar():
    return render_template('about-taar.html')

@app.route('/analysis', methods=['POST'])


def content():
    data = request.form['projectFilepath']
    txt = TextBlob(data)
    score = 0
    for sentence in txt.sentences:

        sentence_score = sentence.sentiment.subjectivity
        if sentence_score == 0:
            score = score + 0
        else:
            score = score + sentence_score
    score = score/len(txt.sentences)
    score = score*100
    int_score = int(score)

    return render_template('analysis.html',score = int_score)





if __name__ == "__main__":
    app.run(debug=True)
