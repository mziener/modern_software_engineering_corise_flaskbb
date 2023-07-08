terraform {
  backend "s3" {
    bucket = "terraform-state-flaskbb-mziener" 
    key    = "core/terraform.tfstate"
    region = "eu-north-1"
  }
}
