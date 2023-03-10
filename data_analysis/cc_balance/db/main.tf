module "db" {
  source = "github.com/glinerosuarez/tf-utils/postgreSQL"

  init_queries_path = "./queries"
}