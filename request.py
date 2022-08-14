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
        schedule[self.date]['pending'].append(
            [self.user_info, self.time_slots])

    def accept_req(self, schedule):
        # flag keeps track of whether a req was accepted
        req_accepted = False

        # take the req time slots
        # bring to accepted + user info
        for date in schedule.keys():
            if (date == self.date):
                for time_slot in self.time_slots:
                    for availability in schedule[self.date]['available']:
                        if (time_slot == availability):
                            schedule[self.date]['accepted'].append(
                                [time_slot, self.user_info])
                            schedule[self.date]['available'].remove(
                                availability)
                            req_accepted = True
        if (req_accepted == True):
            # remove pending reqs with similar slots from schedule
            # all this to be re factored to seperate fn + add
            # notify method
            for date in schedule.keys():
                if (date == self.date):
                    for time_slot in self.time_slots:
                        for pending_req in schedule[self.date]['pending']:
                            for pending_req_t_slot in pending_req[1]:
                                print(
                                    f'\nchecking {pending_req[0]}')
                                if (time_slot == pending_req_t_slot):
                                    schedule[self.date]['pending'].remove(
                                        pending_req)
                                    print(
                                        f'removing {pending_req[0]}')
                                    break

            # notify user if their spot is canceled

        # notify user who's spot was accepted

    def __repr_(self):
        return self.user_info, self.date, self.time_slots


req2 = Requests(['alex', 'lek6ci@gmail.com'], '01-01-2022', ['12PM', '1PM'])
