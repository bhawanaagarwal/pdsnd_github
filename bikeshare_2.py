import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
CITIES = ['chicago', 'new york city', 'washington']
MONTHS = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul']
DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
FILTER_CHOICES = ['Month', 'Both', 'None', 'Day']

def get_choice(options, prompt, error_msg = "Incorrect choice! Please try again!"):
    '''
    Input:
    options - can be city, month, day or filter choice
    prompt - user prompt to ask user to make choices
    error_msg - if the chosen value is not present


    Returns the choice of the user for the given option

    '''

    while True:
        try:
            choice = input(prompt).strip()
            if choice.isdigit() and 1 <= int(choice) <= len(options):
                return options[int(choice)-1]
            if choice.capitalize() in options:
                return choice.capitalize()
            print(error_msg)

        except Exception as e:
            print(error_msg)

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    city = get_choice(CITIES, "\nWhich city report would you like to see?\n1. Chicago   2. New York City    3. Washington\nEnter number: ")
    filter_choice = get_choice(FILTER_CHOICES, "\nWould you like to filter the report based on month, day, both, or none?\n")

    if filter_choice == 'None':
        return city, 'all', 'all'
    month = get_choice(MONTHS, "\nWhich month? Choose number 1 to 6 (e.g. 1 = Jan, 6 = Jun): ") if filter_choice in ['Month', 'Both'] else 'all'
    day = get_choice(DAYS, "\nWhich day? Choose number 1 to 7 (e.g. 1 = Sun, 7 = Sat): ") if filter_choice in ['Day', 'Both'] else 'all'


    # get user input for month (all, january, february, ... , june)


    # get user input for day of week (all, monday, tuesday, ... sunday)

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':   
        month = MONTHS.index(month) + 1

        df = df[df['month'] == month]
    
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print(f"Most common month of Travel: {common_month}")
    print(f"Count: {df['month'].value_counts()[common_month]}\n")

    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print(f"Most common day of Travel: {common_day}")
    print(f"Count: {df['day_of_week'].value_counts()[common_day]}\n")

    # display the most common start hour
    hours = df['Start Time'].dt.hour
    common_hour = hours.mode()[0]
    print(f"Most common hour of Travel: {common_hour}")
    print(f"Count: {hours.value_counts()[common_hour]}\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_st = df['Start Station'].mode()[0]
    print(f"Most common Start Station: {common_start_st}")
    print(f"Count: {df['Start Station'].value_counts()[common_start_st]}\n")
    


    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print(f"Most common End Station: {common_end_station}")
    print(f"Count: {df['End Station'].value_counts()[common_end_station]}\n")


    # display most frequent combination of start station and end station trip
    combination = pd.concat([df['Start Station'], df['End Station']])
    comb_mode = combination.mode()[0]
    
    print(f"Most common combination of Start and End Station: {comb_mode}")
    print(f"Count: {combination.value_counts()[comb_mode]}\n")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print(f"Total time to travel: {df['Trip Duration'].sum()}\n")


    # display mean travel time
    print(f"Average time to travel: {df['Trip Duration'].mean()}\n")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print(f"Total number of users based on types: \n{df['User Type'].value_counts()}\n")


    # Display counts of gender
    if "Gender" in df.columns:
        print(f"Total number of users based on types: \n{df['Gender'].value_counts()}\n")
    else:
        print("There is no gender data")



    # Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:
        print(f"Earliest birth year: {df['Birth Year'].min()}\n")
        print(f"Most recent birth year: {df['Birth Year'].max()}\n")
        print(f"Most common birth year: {df['Birth Year'].mode()[0]}\n")
    else:
        print("There is no Birth year data")



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        print(city, month, day)
        df = load_data(city, month, day)

        """
        - Filling Nan values in column Gender and Birth year as other columns doesn't have Nan values. 
        - Because dropping those values will leave us with only one User Type (but it will also lead to biased data when it comes to Gender and Bith year)
        - We can always go with other types of data imputation here ()
        - As Washington.csv doesnt have columns Gender and Birth Year, we need to put the check
        """

        if "Gender" in df.columns:
            df['Gender'] = df['Gender'].fillna(df['Gender'].mode()[0])
        if "Birth Year" in df.columns:
            df['Birth Year'] = df['Birth Year'].fillna(df['Birth Year'].median()).astype('int64')

        print(df.head(10))

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
