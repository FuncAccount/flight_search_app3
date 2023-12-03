import requests
import json
from prettytable import PrettyTable
import pandas as pd
import time
import streamlit as st
import logging
import random
# Configure logging (this is a basic configuration; it can be customized)
logging.basicConfig(level=logging.ERROR)

st.set_page_config(layout="wide")

pd.set_option('display.max_rows', None)
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
        "Content-Type": "application/json"  # 声明文本类型为 json 格式
        # 'Cookie': 'your_cookie_here'  # Optional: Include if needed
    }

    # Assuming 'city' dictionary contains mappings of city names to their codes
city = {
    '上海': 'SHA',
    '北京': 'BJS',
    '广州': 'CAN',
    '深圳': 'SZX',
    '重庆': 'CKG',
    '天津': 'TSN',
    '成都': 'CTU',
    '武汉': 'WUH',
    '杭州': 'HGH',
    '南京': 'NKG',
    '西安': 'SIA',
    '郑州': 'CGO',
    '长沙': 'CSX',
    '青岛': 'TAO',
    '大连': 'DLC',
    '沈阳': 'SHE',
    '济南': 'TNA',
    '宁波': 'NGB',
    '厦门': 'XMN',
    '长春': 'CGQ',
    '昆明': 'KMG',
    '南宁': 'NNG',
    '合肥': 'HFE',
    '呼和浩特': 'HET',
    '哈尔滨': 'HRB',
    '太原': 'TYN',
    '兰州': 'LHW',
    '福州': 'FOC',
    '海口': 'HAK',
    '贵阳': 'KWE',
    '南昌': 'KHN',
    '乌鲁木齐': 'URC',
    '克拉玛依': 'KRY',
    '丽江': 'LJG',
    '哈密': 'HMI',
    '拉萨': 'LXA',
    '银川': 'INC',
    '西宁': 'XNN',
    '兰州': 'LHW',
    '乌鲁木齐': 'URC',
    '临沂': 'LYI',
    '东营': 'DOY',
    '威海': 'WEH',
    '泉州': 'JJN',
    '洛阳': 'LYA',
    '昭通': 'ZAT',
    '吉安': 'KNC',
    '营口': 'YKH',
    '曲靖': 'JUZ',
    '通化': 'TNH',
    '无锡': 'WUX'
# '上海': 'SHA',
#     '北京': 'BJS',
#     '广州': 'CAN',
#     '深圳': 'SZX',
#     '重庆': 'CKG',
#     '天津': 'TSN',
#     '成都': 'CTU',
#     '武汉': 'WUH',
#     '杭州': 'HGH',
#     '南京': 'NKG',
#     '西安': 'SIA',
#     '郑州': 'CGO',
#     '长沙': 'CSX',
#     '青岛': 'TAO',
#     '大连': 'DLC',
#     '沈阳': 'SHE',
#     '济南': 'TNA',
#     '宁波': 'NGB',
#     '厦门': 'XMN',
#     '长春': 'CGQ',
#     '昆明': 'KMG',
#     '南宁': 'NNG',
#     '合肥': 'HFE',
#     '呼和浩特': 'HET',
#     '哈尔滨': 'HRB',
#     '太原': 'TYN',
#     '兰州': 'LHW',
#     '福州': 'FOC',
#     '海口': 'HAK',
#     '贵阳': 'KWE',
#     '南昌': 'KHN',
#     '乌鲁木齐': 'URC',
#     '克拉玛依': 'KRY',
#     '丽江': 'LJG',
#     '哈密': 'HMI',
#     '拉萨': 'LXA',
#     '银川': 'INC',
#     '西宁': 'XNN',
#     '兰州': 'LHW',
#     '乌鲁木齐': 'URC',
#     '临沂': 'LYI',
#     '东营': 'DOY',
#     '威海': 'WEH',
#     '泉州': 'JJN',
#     '洛阳': 'LYA',
#     '昭通': 'ZAT',
#     '吉安': 'KNC',
#     '营口': 'YKH',
#     '曲靖': 'JUZ',
#     '通化': 'TNH',
#     '常州': 'CZX',
#     '徐州': 'XUZ',
#     '拉萨': 'LXA',
#     '邢台': 'XNT',
#     '莆田': 'FUG',
#     '菏泽': 'HEB',
#     '赣州': 'KOW',
#     '舟山': 'HSN',
#     '景德镇': 'JDZ',
#     '宿迁': 'SZV',
#     '襄阳': 'XFN',
#     '绵阳': 'MIG',
#     '九江': 'JIU',
#     '岳阳': 'YYA',
#     '阜阳': 'FUG',
#     '丹东': 'DDG',
#     '扬州': 'YTY',
#     '佳木斯': 'JMU',
#     '泸州': 'LZO',
#     '黄山': 'TXN',
#     '铜仁': 'TEN',
#     '宜宾': 'YBP',
#     '宜春': 'YIC',
#     '赤峰': 'CIF',
#     '锡林浩特': 'XIL',
#     '亳州': 'AQG',
#     '黔江': 'JIQ',
#     '黔东南': 'KJH',
#     '鸡西': 'JXA',
#     '塔城': 'TCG'
    }


def xiecheng2(dcity, acity, date):
    date = date[0:4] + '-' + date[4:6] + '-' + date[6:8]
    headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
            "Content-Type": "application/json"  # 声明文本类型为 json 格式
            # 'Cookie': 'your_cookie_here'  # Optional: Include if needed
        }

        # Assuming 'city' dictionary contains mappings of city names to their codes

    url = 'https://flights.ctrip.com/itinerary/api/12808/products'

    request_payload = {"flightWay": "Oneway",
                        "army": "false",
                        "classType": "ALL",
                        "hasChild": 'false',
                        "hasBaby": 'false',
                        "searchIndex": 1,
                        "portingToken": "3fec6a5a249a44faba1f245e61e2af88",
                        "airportParams": [
                            {"dcity": city.get(dcity), "acity": city.get(acity), "dcityname": dcity, "acityname": acity,
                                "date": date}]}

    response = requests.post(url, data=json.dumps(request_payload), headers=headers).text
    # print(json.loads(response))
    try:
        routeList = json.loads(response)["data"].get('routeList')
    except Exception as e:
        logging.error("An error occurred", exc_info=True)
        # print('route error' ,dcity, '-',acity )
        progress = 'no flight route on'+ dcity+ '-'+ acity
        return None, progress
    
    table2 = PrettyTable(["LowestPrice", "Airline", "FlightNumber", "Legs","PunctualityRate", "ArrivalDate", "DepartureDate"])
    
    progress = dcity + '------->'+ acity+date
    if routeList != None:
        for route in routeList:
            if len(route.get('legs')) !=0:
                info = {}
                legs = route.get('legs')[0]
                flight = legs.get('flight')
                info['LowestPrice'] = legs.get('characteristic').get('lowestPrice')
                info['Airline'] = flight.get('airlineName')
                info['FlightNumber'] = flight.get('flightNumber')
                
                
        ###############################################################################    
                leg_list = []
                total_price = 0 # This entire block is for flights with transit. So although total_price might seems confusing. It is used to add all the price from each leg together
                for leg in route.get('legs'):
                    each_flight = leg.get('flight')
                    leg_city = each_flight.get('arrivalAirportInfo').get('cityName')
                    leg_airport = each_flight.get('arrivalAirportInfo').get('airportName')
                    leg_list.append(leg_city+leg_airport)
                    
                    price0 = leg.get('cabins')[0].get('price').get('price')
                    total_price += price0
                    price0 = 0

                    if len(route.get('legs')) > 1:
                        info['LowestPrice'] = total_price
    ##################################################################################
                info['Legs'] = leg_list

                info['PunctualityRate'] = flight.get('punctualityRate')
                info['ArrivalDate'] = flight.get('arrivalDate')[-8:-3]
                info['DepartureDate'] = flight.get('departureDate')[-8:-3]

                table2.add_row(info.values())
    else:
        # print('no flight route on', dcity, '-',acity)
        progress = 'no flight route on'+ dcity+ '-'+ acity



    # print(table2)
    # filename = dcity+acity+date+".txt"
    # with open(filename, 'w', encoding='utf-8') as file:
    #     # Convert routeList to a pretty formatted string and write to the file
    #     pretty_route_list = json.dumps(routeList, indent=4, ensure_ascii=False)
    #     file.write(pretty_route_list)
    
    # Step 1: Extract the column headers
    headers = table2.field_names

    # Step 2: Extract the rows directly
    rows = [list(row) for row in table2._rows]

    # Step 3: Create DataFrame
    df = pd.DataFrame(rows, columns=headers)

    # display(df)
    return df, progress


def main():
    st.title("Flight Search Tool")

    # Input fields for the user
    dcity = st.text_input("请输入起点：", '深圳')
    acity = st.text_input("请输入终点：", '成都')
    date = st.text_input("请输入出行日期：", '20231210')

    # Initialize log messages variable
    log_messages = ""

    # Button to start the search
    if st.button("Search Flights"):
        if dcity not in city:
            st.error(f"起点城市 {dcity} 不在支持的城市列表中。")
            return  # Stop further execution

        if acity not in city:
            st.error(f"终点城市 {acity} 不在支持的城市列表中。")
            return  # Stop further execution
        
        log_box = st.empty()  # Define an empty placeholder
        all_city = list(city.keys())  # Assuming 'city' is defined in your script
        if dcity in all_city:
            all_city.remove(dcity)

        temp_df = None
        for index, _city in enumerate(all_city):
            # Call your function and capture its string output
            temp_dfx, function_output = xiecheng2(dcity, _city, date)

            # Append the output to the log messages
            log_messages += function_output + "\n"

            # Update the text area with log messages using a unique key
            log_box.text_area("Progress Logs", log_messages, height=300, key=f"log_{index}")

            if isinstance(temp_dfx, pd.DataFrame):
                if temp_df is None:
                    temp_df = temp_dfx
                else:
                    temp_df = pd.concat([temp_df, temp_dfx], axis=0, ignore_index=True)
            sleep_t = random.uniform(0.5, 1)
            time.sleep(sleep_t)  # Adjust as necessary

        filtered_df = temp_df[temp_df['Legs'].apply(lambda x: any(acity in leg for leg in x[:-1]))]
        filtered_df = filtered_df.sort_values(by='LowestPrice')

        filtered_df0 = temp_df[temp_df['Legs'].apply(lambda x: len(x) == 1 and acity in x[0])]
        filtered_df0 = filtered_df0.sort_values(by='LowestPrice')

        # ... rest of your logic ...
         # Convert 'LowestPrice' to numeric in filtered_df
        filtered_df['LowestPrice'] = pd.to_numeric(filtered_df['LowestPrice'], errors='coerce')

        # Find the row with the minimum 'LowestPrice' for each group in filtered_df
        filtered_df_min_price = filtered_df.loc[filtered_df.groupby(['Airline', 'FlightNumber', 'DepartureDate'])['LowestPrice'].idxmin()]

        # Rename the columns in filtered_df_min_price for clarity
        filtered_df_min_price_renamed = filtered_df_min_price.rename(columns={'LowestPrice': 'BetterPrice', 'Legs': 'BetterOption'})

        # Merging the dataframes on specified columns
        merged_df = pd.merge(filtered_df0, filtered_df_min_price_renamed, on=['Airline', 'FlightNumber', 'DepartureDate'], how='outer')

        merged_df['BetterPrice'] = merged_df.apply(
            lambda row: row['BetterPrice'] if row['BetterPrice'] is not None and row['LowestPrice'] is not None and row['BetterPrice'] < row['LowestPrice'] else None, 
            axis=1
        )

        merged_df['BetterOption'] = merged_df.apply(
            lambda row: row['BetterOption'] if row['BetterPrice'] is not None and row['LowestPrice'] is not None and row['BetterPrice'] < row['LowestPrice'] else None, 
            axis=1
        )
        # Keep only the required columns from the merged dataframe
        result_df = merged_df[['LowestPrice', 'Airline', 'FlightNumber', 'Legs', 'PunctualityRate_x', 'ArrivalDate_x', 'DepartureDate', 'BetterOption', 'BetterPrice']]

        # Optionally, rename these columns back to their original names
        result_df.drop(columns=['PunctualityRate_x'], inplace=True)
        result_df.rename(columns={'ArrivalDate_x': 'ArrivalDate'}, inplace=True)

        # Display the result dataframe
        st.write("Result:")
        # st.table(result_df)
        # st.dataframe(result_df)
        st.write(result_df)

if __name__ == "__main__":
    main()
