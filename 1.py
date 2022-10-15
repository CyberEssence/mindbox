
def get_client_group(customer_id):
    return sum(int(x) for x in str(customer_id))


def group_count(n_customers, n_first_id=0):
    if n_customers <= 0 or n_first_id < 0:
        return False
    group_dict = {}
    for customer_id in range(n_first_id, n_first_id + n_customers):
        group_n = get_client_group(customer_id)
        if str(group_n) in group_dict:
            group_dict[f'{get_client_group(customer_id)}'] += 1
        else:
            group_dict[f'{get_client_group(customer_id)}'] = 1
    return {key: value for key, value in sorted(group_dict.items(), key=lambda item: item[1], reverse=True)}


if __name__ == '__main__':
    print(group_count(100))
    print(group_count(100, 100))