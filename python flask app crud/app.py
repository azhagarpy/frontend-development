from flask import Flask,request,redirect, url_for,render_template
import sqlite3
app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def index():
	con=sqlite3.connect("courses")
	con.row_factory=sqlite3.Row
	cur=con.cursor()
	cur.execute("SELECT * FROM dept_tbl")
	data=cur.fetchall()
	return render_template('index.html',data=data)

@app.route('/add_dept',methods=['POST','GET'])
def add_dept():
	if request.method=='POST':
		deptname=request.form.get('deptname')
		deptcode=request.form.get('deptcode')
		con=sqlite3.connect('courses')
		cur=con.cursor()
		cur.execute('INSERT INTO dept_tbl VALUES(?,?)',(deptname,deptcode))
		con.commit()
		return redirect(('/'))
	return render_template('add.html')
@app.route('/edit_dept/<string:deptcode>',methods=['GET','POST'])
def edit_dept(deptcode):
	if request.method=='POST':
		deptname=request.form.get('deptname')
		con=sqlite3.connect("courses")
		con.row_factory=sqlite3.Row
		cur=con.cursor()
		cur.execute("update dept_tbl set dept_name=? where dept_code=?",(deptname,deptcode))
		con.commit()
		return redirect('/')

	con=sqlite3.connect("courses")
	con.row_factory=sqlite3.Row
	cur=con.cursor()
	cur.execute("SELECT * FROM dept_tbl where dept_code=?",(deptcode,))
	data=cur.fetchone()
	return render_template('edit.html',data=data)

@app.route('/delete_dept/<string:deptcode>',methods=['GET'])
def delete_dept(deptcode):
	con=sqlite3.connect("courses")
	con.row_factory=sqlite3.Row
	cur=con.cursor()
	cur.execute("delete from dept_tbl where dept_code=?",(deptcode,))
	con.commit()
	return redirect('/')

if __name__ == '__main__':
	app.run(debug = True,port=4444)
