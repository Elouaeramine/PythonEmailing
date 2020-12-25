msg_template = """Hello {name},
If you're getting this email it's because I'm trying to make 
a python script to automate mailing tasks etc 
""" 

def format_msg(my_name="Amine"):
    my_msg = msg_template.format(name=my_name)
    return my_msg