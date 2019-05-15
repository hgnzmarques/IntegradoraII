import requests
import numpy as np
from matplotlib import pyplot as plt
from superjson import json


def plot_bar_x(label, success_rate, title, xlabel, ylabel):
    index = np.arange(len(label))
    plt.bar(index, success_rate)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.xticks(index, label, fontsize=12, rotation=30)
    plt.title(title)
    plt.show()


# def plot_bar_y(label, success_rate, title, xlabel, ylabel):
#     index = np.arange(len(success_rate))
#     plt.barh(index, success_rate)
#     plt.xlabel(xlabel, fontsize=12)
#     plt.ylabel(ylabel, fontsize=12)
#     plt.xticks(label, success_rate, fontsize=12, rotation=30)
#     plt.title(title)
#     plt.show()


def pie_chart(labels=None, size=None):
    labels = ['Facebook', 'WhatsApp', 'Twitter']
    sizes = [50, 40, 10]
    explode = (0, 0, 0)
    fig1, ax1 = plt.subplots()
    ax1.pie(
        sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90, colors=['blue', 'green', 'cyan']
    )
    plt.title('Where your referrals come from.')
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()


def payment_methods_success_rate():
    url = 'http://localhost:8999/vakinha-creation/payment-methods-success-rate/' 
    response = requests.get(url).content
    data = json.loads(response)
    title = 'Success rate of different payment methods.'
    xlabel = 'Payment Method'
    ylabel = 'Success Rate %'
    plot_bar_x(data[0], data[1], title, xlabel, ylabel)


def contributions_per_value():
    url = 'http://localhost:8999/vakinha-creation/contributions_per_value/' 
    response = requests.get(url).content
    data = json.loads(response)
    title = 'Contributions grouped by the amount donated.'
    xlabel = 'Amount in BRL'
    ylabel = 'Number of donations'
    plot_bar_x(data[0], data[1], title, xlabel, ylabel)


def views_per_day():
    title = 'Number of viewers per day over the last week.'
    xlabel = 'Unique viewers'
    ylabel = 'x days ago'
    days = ['today', 'yesterday', '2 days ago', '3 days ago', '4 days ago', '5 days ago', '6 days ago']
    views = [4, 10, 8, 11, 9, 10, 8]
    plot_bar_x(days, views, title, xlabel, ylabel)


contributions_per_value
if __name__ == "__main__":
    payment_methods_success_rate()
    contributions_per_value()
    pie_chart()
    views_per_day()