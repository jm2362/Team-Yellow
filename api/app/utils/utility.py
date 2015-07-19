TEMPLATE_DIRECTORY = '/home/sangm/ares.sangm.net/api/api/Templates'

def get_template(business_info):
    template = '%s/%s.html' % (TEMPLATE_DIRECTORY, business_info['template'])
    print template
    try:
        f = open(template, 'r')
    except IOError:
        raise IOError("Template does not exist")
    else:
        with f:
            print f.readlines()
    return business_info
