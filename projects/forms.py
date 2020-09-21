from django import forms 
from influxdb_metrics.utils import query

# iterable 
QUERY_CHOICES =( 
	("select time, degrees as value from average_temperature", "Get average temperature"), 
	("select time, pH as value from h2o_pH", "Get water pH"), 
	("select time, degrees as value from h2o_temperature", "Get water temperature"),  
) 

# influx
infxtag = query("show tag values from h2o_pH with key=location")
taglist = list()
for series in infxtag.get_points(measurement='h2o_pH'):
    taglist.append(series['value'])

TAG_CHOICES =()
for k in range(0,len(taglist)):
    tag_tuple = (taglist[k], taglist[k])
    TAG_CHOICES = (tag_tuple,) + TAG_CHOICES


# creating a form 
class QueryForm(forms.Form): 
	get_query = forms.ChoiceField(choices = QUERY_CHOICES) 

class FilterForm(forms.Form):
    get_filter = forms.ChoiceField(choices = TAG_CHOICES)
