terraform {
  required_version = "1.3.7"
}

provider "google" {
  project     = var.project_id
  region      = var.region_central
  zone        = var.zone_central
  credentials = file("${path.cwd}/secrets_key.json")
}

resource "google_storage_bucket" "i4sea_bucket" {
  name     = "i4sea-bucket"
  location = "US"
}
