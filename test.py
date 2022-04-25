import ServerEmail
import argparse

# python test.py --server-name FeiNewML --exp-name testing --test-error
# python test.py --server-name FeiNewML --exp-name testing

def parse_args():
    parser = argparse.ArgumentParser("Automatically Send Email When using Server to Run Experiments")
    parser.add_argument("--server-name", type=str, default="FeiML", help="FeiML, FeiNewML, Miao_Exxact")
    parser.add_argument("--exp-name", type=str, default=None, help="name of the experiment")
    parser.add_argument("--test-error", action="store_true", default=False)
    return parser.parse_args()

def run_exp(arglist):
    if arglist.test_error:
        return 1/0
    else:
        return 1

if __name__ == '__main__':
    arglist = parse_args()
    # customize your choice
    Emails = ServerEmail.ServerEmail(mail_host="smtp.163.com", 
                                mail_sender="******@163.com", 
                                mail_license="ABCDEFGHIJKLMNOP", 
                                mail_receivers="sihong.he@uconn.edu", 
                                server_name=arglist.server_name)

    print("test send begin email")
    Emails.send_begin_email(exp_name=arglist.exp_name)
    try : 
        run_exp(arglist=arglist)
        print("test send end email")
        Emails.send_end_email(exp_name=arglist.exp_name)
    except Exception as errorinfo:
        print("test send error email")
        Emails.send_einfo_email(exp_name=arglist.exp_name, einfo=errorinfo)