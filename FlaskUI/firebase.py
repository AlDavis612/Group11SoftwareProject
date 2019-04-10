import pyrebase

config = {
    "authDomain": "rjiimageprocessing.firebaseapp.com",
    "apiKey": "AIzaSyC0hVt4CnAht6Mvo7M-yGO0Nf4kqlOW2-M",
    "databaseURL": "https://rjiimageprocessing.firebaseio.com",
    "projectId": "rjiimageprocessing",
    "storageBucket": "rjiimageprocessing.appspot.com",
    "messagingSenderId": "11581998729"
}

firebase = pyre.initialize_app(config)

auth = firebase.auth()

email = input('Please enter your email\n')
password = input('Please enter your password\n')

#user = auth.create_user_with_email_and_password(email, password)

user = auth.sign_in_with_email_and_password(email, password)
auth.send_email_verification(user['idToken'])
auth.send_password_reset_email(email)
#print(auth.get_account_info(user['idToken']))