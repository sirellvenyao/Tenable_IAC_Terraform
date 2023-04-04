import time,datetime
import sys,io,os
import json

def sleeptime(hour,min,sec):
    return hour*3600+min*60+sec


def current_time():
    current_time = datetime.datetime.now()
    return current_time

def execute_aws_cli_elv2_description():
    command_str = ""
    os.system(command_str)

def execute_aws_cli_elv2_attribution(lb):
    command_str = 'aws elbv2 describe-load-balancer-attributes --load-balancer-arn ' + lb + '>/Users/ellvenyao/Desktop/ARN.json'
    #print(command_str)
    os.system(command_str)

def getloadbalancerarnlist():
    list = []
    aws_output_json_file = open('/Users/ellvenyao/Desktop/lb.json')
    json_content = json.load(aws_output_json_file)
    for loadbalance in json_content['LoadBalancers']:
        #print(loadbalance['LoadBalancerArn'])
        list.append(loadbalance['LoadBalancerArn'])
    return(list)

def main():
    execute_aws_cli_elv2_description()
    list_disable_s3 = []
    list_disable_delete = []
    list_enable_s3 = []
    list_enable_delete = []
    lb_list = getloadbalancerarnlist()
    for lb in lb_list:
        deletion_protection = 0
        access_logs = 0
        access_logs_bucket =0
        execute_aws_cli_elv2_attribution(lb)
        lb_arn_json_file = open('/Users/ellvenyao/Desktop/ARN.json')
        lb_json_content = json.load(lb_arn_json_file)
        print(lb_json_content)
        for key in (lb_json_content['Attributes']):
            if (key['Key']) == "deletion_protection.enabled" and key['Value'] =="true":
                deletion_protection = 1
            if ((key['Key']) == "access_logs.s3.enabled" and key['Value'] =="true"):
                access_logs = 1
            if ((key['Key']) == "access_logs.s3.bucket" and len(key['Value']) >0):
                access_logs_bucket = 1
        if deletion_protection == 1 :
            print (lb + ' delete protection is good')
            list_enable_delete.append(lb)

        if deletion_protection != 1:
            print (lb + ' delete protection is NULL')
            list_disable_delete.append(lb)

        if access_logs == 1 and access_logs_bucket == 1:
            print (lb + ' access logs s3 is good')
            list_enable_s3.append(lb)

        if access_logs != 1 or access_logs_bucket != 1:
            print (lb + ' access logs s3 is NULL')
            list_disable_s3.append(lb)

        print("---------------------------------------------")

    print("no deletion_protection is ",list_disable_delete)
    print("enable deletion_protection is ",list_enable_delete)    
    print("no access_logs is ",list_disable_s3)
    print("enable access_logs is ",list_enable_s3)



main()