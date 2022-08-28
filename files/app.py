import pywhatkit as app
import json

class CONFIG:
    f = open('config.json')
    data = json.load(f)
    
    phone = data['setting'][0]['phone_number']
    msg = data['setting'][0]['message_text']
    msg_count = data['setting'][0]['message_count']

    f.close()


def SendMsg():
    count = CONFIG.msg_count
    while count > 0:
        try :
            app.sendwhatmsg_instantly(
                phone_no = CONFIG.phone,
                message = CONFIG.msg,
                tab_close = True
            )
            count -= 1
        except :
            print('Error In Sending !')
    print("All Messages Are Sent !")



if __name__ == '__main__':
    SendMsg()