from flask_table import Table,Col


class user_logs(Table):
    timestamp=Col('Time')
    type=Col('Type of Activity')

class user_activity(Table):
    event=Col('Type of event')
    count=Col('Number of times it occured')
    timestamp=Col('Last it occured on')


