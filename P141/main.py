from flask import Flask, jsonify, request
import csv
from storage import all_articles, liked_articles, not_liked_articles
from demo_filtering import output
from content_filtering import get_recommendations
all_articles=[]
with open(r"C:\Users\gauri\OneDrive\Desktop\C and P 136\P141\MAIN.csv",encoding="utf-8") as f:
    data=list(csv.reader(f))
    all_articles=data[1:]
liked_articles=[]
not_liked_articles=[]
app=Flask(__name__)
@app.route("/get-article")
def get_article():
    return jsonify({
        "data":all_articles[0],
        "status":"SUCCESS"
    })
@app.route("/liked-article",methods=["POST"])
def liked_articles():
    articles=all_articles[0]
    all_articles=all_articles[1:]
    liked_articles.append(articles)
    return jsonify({
        "status":"SUCCESS"
    }),200
@app.route("/not-liked-article",methods=["POST"])
def not_liked_articles():
    articles=all_articles[0]
    all_articles=all_articles[1:]
    liked_articles.append(articles)
    return jsonify({
        "status":"SUCCESS"
    }),200
@app.route("/recommended-articles")
def recommended_articles():
    all_recommended = []
    for liked_article in liked_articles:
        output = get_recommendations(liked_articles[19])
        for data in output:
            all_recommended.append(data)
    import itertools
    all_recommended.sort()
    all_recommended = list(all_recommended for all_recommended,_ in itertools.groupby(all_recommended))
    article_data = []
    for recommended in all_recommended:
        _d = {
            'url': recommended[12],
            'title' : recommended[13],
            'text' : recommended[14],
            'lang' : recommended[15],
            'total_events' : recommended[16]
        }
        article_data.append(_d)
    return jsonify({
        "data": article_data,
        "status": "success"
    }), 200   
if __name__=="__main__":
    app.run()
