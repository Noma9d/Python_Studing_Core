from collections import Counter


def get_count_visits_from_ip(ips):
    return Counter(ips)




def get_frequent_visit_from_ip(ips):
    result = Counter(ips)
    return result.most_common(1)[0]