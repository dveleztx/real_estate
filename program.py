import csv
import os

try:
    import statistics
except:
    # error code instead
    import statistics_standin_for_py2 as statistics

from data_types import Purchase


def main():
    print_header()
    filename = get_data_file()
    data = load_file(filename)
    query_data(data)


def print_header():
    print("-------------------------------")
    print("  REAL ESTATE DATA MINING APP")
    print("-------------------------------")
    print()


def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, "data",
                        "SacramentoRealEstateTransactions2008.csv")


def load_file(filename):
    with open(filename, "r") as fin:
        reader = csv.DictReader(fin)
        purchases = []
        for row in reader:
            p = Purchase.create_from_dict(row)
            purchases.append(p)

        return purchases

        # header = fin.readline().strip()
        # reader = csv.reader(fin, delimiter=",")
        # for row in reader:
        #     print(row)
        #     beds = row[4]


# def load_file_basic(filename):
#     with open(filename, "r", encoding="utf-8") as fin:
# header = fin.readline().strip()
# print("found header: " + header)
#
# lines = []
# for line in fin:
#     line_data = line.strip().split(",")
#     bed_count = line_data[4]
#     lines.append(line_data)
#
# # slice 0 to 5
# print(lines[:5])

# def get_price(p):
# return p.price

def query_data(data):  # list[Purchase]):

    # if data was sorted by price:
    data.sort(key=lambda p: p.price)

    # most expensive house?
    high_purchase = data[-1]
    print("The most expensive house is ${:,.2f} with {} beds and {} baths".format(
        high_purchase.price, high_purchase.beds, high_purchase.baths))

    # least expensive house?
    low_purchase = data[0]
    print("The least expensive house is ${:,.2f} with {} beds and {} baths".format(
        low_purchase.price, low_purchase.beds, low_purchase.baths))

    # average price house?
    # prices = []
    # for pur in data:
    #     prices.append(pur.price)

    prices = [
        p.price  # projection or items
        for p in data  # the set to process
    ]

    ave_price = statistics.mean(prices)
    print("The average home price is ${:,.2f}".format(ave_price))

    # average price of 2 bedroom houses
    # prices = []
    # for pur in data:
    #     if pur.beds == 2:
    #         prices.append(pur.price)

    # Concept: List Comprehension
    two_bed_homes = [
        p  # projection or items
        for p in data  # the set to process
        if p.beds == 2  # test / condition
    ]

    ave_price = statistics.mean([p.price for p in two_bed_homes])
    ave_baths = statistics.mean([p.baths for p in two_bed_homes])
    ave_sqft = statistics.mean([p.sq__ft for p in two_bed_homes])
    print("The average price of a 2-bedroom home is ${:,.2f}, baths={}, sq ft={:,}"
          .format((ave_price), round(ave_baths, 1), round(ave_sqft, 1)))


if __name__ == '__main__':
    main()