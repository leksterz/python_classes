import request as r

req1 = r.Requests(['alex', 'lek6ci@gmail.com'], '01-01-2022', ['12PM', '1PM'])
req2 = r.Requests(['kip', 'kip@gmail.com'], '01-01-2022', ['1PM'])

schedule = {
    '01-01-2022': {
        'available': ['12:00PM', '1:00PM', '2:00PM'],
        'accepted': [
            ['3:00PM', ['alex', 'lek6ci@gmail.com']],
            ['4:00PM', ['alex', 'lek6ci@gmail.com']]
        ],
        'pending': [
            req2
        ]
    }
}

req1.submit_req(schedule)

print(schedule['01-01-2022']['pending'][0].user_info)
print()
