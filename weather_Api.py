#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#  @Time   :2025/3/4 21:57
#  @Author :Zhd
#  @File   :weather_Api.py
import requests
def get_weather(city_name, api_key):
    # API 的 URL
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

    # 发送 GET 请求
    response = requests.get(url)

    # 检查请求是否成功
    if response.status_code == 200:
        # 解析 JSON 数据
        data = response.json()

        # 提取所需信息
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']

        # 打印天气信息
        print(f"Weather in {city_name}:")
        print(f"Description: {weather_description}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")


if __name__ == "__main__":
    # 替换为你自己的 API 密钥
    api_key = "ecc889bc7205eeff035e92c656d4a9c0"

    # 输入城市名称
    city_name = input("Enter city name: ")
    # 调用函数获取天气信息
    get_weather(city_name, api_key)