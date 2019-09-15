import boto3

ec2 = boto3.client('ec2')
response = ec2.describe_instances()
for Reservations in response['Reservations']:
    for Instances in Reservations['Instances']:
        if 'PublicIpAddress' in Instances:
            for security_group in Instances['SecurityGroups']:
                sgs=ec2.describe_security_groups(GroupIds=['{0}'.format(security_group['GroupId'])])
                for sg in sgs['SecurityGroups']:
                    inbound = sg['IpPermissions']
                    for i in range(len(sg['IpPermissions'])):
                        for j in range(len(sg['IpPermissions'][i]['IpRanges'])):
                            try:
                                if sg['IpPermissions'][i]['IpRanges'][j]['CidrIp'] == '0.0.0.0/0':
                                    print('Instance Id - {0}'.format(Instances['InstanceId']))
                                    print('Public Ip - {0}'.format(Instances['PublicIpAddress']))
                                    print('GroupName - {0}'.format(security_group['GroupId']))
                                    print(sg['IpPermissions'][i]['IpProtocol'],sg['IpPermissions'][i]['FromPort'])
                                    print('')
                            except:
                                print('something')
rds = boto3.client("rds")
rd = rds.describe_db_instances()
if 'DBInstances' in rd:
    for rds in rd['DBInstances']:
        if rds['PubliclyAccessible'] is True:
            print('RDS Name -{0}'.format(rds['DBInstanceIdentifier']))
            print('RDS Address -{0}'.format(rds['Endpoint']['Address']))
            print('RDS Port -{0}'.format(rds['Endpoint']['Port']))
            print('')

elb = boto3.client("elb")
load_balancers = elb.describe_load_balancers()
if 'LoadBalancerDescriptions' in load_balancers:
    for load_balncer in load_balancers['LoadBalancerDescriptions']:
        if load_balncer['Scheme'] == 'internet-facing':
            print("LoadBalancerName: - {0}".format(load_balncer['LoadBalancerName']))
            print("ELB Info: - {0}".format(load_balncer['DNSName']))
            
