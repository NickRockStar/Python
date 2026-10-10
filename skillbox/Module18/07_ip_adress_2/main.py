ip = input('Введите IP: ').split('.')
for i_ip in ip:
    if not i_ip.isdigit():
        print('{0} — это не целое число.'.format(i_ip))
    elif not -1 < int(i_ip) < 256:
        (
            print('{0} превышает 255.'.format(i_ip)))
    if not len(ip) == 4:
        print('Адрес — это четыре числа, разделённые точками.')
    else:
        print('IP-адрес корректен.')
