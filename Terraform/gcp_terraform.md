In the IAM & Admin section of mine Google Cloud, I created a service account and gived Storage Admin, BigQuery Admin and Compute Admin permissions.


![](https://github.com/antfneves/spotify_top_songs_project/blob/main/Terraform/create_service_account.jpg?raw=true)


Then I generated a new JSON key.


![](https://github.com/antfneves/spotify_top_songs_project/blob/main/Terraform/create_new_key.jpg?raw=true)


Created a main.tf file using the name of my Project ID, Region and the path to my credentials and defined the name of the Google Storage Bucket that i wanted to create.   

Applied the following commands to plan the creation of the GCP Infrastructure:
```
terraform init

terraform plan

terraform apply

```
