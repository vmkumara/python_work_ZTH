student_info = {
   "name": "ramu",
    "age": "15",
   "section": "10",
    "school": "pratibha_school"
}
print(student_info["name"])


ec2_instance_info = [
    {
        "id": "instance-001",
        "type": "t2.micro"
    },
    {
        "id": "instance-002",
        "type": "t2.medium"
    },
    {
        "id": "instance-003",
       "type": "t3.medium"
    }
]
print(ec2_instance_info[0]["id"])


import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

complete_detail = response.json()

for i in range(len(complete_detail)):
    print(complete_detail[i]["user"]["login"])

