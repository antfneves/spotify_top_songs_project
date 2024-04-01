1) In the IAM & Admin section of mine Google Cloud, I created a service account, and I gave Storage Admin, BigQuery Admin and Compute Admin permissions.


![](https://github.com/antfneves/spotify_top_songs_project/blob/main/Terraform/create_service_account.jpg?raw=true)


2) Then I generated a new JSON key.


![](https://github.com/antfneves/spotify_top_songs_project/blob/main/Terraform/create_new_key.jpg?raw=true)

3) Created the [main.tf](https://github.com/antfneves/spotify_top_songs_project/blob/main/Terraform/main.tf) file using the name of my Project ID, Region and the path to my credentials and defined the name of the Google Storage Bucket that i wanted to create.   


4) Applied the following commands to plan the creation of the GCP Infrastructure:
- Initialization
```
terraform init
```
- Planning
```
terraform plan
```
- Applying
```
terraform apply
```
5) Checked the Google Cloud Storage to see if the bucket was created.

![](https://github.com/antfneves/spotify_top_songs_project/blob/main/Terraform/gcs_bucket.jpg?raw=true)
     
