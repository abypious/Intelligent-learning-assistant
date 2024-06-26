import base64
import os
from datetime import datetime


import math
from flask import *
from werkzeug.utils import secure_filename

from src.dbcon import *

app=Flask(__name__)

@app.route("/logincode",methods=['post'])
def logincode():
    uname=request.form['username']
    print(uname)
    password=request.form['password']
    print(password)
    q="select * from login where user_name=%s and password=%s and user_type='student'"
    val=(uname,password)
    res=selectone(q,val)
    if res is None:
        return jsonify({'task':'invalid'})
    else:
        return jsonify({'task':'success','lid':res[0]})

@app.route("/userreg",methods=['post'])
def userreg():


        print(request.form)
        studname=request.form['sname']
        dob=request.form['dob']
        place=request.form['place']
        gender=request.form['gender']
        phonenumber=request.form['phnum']
        description=request.form['description']


        uname = request.form['username']
        passwd = request.form['password']

        qry="INSERT INTO login values(null,%s,%s,'student')"
        val=(uname,passwd)
        id=iud(qry,val)

        qry="INSERT INTO student values(null,%s,%s,%s,%s,%s,%s,%s)"
        val=(studname,dob,place,gender,phonenumber,description,str(id))
        iud(qry,val)
        return jsonify({'task': 'success'})


@app.route("/feedback",methods=['post'])
def addfeedback():

    userid=request.form['userid']
    parentfb=request.form['parentfb']


    qry="INSERT INTO feedback values(null,%s,%s,curdate())"
    val=(userid,parentfb)
    iud(qry,val)
    return jsonify({'task': 'success'})
     









    





@app.route("/intraction",methods=['post'])
def intraction():
     userid= request.form['userid']
     questions=request.form['questions']
     expertid=request.form['expid']

     qry="INSERT INTO intraction values(null,%s,%s,%s,curdate(),curtime())"
     val=(userid,questions,expertid)
     iud(qry,val)
     return jsonify({'task':'success'})



@app.route("/viewresponse",methods=['post'])
def viewresponse():
    print(request.form)
    uid=request.form['uid']


    qry="SELECT `intraction`.*,`response`.* FROM `intraction` JOIN `response` ON `intraction`.`intr_id`=`response`.`intr_id` WHERE `intraction`.`user_id`=%s"
    val=(uid)
    res=androidselectall(qry,val)

    return jsonify(res)

@app.route("/viewtips",methods=['post'])
def viewtips():

    qry="SELECT `tips`.*,`experts`.* FROM `tips` JOIN `experts` ON `tips`.`exp_id`=`experts`.`login_id`"

    res=androidselectallnew(qry)
    return jsonify(res)




@app.route("/review",methods=['post'])
def review():
    print(request.form)


    lid=request.form['lid']
    qry="SELECT `review`,`rating`,`date`,`answer`,`review`.`id` FROM `review` JOIN `dataset` ON `dataset`.`id`=`review`.`qid` WHERE `lid`=%s"
    val=(lid,)
    res = androidselectall(qry,val)
    print(res)
    return jsonify(res)







@app.route("/insertrarting",methods=['post'])
def insertrarting():
    print(request.form)
    lid=request.form['lid']
    review=request.form['review']
    rating = request.form['rating']
    id = request.form['aid']
    qry="INSERT INTO `review` VALUES(NULL,%s,%s,%s,%s,CURDATE())"
    val=(lid,id,review,rating)
    iud(qry,val)
    return jsonify({'task':'ok'})




@app.route("/viewcomp",methods=['post'])
def viewcomp():
    print(request.form)
    lid=request.form['lid']
    qry="SELECT * FROM `complaint` WHERE `lid`=%s"
    val=(lid,)
    res = androidselectall(qry,val)
    print(res)
    return jsonify(res)


@app.route("/sendcomp",methods=['post'])
def sendcomp():
    uid=request.form['lid']
    comp=request.form['comp']
    q="INSERT INTO `complaint` VALUES(NULL,%s,%s,'pending',CURDATE())"
    val=(uid,comp)
    iud(q,val)
    return jsonify({'task':'success'})











@app.route("/viewexpert",methods=['post'])
def viewexpert():
    qry="SELECT * FROM experts"
    res = androidselectallnew(qry)
    print(res)
    return jsonify(res)

@app.route("/viewmaterial",methods=['post'])
def viewmaterial():
    qry="SELECT `study_materials`.*,`experts`.`exp_name` FROM `experts` JOIN `study_materials` ON `study_materials`.`exp_id`=`experts`.`login_id`"
    res = androidselectallnew(qry)
    print(res)
    return jsonify(res)









@app.route("/upload_report",methods=['post'])
def upload_report():
    uid = request.form['uid']
    exid = request.form['exid']
    report=request.files['file']
    fname=secure_filename(report.filename)
    report.save(os.path.join('static/medicalreport',fname))
    qry = "insert into medical_report values(null,%s,%s,%s)"
    val=(uid,fname,exid)
    iud(qry,val)

    return jsonify({'task':"success"})



@app.route("/viewguidance",methods=['post'])
def viewguidance():
    print(request.form)
    lid=request.form['lid']
    qry="SELECT `guidance`.`g_info`,`medical_report`.`report_info`,`experts`.`exp_name` FROM `experts` JOIN `medical_report` ON `medical_report`.`exp_id`=`experts`.`login_id`JOIN `guidance` ON `guidance`.`report_id`=`medical_report`.`report_id` WHERE `medical_report`.`user_id`=%s"
    val=(lid,)
    res = androidselectall(qry,val)
    print(res)
    return jsonify(res)

app.run(host='0.0.0.0',port=5000)
