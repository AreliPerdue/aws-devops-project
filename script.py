import boto3

ec2 = boto3.client('ec2')

def listar_instancias():
    response = ec2.describe_instances()

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            print("Nombre:", [tag['Value'] for tag in instance.get('Tags', []) if tag['Key'] == 'Name'])
            print("ID:", instance['InstanceId'])
            print("Estado:", instance['State']['Name'])
            print("IP Privada:", instance.get('PrivateIpAddress'))
            print("IP Pública:", instance.get('PublicIpAddress'))
            print("------------------------")

listar_instancias()
