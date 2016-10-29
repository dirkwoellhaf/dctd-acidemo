#!/usr/bin/env python
# -*- coding: UTF-8 -*-# enable debugging
import cgitb
import cgi
import random
cgitb.enable()
form = cgi.FieldStorage()
action = form.getfirst("action", "")

print "Content-Type: text/html;charset=utf-8"

def tenant_health(health_score):
    #health_score=50
    if health_score >=80:
        health_label = '<span class="label label-success">'+str(health_score)+'</span>'

    if health_score <80:
        health_label = '<span class="label label-warning">'+str(health_score)+'</span>'

    if health_score <50:
        health_label = '<span class="label label-danger">'+str(health_score)+'</span>'

    return health_label

def tenant_tile(tenant_name):
    health_score = random.randint(1, 100)

    print '''
     <div class="col-sm-6 col-md-4">
        <div class="thumbnail">
          <div class="caption">
            <h1>Tenant: DCTD-'''+tenant_name+'''</h1>
            <p>Health '''+tenant_health(health_score)+'''&nbsp;VRFs: <span class="label label-default">-</span></p>
            <p>BDs: <span class="label label-default">-</span>&nbsp;EPGs: <span class="label label-default">-</span></p>
            <p></br><a href="#" class="btn btn-primary" role="button">Modify</a></p>
          </div>
        </div>
      </div>
    '''
def tenant_add():


    print '''
    <form action="test.py?action=tenant_add" method="post">
    <div class="panel panel-default">
        <div class="panel-heading">
            <h3 class="panel-title">Add Tenant</h3>
        </div>
        <div class="panel-body">
            <div class="input-group">
                <span class="input-group-addon" id="basic-addon1">Name</span>
                <input type="text" class="form-control" placeholder="Tenant Name" name="tenant_name" aria-describedby="basic-addon1">
            </div></br>
            <div class="input-group">
                <span class="input-group-addon" id="basic-addon1">VRF</span>
                <input type="text" class="form-control" placeholder="VRF Name" name="tenant_vrf" aria-describedby="basic-addon1">
            </div>
            </br>
            <input type="hidden" name="tenant_add_state" value="create">
            <p><input type="submit" class="btn btn-primary" value="Add" /></p>
        </div>
    </div>
    </form>
    '''
    if form.getvalue("tenant_add_state") == "create" and form.getvalue("tenant_name") is not None and form.getvalue("tenant_vrf") is not None:
        tenant_name = "DCTD-"+form.getvalue("tenant_name")
        tenant_vrf = "DCTD-"+form.getvalue("tenant_vrf")
        print '''</br><div class="alert alert-success" role="alert">Tenant '''+tenant_name+''' created.</div>'''
    if form.getvalue("tenant_add_state") == "create" and form.getvalue("tenant_name") is None and form.getvalue("tenant_vrf") is None:
        print '''</br><div class="alert alert-danger" role="alert">Upps...Something went wrong!</div>'''

def snapshot_create():
    print '''</br><div class="alert alert-success" role="alert">Snapshot created.</div>'''

#-------------------------------------------------------------------------------
print '''
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="../../favicon.ico">

    <title>Starter Template for Bootstrap</title>

    <!-- Bootstrap core CSS -->
    <link href="css/bootstrap.min.css" rel="stylesheet">

  </head>

  <body>

    <nav class="navbar navbar-inverse navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="#">DC Techdays - ACI Demo</a>
        </div>
        <div id="navbar" class="collapse navbar-collapse">
          <ul class="nav navbar-nav">
            <li class="active"><a href="?">Home</a></li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </nav>

    <div class="container">
    </br>
    </br>
    </br>
    </br>
      <div class="panel panel-default">
      <div class="panel-heading">
        <h3 class="panel-title">Actions</h3>
      </div>
      <div class="panel-body">
        <p><a href="?action=snapshot" class="btn btn-primary" role="button">Create Snapshot</a>&nbsp;<a href="?action=tenant_add" class="btn btn-primary" role="button">Add Tenant</a></p>
      </div>
    </div>
    <div class="row">
      '''




if action == "snapshot" or action =="tenant_add":
    #print action

    if action == "tenant_add":
        tenant_add()
    if action == "snapshot":
        snapshot_create()

else:
    count = 1
    while count <= 10:
        tenant_tile(str(count))
        count = count + 1

print '''
    </div><!-- /.container -->


    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
  </body>
</html>'''
