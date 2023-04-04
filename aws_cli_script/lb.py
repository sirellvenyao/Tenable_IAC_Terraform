import time,datetime
import sys,io,os
import json

def sleeptime(hour,min,sec):
    return hour*3600+min*60+sec


def current_time():
    current_time = datetime.datetime.now()
    return current_time

def execute_aws_cli_ec2_description(instanceid):
    command_str = "aws ec2 describe-instances --instance-ids " + instanceid + " --query 'Reservations[*].Instances[*].{Instance:InstanceId,LaunchTime:LaunchTime,PrivateIpAddress:PrivateIpAddress,Tags:Tags}' >>/Users/ellvenyao/Desktop/EC2.json"
    print(command_str)
    os.system(command_str)



def main():
    EC2InstanceList = ["i-00d82a9c26b15b935","i-01b4a69be5380988c","i-01b5f0ca2e306dfbc","i-02a584709f9966fc0","i-031ce1371214d1b74","i-05c5b39ac7a7248a6","i-079caf8af1b34dca2","i-07c08cc29be866d0e","i-087e742095ae15918","i-09472f4dd635a3002","i-0aab331d327bc53c8","i-0baa7738dabcab616","i-0c4f3c8e338c3785c","i-0da2d14d9ac7f19e3","i-0e0b90679e85a0fe8","i-0f9fb88aad48342c6","i-0054505158064ce8e","i-0087ca6c1f49b478e","i-00d82a9c26b15b935","i-00e4b32461f7fe964","i-011c77506f10b2eaa","i-011ca52dd3f63c146","i-0170f53aa6e2d0e26","i-0192fe662e03aece7","i-01b4a69be5380988c","i-01b5f0ca2e306dfbc","i-02a584709f9966fc0","i-02ea423dcceef0c21","i-0313fd349ff12dbff","i-031ce1371214d1b74","i-03d03baaaf6e98e83","i-04e0b1b3e4d9fffed","i-04f84f762f5a10115","i-05000eb63e77d1eb5","i-0515c94ca23d61684","i-053562ad4cd0bacc4","i-058962013d4b53f8a","i-05c5b39ac7a7248a6","i-05fd61b621a819b01","i-06cb23f047b96e8f1","i-06ec9fe637cf76595","i-0717d6b75ff79cff7","i-078ec2dd6a8c7a4cf","i-0791b54d5b2dddd98","i-079caf8af1b34dca2","i-07c08cc29be866d0e","i-07e02871769a98cf6","i-080326d15494c2238","i-082b598716cedd61f","i-08776853a763fb6a5","i-087e742095ae15918","i-08db190b293ee6824","i-093c552ce526e583e","i-09472f4dd635a3002","i-094bb972df49a792a","i-09625f5594405f64c","i-09bb63b2d053c39b9","i-09efcb9bf481cb325","i-0aab331d327bc53c8","i-0b064c75aa29d82b1","i-0b49b8babf6e9c680","i-0baa7738dabcab616","i-0c2a0551a6562c49d","i-0c4f3c8e338c3785c","i-0c76f721ea62fbbeb","i-0c9f73bda6d263379","i-0cb9ea5607dfdc554","i-0d000447086a75265","i-0d544857afed7421b","i-0da2d14d9ac7f19e3","i-0de89e2173fa79d71","i-0e0b90679e85a0fe8","i-0e3b8ecf5c18c07f9","i-0e9bd9a514f1667a0","i-0ee9bb25196d24500","i-0f0ed897e2124b9e4","i-0f1796adc4079769e","i-0f9fb88aad48342c6","i-0fb85e3d354d10b7d"]
    for instance in EC2InstanceList:
        print(instance)
        execute_aws_cli_ec2_description(instance)




main()