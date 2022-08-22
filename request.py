import os


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

    def clear_pending(self, schedule):
        for date in schedule.keys():
            if (date == self.date):
                # check the
                for time_slot in self.time_slots:
                    for pending_req in schedule[self.date]['pending'][:]:
                        for pending_req_t_slot in pending_req[1][:]:
                            print(
                                f'\nchecking {pending_req_t_slot} from {pending_req[0]} vs {time_slot}')
                            if (time_slot == pending_req_t_slot):
                                schedule[self.date]['pending'].remove(
                                    pending_req)
                                # the print statement below is the email func
                                print(
                                    f'removing {pending_req[0]}')
                                break
                            else:
                                print('no match, keep')

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
            # we want to compare the accepted_req time slots
            # with each of the time_slots for a request
            self.clear_pending(schedule)

    def __repr_(self):
        return self.user_info, self.date, self.time_slots


try:
    env_var = os.environ['TEST']
    print('ENV environment variable exists')
except KeyError:
    print('ENV environment variable does not exist')
