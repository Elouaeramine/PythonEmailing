msg_template = """Hello {name},
If you're getting this email it's because I'm trying to make 
a python script to automate mailing tasks etc 
Mahdi ben zinouba {tahhan} kbir 
""" 

def format_msg(my_name="Amine", tahhan= "tahhan"):
    my_msg = msg_template.format(name=my_name, tahhan = tahhan)
    return my_msg