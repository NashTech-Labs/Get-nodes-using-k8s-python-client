from kubernetes import client, config
from kubernetes import client
from kubernetes.client import ApiClient
import json
from kubernetes.client.rest import ApiException


def __get_kubernetes_client(bearer_token,api_server_endpoint):
    try:
        configuration = client.Configuration()
        configuration.host = api_server_endpoint
        configuration.verify_ssl = False
        configuration.api_key = {"authorization": "Bearer " + bearer_token}
        client.Configuration.set_default(configuration)
        client_api = client.CoreV1Api()
        return client_api
    except Exception as e:
        print("Error getting kubernetes client \n{}".format(e))
        return None

def __format_data_for_nodes(client_output):
        temp_dict={}
        temp_list=[]
        
        json_data=ApiClient().sanitize_for_serialization(client_output)
        #print("JSON_DATA OF KUBERNETES OBJECT:{}".format(json_data))
        if len(json_data["items"]) != 0:
            for node in json_data["items"]:
                temp_dict={
                    "node": node["metadata"]["name"],
                    "labels": node["metadata"]["labels"],
                }
                temp_list.append(temp_dict)
        return temp_list

def get_nodes(cluster_details, namespace="default",all_namespaces=False):
        client_api= __get_kubernetes_client(
            bearer_token=cluster_details["bearer_token"],
            api_server_endpoint=cluster_details["api_server_endpoint"],
        )
       
        node_list = client_api.list_node()
        data=__format_data_for_nodes(node_list)
        print (data)


if __name__ == "__main__":
    cluster_details={
        "bearer_token":"<your_bearer_token>",
        "api_server_endpoint":"<your_server_end_point>"

    }

    
get_nodes(cluster_details)
