from functools import reduce
import sys

# orderItemsFile = open("C://CCA175/data/retail_db/order_items/part-00000")
def getRevenue(path, orderid):
    orderItemsFile = open(path)
    orderItemsRead = orderItemsFile.read()
    orderItems = orderItemsRead.splitlines()
    orderItemsFilter = filter(lambda rec: int(rec.split(",")[1]) == orderid, orderItems)
    orderItemsMap = map(lambda rec: float(rec.split(",")[4]), orderItemsFilter)
    orderItemsRevenue = reduce(lambda total, element: total + element, orderItemsMap)
    orderItemsFile.close()
    return orderItemsRevenue

path = sys.argv[1]
orderid = int(sys.argv[2])
print(getRevenue(path, orderid))