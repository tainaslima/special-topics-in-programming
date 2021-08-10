import sys

def isPossibleToOrganizeCoaches(case):
    list_of_info = case.split("/")
    list_of_info.remove("")
    number_of_coaches = int(list_of_info[0])
    coaches_orders_to_check = list_of_info[1:]
    final_result = ""

    for orders in coaches_orders_to_check:
        arrive_order = [ str(x) for x in range(1,number_of_coaches+1) ]
        station = []
        exit_order = orders.split()
        result = "Yes"

        for coaches in exit_order:
            if(coaches in arrive_order):
                if(coaches == arrive_order[0]):
                    arrive_order.pop(0)
                else:
                    coaches_pos_arrive_order = arrive_order.index(coaches)
                    station.extend(arrive_order[:coaches_pos_arrive_order+1])
                    arrive_order = arrive_order[coaches_pos_arrive_order+1:]
                    station.pop()
            elif(coaches == station[len(station)-1]):
                station.pop()
            else:
                result = "No"
        
        final_result += result + "\n"

    return final_result
    

if __name__ == "__main__":
    cases = []
    case = ""
    zero = False
    for line in sys.stdin:
        if(line.strip() == "0"):
            if(not zero):
                zero = True
                cases.append(case)
                case = ""
            else:
                break
        else:
            case += (line.strip() + "/")
            zero = False
    
    result = ""
    for case in cases:
        result += isPossibleToOrganizeCoaches(case) + "\n"

    print(result.rstrip()+"\n")