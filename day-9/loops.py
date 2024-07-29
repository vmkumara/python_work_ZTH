### 1)
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
  print(fruit)




### 2)
count = 60
while count > 50:
  print(count)
  count -= 2




### 3)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for n in numbers:
  if n == 9:
    break
  print(n)




### 4) 
sequence = [2, 5, 8, 1,4, 7, 3,6, 9, 159]
for s in sequence:
  if s == 4:
    continue
  print(s)




### 5)
log_file = [
   "INFO: Operation successful",
   "ERROR: File not found",
   "DEBUG: Connection established",
   "ERROR: Database connection failed",
]

for line in log_file:
  if "ERROR" in line:
    print(line)

for l in log_file:
  if "DEBUG" in l:
    print(l)





### 6) a)Server Provisioning and Configuration
servers=("server1" "server2" "server3")
for server in "${servers[@]}"; do
    configure_monitoring_agent "$server"
done


# b)Deploying Configurations to Multiple Environments:
environments=("dev" "staging" "prod")
for env in "${environments[@]}"; do
    deploy_configuration "$env"
done


# c)Backup and Restore Operations:
databases=("db1" "db2" "db3")
for db in "${databases[@]}"; do
    create_backup "$db"
done


# d)Log Rotation and Cleanup:
log_files=("app.log" "access.log" "error.log")
for log_file in "${log_files[@]}"; do
    rotate_and_cleanup_logs "$log_file"
done


# e)Monitoring and Reporting:
servers=("server1" "server2" "server3")
for server in "${servers[@]}"; do
    check_resource_utilization "$server"
done


# f)Managing Cloud Resources:
instances=("instance1" "instance2" "instance3")
for instance in "${instances[@]}"; do
    resize_instance "$instance"
done





### 7) a)Continuous Integration/Continuous Deployment (CI/CD) Pipeline:
while kubectl get deployment/myapp | grep -q 0/1; do
    echo "Waiting for myapp to be ready..."
    sleep 10
done


# b) Provisioning and Scaling Cloud Resources:
while ! aws ec2 describe-instance-status --instance-ids i-1234567890abcdef0 | grep -q "running"; do
    echo "Waiting for the EC2 instance to be running..."
    sleep 10
done


# c)Log Analysis and Alerting:
while true; do
    if tail -n 1 /var/log/app.log | grep -q "ERROR"; then
        send_alert "Error detected in the log."
    fi
    sleep 5
done


# d)Database Replication and Data Synchronization:
while true; do
    replication_lag=$(mysql -e "SHOW SLAVE STATUS\G" | grep "Seconds_Behind_Master" | awk '{print $2}')
    if [ "$replication_lag" -gt 60 ]; then
        trigger_data_sync
    fi
    sleep 60
done


# e)Service Health Monitoring and Auto-Recovery:
while true; do
    if ! check_service_health; then
        restart_service
    fi
    sleep 30
done
