#Selenium opens a headless browser. I am using firefox.
from selenium import webdriver
driver = webdriver.Firefox() 


#define the time range
study_period = []
 def add_day_to_month(year,month,day):
    this_period = "2018" +"-"+ str(month)+ "-" + str(day)
    study_period.append(this_period)
for month in range(1,13):
    for day in range(1,32):
        add_day_to_month("2018",month,day)
print(study_period)
#remove the impossible dates
indexes = [59,60,61,123,185,278, 340]
for index in sorted(indexes, reverse=True):
    del study_period[index]
    



collected_temperature_data = [] #temp data will be save in this 
stations = ['STATION1'] #save the names of the stations inside this file

for station in stations:
 for time in study_period:
    driver.get("https://www.wunderground.com/history/daily/us/mi/kalamazoo/" + station+ "/date/" + time)
    elem = driver.find_element_by_class_name("summary-table") 
    data = elem.text
    data_lines = data.split("\n")
    print(data_lines)
    
    for line in data_lines:
        data_lines = line.split(" ")
        if data_lines[0] == "High":
            data_title = " ".join(data_lines[:2])
            sep = ","
            temp_data = sep.join(data_lines[2:])
            line_data = time+sep+data_title+sep+temp_data                
            collected_temperature_data.append(line_data)

            print(collected_temperature_data)

          
          
          
          
#save the scrapped data
write_file = "TempOutput.csv"
with open(write_file, "w") as output:
    for line in collected_temperature_data:
        output.write(line + '\n')
