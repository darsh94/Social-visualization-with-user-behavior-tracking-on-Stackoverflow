from application_code import application
from flask import *
from flask_login import current_user,login_user,logout_user
from  data_table_model import user_login,user_logging,user_stackoverflow_activity
import flask_login
from forms_classes import login_form,registeraton_form
from werkzeug.urls import url_parse
from application_code import database_var
import datetime
from html_tables import user_logs,user_activity
from  sqlalchemy import *
# For making visualizations
from flask import jsonify

from bokeh.models.glyphs import VBar
from bokeh.plotting import figure
from bokeh.core.properties import value
import bokeh.palettes
from bokeh.io import show
from bokeh.embed import components
from bokeh.models.sources import ColumnDataSource






from collections import Counter
from math import pi

import pandas as pd



from bokeh.plotting import figure
from bokeh.transform import cumsum



#
# @application.route('/')
# @application.route('/index')
# def index():
#     return 'Hell bci'




@application.route('/')
def main_page():
    return render_template('index.html')



@application.route('/writeup')
def write_up():
    return render_template('Write-Up.html')


@application.route('/homepage')
@flask_login.login_required
def home_page():
    # print(current_user.)
    uid=current_user.id
    logs = user_logging.query.filter_by(user_id=uid).order_by(user_logging.timestamp).limit(10).all()
    user_activities=user_stackoverflow_activity.query.filter_by(user_id=uid)
    activity=[]
    for act in user_activities:
        activity.append({'event':act.event,'count':act.count,'timestamp':act.timestamp})

    table_activity=user_activity(user_activities)
    table_activity.border=True
    table_len2=len(activity)
    print(table_len2)

    actual_logs = []
    for log in logs:
        actual_logs.append({'timestamp': log.timestamp, 'type': log.type})
    # print(actual_logs)

    user={'username':current_user.user_name,'logs':actual_logs}
    table_to_send=user_logs(actual_logs)
    table_to_send.border=True
    table_len=len(actual_logs)
    link_to_stackoverflow='https://stackoverflow.com/questions/tagged/java?sort=frequent&pageSize=15&uid='+str(current_user.id)
    # print(link_to_stackoverflow)


    return render_template('homepage.html',table=table_to_send,tablelen=table_len,link=link_to_stackoverflow,table2=table_activity,tablelen2=table_len2,users=user)


@application.route('/login-page',methods=['POST','GET'])
def login_page():
    if current_user.is_authenticated:
        redirect(url_for('home_page'))
    form=login_form()
    if form.validate_on_submit():
        user=user_login.query.filter_by(user_name=form.uname.data).first()
        if user is None:
            print('hi')
            flash('The given user is not present. Please register')
            return redirect(url_for('login_page'))
        elif not user.verify_password(form.password.data):
            print('h2i')
            flash('The password is incorrect')
            return redirect(url_for('login_page'))


        # if user is None or not user.verify_password(form.password.data):
        #     print('hi')
        #     flash('Either the username or password is incorrect')
        #     return redirect(url_for('login_page'))
        login_user(user)
        # application.logger.info('Hello')
        user_log=user_logging(user_id=user.id,timestamp=datetime.datetime.now(),type='log in')
        database_var.session.add(user_log)
        database_var.session.commit()
        # print('Hie')
        # print(current_user.id)
        # logs=user_logging.query.filter_by(user_id=user.id)
        # actual_logs=[]
        # for log in logs:
        #     actual_logs.append({'timestamp':log.timestamp,'type of activity':log.type})
        # print(actual_logs)


        success_page=request.args.get('next')
        if not success_page or url_parse(success_page).netloc != '':
            success_page = url_for('home_page')
        return redirect(success_page)

        # return redirect(url_for('homepage'))
    return render_template('login_page.html',form=form)


@application.route('/log_out')
def logoutuser():
    print('logging the user out')
    user_log = user_logging(user_id=current_user.id, timestamp=datetime.datetime.now(), type='log out')
    database_var.session.add(user_log)
    database_var.session.commit()
    logout_user()
    return redirect(url_for('login_page'))


@application.route('/register-page',methods=['POST','GET'])
def register_page():
    if current_user.is_authenticated:
        redirect(url_for('home_page'))
    form=registeraton_form()
    if form.validate_on_submit():
        print('Hie')
        user=user_login(user_name=form.uname.data)
        check_username = user_login.query.filter_by(user_name=form.uname.data).first()
        if (check_username is not None):
            print('username already exists')
            flash('The username already exists. Please enter a different username.')
            return redirect(url_for('register_page'))
        user.set_hashed_password(form.password.data)
        database_var.session.add(user)
        database_var.session.commit()
        flash('Congrats, you have successfully registered on the website')
        return redirect(url_for('login_page'))
    return render_template('register_page.html',form=form)

#
#
@application.route('/profile',methods=['POST','GET'])
def profile_data():
    print('head')

    if request.method=='POST':
        print('yes')
        data=request.form
        temp=dict(data)
        dict_data={}
        for k in temp:
            dict_data[k]=temp[k][0]
        dict_data['count']=int(dict_data['count'])
        # dict_data={k: v for k, v in dict_data.items()}
        print(dict_data)
        user_activity_db = user_stackoverflow_activity.query.filter(and_(user_stackoverflow_activity.user_id==dict_data['id'],
                                                                         user_stackoverflow_activity.event==dict_data['activity'])).first()
        # user_activity_db=user_stackoverflow_activity.query.filter_by(user_id=dict_data['id']).filter_by(event=dict_data['activity']).first()
        if user_activity_db is None:
            user_activity=user_stackoverflow_activity(user_id=dict_data['id'],event=dict_data['activity'],count=dict_data['count'],timestamp=datetime.datetime.now())
            database_var.session.add(user_activity)
            database_var.session.commit()

        else:
            user_activity=user_stackoverflow_activity.query.filter(and_(user_stackoverflow_activity.user_id==dict_data['id'],
                                                                         user_stackoverflow_activity.event==dict_data['activity'])).update({'count':user_stackoverflow_activity.count+dict_data['count'],'timestamp':datetime.datetime.now()})
            # database_var.session.add(user_activity)
            database_var.session.commit()

            # user_activity=user_stackoverflow_activity.filter_by(user_id=dict_data['id']).filter_by(event=dict_data['activity'])\
            #                                          .update({'count':user_stackoverflow_activity.count})



    return 'Ok'







def create_bars(title,data):
    x_name='users'
    y_name='event_count'
    width = 1200
    height = 300
    user=[i for i in data]
    colors = ["#c9d9d3", "#718dbf", "#e84d60"]
    activity={}
    activity['vote']=[]
    activity['share']=[]
    activity['comment']=[]
    for i in data:
        activity['vote'].append(data[i]['vote'])
        activity['share'].append(data[i]['shared_posts'])
        activity['comment'].append(data[i]['comment'])
        # shared_posts
    final_data={'user': user,
            'vote': activity['vote'],
            'share': activity['share'],
            'post': activity['comment']}

    # user=data['users']
    #
    #
    # data = {'user': user,
    #         'vote': [2, 1, 4],
    #         'share': [5, 3, 4],
    #         'post': [3, 2, 4]}
    # #
    p = figure(x_range=user, plot_height=250, title=title,
               toolbar_location=None, tools="")
    # # source = ColumnDataSource(data=dict(user=user, clicks=clicks, color=palette))
    events = ['vote', 'share', 'post']
    p.vbar_stack(events, x='user', width=0.4, color=colors, source=final_data,legend=[value(x) for x in events])
    #
    p.y_range.start = 0
    # p.x_range.range_padding = 0.1
    p.xgrid.grid_line_color = None
    p.axis.minor_tick_line_color = None
    p.outline_line_color = None
    p.legend.location = "top_left"
    p.legend.orientation = "horizontal"

    # x = data['users']
    # user=data['users']
    # clicks=data['click']
    #
    #
    # palette = ["#99d594", "#ffffbf","#99d592"]
    # fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
    # counts = [5, 3, 4, 2, 4, 6]
    #
    # source = ColumnDataSource(data=dict(user=user, clicks=clicks, color=palette))
    #
    # p = figure(x_range=user, y_range=(0, max(clicks)), plot_height=250, title="Clicks",
    #            toolbar_location=None, tools="")
    #
    # p.vbar(x='user', top='clicks', width=0.9, color='color', legend="user", source=source)
    #
    # p.xgrid.grid_line_color = None
    # p.legend.orientation = "horizontal"
    # p.legend.location = "top_center"
    # )
    return p


@application.route('/chart')
def charts():
    user_activity=user_stackoverflow_activity.query.filter_by(user_id=current_user.id).first()
    message_to_show=''
    if(user_activity is None):
        message_to_show='The current user has not interacted with stackoverflow. Please go back and make some interactions to see the data.'
    else:
        data_to_plot={}
        event={}
        user_activity=user_stackoverflow_activity.query.order_by(user_stackoverflow_activity.user_id).all()

        for u in user_activity:
            if (u.event == 'votes'):
                event['vote'] = u.count

            if (u.event == 'shared_posts'):
                event['shared_posts'] = u.count

            if (u.event == 'comment'):
                event['comment'] = u.count
            if(u.user_id not in data_to_plot):
                data_to_plot[u.user_id]=event
        print(data_to_plot)







    # data_to_send={'users':['1','2','3'],'click':[42,32,12]}
    plot_chart=create_bars('Activity Comparison',data_to_plot)
    script,div=components(plot_chart)


    return render_template("chart.html",
                           the_div=div, the_script=script)

@application.route('/chart_pie')
@flask_login.login_required

def pie_chart():
    id=current_user.id
    # For making the pie cahrt for current user
    c_user={}
    message_to_display=''
    # logs = user_logging.query.filter_by(user_id=uid)
    user_activity_data=user_stackoverflow_activity.query.filter_by(user_id=id).all()
    is_none=0


    print(user_activity_data)
    if(user_stackoverflow_activity is None):
        message_to_display+='The current user has not interacted with stackoverflow. Please go back and make some interactions to see the data.'
        is_none=1

    else:
        data_to_show={}

        print(user_activity_data)
        for i in user_activity_data:
            # print(i.id)
            if(i.event =='vote-up'):
                data_to_show ['vote-up']= i.count
            if (i.event == 'vote-down'):
                data_to_show['vote-down'] = i.count
            if (i.event == 'mark_favourite'):
                data_to_show['mark_favourite'] = i.count

            if (i.event == 'shared_posts'):
                data_to_show['shared_posts'] = i.count

            if (i.event == 'comment'):
                data_to_show['comment'] = i.count
        c_user['comment']=data_to_show['comment']
        c_user['shared_post']=data_to_show['shared_posts']
        c_user['vote_up']=data_to_show['vote-up']
        c_user['vote_down'] = data_to_show['vote-down']
        c_user['mark_favourite'] = data_to_show['mark_favourite']
        c_user['id']=id


        other_user={}
        users_activity_data=user_stackoverflow_activity.query.all()
        print(len(users_activity_data))

        for user in users_activity_data:
            print(other_user)
            # print(user.event)
            # print(user.count)
            # print(user.user_id)
            if(user.user_id !=id):
                if user.user_id not in other_user:
                    other_user[user.user_id]={}
                if (user.event == 'shared_posts'):
                    other_user[user.user_id]['shared_posts'] = user.count
                if (user.event == 'mark_favourite'):
                    other_user[user.user_id]['mark_favourite'] = user.count

                if (user.event == 'vote-up'):
                    other_user[user.user_id]['vote-up'] = user.count

                if (user.event == 'vote-down'):
                    other_user[user.user_id]['vote-down'] = user.count


                if (user.event == 'comment'):
                    other_user[user.user_id]['comment'] = user.count
        print(other_user)
        print(c_user)
        # final_data=jsonify(other_user)

        return render_template("chart_pie.html",current_user=c_user,other_users=other_user,uid=id)








