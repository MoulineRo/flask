import flask
from faker import Faker
import statistics
import csv
import requests


app = flask.Flask(__name__)

@app.route("/")
def main():
    return flask.render_template('button.html')


@app.route("/requirements/")
def index():
    req = open('requirements.txt').readlines()
    print(req)
    return flask.render_template('index.html',requirements=req)

@app.route("/users/generate/")
def user():
    fake=Faker()
    name = []
    adress=[]
    result=[]
    for _ in range(10):
        n = fake.name()
        name.append(n)
    for _ in range(10):
        a = fake.address()
        adress.append(a)

    name1=len(name)
    adres1=len(adress)
    if name1 == adres1:
        for n in range(name1):
            res=name[n]+ " - " +adress[n]
            result.append(res)

    return flask.render_template('user.html', new=result)


@app.route("/mean/")
def mean():
    with open('hw.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile)

        file1 = []
        file2 = []
        height = []
        weight = []

        for row in spamreader:
            x = (''.join(row).split(' '))
            file1.append(x[1])
            file2.append(x[2])
        file1.pop(0)
        file2.pop(0)

        for files1 in file1:
            height.append(int(float(files1)))

        for files2 in file2:
            weight.append(int(float(files2)))

        z = str(len(height))+'-People;   '
        x = str(statistics.mean(height))+'-Height;   '
        y = str(statistics.mean(weight))+'-Weight;   '
        res=[z+x+y]
        return flask.render_template('mean.html', mean=res)


@app.route("/space/")
def space():
    r = requests.get('http://api.open-notify.org/astros.json').text
    rr=str(r.count('name')) + '   astronauts in space'
    return flask.render_template('space.html', space=rr)

@app.errorhandler(404)
def page_not_found(error):
    return 'Sorry,page not found',404


if __name__ == "__main__":
    app.run()