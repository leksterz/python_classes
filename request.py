class Requests:
    """The request class manages the submition of requests via
    the initializition. It keeps track of pending requests, status = open.

    The methods in this class deals with accepting a request, which 
    iniatiates the cancelition of requests that shared the time slot.

    The other major method deals with informing the users affect by acepting
    a request. The notify method sends an email if your req was accepted/declined"""

    def __init__(self, user_info,  date, time_slots):
        self.user_info = user_info
        self.date = date
        self.time_slots = time_slots

    @classmethod
    def get_all_reqs(cls, date, schedule):
        for req in schedule[date]['pending']:
            print(req)

    def submit_req(self, schedule):
        schedule[self.date]['pending'].append(self)

    def accept_req(self, schedule):
        # take the req time slots
        # bring to accepted + user info

        for date in schedule.keys():
            if (date == self.date):
                # for time_slot in schedule[self.date]['available']:
                for time_slot in self.time_slots:
                    schedule[self.date]['accepted'].append(
                        [time_slot, self.user_info])

    def __repr_(self):
        return self.user_info, self.date, self.time_slots


req2 = Requests(['alex', 'lek6ci@gmail.com'], '01-01-2022', ['12PM', '1PM'])
