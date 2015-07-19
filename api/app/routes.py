import os
from api import app
from utils import redis_get_domains, redis_insert_domain, get_template
from flask import jsonify, request, render_template

@app.route('/')
def index():
    return "Private API for Marvelous\n"
@app.route('/domains')
def get_domains():
    return jsonify(domains=redis_get_domains())
@app.route('/domain/<domain>')
def exist_domain(domain):
    return jsonify(result = domain in redis_get_domains())
@app.route('/domain/<domain>', methods=['PUT'])
def insert_domain(domain):
    if redis_insert_domain(domain):
        return "Inserted domain: %s" % domain
    else:
        return "Could not insert domain: %s" % domain
@app.route('/register_domain/<domain>', methods=['POST','OPTIONS'])
def register_template(domain):
    import json
    VALID_KEYS = app.config['VALID_KEYS']
    TEMPLATE_DIRECTORY = app.config['TEMPLATE_DIRECTORY']
    VALID_TEMPLATES = app.config['VALID_TEMPLATES']

    business_info = request.get_json() if request.get_json() != None else request.form
    
    if business_info == None:
        return "JSON with keys: [%s] needed\n" % (' '.join(VALID_KEYS))
    for key in VALID_KEYS:
        print key, 
        if key not in business_info:
            return "JSON with keys: [%s] needed\n" % (' '.join([_ for _ in VALID_KEYS if _ not in business_info]))
    if business_info['template'] not in VALID_TEMPLATES:
        return "Valid Templates: [%s] Received: [%s]\n" % (' '.join(VALID_TEMPLATES), business_info['template'])        
    if redis_insert_domain(domain):
        
        template = render_template(business_info['template'] + '.html', info=business_info)
        print template
        path = "%s/%s" % (TEMPLATE_DIRECTORY, domain)
        index  = "%s/index.html" % (path)
        print index
        try:
            os.makedirs(path)
        except OSError as e:
            raise OSError("Directory %s already exists." % path)
        else:
            with open(index, 'w') as f:
                f.write(unicode(template.encode('utf8'), errors='ignore'))
        return "Domain %s created\n" % domain
    else:
        return "Domain %s already exists\n" % domain
