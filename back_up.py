import random
from datetime import datetime, date
import calendar
import csv


class NationLottery:            # Abstract class

    # Function to populate entry ticket
    def populate_draw_ticket(self):

        x = 0
        y = 6
        entry_ticket = []  # List to store 6 draw numbers from the user

        while x < 6:

            user_number = input("Please enter " + str(y) + " numbers into your National Lottery Entry Ticket: ")

            if str(user_number) == '':
                print(
                    'The Entry Ticket should have 6 number, please you are not allowed to skip to enter a number. Thanks!')
                user_number = input("Please enter " + str(y) + " numbers into your National Lottery Entry Ticket: ")

            else:
                pass

            entry_ticket.append(user_number)
            x += 1
            y -= 1

        return entry_ticket

    # Function to generate 7 winning numbers including bonus number which is the last number
    def generate_winning_numbers(self):

        nums = []  # List containing the 7 winning numbers including bonus
        y = 0

        while y < 7:

            for x in range(7):
                lottery_number = random.randint(1, 49)
            nums.append(lottery_number)
            y += 1
        return nums

    # Function to get a winning number by comparing the entered tickets to the winning numbers.
    def getting_winning_numbers(self):

        count = 0
        my_date = date.today()
        tdays_day = calendar.day_name[my_date.weekday()]
        european_countries = ['Belgium', 'Bulgaria', 'Croatia', 'Austria', 'Cyprus', 'Czech Republic', 'Denmark',
                              'Finland', 'Netherlands', 'Poland', 'Switzerland', 'Russia', 'Germany', 'Turkey',
                              'France', 'Italy', 'United Kingdom', 'Greece', 'Portugal', 'Macedonia', 'Latvia',
                              'Monaco', 'San Marino', 'Liechtenstein', 'Andorra', 'Isle of Man', 'Jersey', 'Malta',
                              'Iceland', 'Estonia']
        week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        all_national_lottery = 0

        # National lotteries run once a week, so I choose to run it every wednsday
        if tdays_day == week[2]:

            winning_numbers = self.generate_winning_numbers  # A list of 6 winning numbers and 1 bonus, calling generate_winning_numbers()

            # There are currently 30 independent national lotterie
            while all_national_lottery < 30:

                country = (european_countries[all_national_lottery]).lower()
                draw_date = date.today()
                draw_number = 2589
                entry_ticket_file = country + '_' + str(draw_date) + '_' + str(draw_number)
                draw_numbers = self.populate_draw_ticket()

                # Comparing the entered tickets to the winning numbers.
                for d_nums in draw_numbers:
                    for w_nums in winning_numbers:
                        if int(d_nums) == int(w_nums):
                            print(str(d_nums))
                            count += 1  # Count matched numbers (Main ball set) n (Any additional ball sets)
                        else:
                            pass

                # If a Ticket has matched all numbers, indicate that the jackpot was won
                if count == 6:
                    print(country + " has won the Jackpot, yeeeeee!")
                if count >= 1:  # Indicate number of winning numbers the player won
                    print(country + " won " + str(count) + " number(s)")
                else:
                    print(country + " did not win any number, we are sorry you should try again")
                print(" ")

                # Uploading entry tickets into CSV file
                with open(entry_ticket_file + '.csv', 'w') as csvFile:
                    writer = csv.writer(csvFile)
                    writer.writerows(str(draw_numbers))

                csvFile.close()

                # Upload winning numbers into CSV file
                with open(entry_ticket_file + '.csv', 'w') as csvFile:
                    writer = csv.writer(csvFile)
                    writer.writerows(str(winning_numbers))

                csvFile.close()

                # Increment my While Loop
                all_national_lottery += 1

    def run(self):
        self.getting_winning_numbers()


#a = NationLottery()
#a.getting_winning_numbers()

if __name__ == '__main__':
    NationLottery().run()



















