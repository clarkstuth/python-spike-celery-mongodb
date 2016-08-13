name "rabbitmq_and_mongodb"

default_attributes 'rabbitmq' => { 'loopback_users' => [] }


run_list 'recipe[mongodb]', 'recipe[rabbitmq::mgmt_console]'