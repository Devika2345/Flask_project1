from flask import Flask,render_template
FAI=Flask(__name__)
@FAI.route('/stringresponse')
def stringresponse():
    return 'this is string response'
@FAI.route('/htmlresponse')
def htmlresponse():
    return render_template('hii.html',name='Devika',age=22)

FAI.run(debug=True,host='127.0.0.1',port=8000)