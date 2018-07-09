import json, requests, calendar, web
from datetime import date

render = web.template.render('templates/')


urls = (
    '/', 'index'
)

class index:
    def GET(self):
        return render.index(forecast())
        #return forecast()



def forecast():


  #Get Forecast Data
  url = "http://api.weather.gov/gridpoints/TOP/95,28/forecast"
  r = requests.get(url)
  #Data as Dictionary
  dct = r.json()
  
  #Decalre Variables
  pre_forecast = dict()
  forecast = dict()
  
  
  #Get Day and forcast details from dataset
  for x in range (0, 13):
    pre_forecast[x] = dct["properties"]["periods"][x]["name"],dct["properties"]["periods"][x]["detailedForecast"]
    
  #Get Tomorrow in Day English Format for editing use
  my_date = date.today()
  if my_date.weekday() >=6:
    tomorrow='Monday'
  else:
    tomorrow = calendar.day_name[my_date.weekday()+1]
  
  #Editing Day/Forceast Details
  for x in range (0, 13):
    days = pre_forecast[x]
    
    #get forcast details into list by scentances
    detail = days[1]
    detail = detail.strip('.')
    details = detail.split('.')
    
    #Get number of elements
    elements = len(details)-1
    if elements == 0:
      elements = elements +1
    
    
    #Replaceing/Changing forcast details
    for y in range (0, elements):
      details[y] = details[y].replace(' near', '')
      details[y] = details[y].replace(' around', '')
      details[y] = details[y].replace(', with a ','...the ')
      details[y] = details[y].replace('Mostly cloudy','Overcast')
      #details[x] = details[x].replace('','')
      

    
    
    #Day Formatting
    day = days[0]
    day = day.replace(tomorrow,'Tomorrow')
    #day = day.replace('','')
    
    #Put data into data structure
    
    
    #Print on Console 
    #print day
    #print details[0]+'.'
    
    
    forecast[x] = day,[details[0]+'.']
    
  for x in range(0, 13):
    day = forecast[x]
    detail = day[1]
    print day[0]
    print detail[0]
    
  return forecast
#Boiler Plate Default Main / web app
#if __name__ == '__main__':
#  main()


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
    

