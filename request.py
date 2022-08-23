import os
import smtplib


# with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.ehlo()

#     smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

#     subject = "Testing email python"
#     body = "Wow man amazin!!!"

#     message = f'Subject: {subject}\n\n{body}'
#     smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, message)


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
        # send email to users who's request was denied
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

            subject = "[DECLINED] Your Explode Studio Session was Declined"
            accepted_time_slots = self.time_slots
            body = (
                f'Hey there! Your request for {self.date} was not accepted.\nThis can happen for a number of reasons, so no sweat. Try to find another time.\nHere are the time slots you requested: {accepted_time_slots}. Check back to see if we have other availability')
            for date in schedule.keys():
                if (date == self.date):
                    # check the
                    for time_slot in self.time_slots:
                        for pending_req in schedule[self.date]['pending'][:]:
                            for pending_req_t_slot in pending_req[1][:]:
                                # DEBUG
                                # print(
                                #     f'\nchecking {pending_req_t_slot} from {pending_req[0]} vs {time_slot}')
                                if (time_slot == pending_req_t_slot):
                                    schedule[self.date]['pending'].remove(
                                        pending_req)
                                    # smtp.sendmail(SENDER, RECEIVER- this is user, msg)
                                    # smtp.sendmail(
                                    #     EMAIL_ADDRESS, EMAIL_ADDRESS, message)
                                    break
                                else:
                                    print('no match, keep')

    def accept_req(self, schedule):
        # send accepted email to user
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

            subject = "[ACCEPTED] Your Explode Studio Session is Booked"
            accepted_time_slots = self.time_slots
            body = (
                f'Great news! Your request for {self.date} has been accepted.\nHere are the time slots you requested: {accepted_time_slots}. We look forward to having you in the studio!')

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

                                # sends accepted email to user
                                message = f'Subject: {subject}\n\nHey {self.user_info[0]},\n{body}'
            if (req_accepted == True):
                # we want to compare the accepted_req time slots
                # with each of the time_slots for a request
                smtp.sendmail(
                    EMAIL_ADDRESS, EMAIL_ADDRESS, message)
                self.clear_pending(schedule)

    def __repr_(self):
        return self.user_info, self.date, self.time_slots
