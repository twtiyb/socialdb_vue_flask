class MongoDBConfig:
    g_server_ip = '127.0.0.1'	#mongodb数据库地址
    g_server_port = 32768		#数据库端口
    g_db_name = 'socialdb'  		#数据库名
    error_line_file = "error_log"
    ALLOWED_EXTENSIONS = ['txt', 'csv'] #允许上传的类型