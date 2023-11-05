import math


def accumulate(collection, operation):
    operation_collection = []
    for each_num in collection:
        operation_collection.append(operation(each_num))
    return operation_collection



