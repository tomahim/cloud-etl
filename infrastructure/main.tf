terraform {
 required_providers {
   aws = {
     source = "hashicorp/aws"
   }
 }
}

provider "aws" {
  region = "eu-west-3"
  shared_credentials_files = ["$HOME/.aws/credentials"]
}

resource "aws_dynamodb_table" "scrapped_data" {
 name = "scrapped-data"
 billing_mode = "PROVISIONED"
 read_capacity= "30"
 write_capacity= "30"
 attribute {
  name = "id"
  type = "S"
 }
 hash_key = "id"
}