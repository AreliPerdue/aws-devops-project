import boto3

ALUMNO = "Areli Perdue"
MATRICULA = "AL03072223"
ENVIRONMENT = input("Selecciona ambiente (Development/Production): ")  

ec2 = boto3.client('ec2')


def obtener_instancias():
    response = ec2.describe_instances()

    instancias = []

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:

            tags = {tag['Key']: tag['Value'] for tag in instance.get('Tags', [])}

            if tags.get('Environment') == ENVIRONMENT:

                instancias.append({
                    "Name": tags.get("Name", "N/A"),
                    "Id": instance['InstanceId'],
                    "State": instance['State']['Name'],
                    "PrivateIP": instance.get('PrivateIpAddress', 'N/A'),
                    "PublicIP": instance.get('PublicIpAddress', 'N/A')
                })

    return instancias


def listar_instancias():
    instancias = obtener_instancias()

    if not instancias:
        print("No hay instancias en este ambiente")
        return

    for i, inst in enumerate(instancias):
        print(f"""
[{i}]
Nombre: {inst['Name']}
ID: {inst['Id']}
Estado: {inst['State']}
IP Privada: {inst['PrivateIP']}
IP Pública: {inst['PublicIP']}
--------------------------
""")


def iniciar_instancia():
    listar_instancias()
    idx = int(input("Selecciona el número de instancia: "))
    instancias = obtener_instancias()

    ec2.start_instances(InstanceIds=[instancias[idx]['Id']])
    print("Instancia iniciándose...")


def detener_instancia():
    listar_instancias()
    idx = int(input("Selecciona el número de instancia: "))
    instancias = obtener_instancias()

    ec2.stop_instances(InstanceIds=[instancias[idx]['Id']])
    print("Instancia deteniéndose...")


def reiniciar_instancia():
    listar_instancias()
    idx = int(input("Selecciona el número de instancia: "))
    instancias = obtener_instancias()

    ec2.reboot_instances(InstanceIds=[instancias[idx]['Id']])
    print("Instancia reiniciándose...")


def menu():
    while True:
        print(f"""
========================================
Alumno: {ALUMNO}
Matrícula: {MATRICULA}
Ambiente: {ENVIRONMENT}
========================================
1. Listar instancias
2. Iniciar instancia
3. Detener instancia
4. Reiniciar instancia
5. Salir
========================================
""")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            listar_instancias()
        elif opcion == "2":
            iniciar_instancia()
        elif opcion == "3":
            detener_instancia()
        elif opcion == "4":
            reiniciar_instancia()
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción inválida")


menu()
