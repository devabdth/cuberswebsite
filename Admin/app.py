from flask import Flask, render_template, url_for, request, session, redirect
from flask_session import Session
from database.leads import Leads
from database.agents import Agents
import json

app: Flask = Flask('CUBERS_ADMIN')

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

categories: list = [
  "Insurance",
  "Architecture", 
  "Education",
  "Pharmacy",
  "Medical",
  "Brand",
  "Clothing",
  "Cosmatics",
  "Gym"
]

@app.route('/login/', methods=["GET"])
def login():
  if not session.get('currentAgentId') is None:
    return redirect('../')  
  return render_template(
    'login/index.html'
  )

@app.route('/logout/', methods=["GET"])
def logout():
  if not session.get('currentAgentId') is None:
    session.pop('currentAgentId')
    return redirect('/login/')

@app.route('/login/confirmation/', methods=["GET"])
def login_confirmation():
  params = dict(request.values)
  _id = params['id']
  password = params['password']

  agent = Agents().get(_id)
  if agent is None:
    return app.response_class(status=404)
  else:
    if agent['password'] == password:
      session['currentAgentId'] = _id
      return app.response_class(status=200)

    return app.response_class(status=304)

@app.route('/leads/', methods=["GET"])
@app.route('/', methods=["GET"])
def leads_index():
    if session.get('currentAgentId', None) is None:
      return redirect('../login/')
    return render_template(
      'leads/index.html',
      leads= Leads().data,
      categories= categories,
    )

@app.route('/leads/', methods=["POST"])
def leads_post():
  print(session.get('currentAgentId'))
  agent = session.get('currentAgentId', -1)
  body = dict(json.loads(request.data))
  body["category"] = categories.index(body["category"])
  body["agent"] = agent
  res = Leads().add(body)

  if res:
    return app.response_class(status= 201)

  return app.response_class(status= 500)


@app.route('/mailing/', methods=["GET"])
def mailing_index():
  if session.get('currentAgentId', None) is None:
    return redirect('../login/')
  return render_template(
    'mailing/index.html',
    leads= Leads().data,
    categories= categories,
  )


app.run(
  debug= True,
  port= 8888
)
