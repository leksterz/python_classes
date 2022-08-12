import request as r

req1 = r.Requests(['alex', 'lek6ci@gmail.com'], '01-01-2022', ['12PM', '1PM'])
req2 = r.Requests(['kip', 'kip@gmail.com'], '01-02-2022', ['1PM'])

schedule = {
    '01-01-2022': {
        'available': ['12:00PM', '1:00PM', '2:00PM'],
        'accepted': [
            ['3:00PM', ['alex', 'lekci@gmail.com']],
            ['4:00PM', ['alex', 'lekci@gmail.com']]
        ],
        'pending': [
            req2, req2
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

print(schedule)
req2.accept_req(schedule)
print(schedule)
