### Install Kubernetes Python Client:

`git clone --recursive https://github.com/kubernetes-client/python.git cd`

`cd python`

`python setup.py install`

### Installation from pip:

`pip install kubernetes`

For Nodes, we use CoreV1Api class from client module.

### Authentication to the Kubernetes Python Client in other cluster is done by: 

`configuration.api_key = {"authorization": "Bearer" + bearer_token}`

We will use here the Bearer Token which enable requests to authenticate using an access key.

In get_nodes.py file we have function for getting nodes:

1. Get Nodes (get_nodes)

Give your cluster details:
```
cluster_details={
        "bearer_token":"Your_cluster_bearer_token",
        "api_server_endpoint":"Your_cluster_IP"
    }
```

### Running the File:
```
python3 get_nodes.py
```
### Output:

In the output you will see list of nodes inside a cluster with labels in the following format:
```
[{'node':'<node_name>', 'labels':{'<list_of_labels>'}}]
```