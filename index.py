from newspaper import Article
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
    score = txt.sentiment.subjectivity*100
    int_score = int(score)
    if int_score >= 45 and int_score<60:
        return f"subjectivity score: {int_score}/100 | slightly biased"
    elif int_score >= 60 and int_score<80:
        return f"subjectivity score: {int_score}/100 | biased"
    elif int_score >= 80:
        return f"subjectivity score: {int_score}/100 | highly biased"
    else:
        return f"subjectivity score: {int_score}/100 | unbiased"





if __name__ == "__main__":
    app.run( debug = True)