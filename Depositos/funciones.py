# -*- coding: utf-8 -*-

from django.db.models.query import QuerySet

def json(obj,fields=[]):
    if isinstance(obj,QuerySet):
        if fields==[]:
           return [dict(zip([f.name for f in o._meta.fields],[unicode(getattr(o,f.name)) for f in o._meta.fields])) for o in obj]
        return [dict(zip([f.name for f in fields],[unicode(getattr(o,f.name)) for f in fields])) for o in obj]
    else:
        if fields==[]:
           return dict(zip([f.name for f in obj._meta.fields],[unicode(getattr(obj,f.name)) for f in obj._meta.fields]))
        return dict(zip([f.name for f in fields],[unicode(getattr(obj,f.name)) for f in fields]))

def query(cls,request,queryDict):
    if 'rows' in request.GET:
        rows = int(request.GET['rows'])
        page = int(request.GET['page'])

    query = {}

    for key in queryDict.keys():
        if queryDict[key] in request.GET:
            query['%s__contains'%key] = request.GET[queryDict[key]]

    total = cls.objects.filter(**query).count()

    if 'rows' in request.GET:
        objs = cls.objects.filter(**query)[(page-1) * rows: page * rows]
    else:
        objs = cls.objects.filter(**query)
    return{'total': total, 'rows': json(objs)}



    # if request.GET.has_key('rows'):
    #     rows=int(request.GET['rows'])
    #     page=int(request.GET['page'])
    # query={}
    # for key in queryDict.keys():
    #     if request.GET.has_key(queryDict[key]):
    #         query['%s__contains'%key]=request.GET[queryDict[key]]
    # total=cls.objects.filter(**query).count()
    # if request.GET.has_key('rows'):
    #     objs=cls.objects.filter(**query)[(page-1)*rows:page*rows]
    # else:
    #     objs=cls.objects.filter(**query)
    # return {'total':total,'rows':json(objs)}



# $page = isset($_POST['page']) ? intval($_POST['page']) : 1;
# $rows = isset($_POST['rows']) ? intval($_POST['rows']) : 10;
# // ...
# $rs = mysql_query("select count(*) from item");
# $row = mysql_fetch_row($rs);
# $result["total"] = $row[0];
#
# $rs = mysql_query("select * from item limit $offset,$rows");
#
# $items = array();
# while($row = mysql_fetch_object($rs)){
#     array_push($items, $row);
# }
# $result["rows"] = $items;
#
# echo json_encode($result);