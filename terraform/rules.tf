resource "google_storage_bucket_access_control" "public_rule" {
  bucket = google_storage_bucket.i4sea_bucket.name
  role   = "READER"
  entity = "allUsers"
}
