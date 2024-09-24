from flask import Flask, request,  render_template, redirect, url_for, flash
from db import get_db_connection
import datetime

app= Flask(__name__)

@app.route('/')
def index():
  return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
  UserEmail = request.form['useremail']
  UserPassword = request.form['password']
  print(UserEmail, UserPassword)

  # Establish connection with database
  connection = get_db_connection()
  cursor = connection.cursor()
  
  #login query
  login_query = "SELECT * FROM m_users where s_useremail = %s"
  cursor.execute(login_query, (UserEmail,) )
  user = cursor.fetchone()
  print(user)

    
  return render_template('loginok.html')


#singup page render
@app.route('/register', methods=['GET'])
def register():
    return render_template('registration.html')


#UserRegistration 
@app.route('/userregistration', methods=['POST'])
def userregistration():
  try:
    UserName = request.form['username']
    UserEmail = request.form['useremail']
    UserPassword = request.form['password']
    UserType  = request.form['usertype']
    
    print(UserEmail, UserPassword)

    # Establish connection with database
    connection = get_db_connection()
    cursor = connection.cursor()

    user_ip = request.remote_addr
    login_time = datetime.datetime.now()
    time = str(login_time)
    
    #Select query
    query = "select * from m_users where s_useremail = %s"
    cursor.execute(query, (UserEmail, ))
    users = cursor.fetchone()



    if users:
      return render_template('login.html')
    else:
      
      insert_query="insert into m_users (s_username, s_useremail, ns_password, s_usertype, ns_last_login, ns_last_login_ip) values (%s, %s, %s, %s, %s, %s)"
      cursor.execute(insert_query, (UserName, UserEmail, UserPassword, int(UserType), time, str(user_ip)))
      connection.commit()    
      print("ok?")

    cursor.close()
    connection.close()
    return render_template('login.html')
  
  except Exception as e:
    print(str(e))
  

if __name__ == '__main__':
  app.run(debug=True)


# import datetime

# login_time = datetime.datetime.now()

# print(type(str(login_time)))