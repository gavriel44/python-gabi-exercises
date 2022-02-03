import psutil

def get_process_list():
    process_list = []

    for proc in psutil.process_iter():
        process_info_dict = proc.as_dict(attrs=['pid', 'name', 'cpu_percent'])

        process_list.append(process_info_dict)

    return process_list

