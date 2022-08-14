import request as r

req1 = r.Requests(['alex', 'lek6ci@gmail.com'],
                  '01-01-2022', ['12:00PM', '1:00PM'])
req2 = r.Requests(['kip', 'kip@gmail.com'], '01-02-2022', ['1:00PM'])
req3 = r.Requests(['jackie', 'peace@gmail.com'],
                  '01-01-2022', ['2:00PM'])
req4 = r.Requests(['blaze', 'luckky@gmail.com'],
                  '01-01-2022', ['1:00PM'])
req5 = r.Requests(['steve', 'doner@gmail.com'],
                  '01-01-2022', ['1:00PM'])
req7 = r.Requests(['bill', 'candy@gmail.com'],
                  '01-01-2022', ['1:00PM'])
req6 = r.Requests(['downer', 'downer@gmail.com'],
                  '01-01-2022', ['12:00PM'])

schedule = {
    '01-01-2022': {
        'available': ['12:00PM', '1:00PM', '2:00PM'],
        'accepted': [
            ['3:00PM', ['alex', 'lekci@gmail.com']],
            ['4:00PM', ['alex', 'lekci@gmail.com']]
        ],
        'pending': [
        ]
    },
    '01-02-2022': {
        'available': ['1:00PM', '2:00PM'],
        'accepted': [

        ],
        'pending': [

        ]
    }
}
print(f'\n THE SCHEDULE \n{schedule["01-01-2022"]}')

req1.submit_req(schedule)
req3.submit_req(schedule)
req4.submit_req(schedule)
req5.submit_req(schedule)
req6.submit_req(schedule)
req7.submit_req(schedule)

print(f'\n THE SCHEDULE AFTER SUBMIT \n{schedule["01-01-2022"]}')


req1.accept_req(schedule)

print(f'\n THE SCHEDULE AFTER ACCEPT \n{schedule["01-01-2022"]}')
