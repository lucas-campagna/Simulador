from flask import Flask, render_template, url_for, session, request, make_response
import os

app = Flask(__name__)

tempoDeProva = 4*60*60*1000 # ms

@app.route('/')
def index():
	resp = make_response(render_template('index.html'))
	resp.set_cookie('fazendoProva','false')
	return resp

@app.route('/login', methods=['POST'])
def login():
	username = request.form['username']
	if username == 'admin':
		# passwrd = request.form['passwrd']
		return render_template('admin.html',username=username)

	provas = dict(request.form).pop('username')
	return render_template('login.html',username=username)

@app.route('/prova')
def prova():
	img=''
	options = ['a','b','c','d']
	resp = make_response(render_template('questao.html',image=img,options=options))
	resp.set_cookie('fazendoProva','true')
	return resp

@app.route('/fimDeProva')
def fimDeProva():
	pass

@app.route('/<string:prova>/<string:ano>/<string:n>')
def questao(prova,ano,n):
	options = ['a','b','c','d']
	img='/static/imgs/Provas_Concursos_Militares/'+prova+'/'+ano+'/'+n+'.png'
	return '<img src="'+img+'" >'






if __name__ == '__main__':
	app.run(debug=True,host='192.168.29.5',port=5000)
	pass




# Requests

@app.route('/parametros/tempoDeProva')
def temporDeProva():
	return str(tempoDeProva);


# UTILS

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)