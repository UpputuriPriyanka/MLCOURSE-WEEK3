name=''
from .data.about import bot
from .code import *
def get_intent(data):
    global name 
    m=data['message'].lower()
    if data['key']=="name":
        name=m
        return "next"
    if data['key']=="month":
        return "festivalresult"
    if data['key']=="expression":
        return "evaluateresult"

    if any(x in m for x in ["festivals","festivaldetails"]):
        return "festivals"
    elif any(x in m for x in ["calculate","Calculate","Evaluate","eval","Eval","evaluate","evaluation","Evaluation","expression","Expression","Calculation","calculation"]):
        return "evaluate"
    elif any(x in m for x in ["end","close","bye","Bye"]):
        return "end"
    elif any(x in m for x in ["hy","hi","Hi","Hy","Hello","hello"]):
        return "next"
    else:
        return "echo"

def handle(data):
    global name 
    from flask import render_template
    intent=get_intent(data)
    if intent == 'next':
        return render_template('messages/greet.html',name=name,
        question={'key':'request','text':'What would you like to do?'})
    elif intent == 'festivals':
        return render_template('messages/festivalintro.html',name=name,
        question={'key':'month'})
    elif intent == 'festivalresult':
        return render_template('messages/monthintro.html',data=bot,wdata=festival_report(data['message']),name=name,
        question={'key':'response'})
    elif intent == 'evaluate':
        return render_template('messages/evaluateintro.html',name=name,
        question={'key':'expression'})   
    elif intent == 'evaluateresult':
        return render_template('messages/exprevaluateintro.html',data=bot,wdata=evaluate_expression(data['message']),name=name,
        question={'key':'response'}) 
    elif intent == "end":
        return render_template('messages/endintro.html',name=name,
        question={'key':'Restart'}) 
    else:
        return render_template('messages/echo.html',data=data)
