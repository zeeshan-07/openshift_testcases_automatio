import os
import sys
import requests


def create_serviceaccount_for_token():
    os.system('kubectl apply -f comman_yaml_files/serviceaccount api-service-account')
    os.system('kubectl apply -f comman_yaml_files/serviceaccount.yaml')
    os.system('kubectl apply -f comman_yaml_files/clusterrole.yaml')
    os.system('kubectl apply -f comman_yaml_files/clusterrole_binding.yaml')

def delete_serviceaccount_for_token():
    os.system('kubectl delete -f comman_yaml_files/serviceaccount api-service-account')
    os.system('kubectl delete -f comman_yaml_files/serviceaccount.yaml')
    os.system('kubectl delete -f comman_yaml_files/clusterrole.yaml')
    os.system('kubectl delete -f comman_yaml_files/clusterrole_binding.yaml')


def generate_token():
    os.system('APISERVER=$(kubectl config view --minify | grep server | cut -f 2- -d ":" | tr -d " ")')
    os.system("SECRET_NAME=$(kubectl get serviceaccount api-service-account -o jsonpath='{.secrets[0].name}')")
    os.system("TOKEN=$(kubectl describe secret $SECRET_NAME | grep -E '^token' | cut -f2 -d':' | tr -d " ")")
    os.system("SECRET_NAME=$(kubectl get serviceaccount api-service-account -o jsonpath='{.secrets[0].name}')")
    os.system("TOKEN=$(kubectl get secret $SECRET_NAME -o jsonpath='{.data.token}' | base64 --decode)")

