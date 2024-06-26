import os
from flask import *
from werkzeug.utils import secure_filename

app = Flask (__name__)
app.secret_key="qqwerty124"
import functools
from src.dbcon import *


def login_required(func):
    @functools.wraps(func)
    def secure_function():
        if "ln" not in session:
            return redirect("/")
        return func()
    return secure_function
@app.route ('/')
def main():
    return render_template ('LOGIN.html')
@app.route ('/log',methods=['post'])
def log():
    uname=request.form["textfield"]
    pwd=request.form["textfield2"]
    qry="select*from login where user_name=%s and password=%s"
    val=(uname,pwd)
    res=selectone(qry,val)
    if res is None:
        return'''<script>alert("invalid username or password");window.location="/"</script>'''
    elif res[3]=="admin":
        return redirect('adminhome')
    elif res[3]=="expert":
        session['lid'] =str(res[0])
        return redirect('expert_home')



    else:
        return'''<script>alert("invalid username or password");window.location="/"</script>'''
@app.route ('/adminhome')
@login_required
def adminhome():
    return render_template ('ADMINHOME.html')

@app.route ('/addexperts',methods=['post'])
@login_required
def addexperts():
    return render_template('ADD EXPERTS.html')

@app.route('/addexpert1',methods=['post'])
@login_required
def addexpert1():
    try:
        name=request.form['textfield']
        exp=request.form['textfield2']
        gender=request.form['radiobutton']
        place=request.form['textfield3']
        phone=request.form['textfield4']
        email=request.form['textfield5']
        username=request.form['textfield6']
        password=request.form['textfield7']
        qry="insert into login values(null,%s,%s,'expert')"
        val=(username,password)
        lid=iud(qry,val)
        qry1="insert into experts values(null,%s,%s,%s,%s,%s,%s,%s)"
        val=(name,exp,gender,place,phone,email,str(lid))
        iud(qry1,val)
    except Exception as e:
        return '''<script>alert("Username already exists");window.location="/expertdetails#About"</script>'''


    return'''<script>alert("success");window.location="/expertdetails#About"</script>'''















@app.route('/add_guidance')
@login_required
def addguidance():
    id=request.args.get('id')
    session['rid']=id



    return render_template('ADD_GUIDANCE.html')
@app.route('/addnewguidance',methods=['post'])
@login_required
def addnewguidance():
    guidance=request.form['textarea']
    rid=session['rid']
    expid=session['lid']
    qry="insert into guidance values(null,%s,%s,%s)"
    val=(rid,expid,guidance)
    iud(qry,val)
    return'''<script>alert("success");window.location="/medicalreports"</script>'''




@app.route('/add_materials')
@login_required
def add_materials():
    qry="SELECT * FROM `study_materials` WHERE `exp_id`=%s"
    val=(session['lid'])
    s=selectallll(qry,val)

    return render_template('ADD_MATERIALS.html',val1=s)

@app.route('/addmaterials',methods=['post'])
@login_required
def addmaterials():
    lid=str(session['lid'])
    type=request.form['select']
    material=request.files['file']
    fnm=secure_filename(material.filename)
    path=r"./static/materials"
    material.save(os.path.join(path,fnm))
    qry="insert into study_materials values(null,%s,curdate(),%s,%s)"
    val=(fnm,str(lid),type)
    iud(qry,val)
    return'''<script>alert("success");window.location="/expert_home"</script>'''




@app.route('/addtips',methods=['post'])
@login_required
def addtips():
    return render_template('ADDTIPS.html')


@app.route('/addnewtip',methods=['post'])
@login_required
def addnewtip():
    lid=str(session['lid'])
    tip=request.form ['textarea']
    qry="insert into tips values (null,%s,%s)"
    val=(tip,str(lid))
    iud(qry,val)
    return '''<script>alert("success");window.location="/expert_home"</script>'''




@app.route('/expertdetails')
@login_required
def expertdetails():


    qry="SELECT * FROM `experts`"
    res=selectall(qry)
    return render_template('EXPERT DETAILS.html',val=res)


@app.route('/expert_home')
@login_required
def expert_home():
    return render_template('EXPERT HOME.html')

@app.route('/interaction')
@login_required
def interaction():
    id=session['lid']
    qry="SELECT `intraction`.*,`student`.`std_name` FROM `student` JOIN `intraction` ON `intraction`.`user_id`=`student`.`user_id` WHERE `intraction`.`exp_id`=%s AND `intraction`.`intr_id` NOT IN(SELECT `intr_id` FROM `response`) "
    val=(str(id))
    print(val)
    res=selectallll(qry,val)


    return render_template('INTERACTION.html',val=res)


@app.route('/medicalreports')
@login_required
def medicalreports():
    id=session['lid']

    qry="SELECT `medical_report`.*,`student`.`std_name` FROM `student` JOIN `medical_report` ON `medical_report`.`user_id`=`student`.`user_id` WHERE `medical_report`.`exp_id`=%s AND `medical_report`.`report_id` NOT IN (SELECT `report_id` FROM `guidance`)"
    val=(str(id))
    res=selectallll(qry,val)
    print()

    return render_template('MEDICAL_REPORTS.html',val=res)

@app.route('/reply')
@login_required
def reply():
    id=request.args.get('id')
    session['qid']=id

    return render_template('REPLY.html')

@app.route('/remove')
@login_required
def remove():
    id=request.args.get('id')
    q="delete from tips where tips_id=%s"
    val=(id)
    iud(q,val)

    return '''<script>alert("removed");window.location="/viewtips"</script>'''



@app.route('/removes')
@login_required
def removes():
    id=request.args.get('id')
    q="delete from study_materials where std_mat_id=%s"
    val=(id)
    iud(q,val)

    return '''<script>alert("removed");window.location="/add_materials"</script>'''

@app.route('/viewtips')
@login_required
def viewtips():
    qry="SELECT * FROM `tips` where exp_id=%s"
    val=(session['lid'])
    res=selectallll(qry,val)
    return render_template('view tips.html',val=res)


@app.route('/sendreply',methods=['post'])
@login_required
def sendreply():
    reply=request.form['textarea']
    qry="INSERT INTO `response` VALUES(NULL,%s,%s,CURDATE(),CURTIME())"
    val=(str(session['qid']),reply)
    iud(qry,val)
    return '''<script>alert("success");window.location="/interaction"</script>'''




@app.route('/studentdetails')
@login_required
def studentdetails():
    qry="SELECT * FROM `student`"
    res=selectall(qry)
    return render_template('STUDENT DETAILS.html',val=res)

@app.route('/studentsresponse')
@login_required
def studentsresponse():
    qry = "SELECT * FROM `student`"
    res = selectall(qry)
    return render_template('STUDENTS RESPONSE.html',val=res)



@app.route("/type_view",methods=['get','post'])
@login_required
def type_view():
    id=request.args.get('id')
    print(id)
    nm=request.args.get('nm')
    q = 'SELECT `questions`.`mat_type` FROM `questions` JOIN `video_frame` ON `video_frame`.`id`=`questions`.`id` WHERE `std_id`=%s AND `ratio`>0.5 order by `ratio` DESC'
    val= id
    result = selectone(q,val)
    print(result)
    if result is not None:
        return  render_template('type_view.html',val=result,n=nm)
    else:
        return '''<script>alert('No information');window.location='/dettected_std_dels'</script>'''



@app.route('/feedback')
@login_required
def feedback():
    qry = "SELECT  `feedback`.*,`student`.`std_name` FROM `student` JOIN `feedback` ON `feedback`.`user_id`=`student`.`user_id`  ORDER  BY `f_b_id` DESC"
    res=selectall(qry)

    return render_template('FEEDBACK.html',val=res)


@app.route('/editexpert')
@login_required
def editexpert():
    id=request.args.get('id')
    session['id']=id
    qry="SELECT * from experts where login_id=%s"
    val=str(id)
    res=selectone(qry,val)
    return render_template('EDIT EXPERTS.html',val=res)

@app.route('/logout')
def logout():
    session.clear()
    return render_template('LOGIN.HTML')

@app.route('/updateexperts',methods=['post'])
@login_required
def updateexperts():
    id=session['id']
    name = request.form['textfield']
    exp = request.form['textfield2']
    gender = request.form['radiobutton']
    place = request.form['textfield3']
    phone = request.form['textfield4']
    email = request.form['textfield5']
    qry="update experts set exp_name=%s,experience=%s,gender=%s,place=%s,phone=%s,email=%s where login_id=%s"
    value=(name,exp,gender,place,phone,email,str(id))
    iud(qry,value)
    return '''<script>alert("updated");window.location="/expertdetails"</script>'''




@app.route('/deleteexpert')
@login_required
def deleteexpert():
    id = request.args.get('id')
    session['id'] = id
    qry="DELETE FROM login WHERE user_id=%s"
    val=(id)
    iud(qry,val)
    qry="DELETE FROM experts WHERE login_id=%s"
    iud(qry,val)
    return '''<script>alert("expert deleted ");window.location="/expertdetails#About"</script>'''














app.run(debug=True)
