terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.21.0"
    }
  }
}

provider "google" {
  credentials = "./keys/creedentials.json"
  project     = "dezoomcampproject"
  region      = "us-central1"

}

resource "google_storage_bucket" "deproject-bucket" {
  name          = "dezoomcampproject-terra-bucket"
  location      = "US"
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}

resource "google_bigquery_dataset" "project_dataset" {
  dataset_id = "project_dataset"

}  