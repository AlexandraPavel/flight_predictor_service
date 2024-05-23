import pandas as pd

import warnings
from datetime import datetime, timedelta
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=UserWarning)
warnings.simplefilter(action='ignore', category=pd.errors.PerformanceWarning)

import numpy as np
from sklearn.model_selection import train_test_split
import pickle

class RandomForestRegression:
    def __init__(self):
        path_to_artifacts = "../../research/"
        m = open(path_to_artifacts + 'model_3.pkl','rb')
        self.model = pickle.load(m)

    def compute_prediction(self, input_data):
        try:
            # Read each CSV file and append its DataFrame to the list
            file_path = 'https://raw.githubusercontent.com/AlexandraPavel/PriceFlightEstimator/master/refined_dataset.csv'
            data_frames = pd.read_csv(file_path, skipinitialspace=True)
            train_data = data_frames.iloc[:, 1:]
            pd.set_option("display.max_columns",None)
            train_data.dropna(inplace=True)

            train_data["Flight_day"] =pd.to_datetime(train_data["flight_date"],format="%d/%m/%Y").dt.day
            train_data["Flight_month"] =pd.to_datetime(train_data["flight_date"],format="%d/%m/%Y").dt.month
            train_data["Flight_year"] =pd.to_datetime(train_data["flight_date"],format="%d/%m/%Y").dt.year

            train_data["Enquiry_day"] =pd.to_datetime(train_data["date_of_enquiry"],format="%d/%m/%Y").dt.day
            train_data["Enquiry_month"] =pd.to_datetime(train_data["date_of_enquiry"],format="%d/%m/%Y").dt.month

            enquiry_days_before = []
            enquiry_day = list(train_data["Enquiry_day"])
            enquiry_month = list(train_data["Enquiry_month"])
            flight_day = list(train_data["Flight_day"])
            flight_month = list(train_data["Flight_month"])

            for i in range(len(enquiry_day)):
                no_days = 0
                if enquiry_month[i] == flight_month[i]:
                    no_days = flight_day[i] - enquiry_day[i]
                else:
                    no_days = 31 - enquiry_day[i] + flight_day[i]

                enquiry_days_before.append(no_days)

            train_data["Enquiry_days_before"] = enquiry_days_before

            train_data.drop(["flight_date"], axis = 1, inplace = True)
            train_data.drop(["date_of_enquiry"], axis = 1, inplace = True)
            train_data.drop(["Enquiry_day"], axis = 1, inplace = True)
            train_data.drop(["Enquiry_month"], axis = 1, inplace = True)

            #Extracting Hours
            train_data["Dep_hour"] = pd.to_datetime(train_data["flight_time"],format="%H:%M").dt.hour

            # Extracting Minutes
            train_data["Dep_min"] = pd.to_datetime(train_data["flight_time"],format="%H:%M").dt.minute

            # Now we can drop Dep_Time as it of no use
            train_data.drop(["flight_time"], axis = 1, inplace = True)

            #Extracting Hours
            train_data["Arrival_hour"] = pd.to_datetime(train_data["arrival_time"],format="%H:%M").dt.hour

            # Extracting Minutes
            train_data["Arrival_min"] = pd.to_datetime(train_data["arrival_time"],format="%H:%M").dt.minute

            # Now we can drop Dep_Time as it of no use
            train_data.drop(["arrival_time"], axis = 1, inplace = True)

            Airline = train_data[["airline"]]
            Airline = pd.get_dummies(Airline)

            arl = sorted(list(train_data['airline'].unique()))

            Source =train_data[["departure"]]
            Source =pd.get_dummies(Source)

            src = sorted(list(train_data['departure'].unique()))

            Destination =train_data[["destination"]]
            Destination =pd.get_dummies(Destination)

            des = sorted(list(train_data['destination'].unique()))

            data_train =pd.concat([train_data,Airline,Source,Destination], axis=1)
            data_train.drop(["airline","departure", "destination"], axis=1, inplace=True)

            airline_dict = {}
            flight_durations = {}
            locations = ["Bucuresti", "Cluj", "Iasi", "Timisoara", "Sibiu", "Istanbul", "Londra", "Paris", "Amsterdam", "Madrid", "Frankfurt", "Barcelona", "Munich", "Roma", "Lisabona", "Dublin", "Viena", "Manchester", "Atena", "Zurich", "Oslo", "Copenhaga", "Milano", "Berlin", "Bruxelles"]
            for departure in locations[:3]:
                    for destination in locations[5:25]:
                        df1 = train_data[(train_data["departure"] == departure) & (train_data["destination"] == destination)]
                        if not df1.empty:
                            df1 = df1.sort_values(by=['price'])
                            l = df1["airline"].unique()
                            w = df1["flight_duration"].mean()
                            airline_dict[(departure, destination)] = l
                            flight_durations[(departure, destination)] = w

            for departure in locations[5:25]:
                    for destination in locations[:3]:
                        df1 = train_data[(train_data["departure"] == departure) & (train_data["destination"] == destination)]
                        if not df1.empty:
                            df1 = df1.sort_values(by=['price'])
                            l = df1["airline"].unique()
                            w = df1["flight_duration"].mean()
                            airline_dict[(departure, destination)] = l
                            flight_durations[(departure, destination)] = w

            X = data_train.loc[:, data_train.columns]
            X.drop(["price"], axis = 1, inplace = True)
            y = data_train['price']

            X_train, X_test_2, y_train, y_test_2 = train_test_split(X, y, test_size = 0.2, random_state=1234)
            test_data = pd.concat([pd.DataFrame(X_test_2), pd.DataFrame(pd.DataFrame(y_test_2), columns=['price'])], axis=1)
            X, y = X_train, y_train
            col_list = [col for col in X_test_2.columns]
            dataframe_logic = pd.DataFrame(columns=col_list)
            dataframe_return_logic = pd.DataFrame(columns=col_list)

            mean_array = [X_train[col].mean() for col in col_list]
            std_array = [X_train[col].std() for col in col_list]
            y_max = max(y_train)
            y_min = min(y_train)

            #print("Flight price predictor")
            #dep = input("From: ")
            #ds = input("To: ")
            #date1 = input("Departure date (DD-MM-YYYY): ")
            #date2 = input("Return date (DD-MM-YYYY): ")

            dep = input_data['departure']
            ds = input_data['destination']
            date1 = input_data['flight_date']
            date2 = input_data['arrival_date']

            d1 = datetime.strptime(date1, '%d-%m-%Y')
            d2 = datetime.strptime(date2, '%d-%m-%Y')

            f_d = int(date1[0:2])
            f_m = int(date1[3:5])
            f_y = int(date1[6:])
            flight_duration1 = int(flight_durations[(dep, ds)])
            flight_duration2 = int(flight_durations[(ds, dep)])

            a_d = int(date2[0:2])
            a_m = int(date2[3:5])
            a_y = int(date2[6:])

            airline_list = airline_dict[(dep, ds)][:5]
            airline_condition_1 = [arl.index(x) for x in airline_list]

            airline_list_2 = airline_dict[(ds, dep)][:5]
            airline_condition_2 = [arl.index(x) for x in airline_list_2]

            for layover in range(2):
                for enquiry_days_before in range(20):
                    for dep_hour in [7, 13, 19, 1]:
                            for i in airline_condition_1:
                                row = [0 for x in range(109)]
                                row[0] = layover
                                row[1] = flight_duration1
                                row[2] = f_d
                                row[3] = f_m 
                                row[4] = f_y
                                row[5] = enquiry_days_before    
                                row[6] = dep_hour
                                row[7] = 0
                                row[8] = int(dep_hour + flight_duration1 / 60) % 24
                                row[9] = flight_duration1 % 60
                                row[i + 10] = 1
                                for j in range(len(src)):
                                    if dep in src[j]:
                                        row[62 + j] = 1
                                for j in range(len(des)):
                                    if ds in des[j]:
                                        row[85 + j] = 1
                                dictionary = dict(zip(col_list, row))
                                df_dictionary = pd.DataFrame([dictionary])
                                dataframe_logic = pd.concat([dataframe_logic, df_dictionary], ignore_index=True)

            for layover in range(2):
                for enquiry_days_before in range(25):
                    for dep_hour in [7, 13, 19, 1]:
                            for i in airline_condition_2:
                                row = [0 for x in range(109)]
                                row[0] = layover
                                row[1] = flight_duration2
                                row[2] = a_d
                                row[3] = a_m 
                                row[4] = a_y
                                row[5] = enquiry_days_before    
                                row[6] = dep_hour
                                row[7] = 0
                                row[8] = int(dep_hour + flight_duration2 / 60) % 24
                                row[9] = int(flight_duration2 / 60)
                                row[i + 10] = 1
                                for j in range(len(src)):
                                    if ds in src[j]:
                                        row[62 + j] = 1
                                for j in range(len(des)):
                                    if dep in des[j]:
                                        row[85 + j] = 1
                                dictionary = dict(zip(col_list, row))
                                df_dictionary = pd.DataFrame([dictionary])
                                dataframe_return_logic = pd.concat([dataframe_return_logic, df_dictionary], ignore_index=True)

            dataframe_logic["bias"] = np.ones(shape=(dataframe_logic.shape[0], 1))
            counter = 0
            for col in col_list:
                dataframe_logic[col] = (dataframe_logic[col] - mean_array[counter]) / std_array[counter]
                counter += 1
            y_prediction = self.model.predict(dataframe_logic)
            counter = 0
            for col in col_list:
                dataframe_logic[col] = dataframe_logic[col] * std_array[counter] + mean_array[counter]
                counter += 1
            y_prediction = y_prediction * (y_max - y_min) + y_min
            dataframe_logic["price"] = y_prediction




            dataframe_return_logic["bias"] = np.ones(shape=(dataframe_return_logic.shape[0], 1))
            counter2 = 0
            for col in col_list:
                dataframe_return_logic[col] = (dataframe_return_logic[col] - mean_array[counter2]) / std_array[counter2]
                counter2 += 1
            y_return_prediction = self.model.predict(dataframe_return_logic)
            y_return_prediction = y_return_prediction * (y_max - y_min) + y_min
            counter2 = 0
            for col in col_list:
                dataframe_return_logic[col] = dataframe_return_logic[col] * std_array[counter2] +  mean_array[counter2]
                counter2 += 1
            dataframe_return_logic["price"] = y_return_prediction


            dataframe_logic = dataframe_logic.sort_values(by=['price'])
            dataframe_return_logic = dataframe_return_logic.sort_values(by=['price'])

            time_day_dict = {7:"morning", 13:"day", 19:"evening", 1:"night"}

            #print("Our prediction suggest that the best day to purchase a ticket for the " + dep + "-" + ds + " flight would be " + str(int(dataframe_logic.iloc[0]["Enquiry_days_before"])) + " days before the flight, on " + (d1 - timedelta(days = dataframe_logic.iloc[0]["Enquiry_days_before"])).strftime('%d %B %Y'))
            #print("Based on our data, you should be considering " + time_day_dict[dataframe_logic.iloc[0]["Dep_hour"]] + " flights, with " + str(int(dataframe_logic.iloc[0]["layovers"])) + " layovers, from the " + arl[list(dataframe_logic.iloc[0])[10:61].index(1) + 1] + " airline.")
            #print("You should expect to pay around " + str(int(dataframe_logic.iloc[0]["price"])) + " euros.")
            #print("")
            #print("As per the return flight, we suggest that the best day to purchase a ticket would be " + str(int(dataframe_return_logic.iloc[0]["Enquiry_days_before"])) + " days before the flight, on " + (d2 - timedelta(days = dataframe_return_logic.iloc[0]["Enquiry_days_before"])).strftime('%d %B %Y'))
            #print("For this one, you should be considering " + time_day_dict[dataframe_return_logic.iloc[0]["Dep_hour"]] + " flights, with " + str(int(dataframe_return_logic.iloc[0]["layovers"])) + " layovers, from the " + arl[list(dataframe_return_logic.iloc[0])[10:61].index(1) + 1]  + " airline.")
            #print("You may be paying around " + str(int(dataframe_return_logic.iloc[0]["price"])) + " euros.")
            #print("")

            p1 = "Our prediction suggest that the best day to purchase a ticket for the " + dep + "-" + ds + " flight would be " + str(int(dataframe_logic.iloc[0]["Enquiry_days_before"])) + " days before the flight, on " + (d1 - timedelta(days = dataframe_logic.iloc[0]["Enquiry_days_before"])).strftime('%d %B %Y')
            p2 = "Based on our data, you should be considering " + time_day_dict[dataframe_logic.iloc[0]["Dep_hour"]] + " flights, with " + str(int(dataframe_logic.iloc[0]["layovers"])) + " layovers, from the " + arl[list(dataframe_logic.iloc[0])[10:61].index(1) + 1] + " airline."
            p3 = "You should expect to pay around " + str(int(dataframe_logic.iloc[0]["price"])) + " euros."
            p4 = "As per the return flight, we suggest that the best day to purchase a ticket would be " + str(int(dataframe_return_logic.iloc[0]["Enquiry_days_before"])) + " days before the flight, on " + (d2 - timedelta(days = dataframe_return_logic.iloc[0]["Enquiry_days_before"])).strftime('%d %B %Y')
            p5 = "For this one, you should be considering " + time_day_dict[dataframe_return_logic.iloc[0]["Dep_hour"]] + " flights, with " + str(int(dataframe_return_logic.iloc[0]["layovers"])) + " layovers, from the " + arl[list(dataframe_return_logic.iloc[0])[10:61].index(1) + 1]  + " airline."
            p6 = "You may be paying around " + str(int(dataframe_return_logic.iloc[0]["price"])) + " euros."
            
            days_diff = (d2 - d1).days
            elem_found = 0
            for i in range(len(dataframe_logic)):
                day_list = list(dataframe_logic.iloc[:(i+1)]["Enquiry_days_before"])
                return_day_list = list(dataframe_return_logic.iloc[:(i+1)]["Enquiry_days_before"])
                min_inq = min(day_list)
                max_ret_inq = max(return_day_list)
                if (max_ret_inq - min_inq) > days_diff:
                    for elem in day_list:
                        if int(int(elem) + days_diff) in return_day_list:
                            elem_found = 1
                            p7 = "We believe the best day for purchasing both of the tickets would be: " + (d1 - timedelta(days = elem)).strftime('%d %B %Y')
                            break
                if elem_found == 1:
                    break
            if elem_found == 0:
                p7 = "We believe the best day for purchasing both of the tickets would be: " + (d1 - timedelta(days=dataframe_logic.iloc[:1]["Enquiry_days_before"])).strftime('%d %B %Y')
            return {"status": "OK" , "dep_date": p1, "dep_info" : p2, "dep_price": p3, "ret_date": p4, "ret_info": p5, "ret_price": p6, "both_date": p7}        
        
        except Exception as e:
            return {"status": "Error", "message": str(e)}

        #return prediction
