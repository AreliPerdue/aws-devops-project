# AWS DevOps Project - VPC + EC2 + boto3

## Descripción
Este proyecto implementa una arquitectura en AWS con dos ambientes:
- Desarrollo (Development)
- Producción (Production)

Cada ambiente cuenta con:
- VPC independiente
- Subnet pública y privada
- EC2 pública (bastion host)
- EC2 privada (servicio interno)

## Arquitectura
Se aplicó segmentación de red utilizando VPC y subnets para mejorar la seguridad.

## Seguridad
- Uso de Security Groups
- Acceso SSH restringido
- Instancias privadas sin acceso a Internet
- Uso de bastion host

## Script en Python (boto3)
Se desarrolló un script que permite:
- Listar instancias EC2
- Iniciar instancias
- Detener instancias
- Reiniciar instancias

El script utiliza tags para identificar el ambiente:
- Environment = Development
- Environment = Production

## Tecnologías utilizadas
- AWS (EC2, VPC, Security Groups)
- Python (boto3)
- Git y GitHub

## Autor
Areli Perdue
